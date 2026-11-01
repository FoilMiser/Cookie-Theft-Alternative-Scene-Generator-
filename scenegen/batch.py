"""Batch generation: the showcase set (every setting at every tier) and isomorph pairs.

    python -m scenegen.batch showcase --out scenes
    python -m scenegen.batch isomorphs --out scenes

Isomorph rule (Difficulty Model Spec): two scenes are interchangeable forms of a tier when their
items match type for type with the same chain lengths, their predicted content and inference
completeness differ by no more than 0.02, and their clutter falls in the same band. B is built from
A by swapping every template for a different one with the same item signature (and, for
contradictions, the same knowledge domain) that fits B's setting, keeping A's number of scored
setting entities, and steering B's entity choice toward A's content completeness.
"""
import argparse
import json
import os
import random
import time

from . import difficulty as DF
from . import scene as SCN
from . import templates as TP
from .generate import build_one, save, scene_name
from .library import Library
from .planner import feasible, finalize, plan, realize, signature
from .scene import PlacementError

# cells whose template variety is counted within their own setting, not across the batch: counted across
# the batch, the least-used templates left these busiest cells only combinations that cannot be placed
# (v0.7: in the garden they were all hose, flower-bed and fence events competing for one corner)
LOCAL_VARIETY = {("playground", 4), ("garden", 4), ("street", 4)}
SHOWCASE = [("garden", 1, 11), ("garden", 2, 12), ("garden", 3, 13), ("garden", 4, 14),
            ("park", 1, 21), ("park", 2, 22), ("park", 3, 23), ("park", 4, 24),
            ("street", 1, 31), ("street", 2, 32), ("street", 3, 133), ("street", 4, 34),
            ("playground", 1, 41), ("playground", 2, 42), ("playground", 3, 43), ("playground", 4, 47)]


def iso_key(c):
    return (c.kind, tuple(sorted(TP.SIG[c.id])), c.domain if c.kind == "contradiction" else None)


def iso_map(ids, setting, rng):
    """Map each template of A to a different template with the same signature that fits `setting`."""
    out, used_res = {"modules": [], "contradictions": [], "events": []}, set()
    taken = set()
    sky = "dark" if "rain_coming" in ids else "clear"
    order = sorted(ids, key=lambda i: TP.ALL_TEMPLATES[i].kind != "inference")
    for tid in order:
        src = TP.ALL_TEMPLATES[tid]
        cands = [c for c in TP.ALL_TEMPLATES.values() if iso_key(c) == iso_key(src) and c.id not in taken
                 and not (set(c.exclusive) & used_res)]
        cands = [c for c in cands if feasible(c, setting, "dark" if c.sky == "dark" else sky)]
        if not cands:
            raise PlacementError(f"no isomorph for {tid} in {setting}")
        rng.shuffle(cands)
        cands.sort(key=lambda c: c.id == tid)     # prefer a different template
        c = cands[0]
        if c.sky == "dark" and sky != "dark":
            # a dark-sky module can only come in when A had one too
            alt = [x for x in cands if x.sky != "dark"]
            if not alt:
                raise PlacementError("dark sky mismatch")
            c = alt[0]
        taken.add(c.id)
        used_res |= set(c.exclusive)
        out[{"inference": "modules", "contradiction": "contradictions", "event": "events"}[c.kind]].append(c.id)
    return out


def build_isomorph(lib, rec_a, setting, seed, out_dir, tries=14, layouts=10, log=print):
    rng = random.Random(seed)
    ids = [t["id"] for t in rec_a["templates"]]
    n_ent = sum(1 for it in rec_a["items"] if it["template"] == "setting")
    pcA, piA = rec_a["predicted"]["theta_0"]["content"], rec_a["predicted"]["theta_0"]["inference"]
    sigA = [tuple(x) for x in rec_a["signature"]]
    notes = []
    for k in range(tries):
        s = seed + 1000 * k
        try:
            forced = iso_map(ids, setting, rng)
            sc = plan(rec_a["tier"], setting, s, lib, forced)
        except PlacementError as e:
            notes.append(str(e))
            continue
        lib.ensure(sc.variants, log=log)
        knob = 0
        for r in range(layouts):
            sc.reset_layout(s * 31 + r)
            sc.knob = knob
            ok, why = realize(sc)
            if not ok:
                notes.append(why)
                continue
            fin = finalize(sc, entity_k=n_ent, pc_target=pcA)
            if not fin["checks"]["occlusion_and_size"][0]:
                notes.append(fin["checks"]["occlusion_and_size"][1][:120])
                continue
            if not fin["checks"]["legibility"][0]:
                notes.append("legibility: " + fin["checks"]["legibility"][1][:120])
                continue
            if not fin["checks"]["clutter_band"][0]:
                notes.append(fin["checks"]["clutter_band"][1])
                continue
            if signature(sc.items) != sigA:
                notes.append("signature mismatch")
                break
            pcB, piB = fin["pc"][0], fin["pi"][0]
            dc = abs(pcB - pcA)
            di = abs((piB or 0) - (piA or 0))
            notes.append(f"knob {knob}: dc={dc:.3f} di={di:.3f}")
            if di > 0.02 and piA is not None:
                knob = max(-1, min(1, knob + (1 if piB > piA else -1)))
                continue
            if dc <= 0.02 and all(fin["bands"].values()):
                name = scene_name(rec_a["tier"], setting, s) + "_iso"
                rec = save(sc, fin, out_dir, name)
                rec["isomorph_of"] = rec_a["name"]
                rec["knob"] = sc.knob
                rec["regen"] = {"isomorph_of": rec_a["name"], "seed": seed, "placement_rev": SCN.PLACEMENT_REV}
                rec["isomorph_check"] = {"same_signature": True, "content_diff": round(dc, 3), "inference_diff": round(di, 3),
                                         "clutter_A": rec_a["clutter"], "clutter_B": rec["clutter"], "attempts": notes[-12:]}
                json.dump(rec, open(os.path.join(out_dir, name + ".json"), "w"), indent=1)
                return rec
    return {"failed": notes[-30:]}


def run_showcase(out_dir, which=None):
    from collections import Counter
    from .planner import USAGE
    lib = Library()
    os.makedirs(out_dir, exist_ok=True)
    summary = []
    # pictures already in the folder (and not being remade) count toward template variety
    import glob
    for f in glob.glob(os.path.join(out_dir, "T*.json")):
        r = json.load(open(f))
        if r.get("isomorph_of") or (which and f"{r['setting']}{r['tier']}" in which):
            continue
        USAGE.update(t["id"] for t in r["templates"])
    for setting, tier, seed in SHOWCASE:
        if which and f"{setting}{tier}" not in which:
            continue
        t0 = time.time()
        saved = None
        if (setting, tier) in LOCAL_VARIETY:
            # counted across the whole batch, the least-used templates left the busiest playground only
            # combinations that could not be placed among its frames: here variety is counted within
            # the setting
            saved = Counter(USAGE)
            USAGE.clear()
            for f in glob.glob(os.path.join(out_dir, "T*.json")):
                r = json.load(open(f))
                if r["setting"] == setting and r["tier"] != tier and not r.get("isomorph_of"):
                    USAGE.update(t["id"] for t in r["templates"])
        # tier 4 pictures are crowded and need more casts to find one that places (the playground most)
        rec, sc, fin = build_one(lib, tier, setting, seed, out_dir, max_tries=40 if tier == 4 else 24, log=lambda *a: None)
        if rec is None:
            if saved is not None:
                USAGE.clear()
                USAGE.update(saved)
            summary.append({"setting": setting, "tier": tier, "failed": fin})
            print(setting, tier, "FAILED", json.dumps(fin)[:400], flush=True)
            continue
        if saved is not None:
            USAGE.clear()
            USAGE.update(saved)
            USAGE.update(t["id"] for t in rec["templates"])
        summary.append({"name": rec["name"], "setting": setting, "tier": tier, "attempts": len(rec["attempts"]) + 1,
                        "predicted": rec["predicted"], "counts": rec["counts"], "seconds": round(time.time() - t0)})
        print(setting, tier, rec["name"], rec["predicted"]["theta_0"], f"attempts={len(rec['attempts']) + 1}", f"{time.time() - t0:.0f}s", flush=True)
    path = os.path.join(out_dir, "showcase_summary.json")
    old = json.load(open(path)) if os.path.exists(path) and which else []
    keep = [x for x in old if f"{x['setting']}{x['tier']}" not in (which or [])]
    json.dump(keep + summary, open(path, "w"), indent=1)


def run_isomorphs(out_dir, pairs):
    lib = Library()
    res = []
    for a_name, setting, seed in pairs:
        rec_a = json.load(open(os.path.join(out_dir, a_name + ".json")))
        t0 = time.time()
        r = build_isomorph(lib, rec_a, setting, seed, out_dir, log=lambda *a: None)
        res.append({"A": a_name, "B": r.get("name"), "check": r.get("isomorph_check"), "failed": r.get("failed")})
        print(a_name, "->", r.get("name"), json.dumps(r.get("isomorph_check", r.get("failed")))[:300], f"{time.time() - t0:.0f}s", flush=True)
    json.dump(res, open(os.path.join(out_dir, "isomorph_summary.json"), "w"), indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["showcase", "isomorphs"])
    ap.add_argument("--out", default="scenes")
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--pairs", default=None, help="json list of [A_name, setting, seed]")
    a = ap.parse_args()
    if a.mode == "showcase":
        run_showcase(a.out, a.only)
    else:
        run_isomorphs(a.out, json.loads(a.pairs))


if __name__ == "__main__":
    main()
