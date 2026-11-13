"""strict_count.py : the gate again with the full marks the scorers themselves listed as judgement calls halved (from v0.41; the scorers are
asked for the list from v0.47). Fill TWO (the target beside another reading) and NEAR (a near word, or a target partly said) by hand from the
scores_summary files of the release; the lists below are v0.53's (32 and 47). Prints the templates that would fall under 0.9 with TWO
halved, and with both halved. Run after the swap and vision/gate.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections, json, os
os.chdir(ROOT)
TWO = {
    # scorer a
    ("pic_01", "i03"), ("pic_02", "i02"), ("pic_03", "i03"), ("pic_04", "i03"), ("pic_06", "i03"), ("pic_08", "i04"), ("pic_11", "i04"),
    ("pic_15", "i07"), ("pic_15", "i16"), ("pic_22", "i04"),
    # scorer b (pic_35 i01 is here: who threw the ball, and the teenager a boy as well)
    ("pic_26", "i04"), ("pic_29", "i04"), ("pic_30", "i02"), ("pic_30", "i03"), ("pic_31", "i01"), ("pic_32", "i05"), ("pic_35", "i01"),
    ("pic_47", "i05"),
    # scorer c (pic_68 i07 is a wheelbarrow's square wheel beside "a separate square object")
    ("pic_58", "i09"), ("pic_58", "i11"), ("pic_60", "i04"), ("pic_64", "i03"), ("pic_68", "i07"), ("pic_70", "i03"), ("pic_72", "i02"),
    ("pic_75", "i06"),
    # scorer d
    ("pic_78", "i04"), ("pic_82", "i04"), ("pic_85", "i04"), ("pic_86", "i02"), ("pic_87", "i04"), ("pic_97", "i02")}
NEAR = {
    # scorer a (the last five are the teenager called a boy)
    ("pic_05", "i03"), ("pic_15", "i11"), ("pic_20", "i04"), ("pic_21", "i03"), ("pic_21", "i06"), ("pic_08", "i06"), ("pic_12", "i05"),
    ("pic_14", "i03"), ("pic_15", "i19"), ("pic_20", "i05"),
    # scorer b (a woman called a girl and a man a boy in pic_29; the bird feeder a bird box three times; the last six the teenager a boy)
    ("pic_29", "i01"), ("pic_29", "i05"), ("pic_37", "i09"), ("pic_33", "i05"), ("pic_34", "i06"), ("pic_38", "i11"), ("pic_34", "i02"),
    ("pic_36", "i02"), ("pic_37", "i04"), ("pic_39", "i04"), ("pic_46", "i02"), ("pic_49", "i03"),
    # scorer c (the man in the red shirt a boy in pic_60 and pic_67)
    ("pic_51", "i04"), ("pic_52", "i02"), ("pic_60", "i05"), ("pic_60", "i12"), ("pic_61", "i03"), ("pic_63", "i16"), ("pic_67", "i01"),
    ("pic_67", "i02"), ("pic_75", "i02"),
    # scorer d (the last eight are the teenager called a boy. This scorer also listed seven items where a grandparent is "an older man" or
    #  "an older woman": those are the key's own accepted names and are not counted: pic_83 i11, pic_94 i01, pic_96 i01, pic_78 i09,
    #  pic_86 i06, pic_89 i09, pic_97 i01)
    ("pic_78", "i08"), ("pic_83", "i01"), ("pic_83", "i03"), ("pic_88", "i03"), ("pic_88", "i07"), ("pic_89", "i05"), ("pic_94", "i03"),
    ("pic_98", "i01"), ("pic_77", "i03"), ("pic_79", "i01"), ("pic_82", "i01"), ("pic_87", "i01"), ("pic_88", "i05"), ("pic_89", "i02"),
    ("pic_91", "i02"), ("pic_97", "i14")}
assert len(TWO) == 32 and len(NEAR) == 47 and not (TWO & NEAR), (len(TWO), len(NEAR), TWO & NEAR)
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
