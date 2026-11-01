"""Find body parts that come apart in a pose.

    python gapcheck.py <cast_dir> <family> [pose ...]     (run from assets/cast; prints GAPJSON {...})

For every pose of a family, the visible body meshes (props except hand parts left out) are split into
mesh islands, two islands are joined when their surfaces touch or cross, or one lies inside the other,
and any pose whose body falls into more than one group is reported with the islands that float free
and how far they are from the rest.
"""
import json
import math
import os
import sys

import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree

cast, fam = sys.argv[1], sys.argv[2]
only = set(sys.argv[3:])
cfg = json.load(open(os.path.join(cast, fam + ".json")))
bpy.ops.wm.open_mainfile(filepath=os.path.join(cast, fam + ".blend"))

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, ".."))
import render_assets as RA  # noqa: E402

root = bpy.data.objects[cfg.get("root", "ROOT")]
HANDPART = ("fing", "palm", "thumb")
EPS = 0.0015


def body_objects():
    out = []
    for o in RA.asset_objects(root):
        if o.type not in ("MESH", "CURVE") or o.hide_render:
            continue
        n = o.name
        if n.startswith("ANCHOR_") or n.startswith("F_"):
            continue
        if n.startswith("PROP_"):
            tail = n.split("_")[-1]
            if not tail.startswith(HANDPART):
                continue
        out.append(o)
    return out


def islands(o, dg):
    ev = o.evaluated_get(dg)
    me = ev.to_mesh()
    M = o.matrix_world
    vs = [M @ v.co for v in me.vertices]
    parent = list(range(len(vs)))

    def f(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for e in me.edges:
        a, b = f(e.vertices[0]), f(e.vertices[1])
        if a != b:
            parent[a] = b
    groups = {}
    for i in range(len(vs)):
        groups.setdefault(f(i), []).append(i)
    polys = [list(p.vertices) for p in me.polygons]
    out = []
    for g in groups.values():
        gs = set(g)
        remap = {v: k for k, v in enumerate(g)}
        pp = [[remap[v] for v in p] for p in polys if p[0] in gs]
        pts = [vs[v] for v in g]
        if not pp or len(pts) < 4:
            continue
        out.append({"obj": o.name, "n": len(pts), "pts": pts,
                    "bvh": BVHTree.FromPolygons(pts, pp, epsilon=EPS)})
    ev.to_mesh_clear()
    return out


def inside(p, tree):
    """Odd number of crossings along +Z means p is inside the closed surface."""
    n, o, d = 0, Vector(p), Vector((0.0013, 0.0007, 1.0)).normalized()
    for _ in range(64):
        hit = tree.ray_cast(o, d, 10.0)
        if hit[0] is None:
            break
        n += 1
        o = hit[0] + d * 1e-5
    return n % 2 == 1


def gap(a, b):
    best = 9.0
    step = max(1, len(a["pts"]) // 400)
    for p in a["pts"][::step]:
        r = b["bvh"].find_nearest(p)
        if r[0] is not None:
            best = min(best, r[3])
    return best


def check_pose(pname):
    RA.apply_pose(root, cfg["poses"][pname])
    RA.apply_pose_objects(cfg, pname)
    if cfg.get("expression_states"):
        RA.apply_expression_states(cfg["expression_states"], "neutral" if "neutral" in cfg["expression_states"] else list(cfg["expression_states"])[0])
    bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    isl = []
    for o in body_objects():
        isl += islands(o, dg)
    n = len(isl)
    parent = list(range(n))

    def f(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i in range(n):
        for j in range(i + 1, n):
            if f(i) == f(j):
                continue
            a, b = isl[i], isl[j]
            if a["bvh"].overlap(b["bvh"]) or inside(a["pts"][0], b["bvh"]) or inside(b["pts"][0], a["bvh"]):
                parent[f(i)] = f(j)
    comps = {}
    for i in range(n):
        comps.setdefault(f(i), []).append(i)
    if len(comps) <= 1:
        return None
    main = max(comps.values(), key=lambda c: sum(isl[i]["n"] for i in c))
    loose = []
    for c in comps.values():
        if c is main:
            continue
        cs = set(c)
        d = min(gap(isl[i], isl[j]) for i in c for j in range(n) if j not in cs)   # to the nearest other part
        loose.append({"parts": sorted({isl[i]["obj"] for i in c}), "gap_mm": round(d * 1000, 1)})
    return loose


report = {}
for pname in cfg["poses"]:
    if only and pname not in only:
        continue
    r = check_pose(pname)
    if r:
        report[pname] = r
print("GAPJSON " + json.dumps({"family": fam, "loose": report}))
