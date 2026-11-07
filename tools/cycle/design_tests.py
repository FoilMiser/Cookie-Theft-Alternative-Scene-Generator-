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
    # v0.38 (revision 36; tests 1 and 2 are v0.37's pictures 12 and 74 rebuilt on their seeds, tpdb_work/rb38.py):
    # a garden: the washing hung out, its shirt dripping, beside a planter and a sweeper (the picnic and its basket are the park's, and the washing
    # the garden's, so the two baskets never meet; and the washing and a watering can placed 0 of 12 together, with the basket or without it)
    ("garden", 3, 38401, {"events": ["hang_laundry", "plant_flowers", "sweep"]}, "washbasket"),
    # a garden: the washing hung out among a digger and a dog at play
    ("garden", 3, 38402, {"events": ["hang_laundry", "dig", "dog_playing"]}, "washbasket"),
    # a garden: the storm pointer with a cat stalking a bird, the cat on the ground
    ("garden", 3, 38403, {"modules": ["rain_coming", "cat_stalks_bird"], "events": ["paint_fence"]}, "stalkground"),
    # a garden: the storm pointer among the templates of v0.37's picture 57 (where the cat on the fence was offered in the clouds' place), the cat left out
    ("garden", 3, 38404, {"modules": ["rain_coming", "dog_wants_walk", "paint_tracks"], "events": ["paint_fence", "play_catch", "dig"]}, "nofencecat"),
]


def ok(rec, rule):
    if rule is None:
        return True
    if rule == "washbasket":
        return any(e["id"].startswith("washbasket") for e in rec["elements"])
    if rule == "stalkground":
        return any(it.get("template") == "cat_stalks_bird" and "fence" not in it["text"] for it in rec["items"])
    if rule == "nofencecat":
        return not any(e["id"].startswith(("fencecat", "stalkcat")) and e.get("bbox") and e["bbox"][3] < 470 for e in rec["elements"])
    if rule == "noline":
        return not any(e["id"] in ("clothesline", "laundry") for e in rec["elements"])
    if rule == "tomasbucket":
        return any(e.get("asset", {}).get("variant", "").startswith("person.tomas__bucket_hat") for e in rec["elements"])
    if rule == "meisit":
        return any(e.get("asset", {}).get("variant", "").startswith("person.mei__sit_read") for e in rec["elements"])
    if rule == "tomas":
        return any(e.get("asset", {}).get("family") == "person.tomas" for e in rec["elements"])
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
    for k in range(80):
        USAGE.clear()
        r_, sc, fin = build_one(lib, t, st, seed + 1000 * k, OUT, forced=forced, require_band=False, max_tries=8, log=lambda *a: None)
        if r_ and ok(r_, rule):
            rec = r_
            break
    print(st, t, seed, rec["name"] if rec else ("FAIL " + json.dumps(fin, default=str)[:300]), flush=True)
