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
for i, n in enumerate(names, 1):
    k = f"pic_{i:02d}"
    key_map[k] = n
    src = where[n]
    shutil.copy(os.path.join(src, n + ".png"), os.path.join(out, "blind", k + ".png"))
    r = json.load(open(os.path.join(src, n + ".json")))
    keys[k] = {"items": [{"id": it["id"], "type": it["type"], "text": it["text"],
                          "accepted": (it["accepted"] if isinstance(it["accepted"], list) else it["accepted"].get("what", []))[:8]}
                         for it in r["items"]]}
json.dump(key_map, open(os.path.join(out, "key_map.json"), "w"), indent=1)
json.dump(keys, open(os.path.join(out, "keys.json"), "w"), indent=1)
print(len(names), "pictures,", sum(len(v["items"]) for v in keys.values()), "items")
