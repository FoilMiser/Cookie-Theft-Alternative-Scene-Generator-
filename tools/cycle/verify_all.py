"""verify_all.py DIR... : rebuild every record from its JSON, compare pixels, and log every variant the
rebuild asks for (so lib6 can be pruned to exactly what exact rebuilds need)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, os, sys, glob, shutil
sys.path.insert(0, ROOT); os.chdir(ROOT)
from PIL import Image, ImageChops
from scenegen import generate as G
from scenegen.library import Library, vid
S = WORK
OUT = os.path.join(S, "verify")
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
used = set()
lib = Library()
orig = lib.ensure
def ensure(variants, log=print):
    for v in variants:
        used.add(vid(*v))
    return orig(variants, log)
lib.ensure = ensure
ok = bad = 0
for d in sys.argv[1:]:
    recs = sorted(glob.glob(os.path.join(d, "T*.json")))
    # isomorphs read their source record from the same folder: copy the folder's records alongside
    for f in recs:
        r = json.load(open(f))
        n = r["name"]
        G.regenerate(lib, f, OUT)
        p = os.path.join(OUT, n + ".png")
        if not os.path.exists(p):
            print(n, "MISSING", flush=True); bad += 1; continue
        same = ImageChops.difference(Image.open(os.path.join(d, n + ".png")).convert("RGB"), Image.open(p).convert("RGB")).getbbox() is None
        print(n, "IDENTICAL" if same else "DIFFERENT", flush=True)
        ok += same; bad += (not same)
        # every element variant of the final picture too
        for e in r["elements"]:
            if e.get("asset"):
                used.add(e["asset"]["variant"])
json.dump(sorted(used), open(os.path.join(S, "variants_used.json"), "w"))
print("VERIFY_END", ok, "identical,", bad, "not", len(used), "variants used", flush=True)
