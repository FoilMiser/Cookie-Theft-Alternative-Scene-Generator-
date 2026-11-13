"""Build the showcase site (index.html + img/) from generated scenes, counts, gallery renders and the
blind legibility screen.

    python -m scenegen.site --scenes scenes --gallery assets/cast/gallery6 --old-gallery <v0.5 gallery> \
        --combos combos.json --screen vision/screen_summary.json --out site
"""
import argparse
import glob
import json
import os

from PIL import Image, ImageDraw

from . import templates as TP
from .difficulty import SALIENCE_REF, TIERS, WEIGHTS

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_HTML = os.path.join(HERE, "site_template.html")

DESCR = {
    # inference modules
    "blocked_hose": "A dog or goat stands on the hose; the person peers into the dry nozzle. Cause, 2 steps.",
    "rain_coming": "Dark clouds roll in while someone points up at the sky. Prediction, 1 step.",
    "cat_stalks_bird": "A cat crouches low, eyes on a bird pecking nearby. Intention, 1 step (gaze checked).",
    "ball_in_tree": "A ball sits up in a tree; a child points or reaches for it, upset. Cause, 1 step.",
    "kite_in_tree": "A kite is caught in a tree, its string still in the child's hand. Cause, 1 step.",
    "ice_cream_drop": "A child holds an empty cone; the scoop is on the ground and a dog is licking it. Cause, 1 step.",
    "about_to_trip": "Someone reads while walking straight toward a long low box, or a bucket beside another box. Prediction, 1 step.",
    "dog_begs": "Someone eats on a bench; a dog sits beside it looking up at the food. Intention, 1 step (gaze checked).",
    "sprinkler_package": "A sprinkler sprays toward a package left on the grass. Prediction, 1 step.",
    "paint_tracks": "Fresh paint on the fence, a paint tray, and paw prints leading to the dog. Cause, 2 steps.",
    "windy_hat": "A hat blows off; its owner reaches after it. Cause, 2 steps.",
    "bird_steals": "A bird pecks at a sandwich on the bench while the reader isn't looking. Viewpoint, 2 steps.",
    "lost_balloon": "A balloon floats away high in the sky; a child below reaches up, upset. Cause, 1 step.",
    "ducks_bread": "Someone throws bread on the pond; a duck bends to a crumb. Intention, 1 step.",
    "seesaw_heavy": "A grown-up sits on the low end of the seesaw; a child is stuck high in the air. Cause, 1 step.",
    "dog_wants_walk": "A dog sits by the back door with its leash in its mouth. Intention, 1 step.",
    # contradictions
    "water_upward": "Water from a watering can arcs up into the air. Physical.",
    "floating_box": "A box floats in mid-air with nothing holding it up. Physical.",
    "square_wheel": "A wheelbarrow or bicycle with square wheels. Physical.",
    "fish_in_tree": "A fish sitting in a tree. Biological.",
    "pan_watering": "Watering the flowers with a frying pan. Functional.",
    "sweep_fork": "Sweeping with a giant fork. Functional.",
    "bucket_hat": "Wearing a bucket as a hat. Functional.",
    "sitting_on_air": "Someone sits reading or drinking with no chair under them. Physical.",
    "ladder_nothing": "A ladder leans on nothing at all. Physical.",
    "dog_reading": "A dog sits up reading a newspaper. Biological.",
}

# the screens the page compares: the current one and the one before it
PREV, CUR = "v049", "v050"

# v0.50 worked the list of the v0.49 screen (vision/flaws_v049.md) on the bench (vision/isolation_v050.md, vision/design_tests_v050.md): the grown
# figures drawn again, the children on the seesaw seated, the lost balloon, the stake of the goat, the held balloon and the pole of the painter;
# the stopped hose and the slide were benched and left, and the dogs were looked at and left (vision/flaws_v050.md)
REDRAWN_NOTES = {
    "seesaw": "A child on the seesaw is set down until its own drawing rests on the plank, and the handle is a grab bar ahead of the knees. In full in five pictures, as in three before; what changed is the remark. v0.49: 'perches a little above the plank'. v0.50: no rider above the plank in any picture, 'sitting on the raised left end of the seesaw, holding the handle'.",
    "seesaw_heavy": "The child is seated the same way, the grown rider as before. In full in five pictures, with two of its marks a judgement call: 'most likely she is calling to the man'. The grown rider is once 'partly seated on the board and partly crouched/sitting in front of it'.",
    "lost_balloon": "In the garden the end of the string had been lifted onto the hedge, far from the hand: 'The red balloon may belong to the girl (she let go) or to someone else; she seems to be reaching for it.' It now ends a little above the reaching hand in every setting. In full in five pictures, and the balloon belongs to nobody else in any. In three the end is now near something else: 'tied to something on the fence'.",
    "goat_grazing": "The stake is half as tall again and the rope goes round its upper part in two turns. In full in five pictures, and no reader calls the stake short: 'it is just tethered, not escaping'.",
    "balloon": "The string hangs in a loose S, where it was a straight line that two bench readers of three took for a stick. In full in five pictures, and a stick in none.",
    "paint_fence": "The pole of the roller is dark, where it had the colour of the fence behind it. In full in nine pictures, painting in each. One reader of one picture: 'looks almost like a separate pale cylinder against the fence'.",
    "blocked_hose": "Benched with no swelling before the paw, and left as it was: without the swelling one bench reader of three went on to the stopped water, for two of three with it. Two half marks in one picture of five: 'actually on the hose or just behind the bulge'.",
    "slide": "Left as it was, after four places for the slider read alike on the bench. In full in five pictures. One reader: 'slightly above the chute surface in places, but it reads normally as sliding'.",
    "bird_steals": "Not worked. A half mark and a zero in five pictures, the theft not said: 'or he may be sharing it'.",
    "ducks_bread": "Not worked. A half mark in three pictures: 'her hand item is small and hard to make out'.",
    "dog_sleeping": "Looked at and left. In full in five pictures, with two of its marks beside another reading: 'The dog could be asleep, resting, or crouching scared of the coming storm.'",
    "dog_wants_walk": "Looked at and left. In full in five pictures, with three of its marks beside another reading: 'or simply carrying the leash'.",
    "dog_begs": "Looked at and left. In full in six pictures, with four of its marks beside another reading.",
}

# the two templates that fail the v0.50 gate, first on the list for v0.51 (vision/flaws_v050.md, R1 and R2)
WEAK_NOTES = {
    "play_catch": "Fails the gate: four half marks in two pictures of five. In both a small girl has thrown to a grown woman, and the ball is drawn at the end of its path, by the hands of the woman: 'the ball is either just leaving the woman or arriving at her'. The three other pictures read right. Next: the ball early on its path with the dashed line only behind it, and the thrower standing with the arm through.",
    "square_wheel": "Fails the gate: a half mark and the one misread of the screen, both in one picture of four. The three bicycles are read at once. The wheelbarrow has the hose of the sprinkler on the ground behind its square wheel: 'looks like a hose reel or a fan-like grate'. Next: a rule that keeps any hose off the barrow, and the wheel of the barrow drawn as the wheel of the bicycle is.",
}
SCREEN_NOTE = ("The v0.50 screen read the set pictures and enough probe pictures that every template appeared in at least three "
               "screened pictures, and every angle an animal is drawn at in at least two. What makes a grown figure read as grown was measured first, in whole scenes: pictures of the v0.49 screen were built again with four casts and read blind, and marks of age with a smaller head left one young name in 45 appearances, where the cast of v0.49 had 13. "
               "946 of 992 items had full marks and one was misread. 62 of the 64 templates pass the gate, where all 64 did in v0.49: the game of catch and the square wheel fail, each in a set picture. Nothing was mended, swapped or read again after the screen. "
               "With the 33 full marks that stand beside another reading halved, 52 of the 64 pass. "
               "Of the 46 items under full marks, 35 are the clouds or a tree, left out by six readers. "
               "Every grown figure is drawn anew, so no picture is the same as in v0.49; five of the sixteen cells have the templates of v0.49. "
               "AI readers describe exhaustively, so the screen filters illegible drawing but cannot rank the templates by difficulty, which is the pilot's job.")


FIXES = [("pair:person.ana__stand__smile__y000>person.ana__stand__smile__y000", "The woman in purple",
          "v0.49: a girl first in 9 of her 24 screened pictures: 'Girl, centre-front: dark ponytail, purple top, teal trousers; running to the right.' v0.50: as tall as the woman in yellow, with a bust, and a head 0.86 of its size on the same body. A girl first in 1 of 18, and the runner is now 'Woman 2, right, front: dark hair, purple top, teal trousers; running to the right, speed lines behind her.'"),
         ("pair:person.mei__stand__smile__y000>person.mei__stand__smile__y000", "The woman in the yellow dress",
          "v0.49: a girl first in 5 of her 18 screened pictures. v0.50: a bust, the dress to below the knee, and the smaller head. A girl in none of 18."),
         ("pair:person.dev__stand__smile__y000>person.dev__stand__smile__y000", "The man in green",
          "v0.49: a boy first in 4 of his 25 screened pictures, and the beard named in none. v0.50: a fuller beard that stands off the chin, on the smaller head. A boy in none of 20, and the beard named in 16: 'short dark hair and beard, green shirt, beige trousers'."),
         ("pair:person.ben__stand__smile__y000>person.ben__stand__smile__y000", "The man in the red shirt",
          "v0.49: the moustache named in 13 of his 22 screened pictures. v0.50: the same moustache on the smaller head, named in 7 of 23. He is the one grown figure still called a boy, twice, sweeping: 'Boy, left front: brown hair, red shirt, blue jeans; sweeping leaves on the path with a broom.' On the list for v0.51."),
         ("pair:person.rosa__stand__smile__y000>person.rosa__stand__smile__y000", "The older woman",
          "The grandparents have the smaller head too. The glasses of the older woman are named in all 14 of her screened descriptions and her bun in 9."),
         ("pair:person.kai__stand__smile__y000>person.kai__stand__smile__y000", "A child, unchanged",
          "The children and the teenager are as v0.49 drew them. Beside them a grown figure is now about five heads tall, for four and a third."),
         ("crop:vision/isolation_v050/round1/iso_29.png@0,0,570,340>vision/isolation_v050/round2/iso_04.png@0,0,570,340", "The children on the seesaw",
          "v0.49: 'The right child appears to sit slightly above/in front of the plank rather than firmly on it'. v0.50: each child is set down until its own drawing rests on the plank, and the handle is a grab bar that comes down to the plank ahead of the knees: 'holding a black curved handle'. One seed, cut out for the bench."),
         ("crop:vision/isolation_v050/round1/iso_03.png@0,0,420,688>vision/isolation_v050/round2/iso_05.png@0,0,420,622", "The string of the lost balloon",
          "v0.49, in the garden: the end of the string lifted onto the hedge above the fence, 'so the link between him and that balloon is implied rather than shown'. v0.50: the end a little above the reaching hand, as in the other settings. Escaped from this child to all three bench readers of each drawing."),
         ("crop:vision/isolation_v050/round1/iso_07.png@0,0,420,305>vision/isolation_v050/round1/iso_11.png@0,0,420,305", "The stake of the goat",
          "v0.49: 'looks very short; the goat could be tethered or just standing by a stake'. v0.50: half as tall again, with the rope in two turns round its upper part. Tethered to both bench readers, and still 'a short brown wooden stake' to the second."),
         ("crop:vision/isolation_v050/round4/iso_07.png@0,0,420,370>vision/isolation_v050/round4/iso_02.png@0,0,420,370", "The string of a held balloon",
          "v0.49: a straight line, and a stick to two bench readers of three: 'so it could read as a stick (a balloon on a stick) rather than a string'. v0.50: a loose S, and a string to three of three."),
         ("crop:vision/isolation_v050/round4/iso_12.png@0,0,420,386>vision/isolation_v050/round4/iso_05.png@0,0,420,386", "The pole of the painter",
          "v0.49: the pole had the colour of the fence behind it, so the head of the roller stood alone above the hands: 'The roller looks a little small and oddly held'. v0.50: a dark pole, a little thicker. A long-handled roller to all six bench readers.")]



# v0.31: the whole document, as the publishing route refuses a page with no doctype. This is the skeleton the old route put round the template, so the page renders as it did.
PAGE_OPEN = ('<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover">'
             '<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
             'html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}'
             'img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n')
PAGE_CLOSE = "\n</body></html>"


def webp(src, dst, size=None, gray=False, q=86):
    im = Image.open(src)
    im = im.convert("L" if gray else "RGB") if im.mode not in ("RGBA",) else im
    if size:
        im.thumbnail(size, Image.LANCZOS)
    im.save(dst, "WEBP", quality=q, method=6)
    return im.size


def crop_tile(png, dst, scale, pad=6):
    im = Image.open(png).convert("RGBA")
    bb = im.getbbox()
    if bb:
        im = im.crop((max(0, bb[0] - pad), max(0, bb[1] - pad), min(im.width, bb[2] + pad), min(im.height, bb[3] + pad)))
    im = im.resize((max(1, round(im.width * scale)), max(1, round(im.height * scale))), Image.LANCZOS)
    im.save(dst, "WEBP", quality=88, method=6)
    return im.size


def portrait(png, man, dst):
    m = json.load(open(man))
    im = Image.open(png).convert("RGBA")
    A = m["anchors"]
    ht, ey = A["head_top"]["px"], A["eye_L"]["px"]
    cx = (A["eye_L"]["px"][0] + A["eye_R"]["px"][0]) / 2
    size = (ey[1] - ht[1]) * 2.6
    top = ht[1] - 10
    crop = im.crop((round(cx - size * 0.56), round(top), round(cx + size * 0.56), round(top + size)))
    crop = crop.resize((220, round(220 * crop.height / crop.width)), Image.LANCZOS)
    crop.save(dst, "WEBP", quality=90, method=6)


def fix_pairs(old_dir, new_dir, gimg):
    """Tiles of the same variant rendered by the previous and the current cast."""
    out = []
    if not (old_dir and os.path.isdir(old_dir) and new_dir and os.path.isdir(new_dir)):
        return out
    olds = {os.path.basename(f)[:-5]: f for f in glob.glob(os.path.join(old_dir, "*.json"))}
    news = {os.path.basename(f)[:-5]: f for f in glob.glob(os.path.join(new_dir, "*.json"))}
    for key, label, note in FIXES:
        a = b = None
        if key.startswith("crop:"):
            # v0.22: a drawing of the scene composer (not a cast render), cut from an old and a new picture
            tiles = []
            for tag, spec in zip(("old", "new"), key[5:].split(">")):
                path, box = spec.split("@")
                if not os.path.exists(path):
                    break
                bx = [int(v) for v in box.split(",")]
                name = f"fix_{tag}_{os.path.basename(os.path.dirname(path))}_{os.path.basename(path)[:-4]}_{bx[0]}_{bx[1]}.webp"     # (two crops of one picture, or of two folders, stay two files)
                im = Image.open(path).convert("RGB").crop(tuple(bx))
                im.save(os.path.join(gimg, name), "WEBP", quality=90, method=6)
                tiles.append({"src": f"img/g/{name}", "w": im.width, "h": im.height})
            if len(tiles) == 2:
                out.append({"label": label, "note": note, "old": tiles[0], "new": tiles[1]})
            continue
        if key.startswith("pair:"):
            a, b = key[5:].split(">")
            if a not in olds or b not in news:
                continue
            tiles = []
            for tag, d, v in (("old", old_dir, a), ("new", new_dir, b)):
                m = json.load(open(os.path.join(d, v + ".json")))
                name = f"fix_{tag}_{v.replace('.', '_')}.webp"
                w, h = crop_tile(os.path.join(d, m["files"]["image"]["path"]), os.path.join(gimg, name), 0.42)
                tiles.append({"src": f"img/g/{name}", "w": w, "h": h})
            out.append({"label": label, "note": note, "old": tiles[0], "new": tiles[1]})
            continue
        if key.startswith("portrait:"):
            v = key[9:]
            if v in olds and v in news:
                tiles = []
                for tag, d in (("old", old_dir), ("new", new_dir)):
                    m = json.load(open(os.path.join(d, v + ".json")))
                    name = f"fix_{tag}_p_{v.replace('.', '_')}.webp"
                    portrait(os.path.join(d, m["files"]["image"]["path"]), os.path.join(d, v + ".json"), os.path.join(gimg, name))
                    w, h = Image.open(os.path.join(gimg, name)).size
                    tiles.append({"src": f"img/g/{name}", "w": w, "h": h})
                out.append({"label": label, "note": note, "old": tiles[0], "new": tiles[1]})
            continue
        if key.startswith("animal:"):
            spec = key[7:]
            if ">" in spec and spec != "lie>sleep":
                o, n = spec.split(">")
                a = next((v for v in sorted(olds) if v.startswith(f"animal.dog_01__{o}__")), None)
                b = next((v for v in sorted(news) if v.startswith(f"animal.dog_01__{n}__")), None)
            elif spec == "sit":
                a = b = next((v for v in sorted(olds) if v.startswith("animal.dog_01__sit__") and v in news), None)
            elif spec == "lie>sleep":
                a = next((v for v in sorted(olds) if v.startswith("animal.dog_01__lie__")), None)
                b = next((v for v in sorted(news) if v.startswith("animal.dog_01__sleep__")), None)
            elif spec == "goat_stand":
                a = b = next((v for v in sorted(olds) if v.startswith("animal.goat_01__stand__") and v in news), None)
            elif spec == "fly":
                a = b = next((v for v in sorted(olds) if v.startswith("animal.bird_01__fly__") and v in news), None)
        elif key.startswith("person:"):
            a = b = next((v for v in sorted(olds) if v.startswith("person." + key[7:] + "__") and v in news), None)
        elif "__" in key:
            a = b = key if (key in olds and key in news) else None      # v0.15: one variant id, rendered by both casts
        else:
            a = b = next((v for v in sorted(olds) if v.split("__")[1] == key and v in news), None)
        if not a or not b:
            continue
        tiles = []
        for tag, d, v in (("old", old_dir, a), ("new", new_dir, b)):
            m = json.load(open(os.path.join(d, v + ".json")))
            name = f"fix_{tag}_{v.replace('.', '_')}.webp"
            w, h = crop_tile(os.path.join(d, m["files"]["image"]["path"]), os.path.join(gimg, name), 0.42)
            tiles.append({"src": f"img/g/{name}", "w": w, "h": h})
        out.append({"label": label, "note": note, "old": tiles[0], "new": tiles[1]})
    return out


def build(scenes_dir, gallery_dir, combos_path, out, old_gallery=None, screen=None):
    img = os.path.join(out, "img")
    os.makedirs(img, exist_ok=True)
    scenes = []
    for f in sorted(glob.glob(os.path.join(scenes_dir, "T*.json"))):
        r = json.load(open(f))
        n = r["name"]
        webp(os.path.join(scenes_dir, n + ".png"), os.path.join(img, n + ".webp"))
        webp(os.path.join(scenes_dir, n + "_gray.png"), os.path.join(img, n + "_g.webp"), gray=True)
        webp(os.path.join(scenes_dir, n + ".png"), os.path.join(img, n + "_t.webp"), size=(560, 350), q=82)
        els = {e["id"]: e for e in r["elements"]}
        scenes.append({
            "name": n, "tier": r["tier"], "setting": r["setting"], "sky": r["sky"], "seed": r["seed"], "mirror": r["mirror"],
            "load": r["scene_load"], "counts": r["counts"], "pred": r["predicted"], "bands": r["bands"], "in_tier": r["in_tier"],
            "clutter": r["clutter"], "templates": r["templates"], "iso_of": r.get("isomorph_of"), "iso": r.get("isomorph_check"),
            "checks": r["checks"], "attempts": len(r.get("attempts", [])),
            "items": [{"id": it["id"], "type": it["type"], "text": it["text"], "b": it["b"], "p0": it["p0"], "pm1": it["pm1"],
                       "chain": it["chain"], "aoi": it["aoi_cells"], "f": it["features"], "tpl": it["template"],
                       "acc": it["accepted"] if isinstance(it["accepted"], list) else it["accepted"].get("what", []),
                       "boxes": [els[e]["bbox"] for e in it["elements"] if e in els and els[e].get("bbox")]} for it in r["items"]],
            "cast": [{"id": e["id"], "variant": e["asset"]["variant"]} for e in r["elements"] if e.get("asset")],
        })
    # gallery
    gal = {"actions": [], "animals": [], "lineup": [], "lineup45": [], "expr_a": [], "expr_b": []}
    from .library import CAST_DIR
    cat = json.load(open(os.path.join(CAST_DIR, "cast_catalog.json")))
    from .reach import reachable
    used_poses = set(reachable()) | {"stand"}
    n_used = sum(1 for a in cat["actions"] if a in used_poses)
    if gallery_dir and os.path.isdir(gallery_dir):
        gimg = os.path.join(img, "g")
        os.makedirs(gimg, exist_ok=True)
        K = 0.42
        for js in sorted(glob.glob(os.path.join(gallery_dir, "*.json"))):
            m = json.load(open(js))
            v = m["variant_id"]
            fam, pose, expr, yaw = v.split("__")
            png = os.path.join(gallery_dir, m["files"]["image"]["path"])
            name = v.replace(".", "_") + ".webp"
            label = m["labels"]["everyday_name"]
            if m["class"] == "animal":
                if pose not in used_poses:
                    continue
                w, h = crop_tile(png, os.path.join(gimg, name), K)
                gal["animals"].append({"src": f"img/g/{name}", "w": w, "h": h, "fam": fam, "pose": pose, "label": label})
                continue
            tile = None

            def get_tile():
                w, h = crop_tile(png, os.path.join(gimg, name), K)
                return {"src": f"img/g/{name}", "w": w, "h": h}
            used = False
            if pose == "stand" and expr == "smile" and yaw == "y000":
                tile = tile or get_tile()
                gal["lineup"].append(dict(tile, fam=fam, label=label))
                used = True
            if pose == "stand" and expr == "neutral" and yaw == "y045":
                tile = tile or get_tile()
                gal["lineup45"].append(dict(tile, fam=fam, label=label))
                used = True
            if pose == "stand" and fam == "person.mei" and yaw == "y000":
                pname = "p_" + name
                portrait(png, js, os.path.join(gimg, pname))
                gal["expr_a"].append({"src": f"img/g/{pname}", "expr": expr})
                used = True
            if pose == "stand" and fam == "person.kai" and yaw == "y045":
                pname = "p_" + name
                portrait(png, js, os.path.join(gimg, pname))
                gal["expr_b"].append({"src": f"img/g/{pname}", "expr": expr})
                used = True
            # v0.15: the gallery shows the actions the templates use; spare actions stay in the cast but out of the gallery
            if pose in cat["actions"] and pose in used_poses and not any(x["pose"] == pose for x in gal["actions"]) and (pose != "stand" or yaw == "y045"):
                tile = tile or get_tile()
                a = cat["actions"].get(pose, {})
                gal["actions"].append(dict(tile, fam=fam, pose=pose, expr=expr, desc=a.get("description", pose), label=label, tags=a.get("tags", [])))
        order = {e: i for i, e in enumerate(cat["people_expressions"])}
        gal["expr_a"].sort(key=lambda x: order.get(x["expr"], 99))
        gal["expr_b"].sort(key=lambda x: order.get(x["expr"], 99))
        aorder = {a: i for i, a in enumerate(cat["actions"])}
        gal["actions"].sort(key=lambda x: aorder.get(x["pose"], 999))
    gimg = os.path.join(img, "g")
    os.makedirs(gimg, exist_ok=True)
    fixes = fix_pairs(old_gallery, gallery_dir, gimg)
    scr = json.load(open(screen)) if screen and os.path.exists(screen) else None
    if scr and scr.get(CUR, {}).get("by_template"):
        b5, b6 = scr.get(PREV, {}).get("by_template", {}), scr[CUR]["by_template"]
        scr["redrawn"] = [{"id": t, "before": b5[t]["mean"], "before_items": b5[t]["items"], "after": b6.get(t, {}).get("mean"),
                           "after_items": b6.get(t, {}).get("items", 0), "note": REDRAWN_NOTES[t]}
                          for t in sorted(REDRAWN_NOTES, key=lambda t: b5.get(t, {}).get("mean", 9)) if t in b5]
        # v0.47: a template whose mean is at the bar and which fails the gate on a misread is on the next list too
        gate_file = os.path.join(os.path.dirname(screen), CUR, "gate.json") if screen else ""
        failed = {t for t, v in json.load(open(gate_file)).items() if v["status"] == "fail"} if gate_file and os.path.exists(gate_file) else set()
        scr["weak"] = [{"id": t, "mean": b6[t]["mean"], "items": b6[t]["items"], "note": WEAK_NOTES.get(t, "")}
                       for t in sorted(b6, key=lambda t: b6[t]["mean"]) if b6[t]["mean"] < 0.9 or t in failed]
        for k in ("v04", "v05", "v06", "v07", "v08", "v09", "v010", "v011", "v012", "v013", "v014", "v015", "v016", "v017", "v018", "v019", "v020", "v021"):
            scr.get(k, {}).pop("by_template", None)
        if screen and os.path.exists(os.path.join(os.path.dirname(screen), CUR, "gate.json")):
            g = json.load(open(os.path.join(os.path.dirname(screen), CUR, "gate.json")))
            scr["gate"] = {st: sorted(t for t, v in g.items() if v["status"] == st) for st in ("pass", "too_few", "fail")}
        scr["note"] = (scr.get("note", "") + " " + SCREEN_NOTE).strip()
    combos = json.load(open(combos_path)) if combos_path and os.path.exists(combos_path) else {}
    tpl = {"events": [], "modules": [], "contradictions": []}
    for c in TP.EVENTS:
        tpl["events"].append({"id": c.id, "settings": list(c.settings), "sig": TP.SIG[c.id]})
    for c in TP.MODULES:
        tpl["modules"].append({"id": c.id, "settings": list(c.settings), "sig": TP.SIG[c.id], "desc": DESCR.get(c.id, ""), "sky": c.sky})
    for c in TP.CONTRADICTIONS:
        tpl["contradictions"].append({"id": c.id, "settings": list(c.settings), "domain": c.domain, "desc": DESCR.get(c.id, "")})
    people = [{"fam": f, "label": d["labels"]["everyday_name"], "accepted": d["labels"]["accepted_names"], "kind": d["kind"],
               "wardrobe": d.get("wardrobe", {})} for f, d in cat["families"].items() if d["class"] == "person"]
    animals = [{"fam": f, "label": d["labels"]["everyday_name"], "kind": d["kind"], "poses": [q for q in d["poses"] if q in used_poses]}
               for f, d in cat["families"].items() if d["class"] == "animal"]
    data = {"scenes": scenes, "gallery": gal, "combos": combos, "templates": tpl, "tiers": {str(k): v for k, v in TIERS.items()},
            "weights": {k: v for k, v in WEIGHTS.items() if k != "domain"} | {"domain": {str(k): v for k, v in WEIGHTS["domain"].items()}},
            "salience": SALIENCE_REF, "people": people, "animals": animals, "n_actions": n_used,
            "n_spare": len(cat["actions"]) - n_used,
            "n_expressions": len(cat["people_expressions"]), "fixes": fixes, "screen": scr}
    html = open(TEMPLATE_HTML).read().replace("/*__DATA__*/null", json.dumps(data, separators=(",", ":")))
    open(os.path.join(out, "index.html"), "w").write(PAGE_OPEN + html + PAGE_CLOSE)
    print("site:", len(scenes), "scenes,", len(gal["actions"]), "actions,", len(gal["animals"]), "animal poses")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scenes", default="scenes")
    ap.add_argument("--gallery", default=None)
    ap.add_argument("--combos", default=None)
    ap.add_argument("--out", default="site4")
    ap.add_argument("--old-gallery", default=None)
    ap.add_argument("--screen", default=None)
    a = ap.parse_args()
    build(a.scenes, a.gallery, a.combos, a.out, a.old_gallery, a.screen)


if __name__ == "__main__":
    main()
