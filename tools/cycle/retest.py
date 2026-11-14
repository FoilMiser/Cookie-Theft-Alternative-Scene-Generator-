"""(v0.55's own script: its two releases are written in. Edit them.)
retest.py : v0.55's screen beside v0.54's, item for item, in two groups of pictures: those that are v0.54's to the pixel (a second reading)
and those that hold a seated figure drawn again (the same templates, people and places: what the new legs changed in the reading)."""
import json, os
from PIL import Image, ImageChops
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
kmN = json.load(open("vision/v055/key_map.json")); kmP = json.load(open("vision/v054/key_map.json"))
inv2 = {v: k for k, v in kmP.items()}
s3 = json.load(open("vision/v055/scores.json")); s2 = json.load(open("vision/v054/scores.json"))
k3 = json.load(open("vision/v055/keys.json")); k2 = json.load(open("vision/v054/keys.json"))


def val(x):
    v = x["score"] if isinstance(x, dict) else x
    return 0.0 if v == "misread" else float(v)


def items_of(k, pic):
    e = k[pic]
    its = e["items"] if isinstance(e, dict) and "items" in e else e
    return {i["id"]: i for i in its}


groups = {"same": [], "changed": []}
for pic, name in sorted(kmN.items()):
    f3 = next(p for p in (f"scenes/{name}.png", f"probes/{name}.png") if os.path.exists(p))
    f2 = next((p for p in (f"scenes_v054/{name}.png", f"probes_v054/{name}.png") if os.path.exists(p)), None)
    if not f2 or name not in inv2:
        print("no v0.54 picture for", pic, name)
        continue
    a, b = Image.open(f3).convert("RGB"), Image.open(f2).convert("RGB")
    ident = a.size == b.size and ImageChops.difference(a, b).getbbox() is None
    groups["same" if ident else "changed"].append((pic, inv2[name], name))
for g, pics in groups.items():
    tot = same = up = down = 0
    moved = []
    for p3, p2, name in pics:
        i3, i2 = items_of(k3, p3), items_of(k2, p2)
        assert set(i3) == set(i2), (p3, p2)
        for iid in sorted(i3):
            a, b = val(s3[p3]["items"][iid]), val(s2[p2]["items"][iid])
            tot += 1
            if a == b:
                same += 1
            else:
                up += a > b; down += a < b
                moved.append((name, p3, iid, b, a, i3[iid].get("type"), (i3[iid].get("target") or i3[iid].get("text") or "")[:70]))
    print("==", g, len(pics), "pictures;", "items", tot, "same", same, "up", up, "down", down,
          "| sum v0.54 %.1f v0.55 %.1f" % (sum(val(s2[p2]["items"][i]) for _, p2, _ in pics for i in s2[p2]["items"]),
                                         sum(val(s3[p3]["items"][i]) for p3, _, _ in pics for i in s3[p3]["items"])))
    for m in moved:
        print("  ", m)
json.dump(groups, open("tpdb_work/v055/same_pics.json", "w"))
