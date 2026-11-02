"""Measure each inference template's realized item features (salience, cues, separation) so the
planner's priors match what placement actually produces.

    python -m scenegen.calibrate --out calibration.json

For every inference module and contradiction, in every setting it fits, the template is cast
alone (seeds 1..n), placed in several layouts, measured from masks, and its inference items'
difficulty without the scene-load term (b0 = b - 0.12 L) is recorded.
"""
import argparse
import json
import statistics

from . import difficulty as DF
from . import templates as TP
from .library import Library
from .planner import feasible, finalize, plan, realize
from .scene import PlacementError


def run(n_seeds=2, layouts=3, out="calibration.json", only=None):
    import os
    lib = Library()
    res = json.load(open(out)) if only and os.path.exists(out) else {}
    for c in TP.MODULES + TP.CONTRADICTIONS:
        if only and c.id not in only:
            continue
        rows = []
        for setting in ("garden", "park", "street", "playground"):
            sky = "dark" if c.sky == "dark" else "clear"
            if not feasible(c, setting, sky):
                continue
            kind = "modules" if c.kind == "inference" else "contradictions"
            for seed in range(1, n_seeds + 1):
                try:
                    sc = plan(2, setting, seed, lib, forced={kind: [c.id]})
                except PlacementError:
                    continue
                lib.ensure(sc.variants, log=lambda *a: None)
                for r in range(layouts):
                    sc.reset_layout(seed * 97 + r)
                    ok, why = realize(sc)
                    if not ok:
                        continue
                    fin = finalize(sc, objects_target=18)
                    L = len(sc.events)
                    for it in sc.items:
                        if it["type"] in DF.INFERENCE_TYPES:
                            f = it["features"]
                            rows.append({"setting": setting, "type": it["type"], "b0": round(it["b"] - DF.WEIGHTS["load"] * L, 3),
                                         "s": f["s"], "d": f["d"], "r": f["r"], "f": f["f"], "a": f.get("a"),
                                         "aoa_raw": f.get("aoa_raw"), "chain": f["chain"]})
        by = {}
        for row in rows:
            by.setdefault(row["type"], []).append(row)
        res[c.id] = {t: {"n": len(v), "b0_mean": round(statistics.mean(x["b0"] for x in v), 3),
                         "b0_sd": round(statistics.pstdev(x["b0"] for x in v), 3),
                         "s_mean": round(statistics.mean(x["s"] for x in v), 3), "d_mean": round(statistics.mean(x["d"] for x in v), 3),
                         "r": v[0]["r"], "f": v[0]["f"], "a": v[0]["a"], "aoa_raw": v[0]["aoa_raw"], "chain": v[0]["chain"]}
                     for t, v in by.items()}
        print(c.id, json.dumps(res[c.id]), flush=True)
        json.dump(res, open(out, "w"), indent=1)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="calibration.json")
    ap.add_argument("--seeds", type=int, default=2)
    ap.add_argument("--layouts", type=int, default=3)
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    run(a.seeds, a.layouts, a.out, a.only)


if __name__ == "__main__":
    main()
