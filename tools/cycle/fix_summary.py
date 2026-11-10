"""Rewrite scenes<TAG>/showcase_summary.json from the records. OPEN and NOTES are per release: edit them for the cells that came from wide searches."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, glob, sys
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.batch import SHOWCASE
OPEN = {("garden", 4), ("park", 4), ("street", 4), ("playground", 4)}
NOTES = {("garden", 4): "v0.45's seed, 510013, and the next two of its list fail under v0.46's prior (calibrated again with the v0.46 cast); the "
                        "fourth seed, 522986, placed, with other templates",
         ("park", 4): "the v0.43 seed, which placed again under revision 43 with the same templates, as in v0.39 to v0.45; redrawn with the v0.46 cast",
         ("street", 4): "v0.44's template set (v0.29 to v0.43's with the upward water, which revisions 42 and 43 keep out of the street, swapped for the "
                        "square wheel), forced on the v0.32 seed as in v0.44 and v0.45 (free search failed 39 seeds in v0.32) (regen.forced)",
         ("playground", 4): "v0.45's seed, 494878, and the next six of its search fail under v0.46's prior; the eighth seed, 486950, placed, with "
                            "other templates",
         ("playground", 3): "placed by the showcase pass under v0.46's prior, on the showcase seed's seventh step (s6043); v0.43 to v0.45 took it "
                            "from a kept seed list (s32043)"}
recs = {}
for f in glob.glob(f"scenes{TAG}/T*.json"):
    r = json.load(open(f))
    if r.get("isomorph_of"): continue
    assert (r["setting"], r["tier"]) not in recs, f
    recs[(r["setting"], r["tier"])] = r
out = []
for st, t, seed in SHOWCASE:
    r = recs[(st, t)]
    e = {"name": r["name"], "setting": st, "tier": t, "attempts": len(r["attempts"]) + 1, "predicted": r["predicted"], "counts": r["counts"],
         "seconds": None, "base_seed": r["regen"]["base_seed"]}
    if (st, t) in OPEN:
        e["note"] = "found by a wider seed search with no template-variety steering (regen.usage is empty), as since v0.15"
    elif r["regen"]["base_seed"] != seed:
        e["note"] = f"found by a seed search past the showcase seed {seed} (batch rules, template variety honoured)"
    if (st, t) in NOTES:
        e["note"] = (e.get("note", "") + "; " if e.get("note") else "") + NOTES[(st, t)]
    out.append(e)
    print(st, t, r["name"], r["regen"]["base_seed"], e.get("note", "")[:90])
json.dump(out, open(f"scenes{TAG}/showcase_summary.json", "w"), indent=1)
