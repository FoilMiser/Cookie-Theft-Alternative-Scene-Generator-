"""(v0.58's own script: its rows and paths are written in.)
bench_tally.py [ROW ...] : v0.58's whole-picture bench. For every row (default: all) writes tpdb_work/v058/bench/tally_<row>.txt: for each
reading of a picture that serves the row, by arm (S the reading v0.57's own screen had of the picture, O a fresh reading of the same
picture, B the trial cast and v0.58's drawings, C the alternatives) and then by reader, the sentences of the free description, the
inventory lines and the lines of the unsure section that hold one of the row's words. A reader has a row's pictures in one arm only
(bench_prepare.py), so a habit shows as one reader's lines. Prints how many readings each row has in each arm. The reading itself is done
from those files: nothing is counted here."""
import collections, json, os, re, sys
ROOT = "E:/Cognitive_Test_Scene_Creator/"
rows = json.load(open(ROOT + "tpdb_work/v058/maps/bench_map.json"))
WORDS = {
    "barrow": r"barrow|wheel|cart\b|trolley|square|boxy|spoke|tyre|tire|frame|crate",
    "heavy": r"see-?saw|teeter|plank|stuck|heav|weigh|seat|handle|climb|ground|down\b|balance|purpose|teas",
    "plain": r"see-?saw|teeter|plank|seat|handle|float",
    "kite": r"kite|string|line\b|reel|spool|handle|reach|point",
    "catch": r"ball|throw|catch|toss|pitch|fence|rail",
}
ORDER = "SOBC"
want = sys.argv[1:] or sorted(WORDS)
cnt = collections.Counter()


def lines_of(f, pat):
    t = open(f, encoding="utf-8").read()
    mu = re.search(r"(?im)^#*\s*\W*\d?\W*\s*\**\s*unsure", t)
    mi = re.search(r"(?im)^#*\s*\W*\d?\W*\s*\**\s*inventory", t)
    free = t[:mi.start()] if mi else t
    inv = t[mi.end():mu.start()] if (mi and mu and mu.start() > mi.end()) else ""
    uns = t[mu.end():] if mu else ""
    out = []
    for s in re.split(r"(?<=[.!?])\s+", " ".join(l.strip() for l in free.splitlines() if l.strip() and not l.lstrip().startswith("#"))):
        if pat.search(s):
            out.append("   F: " + s.strip()[:420])
    for l in inv.splitlines():
        if pat.search(l) and l.strip():
            out.append("   I: " + l.strip()[:420])
    for l in uns.splitlines():
        if pat.search(l) and l.strip():
            out.append("   U: " + l.strip()[:420])
    return out


for row in want:
    pat = re.compile(WORDS[row], re.I)
    out = []
    mine = [r for r in rows if row in r["rows"]]
    for n, pick in sorted({(r["name"], r["pick"]) for r in mine}):
        cnt[(row, "S")] += 1
        out.append("== %s arm S (v0.57's screen, %s)" % (n, pick))
        out += lines_of(ROOT + "vision/v057/desc_%s.md" % pick, pat)
    for r in sorted(mine, key=lambda r: (ORDER.index(r["arm"]), r["reader"], r["name"])):
        f = ROOT + "vision/isolation_v058/bench/desc_%s.md" % r["pic"]
        if not os.path.exists(f):
            out.append("== %s arm %s reader %d (%s): NO DESCRIPTION" % (r["name"], r["arm"], r["reader"], r["pic"]))
            continue
        cnt[(row, r["arm"])] += 1
        out.append("== %s arm %s reader %d (%s)" % (r["name"], r["arm"], r["reader"], r["pic"]))
        out += lines_of(f, pat)
    open(ROOT + "tpdb_work/v058/bench/tally_%s.txt" % row, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
for row in want:
    print(row, {a: cnt[(row, a)] for a in ORDER if cnt[(row, a)]})
