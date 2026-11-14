"""(v0.54's own script, kept in tools/cycle as a model: its paths and its test are written in. Edit them.)
bench_search.py SETTING SEED0 TRIES WANT template,template,... : extra pictures of the man in the red shirt reading, for v0.54's bench. Builds tier-3
pictures with the given templates forced (v0.53's code and cast, revision 49) on seeds SEED0+1.. into tpdb_work/v054/bench/sc_X, and keeps the first
WANT in which person.ben holds a reading pose; the others are deleted."""
import json, os, sys
ROOT = "E:/Cognitive_Test_Scene_Creator"
sys.path.insert(0, ROOT); os.chdir(ROOT)
setting, seed, tries, want, pick = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
W = "tpdb_work/v054/bench/"
OUT = W + "sc_X"
os.makedirs(OUT, exist_ok=True)
from scenegen import templates as TT
from scenegen.generate import build_one
from scenegen.library import Library
from scenegen.planner import USAGE
kind_of = {c.id: k for k, lst in (("events", TT.EVENTS), ("modules", TT.MODULES), ("contradictions", TT.CONTRADICTIONS)) for c in lst}
forced = {}
for t in pick.split(","):
    forced.setdefault(kind_of[t], []).append(t)
lib = Library(cast_dir="assets/cast/out053", lib_dir=W + "lib_O")
got = 0
for k in range(tries):
    seed += 1
    USAGE.clear()
    rec, sc, fin = build_one(lib, 3, setting, seed, OUT, forced=forced, require_band=False, max_tries=4, log=lambda *a: None)
    if not rec:
        print("FAIL", setting, seed, flush=True)
        continue
    v = [(e.get("asset") or {}).get("variant", "") for e in rec["elements"]]
    hit = [x for x in v if x.startswith("person.ben__") and "read" in x.split("__")[1]]
    if hit:
        got += 1
        print("KEEP", rec["name"], hit, [t["id"] for t in rec["templates"]], flush=True)
        if got >= want:
            break
    else:
        for ext in (".json", ".png", ".svg", "_gray.png"):
            p = os.path.join(OUT, rec["name"] + ext)
            if os.path.exists(p):
                os.remove(p)
        print("skip", rec["name"], [x.split("__")[0] + ":" + x.split("__")[1] for x in v if "read" in x], flush=True)
print("SEARCH_END", setting, got)
