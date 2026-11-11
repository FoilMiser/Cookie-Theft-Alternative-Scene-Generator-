"""
TPDB stand-in cast builder, v0.4 (Blender 5.2, bpy).

    python build_cast.py <out_dir> [family ...]

Builds every family (10 people, 5 quadrupeds, 3 birds) as <family>.blend plus a render
config <family>.json, and writes cast_catalog.json: labels, actions (with their props,
descriptions and tags), poses and expressions per family.

Modules (castlib/):
  core.py     materials, rig, skin bodies, primitives, frames
  face.py     face kit v2 and the 19 people expressions
  people.py   skeleton, body builds, wardrobe, hair, hats, facial hair, anchors
  actions.py  lower-body postures x upper-body activities, props built prop-first
  animals.py  parameterized quadruped (dog, cat, goat) and birds (songbird, duck)
  specs.py    the cast
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
import blender_run  # noqa: E402

blender_run.ensure(__file__)

import bpy  # noqa: E402

from castlib.core import reset_scene  # noqa: E402
from castlib.face import PEOPLE_EXPRESSIONS  # noqa: E402
from castlib.people import build_person  # noqa: E402
from castlib.actions import make_people_actions  # noqa: E402
from castlib.animals import build_bird, build_quadruped  # noqa: E402
from castlib.specs import BIRDS, PEOPLE, PERSON_AFFORDANCES, QUAD_AFFORDANCES, QUADRUPEDS  # noqa: E402

BUILDER_VERSION = "0.48.0"
# the postures with both thighs swung forward of the trunk, in which a skirt is drawn as a wrap of the thighs (people.py, TPDB_SEAT47)
SEATED47 = {"sit", "sit_swing", "sit_ground", "sit_dangle", "sit_hang", "sit_low", "sit_slide", "crouch", "jump_tuck"}

# v0.46 bench switch (vision/isolation_v046.md), "O" for v0.45's drawing. TPDB_STYLE46 "B": the whole figure's outer edge
# is drawn at 9.5 px (4.5 px in a picture at the set's median scale, the settings' own line) and the lines inside it at
# 5.5 px; and the cel shading has two tones, a shadow and the flat colour, with no pool of light on top. v0.45's figures
# had one 5 px line, under half the weight of the settings' line, and three soft tones against the settings' flat fills.
STYLE46 = os.environ.get("TPDB_STYLE46", "B")
# (after round 3, TPDB_SHADE46 "B": the shadow tone 0.86 of the flat colour for 0.72. As a hard-edged band the darker tone was read as a
# mark on the cloth: "a darker, dull yellow band that looks like a stain or a shadow pasted on", "dark shading patches on the trousers
# look like stains rather than folds". "O" keeps the first three rounds' tone.)
SHADE46 = {"O": 0.72, "B": 0.86}[os.environ.get("TPDB_SHADE46", "B")]
# (after the validator's first run on the release renders, TPDB_INK46 "B": the line is drawn unlit, in the palette's outline colour, which
# is the settings' own line colour. Lit like a surface it came out darker, (28, 28, 34) for (38, 38, 46): render_assets.setup_outline.
# "O" keeps the lit line of every release before, and of the bench's rounds 1 to 3.)
INK46 = os.environ.get("TPDB_INK46", "B")
# v0.48 (TPDB_FLAT48 "B"; vision/isolation_v048.md): one flat tone, no shadow tone. The second tone is laid by a surface's normal, so wherever a
# surface folds away it left a small island of the darker tone: at a trouser's crotch, on a child's shorts, under a jaw. Reviewers of v0.46 had
# such a patch as "a stain", of v0.47 as "her arm drawn faintly through her body", and of this release's first pairs as "a faint lighter
# triangular mark on the far thigh, like a stray patch". The settings are flat fills. "O": v0.46's two tones
FLAT48 = os.environ.get("TPDB_FLAT48", "B")
if FLAT48 == "B":
    SHADE46 = 1.0


def write_config(out_dir, fam, cls, labels, poses, expressions, states, affordances, prop_objects=(), extra=None):
    cfg = {
        "family_id": fam, "class": cls, "root": "ROOT", "builder_version": BUILDER_VERSION,
        "labels": dict(labels, animate=True),
        "poses": poses,
        "prop_objects": sorted(prop_objects),
        "expressions": expressions,
        "expression_states": states,
        "yaws": [0, 45, 90],
        "mirror_ok": True,
        "outline": ({"method": "lineart", "width_px": 5.5, "silhouette_px": 9.5, **({"unlit": True} if INK46 == "B" else {})} if STYLE46 == "B"
                    else {"method": "lineart", "width_px": 5.0}),
        **({"cel": {"shadow": SHADE46, "light": 1.0, **({"rest": True} if os.environ.get("TPDB_SHADE47", "B") == "B" else {})}} if STYLE46 == "B" else {}),
        "affordances": affordances,
        "contradiction_roles": [],
        "license": {"source": "original", "author": "TPDB stand-in cast (procedural)"},
    }
    if extra:
        cfg.update(extra)
    json.dump(cfg, open(os.path.join(out_dir, fam + ".json"), "w"), indent=1)


def main(out_dir, only=None):
    os.makedirs(out_dir, exist_ok=True)
    catalog = {"builder_version": BUILDER_VERSION, "families": {}, "actions": {}, "people_expressions": list(PEOPLE_EXPRESSIONS)}
    cat_path = os.path.join(out_dir, "cast_catalog.json")
    if only and os.path.exists(cat_path):
        catalog = json.load(open(cat_path))
        catalog["builder_version"] = BUILDER_VERSION
    for fam, spec in PEOPLE.items():
        if only and fam not in only:
            continue
        reset_scene()
        if fam == "person.mei" and os.environ.get("TPDB_HAIR34", "L") == "L":
            # v0.34, chosen on the bench: the woman in yellow with long hair, tied back. With the bob, seated reading, she was "a child with
            # short dark hair" or "a boy"; with it, "a woman", "a girl or young woman" (vision/isolation_v034.md). O keeps the bob
            spec = dict(spec, hair="long")
        rig, states, ctx = build_person(spec)
        P = make_people_actions(rig, ctx)
        if bpy.data.objects.get("SkirtPanel"):
            # v0.34 bench: the cloth across the lap shows only seated on a bench or the ground's edge (lower "sit", "sit_low")
            for _n, _m in P.meta.items():
                if _m["lower"] not in ("sit", "sit_low"):
                    P.hides.setdefault(_n, []).append("SkirtPanel")
        if bpy.data.objects.get("SkirtSeat"):
            # v0.47 (TPDB_SEAT47): a skirt is the wrap of the thighs in the seated postures and the bell in the rest
            for _n, _m in P.meta.items():
                # (the lobes over the thighs lie inside the wrap and are not needed with it)
                P.hides.setdefault(_n, []).extend(["Skirt", "SkirtLap"] if _m["lower"] in SEATED47 else ["SkirtSeat", "SkirtSeatLid"])
        poses = {}
        props = []
        hideable = set()
        for name, meta in P.meta.items():
            shown = P.props.get(name, [])
            props += shown
            parts = sorted(n[len(f"PROP_{name}_"):] for n in shown)
            hide = sorted(set(P.hides.get(name, [])))
            hideable |= set(hide)
            poses[name] = {"action": name, "frame": 1, "show": shown, "hide": hide, "props": parts, "airborne": bool(meta.get("airborne"))}
            if name + "__p" in bpy.data.actions:
                poses[name]["action_profile"] = name + "__p"
            if getattr(P, "profile_face", {}).get(name):
                poses[name]["profile_face"] = True      # v0.48 (face.PROF48)
            catalog["actions"][name] = {"lower": meta["lower"], "upper": meta["upper"], "description": meta["description"],
                                        "tags": meta["tags"], "props": parts,
                                        "prop_anchors": sorted(set(P.anchors.get(name, [])))}
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out_dir, fam + ".blend"))
        write_config(out_dir, fam, "person", spec["labels"], poses, list(PEOPLE_EXPRESSIONS), states, PERSON_AFFORDANCES, props,
                     extra={"hideable_objects": sorted(hideable),
                            # v0.48 (face.PROF48): the face of a side view whose pose has the side view's twin
                            **({"expression_states_profile": ctx.states_profile} if getattr(ctx, "states_profile", None) else {})})
        catalog["families"][fam] = {"class": "person", "kind": spec["age"], "labels": spec["labels"],
                                    "wardrobe": {k: spec.get(k) for k in ("top", "bottom", "hair", "hat", "facial_hair", "glasses")},
                                    "poses": list(poses), "expressions": list(PEOPLE_EXPRESSIONS)}
        miss = {a: m for a, m in P.misses.items()}
        print("built", fam, len(poses), "actions", len(props), "props", ("reach misses: " + json.dumps(miss)) if miss else "")
    for fam, spec in QUADRUPEDS.items():
        if only and fam not in only:
            continue
        reset_scene()
        rig, states, names = build_quadruped(spec)
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out_dir, fam + ".blend"))
        pp = getattr(rig, "pose_props", {})        # v0.47: a quadruped's pose may hold a thing of its own (the reading dog's paper)
        poses = {p: {"action": p, "frame": 1, "show": sorted(pp.get(p, [])), "airborne": False} for p in names}
        ph = getattr(rig, "pose_hides", {})        # v0.47: and may hide a part of the standing animal (the collar, redrawn for the upright neck)
        for p in names:
            if ph.get(p):
                poses[p]["hide"] = sorted(ph[p])
        exprs = list(states)
        write_config(out_dir, fam, "animal", spec["labels"], poses, exprs, states, QUAD_AFFORDANCES[spec["kind"]],
                     sorted(n for v in pp.values() for n in v),
                     extra={"hideable_objects": sorted({n for v in ph.values() for n in v})} if ph else None)
        catalog["families"][fam] = {"class": "animal", "kind": spec["kind"], "labels": spec["labels"], "poses": names, "expressions": exprs}
        print("built", fam, len(names), "poses")
    for fam, spec in BIRDS.items():
        if only and fam not in only:
            continue
        reset_scene()
        rig, states, names = build_bird(spec)
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out_dir, fam + ".blend"))
        poses = {p: {"action": p, "frame": 1, "show": [], "airborne": p == "fly"} for p in names}
        exprs = list(states)
        write_config(out_dir, fam, "animal", spec["labels"], poses, exprs, states, ["perch", "fly", "peck", "sing", "swim"])
        catalog["families"][fam] = {"class": "animal", "kind": spec["kind"], "labels": spec["labels"], "poses": names, "expressions": exprs}
        print("built", fam, len(names), "poses")
    json.dump(catalog, open(cat_path, "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "out4", sys.argv[2:] or None)
