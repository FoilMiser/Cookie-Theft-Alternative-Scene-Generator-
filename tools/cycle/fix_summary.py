"""Rewrite scenes<TAG>/showcase_summary.json from the records. OPEN and NOTES are per release: edit them for the cells that came from wide searches."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, glob, sys
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.batch import SHOWCASE
OPEN = {("garden", 4), ("park", 4), ("street", 4), ("playground", 4), ("playground", 3)}
NOTES = {("garden", 4): "the fourth seed of the search: v0.42's seed and two new ones did not place under revision 41 with the redrawn cast",
         ("park", 4): "the v0.42 seed, which placed again under revision 41 on the same layout, as in v0.39 to v0.42; redrawn with the v0.43 cast",
         ("street", 4): "v0.29 to v0.42's template set, forced on the v0.32 seed as there (free search failed 39 seeds in v0.32), placed under "
                        "revision 41 on v0.42's layout (regen.forced)",
         ("playground", 4): "the v0.42 seed (the 40th of its search), which placed again under revision 41 on the same layout; redrawn with the "
                            "v0.43 cast",
         ("playground", 3): "the showcase pass and its search placed nothing on 13 base seeds under revision 41; two new seed lists side by side "
                            "(tpdb_work/t3pg43.sh) each placed on their first seed, and the second's is kept"}
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
