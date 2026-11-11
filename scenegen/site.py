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
PREV, CUR = "v047", "v048"

# v0.48 drew the heads, faces and hair again from a study of two figures, and every animal (vision/isolation_v048.md, vision/design_tests_v048.md): the one
# template it worked, the templates of the v0.47 list that carry the redrawn figures, the two that fell, and the plain events of the redrawn animals
# (vision/flaws_v048.md)
REDRAWN_NOTES = {
    "about_to_trip": "Two motion lines behind the walker, the obstacle half a step from the leading toe, and a side view with a face of its own. In full in five pictures, after failing two gates: 'he looks about to trip over it'. Four of the five readings add that the walker may miss the box, 'she could trip on it or might pass just beside it'.",
    "rain_coming": "Not worked; only the figure who points is drawn anew. It fails: in one picture of three the reader named the storm clouds and the child pointing at them and did not go on to the rain. See the next list.",
    "ice_cream": "The eaters drawn anew, with the new face. Two half marks in twenty pictures, on walkers whose cone is held up and not seen at the mouth: 'he does not seem to be eating at this moment, just holding the cone up'.",
    "blocked_hose": "Not worked; the new dog stands on the hose. Two half marks in five pictures, both for the tap: 'this could be because the dog is standing on it (pinching it) or simply because the tap is not on'.",
    "lost_balloon": "Not worked. Two half marks in five pictures: 'The red balloon might have been let go by the girl, or the girl is just looking at it.'",
    "bird_steals": "The birds drawn without a line at the neck. One half mark in six pictures, where the bird was pecking at the sandwich and the theft was not said.",
    "water_upward": "Not worked. In full in five pictures; a hose or a thin pipe is offered beside the water in two.",
    "cat_stalks_bird": "The cats drawn anew: a longer body, a broad skull, large ears and a bright iris. In full in five pictures, and no scorer listed a judgement call against it.",
    "dog_reading": "The new dog in its reading pose. In full in five pictures: 'A dog wearing glasses and reading a newspaper is impossible.'",
    "walk_dog": "The dogs drawn anew, and the walker with the face of a side view. In full in six pictures, each walker and dog going one way.",
    "dog_sleeping": "The new dog lies on its belly with its head down. In full in five pictures.",
    "dog_begs": "The new dog sits up on its haunches with its forepaws folded. In full in four pictures.",
    "dog_playing": "The new dog in a play bow. In full in four pictures.",
    "goat_grazing": "A deeper barrel, slim legs on split hooves and a wedge face. In full in four pictures: a goat in all four, and a sheep in none.",
    "cat_on_fence": "The new cat walking the fence. In full in three pictures.",
    "cat_sleeping": "The new cat asleep. In full in three pictures, a cat in each.",
}

# what the v0.48 screen readers made of the one template that fails the gate (vision/flaws_v048.md); nothing was mended or read again after the screen
WEAK_NOTES = {
    "rain_coming": "Read in two pictures of three: 'A back garden under a grey sky with three dark storm clouds, so it looks like rain is coming.' In the third the reader had the dark clouds and a child pointing up, 'perhaps at the storm clouds', and did not say that rain is coming: a zero on the inference, and no item misread. Nothing of the template was changed in this release but the figure who points, and it read in full in v0.47. First on the list for v0.49: something a person does about the rain.",
}
SCREEN_NOTE = ("The v0.48 screen read the set pictures and enough probe pictures that every template appeared in at least three "
               "screened pictures, and every angle an animal is drawn at in at least two. The new heads, faces and hair and the redrawn animals were judged on the bench first, in five rounds of pairs beside the drawing of v0.47, a bench on which way a figure goes and four rounds of cut-outs, and then in whole test scenes. "
               "939 of 971 items had full marks and none was misread. 63 of the 64 templates pass the gate and one fails it, the coming rain, where the walker about to trip failed in v0.47; nothing was mended, swapped or read again after the screen. "
               "With the 33 full marks that stand beside another reading halved, 55 of the 64 pass. "
               "Every person and every animal is drawn anew, so no picture is the same as in v0.47. "
               "AI readers describe exhaustively, so the screen filters illegible drawing but cannot rank the templates by difficulty, which is the pilot's job.")


FIXES = [("portrait:person.mei__stand__smile__y000", "The head and the face",
          "v0.47: a head wider than tall, a fringe cut straight across the brow with a square corner at each temple, and a smile drawn as an angular red shape with a dark edge. v0.48: an egg head with a jaw and a chin, the hair parted in the middle and rounding down at the temples, and the mouth one plain line. A bench reviewer, of the new one beside the old: 'The face reads clearly as a smiling woman with a simple nose and mouth, and the hair falls naturally'. The new drawing was the better in 10, 9 and 12 pairs of 16 over three benches."),
         ("portrait:person.ben__stand__smile__y000", "The second figure of the study",
          "v0.47: a moustache with curled ends over an open red mouth, to one reviewer 'very large and curled, sitting over an open red mouth; slightly comic'. v0.48: a short thin moustache over a plain mouth, ears that show, and a hairline with a temple. It cost a reading: no screen reader named a moustache in any of his 17 pictures, where 10 of 15 had in v0.47, and he is a boy in 2 of the 17."),
         ("pair:person.ben__walk__smile__y090>person.ben__walk__smile__y090", "A side view has a face of its own",
          "v0.47: the head of a side view turned 48 degrees to the viewer, a three-quarter face over a body in profile, and five readers of that screen wrote of which way a figure faces. v0.48: the head turns 22 degrees, and the near eye, its brow and the mouth are set round the cheek as in a drawn profile, with nothing of the far eye. On the bench: 'the profile head looking down at the foot fits the kick and the face is placed consistently on the head'. One remark on direction in the screen, and no misread."),
         ("pair:person.ben__stand__neutral__y045>person.ben__stand__neutral__y045", "One flat tone, and a tee to the hips",
          "v0.47: a second, darker tone laid by the turn of the surface, and a tee hemmed at the waist. Of both, on the bench: 'a faint lighter triangular mark on the far thigh, like a stray patch'; 'the shirt is very short and the trouser waist very high, so the upper body looks short against long legs'. v0.48: flat colour inside the line, the tee hemmed at the hips, the standing feet turned out."),
         ("portrait:person.rosa__stand__smile__y000", "The glasses and the bun",
          "v0.47: heavy round rims and a fringe straight across the brow. v0.48: a lighter wire with an arm to each ear, hair swept from a parting, and a larger bun, after one reviewer had 'the bun on top is very small and hard to see, so the hair could read as a cap or helmet'. The glasses are named in all 16 of her screened descriptions and the bun in 8."),
         ("portrait:person.dev__stand__smile__y000", "The beard",
          "v0.47: a dark block of beard across the chin under an angular red mouth. v0.48: a small dark beard on the chin under a short thin moustache, the fourth drawing on the study sheets; one before it, a soft tone with no line, 'reads more like a shadow or dirt than a beard'. No screen reader named the beard in any of his 24 pictures."),
         ("pair:person.kai__stand__smile__y000>person.kai__stand__smile__y000", "A child",
          "v0.47: a round, wide head. v0.48: the egg head on a fuller neck. The first trial of the new head lost its pair here, the neck 'long and thin like a stalk, so the head looks perched on a stick', and the neck was made fuller and the chin lower before the next bench."),
         ("pair:animal.dog_01__sit__happy__y090>animal.dog_01__sit__happy__y090", "The sitting dog",
          "v0.47: to a reviewer 'a ramp-shaped body with no hind quarters and an over-long neck'. v0.48: a haunch, a folded hind leg and a tail of its own: 'it reads clearly as a sitting dog with a proper haunch, hind leg and separate tail'."),
         ("pair:animal.dog_01__stand__neutral__y090>animal.dog_01__stand__neutral__y090", "The legs of the dogs",
          "v0.47: legs set under the body with no shoulder or thigh of their own. v0.48: a shoulder, an elbow, a wrist and a paw, and a hip, a stifle, a hock and a paw, each on a bone of its own. The first new legs lost this pair, 'very long and thin for the body, giving a stilt-like, spidery look', and were shortened and thickened: 'Its legs and hip join cleanly and the body reads as solid and balanced'."),
         ("pair:animal.cat_01__sit__happy__y090>animal.cat_01__sit__happy__y090", "The cats",
          "v0.47: to a reviewer 'a detached ball head, no hind quarters and a tail fused into a ramp-shaped body'. v0.48: 'it reads as a proper sitting cat with a haunch, folded hind leg, neck and separate tail', with a bright iris and a slit pupil that stay open in every face but the sleeping one. A cat is a cat in all 11 screened descriptions of a picture with one."),
         ("pair:animal.goat_01__graze__neutral__y090>animal.goat_01__graze__neutral__y090", "The goat",
          "v0.47: a straight sloping back on thin legs of one width. v0.48: a deeper barrel, slim legs on split hooves and a wedge face. A goat in all four of its screened pictures and a sheep in none, where two readers of v0.47 had offered a sheep."),
         ("pair:animal.dog_01__beg__happy__y090>animal.dog_01__beg__happy__y090", "The begging dog",
          "v0.47: upright on a narrow base. v0.48: sitting up on its haunches with the forepaws folded at the chest. A bench reader of a cut-out: 'sits up on its hind legs on the grass next to the bench, looking up toward her, as if begging for the ice cream'. In full in four screened pictures.")]



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
                name = f"fix_{tag}_{os.path.basename(path)[:-4]}_{bx[0]}_{bx[1]}.webp"     # (two crops of one picture stay two files)
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
