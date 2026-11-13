"""Rewrite scenes<TAG>/showcase_summary.json from the records. OPEN and NOTES are per release: edit them for the cells that came from wide searches."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, glob, sys
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.batch import SHOWCASE
OPEN = {("garden", 4), ("park", 4), ("street", 4), ("playground", 4)}
# a cell built from a forced template set (regen.forced) carries this note in place of the search notes
FORCED = set()
NOTES = {("garden", 4): "v0.49's seed, 763887, fails on all forty of its steps under revision 47 and v0.50's prior (calibrated again with "
                        "the v0.50 cast), and three more bases beside it; v0.48's seed, 552716, placed on its seventh step (s558716), with other templates",
         ("park", 4): "the v0.43 seed, which placed again under revision 47 with the same templates, as in v0.39 to v0.49; redrawn with the v0.50 cast",
         ("street", 4): "v0.49's seed, 443887, which placed again on its twenty-second step (s464887) with the same templates; redrawn with the "
                        "v0.50 cast",
         ("playground", 4): "v0.47's seed (v0.45's, 494878), which placed again on its ninth step with the same templates; redrawn with the v0.50 cast"}
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
