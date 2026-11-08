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
    # v0.41 (builder 0.41.0: the begging dog's forelegs folded, elbows forward and paws tipped down at the chest; revision 39 draws nothing new):
    # a street: a dog begging in profile, a sweeper, an ice cream
    ("street", 3, 41402, {"modules": ["dog_begs"], "events": ["sweep", "ice_cream"], "yaws": {"dog_begs": 90}}, None),
    # a park: a dog begging at an angle, a kicker, a raker
    ("park", 3, 41405, {"modules": ["dog_begs"], "events": ["kick_ball", "rake"], "yaws": {"dog_begs": 45}}, None),
    # a park: a dog begging in profile, a game of catch
    ("park", 3, 41406, {"modules": ["dog_begs"], "events": ["play_catch"], "yaws": {"dog_begs": 90}}, None),
    # v0.40 (revision 38 and builder 0.40.0: the reach for a blown hat with one hand, the hose in two hands, the goat's graze and its tuft ahead of the
    # muzzle, the heaps of dry leaves, the ice-cream eater not tiny at the back):
    # a park: a hat blown off, an ice cream, the goat grazing at an angle
    ("park", 3, 40401, {"modules": ["windy_hat"], "events": ["ice_cream", "goat_grazing"]}, "angled"),
    # a garden: the hose inspected, a raker's dry leaves, the washing hung out
    ("garden", 3, 40402, {"modules": ["blocked_hose"], "events": ["rake", "hang_laundry"]}, None),
    # a street: a sweeper's dry leaves under the one tree, an ice cream, a reader on a bench
    ("street", 3, 40403, {"events": ["sweep", "ice_cream", "read_bench"]}, None),
    # a park: the goat at an angle, an ice cream, a kicker
    ("park", 3, 40404, {"events": ["goat_grazing", "ice_cream", "kick_ball"]}, "angled"),
    # v0.39 (revision 37 and builder 0.39.0: the cast redrawn, the animals at more angles than profile, the broom's heap for summer, the caught ball
    # short of the hands):
    # a park: the goat grazing at an angle, a dog walked, a kicker
    ("park", 3, 39401, {"events": ["goat_grazing", "walk_dog", "kick_ball"]}, "angled"),
    # a street: a dog begging at a bench, a sweeper's summer heap, a shopper with a bag
    ("street", 3, 39402, {"modules": ["dog_begs"], "events": ["sweep", "carry_bag"]}, "angled"),
    # a garden: the washing hung out, a raker, a cat stalking a bird
    ("garden", 3, 39403, {"modules": ["cat_stalks_bird"], "events": ["hang_laundry", "rake"]}, "stalkground"),
    # a park: a game of catch, a dog at play, a reader on a bench
    ("park", 3, 39404, {"events": ["play_catch", "dog_playing", "read_bench"]}, "angled"),
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
    if rule == "angled":
        # (revision 37: at least one template's animal turned from profile)
        return any(e.get("asset", {}).get("family", "").startswith("animal.") and not e["asset"]["variant"].endswith("__y090")
                   and not e["asset"]["family"].startswith(("animal.bird", "animal.duck")) for e in rec["elements"])
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
