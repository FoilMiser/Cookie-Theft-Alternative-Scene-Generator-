"""extra_probes.py SEED SETTING:template,template[,...] [SETTING:template,...] ... : probes forced whatever the counts say (v0.51).

probes.py and more_probes.py count pictures per template. A template with two carriers can have its five pictures and one carrier in only
one of them: v0.50's square wheel was a bicycle in three pictures of four, and failed its gate on the one wheelbarrow, which is the garden's
and the park's. This builds one tier-3 probe for each group given, in its setting, on seeds SEED+1, SEED+2, ... (eight tries a group), and
marks the record "probe": true, as more_probes.py does. Give it seeds that the other passes do not use (probes.py 23000+, more_probes.py
23700+, probe_angle.py 40500+)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen import templates as TT
from scenegen.generate import build_one
from scenegen.library import Library
from scenegen.planner import USAGE
OUT = f"probes{TAG}"
kind_of = {c.id: k for k, lst in (("events", TT.EVENTS), ("modules", TT.MODULES), ("contradictions", TT.CONTRADICTIONS)) for c in lst}
seed = int(sys.argv[1])
lib = Library()
for g in sys.argv[2:]:
    setting, pick = g.split(":")
    forced = {}
    for t in pick.split(","):
        forced.setdefault(kind_of[t], []).append(t)
    for k in range(8):
        seed += 1
        USAGE.clear()
        rec, sc, fin = build_one(lib, 3, setting, seed, OUT, forced=forced, require_band=False, max_tries=6, log=lambda *a: None)
        if rec:
            p = os.path.join(OUT, rec["name"] + ".json")
            r = json.load(open(p)); r["probe"] = True
            json.dump(r, open(p, "w"), indent=1)
            print("PROBE", rec["name"], [t["id"] for t in r["templates"]], flush=True)
            break
        print("FAIL", setting, pick, seed, json.dumps(fin)[:200], flush=True)
print("EXTRA_END")
