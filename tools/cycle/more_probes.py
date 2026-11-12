"""more_probes.py : force the templates that probes.py left short, in small groups in a setting that suits them (RUNBOOK, step 6). probes.py gives a
template up after three failed groups, and the failures are often a partner's. Edit GROUPS (target, setting, forced set) and NEED_T (as in
probes.py) for the release. Each group gets up to eight seeds, a target's later groups are skipped once it has what it needs, and records are
marked "probe": true as probes.py marks them. Must end SHORT {}. The groups below are v0.49's, for nine templates; v0.47's and v0.48's were for the blown hat."""
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
NEED_T = {"rain_coming": 5, "about_to_trip": 5, "blocked_hose": 5, "lost_balloon": 5, "water_upward": 5, "dog_reading": 5, "bird_steals": 5,
          "cat_stalks_bird": 5, "walk_dog": 5, "dog_sleeping": 5}
# v0.49: probes.py gave up nine templates. The washing: only the three tallest grown figures reach the line (the hanger's feet must stand
# within 30 px of the posts' depth), and its groups cast a shorter one on most seeds. The others lost their three groups to a partner:
# the storm with a watering template (not feasible under a dark sky), the begging dog and the dog that wants its walk with a second dog
# template (one dog too few), the playground's own events with each other. Small groups whose partners place beside the target
GROUPS = [("hang_laundry", "garden", ["hang_laundry", "cat_on_fence", "rake"]),
          ("hang_laundry", "garden", ["hang_laundry", "cat_on_fence"]),
          ("hang_laundry", "garden", ["hang_laundry", "rake", "sweep"]),
          ("hang_laundry", "garden", ["hang_laundry", "dog_sleeping"]),
          ("hang_laundry", "garden", ["hang_laundry", "dig", "swing"]),
          ("hang_laundry", "garden", ["hang_laundry", "paint_fence"]),
          ("hang_laundry", "garden", ["hang_laundry", "dog_playing", "carry_box"]),
          ("rain_coming", "garden", ["rain_coming", "sweep"]),
          ("rain_coming", "garden", ["rain_coming", "dog_sleeping", "walk_dog"]),
          ("rain_coming", "garden", ["rain_coming"]),
          ("rain_coming", "park", ["rain_coming", "read_bench"]),
          ("rain_coming", "garden", ["rain_coming", "paint_fence", "dig"]),
          ("rain_coming", "playground", ["rain_coming", "kick_ball"]),
          ("rain_coming", "street", ["rain_coming", "carry_bag"]),
          ("fishing", "park", ["fishing"]),
          ("fishing", "park", ["fishing", "carry_bag", "balloon"]),
          ("fishing", "park", ["fishing", "run"]),
          ("seesaw", "playground", ["seesaw"]),
          ("seesaw", "playground", ["seesaw", "ice_cream"]),
          ("sandbox", "playground", ["sandbox"]),
          ("sandbox", "playground", ["sandbox", "kick_ball"]),
          ("slide", "playground", ["slide"]),
          ("slide", "playground", ["slide", "ice_cream"]),
          ("seesaw_heavy", "playground", ["seesaw_heavy"]),
          ("seesaw_heavy", "playground", ["seesaw_heavy", "ice_cream"]),
          ("dog_begs", "park", ["dog_begs", "ice_cream"]),
          ("dog_begs", "street", ["dog_begs", "sweep", "carry_bag"]),
          ("dog_begs", "playground", ["dog_begs", "kick_ball"]),
          ("windy_hat", "park", ["windy_hat", "feed_birds", "walk_dog"]),
          ("windy_hat", "street", ["windy_hat", "carry_box", "sweep"]),
          ("windy_hat", "garden", ["windy_hat", "rake", "paint_fence"]),
          ("windy_hat", "park", ["windy_hat", "ice_cream"]),
          ("dog_wants_walk", "garden", ["dog_wants_walk"]),
          ("dog_wants_walk", "garden", ["dog_wants_walk", "sweep"]),
          ("dog_wants_walk", "garden", ["dog_wants_walk", "lost_balloon", "bucket_hat"])]
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
print("BEFORE", {t: cnt[t] for t in sorted({g[0] for g in GROUPS})}, flush=True)
for target, setting, pick in GROUPS:
    if cnt[target] >= max(3, NEED_T.get(target, 0)):
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
