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
    # a busy park: the older man carrying a bag and a sleeping cat (kept clear of his feet on both sides), people kept out of
    # the strip of ground before the horizon, the reading walker, the ducks
    ("park", 4, 24401, {"modules": ["about_to_trip", "ducks_bread"], "events": ["carry_bag", "cat_sleeping", "ice_cream"]}, "tomascarry"),
    # a playground with the riders on the seesaw and the teenager kicking
    ("playground", 3, 24402, {"events": ["seesaw", "kick_ball", "walk_dog", "wave"]}, "teen"),
    # a park with the teenager's ice cream, a sleeping dog among walkers and a runner
    ("park", 3, 24403, {"events": ["ice_cream", "dog_sleeping", "walk_dog", "run"]}, "teen"),
    # a busy street with the teenager, a hat blowing off someone else, a bucket for a hat (over the teenager's cap, if cast)
    ("street", 4, 24404, {"modules": ["windy_hat"], "contradictions": ["bucket_hat"], "events": ["carry_box", "ice_cream", "photo"]}, "teen"),
    # a garden with the teenager playing catch and a sleeping cat beside someone walking
    ("garden", 3, 24405, {"events": ["play_catch", "cat_sleeping", "carry_box", "walk_dog"]}, "teen"),
    # a playground with the other child on the slide, a sleeping dog and a pram
    ("playground", 2, 24406, {"events": ["slide", "dog_sleeping", "push_stroller", "wave"]}, "nia_slide"),
]


def ok(rec, rule):
    if rule is None:
        return True
    if rule == "teen":
        return any(e.get("asset", {}).get("family") == "person.leo" for e in rec["elements"])
    if rule == "nia_slide":
        els = {e["id"]: e for e in rec["elements"]}
        return any(it.get("template") == "slide" and any(els.get(i, {}).get("asset", {}).get("family") == "person.nia" for i in it["elements"]) for it in rec["items"])
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
