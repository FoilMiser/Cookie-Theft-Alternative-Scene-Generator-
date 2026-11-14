"""pixcmp.py DIR_A DIR_B [DIR_B2 ...] : which records' pictures in DIR_A are identical to the pixel to the picture of the same name in DIR_B (or B2 ...)."""
import glob, json, os, sys
from PIL import Image, ImageChops
os.chdir("E:/Cognitive_Test_Scene_Creator")
A, Bs = sys.argv[1], sys.argv[2:]
same, diff, new = [], [], []
for f in sorted(glob.glob(A + "/T*.json")):
    name = os.path.basename(f)[:-5]
    fb = next((f"{b}/{name}.png" for b in Bs if os.path.exists(f"{b}/{name}.png")), None)
    if not fb:
        new.append(name); continue
    a, b = Image.open(f"{A}/{name}.png").convert("RGB"), Image.open(fb).convert("RGB")
    if a.size == b.size and ImageChops.difference(a, b).getbbox() is None:
        same.append(name)
    else:
        bb = ImageChops.difference(a, b).getbbox() if a.size == b.size else None
        diff.append((name, bb))
print(len(same), "identical;", len(diff), "differ:", diff, ";", len(new), "new:", new)
json.dump({"same": same, "diff": [d[0] for d in diff], "new": new}, open("tpdb_work/v054/pix_%s.json" % os.path.basename(A), "w"), indent=1)
