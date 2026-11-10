"""
Validate TPDB asset manifests and their images.

    python validate_assets.py library/ --schema asset_manifest.schema.json --palette palette.json

Exit code 0 if every asset passes all hard checks. Soft checks print warnings.
Writes validation_report.json into the library folder.
"""
import argparse
import glob
import hashlib
import json
import os
import sys

import numpy as np
from jsonschema import Draft202012Validator
from PIL import Image

HEIGHT_RANGES = {  # meters
    ("person", "child"): (0.75, 1.55), ("person", "teen"): (1.35, 1.85), ("person", "adult"): (1.5, 2.0), ("person", "older_adult"): (1.4, 1.95),
    ("animal", None): (0.05, 2.5), ("prop", None): (0.02, 3.0), ("plant", None): (0.05, 8.0), ("structure", None): (0.3, 12.0),
}
GROUND_TOL_PX = 6
CONTACT_TOL_FRAC = 0.03
PALETTE_TOL = 10          # max RGB distance to count as on-palette
PALETTE_MIN_SHARE = 0.90
SOFT_PER_EDGE_MAX = 4.5   # semi-transparent pixels per outline pixel (this pipeline runs ~3.6)
FRONTAL_GAZE_COS = 0.7
SUPPORTED_POSES = {"sit_swing", "seesaw_stuck_call"}  # held off the ground by scenery (the swing seat; the raised end of a seesaw, the legs hanging)    # gaze within ~45 deg of the camera = looking at the viewer


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def hex_rgb(h):
    return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)], dtype=float)


def _to_lin(c):
    c = c / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def _to_srgb(c):
    c = np.where(c <= 0.0031308, c * 12.92, 1.055 * np.power(c, 1 / 2.4) - 0.055)
    return np.clip(c * 255.0, 0, 255)


def palette_targets(pal):
    """Lit tones are the palette itself; shadow tones are base x factor in linear light."""
    base = [hex_rgb(c) for c in pal["colors"].values()]
    f = pal.get("shadow_factor", 0.72)
    hi = pal.get("highlight_factor")
    tones = base + [_to_srgb(_to_lin(b) * f) for b in base]
    if hi:
        tones += [_to_srgb(np.minimum(_to_lin(b) * hi, 1.0)) for b in base]
    return np.array(tones)


_PAL, _CEL_TARGETS = {}, {}


def cel_targets(cel):
    """v0.46: a cast that sets its own cel tones (render.cel in the record) is measured against those tones, not the palette file's."""
    key = (cel["shadow"], cel["light"])
    if key not in _CEL_TARGETS:
        _CEL_TARGETS[key] = palette_targets(dict(_PAL, shadow_factor=cel["shadow"], highlight_factor=cel["light"] if cel["light"] != 1.0 else None))
    return _CEL_TARGETS[key]


def check(path, schema, targets):
    hard, soft, info = [], [], {}
    folder = os.path.dirname(path)
    m = json.load(open(path))

    errs = sorted(Draft202012Validator(schema).iter_errors(m), key=lambda e: list(e.path))
    for e in errs:
        hard.append(f"schema: {'/'.join(map(str, e.path)) or '(root)'}: {e.message[:160]}")
    if errs:
        return m.get("variant_id", os.path.basename(path)), hard, soft, info

    v = m["variant"]
    expect = f'{m["family_id"]}__{v["pose"]}__{v["expression"]}__y{v["yaw_deg"]:03d}'
    if m["variant_id"] != expect:
        hard.append(f"variant_id should be {expect}")
    if not m["family_id"].startswith(m["class"] + "."):
        hard.append("family_id prefix does not match class")

    imgs = {}
    for key, fd in m["files"].items():
        fp = os.path.join(folder, fd["path"])
        if not os.path.exists(fp):
            hard.append(f"missing file {fd['path']}")
            continue
        if sha256(fp) != fd["sha256"]:
            hard.append(f"{key}: sha256 mismatch")
        im = Image.open(fp)
        if im.size != (fd["width"], fd["height"]):
            hard.append(f"{key}: size {im.size} != manifest {(fd['width'], fd['height'])}")
        imgs[key] = im
    if hard:
        return m["variant_id"], hard, soft, info

    rgba = np.asarray(imgs["image"].convert("RGBA")).astype(float)
    alpha = rgba[..., 3]
    mask = np.asarray(imgs["mask"].convert("L")) > 127
    H, W = alpha.shape

    if not np.array_equal(mask, alpha >= 127.5):
        diff = np.mean(mask != (alpha >= 127.5))
        (hard if diff > 0.002 else soft).append(f"mask differs from image alpha on {diff:.3%} of pixels")

    ys, xs = np.nonzero(mask)
    bbox = [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]
    if max(abs(a - b) for a, b in zip(bbox, m["geometry"]["bbox_px"])) > 1:
        hard.append(f"bbox {m['geometry']['bbox_px']} != measured {bbox}")

    gx, gy = m["geometry"]["ground_point_px"]
    # With the camera tilted down, the near edge of the footprint (toes, front paws)
    # projects below the ground point. Allow for half the footprint plus the outline.
    r = m["render"]
    fp = m["geometry"]["footprint_m"]
    # full extent, not half: a seated figure's feet reach well forward of its origin
    extent = max(fp["width"], fp["depth"])
    if v.get("props"):
        extent += 0.55          # a held tool can rest on the ground ahead of the feet (broom, rake, shovel)
    reach = extent * np.sin(np.radians(r["camera"]["tilt_deg"])) * r["pixels_per_meter"]
    below = bbox[3] - gy
    # (from v0.46 the figure's outer edge may be drawn wider than the lines inside it)
    max_below = reach + max(r["outline"]["width_px"], r["outline"].get("silhouette_px") or 0) / 2 + GROUND_TOL_PX
    info["ground_offset_px"] = round(float(below), 1)
    # a figure drawn in two pieces (render_assets.py, from v0.31): each piece is checked by its base pose, and the piece without
    # the body (the far leg, or the legs) shares its twin's origin, so the twin carries the ground rule
    base, _, piece = v.get("pose", "").partition("~")
    if v.get("airborne") or base in SUPPORTED_POSES or piece in ("far", "legs"):
        pass                      # jumping / flying / on a swing: the ground point is where the shadow goes
    elif below < -GROUND_TOL_PX or below > max_below:
        hard.append(f"lowest opaque row is {below:+.1f}px from the ground point (allowed {-GROUND_TOL_PX} to {max_below:.1f})")
    if not (bbox[0] <= gx <= bbox[2]) and piece not in ("far", "legs"):
        hard.append("ground point x outside the opaque bbox")

    for name, a in m["anchors"].items():
        x, y = a["px"]
        # gaze targets and *_aim anchors are direction helpers and may lie outside the image
        if name != "gaze_target" and not name.endswith("_aim") and not (0 <= x <= W and 0 <= y <= H):
            hard.append(f"anchor {name} outside the image")
        if a["kind"] == "contact" and name != "seat" and abs(y - gy) > CONTACT_TOL_FRAC * H:
            soft.append(f"contact anchor {name} is {y - gy:+.0f}px from the ground line")

    cls = m["class"]
    age = m["labels"].get("person", {}).get("age_group") if cls == "person" else None
    lo, hi = HEIGHT_RANGES.get((cls, age), (0, 99))
    hm = m["geometry"]["height_m"]
    if v["pose"] in ("stand", "rest", "perch"):
        if not (lo <= hm <= hi):
            hard.append(f"standing height {hm} m outside {lo}-{hi} m for {cls} {age or ''}".strip())
    elif hm > hi * 1.35:
        soft.append(f"height {hm} m in pose '{v['pose']}' is unusually tall for {cls}")

    ppm = m["render"]["pixels_per_meter"]
    px_height = bbox[3] - bbox[1]
    implied = px_height / ppm
    if abs(implied - m["geometry"]["height_m"]) > 0.08 + 0.12 * m["geometry"]["height_m"]:
        soft.append(f"opaque height {implied:.2f} m vs model height {m['geometry']['height_m']:.2f} m")

    solid = alpha == 255
    soft_px = np.sum((alpha > 0) & (alpha < 255))
    # measure soft pixels against the silhouette's outline length, not its area,
    # so thin shapes are not penalized; about 2-3 px of anti-aliasing is normal
    inside = alpha >= 128
    edge = inside & ~(np.roll(inside, 1, 0) & np.roll(inside, -1, 0) & np.roll(inside, 1, 1) & np.roll(inside, -1, 1))
    ratio = soft_px / max(1, edge.sum())
    info["soft_px_per_edge_px"] = round(float(ratio), 2)
    if ratio > SOFT_PER_EDGE_MAX:
        soft.append(f"soft edge band {ratio:.1f} px wide on average (limit {SOFT_PER_EDGE_MAX})")

    if m.get("render", {}).get("cel") and _PAL:
        targets = cel_targets(m["render"]["cel"])
    px = rgba[solid][:, :3]
    if len(px) > 50000:
        px = px[np.random.default_rng(0).choice(len(px), 50000, replace=False)]
    d = np.min(np.linalg.norm(px[:, None, :] - targets[None, :, :], axis=2), axis=1)
    share = float(np.mean(d <= PALETTE_TOL))
    info["on_palette_share"] = round(share, 4)
    if share < PALETTE_MIN_SHARE:
        soft.append(f"only {share:.1%} of opaque pixels are on-palette (target {PALETTE_MIN_SHARE:.0%})")

    if cls == "person":
        A = m["anchors"]
        # gaze_target sits 1 m in front of the eyes, so its change in depth is the
        # cosine between the gaze and the viewing direction (negative = toward camera).
        toward = -(A["gaze_target"]["depth_m"] - (A["eye_L"]["depth_m"] + A["eye_R"]["depth_m"]) / 2)
        el, er, gt = (np.array(A[k]["px"]) for k in ("eye_L", "eye_R", "gaze_target"))
        g = gt - (el + er) / 2
        if toward > FRONTAL_GAZE_COS:
            info["gaze"] = "at viewer"
        else:
            info["gaze"] = f"{float(np.degrees(np.arctan2(-g[1], g[0]))):.0f} deg"

    return m["variant_id"], hard, soft, info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("library")
    ap.add_argument("--schema", default="asset_manifest.schema.json")
    ap.add_argument("--palette", default="palette.json")
    a = ap.parse_args()
    schema = json.load(open(a.schema))
    _PAL.update(json.load(open(a.palette)))
    targets = palette_targets(_PAL)
    report, failed = [], 0
    for p in sorted(glob.glob(os.path.join(a.library, "*.json"))):
        if p.endswith("validation_report.json"):
            continue
        vid, hard, soft, info = check(p, schema, targets)
        failed += bool(hard)
        report.append({"variant_id": vid, "pass": not hard, "errors": hard, "warnings": soft, **info})
        flag = "PASS" if not hard else "FAIL"
        extra = " ".join(f"{k}={v}" for k, v in info.items())
        print(f"{flag}  {vid}  {extra}")
        for e in hard:
            print("      error:", e)
        for w in soft:
            print("      warn: ", w)
    json.dump(report, open(os.path.join(a.library, "validation_report.json"), "w"), indent=1)
    print(f"\n{len(report) - failed}/{len(report)} assets passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
