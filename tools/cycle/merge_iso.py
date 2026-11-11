"""merge_iso.py : the isomorph summaries of the separate runs (scenes<TAG>/isomorph_summary_*.json) merged into scenes<TAG>/isomorph_summary.json,
each entry checked against its record's own isomorph_check; the parts are moved to <WORK>/iso_parts<TAG>. Run once, when the isomorphs are
settled and any picture taken out has had its entry removed from its part."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import os, json, glob, shutil
os.chdir(ROOT)
OUT, PARTS = f"scenes{TAG}", os.path.join(WORK, f"iso_parts{TAG}")
assert not os.path.exists(OUT + "/isomorph_summary.json")
parts = sorted(glob.glob(OUT + "/isomorph_summary_*.json"))
ent = []
for p in parts:
    ent += json.load(open(p))
recs = {os.path.basename(f)[:-5]: json.load(open(f)) for f in glob.glob(OUT + "/T*_iso.json")}
assert sorted(e["B"] for e in ent) == sorted(recs), (sorted(e["B"] for e in ent), sorted(recs))
for e in ent:
    r = recs[e["B"]]
    assert r["isomorph_of"] == e["A"] and e["failed"] is None, e["B"]
    assert os.path.exists(f"{OUT}/{e['A']}.json"), e["A"]
    assert r["isomorph_check"] == e["check"], e["B"]
    assert r["isomorph_check"]["same_signature"] and r["isomorph_check"]["content_diff"] <= 0.02 and r["isomorph_check"]["inference_diff"] <= 0.02
ent.sort(key=lambda e: (recs[e["B"]]["tier"], e["A"]))
json.dump(ent, open(OUT + "/isomorph_summary.json", "w", newline="\n"), indent=1)
os.makedirs(PARTS, exist_ok=True)
for p in parts:
    shutil.move(p, PARTS + "/" + os.path.basename(p))
for e in ent:
    c = e["check"]
    print(e["A"], "->", e["B"], "dc", c["content_diff"], "di", c["inference_diff"])
print("MERGED", len(ent))
