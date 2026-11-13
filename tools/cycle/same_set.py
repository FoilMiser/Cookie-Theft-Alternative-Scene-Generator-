"""same_set.py NEW_DIR OLD_DIR [PX] : did the pictures of one folder come back from another release's? (v0.52)
For every record of NEW_DIR that OLD_DIR holds under the same name: are the templates the same, are the cast's variants the same, and does every
figure stand within PX pixels (default 12) of where it stood. A release that changes the cast by a few pixels of outline, and no rule, can bring
the whole set back, and its screen is then a second reading of the last one."""
import glob, json, os, sys
new, old = sys.argv[1], sys.argv[2]
px = float(sys.argv[3]) if len(sys.argv) > 3 else 12.0
n = same_t = same_c = same_p = 0
for f in sorted(glob.glob(os.path.join(new, "T*.json"))):
    name = os.path.basename(f)
    g = os.path.join(old, name)
    if not os.path.exists(g):
        print(name, "not in", old)
        continue
    a, b = json.load(open(f, encoding="utf-8")), json.load(open(g, encoding="utf-8"))
    n += 1
    ta, tb = [t["id"] for t in a["templates"]], [t["id"] for t in b["templates"]]
    ea = sorted(((e.get("asset") or {}).get("variant", ""), [round(x) for x in e.get("bbox", [])]) for e in a["elements"] if e.get("asset"))
    eb = sorted(((e.get("asset") or {}).get("variant", ""), [round(x) for x in e.get("bbox", [])]) for e in b["elements"] if e.get("asset"))
    va, vb = [x[0] for x in ea], [x[0] for x in eb]
    near = va == vb and all(max(abs(p - q) for p, q in zip(x[1], y[1])) <= px for x, y in zip(ea, eb))
    same_t += ta == tb
    same_c += va == vb
    same_p += near
    if not (ta == tb and near):
        print(name, "templates same" if ta == tb else "TEMPLATES DIFFER", "cast same" if va == vb else "CAST DIFFERS", "" if near else "places differ")
print(f"{n} records of {new} are in {old}: templates the same in {same_t}, the cast in {same_c}, every figure within {px:g} px in {same_p}")
