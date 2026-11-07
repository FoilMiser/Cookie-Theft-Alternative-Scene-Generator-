"""Prepare a blind legibility screen: anonymized copies of every picture plus the scoring key.

    python vision/prepare_screen.py scenes vision/v05
    python vision/prepare_screen.py scenes,probes vision/v06      # several folders, shuffled together

Writes <out>/blind/pic_NN.png (no file names, records or code nearby), <out>/key_map.json
(pic -> scene name) and <out>/keys.json (pic -> scored items with accepted phrasings).
Describers get only the blind images; a separate scorer gets their descriptions and keys.json.
"""
import glob
import json
import os
import random
import shutil
import sys

srcs, out = sys.argv[1].split(","), sys.argv[2]
os.makedirs(os.path.join(out, "blind"), exist_ok=True)
where = {}
for src in srcs:
    for p in glob.glob(os.path.join(src, "T*.png")):
        if not p.endswith(("_gray.png", "_thumb.png", "_t.png")):
            where[os.path.basename(p)[:-4]] = src
names = sorted(where)
random.Random(5).shuffle(names)
key_map, keys = {}, {}
ANGLE = {0: "facing the viewer", 45: "three-quarter front", 90: "profile", 135: "three-quarter back"}
for i, n in enumerate(names, 1):
    k = f"pic_{i:02d}"
    key_map[k] = n
    src = where[n]
    shutil.copy(os.path.join(src, n + ".png"), os.path.join(out, "blind", k + ".png"))
    r = json.load(open(os.path.join(src, n + ".json")))
    keys[k] = {"items": [{"id": it["id"], "type": it["type"], "text": it["text"],
                          "accepted": (it["accepted"] if isinstance(it["accepted"], list) else it["accepted"].get("what", []))[:8]}
                         for it in r["items"]]}
    # (v0.39: every animal drawn, with its angle, for the scorers' oddity tally by angle)
    an = []
    for e in r.get("elements", []):
        a = e.get("asset") or {}
        if a.get("family", "").startswith("animal.") and "__y" in a.get("variant", ""):
            x = {"animal": a.get("labels", {}).get("everyday_name", a["family"][7:]), "angle": ANGLE.get(int(a["variant"].rsplit("__y", 1)[1]), "?")}
            if x not in an:
                an.append(x)
    if an:
        keys[k]["animals"] = an
json.dump(key_map, open(os.path.join(out, "key_map.json"), "w"), indent=1)
json.dump(keys, open(os.path.join(out, "keys.json"), "w"), indent=1)
print(len(names), "pictures,", sum(len(v["items"]) for v in keys.values()), "items")
