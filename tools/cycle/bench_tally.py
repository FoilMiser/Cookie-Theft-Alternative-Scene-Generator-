"""(v0.54's own script, kept in tools/cycle as a model: its paths and patterns are written in. Edit them.)
bench_tally.py [lines] : count v0.54's whole-scene bench (vision/isolation_v054/bench, map tpdb_work/v054/maps/bench_map.json).
Read: by who_cmp.py's rule, the first word for a person in the first inventory line that names the man in the red shirt's red top.
Bike, barrow: is the wheel called square, and where: in the free description or the inventory (said), or only in the unsure section; and
every sentence that offers another reading of the square (a crate, a grate, a frame, a box, a window)."""
import collections, json, os, re, sys
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP = "vision/isolation_v054/bench", "tpdb_work/v054/maps/bench_map.json"
rows = json.load(open(MAP))
WORD = re.compile(r"\b(young woman|woman|lady|girl|teenager|teen|boy|young man|man|child|kid|person|adult|father|dad|guy)\b")
YOUNG = {"girl", "boy", "teenager", "teen", "child", "kid"}
RED = re.compile(r"red (t-?shirt|shirt|top|tee|short-sleeved|jumper|sweater)|red-shirt", re.I)
show = len(sys.argv) > 1
SENT = r"(?<=[.!?])\s+|\n"
print("READ (the man in the red shirt, young first of readings):")
tot, young, none = collections.Counter(), collections.Counter(), collections.Counter()
by_reader = collections.defaultdict(list)
lines_ = []
for r in sorted(rows, key=lambda r: (r["bench"], r["arm"], r["pick"], r["reader"])):
    if r["bench"] != "read":
        continue
    dp = f"{OUT}/desc_{r['pic']}.md"
    if not os.path.exists(dp):
        print("no description:", r["pic"], "reader", r["reader"]); continue
    s = open(dp, encoding="utf-8").read()
    low = s.lower()
    i_inv, i_uns = low.find("inventory"), low.rfind("unsure")
    inv = s[i_inv:i_uns if i_uns > i_inv else len(s)]
    ls = [l.strip() for l in inv.splitlines() if RED.search(l) and WORD.search(l.lower())]
    tot[r["arm"]] += 1
    if not ls:
        none[r["arm"]] += 1
        by_reader[(r["arm"], r["reader"])].append("?")
        lines_.append((r["arm"], r["pick"], r["pic"], "rd%d" % r["reader"], "NO LINE", ""))
        continue
    w = WORD.findall(ls[0].lower())
    y = w[0] in YOUNG
    young[r["arm"]] += y
    by_reader[(r["arm"], r["reader"])].append(w[0])
    must = bool(re.search(r"moustache|mustache", ls[0], re.I))
    lines_.append((r["arm"], r["pick"], r["pic"], "rd%d" % r["reader"], ("YOUNG" if y else "grown") + (" +moustache" if must else ""), ls[0][:150]))
for arm in ("O", "B"):
    print("  ", arm, young[arm], "of", tot[arm], ("(no line %d)" % none[arm]) if none[arm] else "")
for (arm, rd), v in sorted(by_reader.items()):
    print("   reader", rd, arm, v)
for l in lines_:
    print("   " + " | ".join(l) if show else "   " + " | ".join(l[:5]))
sq = re.compile(r"square|squar|cube|box-shaped|rectang|not round|isn't round|is not round|aren't round|are not round")
other = re.compile(r"crate|grate|grating|frame|window|box\b|boxes|cage|panel|grid")
for bench in ("bike", "barrow"):
    print(bench.upper() + ":")
    by_arm = collections.defaultdict(list)
    by_reader = collections.defaultdict(list)
    alt = collections.defaultdict(list)
    for r in sorted(rows, key=lambda r: (r["arm"], r["reader"], r["pick"])):
        if r["bench"] != bench:
            continue
        dp = f"{OUT}/desc_{r['pic']}.md"
        if not os.path.exists(dp):
            print("no description:", r["pic"], "reader", r["reader"]); continue
        s = open(dp, encoding="utf-8").read()
        low = s.lower()
        i_uns = low.rfind("unsure")
        head, tail = (low[:i_uns], low[i_uns:]) if i_uns > 0 else (low, "")
        in_head = any(sq.search(l) and re.search(r"wheel", l) for l in re.split(SENT, head))
        in_tail = any(sq.search(l) and re.search(r"wheel", l) for l in re.split(SENT, tail))
        verdict = "SAID" if in_head else ("unsure only" if in_tail else "NOT NAMED")
        by_arm[r["arm"]].append(verdict)
        by_reader[(r["arm"], r["reader"])].append(verdict)
        print("  ", r["arm"], r["pick"], r["pic"], "rd%d" % r["reader"], verdict)
        for l in re.split(SENT, s):
            ll = l.lower()
            if re.search(r"wheel|barrow|bicycle|bike", ll) and other.search(ll):
                alt[r["arm"]].append((r["pick"], r["pic"], "rd%d" % r["reader"], l.strip()[:260]))
            if show and re.search(r"wheel|barrow|bicycle|bike", ll):
                print("        ", l.strip()[:230])
    for arm, v in sorted(by_arm.items()):
        print("  ", arm, dict(collections.Counter(v)), "of", len(v))
    for (arm, rd), v in sorted(by_reader.items()):
        print("   reader", rd, arm, v)
    for arm, v in sorted(alt.items()):
        print("   other readings,", arm, len(v), "sentences in", len({x[1] for x in v}), "descriptions:")
        for x in v:
            print("      ", " | ".join(x))
