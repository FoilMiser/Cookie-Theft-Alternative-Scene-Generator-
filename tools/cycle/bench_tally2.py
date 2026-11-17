"""(v0.56's own script.) bench_tally2.py : the second round of v0.56's bench. For each of its three questions writes
tpdb_work/v056/bench/tally2_<row>.txt: every reading's sentences, inventory lines and unsure lines that hold one of the row's words,
by picture and arm. The reading is done from those files: nothing is counted here."""
import json, os, re
ROOT = "E:/Cognitive_Test_Scene_Creator/"
rows = json.load(open(ROOT + "tpdb_work/v056/maps/bench2_map.json"))
WORDS = {"bird": r"sandwich|bird|bench|bread|slice", "photo": r"camera|photo|picture of|aim|point", "hose": r"hose|nozzle|tap|reel|drip|drop|water|dog|leak|puddle"}
for row, pat_ in WORDS.items():
    pat = re.compile(pat_, re.I)
    out = []
    for r in sorted((r for r in rows if row in r["rows"]), key=lambda r: (r["name"], r["arm"], r["reader"])):
        f = ROOT + "vision/isolation_v056/bench2/desc_%s.md" % r["pic"]
        if not os.path.exists(f):
            out.append("== %s arm %s reader %d (%s): NO DESCRIPTION" % (r["name"], r["arm"], r["reader"], r["pic"]))
            continue
        t = open(f, encoding="utf-8").read()
        mu = re.search(r"(?im)^#*\s*\W*\d?\W*\s*\**\s*unsure", t)
        mi = re.search(r"(?im)^#*\s*\W*\d?\W*\s*\**\s*inventory", t)
        free = t[:mi.start()] if mi else t
        inv = t[mi.end():mu.start()] if (mi and mu and mu.start() > mi.end()) else ""
        uns = t[mu.end():] if mu else ""
        out.append("== %s arm %s reader %d (%s)" % (r["name"], r["arm"], r["reader"], r["pic"]))
        for s in re.split(r"(?<=[.!?])\s+", " ".join(l.strip() for l in free.splitlines() if l.strip() and not l.lstrip().startswith("#"))):
            if pat.search(s):
                out.append("   F: " + s.strip()[:500])
        for l in inv.splitlines():
            if pat.search(l) and l.strip():
                out.append("   I: " + l.strip()[:500])
        for l in uns.splitlines():
            if pat.search(l) and l.strip():
                out.append("   U: " + l.strip()[:500])
    open(ROOT + "tpdb_work/v056/bench/tally2_%s.txt" % row, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    print(row, sum(1 for l in out if l.startswith("==")), "readings")
