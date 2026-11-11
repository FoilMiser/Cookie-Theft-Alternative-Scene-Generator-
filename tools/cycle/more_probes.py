"""more_probes.py : force the templates that probes.py left short, in small groups in a setting that suits them (RUNBOOK, step 6). probes.py gives a
template up after three failed groups, and the failures are often a partner's. Edit GROUPS (target, setting, forced set) and NEED_T (as in
probes.py) for the release. Each group gets up to eight seeds, a target's later groups are skipped once it has its three, and records are
marked "probe": true as probes.py marks them. Must end SHORT {}. The groups below are v0.47's and v0.48's, for the blown hat."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections, glob, json, os, sys
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen import templates as TT
from scenegen.generate import build_one
from scenegen.library import Library
from scenegen.planner import USAGE
OUT = f"probes{TAG}"
NEED_T = {"about_to_trip": 5, "blocked_hose": 5, "lost_balloon": 5, "water_upward": 5, "dog_reading": 5, "bird_steals": 5, "cat_stalks_bird": 5,
          "walk_dog": 5, "dog_sleeping": 5}
GROUPS = [("windy_hat", "park", ["windy_hat", "feed_birds", "walk_dog"]),
          ("windy_hat", "street", ["windy_hat", "carry_box", "sweep"]),
          ("windy_hat", "garden", ["windy_hat", "rake", "paint_fence"]),
          ("windy_hat", "garden", ["windy_hat", "fish_in_tree", "plant_flowers"]),
          ("windy_hat", "park", ["windy_hat", "ice_cream"]),
          ("windy_hat", "playground", ["windy_hat", "slide", "kick_ball"]),
          ("windy_hat", "street", ["windy_hat", "walk_dog"])]
kind_of = {c.id: k for k, lst in (("events", TT.EVENTS), ("modules", TT.MODULES), ("contradictions", TT.CONTRADICTIONS)) for c in lst}


def count():
    c = collections.Counter()
    for f in glob.glob(f"scenes{TAG}/T*.json") + glob.glob(OUT + "/T*.json"):
        for t in json.load(open(f))["templates"]:
            c[t["id"]] += 1
    return c


lib = Library()
seed = 23700
cnt = count()
print("BEFORE", {t: cnt[t] for t in ("windy_hat", "dog_begs")}, flush=True)
for target, setting, pick in GROUPS:
    if cnt[target] >= 3:
        continue
    forced = {}
    for t in pick:
        forced.setdefault(kind_of[t], []).append(t)
    for k in range(8):
        seed += 1
        USAGE.clear()
        rec, sc, fin = build_one(lib, 3, setting, seed, OUT, forced=forced, require_band=False, max_tries=6, log=lambda *a: None)
        if rec:
            p = os.path.join(OUT, rec["name"] + ".json")
            r = json.load(open(p)); r["probe"] = True
            json.dump(r, open(p, "w"), indent=1)
            for t in r["templates"]:
                cnt[t["id"]] += 1
            print("PROBE", rec["name"], [t["id"] for t in r["templates"]], flush=True)
            break
        print("FAIL", setting, pick, seed, json.dumps(fin)[:200], flush=True)
cnt = count()
print("SHORT", {t: cnt[t] for t in TT.ALL_TEMPLATES if cnt[t] < max(3, NEED_T.get(t, 0))})
