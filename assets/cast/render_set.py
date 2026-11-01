"""Render a list of (family, pose, expression, yaw) variants, one Blender process per family.

    python render_set.py <cast_dir> <out_dir> <variants.json> [samples]
variants.json: [["person.ana", "stand", "neutral", 45], ...]
"""
import json
import os
import subprocess
import sys
from collections import defaultdict

cast, out, vfile = sys.argv[1], sys.argv[2], sys.argv[3]
samples = sys.argv[4] if len(sys.argv) > 4 else "16"
here = os.path.dirname(os.path.abspath(__file__))
groups = defaultdict(list)
for fam, pose, expr, yaw in json.load(open(vfile)):
    groups[fam].append([pose, expr, yaw])
os.makedirs(out, exist_ok=True)
for fam, vs in groups.items():
    cfg = json.load(open(os.path.join(cast, fam + ".json")))
    todo = [v for v in vs if not os.path.exists(os.path.join(out, f"{fam}__{v[0]}__{v[1]}__y{int(v[2]):03d}.json"))]
    if not todo:
        continue
    cfg["variants"] = todo
    tmp = os.path.join(out, f".{fam}.{os.getpid()}.cfg.json")   # per process: two generators may render one family at once
    json.dump(cfg, open(tmp, "w"))
    r = subprocess.run([sys.executable, os.path.join(here, "..", "render_assets.py"), "--blend", os.path.join(cast, fam + ".blend"),
                        "--config", tmp, "--out", out, "--samples", samples], capture_output=True, text=True)
    tail = [l for l in r.stdout.splitlines() + r.stderr.splitlines() if "TPDB" in l or "Error" in l and "EGL" not in l or "Traceback" in l]
    print(fam, len(todo), "|", " ".join(tail[-3:]), flush=True)
    os.remove(tmp)
