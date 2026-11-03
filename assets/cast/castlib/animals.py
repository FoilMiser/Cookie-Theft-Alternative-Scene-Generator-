"""Animals: a parameterized quadruped (dogs, cats, goat) and birds (songbirds, duck)."""
import json
import math
import os

import bpy  # noqa: F401
import bmesh
from mathutils import Matrix, Quaternion, Vector

from .core import Rig, _mesh_object, anchor, cyl, ellipsoid, link, list_m, mat, nrm, skin_like, skin_object, upd
from .face import Face
from .people import surface_points


# ================================================================== quadrupeds
def build_quadruped(spec):
    kind = spec["kind"]
    S = spec.get("scale", 1.0)
    LH = spec.get("legs", 1.0)

    def P(x, y, z):
        return Vector((x * S, y * S, z * S))

    root = link(bpy.data.objects.new("ROOT", None))
    hip_z, chest_z, knee_z = 0.44 * LH, 0.46 * LH, 0.24 * LH
    bones = {
        "hips": (P(0, 0.20, hip_z), P(0, 0.20, hip_z + 0.06), None),
        "spine": (P(0, 0.20, hip_z), P(0, -0.16, chest_z), "hips"),
        "neck": (P(0, -0.16, chest_z), P(0, -0.25, chest_z + 0.15), "spine"),
        "head": (P(0, -0.25, chest_z + 0.15), P(0, -0.25, chest_z + 0.40), "neck"),
        "tail1": (P(0, 0.27, hip_z + 0.04), P(0, 0.38, hip_z + 0.14), "hips"),
        "tail2": (P(0, 0.38, hip_z + 0.14), P(0, 0.44, hip_z + 0.27), "tail1"),
    }
    for sd, sg in (("L", 1), ("R", -1)):
        bones.update({
            f"fleg_{sd}": (P(sg * 0.075, -0.15, chest_z - 0.06), P(sg * 0.075, -0.15, knee_z), "spine"),
            f"fshin_{sd}": (P(sg * 0.075, -0.15, knee_z), P(sg * 0.075, -0.16, 0.04), f"fleg_{sd}"),
            f"bleg_{sd}": (P(sg * 0.075, 0.20, hip_z - 0.04), P(sg * 0.075, 0.25, knee_z), "hips"),
            f"bshin_{sd}": (P(sg * 0.075, 0.25, knee_z), P(sg * 0.075, 0.21, 0.04), f"bleg_{sd}"),
        })
    rig = Rig(root, bones)
    body, belly, acc = spec["body"], spec.get("belly", spec["body"]), spec.get("accent", spec["body"])
    k = S
    G = spec.get("girth", 1.0)

    verts = [P(0, 0.22, hip_z), P(0, -0.15, chest_z), P(0, -0.24, chest_z + 0.12),
             P(0, 0.097, hip_z + 0.007), P(0, -0.027, hip_z + 0.013)]
    radii = [(0.115 * k * G, 0.12 * k * G), (0.125 * k * G, 0.12 * k * G), (0.07 * k, 0.07 * k),
             (0.118 * k * G, 0.12 * k * G), (0.122 * k * G, 0.12 * k * G)]
    wts = [{"hips": 1.0}, {"spine": 1.0}, {"neck": 1.0}, {"hips": 0.67, "spine": 0.33}, {"hips": 0.33, "spine": 0.67}]
    edges = [(0, 3), (3, 4), (4, 1), (1, 2)]
    LR = spec.get("leg_r", 1.0)
    for sd, sg in (("L", 1), ("R", -1)):
        i0 = len(verts)
        verts += [P(sg * 0.075, -0.15, chest_z - 0.07), P(sg * 0.075, -0.15, knee_z), P(sg * 0.075, -0.16, 0.035)]
        radii += [0.058 * k * LR, 0.046 * k * LR, 0.040 * k * LR]
        wts += [{"spine": 0.4, f"fleg_{sd}": 0.6}, {f"fleg_{sd}": 0.5, f"fshin_{sd}": 0.5}, {f"fshin_{sd}": 1.0}]
        edges += [(1, i0), (i0, i0 + 1), (i0 + 1, i0 + 2)]
        i0 = len(verts)
        verts += [P(sg * 0.075, 0.20, hip_z - 0.05), P(sg * 0.075, 0.25, knee_z), P(sg * 0.075, 0.21, 0.035)]
        radii += [0.070 * k * LR, 0.046 * k * LR, 0.040 * k * LR]
        wts += [{"hips": 0.4, f"bleg_{sd}": 0.6}, {f"bleg_{sd}": 0.5, f"bshin_{sd}": 0.5}, {f"bshin_{sd}": 1.0}]
        edges += [(0, i0), (i0, i0 + 1), (i0 + 1, i0 + 2)]
    if kind == "goat":
        # a proper neck up to the head (the goat's head sits high on long legs)
        i0 = len(verts)
        verts += [P(0, -0.27, chest_z + 0.20)]
        radii += [(0.060 * k, 0.062 * k)]
        wts += [{"neck": 0.5, "head": 0.5}]
        edges += [(2, i0)]
    tail = spec.get("tail", kind)
    i0 = len(verts)
    if tail == "goat":
        verts += [P(0, 0.30, hip_z + 0.06), P(0, 0.33, hip_z + 0.13)]
        radii += [0.030 * k, 0.020 * k]
        wts += [{"tail1": 1.0}, {"tail1": 1.0}]
        edges += [(0, i0), (i0, i0 + 1)]
    else:
        tr = {"dog": (0.030, 0.026, 0.018), "cat": (0.026, 0.022, 0.020), "curl": (0.034, 0.030, 0.026)}[tail]
        verts += [P(0, 0.30, hip_z + 0.06), P(0, 0.38, hip_z + 0.14), P(0, 0.44, hip_z + 0.27)]
        radii += [tr[0] * k, tr[1] * k, tr[2] * k]
        wts += [{"tail1": 1.0}, {"tail1": 0.5, "tail2": 0.5}, {"tail2": 1.0}]
        edges += [(0, i0), (i0, i0 + 1), (i0 + 1, i0 + 2)]
    body_ob = skin_object("Body", verts, edges, radii, body, rig, wts)

    for sd, sg in (("L", 1), ("R", -1)):
        ellipsoid(f"FPaw_{sd}", P(sg * 0.075, -0.180, 0.030), (0.046 * k * LR, 0.058 * k * LR, 0.032 * k), spec.get("paws", belly), rig, f"fshin_{sd}")
        ellipsoid(f"BPaw_{sd}", P(sg * 0.075, 0.195, 0.030), (0.046 * k * LR, 0.058 * k * LR, 0.032 * k), spec.get("paws", belly), rig, f"bshin_{sd}")
    ellipsoid("Chest", P(0, -0.22, chest_z - 0.02), (0.085 * k, 0.05 * k, 0.095 * k), belly, rig, "spine")

    # spots on the flanks, sitting on the actual body surface
    if spec.get("spots"):
        pts = surface_points(body_ob)
        for i, (y, z, rx, rz, side) in enumerate(spec["spots"]):
            yy, zz = y * S, z * S
            near = [q for q in pts if abs(q.y - yy) < 0.03 * S and abs(q.z - zz) < 0.03 * S and q.x * side > 0]
            xs = max((abs(q.x) for q in near), default=0.11 * S)
            bone = "hips" if y > 0.05 else "spine"
            skin_like(ellipsoid(f"Spot{i}", Vector((side * (xs - 0.004 * S), yy, zz)), (0.012 * k, rx * k, rz * k), spec["spot_col"], rig, bone), body_ob, rig)   # v0.15: bends with the flank

    hc = P(0, -0.30, chest_z + 0.22)
    hr = spec.get("head_r", 0.115 if kind == "dog" else 0.135) * k
    ellipsoid("Head", hc, (hr * 1.02, hr, hr * 0.96), body, rig, "head", seg=36, rings=20)
    ears = spec.get("ears", "flop" if kind == "dog" else "prick")
    if kind in ("dog", "goat"):
        sl = spec.get("snout", 1.0)
        snout_c = hc + Vector((0, -hr * 0.95, -0.045 * k))
        ellipsoid("Snout", snout_c, (0.058 * k * (0.85 if kind == "goat" else 1.0), 0.062 * k * sl, 0.045 * k), belly, rig, "head")
        nose_p = snout_c + Vector((0, -0.058 * k * sl, 0.012 * k))
        ellipsoid("NoseTip", nose_p, (0.020 * k, 0.014 * k, 0.015 * k), "outline" if kind == "dog" else "pink", rig, "head")
        mouth_p = snout_c + Vector((0, -0.045 * k * sl, -0.032 * k))
    else:
        snout_c = hc + Vector((0, -hr * 0.90, -0.035 * k))
        ellipsoid("Snout", snout_c, (0.040 * k, 0.030 * k, 0.028 * k), belly, rig, "head")
        nose_p = snout_c + Vector((0, -0.030 * k, 0.012 * k))
        ellipsoid("NoseTip", nose_p, (0.011 * k, 0.007 * k, 0.008 * k), "pink", rig, "head")
        mouth_p = snout_c + Vector((0, -0.024 * k, -0.025 * k))
    for sd, sg in (("L", 1), ("R", -1)):
        if ears == "flop":
            ellipsoid(f"Ear_{sd}", hc + Vector((sg * hr * 0.92, 0.02 * k, -0.035 * k)), (0.028 * k, 0.050 * k, 0.085 * k), acc, rig, "head",
                      rot=Quaternion((0, 1, 0), sg * 0.25))
        elif ears == "goat":
            ellipsoid(f"Ear_{sd}", hc + Vector((sg * hr * 1.05, 0.02 * k, 0.01 * k)), (0.075 * k, 0.030 * k, 0.022 * k), acc, rig, "head",
                      rot=Quaternion((0, 1, 0), -sg * 0.35))
        else:
            big = spec.get("ear_size", 1.0)
            bm = bmesh.new()
            bmesh.ops.create_cone(bm, cap_ends=True, segments=16, radius1=0.060 * k * big, radius2=0.004 * k, depth=0.11 * k * big)
            ob = _mesh_object(f"Ear_{sd}", bm, acc if kind == "dog" else body)
            ob.location = hc + Vector((sg * hr * 0.55, 0.0, hr * 0.85))
            ob.rotation_euler = (0.1, sg * 0.35, 0)
            ob.scale = (1, 0.55, 1)
            upd()
            rig.attach(ob, "head")
            if spec.get("inner_ear"):
                bm = bmesh.new()
                bmesh.ops.create_cone(bm, cap_ends=True, segments=16, radius1=0.036 * k * big, radius2=0.003 * k, depth=0.07 * k * big)
                ob2 = _mesh_object(f"EarIn_{sd}", bm, spec["inner_ear"])
                ob2.location = hc + Vector((sg * hr * 0.55, -0.012 * k, hr * 0.82))
                ob2.rotation_euler = (0.1, sg * 0.35, 0)
                ob2.scale = (1, 0.40, 1)
                upd()
                rig.attach(ob2, "head")
    if spec.get("horns"):
        # horns sweep up and back in a tapering arc (v0.17: horn_size, larger and darker, so a white goat is not "a lamb or
        # a white dog")
        hs = spec.get("horn_size", 1.0)
        for sd, sg in (("L", 1), ("R", -1)):
            base = hc + Vector((sg * hr * 0.34, 0.015 * k, hr * 0.84))
            arc = [base + Vector((sg * 0.012 * t * hs, (0.075 * t * t + 0.020 * t) * hs, (0.085 * t - 0.050 * t * t * t) * hs)) * k
                   for t in (0.0, 0.3, 0.55, 0.8, 1.0)]
            for i in range(len(arc) - 1):
                r0 = 0.019 * k * min(hs, 1.25) * (1 - 0.8 * i / 4)
                r1 = 0.019 * k * min(hs, 1.25) * (1 - 0.8 * (i + 1) / 4)
                ob = cyl(f"Horn_{sd}{i}", arc[i], arc[i + 1] + (arc[i + 1] - arc[i]) * 0.08, r0, spec.get("horn_col", "khaki"), r1=r1)
                rig.attach(ob, "head")
    if spec.get("beard"):
        bs = spec.get("beard_size", 1.0)
        if bs > 1.0:
            # v0.17: a pointed tuft growing from the chin (an oval hung below the snout read as a tongue or a tag)
            ob = cyl("Beard", mouth_p + Vector((0, 0.010, 0.006)) * k, mouth_p + Vector((0, 0.026, -0.055 * bs)) * k, 0.024 * k,
                     spec.get("beard_col", belly), r1=0.004 * k)
            rig.attach(ob, "head")
        else:
            ellipsoid("Beard", mouth_p + Vector((0, 0.012, -0.040)) * k, (0.022 * k, 0.020 * k, 0.040 * k), spec.get("beard_col", belly), rig, "head")
    if spec.get("collar"):
        ob = cyl("Collar", P(0, -0.20, chest_z + 0.06) + Vector((0, 0.03, 0)) * k, P(0, -0.235, chest_z + 0.115), 0.075 * k, spec["collar"], seg=24)
        rig.attach(ob, "neck")

    face = Face(rig, "head", hc, (hr * 1.02, hr, hr * 0.96), k, prefix="F")
    eye_dx, eye_z = 0.052 * k, 0.022 * k
    r_e = 0.024 * k
    for sd, sg in (("L", 1), ("R", -1)):
        x = sg * eye_dx
        face.place(f"eye_{sd}", ellipsoid("eye", (0, 0, 0), (1, 1, 1), "outline"), face.frame(x, eye_z, 0.0, scale=(r_e * 0.85, 0.010 * k, r_e * 1.15)))
        face.place(f"catch_{sd}", ellipsoid("catch", (0, 0, 0), (1, 1, 1), "cream"), face.frame(x + 0.006 * k * sg, eye_z + 0.012 * k, 0.009 * k, scale=(r_e * 0.30, 0.004 * k, r_e * 0.36)))
        w = r_e * 1.1
        face.curve_on(f"arcup_{sd}", [(x - w, eye_z - 0.010 * k), (x, eye_z + 0.013 * k), (x + w, eye_z - 0.010 * k)], 0.006 * k, "outline", 0.004 * k)
        face.curve_on(f"arcdn_{sd}", [(x - w, eye_z + 0.002 * k), (x, eye_z - 0.012 * k), (x + w, eye_z + 0.002 * k)], 0.006 * k, "outline", 0.004 * k)
        face.place(f"brow_{sd}", ellipsoid("brow", (0, 0, 0), (1, 1, 1), "outline"),
                   face.frame(x, eye_z + 0.040 * k, 0.004 * k, spin=-math.radians(20) * sg, scale=(0.020 * k, 0.006 * k, 0.006 * k)))
    face.obj("tongue", ellipsoid("Tongue", mouth_p + Vector((0, -0.006 * k, -0.018 * k)), (0.020 * k, 0.010 * k, 0.026 * k), "throat", rig, "head"))

    expr = {
        "neutral": {"eye_L", "eye_R", "catch_L", "catch_R"},
        "happy": {"arcup_L", "arcup_R"} | ({"tongue"} if kind == "dog" else set()),
        "sleepy": {"arcdn_L", "arcdn_R"},
        "alert": {"eye_L", "eye_R", "catch_L", "catch_R"},
        "sad": {"eye_L", "eye_R", "catch_L", "catch_R", "brow_L", "brow_R"},
    }
    states = {}
    for name, show in expr.items():
        st = {key_ob.name: {"hide": key not in show} for key, key_ob in face.objs.items()}
        sc = {"alert": 1.25, "sad": 1.08}.get(name, 1.0)
        for sd, sg in (("L", 1), ("R", -1)):
            st[face.objs[f"eye_{sd}"].name]["basis"] = list_m(face.frame(sg * eye_dx, eye_z, 0.0, scale=(r_e * 0.85 * sc, 0.010 * k, r_e * 1.15 * sc)))
        states[name] = st

    for sd, sg in (("L", 1), ("R", -1)):
        anchor(rig, f"eye_{sd}", face.at(sg * eye_dx, eye_z), "head")
        anchor(rig, f"paw_F{sd}", P(sg * 0.075, -0.18, 0.0), f"fshin_{sd}")
        anchor(rig, f"paw_B{sd}", P(sg * 0.075, 0.19, 0.0), f"bshin_{sd}")
    mid = (face.at(eye_dx, eye_z) + face.at(-eye_dx, eye_z)) / 2
    anchor(rig, "gaze_target", mid + Vector((0, -1.0, 0)), "head")
    anchor(rig, "head_top", hc + Vector((0, 0, hr + 0.01)), "head")
    anchor(rig, "mouth", mouth_p, "head")
    anchor(rig, "back", P(0, 0.02, chest_z + 0.12), "spine")
    anchor(rig, "collar", P(0, -0.235, chest_z + 0.08), "neck")
    names = make_quadruped_poses(rig, S, kind, hip_z, chest_z)
    return rig, states, names


SB = {"cx": 0.0, "tail": (-0.9, -0.45, -0.05), "tail2": (-0.2, -1.0, -0.05), "neck": (-0.35, -0.85, -0.25), "hp": -30, "ht": 0,
      "bl": (0.09, 0.10, 0), "br": (-0.09, 0.14, 0), "bh": (0, -1, -0.3)}


def make_quadruped_poses(rig, S, kind, hip_z, chest_z):
    names = []
    LH = hip_z / 0.44

    def legs(front, back, fhint=(0, 0.6, 0.2), bhint=(0, -1, 0.1)):
        for sd in ("L", "R"):
            rig.ik2(f"fleg_{sd}", f"fshin_{sd}", Vector(front[sd]) * S, fhint)
            rig.ik2(f"bleg_{sd}", f"bshin_{sd}", Vector(back[sd]) * S, bhint)

    def body(hip_drop=0.0, chest_drop=0.0, head_pitch=0.0, head_turn=0.0, tail=(0, 0.6, 1.0), neck=(0, -0.5, 1.0), hip_back=0.0, chest_y=-0.16, chest_x=0.0,
             spine_scale=None):
        hb = rig.arm.pose.bones["hips"]
        hb.location = (0, -hip_drop * S * LH, -hip_back * S)
        if spine_scale:
            # v0.13: the trunk drawn shorter and rounder (a cat curled up asleep); the neck and front legs keep their size
            for b in ("neck", "fleg_L", "fleg_R"):
                rig.arm.data.bones[b].inherit_scale = "NONE"
            rig.arm.pose.bones["spine"].scale = tuple(spine_scale)
        upd()
        chest = Vector((chest_x * S, chest_y * S, (chest_z - chest_drop * LH) * S))
        rig.aim("spine", chest)
        rig.aim_dir("neck", neck)
        p = math.radians(head_pitch)
        rig.aim_dir("head", (0, math.sin(p), math.cos(p)), twist=math.radians(head_turn))
        rig.aim_dir("tail1", tail)
        rig.aim_dir("tail2", (tail[0], tail[1] * 0.6, tail[2] * 1.2))

    def paws(fy=-0.16, by=0.21, z=0.04):
        return ({"L": (0.075, fy, z), "R": (-0.075, fy, z)}, {"L": (0.075, by, z), "R": (-0.075, by, z)})

    def pose(name, fn):
        rig.reset()
        fn()
        rig.key_pose(name)
        names.append(name)

    def stand():
        body()
        legs(*paws())

    def walk():
        body(tail=(0, 0.5, 1.0))
        legs({"L": (0.075, -0.25, 0.06), "R": (-0.075, -0.08, 0.04)}, {"L": (0.075, 0.13, 0.04), "R": (-0.075, 0.29, 0.06)})

    def sit():
        # haunches down and forward under the body, chest up over straight front legs
        body(hip_drop=0.25, hip_back=-0.12, chest_drop=-0.03, tail=(0.15, 0.9, -0.35), neck=(0, -0.20, 1), head_pitch=6)
        legs({"L": (0.075, -0.165, 0.04), "R": (-0.075, -0.165, 0.04)}, {"L": (0.10, 0.00, 0.035), "R": (-0.10, 0.02, 0.035)},
             fhint=(0, 0.3, 0.1), bhint=(0, -1, 0.35))

    def sit_look_down():
        # sitting, head bent down as if looking at something held in front of the chest
        sit()
        rig.aim_dir("neck", (0, -0.45, 1))
        p = math.radians(-30)
        rig.aim_dir("head", (0, math.sin(p), math.cos(p)))

    def sit_up_hold():
        # sitting up on the haunches, front legs raised to hold something in front of the chest,
        # head bent down over it (a dog "reading" with its paws on the paper)
        body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.30, chest_y=0.0, tail=(0.35, 0.75, -0.55), neck=(0, -0.45, 1), head_pitch=-34)
        # v0.11: the tail curled forward along the ground beside the haunch (straight out behind, long and
        # thin, it read as a fox's or a kangaroo's)
        rig.aim_dir("tail2", (0.55, -0.80, -0.05))
        fz = chest_z * 0.72
        # v0.25: the paws at different heights, so both show on the paper in profile (level, one hid the other: "only one paw
        # clearly touches it", on the bench)
        legs({"L": (0.065, -0.25, fz + 0.055), "R": (-0.065, -0.25, fz - 0.055)}, {"L": (0.11, -0.17, 0.035), "R": (-0.11, -0.15, 0.035)},
             fhint=(0, 0.4, -1), bhint=(0, -0.3, 1))

    def sleep():
        # lying down, head resting on the front paws, tail curled along the side, eyes closed by expression
        body(hip_drop=0.32, chest_drop=0.33, tail=(0.9, -0.5, -0.1), neck=(0, -0.95, 0.05), head_pitch=-38, head_turn=8)
        legs({"L": (0.06, -0.40, 0.035), "R": (-0.06, -0.38, 0.035)}, {"L": (0.13, 0.12, 0.035), "R": (-0.12, 0.20, 0.035)},
             fhint=(0, 1, -0.4), bhint=(0, -1, -0.2))

    def sleep_curl():
        # v0.10: curled up asleep, the head turned back along the side and laid down by the front
        # paws, legs tucked under, the tail wrapped forward round the body (the sleeping cat lying
        # stretched out read as "crouched low")
        body(hip_drop=0.34, hip_back=-0.05, chest_drop=0.34, chest_y=-0.13, tail=(-0.95, -0.55, -0.05),
             neck=(-0.45, -0.60, -0.10), head_pitch=-30, head_turn=-35)
        legs({"L": (0.07, -0.24, 0.03), "R": (-0.07, -0.21, 0.03)}, {"L": (0.11, 0.03, 0.03), "R": (-0.11, 0.06, 0.03)},
             fhint=(0, 1, -0.5), bhint=(0, -1, -0.1))

    def sleep_ball():
        # v0.13: curled up in a ball to sleep, the front half swung round to one side so the body makes a
        # ring, the head laid on the back haunch, the paws tucked in, the tail wrapped round the front (lying
        # stretched out flat, a sleeping cat or dog "could also be read as collapsed", "unwell")
        body(hip_drop=0.33, hip_back=-0.08, chest_drop=0.35, chest_y=-0.08, chest_x=SB["cx"], tail=SB["tail"],
             neck=SB["neck"], head_pitch=SB["hp"], head_turn=SB["ht"])
        legs({"L": (0.05 + SB["cx"] * 0.5, -0.30, 0.025), "R": (-0.05 + SB["cx"] * 0.5, -0.28, 0.025)},
             {"L": (SB["bl"][0], SB["bl"][1], 0.025), "R": (SB["br"][0], SB["br"][1], 0.025)}, fhint=(0, 1, 0.2), bhint=SB["bh"])
        rig.aim_dir("tail2", SB["tail2"])

    def sleep_tuck():
        # v0.13 (cats): curled up asleep, the trunk drawn short and round, the legs tucked under, the head bowed
        # down onto the front paws and turned to the viewer, the tail laid along the side (the cat curled face-on
        # was too small to see; turned three-quarters with the trunk at full length it read as "stretched out on
        # its belly with its back legs extended behind it ... collapsed, injured or dead")
        body(hip_drop=0.33, hip_back=-0.08, chest_drop=0.36, chest_y=-0.08, neck=(-0.5, -0.7, -0.45), head_pitch=-30, head_turn=-45,
             tail=(-0.9, -0.45, -0.05), spine_scale=(1.25, 0.55, 1.0))
        legs({"L": (0.04, -0.18, 0.025), "R": (-0.06, -0.16, 0.025)}, {"L": (0.09, 0.04, 0.02), "R": (-0.09, 0.06, 0.02)},
             fhint=(0, 1, 0.2), bhint=(0, -1, -0.3))
        rig.aim_dir("tail2", (-0.1, -1, -0.05))

    def lie():
        body(hip_drop=0.31, chest_drop=0.30, tail=(0.5, 0.8, -0.15), neck=(0, -0.7, 0.6), head_pitch=-14)
        legs({"L": (0.08, -0.40, 0.035), "R": (-0.08, -0.37, 0.035)}, {"L": (0.11, 0.24, 0.035), "R": (-0.11, 0.25, 0.035)},
             fhint=(0, 1, -0.4), bhint=(0, -1, -0.3))

    def crouch():
        body(hip_drop=0.06, chest_drop=0.16, tail=(0, 1.0, 0.05), neck=(0, -1.0, 0.45), head_pitch=-4)
        legs({"L": (0.085, -0.22, 0.04), "R": (-0.085, -0.20, 0.04)}, {"L": (0.085, 0.24, 0.04), "R": (-0.085, 0.22, 0.04)},
             fhint=(0, 0.5, 0.5), bhint=(0, -1, 0.3))

    def stalk():
        # v0.8: stalking, belly almost on the ground, head low and level, eyes forward, tail straight
        # back and low; front paws reaching forward, back legs folded under (the old crouch read as
        # running)
        body(hip_drop=0.15, chest_drop=0.24, tail=(0, 1.0, -0.10), neck=(0, -1.0, 0.18), head_pitch=0)
        legs({"L": (0.085, -0.30, 0.035), "R": (-0.085, -0.25, 0.035)}, {"L": (0.09, 0.25, 0.035), "R": (-0.09, 0.27, 0.035)},
             fhint=(0, 0.7, 0.3), bhint=(0, -1, 0.6))

    def stalk_paw():
        # v0.13: stalking, frozen mid-step, one front paw lifted and bent, the hind legs bunched under ready to
        # spring, belly low, head low and level on the prey, the tail low (crawling on all four legs stretched
        # out, the stalking cat read as "creeping or running toward" the bird, "or just running past")
        # (v0.14: a lower crouch with the rump level with the shoulders, the hind legs folded under and the tail low was
        # read on the bench side by side with this one, three scenes each: it read as "running or creeping toward the
        # bird" twice, this one as "crouched low ... stalking" three times, so this one stays)
        body(hip_drop=0.10, chest_drop=0.22, tail=(0, 1.0, -0.12), neck=(0, -1.0, 0.10), head_pitch=0)
        rig.aim_dir("tail2", (0, 1.0, 0.2))
        legs({"L": (0.085, -0.27, 0.035), "R": (-0.085, -0.33, 0.17)}, {"L": (0.08, 0.15, 0.035), "R": (-0.08, 0.18, 0.035)},
             fhint=(0, 1, -0.6), bhint=(0, -1, 0.7))

    def graze():
        # v0.8: grazing, muzzle down in the grass (sniffing read as "about to butt" or "sniffing")
        body(chest_drop=0.08, neck=(0, -0.75, -0.65), head_pitch=-82, tail=(0, 0.5, 0.8))
        legs(*paws(fy=-0.15))

    def look_up():
        body(head_pitch=38, neck=(0, -0.35, 1), tail=(0, 0.5, 1.0))
        legs(*paws())

    def beg():
        # v0.9: begging, sitting square with the haunches and tail on the ground, the body leaning
        # less steeply, the head tipped right up toward the food (the upright sit read as rearing up,
        # standing and looking up as just watching)
        style = os.environ.get("TPDB_BEG", "A3")   # v0.23: A3 (bench A and A2: "sits up ... as if begging" in all four)
        if style == "A3":
            # as A2, the tail curled tight round the near haunch instead of laid out on the ground behind (laid out, the
            # sitting dog's "lower body stretches long and flat ... like a kangaroo")
            body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.30, chest_y=0.0, tail=(-0.55, 0.45, -0.70), neck=(0, -0.20, 1), head_pitch=38)
            rig.aim_dir("tail2", (-0.35, -0.90, -0.05))
            fz = chest_z * 0.62
            legs({"L": (0.065, -0.17, fz), "R": (-0.065, -0.17, fz)}, {"L": (0.10, -0.06, 0.035), "R": (-0.10, -0.04, 0.035)},
                 fhint=(0, -0.2, -1), bhint=(0, -1, 0.35))
            return
        if style == "A2":
            # v0.23 bench round 2: as A, with the hind legs folded under the haunches instead of stretched forward (A's hind
            # paws out in front read "as if kneeling", "legs stretched forward like a person")
            body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.30, chest_y=0.0, tail=(0.35, 0.75, -0.55), neck=(0, -0.20, 1), head_pitch=38)
            rig.aim_dir("tail2", (0.55, -0.80, -0.05))
            fz = chest_z * 0.62
            legs({"L": (0.065, -0.17, fz), "R": (-0.065, -0.17, fz)}, {"L": (0.10, -0.06, 0.035), "R": (-0.10, -0.04, 0.035)},
                 fhint=(0, -0.2, -1), bhint=(0, -1, 0.35))
            return
        if style == "A":
            # v0.23 bench A: sitting up on the haunches, both front paws lifted and folded at the chest, the tail curled
            # forward along the ground (the v0.9 slope, its tail stretched out behind, read "as if half-lying")
            body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.30, chest_y=0.0, tail=(0.35, 0.75, -0.55), neck=(0, -0.20, 1), head_pitch=38)
            rig.aim_dir("tail2", (0.55, -0.80, -0.05))
            fz = chest_z * 0.62
            legs({"L": (0.065, -0.17, fz), "R": (-0.065, -0.17, fz)}, {"L": (0.11, -0.17, 0.035), "R": (-0.11, -0.15, 0.035)},
                 fhint=(0, -0.2, -1), bhint=(0, -0.3, 1))
            return
        if style == "B":
            # v0.23 bench B: sitting square and upright as in sit(), the near front paw lifted toward the food, the head
            # tipped up, the tail curled forward beside the haunch
            body(hip_drop=0.25, hip_back=-0.12, chest_drop=-0.05, tail=(0.35, 0.75, -0.55), neck=(0, -0.22, 1), head_pitch=38)
            rig.aim_dir("tail2", (0.55, -0.80, -0.05))
            legs({"L": (0.075, -0.165, 0.04), "R": (-0.075, -0.24, chest_z * 0.45)}, {"L": (0.10, 0.00, 0.035), "R": (-0.10, 0.02, 0.035)},
                 fhint=(0, 0.3, 0.1), bhint=(0, -1, 0.35))
            return
        body(hip_drop=0.30, hip_back=-0.10, chest_drop=0.07, tail=(0.25, 0.95, -0.45), neck=(0, -0.30, 1), head_pitch=40)
        legs({"L": (0.075, -0.215, 0.04), "R": (-0.075, -0.215, 0.04)}, {"L": (0.10, 0.01, 0.035), "R": (-0.10, 0.03, 0.035)},
             fhint=(0, 0.3, 0.1), bhint=(0, -1, 0.35))

    def sniff():
        body(chest_drop=0.05, neck=(0, -1.0, -0.15), head_pitch=-70, tail=(0, 0.6, 0.8))
        legs(*paws(fy=-0.17))

    def play_bow():
        # v0.12: the hind legs apart, hocks bent, and the tail raised at a slant (both hind legs on one line
        # and a straight upright tail read as one stiff stick: "stretching or play-bowing")
        body(hip_drop=-0.02, chest_drop=0.24, neck=(0, -0.9, 0.55), head_pitch=12, tail=(0, 0.55, 0.85))
        legs({"L": (0.085, -0.38, 0.035), "R": (-0.085, -0.36, 0.035)}, {"L": (0.075, 0.13, 0.04), "R": (-0.075, 0.28, 0.04)},
             fhint=(0, 1, -0.5), bhint=(0, -1, 0.45))

    # v0.15: the poses that earlier releases replaced (lie, sleep, crouch, look_up, sit_look_down, stalk,
    # sleep_curl) are retired; no template asks for them, so they leave the cast and the gallery
    plan = [("stand", stand), ("walk", walk), ("sit", sit), ("sniff", sniff), ("play_bow", play_bow)]
    if kind == "dog":
        plan.append(("beg", beg))
        plan.append(("sit_up_hold", sit_up_hold))
    if kind == "cat":
        plan.append(("stalk_paw", stalk_paw))
    if kind == "dog":
        plan.append(("sleep_ball", sleep_ball))
    if kind == "cat":
        plan.append(("sleep_tuck", sleep_tuck))
    if os.environ.get("TPDB_EXP") and kind in ("cat", "dog"):
        # pose experiments for the isolation bench (never set in a release build)
        for i, d in enumerate(json.loads(os.environ["TPDB_EXP"])):
            def _exp(d=d):
                body(**d["body"])
                legs({"L": tuple(d["fL"]), "R": tuple(d["fR"])}, {"L": tuple(d["bL"]), "R": tuple(d["bR"])},
                     fhint=tuple(d.get("fh", (0, 1, 0.2))), bhint=tuple(d.get("bh", (0, -1, -0.3))))
                if d.get("tail2"):
                    rig.aim_dir("tail2", tuple(d["tail2"]))
            plan.append((f"exp{i}", _exp))
    if kind == "goat":
        plan = [p for p in plan if p[0] != "sit"]       # goats lie down rather than sit
        plan.append(("graze", graze))
    for nm, fn in plan:
        pose(nm, fn)
    rig.reset()
    return names


# ================================================================== birds
def build_bird(spec):
    kind = spec.get("kind", "songbird")
    S = spec.get("scale", 1.0)
    duck = kind == "duck"

    def P(x, y, z):
        return Vector((x * S, y * S, z * S))

    root = link(bpy.data.objects.new("ROOT", None))
    if duck:
        bz, hz, hy = 0.12, 0.27, -0.10
    else:
        bz, hz, hy = 0.10, 0.17, -0.045
    bones = {
        "body": (P(0, 0, bz - 0.04), P(0, 0, bz + 0.04), None),
        "neck": (P(0, hy * 0.5, bz + 0.03), P(0, hy, hz - 0.03), "body"),
        "head": (P(0, hy, hz - 0.03), P(0, hy, hz + 0.05), "neck"),
        "tail": (P(0, 0.05, bz + 0.01), P(0, 0.14, bz + 0.05), "body"),
    }
    for sd, sg in (("L", 1), ("R", -1)):
        bones[f"wing_{sd}"] = (P(sg * 0.045, -0.01, bz + 0.03), P(sg * 0.050, 0.07, bz + 0.02), "body")
        bones[f"leg_{sd}"] = (P(sg * 0.025, 0.0, bz - 0.04), P(sg * 0.025, 0.0, 0.005), "body")
    rig = Rig(root, bones)
    k = S
    col, bel, acc = spec["body"], spec.get("belly", spec["body"]), spec.get("accent", "yellow")
    if duck:
        ellipsoid("Body", P(0, 0.02, bz), (0.090 * k, 0.140 * k, 0.075 * k), col, rig, "body", rot=Quaternion((1, 0, 0), -0.15))
        ellipsoid("Neck", P(0, -0.07, bz + 0.08), (0.040 * k, 0.040 * k, 0.070 * k), col, rig, "neck")
        hr = 0.052 * k
    else:
        ellipsoid("Body", P(0, 0.012, bz), (0.055 * k, 0.078 * k, 0.052 * k), col, rig, "body", rot=Quaternion((1, 0, 0), -0.35))
        ellipsoid("Belly", P(0, -0.020, bz - 0.010), (0.044 * k, 0.045 * k, 0.040 * k), bel, rig, "body")
        hr = 0.043 * k
    hc = P(0, hy, hz)
    ellipsoid("Head", hc, (hr, hr, hr), col, rig, "head", seg=28, rings=16)
    tail_tip = P(0, 0.15, bz + (0.06 if not duck else 0.08))
    ob = cyl("Tail", P(0, 0.05, bz + 0.01), tail_tip, 0.028 * k, spec.get("tail_col", col), seg=4, r1=0.012 * k)
    rig.attach(ob, "tail")
    for sd, sg in (("L", 1), ("R", -1)):
        if duck:
            # a smaller wing set back and tilted up toward the tail, so the body still reads as a body
            ellipsoid(f"Wing_{sd}", P(sg * 0.074, 0.050, bz + 0.035), (0.018 * k, 0.070 * k, 0.030 * k), spec.get("wing_col", col), rig, f"wing_{sd}",
                      rot=Quaternion((1, 0, 0), -0.50))
        else:
            ellipsoid(f"Wing_{sd}", P(sg * 0.050, 0.025, bz + 0.02), (0.014 * k, 0.065 * k, 0.034 * k), spec.get("wing_col", col), rig, f"wing_{sd}",
                      rot=Quaternion((1, 0, 0), -0.3))
        lc = spec.get("leg_col", "orange")
        if duck:
            ob = cyl(f"Leg_{sd}", P(sg * 0.035, 0.0, bz - 0.05), P(sg * 0.035, -0.005, 0.012), 0.010 * k, lc)
            rig.attach(ob, f"leg_{sd}")
            ellipsoid(f"Foot_{sd}", P(sg * 0.035, -0.02, 0.008), (0.030 * k, 0.040 * k, 0.008 * k), lc, rig, f"leg_{sd}")
        else:
            ob = cyl(f"Leg_{sd}", P(sg * 0.022, 0.0, bz - 0.04), P(sg * 0.022, 0.0, 0.006), 0.0055 * k, lc)
            rig.attach(ob, f"leg_{sd}")
            for i, a in enumerate((-0.5, 0.0, 0.5)):
                d = Vector((math.sin(a) * 0.4, -math.cos(a), 0)) * 0.022 * k
                ob = cyl(f"Toe_{sd}{i}", P(sg * 0.022, 0.0, 0.004), P(sg * 0.022, 0.0, 0.004) + d, 0.004 * k, lc)
                rig.attach(ob, f"leg_{sd}")

    face = Face(rig, "head", hc, (hr, hr, hr), k * (0.30 if not duck else 0.36), prefix="F")
    fk = face.k
    eye_dx, eye_z = hr * 0.52, hr * 0.18
    # beak: upper and lower halves so "sing" can open it
    bl = 0.040 * k if not duck else 0.060 * k
    bw = 0.013 * k if not duck else 0.026 * k
    base = face.at(0, -hr * 0.05, -0.004 * k)
    up = ellipsoid("BeakUp", (0, 0, 0), (1, 1, 1), acc)
    lo = ellipsoid("BeakLo", (0, 0, 0), (1, 1, 1), acc)
    if duck:
        Mu = Matrix.LocRotScale(base + Vector((0, -bl * 0.55, 0.004 * k)), Quaternion(), Vector((bw, bl * 0.6, 0.010 * k)))
        Ml = Matrix.LocRotScale(base + Vector((0, -bl * 0.45, -0.008 * k)), Quaternion(), Vector((bw * 0.9, bl * 0.5, 0.008 * k)))
    else:
        Mu = Matrix.LocRotScale(base + Vector((0, -bl * 0.45, 0.003 * k)), Quaternion(), Vector((bw, bl * 0.55, 0.008 * k)))
        Ml = Matrix.LocRotScale(base + Vector((0, -bl * 0.35, -0.006 * k)), Quaternion(), Vector((bw * 0.85, bl * 0.42, 0.006 * k)))
    face.place("beak_up", up, Mu)
    face.place("beak_lo", lo, Ml)
    Ml_open = Matrix.Translation(base) @ Matrix.Rotation(math.radians(28), 4, "X") @ Matrix.Translation(-base) @ Ml
    r_e = hr * 0.20
    for sd, sg in (("L", 1), ("R", -1)):
        x = sg * eye_dx
        face.place(f"eye_{sd}", ellipsoid("eye", (0, 0, 0), (1, 1, 1), "outline"), face.frame(x, eye_z, 0.0, scale=(r_e * 0.85, r_e * 0.5, r_e * 1.1)))
        face.place(f"catch_{sd}", ellipsoid("catch", (0, 0, 0), (1, 1, 1), "cream"), face.frame(x + r_e * 0.3 * sg, eye_z + r_e * 0.45, r_e * 0.35, scale=(r_e * 0.28, r_e * 0.2, r_e * 0.34)))
        w = r_e * 1.1
        face.curve_on(f"arcdn_{sd}", [(x - w, eye_z + r_e * 0.1), (x, eye_z - r_e * 0.5), (x + w, eye_z + r_e * 0.1)], r_e * 0.22, "outline", r_e * 0.15)

    expr = {"neutral": ({"eye_L", "eye_R", "catch_L", "catch_R", "beak_up", "beak_lo"}, False),
            "sing": ({"eye_L", "eye_R", "catch_L", "catch_R", "beak_up", "beak_lo"}, True),
            "sleepy": ({"arcdn_L", "arcdn_R", "beak_up", "beak_lo"}, False)}
    states = {}
    for name, (show, opened) in expr.items():
        st = {ob.name: {"hide": key not in show} for key, ob in face.objs.items()}
        st[face.objs["beak_lo"].name]["basis"] = list_m(Ml_open if opened else Ml)
        states[name] = st

    for sd, sg in (("L", 1), ("R", -1)):
        anchor(rig, f"eye_{sd}", face.at(sg * eye_dx, eye_z), "head")
        anchor(rig, f"foot_{sd}", P(sg * 0.025, 0.0, 0.0), f"leg_{sd}")
    mid = (face.at(eye_dx, eye_z) + face.at(-eye_dx, eye_z)) / 2
    anchor(rig, "gaze_target", mid + Vector((0, -1.0, 0)), "head")
    anchor(rig, "head_top", hc + Vector((0, 0, hr + 0.005 * k)), "head")
    anchor(rig, "mouth", base + Vector((0, -bl, 0)), "head")
    names = make_bird_poses(rig, S, duck, bz)
    return rig, states, names


def make_bird_poses(rig, S, duck, bz):
    names = []

    def pose(name, fn):
        rig.reset()
        fn()
        rig.key_pose(name)
        names.append(name)

    def perch():
        pass

    def peck():
        pb = rig.arm.pose.bones["body"]
        upd()
        M = pb.matrix.copy()
        h = Vector((0, 0, 0.004 * S))
        pb.matrix = Matrix.Translation(h) @ Matrix.Rotation(math.radians(28), 4, "X") @ Matrix.Translation(-h) @ M
        upd()
        rig.aim_dir("neck", (0, -0.9, -0.5))
        rig.aim_dir("head", (0, -0.7, -0.6))
        for sd in ("L", "R"):
            rig.aim_dir(f"leg_{sd}", (0, 0.05, -1))

    def fly():
        # wings raised and lengthened, legs tucked back, tail streaming
        rig.arm.pose.bones["body"].location = (0, 0.05 * S, 0)
        upd()
        for sd, sg in (("L", 1), ("R", -1)):
            rig.aim_dir(f"wing_{sd}", (sg * 0.45, 0.30, 1.0))
            rig.arm.pose.bones[f"wing_{sd}"].scale = (1.0, 1.9, 1.35)
            rig.aim_dir(f"leg_{sd}", (0, 1, -0.15))
        rig.aim_dir("tail", (0, 1, 0.1))
        upd()

    def sing():
        rig.aim_dir("neck", (0, -0.25, 1))
        rig.aim_dir("head", (0, -0.3, 1))

    def swim():
        # lower the body so the waterline sits at the root origin; tuck the legs
        rig.arm.pose.bones["body"].location = (0, -(bz - 0.075) * S, 0)
        upd()
        for sd in ("L", "R"):
            rig.aim_dir(f"leg_{sd}", (0, 1, 0.2))

    plan = [("perch", perch), ("peck", peck), ("fly", fly), ("sing", sing)]
    if duck:
        plan.append(("swim", swim))
    for nm, fn in plan:
        pose(nm, fn)
    rig.reset()
    return names
