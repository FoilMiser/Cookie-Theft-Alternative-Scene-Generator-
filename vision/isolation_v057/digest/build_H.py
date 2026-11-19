"""build_H.py : round 2 of the game of catch: new pictures under revision 51 with the catcher cast young (CATCHCAST "B") and the flat
flight, on the forced sets of arm F whose catcher was a grown figure (the playground's with partners that need no child). Tier 3, band
not required, the loop of tools/cycle/extra_probes.py. Cast tpdb_work/v057/bench/out_B, library lib_B. Into sc_H."""
import os, sys, json
ROOT = "E:/Cognitive_Test_Scene_Creator"
sys.path.insert(0, ROOT); os.chdir(ROOT)
W = "tpdb_work/v057/bench/"
from scenegen import templates as TT
from scenegen.generate import build_one
from scenegen.library import Library
from scenegen.planner import USAGE
OUT = W + "sc_H"
os.makedirs(OUT, exist_ok=True)
kind_of = {c.id: k for k, lst in (("events", TT.EVENTS), ("modules", TT.MODULES), ("contradictions", TT.CONTRADICTIONS)) for c in lst}
GROUPS = [(57100, "garden:play_catch,cat_on_fence,dig"), (57102, "park:play_catch,walk_dog,feed_birds"),
          (57300, "playground:play_catch,push_stroller,dog_playing"), (57104, "street:play_catch,carry_bag,sweep"), (57400, "garden:play_catch,paint_fence,cat_on_fence")]
lib = Library(cast_dir=W + "out_B", lib_dir=W + "lib_B")
for seed, g in GROUPS:
    setting, pick = g.split(":")
    forced = {}
    for t in pick.split(","):
        forced.setdefault(kind_of[t], []).append(t)
    for k in range(8):
        seed += 1
        USAGE.clear()
        rec, sc, fin = build_one(lib, 3, setting, seed, OUT, forced=forced, require_band=False, max_tries=6, log=lambda *a: None)
        if rec:
            who = [e["asset"]["family"] for e in rec["elements"] if e.get("asset") and e["id"].startswith(("thrower", "catcher"))]
            print("BUILT", rec["name"], "seed", seed, setting, [t["id"] for t in rec["templates"]], who, flush=True)
            break
        print("FAIL", setting, pick, seed, str(fin)[-160:], flush=True)
print("H_END")
