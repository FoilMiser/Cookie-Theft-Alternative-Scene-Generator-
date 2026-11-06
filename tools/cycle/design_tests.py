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
    # v0.35: a garden: the child on the swing, swung out in the wider frame, among others
    ("garden", 3, 35401, {"events": ["swing", "rake"]}, None),
    # a garden: the same, by a kite stuck in a tree and someone carrying a box
    ("garden", 3, 35402, {"modules": ["kite_in_tree"], "events": ["swing", "carry_box"]}, None),
    # a garden: the same, with someone sitting on nothing
    ("garden", 3, 35403, {"contradictions": ["sitting_on_air"], "events": ["swing"]}, None),
    # a garden: the swing in the wind
    ("garden", 3, 35404, {"modules": ["windy_hat"], "events": ["swing", "cat_sleeping"]}, None),
    # a garden: the wind, with no pile swept or raked (revision 33), someone digging and a cat on the fence
    ("garden", 3, 35405, {"modules": ["windy_hat"], "events": ["dig", "cat_on_fence"]}, None),
    # a park: sweeping and raking with no wind, which revision 33 leaves as they were
    ("park", 3, 35406, {"events": ["sweep", "rake"]}, None),
]


def ok(rec, rule):
    if rule is None:
        return True
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
