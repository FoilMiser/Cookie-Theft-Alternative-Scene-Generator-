"""strict_count.py : the gate again with the full marks the scorers themselves flagged as judgement calls halved.

From v0.57 the scorers write the flag beside each score ("call": "two" where a score of 1 has another reading beside the target, "near"
where it rests on a near word or a target partly said; tools/cycle/prompts/scorer_template.txt), and this script reads the flags from
vision/v<TAG>/scores.json and the parts scores_<a..f>.json. From v0.41 to v0.56 the two lists were sorted by hand from the scorers'
prose (v0.56's 33 and 46 are in this file's history). DROP is for flags that are not calls by the rule (a name the key accepts), each
with its reason; it should stay empty. Prints the templates that would fall under 0.9 with the "two" calls halved, and with both
halved, and how many each scorer flagged. Run after the swap and vision/gate.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections, glob, json
os.chdir(ROOT)
DROP = {
    # ("pic_NN", "iNN"): "why this flag is not a call",
}
km = json.load(open(f"vision/v{TAG}/key_map.json"))
sc = json.load(open(f"vision/v{TAG}/scores.json", encoding="utf-8"))
TWO, NEAR, odd = set(), set(), []
for pic, v in sc.items():
    for iid, s in v["items"].items():
        c = s.get("call")
        if c in (None, "", "null", "none"):
            continue
        if (pic, iid) in DROP:
            continue
        if s.get("score") != 1:
            odd.append((pic, iid, s.get("score"), c))      # a flag on a score that is not 1: not counted, printed
            continue
        if c == "two":
            TWO.add((pic, iid))
        elif c == "near":
            NEAR.add((pic, iid))
        else:
            odd.append((pic, iid, s.get("score"), c))
print("flags: two", len(TWO), "near", len(NEAR), "dropped", len(DROP), "odd", odd)
for p in sorted(glob.glob(f"vision/v{TAG}/scores_?.json")):
    part = json.load(open(p, encoding="utf-8"))
    n2 = sum(1 for pic, v in part.items() for s in v["items"].values() if s.get("call") == "two" and s.get("score") == 1)
    nn = sum(1 for pic, v in part.items() for s in v["items"].values() if s.get("call") == "near" and s.get("score") == 1)
    print("  scorer", os.path.basename(p)[7:-5], "two", n2, "near", nn, "of", sum(len(v["items"]) for v in part.values()), "items")


def run(label, hedged):
    vals, tmpl_of, seen = collections.defaultdict(list), {}, set()
    for pic, name in km.items():
        f = next(p for p in (f"scenes/{name}.json", f"probes/{name}.json") if os.path.exists(p))
        r = json.load(open(f, encoding="utf-8"))
        for it in r["items"]:
            key = (pic, it["id"])
            if key in hedged:
                seen.add(key)
            t = it.get("template")
            if not t or t == "setting":
                continue
            v = sc[pic]["items"][it["id"]]["score"]
            v = 0.0 if isinstance(v, str) else float(v)
            if key in hedged:
                assert v == 1.0, (key, v)
                tmpl_of[key] = t
                v = 0.5
            vals[t].append(v)
    assert seen == hedged, sorted(hedged - seen)
    print(label, "calls", len(hedged), "on template items", len(tmpl_of), "on setting items", len(hedged) - len(tmpl_of))
    print("  by template", dict(collections.Counter(tmpl_of.values()).most_common()))
    for t in sorted(vals):
        m = sum(vals[t]) / len(vals[t])
        if m < 0.9:
            print("  UNDER", t, round(m, 3), len(vals[t]))
    print("  pass", sum(1 for t in vals if sum(vals[t]) / len(vals[t]) >= 0.9), "of", len(vals))


run("TWO", TWO)
run("ALL", TWO | NEAR)
