"""strict_count.py : the gate again with the full marks the scorers themselves listed as judgement calls halved (from v0.41; the scorers are
asked for the list from v0.47). Fill TWO (the target beside another reading) and NEAR (a near word, or a target partly said) by hand from the
scores_summary files of the release; the lists below are v0.50's (33 and 49). Prints the templates that would fall under 0.9 with TWO
halved, and with both halved. Run after the swap and vision/gate.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections, json, os
os.chdir(ROOT)
TWO = {
    # scorer a
    ("pic_02", "i01"), ("pic_02", "i04"), ("pic_06", "i12"), ("pic_09", "i04"), ("pic_10", "i11"), ("pic_14", "i03"), ("pic_15", "i07"),
    ("pic_16", "i04"), ("pic_17", "i08"),
    # scorer b
    ("pic_24", "i05"), ("pic_25", "i02"), ("pic_27", "i01"), ("pic_30", "i04"), ("pic_34", "i06"), ("pic_38", "i04"), ("pic_38", "i12"),
    ("pic_42", "i03"), ("pic_44", "i01"),
    # scorer c
    ("pic_48", "i02"), ("pic_48", "i06"), ("pic_50", "i03"), ("pic_52", "i03"), ("pic_53", "i03"), ("pic_54", "i03"), ("pic_56", "i03"),
    ("pic_59", "i13"), ("pic_63", "i03"),
    # scorer d
    ("pic_70", "i02"), ("pic_71", "i02"), ("pic_72", "i02"), ("pic_77", "i03"), ("pic_83", "i02"), ("pic_90", "i03")}
NEAR = {
    # scorer a (the last nine are the teenager called a boy, which the scorer listed as one line for ten pictures; pic_02's is in TWO)
    ("pic_04", "i09"), ("pic_04", "i13"), ("pic_14", "i10"), ("pic_18", "i02"),
    ("pic_03", "i03"), ("pic_04", "i04"), ("pic_07", "i07"), ("pic_10", "i19"), ("pic_14", "i19"), ("pic_15", "i06"), ("pic_16", "i02"),
    ("pic_18", "i05"), ("pic_21", "i01"),
    # scorer b (pic_44 i01, listed under both kinds, is in TWO)
    ("pic_25", "i01"), ("pic_31", "i01"), ("pic_33", "i05"), ("pic_38", "i14"), ("pic_38", "i15"), ("pic_32", "i01"), ("pic_33", "i04"),
    ("pic_37", "i02"), ("pic_38", "i05"), ("pic_40", "i03"), ("pic_41", "i01"), ("pic_42", "i04"), ("pic_43", "i06"), ("pic_27", "i03"),
    ("pic_34", "i09"), ("pic_38", "i10"), ("pic_38", "i20"),
    # scorer c
    ("pic_47", "i01"), ("pic_59", "i06"), ("pic_59", "i09"),
    # scorer d
    ("pic_69", "i03"), ("pic_89", "i02"), ("pic_80", "i01"), ("pic_81", "i01"), ("pic_82", "i05"), ("pic_83", "i03"), ("pic_88", "i01"),
    ("pic_90", "i04"), ("pic_75", "i01"), ("pic_77", "i04"), ("pic_81", "i02"), ("pic_84", "i05"), ("pic_77", "i05"), ("pic_84", "i04"),
    ("pic_90", "i09"), ("pic_72", "i05")}
assert len(TWO) == 33 and len(NEAR) == 49 and not (TWO & NEAR), (len(TWO), len(NEAR), TWO & NEAR)
km = json.load(open(f"vision/v{TAG}/key_map.json"))
sc = json.load(open(f"vision/v{TAG}/scores.json", encoding="utf-8"))


def run(label, hedged):
    vals, tmpl_of, seen = collections.defaultdict(list), {}, set()
    for pic, name in km.items():
        f = next(p for p in (f"scenes/{name}.json", f"probes/{name}.json") if os.path.exists(p))
        r = json.load(open(f))
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
