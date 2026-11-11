"""Rewrite scenes<TAG>/showcase_summary.json from the records. OPEN and NOTES are per release: edit them for the cells that came from wide searches."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, glob, sys
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.batch import SHOWCASE
OPEN = {("garden", 4), ("park", 4), ("playground", 4)}
# a cell built from a forced template set (regen.forced) carries this note in place of the search notes
FORCED = {("street", 4)}
NOTES = {("garden", 4): "v0.47's seed, 521004, and thirty-two more seeds of the search fail under revision 45 and v0.48's prior (calibrated again "
                        "with the v0.48 cast); the thirty-fourth, 552716, placed on its seventh step (s558716), with other templates",
         ("park", 4): "the v0.43 seed, which placed again under revision 45 with the same templates, as in v0.39 to v0.47; redrawn with the v0.48 cast",
         ("street", 4): "v0.47's template set (v0.44's with the walker about to trip swapped for the dropped ice cream) on the v0.32 seed, which "
                        "placed on its second step (s431752). The set with the walker placed on 0 seeds of 8 under revision 45, every one of its "
                        "112 layouts failing on the walker: he wants no post, tree or stall behind or ahead of him (templates.TRIP47) and now "
                        "clear room for two motion lines behind his back (templates.TRIP48), and the crowded street leaves him no such place",
         ("playground", 4): "v0.47's seed (v0.45's, 494878), which placed again on its ninth step with the same templates; redrawn with the v0.48 cast",
         ("playground", 3): "placed by the showcase pass on its seed, 43 (its eighth step, s7043), where v0.47's cell was built from a forced set",
         ("street", 3): "placed by the showcase pass on its seed, 133, where v0.47's cell came from a search past it; it holds the walker about to "
                        "trip, which this release gave motion lines and a nearer obstacle"}
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
    if (st, t) in FORCED:
        assert r["regen"].get("forced"), r["name"]
        e["note"] = "built from a forced template set (regen.forced), with no template-variety steering (regen.usage is empty)"
    elif (st, t) in OPEN:
        e["note"] = "found by a wider seed search with no template-variety steering (regen.usage is empty), as since v0.15"
    elif r["regen"]["base_seed"] != seed:
        e["note"] = f"found by a seed search past the showcase seed {seed} (batch rules, template variety honoured)"
    if (st, t) in NOTES:
        e["note"] = (e.get("note", "") + "; " if e.get("note") else "") + NOTES[(st, t)]
    out.append(e)
    print(st, t, r["name"], r["regen"]["base_seed"], e.get("note", "")[:90])
json.dump(out, open(f"scenes{TAG}/showcase_summary.json", "w"), indent=1)
