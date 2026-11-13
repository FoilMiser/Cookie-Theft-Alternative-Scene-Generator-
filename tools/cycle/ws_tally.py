"""(v0.51's own script, kept in tools/cycle as the model for the next whole-scene bench: its picks, arms and paths are written in. Edit them.)
ws_tally.py [catch|moustache] : the whole-scene bench of v0.51, read back by arm (map tpdb_work/v051/maps/ws_map.json).
catch: every sentence of each description that has the ball, a throw or a catch in it, by picture and arm.
moustache: the first inventory line that names the red shirt: called young first? a moustache in it? (who_cmp.py's rule for the first.)"""
import collections, io, json, os, re, sys
os.chdir("E:/Cognitive_Test_Scene_Creator")
OUT = "vision/isolation_v051/ws"
rows = json.load(open("tpdb_work/v051/maps/ws_map.json"))
what = sys.argv[1] if len(sys.argv) > 1 else "catch"
WORD = re.compile(r"\b(young woman|woman|lady|girl|teenager|teen|boy|young man|man|child|kid|person|adult)\b")
YOUNG = {"girl", "boy", "teenager", "teen", "child", "kid"}
if what == "catch":
    for r in sorted((r for r in rows if r["bench"] == "catch"), key=lambda r: (r["pick"], r["arm"], r["pic"])):
        p = f"{OUT}/desc_{r['pic']}.md"
        if not os.path.exists(p):
            print(r["pick"], r["arm"], r["pic"], "NO DESCRIPTION"); continue
        s = io.open(p, encoding="utf-8").read()
        print(f"=== {r['pick']} arm {r['arm']} ({r['pic']}, reader {r['reader']})")
        for line in s.splitlines():
            for sent in re.split(r"(?<=[.!?])\s+", line):
                if re.search(r"\b(ball|throw|thrown|threw|catch|caught|tossed|toss)\w*", sent, re.I):
                    print("   ", sent.strip()[:420])
else:
    tot, young, mou, none = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
    for r in sorted((r for r in rows if r["bench"] == "moustache"), key=lambda r: (r["arm"], r["pick"])):
        p = f"{OUT}/desc_{r['pic']}.md"
        if not os.path.exists(p):
            print(r["pick"], r["arm"], r["pic"], "NO DESCRIPTION"); continue
        s = io.open(p, encoding="utf-8").read()
        inv = s[s.lower().find("inventory"):]
        ls = [l.strip() for l in inv.splitlines() if re.search(r"red (t-?shirt|shirt|top|tee)", l, re.I)]
        tot[r["arm"]] += 1
        if not ls:
            none[r["arm"]] += 1
            print(r["arm"], r["pick"], r["pic"], "no line"); continue
        w = WORD.findall(ls[0].lower())
        y = bool(w and w[0] in YOUNG)
        m = bool(re.search("moustache|mustache", ls[0], re.I))
        many = bool(re.search("moustache|mustache", s, re.I))
        young[r["arm"]] += y; mou[r["arm"]] += m
        print(r["arm"], r["pick"], r["pic"], "YOUNG" if y else "grown", "MOUSTACHE" if m else ("(moustache elsewhere)" if many else "-"), "|", ls[0][:140])
    for a in sorted(tot):
        print(a, "young first", young[a], "of", tot[a], "| moustache in the line", mou[a], "of", tot[a], "| no line", none[a])
