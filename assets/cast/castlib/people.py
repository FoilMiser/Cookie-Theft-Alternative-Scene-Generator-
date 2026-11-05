"""People: skeleton, body, wardrobe, hair, hats, facial hair, face and anchors."""
import math
import random

import bpy  # noqa: F401
import bmesh
from mathutils import Quaternion, Vector

from .core import Rig, anchor, cyl, ellipsoid, link, mat, skin_like, skin_object, tube, tube_mesh, upd, _mesh_object
from .face import Face, build_people_face, people_expression_states

# v0.23 (TPDB_HEAD; the release builds with B): the older man's fringe of hair kept to the back, and a fuller nose
HEAD_STYLE = __import__("os").environ.get("TPDB_HEAD", "B")   # v0.23: B (bench: both readers had him walking the right way)


def person_skeleton(kind):
    if kind == "child":
        return dict(ankle=0.05, knee=0.26, hip=0.48, pelvis=0.53, chest=0.71, neck=0.79, head_base=0.82,
                    head_c=0.950, head_r=0.140, sh_x=0.115, sh_z=0.765, el_z=0.615, wr_z=0.485, hand_len=0.055,
                    hip_x=0.065, toe=0.09, s=0.66)
    if __import__("os").environ.get("TPDB_BODY", "B") == "B":
        # v0.27, chosen on the bench: legs an eighth shorter, the rest of the figure lowered with them, the shin kept so a sitter's feet still reach the ground ("very long, thin legs and a small
        # torso", "long and thin relative to" the rest, on nearly every cut-out)
        L_ = 0.10
        return dict(ankle=0.07, knee=0.44, hip=0.84 - L_, pelvis=0.90 - L_, chest=1.16 - L_, neck=1.30 - L_, head_base=1.34 - L_,
                    head_c=1.485 - L_, head_r=0.158, sh_x=0.175, sh_z=1.245 - L_, el_z=1.005 - L_, wr_z=0.785 - L_, hand_len=0.075,
                    hip_x=0.09, toe=0.13, s=1.0)
    return dict(ankle=0.07, knee=0.45, hip=0.84, pelvis=0.90, chest=1.16, neck=1.30, head_base=1.34,
                head_c=1.485, head_r=0.158, sh_x=0.175, sh_z=1.245, el_z=1.005, wr_z=0.785, hand_len=0.075,
                hip_x=0.09, toe=0.13, s=1.0)


class PersonCtx:
    """Everything the action builder needs to know about a built person."""


def surface_points(obj):
    upd()
    dg = bpy.context.evaluated_depsgraph_get()
    oe = obj.evaluated_get(dg)
    me = oe.to_mesh()
    pts = [oe.matrix_world @ vv.co for vv in me.vertices]
    oe.to_mesh_clear()
    return pts


def front_y(pts, z, x=0.0, tol=0.02):
    near = [q for q in pts if abs(q.z - z) < tol and abs(q.x - x) < tol * 2]
    return min(q.y for q in near) if near else min(q.y for q in pts)


TORSO = {"hips", "spine", "chest", "neck"}


def build_person(spec):
    kind = "child" if spec["age"] in ("child",) else "adult"
    J = person_skeleton(kind)
    S = spec.get("scale", 1.0)
    s = J["s"]
    HS = spec.get("head_scale", 1.0)

    def P(x, y, z):
        return Vector((x * S, y * S, z * S))

    root = link(bpy.data.objects.new("ROOT", None))
    sx, hx = J["sh_x"], J["hip_x"]
    bones = {
        "hips": (P(0, 0, J["pelvis"]), P(0, 0, J["pelvis"] + 0.08 * s), None),
        "spine": (P(0, 0, J["pelvis"]), P(0, 0, J["chest"]), "hips"),
        "chest": (P(0, 0, J["chest"]), P(0, 0, J["neck"]), "spine"),
        "neck": (P(0, 0, J["neck"]), P(0, 0, J["head_base"]), "chest"),
        "head": (P(0, 0, J["head_base"]), P(0, 0, J["head_base"] + 0.30 * s), "neck"),
    }
    for side, sg in (("L", 1), ("R", -1)):
        bones.update({
            f"upper_arm_{side}": (P(sg * sx, 0, J["sh_z"]), P(sg * (sx + 0.015 * s), 0, J["el_z"]), "chest"),
            f"forearm_{side}": (P(sg * (sx + 0.015 * s), 0, J["el_z"]), P(sg * (sx + 0.025 * s), 0, J["wr_z"]), f"upper_arm_{side}"),
            f"hand_{side}": (P(sg * (sx + 0.025 * s), 0, J["wr_z"]), P(sg * (sx + 0.028 * s), 0, J["wr_z"] - J["hand_len"]), f"forearm_{side}"),
            f"thigh_{side}": (P(sg * hx, 0, J["hip"]), P(sg * hx, -0.01 * s, J["knee"]), "hips"),
            f"shin_{side}": (P(sg * hx, -0.01 * s, J["knee"]), P(sg * hx, 0, J["ankle"]), f"thigh_{side}"),
            f"foot_{side}": (P(sg * hx, 0, J["ankle"]), P(sg * hx, -J["toe"], 0.02 * s), f"shin_{side}"),
        })
    rig = Rig(root, bones)

    hr = J["head_r"] * S * HS
    hc = P(0, 0, J["head_c"]) + Vector((0, 0, (HS - 1) * J["head_r"] * S * 0.6))
    HR = (hr * 1.04, hr * 0.98, hr * 0.96)
    sh = {sd: P(sg * sx, 0, J["sh_z"]) for sd, sg in (("L", 1), ("R", -1))}
    el = {sd: P(sg * (sx + 0.015 * s), 0, J["el_z"]) for sd, sg in (("L", 1), ("R", -1))}
    wr = {sd: P(sg * (sx + 0.025 * s), 0, J["wr_z"]) for sd, sg in (("L", 1), ("R", -1))}
    k = S * s if kind == "child" else S
    kh = k * HS

    B = dict(chest=1.0, waist=1.0, hips=1.0, depth=1.0, belly=0.0, limbs=1.0)
    B.update(spec.get("build", {}))
    if __import__("os").environ.get("TPDB_BODY", "B") == "B":
        B["limbs"] *= 1.14
    if __import__("os").environ.get("TPDB_BODY", "B") == "A":
        # v0.26 bench: fuller from the side (nearly every cut-out of the first round: "the torso is extremely thin from the side", "very long,
        # thin legs"). Tried and left: the readers' words did not move (isolation_v026.md)
        B["depth"] *= 1.22
        B["limbs"] *= 1.12
    pel, ch, nk = J["pelvis"], J["chest"], J["neck"]
    top, bottom = spec.get("top", "tee"), spec.get("bottom", "pants")
    long_sleeve = top in ("long", "hoodie", "cardigan") or spec.get("sleeves") == "long"
    top_col = spec["shirt"]
    dp = B["depth"]
    LB = B["limbs"]
    TI = 1.12

    # --- torso (shirt / dress top / cardigan / hoodie) ----------------------
    verts = [P(0, 0, pel + 0.035 * s), P(0, 0, pel + 0.13 * s), P(0, 0, ch - 0.01 * s), P(0, 0, nk - 0.020 * s)]
    radii = [(0.142 * k * B["waist"] * 1.05 * TI, 0.108 * k * dp * TI), (0.132 * k * B["waist"] * TI, 0.104 * k * dp * TI),
             (0.160 * k * B["chest"] * TI, 0.116 * k * dp * TI), (0.128 * k * B["chest"] * TI, 0.086 * k * dp * TI)]
    # the hem follows the hips so a forward lean bends the shirt at the waist instead of lifting it off the pants
    wts = [{"hips": 0.85, "spine": 0.15}, {"spine": 0.70, "hips": 0.30}, {"spine": 0.4, "chest": 0.6}, {"chest": 1.0}]
    edges = [(0, 1), (1, 2), (2, 3)]
    if B["belly"] > 0:
        i0 = len(verts)
        verts.append(P(0, -0.060 * s * B["belly"], pel + 0.12 * s))
        radii.append((0.128 * k * B["waist"], 0.100 * k * dp))
        wts.append({"spine": 0.8, "hips": 0.2})
        edges.append((1, i0))
    for sd, sg in (("L", 1), ("R", -1)):
        i0 = len(verts)
        shp = sh[sd] + Vector((-sg * 0.006 * k, 0, 0.004 * k))
        verts.append(shp); radii.append(0.060 * k * LB); wts.append({"chest": 0.45, f"upper_arm_{sd}": 0.55})
        edges.append((3, i0))
        if long_sleeve:
            verts += [el[sd], wr[sd] + (el[sd] - wr[sd]) * 0.08]
            radii += [0.052 * k * LB, 0.047 * k * LB]
            wts += [{f"upper_arm_{sd}": 0.5, f"forearm_{sd}": 0.5}, {f"forearm_{sd}": 1.0}]
            edges += [(i0, i0 + 1), (i0 + 1, i0 + 2)]
        else:
            verts.append(sh[sd].lerp(el[sd], 0.50)); radii.append(0.057 * k * LB); wts.append({f"upper_arm_{sd}": 1.0})
            edges.append((i0, i0 + 1))
    shirt = skin_object("Shirt", verts, edges, radii, top_col, rig, wts)

    if top == "vest":
        # a sleeveless layer over the shirt: wider than the shirt everywhere below the shoulders,
        # open down the front (a strip of shirt shows through) so it reads as a vest, not a bib
        vv = [P(0, 0, pel + 0.040 * s), P(0, 0, pel + 0.13 * s), P(0, 0, ch - 0.01 * s), P(0, 0, nk - 0.016 * s)]
        # v0.31 bench (isolation_v031.md): "B" wider than the shirt by enough that the shirt cannot come through (it did, and drew "a jagged edge against the white shirt"); "C" wider still
        vest31 = __import__("os").environ.get("TPDB_VEST", "B") if spec.get("vest_style") != "hivis" else "O"
        vk31 = {"O": (1.075, 1.10), "B": (1.12, 1.20), "C": (1.16, 1.28)}[vest31]
        vr = [(r[0] * vk31[0], r[1] * vk31[1]) for r in radii[:4]]
        vr[3] = (radii[3][0] * 1.16, radii[3][1] * 1.14) if vest31 == "O" else (radii[3][0] * 1.18, radii[3][1] * vk31[1])
        vw = wts[:4]
        ve = [(0, 1), (1, 2), (2, 3)]
        if B["belly"] > 0:
            vv.append(verts[4]); vr.append((radii[4][0] * (1.07 if vest31 == "O" else vk31[0]), radii[4][1] * vk31[1])); vw.append(wts[4])
            ve.append((1, len(vv) - 1))
        # shoulder straps: the vest runs over the top of each shoulder, so it reads as a garment and
        # not as a tube around the chest
        for sd, sg in (("L", 1), ("R", -1)):
            vv.append(sh[sd] + Vector((-sg * 0.030 * k, 0, 0.010 * k)))
            vr.append(0.066 * k * LB)
            vw.append({"chest": 0.55, f"upper_arm_{sd}": 0.45})
            ve.append((3, len(vv) - 1))
        vest = skin_object("Vest", vv, ve, vr, spec["vest"], rig, vw)
        vest_pts = surface_points(vest)
        z0, z1 = (pel + 0.05 * s) * S, (nk - 0.03 * s) * S
        if spec.get("vest_style") == "hivis":
            # safety vest: two flat silver stripes hugging the vest (ribbons, not ropes)
            for i, zf in enumerate((0.26, 0.62)):
                zb = z0 + (z1 - z0) * zf
                hh = 0.020 * k
                bm = bmesh.new()
                rows = []
                for zz in (zb - hh, zb + hh):
                    ring_pts = [q for q in vest_pts if abs(q.z - zz) < 0.012 * S] or vest_pts
                    row = []
                    for j in range(64):
                        a = j / 64 * 2 * math.pi
                        dirv = Vector((math.cos(a), math.sin(a), 0))
                        rad = max((q.x * dirv.x + q.y * dirv.y for q in ring_pts if (q.x * dirv.x + q.y * dirv.y) > 0 and
                                   abs(q.x * dirv.y - q.y * dirv.x) < 0.02 * k), default=0.15 * k)
                        row.append(bm.verts.new(Vector((dirv.x * (rad + 0.004 * k), dirv.y * (rad + 0.004 * k), zz))))
                    rows.append(row)
                for j in range(64):
                    a0, a1 = rows[0][j], rows[0][(j + 1) % 64]
                    b0, b1 = rows[1][j], rows[1][(j + 1) % 64]
                    bm.faces.new((a0, a1, b1, b0))
                bmesh.ops.solidify(bm, geom=bm.faces[:], thickness=0.003 * k)
                band = _mesh_object(f"VestBand{i}", bm, "silver", smooth=True)
                upd()
                skin_like(band, vest, rig, TORSO)
        else:
            pts = []
            for i in range(9):
                z = z0 + (z1 - z0) * i / 8
                pts.append(Vector((0, front_y(vest_pts, z, 0.0, 0.03 * k) - 0.001 * k, z)))
            strip = tube_mesh("VestOpening", pts, 0.022 * k, spec["shirt"])
            skin_like(strip, vest, rig, TORSO)
            for i in range(3):
                z = z0 + (z1 - z0) * (0.18 + 0.22 * i)
                skin_like(ellipsoid(f"VestButton{i}", (0.030 * k, front_y(vest_pts, z, 0.030 * k, 0.03 * k) - 0.004 * k, z), (0.008 * k, 0.004 * k, 0.008 * k), "outline", rig, "spine"), vest, rig, TORSO)
    torso_pts = surface_points(shirt)
    if top == "cardigan":
        z0, z1 = (pel + 0.06 * s) * S, (nk - 0.04 * s) * S
        pts = []
        for i in range(9):
            z = z0 + (z1 - z0) * i / 8
            pts.append(Vector((0, front_y(torso_pts, z, 0.0, 0.03 * k) - 0.002 * k, z)))
        strip = tube_mesh("Placket", pts, 0.017 * k, spec.get("inner", "cream"))
        skin_like(strip, shirt, rig, TORSO)
        for i in range(3):
            z = z0 + (z1 - z0) * (0.25 + 0.25 * i)
            skin_like(ellipsoid(f"Button{i}", (0.026 * k, front_y(torso_pts, z, 0.026 * k, 0.03 * k) - 0.004 * k, z), (0.008 * k, 0.004 * k, 0.008 * k), "outline", rig, "spine"), shirt, rig, TORSO)
    if top == "hoodie":
        skin_like(ellipsoid("Hood", P(0, 0.075 * s, nk - 0.005 * s), (0.125 * k, 0.065 * k, 0.075 * k), top_col, rig, "chest"), shirt, rig, TORSO)
        for sg in (1, -1):
            zt = (nk - 0.03 * s) * S
            x = sg * 0.030 * k
            pts = [Vector((x, front_y(torso_pts, zt - d * 0.12 * k, x, 0.03 * k) - 0.004 * k, zt - d * 0.12 * k)) for d in (0, 0.5, 1)]
            tube_and = tube_mesh(f"String{'L' if sg > 0 else 'R'}", pts, 0.006 * k, "cream")
            skin_like(tube_and, shirt, rig, TORSO)
        zp = (pel + 0.11 * s) * S
        pk = skin_like(ellipsoid("Pocket", (0, front_y(torso_pts, zp, 0, 0.03 * k) + 0.012 * k, zp), (0.085 * k, 0.020 * k, 0.045 * k), top_col, rig, "spine"), shirt, rig, TORSO)

    # --- bottoms ----------------------------------------------------------
    bare_legs = bottom in ("shorts", "skirt", "dress")
    bcol = top_col if bottom == "dress" else spec["pants"]
    if bottom in ("pants", "shorts"):
        # the waistband runs well up inside the shirt (narrower than it) so leaning never opens a gap
        verts = [P(0, 0, pel + 0.115 * s), P(0, 0, pel + 0.045 * s), P(0, 0, pel - 0.010 * s), P(0, 0.006 * s, pel - 0.070 * s)]
        radii = [(0.118 * k * B["waist"] * TI, 0.090 * k * dp * TI), (0.136 * k * B["waist"] * TI, 0.104 * k * dp * TI),
                 (0.150 * k * B["hips"] * TI, 0.114 * k * dp * TI), (0.136 * k * B["hips"] * TI, 0.104 * k * dp * TI)]
        wts = [{"hips": 0.6, "spine": 0.4}, {"hips": 0.92, "spine": 0.08}, {"hips": 1.0}, {"hips": 1.0}]
        edges = [(0, 1), (1, 2), (2, 3)]
        for sd, sg in (("L", 1), ("R", -1)):
            i0 = len(verts)
            if bottom == "pants":
                verts += [P(sg * hx, 0, J["hip"] - 0.03 * s), P(sg * hx, -0.01 * s, J["knee"]), P(sg * hx, 0, J["ankle"] + 0.005 * s)]
                radii += [0.080 * k * B["hips"], 0.064 * k * LB, 0.055 * k * LB]
                wts += [{"hips": 0.35, f"thigh_{sd}": 0.65}, {f"thigh_{sd}": 0.5, f"shin_{sd}": 0.5}, {f"shin_{sd}": 1.0}]
                edges += [(3, i0), (i0, i0 + 1), (i0 + 1, i0 + 2)]
            else:
                verts += [P(sg * hx, 0, J["hip"] - 0.03 * s), P(sg * hx, -0.006 * s, J["knee"] + 0.10 * s)]
                radii += [0.082 * k * B["hips"], 0.074 * k * LB]
                wts += [{"hips": 0.35, f"thigh_{sd}": 0.65}, {f"thigh_{sd}": 1.0}]
                edges += [(3, i0), (i0, i0 + 1)]
        pants_ob = skin_object("Pants", verts, edges, radii, bcol, rig, wts)
    else:
        hem_z = J["knee"] + (0.05 if bottom == "skirt" else 0.03) * s
        verts = [P(0, 0, pel + 0.055 * s), P(0, 0, pel - 0.020 * s), P(0, 0.004 * s, hem_z)]
        radii = [(0.136 * k * B["waist"] * TI, 0.104 * k * dp * TI), (0.158 * k * B["hips"] * TI, 0.122 * k * dp * TI),
                 (0.205 * k * B["hips"], 0.165 * k * dp)]
        wts = [{"hips": 0.8, "spine": 0.2}, {"hips": 1.0}, {"hips": 0.4, "thigh_L": 0.3, "thigh_R": 0.3}]
        pants_ob = skin_object("Skirt", verts, [(0, 1), (1, 2)], radii, bcol, rig, wts)
        # v0.15: the fabric over each thigh. The bell above hangs from the hips and cannot follow two legs, so
        # when a thigh swung forward (sitting, kicking, sliding) the leg below it came out of nowhere, a gap
        # between the hem and a floating leg. Each lobe runs from the hip joint past the top of the bare leg
        # and turns with its thigh; standing, both lie inside the bell, so the skirt looks as it did.
        lv, lr, lw, le = [], [], [], []
        f = 0.80
        for sd, sg in (("L", 1), ("R", -1)):
            i0 = len(lv)
            lx = sg * hx * 0.8      # a little inside the leg, so standing it stays clear of the hem's rounded edge
            # three nodes (two made a box that the smoothing shrank to a short blob), flatter front to back and tapering to
            # a thin end that overlaps the top of the bare leg; the lower nodes a little to the front, so a leg swung back
            # in a stride barely lifts the back of the skirt
            lv += [P(lx, 0, J["hip"]), P(lx, -0.012 * s, J["hip"] + (J["knee"] - J["hip"]) * f * 0.5),
                   P(lx, -0.020 * s, J["hip"] + (J["knee"] - J["hip"]) * f)]
            lr += [(0.080 * k * B["hips"], 0.064 * k * B["hips"]), (0.072 * k * B["hips"], 0.058 * k * B["hips"]),
                   (0.048 * k * B["hips"], 0.044 * k * B["hips"])]
            lw += [{f"thigh_{sd}": 0.7, "hips": 0.3}, {f"thigh_{sd}": 1.0}, {f"thigh_{sd}": 1.0}]
            le += [(i0, i0 + 1), (i0 + 1, i0 + 2)]
        lap = skin_object("SkirtLap", lv, le, lr, bcol, rig, lw)
        # no line where a lobe passes into the bell: in a stride the lobe's crossing drew an outlined patch on the skirt
        # ("a pocket, a fold, or a stain"); where it shows, it is the same cloth, bulging with the leg
        try:
            lap.lineart.usage = "NO_INTERSECTION"
        except AttributeError:
            pass
    if bare_legs:
        verts, radii, wts, edges = [], [], [], []
        for sd, sg in (("L", 1), ("R", -1)):
            i0 = len(verts)
            # v0.15: every bare leg runs down to the ankle joint, inside the shoe, so the foot never stands
            # apart from it
            top_z = J["knee"] + (0.14 if bottom == "shorts" else 0.10) * s
            verts += [P(sg * hx, -0.006 * s, top_z), P(sg * hx, -0.01 * s, J["knee"]), P(sg * hx, 0, J["ankle"])]
            radii += [0.060 * k * LB, 0.050 * k * LB, 0.041 * k * LB]
            wts += [{f"thigh_{sd}": 1.0}, {f"thigh_{sd}": 0.5, f"shin_{sd}": 0.5}, {f"shin_{sd}": 1.0}]
            edges += [(i0, i0 + 1), (i0 + 1, i0 + 2)]
        skin_object("Legs", verts, edges, radii, spec["skin"], rig, wts)

    if __import__("os").environ.get("TPDB_DRESS", "B") == "B" and bottom == "dress":
        # v0.27, chosen on the bench: a belt at the join (the top and the bell drawn as two lobes: "two pieces with a visible join or drawing seam at the waist")
        spec = dict(spec, belt="wood", buckle="sun")
        pants_ob = shirt
    if spec.get("belt") and bottom in ("pants", "shorts", "dress") and (bottom != "dress" or __import__("os").environ.get("TPDB_DRESS", "B") == "B"):
        zb = (pel + (0.024 if bottom != "dress" else 0.050) * s) * S
        ring_pts = surface_points(pants_ob)
        band = [q for q in ring_pts if abs(q.z - zb) < 0.012 * S] or ring_pts
        bw = max(abs(q.x) for q in band) + 0.004 * k
        bd = max(abs(q.y) for q in band) + 0.004 * k
        ring = [Vector((bw * math.cos(a), bd * math.sin(a), zb)) for a in [i / 64 * 2 * math.pi for i in range(64)]]
        cu = tube("Belt", [tuple(r) for r in ring], 0.012 * k, spec["belt"], None, None)
        cu.data.splines[0].use_cyclic_u = True
        cu.data.bevel_depth = 0.011 * k
        upd()
        rig.attach(cu, "hips")
        ellipsoid("Buckle", Vector((0, -bd - 0.010 * k, zb)), (0.020 * k, 0.008 * k, 0.016 * k), spec.get("buckle", "sun"), rig, "hips")

    # --- skin: neck + forearms (+ upper arms for sleeveless) ---------------
    verts = [P(0, 0, nk - 0.05 * s), P(0, 0, J["head_base"] + 0.03 * s)]
    neck_r = (0.060 if kind == "child" else 0.054) * (1.0 + 0.5 * (HS - 1))
    radii = [neck_r * k * 1.1, neck_r * k]
    wts = [{"chest": 1.0}, {"neck": 0.5, "head": 0.5}]
    edges = [(0, 1)]
    if not long_sleeve:
        for sd in ("L", "R"):
            i0 = len(verts)
            start = sh[sd].lerp(el[sd], 0.38)
            verts += [start, el[sd], wr[sd]]
            radii += [0.046 * k * LB, 0.043 * k * LB, 0.037 * k * LB]
            wts += [{f"upper_arm_{sd}": 1.0}, {f"upper_arm_{sd}": 0.5, f"forearm_{sd}": 0.5}, {f"forearm_{sd}": 1.0}]
            edges += [(i0, i0 + 1), (i0 + 1, i0 + 2)]
    else:
        for sd in ("L", "R"):
            i0 = len(verts)
            verts += [wr[sd] + (el[sd] - wr[sd]) * 0.12, wr[sd]]
            radii += [0.040 * k * LB, 0.037 * k * LB]
            wts += [{f"forearm_{sd}": 1.0}, {f"forearm_{sd}": 1.0}]
            edges += [(i0, i0 + 1)]
    skin_object("Skin", verts, edges, radii, spec["skin"], rig, wts)

    for sd, sg in (("L", 1), ("R", -1)):
        hcen = wr[sd] + Vector((0.002 * sg, 0, -0.042 * k))
        ellipsoid(f"Hand_{sd}", hcen, (0.040 * k, 0.034 * k, 0.050 * k), spec["skin"], rig, f"hand_{sd}")
        ellipsoid(f"Thumb_{sd}", hcen + Vector((-sg * 0.012 * k, -0.030 * k, 0.012 * k)), (0.015 * k, 0.016 * k, 0.026 * k),
                  spec["skin"], rig, f"hand_{sd}", rot=Quaternion((1, 0, 0), 0.5))
        ellipsoid(f"Heel_{sd}", P(sg * hx, 0.010 * s, 0.040 * s), (0.050 * k, 0.060 * k, 0.040 * k), spec["shoes"], rig, f"foot_{sd}")
        ellipsoid(f"Toe_{sd}", P(sg * hx, -0.062 * s, 0.034 * s), (0.058 * k, 0.080 * k, 0.036 * k), spec["shoes"], rig, f"foot_{sd}")

    # --- head --------------------------------------------------------------
    ellipsoid("Head", hc, HR, spec["skin"], rig, "head", seg=40, rings=22)
    for sd, sg in (("L", 1), ("R", -1)):
        ellipsoid(f"Ear_{sd}", hc + Vector((sg * HR[0] * 0.97, 0.005, -0.012 * kh)), (0.016 * kh, 0.026 * kh, 0.034 * kh), spec["skin"], rig, "head")
    face = Face(rig, "head", hc, HR, kh)
    eye_dx, eye_z = 0.060 * kh, 0.010 * kh
    if HEAD_STYLE == "B" and spec.get("hair") == "bald_ring":
        # v0.23 bench B: a fuller nose standing out from the face, so a profile shows which way the face is turned
        ellipsoid("Nose", face.at(0, eye_z - 0.044 * kh, 0.010 * kh), (0.026 * kh, 0.030 * kh, 0.022 * kh), spec["skin"], rig, "head")
    else:
        ellipsoid("Nose", face.at(0, eye_z - 0.040 * kh, -0.004 * kh), (0.020 * kh, 0.018 * kh, 0.016 * kh), spec["skin"], rig, "head")
    build_hair(spec, rig, hc, HR, kh)
    build_facial_hair(spec, rig, face, eye_z, kh)
    build_hat(spec, rig, hc, HR, kh)
    if spec.get("backpack"):
        # v0.24 bench (TPDB_TEEN=B): a school backpack on the chest bone, with a pocket and two straps over the shoulders
        bz = (J["chest"] - 0.02) * S
        ellipsoid("Backpack", Vector((0, 0.185 * S, bz)), (0.125 * S, 0.075 * S, 0.175 * S), spec["backpack"], rig, "chest")
        ellipsoid("BackpackPocket", Vector((0, 0.255 * S, bz - 0.05 * S)), (0.085 * S, 0.028 * S, 0.075 * S), spec.get("backpack2", "charcoal"), rig, "chest")
        for sd, sg in (("L", 1), ("R", -1)):
            _blob_chain(f"BackpackStrap_{sd}", [Vector((sg * 0.10 * S, 0.13 * S, (J["sh_z"] + 0.02) * S)), Vector((sg * 0.105 * S, 0.0, (J["sh_z"] + 0.088) * S)),
                                                Vector((sg * 0.11 * S, -0.135 * S, J["sh_z"] * S)), Vector((sg * 0.125 * S, -0.150 * S, (J["chest"] - 0.06) * S)),
                                                Vector((sg * 0.165 * S, -0.065 * S, (J["chest"] - 0.14) * S))],
                        [(0.026 * S, 0.010 * S)] * 5, spec.get("backpack2", "charcoal"), rig, bone="chest")
    build_people_face(face, eye_dx, eye_z, kh, glasses=spec.get("glasses", False))

    for sd, sg in (("L", 1), ("R", -1)):
        anchor(rig, f"hand_{sd}_grip", wr[sd] + Vector((0.004 * sg, -0.005, -0.045 * k)), f"hand_{sd}")
        anchor(rig, f"foot_{sd}", P(sg * hx, -0.045 * s, 0.0), f"foot_{sd}")
        anchor(rig, f"eye_{sd}", face.at(sg * eye_dx, eye_z), "head")
    mid = (face.at(eye_dx, eye_z) + face.at(-eye_dx, eye_z)) / 2
    anchor(rig, "gaze_target", mid + Vector((0, -1.0, 0)), "head")
    anchor(rig, "head_top", hc + Vector((0, 0, HR[2] + 0.02 * kh)), "head")
    anchor(rig, "seat", P(0, 0.02 * s, J["pelvis"] - 0.10 * s), "hips")
    anchor(rig, "mouth", face.at(0, eye_z - 0.080 * kh), "head")
    anchor(rig, "chest", P(0, -0.12 * s, J["chest"]), "spine")
    states = people_expression_states(face, eye_dx, eye_z, kh)

    ctx = PersonCtx()
    ctx.J, ctx.S, ctx.s, ctx.k, ctx.kh, ctx.HS = J, S, s, k, kh, HS
    ctx.hc, ctx.HR, ctx.face, ctx.eye_dx, ctx.eye_z = hc, HR, face, eye_dx, eye_z
    ctx.spec, ctx.kind = spec, kind
    return rig, states, ctx


# ------------------------------------------------------------------ hair
def _shell(name, hc, HR, extra, keep, matkey, rig, k, thick=0.012, subsurf=1):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=44, v_segments=24, radius=1.0)
    doomed = [vv for vv in bm.verts if not keep(vv.co)]
    bmesh.ops.delete(bm, geom=doomed, context="VERTS")
    for vv in bm.verts:
        vv.co = Vector((vv.co.x * (HR[0] + extra), vv.co.y * (HR[1] + extra), vv.co.z * (HR[2] + extra)))
    bmesh.ops.solidify(bm, geom=bm.faces[:], thickness=thick * k)
    ob = _mesh_object(name, bm, matkey)
    ob.location = hc
    if subsurf:
        sub = ob.modifiers.new("Subsurf", "SUBSURF")
        sub.levels = sub.render_levels = subsurf
    upd()
    rig.attach(ob, "head")
    return ob


def _face_window(c, top=0.46, chin=-0.45):
    """True where hair may grow: not the face window (front, below the hairline) and not under the chin."""
    if c.y < -0.35 and c.z < top:
        return False
    if c.z < chin and c.y < 0.3:
        return False
    return True


def _blob_chain(name, pts, radii, matkey, rig, bone="head"):
    me = bpy.data.meshes.new(name)
    me.from_pydata([tuple(p) for p in pts], [(i, i + 1) for i in range(len(pts) - 1)], [])
    ob = link(bpy.data.objects.new(name, me))
    ob.modifiers.new("Skin", "SKIN").use_smooth_shade = True
    for i, r in enumerate(radii):
        me.skin_vertices[0].data[i].radius = r
    me.skin_vertices[0].data[0].use_root = True
    sub = ob.modifiers.new("Subsurf", "SUBSURF")
    sub.levels = sub.render_levels = 2
    ob.data.materials.append(mat(matkey))
    for p in ob.data.polygons:
        p.use_smooth = True
    upd()
    rig.attach(ob, bone)
    return ob


BOB_SIDE_FRONT = 0.30
BOB_HAIRLINE = 0.60
# v0.19: no curls over the front half of the head below the hairline (curls on the cheeks hid a profile's face: a boy's
# head looked "almost seen from behind while the body is side-on"; a kicker's face "faces left ... as if kicking backward")
CURLY_FRONT = 0.0
CURLY_HAIRLINE = 0.55
CURLY_SIDE_BACK = 0.10
CURLY_TEMPLE = 0.30


def build_hair(spec, rig, hc, HR, k):
    style, col = spec["hair"], spec["hair_col"]
    off = Vector((0, 0.006 * k, 0.012 * k))
    hcx = hc + off
    if style in ("short", "long", "bun", "ponytail", "puffs"):
        _shell("Hair", hcx, HR, 0.012 * k, lambda c: _face_window(c, 0.46), col, rig, k)
    elif style == "curly":
        # (v0.19: below the temples the hair stays behind the ear, so a profile shows the cheek; covering the side of the
        # head, the curly boy in profile "could be looking away ... or be seen from behind at an angle")
        _shell("Hair", hcx, HR, 0.012 * k, lambda c: _face_window(c, 0.50) and (c.y > CURLY_SIDE_BACK or c.z > CURLY_TEMPLE), col, rig, k)
    elif style == "bob":
        # (v0.18: the side panels stop short of the cheek, so a profile shows the face; covering it, the woman in profile
        # read as having "no visible face; head is a round dark shape")
        _shell("Hair", hcx, HR, 0.016 * k, lambda c: (abs(c.x) > 0.62 and c.z > -0.62 and c.y > BOB_SIDE_FRONT) or _face_window(c, BOB_HAIRLINE, -0.30), col, rig, k, thick=0.018)
    elif style == "buzz":
        _shell("Hair", hc + Vector((0, 0.004 * k, 0.006 * k)), HR, 0.004 * k, lambda c: _face_window(c, 0.52, -0.2) and c.z > -0.25, col, rig, k, thick=0.008)
    elif style == "bald_ring":
        # a fringe of hair round the back of the head, from the nape up to the hat line, with a short
        # tuft above each ear and a scalloped lower edge: a crescent of hair, not a band (a narrow
        # band at ear height read as headphones or a bandage)
        def fringe(c):
            # behind the ears only (hair over the ear read as an earmuff or a pad), from the hat line
            # down to the nape, with a scalloped lower edge
            a = math.atan2(c.x, c.y)
            if HEAD_STYLE in ("A", "B"):
                # v0.23 bench: a narrower crescent kept to the back of the head, behind the ear and above the nape (in
                # profile the wide grey patch behind the ear read as "a beard" or "a face mask" on a face turned the
                # other way)
                low = -0.55 + 0.05 * math.sin(a * 9.0)
                back = 0.42 - 0.10 * max(0.0, c.z)
                return c.y > back and low < c.z < 0.22
            low = -0.82 + 0.06 * math.sin(a * 9.0)
            back = 0.16 - 0.10 * max(0.0, c.z)          # the front edge leans back toward the crown
            return c.y > back and low < c.z < 0.24
        _shell("Hair", hc + Vector((0, 0.008 * k, -0.002 * k)), HR, 0.007 * k, fringe, col, rig, k, thick=0.012)
    if style == "long":
        _blob_chain("HairBack", [hc + Vector((0, 0.07 * k, 0.05 * k)), hc + Vector((0, 0.10 * k, -0.12 * k)), hc + Vector((0, 0.08 * k, -0.30 * k))],
                    [(0.15 * k, 0.09 * k), (0.15 * k, 0.07 * k), (0.12 * k, 0.04 * k)], col, rig)
    if style == "bun":
        ellipsoid("Bun", hc + Vector((0, 0.07 * k, HR[2] * 0.92)), (0.062 * k, 0.058 * k, 0.055 * k), col, rig, "head")
    if style == "ponytail":
        _blob_chain("Ponytail", [hc + Vector((0, HR[1] * 0.92, 0.07 * k)), hc + Vector((0, HR[1] * 1.25, -0.02 * k)),
                                 hc + Vector((0, HR[1] * 1.20, -0.17 * k))],
                    [(0.045 * k, 0.040 * k), (0.050 * k, 0.045 * k), (0.030 * k, 0.026 * k)], col, rig)
        ellipsoid("Tie", hc + Vector((0, HR[1] * 0.98, 0.07 * k)), (0.030 * k, 0.020 * k, 0.030 * k), spec.get("tie", "red"), rig, "head")
    if style == "puffs":
        for sg in (1, -1):
            ellipsoid(f"Puff{'L' if sg > 0 else 'R'}", hc + Vector((sg * HR[0] * 0.80, 0.03 * k, HR[2] * 0.62)),
                      (0.070 * k, 0.064 * k, 0.066 * k), col, rig, "head")
    if style == "curly":
        rnd = random.Random(7)
        for i in range(26):
            th = rnd.uniform(0, 2 * math.pi)
            ph = rnd.uniform(0.15, 1.25)
            d = Vector((math.cos(th) * math.sin(ph), math.sin(th) * math.sin(ph), math.cos(ph)))
            if d.y < CURLY_FRONT and d.z < CURLY_HAIRLINE:
                continue
            if d.y < CURLY_SIDE_BACK and d.z < CURLY_TEMPLE:
                continue
            ellipsoid(f"Curl{i}", hc + Vector((d.x * HR[0], d.y * HR[1], d.z * HR[2])) * 1.0 + d * 0.012 * k,
                      (0.042 * k,) * 3, col, rig, "head", seg=12, rings=8)


def build_facial_hair(spec, rig, face, eye_z, k):
    col = spec.get("facial_hair_col", spec["hair_col"])
    fh = spec.get("facial_hair")
    if not fh:
        return
    mz = eye_z - 0.080 * k
    if fh in ("mustache", "beard"):
        pts = [(-0.034 * k, mz + 0.006 * k), (-0.016 * k, mz + 0.020 * k), (0, mz + 0.018 * k), (0.016 * k, mz + 0.020 * k), (0.034 * k, mz + 0.006 * k)]
        ob = face.curve_on("mustache", pts, 0.0105 * k, col, 0.010 * k)
        ob.name = "FH_mustache"
    if fh == "beard":
        ax, ay, az = face.ax, face.ay, face.az
        mzr = (mz - 0.016 * k) / az

        def keep(c):
            if c.y > 0.35:
                return False
            if __import__("os").environ.get("TPDB_BEARD", "D") == "D":
                # v0.28 bench: a goatee, on the chin alone, joined to the moustache
                return c.z < mzr and c.z > -0.98 and abs(c.x) < 0.46 and c.y < 0.2
            if c.z < mzr and c.z > -0.98:
                return True
            if __import__("os").environ.get("TPDB_BEARD", "D") == "C":
                # v0.28: fuller on the cheek, still short of the ear ("a thin dark strap along the jaw", "it could look like a chin strap")
                return abs(c.x) > 0.44 and -0.9 < c.z < -0.30 and c.y < 0.05
            if __import__("os").environ.get("TPDB_BEARD", "D") == "B":
                # v0.27: stopping short of the ear, so hair and beard do not join in one shape ("a chin strap, helmet strap or face mask", "a dark face covering or mask",
                # now that the turned head shows it; "hair and beard merge into one dark shape")
                return abs(c.x) > 0.60 and -0.9 < c.z < -0.34 and c.y < 0.05
            return abs(c.x) > 0.60 and -0.9 < c.z < 0.02 and c.y < 0.25
        _shell("Beard", face.c, (ax, ay, az), 0.004 * k, keep, col, rig, k, thick=0.020)


def build_hat(spec, rig, hc, HR, k):
    hat = spec.get("hat")
    if not hat:
        return
    col = spec.get("hat_col", "blue")
    R = (HR[0] + 0.020 * k, HR[1] + 0.020 * k, HR[2] + 0.020 * k)
    dome_c = hc + Vector((0, 0.004 * k, 0.020 * k))
    # the dome sits above the brows at the front and lower at the back
    _shell("HatDome", dome_c, R, 0.0, lambda c: c.z > 0.56 - 0.34 * (c.y + 1) / 2, col, rig, k, thick=0.010, subsurf=1)
    if hat == "cap" and spec.get("brim_short"):
        # v0.26 bench (TPDB_OLD=C): a short peak tipped up, so it does not sit over the eye in profile
        ellipsoid("HatBrim", hc + Vector((0, -R[1] * 0.92, R[2] * 0.66)), (0.105 * k, 0.060 * k, 0.011 * k), col, rig, "head",
                  rot=Quaternion((1, 0, 0), 0.10))
        ellipsoid("HatButton", dome_c + Vector((0, 0, R[2] * 1.0)), (0.012 * k,) * 3, col, rig, "head")
    elif hat == "cap":
        ellipsoid("HatBrim", hc + Vector((0, -R[1] * 0.88, R[2] * 0.56)), (0.110 * k, 0.095 * k, 0.012 * k), col, rig, "head",
                  rot=Quaternion((1, 0, 0), -0.12))
        ellipsoid("HatButton", dome_c + Vector((0, 0, R[2] * 1.0)), (0.012 * k,) * 3, col, rig, "head")
    elif hat == "cap_back":
        # v0.24 bench (TPDB_TEEN=A): a cap worn backwards, the brim over the nape
        ellipsoid("HatBrim", hc + Vector((0, R[1] * 0.90, R[2] * 0.44)), (0.105 * k, 0.095 * k, 0.012 * k), col, rig, "head",
                  rot=Quaternion((1, 0, 0), -0.30))
        ellipsoid("HatButton", dome_c + Vector((0, 0, R[2] * 1.0)), (0.012 * k,) * 3, col, rig, "head")
    elif hat == "sun":
        ellipsoid("HatBrim", hc + Vector((0, 0.004 * k, R[2] * 0.52)), (R[0] * 1.85, R[1] * 1.85, 0.012 * k), col, rig, "head")
        ellipsoid("HatBand", hc + Vector((0, 0.004 * k, R[2] * 0.62)), (R[0] * 0.90, R[1] * 0.90, 0.022 * k), spec.get("band_col", "red"), rig, "head")
    elif hat == "beanie":
        ellipsoid("HatBand", hc + Vector((0, 0.004 * k, R[2] * 0.56)), (R[0] * 0.98, R[1] * 0.98, 0.036 * k), col, rig, "head")
        ellipsoid("HatPom", dome_c + Vector((0, 0, R[2] * 1.0)), (0.030 * k,) * 3, spec.get("band_col", "cream"), rig, "head")
