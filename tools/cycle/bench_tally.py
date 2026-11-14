"""(v0.55's own script: its paths are written in.)
bench_tally.py [pick ...] : v0.55's whole-scene bench. For every pick and arm, each reader's lines on the seated figures: the inventory lines that
name a sitter (sit, seat, swing, seesaw, slide, perch) and the lines of the unsure section that name legs, knees, feet, a seat or a bench, or
something floating. Then the counts by arm: readings that say the figure sits, and readings whose unsure section has a remark on the sitter's
legs, seat or feet."""
import collections, json, re, sys
ROOT = "E:/Cognitive_Test_Scene_Creator/"
rows = json.load(open(ROOT + "tpdb_work/v055/maps/bench_map.json"))
want = set(sys.argv[1:])
SIT = re.compile(r"\b(sit|sits|sitting|seated|sat|perch\w*|swing\w*|seesaw|see-saw|slid\w*|riding)\b", re.I)
LEG = re.compile(r"\b(legs?|knees?|feet|foot|thighs?|shins?|seat|bench|lap|hover\w*|float\w*|mid-?air|slid\w*|squat\w*|crouch\w*|perch\w*|dangl\w*)\b", re.I)
ODD = re.compile(r"\b(legs?|knees?|feet|foot|thighs?|shins?)\b", re.I)
by = collections.defaultdict(list)
for r in rows:
    by[(r["pick"], r["arm"])].append(r)
cnt = collections.Counter()
for (pick, arm) in sorted(by, key=lambda k: (int(k[0][4:]), k[1] != "O")):
    if want and pick not in want:
        continue
    for r in sorted(by[(pick, arm)], key=lambda r: r["reader"]):
        t = open(ROOT + "vision/isolation_v055/bench/desc_%s.md" % r["pic"], encoding="utf-8").read()
        m = re.search(r"(?im)^#+\s*\W*\d?\W*\s*unsure", t) or re.search(r"(?im)^\W*\d?\W*\s*\**unsure", t)
        m2 = re.search(r"(?im)^#+\s*\W*\d?\W*\s*inventory", t) or re.search(r"(?im)^\W*\d?\W*\s*\**inventory", t)
        inv = t[m2.end():m.start()] if (m and m2) else t
        uns = t[m.end():] if m else ""
        sit_lines = [l.strip() for l in inv.splitlines() if SIT.search(l) and l.strip().startswith(("-", "*"))]
        odd_lines = [l.strip() for l in uns.splitlines() if LEG.search(l) and l.strip().startswith(("-", "*"))]
        cnt[(arm, "readings")] += 1
        cnt[(arm, "sits")] += bool(sit_lines)
        cnt[(arm, "leg remark")] += any(ODD.search(l) for l in odd_lines)
        print("== %s %s %s reader %d (%s)" % (pick, r["name"], arm, r["reader"], r["pic"]))
        for l in sit_lines:
            print("   I:", l[:330])
        for l in odd_lines:
            print("   U:", l[:330])
print({k: v for k, v in sorted(cnt.items())})
