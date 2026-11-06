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
    # v0.36: a garden: the grandfather under the bucket, with his moustache and the bucket sat higher, among others
    ("garden", 3, 36401, {"contradictions": ["bucket_hat"], "events": ["rake", "cat_sleeping"]}, "tomasbucket"),
    # a park: the same, by the pond
    ("park", 3, 36402, {"contradictions": ["bucket_hat"], "events": ["fishing"]}, "tomasbucket"),
    # a street: the same
    ("street", 3, 36403, {"contradictions": ["bucket_hat"], "events": ["carry_bag"]}, "tomasbucket"),
    # a park: the grandfather in his other poses, with the moustache, fishing or planting
    ("garden", 3, 36404, {"events": ["plant_flowers", "rake"]}, "tomas"),
    # a garden: the storm pointer, the washing line empty (revision 34)
    ("garden", 3, 36405, {"modules": ["rain_coming"], "events": ["dig"]}, "clothesline"),
    # a garden: sweeping on the path by the gate, every head clear of its knob (revision 34)
    ("garden", 3, 36406, {"contradictions": ["sweep_fork"], "events": ["sweep"]}, None),
]


def ok(rec, rule):
    if rule is None:
        return True
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
