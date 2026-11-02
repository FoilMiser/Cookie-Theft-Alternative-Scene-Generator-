"""verify_some.py PATH.json... : rebuild the given records with the current code and compare pixels (paths relative to the package root)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, os, sys, shutil
sys.path.insert(0, ROOT); os.chdir(ROOT)
from PIL import Image, ImageChops
from scenegen import generate as G
from scenegen.library import Library
lib = Library()
OUT = os.path.join(WORK, "vsome")
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
for p in sys.argv[1:]:
    r = json.load(open(p))
    G.regenerate(lib, p, OUT)
    a = Image.open(p[:-5] + ".png").convert("RGB")
    b = Image.open(os.path.join(OUT, r["name"] + ".png")).convert("RGB")
    print(r["name"], "IDENTICAL" if a.size == b.size and ImageChops.difference(a, b).getbbox() is None else "DIFFERENT", flush=True)
