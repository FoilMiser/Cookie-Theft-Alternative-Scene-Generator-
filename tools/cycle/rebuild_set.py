"""rebuild_set.py DIR : rebuild every record of a folder in place under the code as it now is, after a change to shared drawing. Pictures first, then the isomorphs that read them.
Says which changed, and which no longer come out under their own name. Afterwards refresh isomorph_summary.json's checks from the records."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK  # noqa: E402
import glob, json, shutil, sys
sys.path.insert(0, ROOT); os.chdir(ROOT)
from PIL import Image, ImageChops
from scenegen import generate as G
from scenegen.library import Library

d = sys.argv[1]
tmp = os.path.join(WORK, "rebuild_set", os.path.basename(d))
shutil.rmtree(tmp, ignore_errors=True)
os.makedirs(tmp)
lib = Library()
for f in sorted(glob.glob(os.path.join(d, "T*.json")), key=lambda f: ("_iso" in f, f)):
    n = os.path.basename(f)[:-5]
    old = json.load(open(f, encoding="utf-8"))
    G.regenerate(lib, f, tmp)
    p = os.path.join(tmp, n + ".png")
    if not os.path.exists(p):
        print(n, "NOT REBUILT", flush=True)
        continue
    same = ImageChops.difference(Image.open(os.path.join(d, n + ".png")).convert("RGB"), Image.open(p).convert("RGB")).getbbox() is None
    new = json.load(open(os.path.join(tmp, n + ".json"), encoding="utf-8"))
    if old.get("probe"):
        new["probe"] = True
        json.dump(new, open(os.path.join(tmp, n + ".json"), "w"), indent=1)
    ni, oi = [i["text"] for i in new["items"]], [i["text"] for i in old["items"]]
    for fn in glob.glob(os.path.join(tmp, n + "*")):
        shutil.copy(fn, os.path.join(d, os.path.basename(fn)))
    print(n, "identical" if same else "changed", "items same" if ni == oi else f"ITEMS {sorted(set(ni) ^ set(oi))}", "in_tier", new.get("in_tier"), flush=True)
print("REBUILD_END", flush=True)
