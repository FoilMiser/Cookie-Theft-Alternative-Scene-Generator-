"""(v0.54's own script, kept in tools/cycle as a model: its paths and its test are written in. Edit them.)
bench_extra.py SETTING SEED0 template,template,... : one extra tier-3 picture for v0.54's bench with the given templates forced, built with v0.53's
code and cast (revision 49) into tpdb_work/v054/bench/sc_X on the first of seeds SEED0+1.. that places."""
import json, os, sys
ROOT = "E:/Cognitive_Test_Scene_Creator"
sys.path.insert(0, ROOT); os.chdir(ROOT)
setting, seed, pick = sys.argv[1], int(sys.argv[2]), sys.argv[3]
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
for k in range(12):
    seed += 1
    USAGE.clear()
    rec, sc, fin = build_one(lib, 3, setting, seed, OUT, forced=forced, require_band=False, max_tries=4, log=lambda *a: None)
    if rec:
        print("KEEP", rec["name"], [t["id"] for t in rec["templates"]], flush=True)
        break
    print("FAIL", setting, seed, flush=True)
print("EXTRA_END")
