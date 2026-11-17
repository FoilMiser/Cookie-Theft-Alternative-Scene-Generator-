"""Rewrite scenes<TAG>/showcase_summary.json from the records. OPEN and NOTES are per release: edit them for the cells that came from wide searches."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, glob, sys
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.batch import SHOWCASE
OPEN = {("garden", 4), ("park", 4), ("street", 4), ("playground", 4)}
# a cell built from a forced template set (regen.forced) carries this note in place of the search notes
FORCED = {("garden", 4), ("street", 4)}
NOTES = {("garden", 4): "v0.46's set on v0.46's seed, 552986 (tools/cycle/forced_cell.py, v046garden), as in v0.53 to v0.55, after the free search "
                        "failed on fourteen bases; the pictures are new, since v0.56's cast and placement revision 50 move every figure",
         ("park", 4): "the free search's fifth base, 732977 (v0.55's seed 728923 first, which no longer placed)",
         ("street", 4): "v0.55's street set with the dog that reads a newspaper in place of the man who sits on nothing "
                        "(tools/cycle/forced_cell.py, v056street), on base 445887. The free search failed on 46 bases, and v0.55's own set, which now "
                        "holds the bicycle's owner as well, did not place on eight",
         ("playground", 4): "the free search on a second range of seeds, base 560007, its ninth step (s568007); v0.55's base 506950 and seven "
                            "more failed first"}
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
