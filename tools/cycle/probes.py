"""Probe pictures for v0.10: every template must appear in at least three screened pictures (set + probes).
Greedy: pick a setting, force up to 5 templates still short of two appearances (respecting settings and
shared resources), build a tier-3 picture, repeat. Records are marked "probe": true."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, os, sys, glob, random, collections
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen import templates as TT
from scenegen.generate import build_one
from scenegen.library import Library
from scenegen.planner import feasible, USAGE
OUT = f"probes{TAG}"
os.makedirs(OUT, exist_ok=True)
NEED = int(sys.argv[1]) if len(sys.argv) > 1 else 3
# v0.39: five pictures for the one-item templates nearest the gate (with three, one half mark takes one under 0.9: hang_laundry in v0.30 and v0.37)
# v0.40: five for windy_hat and dog_wants_walk, v0.39's lowest by the strict count and by the gate (vision/flaws_v039.md R1, R2)
# v0.41: five for play_catch and floating_box (vision/flaws_v040.md R1, R2); v0.42: five for blocked_hose and rain_coming, v0.41's two under the
# strict count (vision/flaws_v041.md R1, R2); v0.43: five for about_to_trip (under the gate in v0.42, on one zero in three pictures), plant_flowers
# and photo (under the strict count; vision/flaws_v042.md R1, R3)
# v0.44: five for dog_reading and dog_wants_walk, the two v0.43 failures (R1, R2), and photo, the lowest pass (R3)
# v0.45: five for v0.44's three lowest, each redrawn (ice_cream, photo, lost_balloon; vision/flaws_v044.md R1 to R3), and for the two templates whose
# drawing changed most (plant_flowers digs in the bed with a trowel, paint_fence stands a step forward with a new roller)
# v0.46: five for v0.45's three lowest, which v0.46 carries (bird_steals, square_wheel, cat_stalks_bird; vision/flaws_v045.md R1 to R3), for the
# reading dog, which failed v0.45's first count and was drawn again after its screen, and for the ice cream, the pose in which the bench's reviewers
# named the neck (vision/isolation_v046.md)
# v0.47: five for the eight templates of v0.46's list, each drawn or placed anew in this release: the four under the gate (dog_reading,
# about_to_trip, sweep_fork, blocked_hose; vision/flaws_v046.md R1 to R4), bird_steals (R5) and the three of R6 (cat_stalks_bird, water_upward,
# lost_balloon)
# v0.48: five for the four R rows of v0.47's list (about_to_trip, which failed the gate twice and has motion lines and a nearer obstacle now;
# blocked_hose, lost_balloon, water_upward: vision/flaws_v047.md R1 to R4) and for five templates whose animal was drawn anew and carries the
# reading: dog_reading, bird_steals and cat_stalks_bird (R5), walk_dog (the dog whose stand and walk lost its pair on the bench, and a walker
# whose direction one bench reader had the other way) and dog_sleeping (not read small and far in the bench's fourth round)
# v0.49: five for rain_coming too (vision/flaws_v048.md R1: it failed the gate at 0.889 on one unsaid inference in three pictures, and its
# verdict rests on one inference a picture)
# v0.50: five for the R rows of v0.49's list (lost_balloon, blocked_hose, play_catch, the four dog templates, seesaw_heavy:
# vision/flaws_v049.md R1 to R5), for the templates whose drawing or placing changed (seesaw and slide, O2; balloon, O5; paint_fence, O3;
# goat_grazing, O4) and for rain_coming, whose verdict rests on one inference a picture. The eight of v0.48 that are not on v0.49's list
# go back to three
# v0.51: five for the R rows of v0.50's list (play_catch and square_wheel, which failed the gate; bird_steals, blocked_hose, ducks_bread:
# vision/flaws_v050.md R1 to R5; and R6's five, jump, dog_sleeping, dog_wants_walk, dog_begs and plant_flowers, whose full marks rest on
# hedges), for lost_balloon and paint_fence, whose placing changed (O1, O3), and for rain_coming, whose verdict rests on one inference a
# picture. Six of v0.50's that are not on v0.50's list go back to three (dog_playing, seesaw_heavy, seesaw, slide, balloon, goat_grazing).
# square_wheel has two carriers, the barrow and the bicycle: count them after the passes and see that each has two pictures or more
NEED_T = {"rain_coming": 5, "play_catch": 5, "square_wheel": 5, "bird_steals": 5, "blocked_hose": 5, "ducks_bread": 5, "lost_balloon": 5,
          "paint_fence": 5, "jump": 5, "dog_sleeping": 5, "dog_wants_walk": 5, "dog_begs": 5, "plant_flowers": 5}
need = lambda t: max(NEED, NEED_T.get(t, 0))
cnt = collections.Counter()
for f in glob.glob(f"scenes{TAG}/T*.json") + glob.glob(OUT + "/T*.json"):
    for t in json.load(open(f))["templates"]:
        cnt[t["id"]] += 1
kind_of = {c.id: k for k, lst in (("events", TT.EVENTS), ("modules", TT.MODULES), ("contradictions", TT.CONTRADICTIONS)) for c in lst}
cls = TT.ALL_TEMPLATES
lib = Library()
rng = random.Random(78)
seed = 23000
fails = collections.Counter()
solo = set()      # templates whose group failed: probed alone from then on
MAXG = 3
DUCKS = {"ducks_bread", "ducks_swimming"}
alone = set()     # templates already probed on their own
for rnd in range(80):
    short = [t for t in cls if cnt[t] < need(t) and fails[t] < 3]
    if not short:
        break
    short.sort(key=lambda t: (cnt[t], fails[t], rng.random()))
    best = None
    for setting in ("garden", "park", "street", "playground"):
        sky = "clear"
        pick, used = [], set()
        n_mod = n_con = 0
        for t in short:
            # at most one template whose earlier group failed, and at most one duck template, per picture
            if t in solo and set(pick) & solo:
                continue
            if t in DUCKS and set(pick) & DUCKS:
                continue
            c = cls[t]
            sk = "dark" if getattr(c, "sky", None) == "dark" else "clear"
            if setting not in c.settings or not feasible(c, setting, sk):
                continue
            if sk == "dark" and sky == "clear" and pick:
                continue
            if any(r in used for r in c.exclusive):
                continue
            k = kind_of[t]
            if k == "modules" and n_mod >= 2 or k == "contradictions" and n_con >= 1:
                continue
            pick.append(t); used |= set(c.exclusive)
            if sk == "dark":
                sky = "dark"
            n_mod += k == "modules"; n_con += k == "contradictions"
            if len(pick) >= MAXG:
                break
        if pick and (best is None or len(pick) > len(best[1])):
            best = (setting, pick)
    setting, pick = best
    forced = {"events": [], "modules": [], "contradictions": []}
    for t in pick:
        forced[kind_of[t]].append(t)
    if pick == ["photo"]:
        # v0.17 (revision 15): a photographer needs someone to photograph
        forced["events"].append({"park": "ice_cream", "street": "read_bench", "playground": "ice_cream"}[setting])
    elif len(pick) == 1 and pick[0] in alone:
        # v0.26: one template alone a second time looks the same as the first (two seesaw probes: "This picture looks the same as
        # picture 61"), so the second has company
        forced["events"].append({"garden": "sweep", "park": "ice_cream", "street": "read_bench", "playground": "ice_cream"}[setting])
    elif len(pick) == 1:
        alone.add(pick[0])
    forced = {k: v for k, v in forced.items() if v}
    if forced.get("events") == ["wave"]:
        # a wave needs someone to wave at, so it cannot be probed alone
        forced["events"] = ["wave", "sweep", "carry_box"] if setting == "garden" else ["wave", "walk_dog", "ice_cream"]
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
    else:
        # try the hardest one alone next time
        for t in pick:
            fails[t] += 1
            if len(pick) > 1:
                solo.add(t)
        print("FAIL", setting, pick, json.dumps(fin)[:300], flush=True)
print("SHORT", {t: cnt[t] for t in cls if cnt[t] < need(t)})
