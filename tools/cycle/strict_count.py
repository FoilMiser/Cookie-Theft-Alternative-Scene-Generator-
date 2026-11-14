"""strict_count.py : the gate again with the full marks the scorers themselves listed as judgement calls halved (from v0.41; the scorers are
asked for the list from v0.47). Fill TWO (the target beside another reading) and NEAR (a near word, or a target partly said) by hand from the
scores_summary files of the release; the lists below are v0.55's (48 and 37). Prints the templates that would fall under 0.9 with TWO
halved, and with both halved. Run after the swap and vision/gate.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections, json, os
os.chdir(ROOT)
TWO = {
    # scorer a (pic_07 i01 and pic_13 i01: the grandfather on the seesaw's low end beside "sitting on the ground in front of the seesaw end")
    ("pic_02", "i02"), ("pic_03", "i01"), ("pic_03", "i03"), ("pic_07", "i01"), ("pic_13", "i01"), ("pic_08", "i04"), ("pic_08", "i07"),
    ("pic_11", "i04"), ("pic_15", "i07"), ("pic_21", "i06"), ("pic_22", "i04"), ("pic_22", "i08"),
    # scorer b (pic_49 i03 is here: pointing at the sky beside another reading, and the teenager a boy as well)
    ("pic_27", "i03"), ("pic_38", "i03"), ("pic_38", "i04"), ("pic_46", "i03"), ("pic_46", "i04"), ("pic_29", "i02"), ("pic_29", "i04"),
    ("pic_37", "i07"), ("pic_37", "i03"), ("pic_38", "i07"), ("pic_32", "i03"), ("pic_47", "i04"), ("pic_49", "i03"),
    # scorer c
    ("pic_52", "i01"), ("pic_53", "i02"), ("pic_58", "i09"), ("pic_60", "i04"), ("pic_60", "i11"), ("pic_64", "i03"), ("pic_67", "i04"),
    ("pic_68", "i03"), ("pic_70", "i03"), ("pic_72", "i02"), ("pic_73", "i07"), ("pic_75", "i08"),
    # scorer d
    ("pic_78", "i04"), ("pic_80", "i03"), ("pic_81", "i03"), ("pic_82", "i04"), ("pic_87", "i04"), ("pic_86", "i02"), ("pic_86", "i05"),
    ("pic_89", "i07"), ("pic_98", "i03"), ("pic_90", "i01"), ("pic_97", "i18")}
NEAR = {
    # scorer a (the woman in the yellow dress a girl in pic_11; four are the teenager called a boy)
    ("pic_05", "i03"), ("pic_18", "i03"), ("pic_08", "i06"), ("pic_12", "i05"), ("pic_14", "i03"), ("pic_15", "i19"), ("pic_11", "i05"),
    ("pic_15", "i16"),
    # scorer b (six are the teenager called a boy, three a bird box for the birdhouse. This scorer also listed pic_38 i12, a fence named
    #  as a gate, which is the key's own accepted phrasing, and three marks of an older man for the grandfather: not counted)
    ("pic_37", "i13"), ("pic_41", "i07"), ("pic_42", "i05"), ("pic_30", "i03"), ("pic_34", "i02"), ("pic_35", "i01"), ("pic_36", "i02"),
    ("pic_37", "i04"), ("pic_39", "i04"), ("pic_46", "i02"), ("pic_33", "i05"), ("pic_34", "i06"), ("pic_38", "i11"), ("pic_31", "i01"),
    ("pic_34", "i01"),
    # scorer c (the man in the red shirt a boy in pic_67; pic_51 i03 is the thief bird said only among the unsure things)
    ("pic_51", "i03"), ("pic_67", "i02"),
    # scorer d (the woman in purple a girl or young woman in pic_87; seven are the teenager called a boy. This scorer also listed eight
    #  marks of an older woman or man for a grandparent: not counted)
    ("pic_77", "i03"), ("pic_79", "i01"), ("pic_82", "i01"), ("pic_87", "i01"), ("pic_88", "i05"), ("pic_89", "i02"), ("pic_97", "i14"),
    ("pic_87", "i05"), ("pic_78", "i08"), ("pic_83", "i03"), ("pic_89", "i05"), ("pic_96", "i03")}
assert len(TWO) == 48 and len(NEAR) == 37 and not (TWO & NEAR), (len(TWO), len(NEAR), TWO & NEAR)
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
