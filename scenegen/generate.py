"""Generate TPDB scenes at target tiers.

    python -m scenegen.generate --tier 2 --setting park --seed 7 --out scenes/
    python -m scenegen.generate --batch showcase --out scenes/

Each scene is saved as <name>.svg, <name>.png, <name>_gray.png and <name>.json (the record:
items with accepted phrasings, features, difficulty and predicted probability, element ids and
AOI cells, clutter metrics, every check, and what is needed to regenerate it exactly).
"""
import argparse
import json
import os
import time

from . import compose as K
from . import difficulty as DF
from . import draw as D
from .library import Library
from .planner import GENERATOR_VERSION, USAGE, finalize, near_band, plan, quick_estimate, realize, signature
from . import scene as SCN
from .scene import PlacementError


def scene_name(tier, setting, seed):
    return f"T{tier}_{setting}_s{seed:03d}"


def record(sc, fin, name):
    stats = fin["stats"]
    mir = sc.mirror_scene

    def mb(b):
        if b is None:
            return None
        return [round(b[0], 1), round(b[1], 1), round(b[2], 1), round(b[3], 1)]

    elements = []
    for e in fin["els"]:
        st = stats.get(e["id"])
        d = {"id": e["id"], "label": e["label"], "role": e["role"], "z": round(e["z"], 2)}
        if st:
            d.update({"bbox": mb(st["bbox"]), "area_px": round(st["area"]), "visible_px": round(st["visible"]), "occlusion": round(st["occlusion"], 3)})
        if e["kind"] == "asset":
            p = e["asset"]
            d["asset"] = {"variant": p.v, "family": p.family, "scale": round(p.k, 4), "mirrored": p.mirror != mir,
                          "labels": sc.lib.label(p.family)}
        elements.append(d)
    items = []
    for it in sc.items:
        items.append({k: it[k] for k in ("id", "type", "text", "accepted", "key", "elements", "cues", "effect", "chain", "animate", "domain",
                                         "template", "event", "features", "b", "p0", "pm1", "aoi_cells")})
    pc0, pcm = fin["pc"]
    pi0, pim = fin["pi"]
    lib = sc.lib
    return {
        "name": name,
        "tier": sc.tier,
        "setting": sc.setting_id,
        "sky": sc.sky,
        "seed": sc.seed,
        "mirror": sc.mirror_scene,
        "versions": {"generator": GENERATOR_VERSION, "cast_builder": lib.catalog.get("builder_version"), "weights": "spec-starting-v1",
                     "salience_ref": DF.SALIENCE_REF},
        "features": sorted(sc.features),
        "templates": [{"id": t.id, "kind": t.kind, "event": t.ev, "units": t.units} for t in sc.templates],
        "scene_load": len(sc.events),
        "items": items,
        "counts": {"content": fin["n_content"], "inference_units": fin["n_units"], "contradictions": fin["n_contra"],
                   "items_total": len(items)},
        "predicted": {"theta_0": {"content": round(pc0, 3) if pc0 is not None else None, "inference": round(pi0, 3) if pi0 is not None else None},
                      "theta_minus_1": {"content": round(pcm, 3) if pcm is not None else None, "inference": round(pim, 3) if pim is not None else None}},
        "bands": fin["bands"],
        "in_tier": all(fin["bands"].values()),
        "checks": {k: {"result": bool(v[0]) if isinstance(v, tuple) else bool(v), "detail": v[1] if isinstance(v, tuple) else ""} for k, v in fin["checks"].items()},
        "clutter": fin.get("clutter"),
        "signature": signature(sc.items),
        "elements": elements,
        "canvas": [D.W, D.H],
    }


def save(sc, fin, out_dir, name):
    os.makedirs(out_dir, exist_ok=True)
    body = "".join(K.markup(e) for e in fin["els"])
    svg = K.svg_doc(body, f"TPDB {name}", mirror=sc.mirror_scene)
    open(os.path.join(out_dir, name + ".svg"), "w").write(svg)
    img = K.render_png(svg).convert("RGB")
    img.save(os.path.join(out_dir, name + ".png"), optimize=True)
    K.to_gray(img).save(os.path.join(out_dir, name + "_gray.png"), optimize=True)
    img.resize((480, 300)).save(os.path.join(out_dir, name + "_thumb.png"), optimize=True)
    n_obj = sum(1 for e in fin["els"] if e["role"] != "background")
    fin["clutter"] = K.clutter(img, n_obj)
    rec = record(sc, fin, name)
    json.dump(rec, open(os.path.join(out_dir, name + ".json"), "w"), indent=1)
    return rec


def build_one(lib, tier, setting, seed, out_dir, forced=None, require_band=True, max_tries=12, placements=14, log=print):
    """Try cast/variant sets (seed, seed+1000, ...) and, for each, several layouts of the same rendered
    variants, until a scene places, passes the rules and lands in its tier band."""
    usage0 = dict(USAGE)        # template choice leans away from templates used so far; kept for exact regeneration
    tried = []
    for k in range(max_tries):
        s = seed + 1000 * k
        try:
            sc = plan(tier, setting, s, lib, forced)
        except PlacementError as e:
            tried.append((s, str(e)))
            continue
        lib.ensure(sc.variants, log=log)
        why_set = []
        knob = 0
        Tb = DF.TIERS[tier]
        for r in range(placements):
            sc.reset_layout(s * 31 + r)
            sc.knob = knob
            ok, why = realize(sc)
            if not ok:
                why_set.append(why)
                continue
            pcq, piq = quick_estimate(sc)
            if require_band and not near_band(tier, pcq, piq):
                why_set.append(f"estimate out of band (knob {knob}) pc~{pcq if pcq is None else round(pcq, 3)} pi~{piq if piq is None else round(piq, 3)}")
                # turn the inference radicals (cue size, separation) toward the band
                if Tb["pi"] and piq is not None:
                    if piq > Tb["pi"][1]:
                        knob = min(1, knob + 1)
                    elif piq < Tb["pi"][0]:
                        knob = max(-1, knob - 1)
                continue
            fin = finalize(sc)
            if not fin["checks"]["occlusion_and_size"][0]:
                why_set.append(fin["checks"]["occlusion_and_size"][1])
                continue
            if not fin["checks"]["legibility"][0]:
                why_set.append("legibility: " + fin["checks"]["legibility"][1])
                continue
            if require_band and not fin["checks"]["clutter_band"][0]:
                why_set.append(fin["checks"]["clutter_band"][1])
                continue
            if require_band and not all(fin["bands"].values()):
                why_set.append("out of band: " + json.dumps({k_: v for k_, v in fin["bands"].items() if not v}) +
                               f" pc={fin['pc'][0]:.3f} pi={fin['pi'][0] if fin['pi'][0] is None else round(fin['pi'][0], 3)}")
                continue
            name = scene_name(tier, setting, s)
            rec = save(sc, fin, out_dir, name)
            rec["attempts"] = tried + [(s, f"layout {r + 1}: accepted after {len(why_set)} rejected layouts")]
            rec["layout"] = r
            rec["knob"] = sc.knob
            rec["regen"] = {"base_seed": seed, "max_tries": max_tries, "placements": placements, "require_band": require_band,
                            "usage": usage0, "forced": forced, "placement_rev": SCN.PLACEMENT_REV}
            json.dump(rec, open(os.path.join(out_dir, name + ".json"), "w"), indent=1)
            USAGE.update(t.id for t in sc.templates)
            return rec, sc, fin
        tried.append((s, "; ".join(sorted(set(why_set)))[:600]))
    return None, None, tried


def regenerate(lib, rec_path, out_dir):
    """Rebuild a saved scene exactly: same base seed, same template-usage history, same isomorph source."""
    from .batch import build_isomorph
    r = json.load(open(rec_path))
    g = r["regen"]
    SCN.PLACEMENT_REV = g.get("placement_rev", 1)
    if g.get("isomorph_of"):
        rec_a = json.load(open(os.path.join(os.path.dirname(rec_path), g["isomorph_of"] + ".json")))
        return build_isomorph(lib, rec_a, r["setting"], g["seed"], out_dir, log=lambda *a: None), None, None
    USAGE.clear()
    USAGE.update(g["usage"])
    return build_one(lib, r["tier"], r["setting"], g["base_seed"], out_dir, forced=g.get("forced"), require_band=g["require_band"],
                     max_tries=g["max_tries"], placements=g["placements"], log=lambda *a: None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", type=int, default=2)
    ap.add_argument("--setting", default="garden")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default="scenes")
    ap.add_argument("--any-band", action="store_true")
    ap.add_argument("--from-record", default=None, help="rebuild the scene saved in this JSON record exactly")
    a = ap.parse_args()
    lib = Library()
    t0 = time.time()
    if a.from_record:
        rec, _, _ = regenerate(lib, a.from_record, a.out)
        print("rebuilt", rec.get("name") if rec else rec, f"{time.time() - t0:.1f}s")
        return
    rec, sc, fin = build_one(lib, a.tier, a.setting, a.seed, a.out, require_band=not a.any_band)
    if rec is None:
        print("failed:", json.dumps(fin, indent=1))
        return
    print(json.dumps({k: rec[k] for k in ("name", "counts", "predicted", "bands", "in_tier", "scene_load")}, indent=1))
    for it in rec["items"]:
        print(f'{it["id"]} {it["type"]:22s} b={it["b"]:+.2f} p0={it["p0"]:.2f}  {it["text"]}')
    print(f"{time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
