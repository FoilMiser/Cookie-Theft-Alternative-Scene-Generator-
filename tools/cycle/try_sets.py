"""try_sets.py SETTING SEED N OUTFILE [MODULES CONTRADICTIONS EVENTS] : which template sets fit a crowded cell? Random sets of the planner's shape, each tried for 14 layouts with
no difficulty band, so a set that places is kept even if it misses its tier. Writes a JSON line per set to OUTFILE and the records of those that placed to <WORK>/try_sets/.
Read those records for what the sets have in common, their features and their content counts too (v0.28, vision/flaws_v028.md, Placement)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK  # noqa: E402
import json, random, sys, time
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen import planner as PL
from scenegen import templates as TP
from scenegen.generate import build_one
from scenegen.library import Library
from scenegen.planner import USAGE

setting, seed, n, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
n_m, n_c, n_e = (int(x) for x in sys.argv[5:8]) if len(sys.argv) > 7 else (3, 2, 4)
lib = Library()
rng = random.Random(seed)
feas = lambda cs: [c for c in cs if PL.feasible(c, setting, "clear") and c.sky != "dark"]
mods, cons, evs = feas(TP.MODULES), feas(TP.CONTRADICTIONS), feas(TP.EVENTS)
f = open(out, "a", encoding="utf-8")
done = k = 0
while done < n:
    k += 1
    while True:
        ms, cs, es = rng.sample(mods, n_m), rng.sample(cons, n_c), rng.sample(evs, n_e)
        res = [r for c in ms + cs + es for r in c.exclusive]
        if len(res) == len(set(res)):
            break
    forced = {"modules": [c.id for c in ms], "contradictions": [c.id for c in cs], "events": [c.id for c in es]}
    USAGE.clear()
    t0 = time.time()
    rec, sc, fin = build_one(lib, 4, setting, seed * 1000 + k, os.path.join(WORK, "try_sets"), forced=forced, require_band=False, max_tries=1, log=lambda *a: None)
    why = "" if rec else str(fin)[:300]
    if "no free" in why:     # could not be cast at all: not a test of the set
        continue
    done += 1
    f.write(json.dumps({"set": forced, "placed": bool(rec), "why": why, "secs": round(time.time() - t0, 1)}) + "\n")
    f.flush()
print("TRY_SETS_END")
