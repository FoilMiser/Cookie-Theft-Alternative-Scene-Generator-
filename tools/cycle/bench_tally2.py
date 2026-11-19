"""(v0.57's own script: its rows and paths are written in.)
bench_tally2.py : the second round of v0.57's bench (vision/isolation_v057/bench2). Writes tpdb_work/v057/bench/tally2_<row>.txt, as
bench_tally.py does for the first round: for each reading, by arm (pan: C the dark hollow pan alone, D the same with an unused watering can
beside the holder; seesaw_heavy: E the seat where its rider sits and the man without his book; catch: H the catcher cast young), the
sentences and lines that hold one of the row's words, and prints the readings by row, arm and reader."""
import collections, json, os, re, sys
ROOT = "E:/Cognitive_Test_Scene_Creator/"
rows = json.load(open(ROOT + "tpdb_work/v057/maps/bench2_map.json"))
WORDS = {
    "catch": r"ball|throw|catch|toss|pitch",
    "pan": r"\bpan\b|pot\b|saucepan|frying|skillet|watering|ladle|scoop|bowl|dish|shovel|spade|wok|water|\bcan\b",
    "seesaw_heavy": r"see-?saw|teeter|plank|stuck|heav|weigh|seat|book|newspaper|reading",
}
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


for row in sorted(WORDS):
    pat = re.compile(WORDS[row], re.I)
    out = []
    for r in sorted((r for r in rows if row in r["rows"]), key=lambda r: (r["arm"], r["name"], r["reader"])):
        f = ROOT + "vision/isolation_v057/bench2/desc_%s.md" % r["pic"]
        if not os.path.exists(f):
            out.append("== %s arm %s reader %d (%s): NO DESCRIPTION" % (r["name"], r["arm"], r["reader"], r["pic"]))
            continue
        cnt[(row, r["arm"])] += 1
        out.append("== %s arm %s reader %d (%s)" % (r["name"], r["arm"], r["reader"], r["pic"]))
        out += lines_of(f, pat)
    open(ROOT + "tpdb_work/v057/bench/tally2_%s.txt" % row, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print(dict(cnt))
