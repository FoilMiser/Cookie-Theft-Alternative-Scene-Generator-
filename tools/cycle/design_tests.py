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
    # a park: the begging dog with a walker and a bag about, the ball on its branch, the eater and the runner
    ("park", 4, 28401, {"modules": ["dog_begs", "ball_in_tree"], "events": ["carry_bag", "ice_cream", "run"]}, None),
    # a playground: the begging dog beside a kite and a jumper (v0.27: "or be watching the kite, or doing a trick for the boy")
    ("playground", 3, 28402, {"modules": ["dog_begs"], "events": ["fly_kite", "jump", "ice_cream"]}, None),
    # a playground: the riders further in on one shadow, the walking eater with open eyes
    ("playground", 3, 28403, {"modules": ["seesaw_heavy"], "events": ["ice_cream", "kick_ball"]}, None),
    # a street: the splat, the ball in the tree, the square wheel, a dog walked by
    ("street", 3, 28404, {"modules": ["ice_cream_drop", "ball_in_tree"], "contradictions": ["square_wheel"], "events": ["walk_dog", "photo"]}, None),
    # a garden: the shadows of a sleeper, a digger, a waver, the hose
    ("garden", 3, 28405, {"events": ["dog_sleeping", "dig", "wave", "hose_water"]}, None),
    # a park: faces with closed eyes at a picnic, a runner and a pram, a bird on its branch
    ("park", 3, 28406, {"events": ["picnic", "run", "push_stroller", "bird_perched"]}, None),
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
