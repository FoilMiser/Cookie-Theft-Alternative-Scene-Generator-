"""
TPDB asset renderer (Blender 5.2).

Renders every pose x expression x facing listed in an asset config, as a flat,
cel-shaded transparent PNG at a fixed 400 px/m, and writes one manifest per
variant (see asset_manifest.schema.json).

Run inside Blender:
    blender -b person_adult_03.blend -P render_assets.py -- --config person_adult_03.json --out library/
Or with the `bpy` Python module:
    python render_assets.py --blend person_adult_03.blend --config person_adult_03.json --out library/

The script owns the camera, light, color management, outline and output
settings. The .blend owns geometry, rig, poses (actions), expressions
(shape keys), anchors (empties named ANCHOR_<name>) and materials.
"""
import argparse
import hashlib
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blender_run  # noqa: E402

blender_run.ensure(__file__)

import bpy  # noqa: E402
import numpy as np  # noqa: E402
from bpy_extras.object_utils import world_to_camera_view  # noqa: E402
from mathutils import Vector  # noqa: E402

SCRIPT_VERSION = "0.4.0"
PPM = 400.0            # pixels per meter
TILT_DEG = 10.0        # camera tilt below horizontal
MARGIN_PX = 16
HIDDEN_TOL_M = 0.06    # ignore the anchor's own part when testing occlusion
LIGHT_RIG = "virtual-normal-light-v2"
SHADOW_FACTOR = 0.72   # shadow tone = base color x this (linear light)
HIGHLIGHT_FACTOR = 1.22  # light-pool tone = base color x this (linear light, clipped at white)
VIRTUAL_LIGHT = (-0.38, -0.42, 0.82)   # world direction toward the light: upper left, in front
SETTLE_BELOW = 0.36      # remapped normal.light below this = darker settle (surfaces facing down/away)
LIGHT_POOL_AT = 0.86     # remapped normal.light above this = light pool (surfaces facing up/toward)
INK = (0.149, 0.149, 0.180)   # palette "outline" #26262e, sRGB

DEFAULT_KINDS = {
    "foot_L": "contact", "foot_R": "contact", "base": "contact", "seat": "contact",
    "paw_FL": "contact", "paw_FR": "contact", "paw_BL": "contact", "paw_BR": "contact",
    "hand_L_grip": "grip", "hand_R_grip": "grip", "grip": "grip",
    "eye_L": "gaze", "eye_R": "gaze", "gaze_target": "gaze",
    "nozzle": "emit", "spout": "emit", "chimney": "emit", "mouth": "emit",
    "hose_in": "attach", "rope_end": "attach", "leash_clip": "attach",
    "top": "surface", "head_top": "landmark", "center": "landmark",
}


# ---------------------------------------------------------------- utilities
def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def parse_args(argv):
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        argv = argv[1:]
    ap = argparse.ArgumentParser()
    ap.add_argument("--blend", help="Only needed when running with the bpy module.")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--samples", type=int, default=32)
    ap.add_argument("--no-cel", action="store_true", help="Keep the file's own materials instead of converting to two-tone cel.")
    args = ap.parse_args(argv)
    args.out = os.path.abspath(args.out)   # an installed Blender saves a relative render path somewhere else than Python looks
    return args


# ------------------------------------------------------------ scene setup
def setup_render(scene, samples):
    r = scene.render
    r.engine = "BLENDER_EEVEE"
    r.film_transparent = True
    r.resolution_percentage = 100
    r.image_settings.file_format = "PNG"
    r.image_settings.color_mode = "RGBA"
    r.image_settings.color_depth = "8"
    scene.eevee.taa_render_samples = samples
    vs = scene.view_settings
    vs.view_transform = "Standard"
    vs.look = "None"
    vs.exposure = 0.0
    vs.gamma = 1.0
    scene.display_settings.display_device = "sRGB"
    if scene.world is None:
        scene.world = bpy.data.worlds.new("TPDB_World")
    scene.world.color = (0.25, 0.25, 0.25)


def setup_camera(scene):
    cam = bpy.data.objects.get("TPDB_CAM")
    if cam is None:
        cam = bpy.data.objects.new("TPDB_CAM", bpy.data.cameras.new("TPDB_CAM"))
        scene.collection.objects.link(cam)
    cam.data.type = "ORTHO"
    cam.data.sensor_fit = "AUTO"
    cam.data.clip_start = 0.01
    cam.data.clip_end = 200.0
    cam.rotation_mode = "XYZ"
    cam.rotation_euler = (math.radians(90.0 - TILT_DEG), 0.0, 0.0)
    scene.camera = cam
    return cam


def setup_light(scene):
    sun = bpy.data.objects.get("TPDB_SUN")
    if sun is None:
        sun = bpy.data.objects.new("TPDB_SUN", bpy.data.lights.new("TPDB_SUN", "SUN"))
        scene.collection.objects.link(sun)
    sun.data.energy = 3.0
    sun.data.angle = 0.0
    sun.data.use_shadow = False   # no cast shadows: tones come from surface angle only
    # Light travels toward +X (picture right), +Y (away from camera) and down,
    # so it appears to come from the picture's upper left, in front, at 45 deg.
    d = Vector((0.6, 0.45, -1.0)).normalized()
    sun.rotation_mode = "QUATERNION"
    sun.rotation_quaternion = d.to_track_quat("-Z", "Y")
    return sun


def setup_outline(scene, root, width_px):
    """Scene Line Art at a fixed pixel width (radius in meters = px / 2 / PPM)."""
    gp = bpy.data.objects.get("TPDB_LINEART")
    if gp is None:
        for o in bpy.context.view_layer.objects:
            o.select_set(False)
        bpy.ops.object.grease_pencil_add(type="LINEART_SCENE")
        gp = bpy.context.active_object
        gp.name = "TPDB_LINEART"
    mod = next(m for m in gp.modifiers if m.type == "LINEART")
    mod.radius = (width_px / 2.0) / PPM
    mod.use_contour = True
    mod.use_crease = False
    mod.use_intersection = True
    mat = mod.target_material or (gp.material_slots[0].material if gp.material_slots else None)
    if mat is not None and mat.grease_pencil is not None:
        mat.grease_pencil.color = (*[srgb_to_linear(c) for c in INK], 1.0)
    return gp


def to_cel(materials):
    """Three-tone cel from a fixed virtual light, in the Clawd manner: a light pool on
    surfaces facing up toward the light, the exact palette color elsewhere, and a darker
    settle on surfaces facing down and away. Uses the surface normal only, so the result
    is the same in any engine and never shows cast-shadow blotches."""
    for mat in materials:
        if mat is None or getattr(mat, "grease_pencil", None) is not None:
            continue
        mat.use_nodes = True
        nt = mat.node_tree
        base = None
        for n in nt.nodes:
            if n.type == "BSDF_PRINCIPLED":
                base = tuple(n.inputs["Base Color"].default_value)[:3]
            elif n.type == "BSDF_DIFFUSE" and base is None:
                base = tuple(n.inputs["Color"].default_value)[:3]
            elif n.type == "EMISSION" and base is None and "tpdb_base_color" in mat:
                base = tuple(mat["tpdb_base_color"])
        if base is None:
            base = tuple(mat.get("tpdb_base_color", mat.diffuse_color[:3]))
        nt.nodes.clear()
        geo = nt.nodes.new("ShaderNodeNewGeometry")
        dot = nt.nodes.new("ShaderNodeVectorMath")
        dot.operation = "DOT_PRODUCT"
        dot.inputs[1].default_value = VIRTUAL_LIGHT
        ramp = nt.nodes.new("ShaderNodeValToRGB")
        ramp.color_ramp.interpolation = "CONSTANT"
        e0, e1 = ramp.color_ramp.elements[0], ramp.color_ramp.elements[1]
        e0.position, e0.color = 0.0, (SHADOW_FACTOR, SHADOW_FACTOR, SHADOW_FACTOR, 1)
        e1.position, e1.color = SETTLE_BELOW, (1, 1, 1, 1)
        e2 = ramp.color_ramp.elements.new(LIGHT_POOL_AT)
        e2.color = (HIGHLIGHT_FACTOR, HIGHLIGHT_FACTOR, HIGHLIGHT_FACTOR, 1)
        remap = nt.nodes.new("ShaderNodeMapRange")       # dot in [-1, 1] -> [0, 1]
        remap.inputs["From Min"].default_value = -1.0
        remap.inputs["From Max"].default_value = 1.0
        mult = nt.nodes.new("ShaderNodeVectorMath")
        mult.operation = "MULTIPLY"
        mult.inputs[1].default_value = base
        emit = nt.nodes.new("ShaderNodeEmission")
        emit.inputs["Strength"].default_value = 1.0
        out = nt.nodes.new("ShaderNodeOutputMaterial")
        nt.links.new(geo.outputs["Normal"], dot.inputs[0])
        nt.links.new(dot.outputs["Value"], remap.inputs["Value"])
        nt.links.new(remap.outputs["Result"], ramp.inputs["Fac"])
        nt.links.new(ramp.outputs["Color"], mult.inputs[0])
        nt.links.new(mult.outputs[0], emit.inputs["Color"])
        nt.links.new(emit.outputs[0], out.inputs["Surface"])
        mat["tpdb_base_color"] = list(base)


# ------------------------------------------------------- pose / expression
def asset_objects(root):
    return [root] + list(root.children_recursive)


def apply_pose(root, pose_spec):
    arms = [o for o in asset_objects(root) if o.type == "ARMATURE"]
    for arm in arms:
        if arm.animation_data is None:
            arm.animation_data_create()
        action_name = pose_spec.get("action")
        if not action_name:
            arm.animation_data.action = None
            for pb in arm.pose.bones:
                pb.location = (0, 0, 0)
                pb.rotation_quaternion = (1, 0, 0, 0)
                pb.rotation_euler = (0, 0, 0)
                pb.scale = (1, 1, 1)
        else:
            act = bpy.data.actions[action_name]
            arm.animation_data.action = act
            slots = getattr(act, "slots", None)
            if slots and getattr(arm.animation_data, "action_slot", None) is None:
                arm.animation_data.action_slot = slots[0]
    bpy.context.scene.frame_set(int(pose_spec.get("frame", 1)))


def apply_expression_states(states, expression):
    """Expression = per-object visibility and rest-space transform (face-kit assets)."""
    from mathutils import Matrix
    st = states.get(expression, {})
    for name, s in st.items():
        ob = bpy.data.objects.get(name)
        if ob is None:
            continue
        ob.hide_render = bool(s.get("hide", False))
        ob.hide_viewport = ob.hide_render
        if "basis" in s:
            b = s["basis"]
            ob.matrix_basis = Matrix([b[0:4], b[4:8], b[8:12], b[12:16]])
    bpy.context.view_layer.update()


def apply_pose_objects(cfg, pose_name):
    """Show only the props that belong to this pose; every other prop object stays hidden."""
    shown = set(cfg["poses"][pose_name].get("show", []))
    for name in cfg.get("prop_objects", []):
        ob = bpy.data.objects.get(name)
        if ob is None:
            continue
        ob.hide_render = name not in shown
        ob.hide_viewport = ob.hide_render
    # base body parts an action swaps out (mitten hands replaced by open hands)
    hidden = set(cfg["poses"][pose_name].get("hide", []))
    for name in cfg.get("hideable_objects", []):
        ob = bpy.data.objects.get(name)
        if ob is None:
            continue
        ob.hide_render = name in hidden
        ob.hide_viewport = ob.hide_render
    bpy.context.view_layer.update()


def apply_expression(face, expression, all_expressions):
    if face is None or face.data.shape_keys is None:
        return
    keys = face.data.shape_keys.key_blocks
    for name in all_expressions:
        if name in keys:
            keys[name].value = 0.0
    if expression in keys:
        keys[expression].value = 1.0


def split_leg(root, part, fwd):
    """v0.31: a rider cut in two, so that a plank can run between the legs. "near" is the figure without the leg further from the camera,
    "far" that leg alone, both in the whole figure's frame (frame first). Every mesh that holds the leg is cut by its bone weights, as the legs and the
    trousers are one mesh each; shoes are objects on the foot's bone. Returns what undoes it."""
    origin = root.matrix_world.translation
    depth = {}
    for o in asset_objects(root):
        for sd in ("L", "R"):
            if o.name.split(".")[0] == f"ANCHOR_foot_{sd}":
                depth[sd] = (o.matrix_world.translation - origin).dot(fwd)
    far = "L" if depth["L"] > depth["R"] else "R"
    bones = {f"thigh_{far}", f"shin_{far}", f"foot_{far}"}
    undo = []
    for o in asset_objects(root):
        if o.type == "ARMATURE" or o.name.startswith("ANCHOR_"):
            continue
        on_leg = o.parent_type == "BONE" and o.parent_bone in bones
        names = {g.index: g.name for g in o.vertex_groups} if o.type == "MESH" else {}
        weights = None
        if not on_leg and bones & set(names.values()):
            weights = [sum(g.weight for g in v.groups if names.get(g.group) in bones) for v in o.data.vertices]
            if max(weights) < 0.5:
                weights = None
        if weights is not None:
            vg = o.vertex_groups.new(name="TPDB_LEG")
            for i, w in enumerate(weights):
                vg.add([i], w, "REPLACE")
            m = o.modifiers.new("TPDB_LEG", "MASK")
            m.vertex_group = vg.name
            m.threshold = 0.5
            m.invert_vertex_group = part == "near"
            undo.append((o, m, vg))
            continue
        hide = on_leg if part == "near" else not on_leg
        if hide and not o.hide_render:
            o.hide_render = True
            undo.append((o, None, None))
    bpy.context.view_layer.update()

    def restore():
        for o, m, vg in undo:
            if m is None:
                o.hide_render = False
            else:
                o.modifiers.remove(m)
                o.vertex_groups.remove(vg)
        bpy.context.view_layer.update()
    return restore


# ---------------------------------------------------------------- framing
def frame_camera(scene, cam, root):
    dg = bpy.context.evaluated_depsgraph_get()
    m = cam.matrix_world.to_3x3()
    right, up, fwd = m.col[0].normalized(), m.col[1].normalized(), -m.col[2].normalized()
    rs, us, corners = [], [], []
    for o in asset_objects(root):
        if o.type != "MESH" or o.hide_render:
            continue
        oe = o.evaluated_get(dg)
        me = oe.to_mesh()            # posed, deformed geometry (bound_box can be stale)
        mw = oe.matrix_world
        pts = [mw @ vtx.co for vtx in me.vertices]
        oe.to_mesh_clear()
        if len(pts) > 400:
            pts = pts[::max(1, len(pts) // 400)] + [max(pts, key=lambda q: q.dot(right)), min(pts, key=lambda q: q.dot(right)),
                                                  max(pts, key=lambda q: q.dot(up)), min(pts, key=lambda q: q.dot(up)),
                                                  min(pts, key=lambda q: q.z)]
        for p in pts:
            corners.append(p)
            rs.append(p.dot(right))
            us.append(p.dot(up))
    rmin, rmax, umin, umax = min(rs), max(rs), min(us), max(us)
    res_x = int(math.ceil((rmax - rmin) * PPM)) + 2 * MARGIN_PX
    res_y = int(math.ceil((umax - umin) * PPM)) + 2 * MARGIN_PX
    scene.render.resolution_x, scene.render.resolution_y = res_x, res_y
    cam.data.ortho_scale = max(res_x, res_y) / PPM
    rc, uc = (rmin + rmax) / 2, (umin + umax) / 2
    cam.location = right * rc + up * uc - fwd * 40.0
    bpy.context.view_layer.update()
    return corners, fwd


def project(scene, cam, p):
    v = world_to_camera_view(scene, cam, p)
    return [round(v.x * scene.render.resolution_x, 2), round((1.0 - v.y) * scene.render.resolution_y, 2)]


def is_hidden(scene, p, fwd):
    """True if geometry sits more than HIDDEN_TOL_M in front of the anchor.

    Anchors usually sit inside a small part (an eye, a hand, a shoe), so the part's
    own surface always lies a few centimeters in front; the tolerance ignores it.
    """
    dg = bpy.context.evaluated_depsgraph_get()
    origin = p - fwd * 30.0
    hit, loc, *_ = scene.ray_cast(dg, origin, fwd, distance=30.0)
    return bool(hit and (loc - origin).length < 30.0 - HIDDEN_TOL_M)


# ------------------------------------------------------------ image post
def write_mask(img_path, mask_path):
    img = bpy.data.images.load(img_path, check_existing=False)
    w, h = img.size
    px = np.empty(w * h * 4, dtype=np.float32)
    img.pixels.foreach_get(px)
    alpha = px.reshape(h, w, 4)[..., 3]                 # rows bottom-up
    solid = alpha >= 0.5
    ys, xs = np.nonzero(solid[::-1])                     # top-down rows
    bbox = [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]
    m = bpy.data.images.new("tpdb_mask", w, h, alpha=False)
    v = np.repeat(solid.astype(np.float32)[..., None], 4, axis=2)
    v[..., 3] = 1.0
    m.pixels.foreach_set(v.ravel())
    m.filepath_raw = mask_path
    m.file_format = "PNG"
    m.save()
    bpy.data.images.remove(m)
    bpy.data.images.remove(img)
    return bbox, w, h


# ------------------------------------------------------------------ main
def render_family(cfg, out_dir, blend_path, samples, cel=True):
    scene = bpy.context.scene
    root = bpy.data.objects[cfg.get("root", "ROOT")]
    face = bpy.data.objects.get(cfg.get("face_mesh", "")) if cfg.get("face_mesh") else None
    os.makedirs(out_dir, exist_ok=True)

    setup_render(scene, samples)
    cam = setup_camera(scene)
    setup_light(scene)
    outline = cfg.get("outline", {"method": "lineart", "width_px": 4.0})
    if outline["method"] == "lineart":
        setup_outline(scene, root, outline["width_px"])
    if cel:
        to_cel({s.material for o in asset_objects(root) for s in o.material_slots})

    blend_sha = sha256(blend_path)
    expressions = cfg.get("expressions", ["none"])
    if cfg.get("variants"):
        combos = [(p, e, int(y)) for p, e, y in cfg["variants"]]
    else:
        combos = [(p, e, y) for p in cfg["poses"] for e in expressions for y in cfg.get("yaws", [0, 45, 90])]
    written = []
    for pose_name, expr, yaw in combos:
        if True:
            if True:
                base_pose, _, part = pose_name.partition("~")      # (v0.31: see split_leg)
                pose_spec = cfg["poses"][base_pose]
                if yaw == 90 and pose_spec.get("action_profile"):
                    # v0.27: in full profile, the pose's twin with the head turned a little toward the viewer
                    pose_spec = dict(pose_spec, action=pose_spec["action_profile"])
                apply_pose(root, pose_spec)
                apply_pose_objects(cfg, base_pose)
                if cfg.get("expression_states"):
                    apply_expression_states(cfg["expression_states"], expr)
                else:
                    apply_expression(face, expr, expressions)
                root.rotation_mode = "XYZ"
                root.rotation_euler = (0.0, 0.0, math.radians(yaw))
                if cfg.get("profile_turn") and yaw == 90 and base_pose not in cfg.get("profile_skip", ()):
                    # v0.27: a head in full profile turned a little toward the viewer
                    from mathutils import Quaternion
                    for arm in [o for o in asset_objects(root) if o.type == "ARMATURE"]:
                        pb = arm.pose.bones.get("head")
                        if pb is not None:
                            pb.rotation_mode = "QUATERNION"
                            pb.rotation_quaternion = pb.rotation_quaternion @ Quaternion((0, 1, 0), math.radians(cfg["profile_turn"]))
                bpy.context.view_layer.update()

                corners, fwd = frame_camera(scene, cam, root)
                vid = f'{cfg["family_id"]}__{pose_name}__{expr}__y{yaw:03d}'
                img_path = os.path.join(out_dir, vid + ".png")
                mask_path = os.path.join(out_dir, vid + ".mask.png")
                scene.render.filepath = img_path
                restore = split_leg(root, part, fwd) if part else None
                bpy.ops.render.render(write_still=True)
                if restore:
                    restore()
                bbox, w, h = write_mask(img_path, mask_path)

                origin = root.matrix_world.translation.copy()
                anchors = {}
                for o in asset_objects(root):
                    if not o.name.startswith("ANCHOR_"):
                        continue
                    name = o.name[len("ANCHOR_"):].split(".")[0]
                    if "@" in name:                     # prop anchors belong to one pose
                        name, owner = name.split("@", 1)
                        if owner != base_pose:
                            continue
                    p = o.matrix_world.translation.copy()
                    kind = cfg.get("anchor_kinds", {}).get(name) or DEFAULT_KINDS.get(name, "landmark")
                    anchors[name] = {
                        "kind": kind,
                        "px": project(scene, cam, p),
                        "depth_m": round((p - origin).dot(fwd), 4),
                        "hidden": is_hidden(scene, p, fwd),
                    }

                # Footprint = what touches or sits near the ground (bottom 25 cm), in the
                # asset's own axes, so a raised arm does not widen its floor space.
                inv = root.matrix_world.inverted()
                local = [inv @ c for c in corners]
                low = [p for p in local if p.z < 0.25] or local
                local = low
                manifest = {
                    "schema_version": "0.2",
                    "variant_id": vid,
                    "family_id": cfg["family_id"],
                    "class": cfg["class"],
                    "labels": cfg["labels"],
                    "variant": {"pose": pose_name, "expression": expr, "yaw_deg": yaw,
                                "mirror_ok": bool(cfg.get("mirror_ok", True)),
                                "airborne": bool(pose_spec.get("airborne", False)),
                                "props": list(pose_spec.get("props", []))},
                    "render": {
                        "blender_version": bpy.app.version_string,
                        "script_version": SCRIPT_VERSION,
                        "blend_file": os.path.basename(blend_path),
                        "blend_sha256": blend_sha,
                        "engine": scene.render.engine,
                        "pixels_per_meter": PPM,
                        "camera": {"type": "ortho", "tilt_deg": TILT_DEG},
                        "light_rig": LIGHT_RIG,
                        "view_transform": scene.view_settings.view_transform,
                        "outline": outline,
                    },
                    "files": {
                        "image": {"path": os.path.basename(img_path), "sha256": sha256(img_path), "width": w, "height": h},
                        "mask": {"path": os.path.basename(mask_path), "sha256": sha256(mask_path), "width": w, "height": h},
                    },
                    "geometry": {
                        "ground_point_px": project(scene, cam, origin),
                        "bbox_px": bbox,
                        "height_m": round(max(c.z for c in corners) - origin.z, 4),
                        "footprint_m": {"width": round(max(c.x for c in local) - min(c.x for c in local), 4),
                                        "depth": round(max(c.y for c in local) - min(c.y for c in local), 4)},
                    },
                    "anchors": anchors,
                    "affordances": cfg.get("affordances", []),
                    "contradiction_roles": cfg.get("contradiction_roles", []),
                    "license": cfg["license"],
                    "qa": {"legibility_checked": False},
                }
                with open(os.path.join(out_dir, vid + ".json"), "w") as f:
                    json.dump(manifest, f, indent=1)
                written.append(vid)
    return written


def main(argv):
    args = parse_args(argv)
    if args.blend:
        bpy.ops.wm.open_mainfile(filepath=os.path.abspath(args.blend))
    blend_path = bpy.data.filepath
    with open(args.config) as f:
        cfg = json.load(f)
    done = render_family(cfg, args.out, blend_path, args.samples, cel=not args.no_cel)
    print(f"TPDB: rendered {len(done)} variants to {args.out}")


if __name__ == "__main__":
    main(sys.argv)
