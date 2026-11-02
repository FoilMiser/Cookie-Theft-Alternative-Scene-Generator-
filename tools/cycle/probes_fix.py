import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, os, sys, glob, shutil
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen import templates as TT
from scenegen.generate import build_one
from scenegen.library import Library
from scenegen.planner import USAGE
OUT = f"probes{TAG}"; OLD = os.path.join(WORK, f"old{TAG}", "probes")
kind_of = {c.id: k for k, lst in (("events", TT.EVENTS), ("modules", TT.MODULES), ("contradictions", TT.CONTRADICTIONS)) for c in lst}
lib = Library()
seed = int(sys.argv[2]) if len(sys.argv) > 2 else 23600
for name in sys.argv[1].split(","):
    r0 = json.load(open(os.path.join(OUT, name + ".json")))
    ids = [t["id"] for t in r0["templates"]]
    if os.environ.get("ONLY"): ids = os.environ["ONLY"].split("+")
    forced = {}
    for t in ids:
        forced.setdefault(kind_of[t], []).append(t)
    for k in range(8):
        seed += 1
        USAGE.clear()
        rec, sc, fin = build_one(lib, 3, os.environ.get("SETTING", r0["setting"]), seed, OUT, forced=forced, require_band=False, max_tries=6, log=lambda *a: None)
        if rec and sorted(t["id"] for t in rec["templates"]) == sorted(ids):
            p = os.path.join(OUT, rec["name"] + ".json"); r = json.load(open(p)); r["probe"] = True; json.dump(r, open(p, "w"), indent=1)
            for g in glob.glob(os.path.join(OUT, name + "*")):
                shutil.move(g, OLD)
            print("PROBE", rec["name"], ids, "replaces", name, flush=True)
            break
        elif rec:
            for g in glob.glob(os.path.join(OUT, rec["name"] + "*")):
                os.remove(g)
        print("FAIL", name, seed, json.dumps(fin)[:150], flush=True)
