"""Shared Blender helpers for the TPDB cast: materials, rig, skin bodies, primitives."""
import json
import math
import os

import bpy  # noqa: F401  (must come before bmesh)
import bmesh
from mathutils import Matrix, Quaternion, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
PALETTE = json.load(open(os.path.join(HERE, "..", "..", "palette.json")))["colors"]
# TPDB_SHELL47 "B": a garment made by shell_over rides on the finished surface of the garment under it; "O": it is bent by its own weights
SHELL47 = os.environ.get("TPDB_SHELL47", "B")
# TPDB_SHADE47 "B" (vision/flaws_v046.md O2; rest_shade here, to_cel in render_assets.py): the shadow tone is laid by the surface's normal alone,
# so on a figure who leans over her work the chest faces the ground and the tone's edge ran across the middle of it: "There is a slightly
# lighter, semi-transparent patch on the front of her dress where her arms cross." (v046 pic_89). "B": the cloth of the trunk keeps the shading it has standing upright, whatever the trunk does: every skinned
# mesh carries its rest normal and how much of each vertex belongs to the trunk's bones, and the shader lights the trunk's share of a surface
# by the rest normal (turned with the figure's yaw). The edge then lies along the figure's far side in every pose. Limbs and heads are lit as
# before. "O": v0.46's, the posed normal everywhere
SHADE47 = os.environ.get("TPDB_SHADE47", "B")


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
    if os.environ.get("TPDB_HULLCHECK"):
        # v0.52: where four branches meet (the neck, the chest and two shoulders) the Skin hull can break when a radius changes by a
        # millimetre: the chest's ring then stands out of a collapsed trunk like a plate. A broken hull has edges folded nearly flat.
        hb = bmesh.new()
        hb.from_mesh(baked)
        hb.normal_update()
        folds = sum(1 for e in hb.edges if len(e.link_faces) == 2 and e.link_faces[0].normal.dot(e.link_faces[1].normal) < -0.6)
        print("HULLCHECK", name, "verts", len(hb.verts), "folds", folds, "open", sum(1 for e in hb.edges if len(e.link_faces) != 2))
        hb.free()
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


def rest_shade(bones=("hips", "spine", "chest", "neck")):
    """v0.47 (TPDB_SHADE47): call with the rig at rest. Every mesh with weights on the trunk's bones gets two point attributes: tpdb_rest_n,
    its normal now, and tpdb_rest_w, the trunk's share of the vertex's weights. They ride through Armature, Subdivision, Surface Deform and
    Solidify to the drawn surface; render_assets.to_cel reads them."""
    if SHADE47 != "B":
        return
    for ob in bpy.context.scene.objects:
        if ob.type != "MESH" or not ob.vertex_groups:
            continue
        gi = {g.index for g in ob.vertex_groups if g.name in bones}
        if not gi:
            continue
        me = ob.data
        an = me.attributes.get("tpdb_rest_n") or me.attributes.new("tpdb_rest_n", "FLOAT_VECTOR", "POINT")
        aw = me.attributes.get("tpdb_rest_w") or me.attributes.new("tpdb_rest_w", "FLOAT", "POINT")
        nv, wv = [], []
        for v in me.vertices:
            tot = sum(g.weight for g in v.groups)
            wv.append(sum(g.weight for g in v.groups if g.group in gi) / tot if tot > 1e-6 else 0.0)
            nv.extend(v.normal)
        an.data.foreach_set("vector", nv)
        aw.data.foreach_set("value", wv)


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


def cut_field(bm, f):
    """Cut a bmesh along the zero line of f (a number for every vertex) and remove the side where f is positive. Each crossed edge is split
    at the crossing (the new vertex takes the mix of its two ends' weights), the new vertices are joined across their faces, and the positive
    vertices go; the cut edge is a smooth ring whatever the mesh's own edges do."""
    eps = 1e-7
    on = []
    for e in list(bm.edges):
        a, b = e.verts
        fa, fb = f[a], f[b]
        if (fa > eps and fb < -eps) or (fa < -eps and fb > eps):
            t = fa / (fa - fb)
            co = a.co.lerp(b.co, t)
            _, nv = bmesh.utils.edge_split(e, a, t)
            nv.co = co
            f[nv] = 0.0
            on.append(nv)
    seen = set(on)
    on += [v for v in bm.verts if v not in seen and abs(f[v]) <= eps]
    if on:
        bmesh.ops.connect_verts(bm, verts=on)
    gone = [v for v in bm.verts if f[v] > eps]
    if gone:
        bmesh.ops.delete(bm, geom=gone, context="VERTS")


def _ride_target(host, levels):
    """The host's finished surface in triangles, never drawn: what a shell's Surface Deform is bound to (the binding refuses a target with a
    concave polygon, and a smoothed hull has some). It is smoothed to the level the shell was taken at, so every vertex of the shell lies on
    a vertex or an edge of it: against the host's own coarser level a few vertices in the crease of the armpit lay a millimetre inside,
    were bound across the crease, and flew out a hand's length when the arm went up."""
    c = bpy.data.objects.get(host.name + "Ride")
    if c is None:
        c = link(host.copy())
        c.name = host.name + "Ride"
        for m in c.modifiers:
            if m.type == "SUBSURF":
                m.levels = m.render_levels = levels
        c.modifiers.new("Tri", "TRIANGULATE")
        c.hide_render = True
        try:
            c.lineart.usage = "EXCLUDE"
        except (AttributeError, TypeError):
            pass
        upd()
    return c


def shell_over(host, name, matkey, rig, offset, fields=(), rim=0.0, mark=None, levels=3):
    """v0.47: a garment worn over another as a shell of that garment's own surface: the host's surface at a finer level, cut along the zero
    line of each field in turn (a function of a vertex's rest position and its bone weights by name; the positive side goes), moved out along
    its normals by offset and given an edge rim deep. It carries the host's weights, so it bends exactly as the host does and the host cannot
    come through it. (A second Skin hull over the first is another surface: the shirt came through a vest at the shoulders in ragged patches,
    and the hull itself broke at a node with four branches.) mark picks edges, by their two ends' positions, that are drawn as lines."""
    upd()
    sub = next(m for m in host.modifiers if m.type == "SUBSURF")
    was = (sub.levels, sub.render_levels)
    sub.levels = sub.render_levels = levels
    upd()
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(host.evaluated_get(dg), depsgraph=dg)
    sub.levels, sub.render_levels = was
    upd()
    bm = bmesh.new()
    bm.from_mesh(me)
    bpy.data.meshes.remove(me)
    dl = bm.verts.layers.deform.verify()
    names = {g.index: g.name for g in host.vertex_groups}
    for fn in fields:
        cut_field(bm, {v: fn(v.co, {names[i]: w for i, w in v[dl].items() if i in names}) for v in bm.verts})
    bm.normal_update()
    ride = SHELL47 == "B"
    if not ride:
        for v in bm.verts:
            v.co += v.normal * offset
    marks = []
    if mark is not None:
        bm.edges.ensure_lookup_table()
        marks = [(e.verts[0].co.copy(), e.verts[1].co.copy()) for e in bm.edges if mark(e.verts[0].co, e.verts[1].co)]
    if rim > 0 and not ride:
        bmesh.ops.solidify(bm, geom=bm.faces[:], thickness=rim)
    if not ride:
        # (riding, the faces keep the host's own outward normals, which the Displace moves them along)
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    ob = _mesh_object(name, bm, matkey, smooth=True)
    for g in sorted(host.vertex_groups, key=lambda g: g.index):
        if ob.vertex_groups.get(g.name) is None:
            ob.vertex_groups.new(name=g.name)
    if marks:
        key = lambda p: (round(p.x, 5), round(p.y, 5), round(p.z, 5))
        want = {frozenset((key(a), key(b))) for a, b in marks}
        vs = ob.data.vertices
        hit = [e.index for e in ob.data.edges if frozenset((key(vs[e.vertices[0]].co), key(vs[e.vertices[1]].co))) in want]
        if hasattr(bpy.types.MeshEdge, "use_freestyle_mark"):
            for i in hit:
                ob.data.edges[i].use_freestyle_mark = True
        else:
            # (Blender 5: the mark Line Art reads is a named edge attribute)
            att = ob.data.attributes.get("freestyle_edge") or ob.data.attributes.new("freestyle_edge", "BOOLEAN", "EDGE")
            for i in hit:
                att.data[i].value = True
    ob.parent = rig.arm
    upd()
    bound = False
    if ride:
        # v0.47 (TPDB_SHELL47): the shell rides on the host's finished surface (a Surface Deform bound at rest). The host is bent as a coarse
        # cage and then smoothed; the shell, a fine mesh, was bent vertex by vertex, which is another surface wherever a joint bends far: a
        # cardigan's sleeves showed the top under them in patches at the elbows, and its back at the waist of a kneeling figure.
        # It is bound lying ON the host's surface and moved out along its normals afterwards (a Displace, then a Solidify for the rim): bound
        # a centimetre off, a vertex at the side of the trunk took the inside of the arm hanging beside it as its nearest face, and was
        # dragged out in a fan of spikes when the arm moved.
        m = ob.modifiers.new("Ride", "SURFACE_DEFORM")
        m.target = _ride_target(host, levels)
        try:
            with bpy.context.temp_override(object=ob, active_object=ob, selected_objects=[ob]):
                bpy.ops.object.surfacedeform_bind(modifier=m.name)
            upd()
            bound = bool(m.is_bound)
        except Exception as e:      # noqa: BLE001
            print("shell_over: bind raised", name, e)
        if not bound:
            print("shell_over: NOT BOUND, bent by its own weights:", name)
            ob.modifiers.remove(m)
    if not bound:
        m = ob.modifiers.new("Armature", "ARMATURE")
        m.object = rig.arm
    if ride:
        m = ob.modifiers.new("Out", "DISPLACE")
        m.direction = "NORMAL"
        m.mid_level = 0.0
        m.strength = offset
        if rim > 0:
            m = ob.modifiers.new("Rim", "SOLIDIFY")
            m.thickness = rim
            m.offset = -1.0
            m.use_rim = True
    upd()
    return ob


def open_end(ob, z, rig, matkey, lid=None, inset=0.003, axis=2):
    """v0.47: open a baked hull's flattened end (flatten_below at z). The end's lid comes off the hull and, with lid a name, is an object of
    its own just inside the opening, bent and smoothed as the hull is, so its edge is the opening's edge in every pose. A limb comes out
    through the lid, and the lid draws a line where it does (FORCE_INTERSECTION: limbs are drawn with no such line elsewhere, and the hull,
    whose other end passes into the garment above it, cannot be asked for one). As part of the hull the lid had no line where a knee came
    out of it, round patches on the cloth; a hull left open with a thickness showed its inside as ragged marks."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bm.normal_update()
    dl = bm.verts.layers.deform.verify()
    faces = [f for f in bm.faces if f.normal[axis] < -0.7 and f.calc_center_median()[axis] < z + 0.012]
    quads = [[(v.co.copy(), dict(v[dl].items())) for v in f.verts] for f in faces]
    if faces:
        bmesh.ops.delete(bm, geom=faces, context="FACES")
    bm.to_mesh(ob.data)
    bm.free()
    ob.data.update()
    print("open_end", ob.name, "lid faces", len(quads))
    if not (lid and quads):
        return None
    up = Vector([inset if i == axis else 0.0 for i in range(3)])
    lb = bmesh.new()
    ldl = lb.verts.layers.deform.verify()
    for q in quads:
        vs = []
        for co, w in q:
            v = lb.verts.new(co + up)
            for gi, wt in w.items():
                v[ldl][gi] = wt
            vs.append(v)
        lb.faces.new(vs)
    lo = _mesh_object(lid, lb, matkey, smooth=True)
    for g in sorted(ob.vertex_groups, key=lambda g: g.index):
        lo.vertex_groups.new(name=g.name)
    lo.parent = rig.arm
    m = lo.modifiers.new("Armature", "ARMATURE")
    m.object = rig.arm
    sub = next((x for x in ob.modifiers if x.type == "SUBSURF"), None)
    m = lo.modifiers.new("Subsurf", "SUBSURF")
    m.levels = m.render_levels = sub.levels if sub else 2
    try:
        lo.lineart.usage = "FORCE_INTERSECTION"
    except (AttributeError, TypeError):
        pass
    upd()
    return lo


def open_branch(ob, p, n, rig, matkey, lid, pick, inset=0.004, lid_k=1.0, hem_k=1.0):
    """v0.52: open the end of one branch of a baked hull (a sleeve) at the plane through p whose normal n points out of the end. Of the
    vertices that pick(co, weights by bone name) takes, those past the plane are brought onto it; the faces lying in the plane come off
    the hull and are an object of their own, lid, a little inside the opening, as open_end's lid is: the arm comes out through it, and it
    draws the line where it does. The branch's edge is then the hem."""
    n = n.normalized()
    gname = {g.index: g.name for g in ob.vertex_groups}
    took = set()
    for v in ob.data.vertices:
        if not pick(v.co, {gname[g.group]: g.weight for g in v.groups if g.group in gname}):
            continue
        d = (v.co - p).dot(n)
        if d > -1e-5:
            v.co = v.co - n * d
            took.add(v.index)
    if hem_k != 1.0 and took:
        # (the opening's ring drawn in a little: smoothed, an open edge keeps its ring's size while the tube above it draws in, and the hem
        # stood out like the mouth of a bell)
        cen0 = sum((ob.data.vertices[i].co for i in took), Vector()) / len(took)
        for i in took:
            ob.data.vertices[i].co = cen0 + (ob.data.vertices[i].co - cen0) * hem_k
    ob.data.update()
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bm.normal_update()
    dl = bm.verts.layers.deform.verify()
    faces = [f for f in bm.faces if all(v.index in took for v in f.verts)]
    quads = [[(v.co.copy(), dict(v[dl].items())) for v in f.verts] for f in faces]
    if faces:
        bmesh.ops.delete(bm, geom=faces, context="FACES")
    bm.to_mesh(ob.data)
    bm.free()
    ob.data.update()
    print("open_branch", ob.name, lid, "moved", len(took), "lid faces", len(quads))
    if not quads:
        return None
    lb = bmesh.new()
    ldl = lb.verts.layers.deform.verify()
    seen = {}
    for q in quads:
        vs = []
        for co, w in q:
            key = (round(co.x, 6), round(co.y, 6), round(co.z, 6))
            if key not in seen:
                v = lb.verts.new(co - n * inset)
                for gi, wt in w.items():
                    v[ldl][gi] = wt
                seen[key] = v
            vs.append(seen[key])
        lb.faces.new(vs)
    if lid_k != 1.0 and seen:
        # (the lid a little smaller than the opening: with its edge lying on the sleeve's own wall, Line Art drew short dashes of it there)
        cen = sum((v.co for v in seen.values()), Vector()) / len(seen)
        for v in seen.values():
            v.co = cen + (v.co - cen) * lid_k
    lo = _mesh_object(lid, lb, matkey, smooth=True)
    for g in sorted(ob.vertex_groups, key=lambda g: g.index):
        lo.vertex_groups.new(name=g.name)
    lo.parent = rig.arm
    m = lo.modifiers.new("Armature", "ARMATURE")
    m.object = rig.arm
    sub = next((x for x in ob.modifiers if x.type == "SUBSURF"), None)
    m = lo.modifiers.new("Subsurf", "SUBSURF")
    m.levels = m.render_levels = sub.levels if sub else 2
    try:
        lo.lineart.usage = "FORCE_INTERSECTION"
    except (AttributeError, TypeError):
        pass
    upd()
    return lo


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


def squircle(co, n):
    """A point of the unit sphere moved out to a ball whose level sections are |x|^n + |y|^n = r^n (n = 2: the sphere itself).
    The front, back and side views keep the sphere's outline; between them the ball is fuller, like a head with cheeks."""
    rho = math.hypot(co[0], co[1])
    if not n or n == 2.0 or rho < 1e-9:
        return Vector(co)
    f = ((abs(co[0]) / rho) ** n + (abs(co[1]) / rho) ** n) ** (-1.0 / n)
    return Vector((co[0] * f, co[1] * f, co[2]))


# v0.48 (TPDB_HEAD48; vision/isolation_v048.md): the head is no longer a ball. Sam, of v0.47's cast: "I am not a fan of the squashed oval
# heads, and the faces need fixing". Every head until v0.47 was an ellipsoid wider than it was tall (1.04 : 0.96 of its radius), so a face sat
# in the lower middle of a wide oval and a chin was the underside of a ball. "B": the head is taller than it is wide and is an egg: below
# the height z0 (in units of its half height, 0 the middle) its width and depth narrow toward the chin by `jaw` at the bottom, and the lower
# face is carried forward by `fwd`, so there is a jaw under the cheeks from the front and a chin ahead of the neck from the side. One map
# (head_pt) places every point of the head, its hair, its hats and the features of its face, so they all stay on one surface. "O": v0.47's ball
HEAD48 = os.environ.get("TPDB_HEAD48", "B")
HEAD48_SHAPE = {"z0": 0.22, "jaw": 0.34, "p": 1.45, "fwd": 0.05}


# v0.49 (TPDB_HEAD49; vision/isolation_v049.md): a head with a jaw and a chin. Sam, of v0.48's cast: "they look a little like bowling pins
# since they do not have chins". The egg narrowed to a rounded point no wider than the neck under it, so the jaw's line ran straight on into
# the neck's. "B": below the middle the head's outline is a superellipse (|z|^m, m over 2: fuller toward the bottom) times the taper, so the
# cheeks come down to a corner and the chin is a rounded shelf wider than the neck; the face's side of the head has the same corner (a chin
# in a side view), the back of the head narrows to the nape on its own (`back`). A head's shape is a dict (HEAD49_SHAPES; a person's spec
# names one), set with set_head before that person is built. "O": v0.48's egg
HEAD49 = os.environ.get("TPDB_HEAD49", "B") if HEAD48 == "B" else "O"
HEAD49_SHAPES = {
    # R: half width, depth and height in units of the head's radius; chin: how far the chin is set below v0.47's, in radii; neck: the neck's
    # radius against v0.48's
    "egg48": {"z0": 0.22, "jaw": 0.34, "p": 1.45, "fwd": 0.05, "m": 2.0, "md": 2.0, "back": 0.0, "R": (0.92, 0.97, 1.06), "neck": 1.0},
    # the round jaw, chosen on the head benches (vision/isolation_v049.md): full cheeks down to a broad, rounded chin. `jawd` and `md` are
    # the taper and the fullness of the face's side of the head; `hy` carries the head forward of the neck and `neck_y` sets the neck's top
    # back, so the underside of the chin lies in front of the neck and its line is drawn across it
    "man": {"z0": 0.05, "jaw": 0.28, "jawd": 0.33, "p": 1.3, "fwd": 0.16, "m": 3.2, "md": 3.0, "R": (0.95, 0.97, 1.03), "neck": 0.90,
            "chin": -0.12, "hy": 0.10, "neck_y": 0.04},
    "woman": {"z0": 0.05, "jaw": 0.34, "jawd": 0.33, "p": 1.3, "fwd": 0.16, "m": 3.0, "md": 3.0, "R": (0.95, 0.97, 1.03), "neck": 0.82,
              "chin": -0.12, "hy": 0.10, "neck_y": 0.04},
    "teen": {"z0": 0.05, "jaw": 0.30, "jawd": 0.33, "p": 1.3, "fwd": 0.16, "m": 3.1, "md": 3.0, "R": (0.96, 0.97, 1.02), "neck": 0.86,
             "chin": -0.13, "hy": 0.10, "neck_y": 0.04},
    "child": {"z0": 0.0, "jaw": 0.20, "jawd": 0.29, "p": 1.3, "fwd": 0.16, "m": 3.0, "md": 3.0, "R": (1.0, 0.98, 1.0), "neck": 0.90,
              "chin": -0.15, "hy": 0.10, "neck_y": 0.04},
}
_HEAD = dict(HEAD49_SHAPES["egg48"])


def set_head(shape=None):
    """The shape of the head being built (a name in HEAD49_SHAPES, a dict of changes to "egg48", or None for v0.48's egg)."""
    _HEAD.clear()
    _HEAD.update(HEAD49_SHAPES["egg48"])
    if isinstance(shape, str):
        _HEAD.update(HEAD49_SHAPES[shape])
    elif shape:
        if shape.get("base"):
            _HEAD.update(HEAD49_SHAPES[shape["base"]])
        _HEAD.update({k: v for k, v in shape.items() if k != "base"})
    return _HEAD


def _box(zs, m):
    """How much fuller than the ball's a superellipse outline |r|^m + |z|^m = 1 is at unit height zs, below the middle."""
    if zs >= 0 or m == 2.0:
        return 1.0
    z = min(0.997, -zs)
    return (1.0 - z ** m) ** (1.0 / m) / math.sqrt(1.0 - z * z)


def _taper(zs, sh, key="jaw"):
    if zs >= sh["z0"]:
        return 1.0
    t = min(1.0, (sh["z0"] - zs) / (sh["z0"] + 1.0))
    return 1.0 - sh[key] * t ** sh["p"]


def head_f(zs, shape=None):
    """The share of the ball's width that the head keeps at unit height zs."""
    if HEAD48 != "B":
        return 1.0
    sh = shape or _HEAD
    f = _taper(zs, sh) * _box(zs, sh.get("m", 2.0))
    if sh.get("cheek"):
        # fuller cheeks: a swell centred a third of the way down the lower face
        t = max(0.0, 1.0 - abs(zs + 0.38) / 0.55)
        f *= 1.0 + sh["cheek"] * t * t * (3 - 2 * t)
    return f


def head_fy(zs, back=False, shape=None):
    """The share of the ball's depth that the head keeps at unit height zs: on the face's side, or (back) behind the ears."""
    if HEAD48 != "B":
        return 1.0
    sh = shape or _HEAD
    if back:
        f = _taper(zs, sh)
        if sh.get("back") and zs < 0:
            f *= 1.0 - sh["back"] * min(1.0, -zs) ** 2
        return f
    return _taper(zs, sh, "jawd" if "jawd" in sh else "jaw") * _box(zs, sh.get("md", 2.0))


def head_g(zs, shape=None):
    """How far forward (in units of the head's half depth) the head is carried at unit height zs."""
    if HEAD48 != "B":
        return 0.0
    sh = shape or _HEAD
    if zs >= sh["z0"]:
        return 0.0
    t = min(1.0, (sh["z0"] - zs) / (sh["z0"] + 1.0))
    return sh["fwd"] * t * t * (3 - 2 * t)


def head_pt(q, shape=None):
    """A point of the unit ball (after squircle) moved to the unit head: scale it by the head's radii afterwards."""
    f = head_f(q[2], shape)
    return Vector((q[0] * f, q[1] * head_fy(q[2], q[1] > 0, shape) - head_g(q[2], shape), q[2]))


def ellipsoid(name, center, radii, matkey, rig=None, bone=None, rot=None, seg=24, rings=14, sq=None, head=None):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=rings, radius=1.0)
    if sq:
        for vv in bm.verts:
            vv.co = squircle(vv.co, sq)
    if head is not None:
        for vv in bm.verts:
            vv.co = head_pt(vv.co, head or None)
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
