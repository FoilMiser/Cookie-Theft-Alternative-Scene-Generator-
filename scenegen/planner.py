"""Plan, place, measure and score one scene at a target tier.

plan()      choose the setting features, sky, templates and cast; list the variants to render
realize()   place every template from the rendered manifests (fails if something will not fit)
finalize()  add fillers to the clutter band, measure masks, pick the scored setting entities that
            bring predicted completeness to the band centre, score every item, check every rule
"""
import itertools
import math
import random
from collections import Counter

from . import compose as K
from . import difficulty as DF
from . import draw as D
from . import templates as TP
from . import scene as SCN
from .scene import PlacementError, Scene
from .settings import FEATURES, build as build_setting

GENERATOR_VERSION = "0.20.0"

# how many template instances (scene load) and inference units each tier uses
TIER_PLAN = {
    1: {"units": (0, 0), "contra": (0, 0), "events": (2, 3), "load_max": 3},
    2: {"units": (1, 1), "contra": (0, 0), "events": (2, 3), "load_max": 4},
    3: {"units": (2, 3), "contra": (0, 1), "events": (2, 3), "load_max": 6},
    4: {"units": (4, 5), "contra": (1, 2), "events": (3, 4), "load_max": 9},
}
ORDER_LAST = ("photo",)
ORDER_FIRST = ("seesaw_heavy", "seesaw", "slide", "sandbox", "dog_wants_walk", "swing", "hang_laundry", "blocked_hose", "hose_water", "dog_begs", "bird_steals", "read_bench", "drink_bench",
               "water_flowers", "water_upward", "pan_watering", "plant_flowers", "ball_in_tree", "kite_in_tree", "fish_in_tree",
               "paint_tracks", "paint_fence", "fishing", "ducks_bread", "ducks_swimming", "picnic", "cat_stalks_bird")


def feasible(cls, setting, sky):
    if not cls.feasible(setting, sky):
        return False
    need = cls.features(setting)
    return need <= FEATURES[setting]["optional"] | FEATURES[setting]["default"]


# Prior guesses of each inference item's features (typical cue salience z, cue-effect separation,
# cues - 1, key word), used only to choose templates whose inference difficulty suits the tier
# before anything is rendered; every scene is then scored from its real masks.
PRIOR = {   # (type, chain, salience z, separation, cues - 1, key word); measured by calibrate (v0.20 calibration.json)
    "blocked_hose": [("inference", 2, -0.40, 0.155, 2, "water")],
    "rain_coming": [("inference", 1, 0.95, 0.405, 1, "rain")],
    "cat_stalks_bird": [("inference", 1, -0.49, 0.080, 1, "cat")],
    "ball_in_tree": [("inference", 1, -0.75, 0.141, 1, "stuck")],
    "kite_in_tree": [("inference", 1, -0.54, 0.245, 2, "stuck")],
    "ice_cream_drop": [("inference", 1, -1.16, 0.075, 2, "dropped")],
    "about_to_trip": [("inference", 1, 0.19, 0.091, 1, "trip")],
    "dog_begs": [("inference", 1, -0.70, 0.095, 1, "begging")],
    "sprinkler_package": [("inference", 1, -0.27, 0.167, 1, "wet")],
    "paint_tracks": [("inference", 2, -0.71, 0.142, 2, "paint")],
    "windy_hat": [("inference", 2, -1.23, 0.140, 1, "wind")],
    "bird_steals": [("inference", 2, -1.40, 0.051, 1, "stealing")],
    "lost_balloon": [("inference", 1, -1.05, 0.130, 2, "lost")],
    "ducks_bread": [("inference", 1, -1.41, 0.011, 1, "hungry")],
    "seesaw_heavy": [("inference", 1, -0.76, 0.188, 1, "heavy")],
    "dog_wants_walk": [("inference", 1, -0.75, 0.157, 2, "walk")],
}
for _cid, _s, _k in [("water_upward", -1.38, "water"),
                     ("floating_box", -0.38, "floating"),
                     ("square_wheel", -0.03, "wheel"),
                     ("fish_in_tree", -1.31, "fish"),
                     ("pan_watering", -0.10, "pan"),
                     ("sweep_fork", 0.27, "fork"),
                     ("bucket_hat", 0.28, "bucket"),
                     ("sitting_on_air", 0.07, "chair"),
                     ("ladder_nothing", -0.22, "ladder"),
                     ("dog_reading", -0.46, "newspaper")]:
    PRIOR[_cid] = [("contradiction_notice", 0, _s, 0.0, 0, _k), ("contradiction_explain", 1, _s, 0.0, 0, _k)]
TYPICAL_LOAD = {1: 2.5, 2: 4, 3: 5.5, 4: 8}

# how often each template has been used in this run (a batch spreads its pictures over the templates
# instead of repeating the same favourites)
USAGE = Counter()


def usage(cs):
    return sum(USAGE[c.id] for c in cs)


def prior_ps(tids, tier, load=None):
    L = load if load is not None else TYPICAL_LOAD[tier]
    out = []
    for tid in tids:
        dom = TP.ALL_TEMPLATES[tid].domain
        for ty, h, sal, d, r, key in PRIOR.get(tid, []):
            lex = ty in DF.CONTENT_TYPES
            ft = {"type": ty, "chain": h, "animate": False, "s": sal, "r": r, "d": d, "f": DF.zipf(key) - 4 if lex else 0.0,
                  "a": DF.aoa(key) if lex else DF.AOA_CENTER, "domain": dom}
            out.append(DF.logistic(-DF.item_b(ft, L)))
    return out


def choose(tier, setting, rng, forced=None):
    """Pick templates for a tier. forced: optional dict with 'modules', 'contradictions', 'events' id lists."""
    TPn = TIER_PLAN[tier]
    units = rng.randint(*TPn["units"])
    n_contra = min(units, rng.randint(*TPn["contra"]))
    n_mod = units - n_contra
    sky = "clear"
    picked = []
    used_res = set()

    def ok(c):
        if any(r in used_res for r in c.exclusive):
            return False
        if c.sky and c.sky != sky:
            return False
        return feasible(c, setting, sky) and c not in picked

    def take(c):
        picked.append(c)
        used_res.update(c.exclusive)

    if forced:
        if "rain_coming" in forced.get("modules", []):
            sky = "dark"
        for kind in ("modules", "contradictions", "events"):
            for tid in forced.get(kind, []):
                c = TP.ALL_TEMPLATES[tid]
                if not feasible(c, setting, sky):
                    raise PlacementError(f"{tid} not feasible in {setting}")
                take(c)
        return picked, sky
    # choose the inference templates so their prior inference completeness suits the tier's band
    mods_all = [c for c in TP.MODULES if feasible(c, setting, "dark" if c.sky == "dark" else "clear")]
    cons_all = [c for c in TP.CONTRADICTIONS if feasible(c, setting, "clear")]
    target = DF.CENTER[tier][1]
    tol = {2: 0.035, 3: 0.04, 4: 0.04}.get(tier, 0.04)
    best, good = None, []
    for _ in range(400 if units else 1):
        ms = rng.sample(mods_all, min(n_mod, len(mods_all)))
        cs = rng.sample(cons_all, min(n_contra, len(cons_all)))
        res = [r for c in ms + cs for r in c.exclusive]
        if len(res) != len(set(res)):
            continue
        if not units:
            best = (0, ms, cs)
            break
        ps = prior_ps([c.id for c in ms + cs], tier)
        cost = abs(sum(ps) / len(ps) - target) if ps else 1
        if best is None or cost < best[0]:
            best = (cost, ms, cs)
        if cost <= tol:
            good.append((cost, ms, cs))
    if good:
        # any set whose prior lands near the band will do: pick among the least-used sets, at random
        least = min(usage(g[1] + g[2]) for g in good)
        best = rng.choice([g for g in good if usage(g[1] + g[2]) <= least])
    if best:
        ms, cs = best[1], best[2]
        if SCN.PLACEMENT_REV >= 16 and any(c.sky == "dark" for c in ms + cs):
            # revision 16: a template that needs a clear sky is dropped from a set whose storm clouds another brings (the
            # modules are sampled each under its own sky: a sprinkler soaking a box ran under the storm clouds of a
            # rain warning)
            ms, cs = [c for c in ms if c.sky != "clear"], [c for c in cs if c.sky != "clear"]
        for c in ms:
            if c.sky == "dark":
                sky = "dark"
        for c in ms + cs:
            take(c)
    n_ev = rng.randint(*TPn["events"])
    evs = [c for c in TP.EVENTS if feasible(c, setting, sky)]
    rng.shuffle(evs)
    evs.sort(key=lambda c: USAGE[c.id])
    # animals and people in a healthy mix: at most two animal events
    n_animal = 0
    for c in evs:
        if sum(1 for p in picked if p.kind == "event") >= n_ev:
            break
        animal = issubclass(c, (TP.AnimalEvent,)) or c in (TP.BirdPerched, TP.DucksSwimming, TP.BirdsFlying, TP.CatOnFence)
        if animal and n_animal >= 2:
            continue
        if ok(c):
            take(c)
            n_animal += animal
    return picked, sky


ANIMAL_EVENTS = None


def is_animal_event(c):
    return issubclass(c, TP.AnimalEvent) or c in (TP.BirdPerched, TP.DucksSwimming, TP.BirdsFlying, TP.CatOnFence)


def balance_content(tier, setting, sky, picked, feats, rng):
    """Add events or entity-bearing features until the content band is reachable; drop events if over."""
    lo, hi = DF.TIERS[tier]["content"]
    load_max = TIER_PLAN[tier]["load_max"]
    for _ in range(12):
        inst = build_setting(setting, feats, sky)
        consumed = {u for c in picked for u in c.uses}
        ents = [e for e in inst.entities if e not in consumed]
        est = sum(c.content for c in picked)
        if est > hi - 1 and any(c.kind == "event" for c in picked):
            ev = [c for c in picked if c.kind == "event"]
            picked.remove(ev[-1])
            continue
        if est + max(0, len(ents) - 2) >= lo:
            break
        used = {r for c in picked for r in c.exclusive}
        n_animal = sum(1 for c in picked if c.kind == "event" and is_animal_event(c))
        if len(picked) < load_max:
            evs = [c for c in TP.EVENTS if feasible(c, setting, sky) and c not in picked and not any(r in used for r in c.exclusive)
                   and not (is_animal_event(c) and n_animal >= 2)]
            evs.sort(key=lambda c: -c.content + rng.random() * 0.5 + 0.4 * USAGE[c.id])
            if evs:
                picked.append(evs[0])
                feats |= evs[0].features(setting)
                continue
        opt = sorted(FEATURES[setting]["optional"] - feats)
        if opt:
            feats.add(rng.choice(opt))
            continue
        break
    return picked, feats


def plan(tier, setting, seed, lib, forced=None):
    bumped = Counter()
    try:
        return _plan(tier, setting, seed, lib, forced, bumped)
    finally:
        USAGE.subtract(bumped)            # the temporary penalties never outlive the plan
        for k in [k for k, v in USAGE.items() if v == 0]:
            del USAGE[k]


def _plan(tier, setting, seed, lib, forced, bumped):
    rng = random.Random(seed * 7919 + tier * 104729 + sum(map(ord, setting)))
    for attempt in range(30):
        picked, sky = choose(tier, setting, rng, forced)
        sc = Scene(tier, setting, seed, lib, sky)
        sc.rng = random.Random(rng.random())
        feats = set()
        for c in picked:
            feats |= c.features(setting)
        # a few optional features for variety (entity candidates and clutter)
        extra = sorted(FEATURES[setting]["optional"] - feats)
        if SCN.PLACEMENT_REV >= 5:
            # an empty picnic blanket with nobody on it read as someone gone missing: only with a picnic
            extra = [f for f in extra if f != "blanket"]
        rng.shuffle(extra)
        feats |= set(extra[: rng.randint(0, 2 if tier <= 2 else 3)])
        if not forced:
            picked, feats = balance_content(tier, setting, sky, picked, feats, rng)
        if SCN.PLACEMENT_REV >= 15 and "blanket" in feats and not any(c.id == "picnic" for c in picked):
            # revision 15: the content balance no longer adds an empty picnic blanket either (one lay under a
            # sprinkler's spray with nobody on it)
            feats.discard("blanket")
        if SCN.PLACEMENT_REV >= 17 and any(c.id == "pan_watering" for c in picked):
            # revision 17: no hose reel as scenery beside the frying pan either (it read as "a hose nozzle")
            feats.discard("hose_reel")
        if SCN.PLACEMENT_REV >= 17 and setting == "playground" and {"seesaw", "bench"} <= feats:
            # revision 17: never the playground's seesaw and its bench together: the seesaw stands right in front of the
            # bench, its raised end across a sitter's legs, so with the gap kept from thin parts no one could sit there
            need = set()
            for c in picked:
                need |= c.features(setting)
            if {"seesaw", "bench"} <= need:
                continue
            feats.discard("bench" if "seesaw" in need else "seesaw")
        if SCN.PLACEMENT_REV >= 18 and setting == "garden" and "bench" in feats and any(c.id == "dog_wants_walk" for c in picked):
            # revision 18: never the garden's bench with the dog waiting at the door: the bench stands right in front of the
            # door, so the dog's feet were always "just behind" it (revision 15) and the dog could not be placed; in the
            # tier-4 garden that one clash failed most attempts
            need = set()
            for c in picked:
                if c.id != "dog_wants_walk":
                    need |= c.features(setting)
            if "bench" in need:
                continue
            feats.discard("bench")
        if SCN.PLACEMENT_REV >= 14 and any(c.id == "square_wheel" for c in picked):
            # revision 14: no ordinary bicycle in a rack beside the square-wheeled one (as the fillers keep away since revision 9)
            feats.discard("bicycle")
        if "laundry" in feats:
            feats.add("clothesline")
        if "clothesline" in feats:
            feats.add("laundry")          # an empty line reads as a bare wire
        sc.features = feats
        sc.picked_ids = {c.id for c in picked}
        insts = []
        try:
            for c in picked:
                t = c(sc)
                t.ev = f"e{len(insts) + 1}"
                sc.binding = c.id
                t.bind()
                insts.append(t)
            sc.binding = None
        except PlacementError:
            if forced:
                raise
            # revision 4: the events that could not all be cast together (too few children for a
            # seesaw, a sandbox and a slide, say) count as used for the rest of this plan, so the next
            # attempt reaches for others instead of picking the same set thirty times
            if SCN.PLACEMENT_REV >= 4:
                for c in picked:
                    if c.kind == "event":
                        USAGE[c.id] += 1
                        bumped[c.id] += 1
            continue
        sc.templates = insts
        sc.mirror_scene = rng.random() < 0.5
        return sc
    raise PlacementError("could not cast a scene")


def realize(sc):
    from . import settings as _ST
    _ST.DARK_SCALE["value"] = {-1: 1.2, 0: 1.0, 1: 0.68}[max(-1, min(1, sc.knob))] if sc.sky == "dark" else 1.0
    sc.S = build_setting(sc.setting_id, sc.features, sc.sky)
    def rank(t):
        if t.id in ORDER_FIRST:
            return ORDER_FIRST.index(t.id)
        # revision 5: the photographer goes last, so there is something already there to photograph;
        # revision 6: the person pointing at the storm clouds just before, so the pointing line can be
        # kept clear of everything else
        if SCN.PLACEMENT_REV >= 6 and t.id == "rain_coming":
            return 199
        # revision 13: the waver after everyone else, so there is someone simply going about their day to wave at
        if SCN.PLACEMENT_REV >= 13 and t.id == "wave":
            return 198
        if SCN.PLACEMENT_REV >= 5 and t.id in ORDER_LAST:
            return 200
        return 99
    order = sorted(sc.templates, key=rank)
    for t in order:
        # structures this template puts people on or at (the bench it sits them on, the swing, ...)
        ex = t.features(sc.setting_id) | set(t.uses) | set(t.exclusive) | set(getattr(t, "exempt_extra", ()))
        ex |= {"swing_seat"} if "swing" in ex else set()
        ex |= {"laundry", "clothesline"} if ex & {"laundry", "clothesline"} else set()
        sc.exempt = ex
        sc.placing = t       # revision 14: whose lanes and pointing lines are whose
        before = set(sc.assets) | set(sc.svgs)
        if not t.place():
            sc.exempt = ()
            sc.placing = None
            return False, f"could not place {t.id}"
        sc.exempt = ()
        sc.placing = None
        # every element an event draws belongs to it (the legibility rules leave an event's own
        # strings, seeds and water alone)
        for k in (set(sc.assets) | set(sc.svgs)) - before:
            sc.ev_of[k] = t.ev
        sc.events.append(t.ev)
        for u in t.uses:
            sc.consumed.add(u)
    return True, "ok"


def add_fillers(sc, target):
    n = count_objects(sc)
    slots = list(sc.S.filler_slots)
    sc.rng.shuffle(slots)
    tids = {t.id for t in sc.templates}
    for f in slots:
        if n >= target:
            break
        # never a second wheelbarrow or bicycle beside the square-wheeled one
        if "square_wheel" in tids and f["id"] in ("wheelbarrow", "bike_rack"):
            continue
        if f.get("needs") and not f["needs"](sc):
            continue
        svg, bb = f["fn"](f["x"], f["y"])
        # revision 15: never cut off by the picture's edge (a rubbish bin "cut off by the bottom-left picture edge"): a
        # filler slot at the edge is moved in until the whole thing shows (dropped, the edge slots left tier-4 pictures
        # short of their drawn objects)
        # (revision 16: and well inside it: a bin 6 px from the edge still read as "partly cut off by the edge")
        em = 24 if SCN.PLACEMENT_REV >= 16 else 2
        ei = 30 if SCN.PLACEMENT_REV >= 16 else 6
        if SCN.PLACEMENT_REV >= 15 and (bb[0] < em or bb[2] > D.W - em or bb[3] > D.H - 2):
            dx = (ei - bb[0]) if bb[0] < em else ((D.W - ei) - bb[2] if bb[2] > D.W - em else 0)
            dy = ((D.H - 6) - bb[3]) if bb[3] > D.H - 2 else 0
            svg, bb = f["fn"](f["x"] + dx, f["y"] + dy)
            if bb[0] < em or bb[2] > D.W - em or bb[3] > D.H - 2:
                continue
        if f.get("blocked") and any(f["blocked"][0] <= p.X <= f["blocked"][2] and f["blocked"][1] - 10 <= p.Y <= f["blocked"][3] + 10 for p in sc.assets.values()):
            continue
        if not sc.fits(bb, limit=0.04, margin=-200):
            continue
        # revision 4: a filler keeps a gap from every scored thing (a dog bowl at the edge of a dug hole
        # read as about to fall in) and from every other filler
        if SCN.PLACEMENT_REV >= 4:
            g = (bb[0] - 14, bb[1] - 10, bb[2] + 14, bb[3] + 10)
            if not sc.fits(g, limit=0.0, margin=-200):
                continue
            if any(sc.overlap(g, e["bbox"]) > 0 for e in sc.svgs.values() if e["role"] == "filler" and e.get("bbox")):
                continue
            # nor against a standing structure (pots between the swing's legs seemed to hang from it)
            if not sc.air_clear(bb, 4):
                continue
        # revision 9: nor on what an event drew around itself (a watering can stood on the swept heap's
        # dustpan), nor in the air and ground an event keeps clear
        if SCN.PLACEMENT_REV >= 9:
            if any(sc.overlap(g, e["bbox"]) > 0 for k_, e in sc.svgs.items() if e["role"] == "setting" and e.get("bbox") and not k_.startswith("filler")):
                continue
            if any(min(g[2], z[2]) > max(g[0], z[0]) and min(g[3], z[3]) > max(g[1], z[1]) for z in list(sc.airzones) + list(sc.keepout) + list(getattr(sc, "groundzones", []))):
                continue
        sc.svg(f"filler_{f['id']}", f["label"], svg, f["y"], bb, "filler")
        n += 1
    return n


def count_objects(sc):
    n = sum(1 for e in sc.S.elements if e["role"] != "background")
    n += sum(1 for e in sc.svgs.values() if e["role"] in ("scored", "filler", "setting"))
    n += len(sc.assets)
    return n


def item_features(sc, it, stats):
    W2 = D.W * D.H
    els = [e for e in it["elements"] if e in stats]
    if it["type"] in DF.INFERENCE_TYPES and it["cues"]:
        prim = [it["cues"][0]] if it["cues"][0] in stats else els
    else:
        prim = els
    area = sum(stats[e]["visible"] for e in prim)
    s = DF.salience_z(area, W2)
    r = max(0, len(it["cues"]) - 1) if it["cues"] else 0
    # separation: how far the reader's eye must travel to link the evidence = the largest distance
    # from the primary cue to any other cue or effect element of the item
    d = 0.0
    if it["type"] == "inference" and it["cues"]:
        c = it["cues"][0]
        if c in stats and stats[c]["centroid"]:
            x0, y0 = stats[c]["centroid"]
            for e in set(it["cues"][1:]) | set(it["effect"]):
                if e != c and e in stats and stats[e]["centroid"]:
                    x1, y1 = stats[e]["centroid"]
                    d = max(d, math.hypot(x1 - x0, y1 - y0) / math.hypot(D.W, D.H))
    # the key word's frequency and age of acquisition: recorded raw on every item, used only for entities and actions
    # (v0.20: inference and contradiction items are scored on meaning, with many phrasings, so f = 0 and a is centred)
    z_raw = DF.zipf(it["key"])
    a_raw = DF.aoa(it["key"])
    lex = it["type"] in DF.CONTENT_TYPES
    f = z_raw - 4.0 if lex else 0.0
    a = a_raw if lex else DF.AOA_CENTER
    return {"type": it["type"], "chain": it["chain"], "animate": it["animate"], "s": round(s, 3), "r": r, "d": round(d, 3),
            "f": round(f, 2), "a": round(a, 2), "zipf_raw": round(z_raw, 2), "aoa_raw": round(a_raw, 2), "domain": it.get("domain"),
            "area_px": round(area)}


def score(sc, items, stats):
    L = len(sc.events)
    for it in items:
        ft = item_features(sc, it, stats)
        it["features"] = ft
        it["b"] = round(DF.item_b(ft, L), 3)
        it["p0"] = round(DF.logistic(0 - it["b"]), 3)
        it["pm1"] = round(DF.logistic(-1 - it["b"]), 3)
    return DF.completeness(items, 0.0), DF.completeness(items, -1.0)


def entity_items(sc, stats):
    """Candidate setting entities: visible, not occluded, not used as a template's object."""
    out = []
    used = {e for it in sc.items for e in it["elements"]}
    for eid, ent in sc.S.entities.items():
        if eid in sc.consumed or eid in used or eid not in stats:
            continue
        st = stats[eid]
        if st["occlusion"] > 0.20 or st["visible"] < (0.03 * D.W) ** 2 * 0.5:
            continue
        out.append({"id": None, "type": "entity", "text": ent["text"], "accepted": ent["accepted"], "key": ent["key"],
                    "elements": [eid], "animate": False, "chain": 0, "cues": [], "effect": [], "domain": None,
                    "template": "setting", "event": None})
    return out


def quick_stats(sc):
    """Cheap stand-in for the mask measurement: areas from asset masks and element boxes, no occlusion."""
    st = {}
    for eid, p in sc.assets.items():
        b = p.bbox()
        st[eid] = {"visible": p.area_px(), "area": p.area_px(), "occlusion": 0.0, "centroid": ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2), "bbox": b}
    for e in list(sc.svgs.values()) + sc.S.elements:
        b = e.get("bbox")
        if not b or e["role"] == "background":
            continue
        a = max(1.0, (b[2] - b[0]) * (b[3] - b[1]) * 0.55)
        st[e["id"]] = {"visible": a, "area": a, "occlusion": 0.0, "centroid": ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2), "bbox": b}
    return st


def quick_estimate(sc):
    """Approximate (content, inference) completeness at theta = 0 with the best entity choice."""
    stats = quick_stats(sc)
    T = DF.TIERS[sc.tier]
    items = [dict(it) for it in sc.items]
    score(sc, items, stats)
    cands = entity_items(sc, stats)
    for c in cands:
        score(sc, [c], stats)
    base = [it["p0"] for it in items if it["type"] in DF.CONTENT_TYPES]
    n_tpl = len(base)
    lo_c, hi_c = T["content"]
    center = DF.CENTER[sc.tier][0]
    best = None
    ps_c = sorted(c["p0"] for c in cands)
    for k in range(max(0, lo_c - n_tpl), min(len(cands), hi_c - n_tpl) + 1):
        for combo in itertools.combinations(ps_c, k):
            ps = base + list(combo)
            pc = sum(ps) / len(ps)
            if best is None or abs(pc - center) < abs(best - center):
                best = pc
    inf = [it["p0"] for it in items if it["type"] in DF.INFERENCE_TYPES]
    return best, (sum(inf) / len(inf) if inf else None)


def near_band(tier, pc, pi, slack=0.035):
    T = DF.TIERS[tier]
    if pc is None or not (T["pc"][0] - slack <= pc <= T["pc"][1] + slack):
        return False
    if T["pi"] is None:
        return pi is None
    return pi is not None and T["pi"][0] - slack <= pi <= T["pi"][1] + slack


def finalize(sc, objects_target=None, entity_k=None, pc_target=None):
    T = DF.TIERS[sc.tier]
    lo, hi = T["objects"]
    target = objects_target or sc.rng.randint(lo, hi)
    add_fillers(sc, target)
    els = K.elements_of(sc)
    n_obj = sum(1 for e in els if e["role"] != "background")
    stats = K.measure(sc, els, sc.mirror_scene)
    checks = dict(sc.checks)
    # rules: occlusion <= 20% and size >= 3% of canvas width for every scored element
    bad = []
    for it in sc.items:
        for e in set(it["elements"]):
            st = stats.get(e)
            if st is None:
                bad.append(f"{e} not drawn")
                continue
            if st["occlusion"] > 0.20:
                bad.append(f"{e} occluded {st['occlusion']:.0%}")
        boxes = [stats[e]["bbox"] for e in set(it["elements"]) | set(it["cues"]) if e in stats and stats[e]["bbox"]]
        if boxes:
            x0, y0 = min(b[0] for b in boxes), min(b[1] for b in boxes)
            x1, y1 = max(b[2] for b in boxes), max(b[3] for b in boxes)
            if max(x1 - x0, y1 - y0) < 0.03 * D.W:
                bad.append(f"{it['text']} too small")
    checks["occlusion_and_size"] = (not bad, "; ".join(bad) if bad else "all scored elements visible >= 80% and >= 3% of width")
    ok_l, why_l = K.legibility(sc, els, stats)
    checks["legibility"] = (ok_l, "; ".join(why_l[:6]) if why_l else "no head covered or backed by another element; no string or pole crosses a person")
    checks["clutter_band"] = (lo <= n_obj <= hi, f"{n_obj} drawn objects (tier band {lo}-{hi})")
    # choose scored setting entities to land content completeness at the band centre
    cands = entity_items(sc, stats)
    n_tpl = sum(1 for it in sc.items if it["type"] in DF.CONTENT_TYPES)
    lo_c, hi_c = T["content"]
    best = None
    center = DF.CENTER[sc.tier][0] if pc_target is None else pc_target
    tmp_items = [dict(it) for it in sc.items]
    score(sc, tmp_items, stats)
    for c in cands:
        score(sc, [c], stats)
    base_p = [it["p0"] for it in tmp_items if it["type"] in DF.CONTENT_TYPES]
    k_range = range(max(0, lo_c - n_tpl), min(len(cands), hi_c - n_tpl) + 1) if entity_k is None else [entity_k] if entity_k <= len(cands) else []
    for k in k_range:
        for combo in itertools.combinations(range(len(cands)), k):
            ps = base_p + [cands[i]["p0"] for i in combo]
            if not ps:
                continue
            pc = sum(ps) / len(ps)
            # prefer the band centre; tie-break toward fewer entities so templates carry the scene
            cost = abs(pc - center) + 0.002 * k
            if best is None or cost < best[0]:
                best = (cost, combo)
    chosen = [cands[i] for i in best[1]] if best else list(cands)
    for c in chosen:
        c.pop("b", None), c.pop("p0", None), c.pop("pm1", None), c.pop("features", None)
        sc.items.append(c)
    # final ids, scoring
    for i, it in enumerate(sc.items):
        it["id"] = f"i{i + 1:02d}"
    (pc0, pi0), (pcm, pim) = score(sc, sc.items, stats)
    n_content = sum(1 for it in sc.items if it["type"] in DF.CONTENT_TYPES)
    n_units = sum(t.units for t in sc.templates)
    n_contra = sum(1 for t in sc.templates if t.kind == "contradiction")
    bands = DF.in_band(sc.tier, pc0, pi0, n_content, n_units, n_contra)
    for it in sc.items:
        m = None
        for e in it["elements"]:
            if e in stats:
                m = stats[e]["mask"] if m is None else (m | stats[e]["mask"])
        it["aoi_cells"] = K.aoi_cells(m) if m is not None else []
    return {"stats": stats, "els": els, "checks": checks, "bands": bands, "pc": (pc0, pcm), "pi": (pi0, pim),
            "n_content": n_content, "n_units": n_units, "n_contra": n_contra}


def signature(items):
    """Radical signature for the isomorph rule: item types with chain lengths."""
    return sorted((it["type"], it["chain"]) for it in items)
