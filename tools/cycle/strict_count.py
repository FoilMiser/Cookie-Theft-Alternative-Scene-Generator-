"""strict_count.py : the gate again with the full marks the scorers themselves listed as judgement calls halved (from v0.41; the scorers are
asked for the list from v0.47). Fill TWO (the target beside another reading) and NEAR (a near word, or a target partly said) by hand from the
scores_summary files of the release; the lists below are v0.52's (34 and 33). Prints the templates that would fall under 0.9 with TWO
halved, and with both halved. Run after the swap and vision/gate.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections, json, os
os.chdir(ROOT)
TWO = {
    # scorer a
    ("pic_01", "i01"), ("pic_03", "i02"), ("pic_09", "i11"), ("pic_12", "i07"), ("pic_19", "i06"), ("pic_22", "i01"),
    # scorer b (pic_29 i02 is here: digging or planting, and the teenager a boy as well)
    ("pic_28", "i04"), ("pic_29", "i02"), ("pic_29", "i03"), ("pic_30", "i07"), ("pic_32", "i03"), ("pic_33", "i03"), ("pic_34", "i02"),
    ("pic_34", "i03"), ("pic_38", "i01"), ("pic_40", "i06"), ("pic_41", "i03"), ("pic_42", "i07"), ("pic_44", "i06"), ("pic_48", "i03"),
    ("pic_49", "i04"), ("pic_49", "i07"), ("pic_51", "i04"),
    # scorer c
    ("pic_62", "i04"), ("pic_62", "i06"), ("pic_65", "i03"), ("pic_73", "i16"), ("pic_73", "i17"), ("pic_73", "i18"), ("pic_77", "i01"),
    # scorer d
    ("pic_96", "i02"), ("pic_96", "i03"), ("pic_97", "i06"), ("pic_97", "i09")}
NEAR = {
    # scorer a (a square wheel named only in the unsure section, pic_09 i07, is here: the target partly said)
    ("pic_02", "i04"), ("pic_02", "i13"), ("pic_03", "i01"), ("pic_07", "i03"), ("pic_09", "i07"), ("pic_16", "i05"), ("pic_16", "i06"),
    ("pic_22", "i05"),
    # scorer b (the last 7 are the teenager called a boy, which this scorer named by picture and not by item)
    ("pic_30", "i11"), ("pic_42", "i05"), ("pic_42", "i08"), ("pic_47", "i02"), ("pic_51", "i03"), ("pic_30", "i19"), ("pic_34", "i01"),
    ("pic_35", "i09"), ("pic_36", "i02"), ("pic_41", "i04"), ("pic_42", "i02"), ("pic_49", "i08"),
    # scorer c
    ("pic_53", "i02"), ("pic_56", "i01"), ("pic_62", "i05"), ("pic_62", "i12"), ("pic_63", "i01"), ("pic_71", "i05"), ("pic_73", "i05"),
    ("pic_73", "i08"), ("pic_75", "i01"),
    # scorer d (the last two are a word for a person beside another: a man or older boy, a girl or young woman; v0.51's rule puts a word for a person here)
    ("pic_78", "i04"), ("pic_89", "i06"), ("pic_87", "i02"), ("pic_98", "i03")}
assert len(TWO) == 34 and len(NEAR) == 33 and not (TWO & NEAR), (len(TWO), len(NEAR), TWO & NEAR)
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
