"""Rewrite scenes<TAG>/showcase_summary.json from the records. OPEN and NOTES are per release: edit them for the cells that came from wide searches."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, glob, sys
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.batch import SHOWCASE
OPEN = {("garden", 4), ("park", 4), ("playground", 4)}
NOTES = {("garden", 4): "the v0.22 seed, which placed again under revision 21 with the same events",
         ("park", 4): "the v0.22 seed, which placed again under revision 21 with the same events",
         ("playground", 4): "the v0.22 seed, which placed again under revision 21 with the same events",
         ("street", 4): "found by the showcase pass (attempt 21 of the showcase seed); a search from the v0.22 seed also placed a street, kept out of the set so that each cell has one picture"}
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
        e["note"] = "found by a wider seed search with no template-variety steering (regen.usage is empty), as in v0.15 to v0.22"
    elif r["regen"]["base_seed"] != seed:
        e["note"] = f"found by a seed search past the showcase seed {seed} (batch rules, template variety honoured)"
    if (st, t) in NOTES:
        e["note"] = (e.get("note", "") + "; " if e.get("note") else "") + NOTES[(st, t)]
    out.append(e)
    print(st, t, r["name"], r["regen"]["base_seed"], e.get("note", "")[:90])
json.dump(out, open(f"scenes{TAG}/showcase_summary.json", "w"), indent=1)
