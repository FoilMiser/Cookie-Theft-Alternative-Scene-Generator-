"""Rewrite scenes<TAG>/showcase_summary.json from the records. OPEN and NOTES are per release: edit them for the cells that came from wide searches."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, glob, sys
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.batch import SHOWCASE
OPEN = {("garden", 4), ("park", 4), ("playground", 4)}
# a cell built from a forced template set (regen.forced) carries this note in place of the search notes
FORCED = {("street", 4), ("playground", 3)}
NOTES = {("garden", 4): "v0.46's seed, 522986, fails under revision 44 and v0.47's prior (calibrated again with the v0.47 cast); the next seed of "
                        "the search, 521004, placed on its thirty-sixth step (s556004), with other templates",
         ("park", 3): "built twice from the showcase seed, 23. The first record was its eleventh step (s10023). A rule found after the set was "
                      "built (templates.CONE47: the dropped ice cream drawn with either child) lets the ninth step place, so the cell "
                      "rebuilds to s8023 and that is the record, with other templates",
         ("park", 4): "the v0.43 seed, which placed again under revision 44 with the same templates, as in v0.39 to v0.46; redrawn with the v0.47 cast",
         ("street", 4): "v0.44's template set with the walker about to trip swapped for the dropped ice cream, on the v0.32 seed as in v0.44 to "
                        "v0.46. Revision 44 lets nothing upright of the setting stand behind or ahead of that walker (templates.TRIP47), and the "
                        "crowded street left him no such place: v0.44's set failed on 31 bases of eight sets each, every set on the walker",
         ("playground", 4): "v0.46's seed, 486950, and thirteen more seeds of the search fail under revision 44 and v0.47's prior; v0.45's seed, "
                            "494878, placed on its ninth step (s502878), with other templates",
         ("playground", 3): "the showcase pass failed on its seed and twelve more bases of 24 sets each. Of fourteen forced sets measured, four "
                            "placed inside the tier's band; this one (the lost balloon, the seesaw with its heavy end, the bucket for a hat, a "
                            "perched bird, a dog at play; base 6043) holds three templates no other cell has"}
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
