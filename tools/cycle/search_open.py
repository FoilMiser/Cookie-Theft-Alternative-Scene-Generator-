"""search_open017.py setting tier seeds OUT : a showcase seed for one cell with no template-variety steering (USAGE empty).
The record stores usage {}, so it rebuilds exactly. For the tier-4 cells, where steering toward the templates the setting's
other pictures had not used left mostly combinations that could not be placed together."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import os, sys, glob, time, json
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.generate import build_one
from scenegen.library import Library
from scenegen.planner import USAGE
setting, tier, seeds, OUT = sys.argv[1], int(sys.argv[2]), [int(x) for x in sys.argv[3].split(",")], sys.argv[4]
lib = Library()
for seed in seeds:
    if [f for f in glob.glob(f"{OUT}/T{tier}_{setting}_s*.json") if not f.endswith("_iso.json")]:
        print("FOUND_ELSEWHERE", flush=True); break
    USAGE.clear()
    t0 = time.time()
    rec, sc, fin = build_one(lib, tier, setting, seed, OUT, max_tries=40, log=lambda *a: None)
    print("seed", seed, f"{time.time() - t0:.0f}s", "OK " + rec["name"] if rec else "FAILED " + json.dumps(fin)[:300], flush=True)
    if rec:
        break
print("SEARCH_END", flush=True)
