"""Shared Blender helpers for the TPDB cast: materials, rig, skin bodies, primitives."""
import json
import math
import os

import bpy  # noqa: F401  (must come before bmesh)
import bmesh
from mathutils import Matrix, Quaternion, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
PALETTE = json.load(open(os.path.join(HERE, "..", "..", "palette.json")))["colors"]


def lin(hexc):
    c = [int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    return tuple(x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c) + (1.0,)


_MATS = {}


def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    _MATS.clear()


def mat(key):
    if key not in _MATS:
        m = bpy.data.materials.new(key)
        m.use_nodes = True
        m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = lin(PALETTE[key])
        _MATS[key] = m
    return _MATS[key]


def link(obj):
    bpy.context.scene.collection.objects.link(obj)
    return obj


def nrm(x):
    x = Vector(x)
    return x.normalized() if x.length > 1e-9 else x


def upd():
    bpy.context.view_layer.update()


def list_m(M):
    return [M[i][j] for i in range(4) for j in range(4)]


class Rig:
    """Armature plus helpers to parent things to bones and to pose with IK."""

    def __init__(self, root, bones):
        data = bpy.data.armatures.new("RIG")
        self.arm = link(bpy.data.objects.new("RIG", data))
        self.arm.parent = root
        bpy.context.view_layer.objects.active = self.arm
        bpy.ops.object.mode_set(mode="EDIT")
        for name, (h, t, parent) in bones.items():
            b = data.edit_bones.new(name)
            b.head, b.tail = Vector(h), Vector(t)
            if parent:
                b.parent = data.edit_bones[parent]
        bpy.ops.object.mode_set(mode="OBJECT")
        upd()
        for pb in self.arm.pose.bones:
            pb.rotation_mode = "QUATERNION"

    def attach(self, obj, bone):
        """Parent obj to bone, keeping its current world transform (at the current pose)."""
        pb = self.arm.pose.bones[bone]
        mw = obj.matrix_world.copy()
        obj.parent = self.arm
        obj.parent_type = "BONE"
        obj.parent_bone = bone
        upd()
        bm = self.arm.matrix_world @ pb.matrix @ Matrix.Translation((0, pb.bone.length, 0))
        obj.matrix_parent_inverse = bm.inverted()
        obj.matrix_world = mw
        return obj

    def skin_weights(self, obj, weights):
        for i, wd in enumerate(weights):
            for bone, w in wd.items():
                g = obj.vertex_groups.get(bone) or obj.vertex_groups.new(name=bone)
                g.add([i], w, "REPLACE")
        m = obj.modifiers.new("Armature", "ARMATURE")
        m.object = self.arm

    def reset(self):
        for pb in self.arm.pose.bones:
            pb.location = (0, 0, 0)
            pb.rotation_quaternion = (1, 0, 0, 0)
            pb.scale = (1, 1, 1)
        upd()

    def head(self, bone):
        upd()
        return self.arm.pose.bones[bone].head.copy()

    def tail(self, bone):
        upd()
        return self.arm.pose.bones[bone].tail.copy()

    def aim(self, bone, target, twist=0.0):
        upd()
        pb = self.arm.pose.bones[bone]
        M = pb.matrix.copy()
        h = M.translation.copy()
        cur = (M.to_3x3() @ Vector((0, 1, 0))).normalized()
        want = nrm(Vector(target) - h)
        q = cur.rotation_difference(want)
        R = Matrix.Translation(h) @ q.to_matrix().to_4x4() @ Matrix.Translation(-h)
        M2 = R @ M
        if twist:
            T = Matrix.Translation(h) @ Matrix.Rotation(twist, 4, want) @ Matrix.Translation(-h)
            M2 = T @ M2
        pb.matrix = M2
        upd()

    def aim_dir(self, bone, direction, twist=0.0):
        self.aim(bone, self.head(bone) + nrm(direction), twist)

    def ik2(self, b1, b2, target, hint):
        """Two-bone IK: point b1 and b2 so b2's tail reaches target, bending toward hint.
        Returns the distance still missing (0 when the target is reachable)."""
        upd()
        p0 = self.head(b1)
        l1 = self.arm.pose.bones[b1].bone.length
        l2 = self.arm.pose.bones[b2].bone.length
        t = Vector(target)
        d = t - p0
        dist = min(d.length, (l1 + l2) * 0.999)
        dist = max(dist, abs(l1 - l2) * 1.001 + 1e-4)
        dn = nrm(d)
        a = (l1 * l1 + dist * dist - l2 * l2) / (2 * l1 * dist)
        a = max(-1.0, min(1.0, a))
        h = nrm(Vector(hint) - dn * Vector(hint).dot(dn))
        if h.length < 1e-6:
            h = nrm(dn.orthogonal())
        knee = p0 + dn * (l1 * a) + h * (l1 * math.sqrt(max(0.0, 1 - a * a)))
        self.aim(b1, knee)
        self.aim(b2, p0 + dn * dist)
        return max(0.0, d.length - dist)

    def bone_dir(self, bone):
        upd()
        pb = self.arm.pose.bones[bone]
        return nrm(pb.tail - pb.head)

    def key_pose(self, name):
        if self.arm.animation_data is None:
            self.arm.animation_data_create()
        self.arm.animation_data.action = None
        for pb in self.arm.pose.bones:
            pb.keyframe_insert("location", frame=1)
            pb.keyframe_insert("rotation_quaternion", frame=1)
            pb.keyframe_insert("scale", frame=1)
        act = self.arm.animation_data.action
        act.name = name
        act.use_fake_user = True
        self.arm.animation_data.action = None


def _roots_for(n, edges):
    parent = list(range(n))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for a, b in edges:
        parent[find(a)] = find(b)
    seen, roots = set(), []
    for i in range(n):
        r0 = find(i)
        if r0 not in seen:
            seen.add(r0)
            roots.append(i)
    return roots


def skin_object(name, verts, edges, radii, matkey, rig, weights, subsurf=2):
    me = bpy.data.meshes.new(name)
    me.from_pydata([tuple(p) for p in verts], edges, [])
    ob = link(bpy.data.objects.new(name, me))
    sk = ob.modifiers.new("Skin", "SKIN")
    sk.use_smooth_shade = True
    for i, r in enumerate(radii):
        me.skin_vertices[0].data[i].radius = r if isinstance(r, (tuple, list)) else (r, r)
    for i in _roots_for(len(verts), edges):
        me.skin_vertices[0].data[i].use_root = True
    # Weights go on the skeleton nodes and the Skin modifier carries them onto its hull. It leaves a
    # few end-cap vertices with no weight at all (they then stayed at rest when the body bent far,
    # e.g. lying down), so after baking the hull to a real mesh those get weights from the nearest
    # skeleton edge, measured in units of the hull radius there.
    for i, wd in enumerate(weights):
        for bone, w in wd.items():
            g = ob.vertex_groups.get(bone) or ob.vertex_groups.new(name=bone)
            g.add([i], w, "REPLACE")
    upd()
    dg = bpy.context.evaluated_depsgraph_get()
    baked = bpy.data.meshes.new_from_object(ob.evaluated_get(dg), depsgraph=dg)
    ob.modifiers.remove(sk)
    old = ob.data
    ob.data = baked
    bpy.data.meshes.remove(old)
    baked.name = name
    V = [Vector(p) for p in verts]
    R = [(r, r) if not isinstance(r, (tuple, list)) else tuple(r) for r in radii]
    segs = list(edges) or [(i, i) for i in range(len(V))]
    gidx = {g.name: g for g in ob.vertex_groups}
    for v in baked.vertices:
        if sum(g.weight for g in v.groups) > 0.05:
            continue
        best = None
        for a_, b_ in segs:
            ab = V[b_] - V[a_]
            t = 0.0 if ab.length_squared < 1e-12 else max(0.0, min(1.0, (v.co - V[a_]).dot(ab) / ab.length_squared))
            off = v.co - (V[a_] + ab * t)
            rx = R[a_][0] * (1 - t) + R[b_][0] * t
            ry = R[a_][1] * (1 - t) + R[b_][1] * t
            d = (off.x / rx) ** 2 + (off.y / ry) ** 2 + (off.z / ((rx + ry) / 2)) ** 2
            if best is None or d < best[0]:
                best = (d, a_, b_, t)
        _, a_, b_, t = best
        mix = {}
        for bone, w in weights[a_].items():
            mix[bone] = mix.get(bone, 0.0) + w * (1 - t)
        for bone, w in weights[b_].items():
            mix[bone] = mix.get(bone, 0.0) + w * t
        tot = sum(mix.values()) or 1.0
        for bone, w in mix.items():
            if w > 1e-4:
                (gidx.get(bone) or ob.vertex_groups.new(name=bone)).add([v.index], w / tot, "REPLACE")
                gidx = {g.name: g for g in ob.vertex_groups}
    arm_mod = ob.modifiers.new("Armature", "ARMATURE")
    arm_mod.object = rig.arm
    ob.parent = rig.arm
    s = ob.modifiers.new("Subsurf", "SUBSURF")
    s.levels = s.render_levels = subsurf
    ob.data.materials.append(mat(matkey))
    for p in ob.data.polygons:
        p.use_smooth = True
    return ob


def skin_like(ob, host, rig, keep=None):
    """v0.15: re-bind a decoration (a placket, button, pocket, hood string, coat spot) that sits on a skinned
    surface so it bends with that surface. Parented rigidly to one bone, it stayed put while the surface
    under it bent with the chest or the arms, and floated off the body (a cardigan's placket a hand in front
    of a woman reaching up, a hoodie's strings off a crouching teenager, a spot off a sitting dog). Each of
    its vertices takes the bone weights of the nearest vertex of the host, at rest."""
    from mathutils.kdtree import KDTree
    upd()
    if ob.type != "MESH":
        return ob
    mw = ob.matrix_world.copy()
    ob.parent = None
    ob.matrix_parent_inverse = Matrix.Identity(4)
    ob.data.transform(mw)
    ob.matrix_world = Matrix.Identity(4)
    hv = host.data.vertices
    kd = KDTree(len(hv))
    hw = host.matrix_world
    for v in hv:
        kd.insert(hw @ v.co, v.index)
    kd.balance()
    names = {g.index: g.name for g in host.vertex_groups}
    for v in ob.data.vertices:
        _, i, _ = kd.find(v.co)
        # keep: the bones a decoration may follow (a placket by the collar must not take the shoulder's
        # weight from the arm, or it is dragged up into a sheet when the arms go up)
        ws = {names[g.group]: g.weight for g in hv[i].groups if g.weight > 1e-4 and (keep is None or names[g.group] in keep)}
        tot = sum(ws.values())
        if tot <= 1e-6:
            ws, tot = {"chest": 1.0}, 1.0
        for nm, w in ws.items():
            (ob.vertex_groups.get(nm) or ob.vertex_groups.new(name=nm)).add([v.index], w / tot, "REPLACE")
    m = ob.modifiers.new("Armature", "ARMATURE")
    m.object = rig.arm
    ob.parent = rig.arm
    upd()
    return ob


def _mesh_object(name, bm, matkey, smooth=True):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    if smooth:
        for p in me.polygons:
            p.use_smooth = True
    ob = link(bpy.data.objects.new(name, me))
    ob.data.materials.append(mat(matkey))
    return ob


def ellipsoid(name, center, radii, matkey, rig=None, bone=None, rot=None, seg=24, rings=14):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=rings, radius=1.0)
    ob = _mesh_object(name, bm, matkey)
    ob.scale = radii
    ob.location = center
    if rot is not None:
        ob.rotation_mode = "QUATERNION"
        ob.rotation_quaternion = rot
    upd()
    if rig:
        rig.attach(ob, bone)
    return ob


def half_ellipsoid(name, matkey, keep="lower"):
    """Half of a unit sphere with a flat cut edge: keep='lower' gives a D-shape (flat top)."""
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=28, v_segments=16, radius=1.0)
    if keep == "lower":
        bmesh.ops.delete(bm, geom=[vv for vv in bm.verts if vv.co.z > 0.02], context="VERTS")
    else:
        bmesh.ops.delete(bm, geom=[vv for vv in bm.verts if vv.co.z < -0.02], context="VERTS")
    return _mesh_object(name, bm, matkey)


def capsule_arc(name, matkey, bend=0.25, seg=18):
    """A unit-width bent bar in the local XZ plane (x in [-1,1], arched up by `bend`),
    thickness 1 along Z before scaling. Used for brows."""
    bm = bmesh.new()
    rings = []
    for i in range(seg + 1):
        t = -1 + 2 * i / seg
        cz = bend * (1 - t * t)
        taper = 0.55 + 0.45 * math.sqrt(max(0.0, 1 - t * t))
        ring = []
        for j in range(8):
            a = j / 8 * 2 * math.pi
            ring.append(bm.verts.new((t, math.sin(a) * 0.5 * taper, cz + math.cos(a) * 0.5 * taper)))
        rings.append(ring)
    for i in range(seg):
        for j in range(8):
            bm.faces.new((rings[i][j], rings[i][(j + 1) % 8], rings[i + 1][(j + 1) % 8], rings[i + 1][j]))
    bm.faces.new(rings[0][::-1])
    bm.faces.new(rings[-1])
    return _mesh_object(name, bm, matkey)


def tube(name, pts, radius, matkey, rig=None, bone=None, closed=False):
    cu = bpy.data.curves.new(name, "CURVE")
    cu.dimensions = "3D"
    cu.bevel_depth = radius
    cu.bevel_resolution = 3
    cu.use_fill_caps = True
    sp = cu.splines.new("POLY")
    sp.points.add(len(pts) - 1)
    for i, p in enumerate(pts):
        sp.points[i].co = (p[0], p[1], p[2], 1.0)
    sp.use_cyclic_u = closed
    ob = link(bpy.data.objects.new(name, cu))
    ob.data.materials.append(mat(matkey))
    upd()
    if rig:
        rig.attach(ob, bone)
    return ob


def flat_prism(name, outline, origin, ax, ay, normal, thickness, matkey):
    """A flat plate cut to a 2D outline: outline is [(x, y), ...] in the plane spanned by ax and ay
    (world vectors) around origin, extruded thickness along normal. Used where a prop must show an
    exact silhouette (a piece of cutlery) that primitives would only approximate."""
    bm = bmesh.new()
    O, ax, ay, n = Vector(origin), Vector(ax), Vector(ay), Vector(normal).normalized()
    top = [bm.verts.new(O + ax * x + ay * y + n * (thickness / 2)) for x, y in outline]
    bot = [bm.verts.new(O + ax * x + ay * y - n * (thickness / 2)) for x, y in outline]
    bm.faces.new(top)
    bm.faces.new(list(reversed(bot)))
    k = len(outline)
    for i in range(k):
        j = (i + 1) % k
        bm.faces.new([top[i], top[j], bot[j], bot[i]])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    return _mesh_object(name, bm, matkey, smooth=False)


def tube_mesh(name, pts, radius, matkey, closed=False):
    """A tube converted to a mesh (so it counts for framing and renders like any mesh)."""
    cu = tube(name + "_crv", pts, radius, matkey, closed=closed)
    upd()
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(cu.evaluated_get(dg))
    me.name = name
    ob = link(bpy.data.objects.new(name, me))
    if not ob.data.materials:
        ob.data.materials.append(mat(matkey))
    for p in ob.data.polygons:
        p.use_smooth = True
    bpy.data.objects.remove(cu, do_unlink=True)
    return ob


def smooth_curve(ctrl, n=14):
    """Catmull-Rom through control points -> dense polyline."""
    P = [Vector(c) for c in ctrl]
    if len(P) == 2:
        return [P[0].lerp(P[1], i / (n - 1)) for i in range(n)]
    out = []
    ext = [P[0] + (P[0] - P[1])] + P + [P[-1] + (P[-1] - P[-2])]
    for i in range(1, len(ext) - 2):
        p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
        for k in range(n):
            t = k / n
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t
                              + (-p0 + 3 * p1 - 3 * p2 + p3) * t * t * t))
    out.append(P[-1])
    return out


def cyl(name, p0, p1, r, matkey, seg=16, r1=None, caps=True):
    """Cylinder (or cone when r1 is given) between two world points."""
    p0, p1 = Vector(p0), Vector(p1)
    d = p1 - p0
    L = max(d.length, 1e-5)
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=caps, segments=seg, radius1=r, radius2=r if r1 is None else r1, depth=L)
    ob = _mesh_object(name, bm, matkey)
    q = Vector((0, 0, 1)).rotation_difference(d.normalized())
    ob.rotation_mode = "QUATERNION"
    ob.rotation_quaternion = q
    ob.location = (p0 + p1) / 2
    upd()
    return ob


def box(name, center, size, matkey, rot=None, bevel=0.0):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    if bevel > 0:
        bmesh.ops.bevel(bm, geom=bm.edges[:] + bm.verts[:], offset=bevel / max(min(size), 1e-6), segments=2, affect="EDGES")
    ob = _mesh_object(name, bm, matkey, smooth=False)
    ob.scale = size
    ob.location = center
    if rot is not None:
        ob.rotation_mode = "QUATERNION"
        ob.rotation_quaternion = rot
    upd()
    return ob


def disc(name, center, normal, r, thickness, matkey, seg=32, r_top=None):
    n = nrm(normal)
    return cyl(name, Vector(center) - n * thickness / 2, Vector(center) + n * thickness / 2, r, matkey, seg=seg, r1=r_top)


# v0.39 bench (TPDB_ISECT39): Line Art draws a line wherever two parts pass into each other, so a shoe made of two ellipsoids, a belt on
# the trousers, a dog's chest patch and its paws each drew a seam ("separate rounded pieces, like a jointed doll or mannequin"; "white
# paws that look like mittens or separate pieces"). "B": no intersection line on those parts; their contours stay.
ISECT39 = os.environ.get("TPDB_ISECT39", "B")  # v0.39 bench (vision/isolation_v039.md): B, no intersection lines on the overlap parts


def no_isect(ob):
    """No Line Art intersection line where this part passes into its neighbour (its own contour is still drawn)."""
    try:
        ob.lineart.usage = "NO_INTERSECTION"
    except AttributeError:
        pass
    return ob


def flatten_below(ob, z, axis=2, spare=()):
    """Clamp a baked mesh's rest vertices to z from below (a hem edge, a sole): the Skin modifier ends every chain in a dome. Vertices weighted
    to a bone whose name starts with one of spare are left (a top's sleeves hang below its hem at rest)."""
    gname = {g.index: g.name for g in ob.vertex_groups}
    for v in ob.data.vertices:
        if spare and sum(g.weight for g in v.groups if gname.get(g.group, "").startswith(tuple(spare))) > 0.05:
            continue
        if v.co[axis] < z:
            v.co[axis] = z
    ob.data.update()
    return ob


def flatten_above(ob, z, axis=2):
    """Clamp a baked mesh's rest vertices to z from above (a waistband's top edge)."""
    for v in ob.data.vertices:
        if v.co[axis] > z:
            v.co[axis] = z
    ob.data.update()
    return ob


def anchor(rig, name, loc, bone):
    e = link(bpy.data.objects.new(f"ANCHOR_{name}", None))
    e.empty_display_size = 0.03
    e.location = loc
    upd()
    rig.attach(e, bone)
    return e


class Frame:
    """A local frame: origin + rotation. Local axes match character space
    (+X = character's left, +Y = back, +Z = up)."""

    def __init__(self, origin, rot=None):
        self.o = Vector(origin)
        self.q = rot if rot is not None else Quaternion()

    @staticmethod
    def euler(origin, rx=0.0, ry=0.0, rz=0.0):
        q = (Quaternion((0, 0, 1), math.radians(rz)) @ Quaternion((0, 1, 0), math.radians(ry))
             @ Quaternion((1, 0, 0), math.radians(rx)))
        return Frame(origin, q)

    def p(self, x, y, z):
        return self.o + self.q @ Vector((x, y, z))

    def d(self, x, y, z):
        return self.q @ Vector((x, y, z))


def frame_toward(origin, direction, up=(0, 0, 1)):
    """Frame whose local -Y (forward) points along `direction`, local Z kept as close to `up` as possible."""
    Yw = -nrm(direction)
    up = Vector(up)
    Zw = nrm(up - Yw * up.dot(Yw))
    if Zw.length < 1e-6:
        Zw = nrm(Yw.orthogonal())
    Xw = Yw.cross(Zw)
    M = Matrix((Xw, Yw, Zw)).transposed()
    return Frame(origin, M.to_quaternion())
