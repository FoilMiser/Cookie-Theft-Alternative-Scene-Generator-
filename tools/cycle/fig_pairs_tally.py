"""(v0.52's own script, with fig_pairs.py: its paths are written in.)
fig_pairs_tally.py ROUND... : for each pair sheet of a round, which drawing was row a, which row the reviewer chose and how sure, and the
figures given to each drawing, read from the review's own parts 2 and 4."""
import json, re, sys
ROOT = "E:/Cognitive_Test_Scene_Creator/"
tot_all = {}
for rnd in sys.argv[1:]:
    m = json.load(open(ROOT + "tpdb_work/v052/maps/%s_map.json" % rnd))
    tot = {"O": 0, "B": 0, "none": 0}
    chose = {"O": 0, "B": 0}
    by_set = {}
    for i in sorted(m, key=int):
        t = open(ROOT + "vision/isolation_v052/%s/review_%s.md" % (rnd, i), encoding="utf-8").read()
        k2 = re.search(r"^#+\s*2\b.*$", t, re.M)
        k3 = re.search(r"^#+\s*3\b.*$", t, re.M)
        k4 = re.search(r"^#+\s*4\b.*$", t, re.M)
        sec2 = t[k2.end():k3.start()]
        sec4 = t[k4.end():]
        figs = []
        for line in sec2.splitlines():
            s = line.strip()
            if s.startswith("|"):
                cells = [c.strip().lower().replace("*", "") for c in s.strip("|").split("|")]
                if len(cells) >= 2 and cells[1] in ("a", "b", "no difference"):
                    figs.append(cells[1])
                continue
            if not re.match(r"^(\d+\.|-|\*)\s", s):
                continue
            body = s.split(":", 1)[1] if ":" in s else s
            mm = re.search(r"\b(no difference|a|b)\b", body.replace("*", "").strip().lower()[:40])
            if mm:
                figs.append(mm.group(1))
        figs = figs[:4]
        c4 = re.search(r"\brow\s+([ab])\b", sec4.replace("*", "").lower())
        sure = re.search(r"(fairly sure|toss-up|toss up|\bsure\b)", sec4.lower())
        row = c4.group(1)
        pick = m[i][row]
        chose[pick] += 1
        n = {"O": 0, "B": 0, "none": 0}
        for f in figs:
            n[m[i][f] if f in "ab" else "none"] += 1
        for k in n:
            tot[k] += n[k]
        by_set.setdefault(m[i]["set"], []).append((m[i]["a"], pick))
        print("%s %2s %-12s a=%s chose row %s = %s (%s); figures new %d, v0.51 %d, neither %d%s" % (
            rnd, i, m[i]["set"], m[i]["a"], row, pick, sure.group(1) if sure else "?", n["B"], n["O"], n["none"], "" if len(figs) == 4 else "  <-- parsed %d figures" % len(figs)))
    print(rnd, "chose", chose, "figures", tot)
    for s, v in sorted(by_set.items()):
        print("   ", s, ["row a %s -> chose %s" % x for x in sorted(v)])
