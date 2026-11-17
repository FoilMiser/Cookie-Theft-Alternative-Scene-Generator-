"""strict_count.py : the gate again with the full marks the scorers themselves listed as judgement calls halved (from v0.41; the scorers are
asked for the list from v0.47). Fill TWO (the target beside another reading) and NEAR (a near word, or a target partly said) by hand from the
scores_summary files of the release; the lists below are v0.56's (33 and 46). Prints the templates that would fall under 0.9 with TWO
halved, and with both halved. Run after the swap and vision/gate.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections, json, os
os.chdir(ROOT)
TWO = {
    # scorer a (three are the fish in the tree, impossible beside a toy, an ornament or a kite shaped like a fish)
    ("pic_02", "i04"), ("pic_12", "i02"), ("pic_04", "i04"), ("pic_09", "i03"), ("pic_10", "i02"), ("pic_13", "i05"), ("pic_01", "i03"), ("pic_13", "i04"), ("pic_17", "i07"), ("pic_17", "i03"), ("pic_18", "i04"), ("pic_18", "i05"), ("pic_22", "i03"), ("pic_24", "i02"), ("pic_24", "i03"),
    # scorer b
    ("pic_42", "i06"), ("pic_50", "i03"), ("pic_46", "i02"), ("pic_29", "i01"),
    # scorer c
    ("pic_63", "i04"),
    # scorer d (pic_92 i01: the grandfather reads a newspaper, and whether he sits squarely on the seesaw's seat is asked)
    ("pic_78", "i03"), ("pic_80", "i04"), ("pic_82", "i03"), ("pic_89", "i03"), ("pic_89", "i14"), ("pic_92", "i01"), ("pic_96", "i03"), ("pic_97", "i03"),
    # scorer e
    ("pic_102", "i02"), ("pic_106", "i07"), ("pic_110", "i03"), ("pic_116", "i02"), ("pic_119", "i09")}
NEAR = {
    # scorer a (six are the teenager called a boy; pic_16 i10 is the man who sits on nothing, noticed only among the unsure things. This
    #  scorer also listed seven marks of an older or elderly woman or man for a grandparent, which v0.55's count left out as the key's own
    #  names: not counted)
    ("pic_16", "i10"), ("pic_04", "i14"), ("pic_06", "i02"), ("pic_10", "i04"), ("pic_16", "i17"), ("pic_17", "i01"), ("pic_22", "i04"),
    # scorer b (a man called a boy twice, a woman called a woman or an older girl)
    ("pic_40", "i04"), ("pic_42", "i01"), ("pic_34", "i01"),
    # scorer c (pic_73 i03 and i04 are the wheelbarrow's square wheel said only among the unsure things)
    ("pic_53", "i06"), ("pic_57", "i02"), ("pic_57", "i04"), ("pic_60", "i04"), ("pic_73", "i03"), ("pic_73", "i04"), ("pic_74", "i03"),
    # scorer d (eight are the teenager called a boy, one a man called a boy. This scorer also listed nine grandparents called an older
    #  man or woman, a lead for the leash and two puppies for the dog: not counted)
    ("pic_80", "i01"), ("pic_81", "i02"), ("pic_85", "i02"), ("pic_86", "i03"), ("pic_88", "i02"), ("pic_89", "i04"), ("pic_89", "i10"), ("pic_90", "i01"), ("pic_94", "i07"), ("pic_97", "i04"), ("pic_99", "i03"),
    # scorer e (four are the teenager called a boy, eight a grown figure called a boy or a girl or given beside one, two a bird box for
    #  the bird feeder; pic_114 i02 is the frying pan noticed only among the unsure things)
    ("pic_106", "i01"), ("pic_106", "i05"), ("pic_107", "i02"), ("pic_107", "i06"), ("pic_108", "i04"), ("pic_109", "i01"), ("pic_110", "i05"), ("pic_111", "i02"), ("pic_112", "i01"), ("pic_112", "i05"), ("pic_114", "i01"), ("pic_114", "i02"), ("pic_115", "i01"), ("pic_117", "i02"), ("pic_118", "i03"), ("pic_119", "i02"), ("pic_119", "i03"), ("pic_119", "i16")}
assert len(TWO) == 33 and len(NEAR) == 46 and not (TWO & NEAR), (len(TWO), len(NEAR), TWO & NEAR)
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
