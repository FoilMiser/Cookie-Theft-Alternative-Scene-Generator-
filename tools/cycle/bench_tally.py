"""(v0.56's own script: its rows and paths are written in.)
bench_tally.py [ROW ...] : v0.56's whole-picture bench. For every row of the list (default: all) writes tpdb_work/v056/bench/tally_<row>.txt:
for each reading of a picture that serves the row, by arm (O as v0.55 screened it, B the trial cast and v0.56's drawings, C the
alternatives, L the bicycle leaning on its post alone, F a picture built for the bench under revision 50), the sentences of the free
description, the inventory lines and the lines of the unsure section that hold one of the row's words. And prints how many readings each
row has in each arm. The reading itself is done from those files: nothing is counted here."""
import collections, json, os, re, sys
ROOT = "E:/Cognitive_Test_Scene_Creator/"
rows = json.load(open(ROOT + "tpdb_work/v056/maps/bench_map.json"))
WORDS = {
    "bike": r"bicycle|bike|wheel|post|stand", "barrow": r"wheelbarrow|barrow|cart|wheel|crate|grate", "bird": r"sandwich|bird|bench|bread|slice",
    "hose": r"hose|nozzle|tap|reel|drip|drop|water|dog|kink|blocked", "seesaw_heavy": r"see-?saw|teeter|plank|stuck|heavy", "seesaw_play": r"see-?saw|teeter|plank",
    "lead": r"lead|leash|dog|door|walk", "cat": r"\bcat\b|kitten|bird|stalk|creep|crouch|pounce", "sleep": r"dog|puppy|asleep|sleep|lying|hose",
    "parcel": r"box|parcel|package|sprinkler|delivery|soak|wet", "kite": r"kite|string|tree", "upward": r"watering can|water|upward|upwards|spray",
    "box": r"box|crate|float|hover|thrown|wave", "trail": r"ball|throw|catch|string|yo-?yo", "paint": r"paint|roller|fence|tray|tin|paw|print|pink|blue",
    "plant": r"plant|seedling|kneel|trowel|dig|flower|tray", "bread": r"bread|duck|feed|throw|toss|bag", "feed": r"feed|bird|bag|seed|crumb|sack",
    "point": r"point|cloud|rain|storm|sky", "cone": r"ice[- ]cream|cone|cry|crying|dropped|scoop|splat", "swing": r"swing|rope|chain",
    "hang": r"washing|laundry|clothes|line|peg|hang", "pan": r"\bpan\b|pot|saucepan|frying|watering", "lostcol": r"balloon",
    "picnic": r"picnic|blanket|basket", "trip": r"trip|book|read|box|stumbl|step", "pond": r"pond|water's edge|bank|shore|wading|in the water",
    "ladder": r"ladder", "skirt": r"skirt|dress|shorts",
}
want = sys.argv[1:] or sorted(WORDS)
cnt = collections.Counter()
for row in want:
    pat = re.compile(WORDS[row], re.I)
    out = []
    mine = [r for r in rows if row in r["rows"]]
    for r in sorted(mine, key=lambda r: (r["name"], "OBCLF".index(r["arm"]), r["reader"])):
        f = ROOT + "vision/isolation_v056/bench/desc_%s.md" % r["pic"]
        if not os.path.exists(f):
            out.append("== %s arm %s reader %d (%s): NO DESCRIPTION" % (r["name"], r["arm"], r["reader"], r["pic"]))
            continue
        t = open(f, encoding="utf-8").read()
        mu = re.search(r"(?im)^#*\s*\W*\d?\W*\s*\**\s*unsure", t)
        mi = re.search(r"(?im)^#*\s*\W*\d?\W*\s*\**\s*inventory", t)
        free = t[:mi.start()] if mi else t
        inv = t[mi.end():mu.start()] if (mi and mu and mu.start() > mi.end()) else ""
        uns = t[mu.end():] if mu else ""
        cnt[(row, r["arm"])] += 1
        out.append("== %s arm %s reader %d (%s)" % (r["name"], r["arm"], r["reader"], r["pic"]))
        for s in re.split(r"(?<=[.!?])\s+", " ".join(l.strip() for l in free.splitlines() if l.strip() and not l.lstrip().startswith("#"))):
            if pat.search(s):
                out.append("   F: " + s.strip()[:400])
        for l in inv.splitlines():
            if pat.search(l) and l.strip():
                out.append("   I: " + l.strip()[:400])
        for l in uns.splitlines():
            if pat.search(l) and l.strip():
                out.append("   U: " + l.strip()[:400])
    open(ROOT + "tpdb_work/v056/bench/tally_%s.txt" % row, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
for row in want:
    print(row, {a: cnt[(row, a)] for a in "OBCLF" if cnt[(row, a)]})
