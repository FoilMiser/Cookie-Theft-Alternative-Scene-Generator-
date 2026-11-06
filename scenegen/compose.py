"""Compose a scene to SVG/PNG and measure it: masks, visible areas, occlusion, AOI cells, clutter."""
import io

from . import cairo_compat  # noqa: F401  (before cairosvg)
import cairosvg
import numpy as np
from PIL import Image

from . import draw as D

MASK_SCALE = 0.5   # masks at half resolution; areas are scaled back to full-resolution pixels
BACKGROUND_ROLES = ("background",)


def svg_doc(body, title="", w=D.W, h=D.H, mirror=False):
    if mirror:
        body = f'<g transform="matrix(-1 0 0 1 {w} 0)">{body}</g>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<title>{title}</title>{body}</svg>')


def elements_of(sc):
    """Every drawn element with its z, role and svg markup, in drawing order."""
    els = []
    for e in sc.S.elements:
        els.append(dict(e))
    for e in sc.svgs.values():
        els.append(dict(e))
    for eid, p in sc.assets.items():
        els.append({"id": eid, "label": p.v, "svg": None, "z": p.z, "role": p.role, "bbox": p.bbox(), "kind": "asset", "asset": p})
    for i, e in enumerate(els):
        e["_order"] = i
    els.sort(key=lambda e: (e["z"], e["_order"]))
    return els


def markup(e, shadow=True):
    if e["kind"] == "asset":
        if "_svg" not in e:
            e["_svg"] = e["asset"].svg(shadow=shadow)
        return f'<g id="{e["id"]}" data-role="{e["role"]}" data-asset="{e["asset"].v}">{e["_svg"]}</g>'
    return f'<g id="{e["id"]}" data-role="{e["role"]}">{e["svg"]}</g>'


def render_png(svg, width=D.W):
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=width)
    return Image.open(io.BytesIO(png))


def asset_mask(p, mirror):
    """Coverage of a rendered asset, pasted straight from its alpha channel (no SVG round trip)."""
    if getattr(p, "rot", None):
        # v0.35: a turned figure (the child on a swung seat) is drawn through the SVG, as it appears
        im = render_png(svg_doc(p.svg(shadow=False), mirror=mirror), int(D.W * MASK_SCALE)).convert("RGBA")
        return np.array(im)[:, :, 3] > 96
    W2, H2 = int(D.W * MASK_SCALE), int(D.H * MASK_SCALE)
    im = p.lib.image(p.v)
    w, h = im.size
    k = p.k * MASK_SCALE
    a = im.getchannel("A").resize((max(1, round(w * k)), max(1, round(h * k))), Image.BILINEAR)
    if p.mirror:
        a = a.transpose(Image.FLIP_LEFT_RIGHT)
        x0 = (p.X - p.k * (w - p.gx)) * MASK_SCALE
    else:
        x0 = (p.X - p.k * p.gx) * MASK_SCALE
    y0 = (p.Y - p.k * p.gy) * MASK_SCALE
    arr = np.asarray(a) > 96
    out = np.zeros((H2, W2), dtype=bool)
    xi, yi = int(round(x0)), int(round(y0))
    sx0, sy0 = max(0, -xi), max(0, -yi)
    dx0, dy0 = max(0, xi), max(0, yi)
    wv = min(arr.shape[1] - sx0, W2 - dx0)
    hv = min(arr.shape[0] - sy0, H2 - dy0)
    if wv > 0 and hv > 0:
        out[dy0:dy0 + hv, dx0:dx0 + wv] = arr[sy0:sy0 + hv, sx0:sx0 + wv]
    return out[:, ::-1] if mirror else out


def alpha_mask(e, mirror):
    """Coverage mask of one element (without its ground shadow)."""
    if e["kind"] == "asset":
        return asset_mask(e["asset"], mirror)
    im = render_png(svg_doc(e["svg"], mirror=mirror), int(D.W * MASK_SCALE)).convert("RGBA")
    return np.array(im)[:, :, 3] > 96


def measure(sc, els, mirror):
    """Visible masks for every non-background element; returns dict id -> stats."""
    masks = {}
    order = [e for e in els if e["role"] not in BACKGROUND_ROLES]
    for e in order:
        masks[e["id"]] = alpha_mask(e, mirror)
    cover = np.zeros_like(next(iter(masks.values()))) if masks else None
    stats = {}
    for e in reversed(order):
        m = masks[e["id"]]
        full = int(m.sum())
        vis_m = m & ~cover
        vis = int(vis_m.sum())
        cover |= m
        k = 1.0 / (MASK_SCALE * MASK_SCALE)
        ys, xs = np.nonzero(vis_m) if vis else (np.array([0]), np.array([0]))
        stats[e["id"]] = {"area": full * k, "visible": vis * k, "occlusion": (1 - vis / full) if full else 0.0,
                          "centroid": (float(xs.mean() / MASK_SCALE), float(ys.mean() / MASK_SCALE)) if vis else None,
                          "mask": vis_m, "full": m}
        fb = np.nonzero(m)
        if full:
            stats[e["id"]]["bbox"] = (float(fb[1].min() / MASK_SCALE), float(fb[0].min() / MASK_SCALE), float((fb[1].max() + 1) / MASK_SCALE), float((fb[0].max() + 1) / MASK_SCALE))
        else:
            stats[e["id"]]["bbox"] = None
    return stats


def aoi_cells(mask):
    h, w = mask.shape
    tot = mask.sum()
    cells = []
    if not tot:
        return cells
    for r, rn in enumerate("TMB"):
        for c, cn in enumerate("LCR"):
            sub = mask[r * h // 3:(r + 1) * h // 3, c * w // 3:(c + 1) * w // 3]
            if sub.sum() / tot >= 0.04:
                cells.append(rn + cn)
    return cells


def clutter(img_rgb, n_objects):
    g = np.asarray(img_rgb.convert("L"), dtype=np.float32)
    gx = np.abs(np.diff(g, axis=1))[:-1, :]
    gy = np.abs(np.diff(g, axis=0))[:, :-1]
    edges = (np.hypot(gx, gy) > 40).mean()
    buf = io.BytesIO()
    img_rgb.save(buf, "PNG", optimize=True)
    jbuf = io.BytesIO()
    img_rgb.convert("RGB").save(jbuf, "JPEG", quality=90)
    return {"objects": n_objects, "edge_density": round(float(edges), 4), "png_bytes": len(buf.getvalue()), "jpeg_bytes": len(jbuf.getvalue())}


def to_gray(img):
    """Rec. 709 luma."""
    a = np.asarray(img.convert("RGB"), dtype=np.float32)
    y = 0.2126 * a[:, :, 0] + 0.7152 * a[:, :, 1] + 0.0722 * a[:, :, 2]
    return Image.fromarray(np.clip(y, 0, 255).astype(np.uint8), "L")


# ---------------------------------------------------------------- legibility
# big surfaces a head or body may be seen against without harm
BACKDROP_IDS = {"sky", "ground", "hills", "tree_line", "house", "buildings", "fence", "path", "pond", "blanket", "sandbox", "stall",
                "clouds_white", "clouds_dark", "sun"}


BODY_ANCHORS = {"head_top", "eye_L", "eye_R", "gaze_target", "mouth", "chest", "seat", "foot_L", "foot_R"}


def thin_part(m, width=11):
    """Pixels of a mask that belong to strokes narrower than `width` mask pixels (strings, poles, legs)."""
    from scipy.ndimage import binary_opening
    if not m.any():
        return m
    return m & ~binary_opening(m, structure=np.ones((width, width), dtype=bool))


BODY_LIMIT = 0.10       # share of a person's body a structure they do not use may cover or back (revision 4)
LEGS_PX = 15            # mask pixels of a person's legs a structure in front of them may cover (revision 4)


def legs_of(m):
    """The lower 35% of a figure's mask: legs and feet."""
    rows = np.nonzero(m.any(axis=1))[0]
    out = np.zeros_like(m)
    if rows.size:
        cut = int(rows.min() + 0.65 * (rows.max() - rows.min()))
        out[cut:, :] = m[cut:, :]
    return out
CLEAR_PX = 6            # clearance, in mask pixels (12 px), kept between a thin stroke and a head or a hand
PERSON_CLEAR_PX = 10    # clearance (20 px) kept between a head and any part of another person (a carried box at a face)


def clearance_ok(m, TH, headbox, hands, c=CLEAR_PX):
    """Revision 4: no thin stroke may touch a head or a hand without crossing it (a lamp post standing on
    a cap, a catcher's hands against a pole). `headbox` is (x0, y0, x1, y1) in mask pixels, `hands` are
    full-resolution points."""
    H, W = TH.shape
    x0, y0, x1, y1 = headbox
    ring = TH[max(0, y0 - c):min(H, y1 + c), max(0, x0 - c):min(W, x1 + c)]
    if int(ring.sum()) > 4:
        return False
    for hx, hy in hands:
        cx, cy = int(hx * MASK_SCALE), int(hy * MASK_SCALE)
        if int(TH[max(0, cy - c):min(H, cy + c + 1), max(0, cx - c):min(W, cx + c + 1)].sum()) > 3:
            return False
    return True


def legibility(sc, els, stats, head_limit=0.10, cross_px=30):
    """Readable-figure rules for every person in the picture.

    head:  no other element (except big backdrops and the person's own attached strings/props)
           may cover or sit behind more than `head_limit` of the person's head
    cross: no string, pole or other thin stroke that is not the person's own may cross their body
    Returns (ok, list of problems)."""
    W = D.W
    mir = sc.mirror_scene
    bad = []
    people = [e for e in els if e["kind"] == "asset" and e["asset"].family.startswith("person.")]
    others = [e for e in els if e["role"] not in BACKGROUND_ROLES and e["id"] not in BACKDROP_IDS and e["id"] in stats]
    thin = {}

    ok_pairs = getattr(sc, "legib_ok", set())
    from . import scene as SCN
    rev = SCN.PLACEMENT_REV
    setting_ids = {x["id"] for x in sc.S.elements}
    # elements drawn by the same event as a person (a kite and its flyer, a ball trail and its thrower)
    # belong together: the clearance rules do not apply between them
    owner = {}
    for it in getattr(sc, "items", []):
        for x in list(it.get("elements", [])) + list(it.get("cues", []) or []):
            owner.setdefault(x, set()).add(it.get("event"))
    for x, ev in getattr(sc, "ev_of", {}).items():
        owner.setdefault(x, set()).add(ev)

    def same_event(a, b):
        return bool(owner.get(a, set()) & owner.get(b, set()) - {None})

    def attached(o, p):
        """A drawn extra that hangs off one of this person's prop points (string, leash, water, hose)."""
        if o["kind"] == "asset" or o["id"] not in sc.svgs:
            return False
        b = o.get("bbox")
        if not b:
            return False
        for name, a in p.m["anchors"].items():
            if name.split("@")[0] in BODY_ANCHORS:
                continue
            x, y = p.pt(a["px"])
            if b[0] - 14 <= x <= b[2] + 14 and b[1] - 14 <= y <= b[3] + 14:
                return True
        return False

    for e in people:
        p = e["asset"]
        st = stats.get(e["id"])
        if st is None:
            continue
        full = st["full"]
        ht = p.anchor("head_top")
        em = p.eye_mid()
        r = max(6.0, (em[1] - ht[1]) * 1.30)
        hx = (ht[0] + em[0]) / 2
        bx0, bx1 = hx - r, hx + r
        if mir:
            bx0, bx1 = W - bx1, W - bx0
        X0, X1 = int(max(0, bx0) * MASK_SCALE), int(min(W, bx1) * MASK_SCALE) + 1
        Y0, Y1 = int(max(0, ht[1]) * MASK_SCALE), int((ht[1] + 2.15 * r) * MASK_SCALE) + 1
        head = full[Y0:Y1, X0:X1]
        npx = int(head.sum())
        # the crossing rule ignores the feet: standing on or beside a mark on the ground is natural
        rows = np.nonzero(full.any(axis=1))[0]
        body = full.copy()
        if rows.size:
            cut = int(rows.max() - 0.07 * (rows.max() - rows.min()))
            body[cut:, :] = False
        hands = [p.anchor(h) for h in ("hand_L_grip", "hand_R_grip") if p.has_anchor(h)]
        if mir:
            hands = [(W - hx, hy) for hx, hy in hands]
        body_px = int(full.sum())
        legs = legs_of(full)
        feet = np.zeros_like(full)
        if rows.size:
            fc = int(rows.max() - 0.12 * (rows.max() - rows.min()))
            feet[fc:, :] = full[fc:, :]
        for o in others:
            # (from revision 4 an extra counts as the person's own only if their event drew it: a kite
            # string whose box happened to contain a reader's book passed through his head unchecked)
            if o is e or (o["id"], e["id"]) in ok_pairs or (attached(o, p) and (rev < 4 or same_event(o["id"], e["id"]))):
                continue
            om = stats[o["id"]]["full"]
            if npx >= 12:
                ov = int((head & om[Y0:Y1, X0:X1]).sum()) / npx
                if ov > head_limit:
                    bad.append(f"{o['id']} overlaps {e['id']}'s head ({ov:.0%})")
                    continue
            if o["id"] not in thin:
                thin[o["id"]] = thin_part(om)
            n = int((thin[o["id"]] & body).sum())
            if n > cross_px:
                bad.append(f"{o['id']} crosses {e['id']} ({n} px)")
                continue
            if rev >= 4 and same_event(o["id"], e["id"]):
                continue
            if rev >= 4 and o["kind"] == "asset" and o["asset"].family.startswith("person."):
                # another person's feet or hands may not rest against this person's head
                c = PERSON_CLEAR_PX
                ring = om[max(0, Y0 - c):Y1 + c, max(0, X0 - c):X1 + c]
                if int(ring.sum()) > 25:
                    bad.append(f"{o['id']} touches {e['id']}'s head")
                    continue
            if rev >= 4 and o["kind"] != "asset":
                if not clearance_ok(full, thin[o["id"]], (X0, Y0, X1, Y1), hands):
                    bad.append(f"{o['id']} touches {e['id']}'s head or hand")
                    continue
                if o["id"] in setting_ids and body_px and int((om & body).sum()) > BODY_LIMIT * body_px:
                    bad.append(f"{e['id']} stands in {o['id']}")
                    continue
                if o["id"] in setting_ids and o["z"] > e["z"] and int((om & legs).sum()) > LEGS_PX:
                    bad.append(f"{e['id']} stands behind {o['id']}")
                    continue
            if rev >= 4 and o["kind"] != "asset" and o["id"] not in setting_ids and o["z"] > e["z"] and int((om & feet).sum()) > LEGS_PX:
                # a prop of another event drawn over someone's feet (a man behind a wheelbarrow seemed to
                # stand in it)
                bad.append(f"{e['id']} stands behind {o['id']}")
    return (not bad), bad
