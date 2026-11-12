"""strict_count.py : the gate again with the full marks the scorers themselves listed as judgement calls halved (from v0.41; the scorers are
asked for the list from v0.47). Fill TWO (the target beside another reading) and NEAR (a near word, or a target partly said) by hand from the
scores_summary files of the release; the lists below are v0.49's (42 and 44). Prints the templates that would fall under 0.9 with TWO
halved, and with both halved. Run after the swap and vision/gate.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections, json, os
os.chdir(ROOT)
TWO = {
    # scorer a
    ("pic_01", "i04"), ("pic_02", "i02"), ("pic_05", "i01"), ("pic_07", "i02"), ("pic_08", "i01"), ("pic_09", "i01"), ("pic_12", "i02"),
    ("pic_14", "i02"), ("pic_15", "i04"), ("pic_16", "i01"), ("pic_17", "i03"), ("pic_19", "i07"), ("pic_19", "i08"), ("pic_21", "i02"),
    # scorer b
    ("pic_22", "i07"), ("pic_22", "i10"), ("pic_23", "i02"), ("pic_27", "i02"), ("pic_27", "i08"), ("pic_29", "i01"), ("pic_33", "i01"),
    ("pic_38", "i03"), ("pic_39", "i01"), ("pic_40", "i04"),
    # scorer c
    ("pic_44", "i06"), ("pic_46", "i03"), ("pic_48", "i01"), ("pic_48", "i02"), ("pic_49", "i02"), ("pic_49", "i03"), ("pic_53", "i03"),
    ("pic_54", "i02"), ("pic_55", "i08"), ("pic_55", "i11"), ("pic_56", "i01"), ("pic_62", "i02"),
    # scorer d
    ("pic_72", "i03"), ("pic_72", "i05"), ("pic_78", "i02"), ("pic_78", "i04"),
    # scorer e
    ("pic_89", "i02"), ("pic_94", "i06")}
NEAR = {
    # scorer a
    ("pic_01", "i03"), ("pic_05", "i06"), ("pic_11", "i07"), ("pic_11", "i09"), ("pic_15", "i06"),
    # scorer b
    ("pic_27", "i11"), ("pic_36", "i01"), ("pic_37", "i03"), ("pic_40", "i07"),
    # scorer c
    ("pic_43", "i09"), ("pic_44", "i05"), ("pic_47", "i01"), ("pic_49", "i01"), ("pic_52", "i01"), ("pic_53", "i04"), ("pic_54", "i01"),
    ("pic_54", "i05"), ("pic_55", "i09"), ("pic_56", "i02"), ("pic_57", "i05"), ("pic_61", "i08"), ("pic_62", "i09"), ("pic_64", "i02"),
    # scorer d
    ("pic_65", "i03"), ("pic_74", "i03"), ("pic_75", "i05"), ("pic_78", "i10"), ("pic_79", "i01"), ("pic_84", "i04"), ("pic_85", "i08"),
    # scorer e
    ("pic_86", "i01"), ("pic_88", "i08"), ("pic_88", "i09"), ("pic_88", "i12"), ("pic_89", "i01"), ("pic_95", "i01"), ("pic_99", "i01"),
    ("pic_100", "i04"), ("pic_100", "i13"), ("pic_101", "i02"), ("pic_102", "i05"), ("pic_102", "i09"), ("pic_105", "i02"), ("pic_106", "i04")}
assert len(TWO) == 42 and len(NEAR) == 44 and not (TWO & NEAR), (len(TWO), len(NEAR), TWO & NEAR)
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
