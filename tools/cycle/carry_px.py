"""(v0.57's own script: run before the folders are swapped, when the new pictures are in scenes057 and probes057.)
carry_px.py : for every record that tools/cycle/carry_over.py carried over, how many pixels differ from v0.56's picture (0, a handful, or a drawing)."""
import json, os, collections
from PIL import Image, ImageChops
out = {}
for src, dst in (("scenes", "scenes057"), ("probes", "probes057")):
    st = json.load(open(dst + "/carry_over.json"))
    for name, v in sorted(st.items()):
        if not v["new"] or v["new"] != name:
            out[name] = (v["verdict"], None); continue
        a, b = Image.open(f"{src}/{name}.png").convert("RGB"), Image.open(f"{dst}/{name}.png").convert("RGB")
        d = ImageChops.difference(a, b).convert("L").point(lambda x: 255 if x else 0)
        n = sum(d.histogram()[1:])
        out[name] = (v["verdict"], n)
json.dump(out, open("tpdb_work/v057/carry_px.json", "w"), indent=1)
c = collections.Counter()
for name, (v, n) in out.items():
    c["failed/other" if n is None else "0" if n == 0 else "1-20" if n <= 20 else "21-400" if n <= 400 else ">400"] += 1
print(dict(c))
print("small:", [(k, v[1]) for k, v in out.items() if v[1] and v[1] <= 400])
