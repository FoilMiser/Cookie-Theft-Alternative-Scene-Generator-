"""(v0.54's own script: its two releases are written in. Edit them.)
retest.py : the pictures of v0.54's screen that are v0.53's to the pixel, their items compared score for score with v0.53's screen."""
import glob, json, os, collections
from PIL import Image, ImageChops
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
kmN = json.load(open("vision/v054/key_map.json")); kmP = json.load(open("vision/v053/key_map.json"))
inv2 = {v: k for k, v in kmP.items()}
s3 = json.load(open("vision/v054/scores.json")); s2 = json.load(open("vision/v053/scores.json"))
k3 = json.load(open("vision/v054/keys.json")); k2 = json.load(open("vision/v053/keys.json"))
def val(x):
    v = x["score"] if isinstance(x, dict) else x
    return 0.0 if v == "misread" else float(v)
same_pics = []
for pic, name in sorted(kmN.items()):
    f3 = next(p for p in (f"scenes/{name}.png", f"probes/{name}.png") if os.path.exists(p))
    f2 = next((p for p in (f"scenes_v053/{name}.png", f"probes_v053/{name}.png") if os.path.exists(p)), None)
    if not f2 or name not in inv2:
        continue
    a, b = Image.open(f3).convert("RGB"), Image.open(f2).convert("RGB")
    if a.size == b.size and ImageChops.difference(a, b).getbbox() is None:
        same_pics.append((pic, inv2[name], name))
print(len(same_pics), "pictures identical to v0.53's")
tot = same = up = down = 0
moved = []
def items_of(k, pic):
    e = k[pic]
    its = e["items"] if isinstance(e, dict) and "items" in e else e
    return {i["id"]: i for i in its}
for p3, p2, name in same_pics:
    i3, i2 = items_of(k3, p3), items_of(k2, p2)
    assert set(i3) == set(i2), (p3, p2)
    for iid in sorted(i3):
        a, b = val(s3[p3]["items"][iid]), val(s2[p2]["items"][iid])
        tot += 1
        if a == b: same += 1
        else:
            up += a > b; down += a < b
            moved.append((name, p3, p2, iid, b, a, i3[iid].get("type"), (i3[iid].get("target") or i3[iid].get("text") or "")[:70]))
print("items", tot, "same", same, "up", up, "down", down)
for m in moved:
    print("  ", m)
json.dump(same_pics, open("tpdb_work/v054/same_pics.json", "w"))
