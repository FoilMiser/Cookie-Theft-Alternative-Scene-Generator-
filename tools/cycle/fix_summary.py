"""Rewrite scenes<TAG>/showcase_summary.json from the records. OPEN and NOTES are per release: edit them for the cells that came from wide searches."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, glob, sys
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.batch import SHOWCASE
OPEN = {("garden", 4), ("park", 4), ("street", 4), ("playground", 4), ("playground", 3)}
NOTES = {("garden", 4): "v0.44's seed (the first of v0.44's new list), which placed again under revision 43 with the same templates; redrawn with the "
                        "v0.45 cast",
         ("park", 4): "the v0.43 seed, which placed again under revision 43 with the same templates, as in v0.39 to v0.44; redrawn with the v0.45 cast",
         ("street", 4): "v0.44's template set (v0.29 to v0.43's with the upward water, which revisions 42 and 43 keep out of the street, swapped for the "
                        "square wheel), forced on the v0.32 seed as there (free search failed 39 seeds in v0.32) (regen.forced)",
         ("playground", 4): "the v0.43 seed (v0.42's 40th of its search) placed under revision 43 with the same templates until the lost balloon's "
                            "prior moved by 0.02 (templates.WOOD45, calibrated again after the set's first look); under the final prior it and the "
                            "next 14 of its search fail, and the 16th seed, 494878, placed, with other templates",
         ("garden", 3): "under the final prior (the lost balloon's moved by 0.02 with templates.WOOD45) the showcase seed's sixth try, s5013, where the "
                        "first calibration's took its fourth, s3013, with other templates; built from the first record's usage history",
         ("playground", 3): "the showcase pass and its search placed nothing on 13 base seeds under revision 43, as under revisions 41 and 42; v0.43's "
                            "kept seed list (tpdb_work/more45.sh) placed on its first seed again, v0.43's s32043, with the same templates"}
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
