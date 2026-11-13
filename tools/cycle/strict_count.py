"""strict_count.py : the gate again with the full marks the scorers themselves listed as judgement calls halved (from v0.41; the scorers are
asked for the list from v0.47). Fill TWO (the target beside another reading) and NEAR (a near word, or a target partly said) by hand from the
scores_summary files of the release; the lists below are v0.51's (44 and 51). Prints the templates that would fall under 0.9 with TWO
halved, and with both halved. Run after the swap and vision/gate.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections, json, os
os.chdir(ROOT)
TWO = {
    # scorer a
    ("pic_01", "i01"), ("pic_02", "i06"), ("pic_06", "i02"), ("pic_06", "i03"), ("pic_10", "i02"), ("pic_13", "i03"), ("pic_14", "i04"),
    ("pic_21", "i01"), ("pic_22", "i04"), ("pic_25", "i01"),
    # scorer b
    ("pic_28", "i04"), ("pic_29", "i03"), ("pic_30", "i07"), ("pic_32", "i02"), ("pic_32", "i03"), ("pic_33", "i02"), ("pic_33", "i03"),
    ("pic_34", "i02"), ("pic_38", "i03"), ("pic_40", "i05"), ("pic_41", "i03"), ("pic_46", "i02"), ("pic_49", "i02"),
    # scorer c
    ("pic_52", "i01"), ("pic_53", "i08"), ("pic_55", "i02"), ("pic_57", "i04"), ("pic_59", "i04"), ("pic_64", "i02"), ("pic_65", "i05"),
    ("pic_66", "i06"), ("pic_69", "i06"), ("pic_72", "i03"), ("pic_73", "i17"), ("pic_73", "i18"), ("pic_75", "i04"), ("pic_77", "i01"),
    # scorer d (pic_88 i04, listed under both kinds, is here)
    ("pic_78", "i02"), ("pic_78", "i06"), ("pic_82", "i03"), ("pic_88", "i04"), ("pic_89", "i06"), ("pic_97", "i03"), ("pic_97", "i09")}
NEAR = {
    # scorer a (a square wheel named only in the unsure section, twice two items, is here: the target partly said)
    ("pic_02", "i07"), ("pic_02", "i09"), ("pic_03", "i03"), ("pic_07", "i03"), ("pic_08", "i02"), ("pic_09", "i07"), ("pic_09", "i08"),
    ("pic_11", "i04"), ("pic_11", "i05"), ("pic_19", "i06"), ("pic_19", "i08"), ("pic_23", "i01"),
    # scorer b
    ("pic_30", "i08"), ("pic_30", "i11"), ("pic_35", "i03"), ("pic_42", "i08"), ("pic_44", "i03"), ("pic_51", "i03"),
    # scorer c (this scorer did not list the teenager called a boy)
    ("pic_62", "i05"), ("pic_63", "i01"), ("pic_65", "i08"), ("pic_73", "i12"),
    # scorer d (the first nineteen are words for a person: the teenager a boy eight times, a man a boy, a woman a young woman or a teenage girl, the grandparents an older man or woman nine times)
    ("pic_79", "i03"), ("pic_84", "i05"), ("pic_85", "i04"), ("pic_89", "i04"), ("pic_90", "i05"), ("pic_93", "i03"), ("pic_97", "i04"),
    ("pic_99", "i02"), ("pic_87", "i02"), ("pic_98", "i03"), ("pic_81", "i02"), ("pic_91", "i01"), ("pic_93", "i01"), ("pic_95", "i01"),
    ("pic_96", "i01"), ("pic_97", "i01"), ("pic_100", "i04"), ("pic_100", "i05"), ("pic_101", "i01"), ("pic_78", "i04"), ("pic_83", "i03"),
    ("pic_96", "i03"), ("pic_97", "i13"), ("pic_97", "i19"), ("pic_102", "i06"), ("pic_102", "i07"), ("pic_81", "i07"), ("pic_87", "i06"),
    ("pic_100", "i13")}
assert len(TWO) == 44 and len(NEAR) == 51 and not (TWO & NEAR), (len(TWO), len(NEAR), TWO & NEAR)
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
