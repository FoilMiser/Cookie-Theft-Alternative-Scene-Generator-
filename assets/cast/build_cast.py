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

BUILDER_VERSION = "0.32.0"


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
        "outline": {"method": "lineart", "width_px": 5.0},
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
        rig, states, ctx = build_person(spec)
        P = make_people_actions(rig, ctx)
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
            catalog["actions"][name] = {"lower": meta["lower"], "upper": meta["upper"], "description": meta["description"],
                                        "tags": meta["tags"], "props": parts,
                                        "prop_anchors": sorted(set(P.anchors.get(name, [])))}
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out_dir, fam + ".blend"))
        write_config(out_dir, fam, "person", spec["labels"], poses, list(PEOPLE_EXPRESSIONS), states, PERSON_AFFORDANCES, props,
                     extra={"hideable_objects": sorted(hideable)})
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
        poses = {p: {"action": p, "frame": 1, "show": [], "airborne": False} for p in names}
        exprs = list(states)
        write_config(out_dir, fam, "animal", spec["labels"], poses, exprs, states, QUAD_AFFORDANCES[spec["kind"]])
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
