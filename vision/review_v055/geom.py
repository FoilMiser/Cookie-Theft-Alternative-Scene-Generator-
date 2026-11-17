"""geom.py : what the 99 records say of their own pictures, by geometry. Run from the repo root.

1. scored or prop elements partly covered (occlusion >= 0.10) and what covers them
2. elements cut by the picture's edge
3. a figure whose feet are inside the pond's box, or whose box overlaps the pond's
4. depth: a thing drawn in front of another (higher z) whose base is higher up the picture, their boxes overlapping
5. a sitter and its bench: how far the sitter's box reaches past the bench's ends and below its base
6. the square-wheeled thing's place and size in each picture
7. sizes: the height in pixels of each family over the pictures, and the smallest scored things
Writes tpdb_work/review56/geom.json and prints a summary."""
import glob, json, os, collections

W, H = 1600, 1000
recs = {}
for f in sorted(glob.glob("scenes/T*.json")) + sorted(glob.glob("probes/*.json")):
    recs[os.path.basename(f)[:-5]] = json.load(open(f, encoding="utf-8"))
km = {n: p for p, n in json.load(open("vision/v055/key_map.json", encoding="utf-8")).items()}


def box(e):
    return e.get("bbox")


def inter(a, b):
    x0, y0, x1, y1 = max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])
    return max(0, x1 - x0) * max(0, y1 - y0)


def area(a):
    return max(0, a[2] - a[0]) * max(0, a[3] - a[1])


out = collections.defaultdict(list)
fam_h = collections.defaultdict(list)
small = []
for name, r in recs.items():
    els = [e for e in r["elements"] if box(e)]
    by = {e["id"]: e for e in els}
    tids = [t["id"] for t in r["templates"]]
    pond = by.get("pond")
    for e in els:
        b = box(e)
        fam = (e.get("asset") or {}).get("family")
        var = (e.get("asset") or {}).get("variant", "")
        if fam:
            fam_h[fam].append((round(b[3] - b[1]), name, var))
        # 1 covered
        if e.get("role") in ("scored", "prop", "cue") and e.get("occlusion", 0) >= 0.10:
            cov = [(o["id"], round(inter(b, box(o)) / area(b), 2)) for o in els if o is not e and o["z"] > e["z"] and inter(b, box(o)) > 0]
            cov = sorted(cov, key=lambda x: -x[1])[:3]
            out["covered"].append((km[name], name, e["id"], e.get("label", ""), e["occlusion"], cov))
        # 2 cut by the edge
        if e.get("role") in ("scored", "prop", "cue") and (b[0] < 0 or b[1] < 0 or b[2] > W or b[3] > H):
            out["cut"].append((km[name], name, e["id"], e.get("label", ""), [round(x) for x in b]))
        # 3 pond
        if pond and fam and fam.startswith("person") and e is not pond:
            p = box(pond)
            fx, fy = (b[0] + b[2]) / 2, b[3]
            ov = inter(b, p) / area(b)
            feet_in = p[0] <= fx <= p[2] and p[1] <= fy <= p[3]
            if feet_in or ov > 0.05:
                out["pond"].append((km[name], name, e["id"], var, "feet in the pond's box" if feet_in else "", round(ov, 2),
                                    [round(x) for x in b], [round(x) for x in p]))
        # 7 small scored things
        if e.get("role") == "scored" and (b[3] - b[1]) < 46 and (b[2] - b[0]) < 70:
            small.append((round(b[2] - b[0]), round(b[3] - b[1]), km[name], name, e["id"], e.get("label", "")))
    # 4 depth: in front but based higher
    figs = [e for e in els if (e.get("asset") or {}).get("family")]
    for a in figs:
        for b_ in figs:
            if a is b_ or a["z"] <= b_["z"]:
                continue
            A, B = box(a), box(b_)
            if inter(A, B) / min(area(A), area(B)) > 0.08 and A[3] < B[3] - 14 and not (a["asset"].get("labels", {}).get("category") in ("bird",)):
                out["depth"].append((km[name], name, a["id"], b_["id"], round(B[3] - A[3]), round(inter(A, B) / min(area(A), area(B)), 2)))
    # 5 sitters and benches
    for e in els:
        var = (e.get("asset") or {}).get("variant", "")
        if "__sit" in var and "sit_ground" not in var and "swing" not in var:
            bench = None
            for o in els:
                if o["id"].startswith("bench") or o.get("label", "").lower().endswith("bench"):
                    if inter(box(e), box(o)) > 0:
                        bench = o
            b = box(e)
            if bench:
                q = box(bench)
                out["sitter"].append((km[name], name, e["id"], var, "left %d right %d below %d" % (round(q[0] - b[0]), round(b[2] - q[2]), round(b[3] - q[3])),
                                      [round(x) for x in b], [round(x) for x in q], bench.get("occlusion")))
            else:
                out["sitter_no_bench"].append((km[name], name, e["id"], var, [round(x) for x in b]))
    # 6 the square wheel
    if "square_wheel" in tids:
        for e in els:
            if "bicycle" in e.get("label", "").lower() or "bike" in e["id"] or "barrow" in e["id"] or "wheelbarrow" in e.get("label", "").lower():
                b = box(e)
                out["square"].append((km[name], name, e["id"], e.get("label", ""), [round(x) for x in b], round(b[2] - b[0]), round(b[3] - b[1]),
                                      e.get("occlusion"), "tier %d, %d templates" % (r["tier"], len(tids))))

json.dump({k: v for k, v in out.items()}, open("tpdb_work/review56/geom.json", "w", encoding="utf-8"), indent=1)
for k in ("covered", "cut", "pond", "depth", "sitter", "sitter_no_bench", "square"):
    print(f"\n== {k}: {len(out[k])}")
    for x in sorted(out[k]):
        print("  ", x)
print("\n== small scored things:", len(small))
for x in sorted(small)[:40]:
    print("  ", x)
print("\n== heights by family (min, median, max px; n)")
for fam, hs in sorted(fam_h.items()):
    v = sorted(h for h, _, _ in hs)
    print("  ", fam, v[0], v[len(v) // 2], v[-1], len(v))
