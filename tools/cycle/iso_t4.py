import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import os, sys, json, glob, time
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.batch import build_isomorph
from scenegen.library import Library
OUT = f"scenes{TAG}"
names = {}
for f in glob.glob(OUT + "/T4_*.json"):
    r = json.load(open(f))
    if not r.get("isomorph_of"):
        names[r["setting"]] = r["name"]
pairs = [(a, b) for a in ("park", "playground", "garden", "street") for b in ("park", "street", "playground", "garden") if a != b and a in names]
lib = Library()
res = json.load(open(os.path.join(OUT, "isomorph_summary.json"))) if os.path.exists(os.path.join(OUT, "isomorph_summary.json")) else []
for seed in [int(x) for x in sys.argv[1].split(",")]:
    for a, b in pairs:
        if glob.glob(OUT + "/T4_*_iso.json"):
            print("FOUND", flush=True); sys.exit()
        rec_a = json.load(open(os.path.join(OUT, names[a] + ".json")))
        t0 = time.time()
        r = build_isomorph(lib, rec_a, b, seed, OUT, log=lambda *x: None)
        print("ISO", names[a], b, seed, "->", r.get("name"), json.dumps(r.get("isomorph_check", r.get("failed")))[:150], f"{time.time() - t0:.0f}s", flush=True)
        if r.get("name"):
            res.append({"A": names[a], "B": r["name"], "check": r["isomorph_check"], "failed": None})
            json.dump(res, open(os.path.join(OUT, "isomorph_summary.json"), "w"), indent=1)
            sys.exit()
print("ISO_T4_END", flush=True)
