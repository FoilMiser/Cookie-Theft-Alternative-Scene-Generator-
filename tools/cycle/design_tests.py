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
    # a busy park: the older man's new bag, the sandwich bird, the newspaper dog with its own paws on the paper
    ("park", 4, 25401, {"modules": ["bird_steals", "ducks_bread"], "contradictions": ["dog_reading"], "events": ["carry_bag", "ice_cream"]}, "tomascarry"),
    # a street with someone else carrying the bag, a box carrier beside them, and the sandwich bird
    ("street", 3, 25402, {"modules": ["bird_steals"], "events": ["carry_bag", "carry_box", "photo"]}, None),
    # a garden with the painted fence and its roller, and the wheelbarrow's shadow
    ("garden", 3, 25403, {"events": ["paint_fence", "rake", "walk_dog"]}, "filler_wheelbarrow"),
    # the paw-printed fence in a garden with the barrow and a dig
    ("garden", 3, 25404, {"modules": ["paint_tracks"], "events": ["dig", "sweep"]}, "filler_wheelbarrow"),
    # a busy street: the white newspaper dog, the bag, the sandwich bird and the dropped ice cream
    ("street", 4, 25405, {"modules": ["bird_steals", "ice_cream_drop"], "contradictions": ["dog_reading"], "events": ["carry_bag"]}, None),
    # the square-wheeled barrow, whose own shadow also changed, beside a painter
    ("garden", 3, 25406, {"contradictions": ["square_wheel"], "events": ["paint_fence", "plant_flowers"]}, None),
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
