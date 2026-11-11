"""strict_count.py : the gate again with the full marks the scorers themselves listed as judgement calls halved (from v0.41; the scorers are
asked for the list from v0.47). Fill TWO (the target beside another reading) and NEAR (a near word, or a target partly said) by hand from the
four scores_summary files of the release; the lists below are v0.48's (33 and 36). Prints the templates that would fall under 0.9 with TWO
halved, and with both halved. Run after the swap and vision/gate.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections, json, os
os.chdir(ROOT)
TWO = {
    # scorer a
    ("pic_04", "i04"), ("pic_05", "i03"), ("pic_09", "i07"), ("pic_10", "i04"), ("pic_06", "i02"), ("pic_07", "i03"), ("pic_20", "i03"),
    ("pic_13", "i04"), ("pic_19", "i04"), ("pic_15", "i04"), ("pic_15", "i05"), ("pic_22", "i08"), ("pic_22", "i09"), ("pic_17", "i01"),
    # scorer b
    ("pic_25", "i03"), ("pic_29", "i16"), ("pic_29", "i17"), ("pic_40", "i08"), ("pic_40", "i11"),
    # scorer c
    ("pic_45", "i03"), ("pic_50", "i03"), ("pic_59", "i04"),
    # scorer d
    ("pic_74", "i02"), ("pic_74", "i03"), ("pic_84", "i02"), ("pic_78", "i03"), ("pic_79", "i03"), ("pic_81", "i03"), ("pic_68", "i06"),
    ("pic_71", "i07"), ("pic_77", "i04"), ("pic_80", "i03"), ("pic_86", "i04")}
NEAR = {
    # scorer a
    ("pic_02", "i02"), ("pic_11", "i01"), ("pic_01", "i05"), ("pic_04", "i12"), ("pic_07", "i04"), ("pic_12", "i06"), ("pic_13", "i01"),
    ("pic_17", "i08"), ("pic_19", "i05"), ("pic_20", "i01"), ("pic_19", "i20"),
    # scorer b
    ("pic_33", "i08"), ("pic_34", "i01"), ("pic_35", "i02"), ("pic_36", "i04"), ("pic_40", "i01"),
    # scorer c
    ("pic_52", "i02"), ("pic_54", "i01"), ("pic_55", "i01"), ("pic_59", "i06"), ("pic_62", "i02"), ("pic_63", "i05"), ("pic_64", "i02"),
    # scorer d
    ("pic_72", "i02"), ("pic_81", "i05"), ("pic_83", "i01"), ("pic_69", "i03"), ("pic_73", "i02"), ("pic_74", "i04"), ("pic_76", "i09"),
    ("pic_78", "i07"), ("pic_84", "i04"), ("pic_86", "i01"), ("pic_74", "i10"), ("pic_84", "i13"), ("pic_84", "i09")}
assert len(TWO) == 33 and len(NEAR) == 36 and not (TWO & NEAR), (len(TWO), len(NEAR), TWO & NEAR)
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
