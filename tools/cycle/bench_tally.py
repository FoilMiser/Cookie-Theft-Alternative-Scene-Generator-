"""(v0.53's own script, kept in tools/cycle as a model: its paths and patterns are written in. Edit them.)
bench_tally.py [lines] : count v0.53's whole-scene bench (vision/isolation_v053/who, map tpdb_work/v053/maps/who_map.json).
Who: by who_cmp.py's rule, the first word for a person in the first inventory line that names the woman in purple's purple.
Wheel: is the barrow's wheel called square, and where: in the free description or the inventory (said), or only in the unsure section."""
import collections, json, os, re, sys
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP = "vision/isolation_v053/who", "tpdb_work/v053/maps/who_map.json"
rows = json.load(open(MAP))
WORD = re.compile(r"\b(young woman|woman|lady|girl|teenager|teen|boy|young man|man|child|kid|person|adult|mother|mom)\b")
YOUNG = {"girl", "boy", "teenager", "teen", "child", "kid"}
show = len(sys.argv) > 1
tot, young, none = collections.Counter(), collections.Counter(), collections.Counter()
lines_ = []
for r in sorted(rows, key=lambda r: (r["bench"], r["arm"], r["pick"])):
    dp = f"{OUT}/desc_{r['pic']}.md"
    if not os.path.exists(dp):
        print("no description:", r["pic"], "reader", r["reader"]); continue
    s = open(dp, encoding="utf-8").read()
    low = s.lower()
    i_inv, i_uns = low.find("inventory"), low.find("unsure")
    if r["bench"] == "who":
        inv = s[i_inv:i_uns if i_uns > i_inv else len(s)]
        ls = [l.strip() for l in inv.splitlines() if re.search(r"purple", l, re.I) and WORD.search(l.lower())]
        tot[r["arm"]] += 1
        if not ls:
            none[r["arm"]] += 1
            lines_.append((r["arm"], r["pick"], r["pic"], "rd%d" % r["reader"], "NO LINE", ""))
            continue
        w = WORD.findall(ls[0].lower())
        y = w[0] in YOUNG
        young[r["arm"]] += y
        lines_.append((r["arm"], r["pick"], r["pic"], "rd%d" % r["reader"], "YOUNG" if y else "grown", ls[0][:170]))
print("WHO (young first of readings):")
for arm in ("O", "FC", "FL"):
    print("  ", arm, young[arm], "of", tot[arm], ("(no line %d)" % none[arm]) if none[arm] else "")
if show:
    for l in lines_:
        print("   " + " | ".join(l))
print("WHEEL:")
by_arm = collections.defaultdict(list)
by_reader = collections.defaultdict(list)
for r in sorted(rows, key=lambda r: (r["arm"], r["reader"], r["pick"])):
    if r["bench"] != "wheel":
        continue
    dp = f"{OUT}/desc_{r['pic']}.md"
    if not os.path.exists(dp):
        print("no description:", r["pic"], "reader", r["reader"]); continue
    s = open(dp, encoding="utf-8").read()
    low = s.lower()
    i_uns = low.find("unsure")
    head, tail = (low[:i_uns], low[i_uns:]) if i_uns > 0 else (low, "")
    sq = re.compile(r"square|squar|cube|box-shaped|rectang|not round|isn't round|is not round")
    in_head = any(sq.search(l) and re.search(r"wheel", l) for l in re.split(r"(?<=[.!?])\s+|\n", head))
    in_tail = any(sq.search(l) and re.search(r"wheel", l) for l in re.split(r"(?<=[.!?])\s+|\n", tail))
    verdict = "SAID" if in_head else ("unsure only" if in_tail else "NOT NAMED")
    by_arm[r["arm"]].append(verdict)
    by_reader[(r["arm"], r["reader"])].append(verdict)
    print("  ", r["arm"], r["pick"], r["pic"], "rd%d" % r["reader"], verdict)
    if show:
        for l in re.split(r"(?<=[.!?])\s+|\n", s):
            if re.search(r"wheel|barrow", l, re.I):
                print("        ", l.strip()[:230])
for arm, v in by_arm.items():
    c = collections.Counter(v)
    print("  ", arm, dict(c), "of", len(v))
for (arm, rd), v in sorted(by_reader.items()):
    print("   reader", rd, arm, v)
