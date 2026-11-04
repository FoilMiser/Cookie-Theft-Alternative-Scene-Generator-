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
    "about_to_trip": "Someone reads while walking straight toward a bucket, ball or box. Prediction, 1 step.",
    "dog_begs": "Someone eats on a bench; a dog sits beside it looking up at the food. Intention, 1 step (gaze checked).",
    "sprinkler_package": "A sprinkler sprays toward a package left on the grass. Prediction, 1 step.",
    "paint_tracks": "Fresh paint on the fence, a paint tray, and paw prints leading to the dog. Cause, 2 steps.",
    "windy_hat": "A hat blows off; its owner reaches after it. Cause, 2 steps.",
    "bird_steals": "A bird pecks at a sandwich on the bench while the reader isn't looking. Viewpoint, 2 steps.",
    "lost_balloon": "A balloon floats away high in the sky; a child below reaches up, upset. Cause, 1 step.",
    "ducks_bread": "Someone throws bread toward the pond; a duck swims over. Intention, 1 step.",
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
PREV, CUR = "v027", "v028"

# the templates whose drawing or placement v0.28 changed for the v0.27 screen (vision/flaws_v027.md); each drawing went to the isolation bench first
# (vision/isolation_v028.md) and was read in whole test scenes (vision/design_tests_v028.md)
REDRAWN_NOTES = {
    "dog_begs": "'Could be hers, begging from her bag'. Now at the end of the bench the eater sits nearest, its gaze on the food, and nobody else near: 'begging for the ice cream', in full in its three pictures. Not redrawn.",
    "ice_cream_drop": "'A pink hat or a pink frisbee', 'flying saucer'. Now a flat splat, the dog's mouth over it: 'a pink splat with coloured sprinkles'.",
    "ball_in_tree": "'A blue planet-like sphere', on 'a small bare branch drawn on top of the crown'. Now a beach ball on a limb from a fork at the top of the trunk: a beach ball in all four of its pictures.",
    "seesaw": "'Almost past it', and a shadow under one rider only. The riders further in, and one shadow under the whole seesaw.",
}

# what the v0.28 screen readers made of the templates that read poorly (vision/flaws_v028.md)
WEAK_NOTES = {
    "dog_sleeping": "'Sniffing the grass, lying down, or curled up asleep'; 'could be a puppy or a kitten'. In full in v0.27 on the same drawing and a wide oval of shadow, so the smaller shadow may be why. For v0.29: the bench.",
    "ducks_bread": "'Swimming towards those crumbs'. v0.27's readers wrote much the same and scored in full, so mostly the scorers. For v0.29: the duck's bill at a crumb.",
    "dog_wants_walk": "One reader: 'sits with a red lead in its mouth', no more, in a picture v0.27 read in full. Not changed. Watch.",
}
SCREEN_NOTE = ("The v0.28 screen read the set pictures and enough probe pictures that every template appeared in at least three "
               "screened pictures. The shadows, the fallen ice cream, the seesaw, the ball and its branch, the faces and the beard went to the isolation bench first, "
               "and every change but the goatee was read in whole test scenes. 766 of 775 items had full marks, none was misread, and one was missed. "
               "61 of 64 templates pass the gate, against 63: the begging dog, v0.27's one failure, passes in full, and of the three that now fail, two were not touched and one, the sleeping dog, has the same drawing on a smaller shadow. A retest of the unchanged v0.9 pictures with fresh readers moved the gate by five templates, "
               "so this is not a measure of the drawings getting worse. Readers' remarks went down 12%, though readers differ widely: remarks on shadows and on marks on a face fell, and those on thin figures rose with nothing changed. AI readers describe "
               "exhaustively, so the screen filters illegible drawing but cannot rank the templates by difficulty, which is the pilot's job.")


FIXES = [("crop:scenes_v027/T1_street_s1031.png@1000,640,1270,1000>scenes/T1_street_s1031.png@1000,640,1270,1000", "The shadow", "v0.27: 'a large oval on the grass, a bit wide and offset from her feet'. v0.28: from the figure's own feet. Pictures remarking on shadows fell from 20 to 11, none of them calling one wide. Here on the same seed."),
         ("crop:scenes_v027/T4_playground_s1605000.png@630,780,850,930>scenes/T3_playground_s19143.png@1030,880,1250,1000", "The fallen ice cream", "v0.27: 'a pink hat or a pink frisbee', a flying saucer. v0.28: a flat splat with flecks thrown clear of it: 'a pink splat with coloured sprinkles'."),
         ("crop:scenes_v027/T4_playground_s1605000.png@80,320,300,500>scenes/T4_playground_s621959.png@0,320,220,500", "The ball in the tree", "v0.27: 'a blue planet-like sphere' on 'a small bare branch drawn on top of the crown'. v0.28: a beach ball, on a limb from a fork at the top of the trunk."),
         ("person.dev__stand__smile__y000", "The beard", "v0.27: 'a thin dark strap along the jaw'. Fuller on the cheek it was 'a mask or scarf'. v0.28: a goatee and moustache: 'a small beard'. No strap or mask in 70 pictures.")]


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
        scr["weak"] = [{"id": t, "mean": b6[t]["mean"], "items": b6[t]["items"], "note": WEAK_NOTES.get(t, "")}
                       for t in sorted(b6, key=lambda t: b6[t]["mean"]) if b6[t]["mean"] < 0.9]
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
    open(os.path.join(out, "index.html"), "w").write(html)
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
