"""(v0.57's own script: its rows and paths are written in.)
bench_tally.py [ROW ...] : v0.57's whole-picture bench. For every row (default: all) writes tpdb_work/v057/bench/tally_<row>.txt: for each
reading of a picture that serves the row, by arm (S the reading v0.56's own screen had of the picture, O a fresh reading of the same
picture, B the trial cast and v0.57's drawings, C the alternatives, P v0.55's pan, F a new picture under revision 51, G the same with
v0.56's flight), the sentences of the free description, the inventory lines and the lines of the unsure section that hold one of the
row's words. And prints how many readings each row has in each arm. The reading itself is done from those files: nothing is counted here."""
import collections, json, os, re, sys
ROOT = "E:/Cognitive_Test_Scene_Creator/"
rows = json.load(open(ROOT + "tpdb_work/v057/maps/bench_map.json"))
WORDS = {
    "catch": r"ball|throw|catch|toss|pitch",
    "pan": r"\bpan\b|pot\b|saucepan|frying|skillet|watering|ladle|scoop|bowl|dish|shovel|spade|wok|water",
    "seesaw_heavy": r"see-?saw|teeter|plank|stuck|heav|weigh|seat|book|newspaper|reading",
    "pond": r"pond|water's edge|bank|shore|rim|wading|in the water|fishing|angler|rod|duck|bread",
    "wind": r"wind|gust|streak|breeze|\bcap\b|\bhat\b|washing|laundry|clothes",
    "kite": r"kite|string|line",
    "grey": r"paint|pink|magenta|roller|print|\bbox\b|crate|trip|\bcap\b|\bhat\b",
}
ORDER = "SOBCPFG"
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
    seen_s = set()
    for r in sorted(mine, key=lambda r: (r["name"], ORDER.index(r["arm"]), r["reader"])):
        if r["pick"] and r["name"] not in seen_s:
            seen_s.add(r["name"])
            f = ROOT + "vision/v056/desc_%s.md" % r["pick"]
            cnt[(row, "S")] += 1
            out.append("== %s arm S (v0.56's screen, %s)" % (r["name"], r["pick"]))
            out += lines_of(f, pat)
        f = ROOT + "vision/isolation_v057/bench/desc_%s.md" % r["pic"]
        if not os.path.exists(f):
            out.append("== %s arm %s reader %d (%s): NO DESCRIPTION" % (r["name"], r["arm"], r["reader"], r["pic"]))
            continue
        cnt[(row, r["arm"])] += 1
        out.append("== %s arm %s reader %d (%s)" % (r["name"], r["arm"], r["reader"], r["pic"]))
        out += lines_of(f, pat)
    open(ROOT + "tpdb_work/v057/bench/tally_%s.txt" % row, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
for row in want:
    print(row, {a: cnt[(row, a)] for a in ORDER if cnt[(row, a)]})
