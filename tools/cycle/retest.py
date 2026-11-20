"""(v0.58's own script: its two releases are written in. Edit them.)
retest.py : v0.58's screen beside v0.57's, item for item, in three groups of the pictures that were carried over (vision/v058/carry_over.json,
from tools/cycle/carry_over.py and the count of pixels that differ): those that are v0.57's to the pixel (a second reading), those
that were drawn again or moved with the same templates (what the new drawings changed in the reading), and the rest. Items are matched by
their text, since a redrawn picture may number its items otherwise."""
import collections, json, os
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
kmN = json.load(open("vision/v058/key_map.json")); kmP = json.load(open("vision/v057/key_map.json"))
invN = {v: k for k, v in kmN.items()}; invP = {v: k for k, v in kmP.items()}
sN = json.load(open("vision/v058/scores.json", encoding="utf-8")); sP = json.load(open("vision/v057/scores.json", encoding="utf-8"))
kN = json.load(open("vision/v058/keys.json")); kP = json.load(open("vision/v057/keys.json"))
carry = json.load(open("vision/v058/carry_over.json"))


def val(x):
    v = x["score"] if isinstance(x, dict) else x
    return 0.0 if v == "misread" else float(v)


def by_text(k, s, pic):
    out = collections.defaultdict(list)
    for i in k[pic]["items"]:
        out[i["text"]].append((i["id"], i["type"], val(s[pic]["items"][i["id"]])))
    return out


groups = collections.defaultdict(list)
for old, c in sorted(carry.items()):
    if not c["new"] or c["new"] != old:
        groups["replaced"].append(old); continue
    groups["same" if c["pixels_differ"] == 0 else "drawn or moved"].append(old)
for g in ("same", "drawn or moved"):
    tot = same = up = down = unmatched = 0
    moved = []
    for name in groups[g]:
        a, b = by_text(kN, sN, invN[name]), by_text(kP, sP, invP[name])
        for text in sorted(set(a) | set(b)):
            if text not in a or text not in b or len(a[text]) != len(b[text]):
                unmatched += len(a.get(text, [])) + len(b.get(text, []))
                continue
            for (i1, ty, v1), (i0, _, v0) in zip(a[text], b[text]):
                tot += 1
                if v1 == v0:
                    same += 1
                else:
                    up += v1 > v0; down += v1 < v0
                    moved.append((name, invN[name], i1, v0, v1, ty, text[:70]))
    print("==", g, len(groups[g]), "pictures; items matched", tot, "same", same, "up", up, "down", down, "| items not matched by text", unmatched)
    setting = [m for m in moved if m[5] == "entity" and ("cloud" in m[6] or "tree" in m[6].lower())]
    print("   of the", len(moved), "that moved,", len(setting), "are the clouds or a tree")
    for m in moved:
        if m not in setting:
            print("  ", m)
print("== replaced", groups["replaced"])
