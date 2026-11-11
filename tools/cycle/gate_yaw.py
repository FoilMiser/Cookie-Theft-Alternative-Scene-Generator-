"""gate_yaw.py vision/v<TAG> scenes,probes : the gate per (template, angle) for the templates whose animal is drawn at more than one angle
(templates.yaw_table()), and the scorers' oddities about animals by angle. Writes <screen>/gate_yaw.json. Run after vision/gate.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections
import json
import os
import re
import sys

sys.path.insert(0, ROOT)
os.chdir(ROOT)
from scenegen import templates as TT

MEAN, PICTURES = 0.9, 2
screen, dirs = sys.argv[1], sys.argv[2].split(",")
km = json.load(open(os.path.join(screen, "key_map.json")))
sc = json.load(open(os.path.join(screen, "scores.json")))


def record(name):
    for d in dirs:
        f = os.path.join(d, name + ".json")
        if os.path.exists(f):
            return json.load(open(f))
    return None


vals, pics, mis, low = (collections.defaultdict(list), collections.defaultdict(set), collections.Counter(), collections.defaultdict(list))
for pic, name in km.items():
    r = record(name)
    if r is None:
        continue
    els = {e["id"]: e for e in r["elements"]}
    for it in r["items"]:
        t = it.get("template")
        if t not in TT.yaw_table():
            continue
        ys = set()
        for i in it.get("elements", []):
            a = els.get(i, {}).get("asset") or {}
            if a.get("family", "").startswith("animal.") and "__y" in a.get("variant", ""):
                ys.add(int(a["variant"].rsplit("__y", 1)[1]))
        # (an item names the template's animal, or else it takes the yaw of the template's other items in this picture)
        if not ys:
            for it2 in r["items"]:
                if it2.get("template") == t:
                    for i in it2.get("elements", []):
                        a = els.get(i, {}).get("asset") or {}
                        if a.get("family", "").startswith("animal.") and "__y" in a.get("variant", ""):
                            ys.add(int(a["variant"].rsplit("__y", 1)[1]))
        v = sc.get(pic, {}).get("items", {}).get(it["id"], {}).get("score", 0)
        bad = isinstance(v, str)
        v = 0.0 if bad else float(v)
        for y in ys or {None}:
            vals[(t, y)].append(v)
            pics[(t, y)].add(pic)
            mis[(t, y)] += bad
            if v < 1:
                low[(t, y)].append(f"{pic} {it['id']} {v if not bad else 'misread'}")
out = {}
print(f"{'template':18} {'yaw':>4} {'mean':>6} {'items':>5} {'pics':>4} {'mis':>3}  status")
for t, ys in TT.yaw_table().items():
    for y in [y for y in ys if (t, y) not in TT.UNPLACED] + [None]:
        if (t, y) not in vals and y is None:
            continue
        n = len(vals[(t, y)])
        m = sum(vals[(t, y)]) / n if n else None
        status = "none" if not n else "pass" if m >= MEAN and len(pics[(t, y)]) >= PICTURES and mis[(t, y)] == 0 else (
            "too_few" if m >= MEAN and mis[(t, y)] == 0 else "fail")
        out[f"{t}@{y}"] = {"mean": None if m is None else round(m, 3), "items": n, "pictures": len(pics[(t, y)]), "misreads": mis[(t, y)],
                           "status": status, "below_1": low[(t, y)], "pics": sorted(pics[(t, y)])}
        print(f"{t:18} {str(y):>4} {('-' if m is None else f'{m:.3f}'):>6} {n:>5} {len(pics[(t, y)]):>4} {mis[(t, y)]:>3}  {status}"
              + (f"  {low[(t, y)]}" if low[(t, y)] else ""))
odd = collections.Counter()
odd_txt = collections.defaultdict(list)
for pic, v in sc.items():
    for u in v.get("unintended", []):
        m = re.search(r"\[([^\]]+),\s*([^\]]+)\]\s*$", u)
        if m:
            odd[(m.group(1).strip(), m.group(2).strip())] += 1
            odd_txt[(m.group(1).strip(), m.group(2).strip())].append(f"{pic}: {u}")
print("\nanimal oddities by angle:")
for k, n in sorted(odd.items()):
    print(" ", k, n)
    for s in odd_txt[k]:
        print("     ", s[:200])
json.dump({"gate": out, "oddities_by_angle": {f"{a} @ {b}": odd_txt[(a, b)] for a, b in odd}}, open(os.path.join(screen, "gate_yaw.json"), "w"),
          indent=1)
