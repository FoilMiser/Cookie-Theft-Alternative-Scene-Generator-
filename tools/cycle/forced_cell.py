"""forced_cell.py SETTING TIER SET SEEDS : one cell of the set from a forced template set, when the free search has failed (RUNBOOK, step 5).
SET is a name in SETS below or a comma-separated list of template ids. Builds into scenes<TAG>; stops as soon as the cell exists. The record
keeps the forced set (regen.forced), so it rebuilds exactly. Measure a set first with yield_set.py: it answers in seconds."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import glob, json, time
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen import templates as TP
from scenegen.generate import build_one
from scenegen.library import Library
from scenegen.planner import USAGE

SETS = {
    # the tier-4 street. v0.29 to v0.31 (T4_street_s447752), and v0.32 forced (T4_street_s430752), with the jump that revision 30 keeps clear of
    # the ball in the tree
    "v031": ["bird_steals", "about_to_trip", "ball_in_tree", "dog_reading", "water_upward", "birds_flying", "sweep", "jump", "carry_bag"],
    # v0.28 (T4_street_s3438959), no jump and no watering
    "v028": ["bird_steals", "ice_cream_drop", "ball_in_tree", "about_to_trip", "dog_reading", "carry_bag", "birds_flying", "sweep"],
    # v0.44: v031 with the upward water (never in the street from revision 42, draw.WATER44) swapped for the square wheel
    "v044": ["bird_steals", "about_to_trip", "ball_in_tree", "dog_reading", "square_wheel", "birds_flying", "sweep", "jump", "carry_bag"],
    # v0.47: v044 with the walker about to trip swapped for the dropped ice cream. Under revision 44 the walker wants no post, tree or stall from a
    # body's width behind him to a body's width past his obstacle (templates.TRIP47), and the crowded street left him no such place: v044 failed on
    # 31 bases of eight sets each, every set on about_to_trip. Built on the first seed, 430752
    "v047street": ["bird_steals", "ice_cream_drop", "ball_in_tree", "dog_reading", "square_wheel", "birds_flying", "sweep", "jump", "carry_bag"],
    # v0.47, the tier-3 playground: the free search failed on 13 bases of 24 sets each. This first set (the playground design test's, with the
    # reading dog) placed but never landed in the band on six bases: too few content items for tier 3, and its inferences estimated near 0.43
    # against a band that ends at 0.38
    "v047play3": ["lost_balloon", "dog_reading", "slide", "kick_ball"],
    # v0.47: of fourteen sets measured with yield_set.py four placed in the band; this one, built on base 6043, holds three templates no other
    # cell of the v0.47 set has
    "v047play3b": ["lost_balloon", "seesaw_heavy", "bucket_hat", "bird_perched", "dog_playing"],
}
setting, tier, name, seeds = sys.argv[1], int(sys.argv[2]), sys.argv[3], [int(x) for x in sys.argv[4].split(",")]
forced = {"modules": [], "contradictions": [], "events": []}
for t in SETS.get(name) or name.split(","):
    c = TP.ALL_TEMPLATES[t]
    forced["modules" if c in TP.MODULES else "contradictions" if c in TP.CONTRADICTIONS else "events"].append(t)
print(name, forced, flush=True)
OUT = f"scenes{TAG}"
lib = Library()
for seed in seeds:
    if [f for f in glob.glob(f"{OUT}/T{tier}_{setting}_s*.json") if not f.endswith("_iso.json")]:
        print("FOUND_ELSEWHERE", flush=True)
        break
    USAGE.clear()
    t0 = time.time()
    rec, sc, fin = build_one(lib, tier, setting, seed, OUT, forced=forced, max_tries=8, log=lambda *a: None)
    print("seed", seed, f"{time.time() - t0:.0f}s", "OK " + rec["name"] if rec else "FAILED " + json.dumps(fin)[:400], flush=True)
    if rec:
        break
print("SEARCH_END", flush=True)
