"""python vision/isolation_bench.py OUT [names...] : the isolation bench (v0.20 cases; earlier cases in isolation_v012.md to v019.md).

BENCH_LIB=<dir> runs it against another variant library (the side-by-side readings swapped a pose in a copy).

Each weak visual is built on its own: one template forced alone into a picture (no other events), then
cropped around that template's own elements (or a setting element), so a reader judges that one thing.
Writes OUT/<name>.png (the crop) and OUT/<name>_full.png (the whole single-event picture)."""
import json, os, sys
_OUT0 = os.path.abspath(sys.argv[1])
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); os.chdir(ROOT)
from PIL import Image
from scenegen.library import Library
from scenegen.generate import build_one
from scenegen.planner import USAGE

OUT = _OUT0
ONLY = set(sys.argv[2:])
os.makedirs(OUT, exist_ok=True)
lib = Library(lib_dir=os.environ["BENCH_LIB"]) if os.environ.get("BENCH_LIB") else Library()

# name: (setting, seed, forced templates, what to crop: "event", "full", or a setting element id or filler prefix,
#        accept rule or None)
BENCH = {
    # the bucket on the head drawn as a metal pail pulled down to the brows, rolled rim and ridges, a cap hidden under it
    "pail_a": ("park", 20101, {"contradictions": ["bucket_hat"]}, "event", ("backrow",)),
    "pail_b": ("park", 20102, {"contradictions": ["bucket_hat"]}, "event", None),
    "pail_c": ("street", 20103, {"contradictions": ["bucket_hat"]}, "event", None),
    # the drink a red takeaway cup with a white lid and a straw at the lips
    "drink_a": ("park", 20104, {"events": ["drink_bench"]}, "event", None),
    "drink_b": ("garden", 20105, {"events": ["drink_bench"]}, "event", None),
    "airdrink_a": ("street", 20106, {"contradictions": ["sitting_on_air"]}, "event", None),
    # the garden's wheelbarrow standing on its wheel and legs
    "barrow_a": ("garden", 20107, {"events": ["sweep"]}, "filler_wheelbarrow", ("el", "filler_wheelbarrow")),
    "barrow_b": ("garden", 20108, {"events": ["dig"]}, "filler_wheelbarrow", ("el", "filler_wheelbarrow")),
    # water from a pan and a hose landing inside the bed
    "pan_e": ("garden", 20109, {"contradictions": ["pan_watering"]}, "event", None),
    "hose_c": ("garden", 20110, {"events": ["hose_water"]}, "event", None),
    # the blown empty swing seat kept inside its frame
    "swing_a": ("garden", 20111, {"modules": ["windy_hat"]}, "swing", ("el", "swing_seat")),
    # round 2: the pail more tapered, one ridge, no lugs; the cup a quarter bigger with a thicker straw; the swing seat
    # pushed a little downwind and tilted instead of swung out
    "pail_d": ("park", 20101, {"contradictions": ["bucket_hat"]}, "event", ("backrow",)),
    "pail_e": ("garden", 20122, {"contradictions": ["bucket_hat"]}, "event", None),
    "drink_c": ("park", 20104, {"events": ["drink_bench"]}, "event", None),
    "swing_b": ("garden", 20111, {"modules": ["windy_hat"]}, "swing", ("el", "swing_seat")),
}


def crop_box(rec, what, tids=()):
    els = {e["id"]: e for e in rec["elements"]}
    if what == "event":
        ids = {i for it in rec["items"] if it.get("template") in tids for i in it["elements"]}
        # plus everything the event drew (setting-role svgs keyed to it are listed in the record too)
        boxes = [els[i]["bbox"] for i in ids if i in els and els[i].get("bbox")]
        boxes += [e["bbox"] for e in rec["elements"] if e.get("bbox") and e["id"].startswith(("toyball", "wavelines", "gusts", "seeds", "dustpan", "crownleaves", "speedlines"))]
        if "kite_in_tree" in tids:
            # the whole crown the kite hangs from
            boxes += [e["bbox"] for e in rec["elements"] if e.get("bbox") and e["id"] == "tree"]
    else:
        boxes = [e["bbox"] for e in rec["elements"] if e.get("bbox") and (e["id"] == what or e["id"].startswith(what))]
    x0, y0 = min(b[0] for b in boxes), min(b[1] for b in boxes)
    x1, y1 = max(b[2] for b in boxes), max(b[3] for b in boxes)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    w, h = max(x1 - x0 + 160, 420), max(y1 - y0 + 140, 340)
    return (int(max(0, cx - w / 2)), int(max(0, cy - h / 2)), int(min(1600, cx + w / 2)), int(min(1000, cy + h / 2)))


def fams_of(rec, tid):
    els = {e["id"]: e for e in rec["elements"]}
    return {els[i]["asset"]["variant"].split("__")[0] for it in rec["items"] if it.get("template") == tid
            for i in it["elements"] if i in els and els[i].get("asset")}


def accepted(rec, rule):
    if rule is None:
        return True
    els = {e["id"]: e for e in rec["elements"]}
    if isinstance(rule, tuple):
        if rule[0] == "fam":
            return bool(fams_of(rec, rule[1]) & set(rule[2]))
        if rule[0] == "el":
            return any(e["id"].startswith(rule[1]) for e in rec["elements"])
        if rule[0] == "obj":
            return any(it.get("template") == "about_to_trip" and rule[1] in it["text"] for it in rec["items"])
        if rule[0] == "branchbird":
            return any(it.get("template") == "bird_perched" and "branch" in it["text"] for it in rec["items"])
        if rule[0] == "fencebird":
            return any(it.get("template") == "bird_perched" and "fence" in it["text"] for it in rec["items"]) and \
                any(e["id"] == "clothesline" for e in rec["elements"])
        if rule[0] == "railbird":
            return any(it.get("template") == "bird_perched" and "fence" in it["text"] for it in rec["items"])
        if rule[0] == "noreel":
            return not any(e["id"] == "hose_reel" for e in rec["elements"])
        if rule[0] == "fencecat":
            return any(it.get("template") == "cat_stalks_bird" and "on the fence" in it["text"] for it in rec["items"])
        if rule[0] == "backrow":
            return any(e.get("asset", {}).get("family", "").startswith("person.") and e["bbox"][3] < 700 for e in rec["elements"] if e.get("bbox"))
    if rule == "kidwave":
        return any(it.get("template") == "wave" and any("child" in str(els[i].get("asset", {}).get("labels", {}).get("category", "")) for i in it["elements"] if i in els)
                   for it in rec["items"])
    if rule == "laundry":
        return any(e["id"] == "laundry" for e in rec["elements"])
    return True


for name, (st, seed, forced, what, rule) in BENCH.items():
    if ONLY and name not in ONLY:
        continue
    rec = None
    for k in range(40):
        USAGE.clear()
        r_, sc, fin = build_one(lib, 3, st, seed + 1000 * k, os.path.join(OUT, "_scenes"), forced=forced, require_band=False, max_tries=8, log=lambda *a: None)
        if r_ and accepted(r_, rule):
            rec = r_
            break
    if not rec:
        print(name, "FAIL", flush=True)
        continue
    png = os.path.join(OUT, "_scenes", rec["name"] + ".png")
    im = Image.open(png).convert("RGB")
    if what == "full":
        im.save(os.path.join(OUT, name + ".png"))
        print(name, rec["name"], "full", flush=True)
        continue
    try:
        if what == "event":
            box = crop_box(rec, "event", [t for v in forced.values() for t in v])
        elif what in ("wave",):
            box = crop_box(rec, "event", [what])
        else:
            box = crop_box(rec, what)
    except ValueError:
        print(name, "NO ELEMENT", what, flush=True)
        continue
    im.crop(box).save(os.path.join(OUT, name + ".png"))
    im.save(os.path.join(OUT, name + "_full.png"))
    print(name, rec["name"], box, flush=True)
