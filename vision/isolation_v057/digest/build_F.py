"""build_F.py F|G : the bench's new pictures of the game of catch, under revision 51 (tier 3, forced sets, band not required, the loop of
tools/cycle/extra_probes.py from base seed 57100, as tpdb_work/v057/g_catch/mk.py built them). Arm F: every switch at its default. Arm G:
the same forced sets on the seeds that arm F built, with v0.56's flight and no line rule (TPDB_ARC57=O TPDB_CATCHLINE57=O).
Cast tpdb_work/v057/bench/out_B, library lib_B (the bench's arm B)."""
import os, sys, json, glob
ROOT = "E:/Cognitive_Test_Scene_Creator"
sys.path.insert(0, ROOT); os.chdir(ROOT)
arm = sys.argv[1]
W = "tpdb_work/v057/bench/"
if arm == "G":
    os.environ.update({"TPDB_ARC57": "O", "TPDB_CATCHLINE57": "O"})
from scenegen import templates as TT
from scenegen.generate import build_one
from scenegen.library import Library
from scenegen.planner import USAGE
OUT = W + "sc_" + arm
os.makedirs(OUT, exist_ok=True)
kind_of = {c.id: k for k, lst in (("events", TT.EVENTS), ("modules", TT.MODULES), ("contradictions", TT.CONTRADICTIONS)) for c in lst}
GROUPS = ["garden:play_catch,cat_on_fence,dig", "garden:play_catch,hang_laundry,rake", "park:play_catch,walk_dog,feed_birds",
          "playground:play_catch,slide,balloon", "street:play_catch,carry_bag,sweep"]
lib = Library(cast_dir=W + "out_B", lib_dir=W + "lib_B")


def forced_of(pick):
    f = {}
    for t in pick.split(","):
        f.setdefault(kind_of[t], []).append(t)
    return f


if arm == "F":
    seed = 57100
    for g in GROUPS:
        setting, pick = g.split(":")
        for k in range(8):
            seed += 1
            USAGE.clear()
            rec, sc, fin = build_one(lib, 3, setting, seed, OUT, forced=forced_of(pick), require_band=False, max_tries=6, log=lambda *a: None)
            if rec:
                print("BUILT", rec["name"], "seed", seed, setting, [t["id"] for t in rec["templates"]], flush=True)
                break
            print("FAIL", setting, pick, seed, str(fin)[-200:], flush=True)
else:
    for f in sorted(glob.glob(W + "sc_F/T*.json")):
        r = json.load(open(f, encoding="utf-8"))
        g = r["regen"]
        USAGE.clear(); USAGE.update(g["usage"])
        rec, sc, fin = build_one(lib, 3, r["setting"], g["base_seed"], OUT, forced=g["forced"], require_band=False, max_tries=g["max_tries"], log=lambda *a: None)
        print(r["name"], "->", rec["name"] if rec else ("FAILED " + str(fin)[-200:]), flush=True)
print("F_END", arm)
