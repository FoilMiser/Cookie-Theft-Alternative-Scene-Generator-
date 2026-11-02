import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import os, sys, json
OUT = os.path.abspath(sys.argv[1])
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.library import Library
from scenegen.generate import build_one
from scenegen.planner import USAGE
lib = Library()
ONLY = sys.argv[2].split(",") if len(sys.argv) > 2 else None
# (setting, tier, seed, forced, rule)
jobs = [
    # a garden with the frying pan (the v0.23 pan, seen at a slant on a shorter handle) beside other work
    ("garden", 3, 23401, {"contradictions": ["pan_watering"], "events": ["dig", "walk_dog", "rake"]}, "pan"),
    # a busy park: the older man carrying a bag (his v0.23 profile) near a sleeping cat, the reading walker and her
    # obstacle a full step ahead, the begging dog, the duck feeding
    ("park", 4, 23402, {"modules": ["about_to_trip", "dog_begs", "ducks_bread"], "events": ["carry_bag", "cat_sleeping", "ice_cream"]}, "tomascarry"),
    # a busy street: the begging dog, the reading walker, a runner, a pram, the square-wheeled bicycle
    ("street", 4, 23403, {"modules": ["about_to_trip", "dog_begs"], "contradictions": ["square_wheel"], "events": ["run", "push_stroller", "feed_birds"]}, None),
    # a playground with a runner and a pram (not heading at each other), the seesaw and the cat stalking a bird
    ("playground", 2, 23404, {"modules": ["cat_stalks_bird"], "events": ["run", "push_stroller", "seesaw"]}, None),
    # a park with an angler and the ducks (none at his float), a photographer
    ("park", 3, 23405, {"events": ["fishing", "ducks_swimming", "photo", "walk_dog"]}, None),
    # a garden with the wheelbarrow standing on its strut, the blocked hose and the washing
    ("garden", 3, 23406, {"modules": ["blocked_hose"], "events": ["hang_laundry", "sweep", "cat_sleeping"]}, "filler_wheelbarrow"),
]


def ok(rec, rule):
    if rule is None:
        return True
    if rule == "railbird":
        return any(it.get("template") == "bird_perched" and "fence" in it["text"] for it in rec["items"])
    if rule == "wave":
        return any(it.get("template") == "wave" for it in rec["items"])
    if rule == "meiread":
        els = {e["id"]: e for e in rec["elements"]}
        return any(it.get("template") == "about_to_trip" and any(els.get(i, {}).get("asset", {}).get("variant", "").startswith("person.mei") for i in it["elements"]) for it in rec["items"])
    if rule == "trip":
        return any(it.get("template") == "about_to_trip" for it in rec["items"])
    if rule == "noreel":
        return not any(e["id"] == "hose_reel" for e in rec["elements"]) and any(it.get("template") == "pan_watering" for it in rec["items"])
    if rule == "kick_ball":
        return any(it.get("template") == "kick_ball" for it in rec["items"])
    if rule == "tomascarry":
        els = {e["id"]: e for e in rec["elements"]}
        return any(it.get("template") == "carry_bag" and any(els.get(i, {}).get("asset", {}).get("variant", "").startswith("person.tomas") for i in it["elements"]) for it in rec["items"])
    if rule == "pan":
        return any(it.get("template") == "pan_watering" for it in rec["items"])
    if rule == "windyswing":
        return any(e["id"] == "swing_seat" for e in rec["elements"])
    if rule == "stalkfence":
        return any(it.get("template") == "cat_stalks_bird" and "fence" in it["text"] for it in rec["items"])
    return any(e["id"] == rule for e in rec["elements"])


for st, t, seed, forced, rule in jobs:
    if ONLY and f"{st}{seed}" not in ONLY:
        continue
    rec = None
    for k in range(30):
        USAGE.clear()
        r_, sc, fin = build_one(lib, t, st, seed + 1000 * k, OUT, forced=forced, require_band=False, max_tries=8, log=lambda *a: None)
        if r_ and ok(r_, rule):
            rec = r_
            break
    print(st, t, seed, rec["name"] if rec else ("FAIL " + json.dumps(fin)[:300]), flush=True)
