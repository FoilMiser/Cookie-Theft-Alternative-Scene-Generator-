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
NEED_T = {"play_catch": 5, "floating_box": 5}
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
