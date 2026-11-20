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
PREV, CUR = "v057", "v058"

# v0.58: the brief was the list of the screen of v0.57 (vision/flaws_v057.md). The drawings and rules of the scene are behind scene.sw58 (placement
# revision 52) and four poses of the cast behind TPDB_<NAME>58 (builder 0.58.0); two blind benches read each one first, a reader in one arm only
# (vision/isolation_v058.md). The release is like for like again: the records of v0.57 were built again one by one, and the screen is vision/flaws_v058.md
REDRAWN_NOTES = {
    "square_wheel": "The wheelbarrow is wheeled by a grown figure, a hand on each handle, as the bicycle is held by its owner. Two new wheels were drawn first and changed nothing: in 30 fresh readings the square wheel stood in no description. Wheeled, it is in the description in 9 bench readings of 16 for none of 16 parked, and unseen in none for 4. 1.00 in eleven pictures, six of them wheeled barrows, for 0.967: 'The odd thing is the wheelbarrow: its wheel is drawn as a square with an X/spokes inside rather than a round wheel, which would not roll.' One reader of the six keeps the wheel to the unsure section.",
    "kite_in_tree": "The child holds the reel in a lowered hand and raises the other arm toward the kite. On the bench the kite was stuck with nothing beside it in 24 readings of 34, for 7 of 16 with the reel held up. In the screen it reads 1.00 in six pictures with a hedge in three, as many as before: 'it could also be read as flying just in front of the tree, but it overlaps the branches and the string is slack and looped on the ground, which suggests stuck.' The reel lying on the grass read a little better and was not taken: no reader could then say what the child holds.",
    "seesaw_heavy": "The man sits with his thighs along the pad of his seat and his shins upright. Off his seat in 1 bench reading of 68, for 6 of 15, and no reader of the screen doubts it. The child is the one v0.57 drew, after two new poses of her read worse. 0.967 in five pictures, for 1.00: one reader gives his weight and leaves open whether she is stuck: 'The man sits on the low end, which rests near the ground, and the girl is up on the raised end holding the handle, which fits the heavier person being lower.' First on the next list.",
    "seesaw": "The child on the raised end sits on her pad with her thighs along the plank, both fists on the handle and her legs hanging. Off or above her seat in none of 8 bench readings, for 3 of 12. 1.00 in five pictures, as it was, with no oddity.",
    "play_catch": "The thrown ball keeps off the rails of a fence. Tied to the fence in none of 8 bench readings, for 3 of 9. 1.00 in six pictures, as it was.",
    "sitting_on_air": "Not changed. 1.00 in four pictures; the fourth is the busiest garden, where it stands in the place of the wheelbarrow.",
    "carry_bag": "Not changed, and 1.00 for 0.938 by a rule of the scorers and not by a drawing: a figure called by a word outside the names of the key has that word in a field of its own and loses nothing for it. The picture is the same to the pixel, and its reader wrote: 'In the centre, a boy or young man in a red T-shirt and blue jeans is walking to the left with a yellow shopping bag.'",
    "paint_fence": "Not changed, and 1.00 for 0.958 by the same rule of the scorers.",
}

# the next list: every template under 0.9, and every one that fails the gate. v0.58 has none of either; the list for v0.59 is vision/flaws_v058.md
WEAK_NOTES = {}
SCREEN_NOTE = ("The v0.58 screen read the set pictures and enough probe pictures that every template appeared in at least three "
               "screened pictures, and every angle an animal is drawn at in at least two. "
               "1,442 of 1,458 items had full marks and none was misread. All 64 templates pass the gate, as in v0.57, and 63 of them read 1.00. "
               "The square wheel, at 0.967 in v0.57, reads 1.00 in eleven pictures, six of them wheelbarrows that a grown figure wheels. "
               "The heavy seesaw, at 1.00 in v0.57, reads 0.967: one reader of five left open whether the child is stuck. "
               "Fifteen of the 16 items under full marks are the clouds or a tree that a reader left out. Nothing was mended, swapped or read again after the screen. "
               "The release is like for like: of the 136 pictures of v0.57, 113 came back to the pixel, 22 were drawn again or moved, and one was replaced. "
               "In the 113, 1,136 of 1,175 items have the score they had, and 37 of the 39 others are the clouds or a tree. "
               "Two benches read every drawing before it went into scenes, 248 readings of whole pictures, each reader with the pictures of a thing in one arm only. "
               "Two templates read 1.00 for 0.94 and 0.96 by a new rule of the scorers and not by a drawing: a man called a boy no longer costs a half mark. "
               "With the 3 full marks halved that stand beside another reading in the description itself, all 64 pass; with the 58 halved as well that have another reading only in the unsure section, which is what v0.57 counted, 55 pass, for 54. "
               "AI readers describe exhaustively, so the screen filters illegible drawing but cannot rank the templates by difficulty, which is the job of the pilot.")


FIXES = [("crop:probes_v057/T3_garden_s23030.png@720,640,1100,900>probes/T3_garden_s23030.png@570,600,1030,1000", "The wheelbarrow with a square wheel",
          "v0.57: parked on the grass, its wheel hedged as a stylised one or not seen. v0.58: wheeled by a grown figure. In the description in 9 bench readings of 16, for none of 16: 'Its wheel is a square, not a round wheel, so it could not roll properly.'"),
         ("crop:scenes_v057/T2_playground_s042.png@100,560,520,1000>scenes/T2_playground_s042.png@100,560,520,1000", "The child of the kite in the tree",
          "v0.57: the reel held up before the chest, as one holds it who is flying a kite. v0.58: the reel in a lowered hand, the other arm raised toward the kite. Stuck with nothing beside it in 24 bench readings of 34, for 7 of 16; in the screen a hedge in three pictures of six, as before."),
         ("crop:probes_v057/T3_playground_s23742.png@940,560,1420,920>probes/T3_playground_s23742.png@940,560,1420,920", "The man on the heavy seesaw",
          "v0.57: his feet far out ahead, one long limb across the plank; in front of his seat to nine bench readers of ten. v0.58: thighs along the pad, shins upright. Off his seat in 1 bench reading of 68. The child is not changed: two new poses of her read worse."),
         ("crop:probes_v057/T3_playground_s23703.png@940,560,1430,910>probes/T3_playground_s23703.png@940,560,1430,910", "The raised rider of the seesaw",
          "v0.57: sitting as on a bench over a plank that falls away. v0.58: on her pad, both fists on the handle, legs hanging: 'A smaller girl in a pink outfit sits on the raised right end holding her handle, with her legs dangling.'"),
         ("crop:probes_v057/T3_garden_s23012.png@520,410,1020,810>probes/T3_garden_s23012.png@520,500,1020,900", "The ball and the fence",
          "v0.57: the flat ball at the height of a rail of the fence. v0.58: the ball keeps off the rails, and the game stands further forward. Tied to the fence in none of 8 bench readings, for 3 of 9."),
         ("crop:scenes_v057/T4_garden_s552986.png@200,560,640,900>scenes/T4_garden_s552986.png@380,640,780,1000", "The busiest garden",
          "v0.57: the wheelbarrow with a square wheel, parked. v0.58: the garden has no room for a figure at the barrow, and a woman who sits on nothing stands in its place, read in full."),
         ("person.dev__seesaw_low_look__worried__y090", "The grown rider on the low end",
          "v0.57: the feet 34 cm ahead of the hips and apart. v0.58: the thighs side by side along the pad, rising to the knee, and the near shin upright under it.")]



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
