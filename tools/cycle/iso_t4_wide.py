"""iso_t4_wide.py SEED,SEED,... : a wider search for the tier-4 isomorph when iso_t4.py finds none (from v0.47). Only the pairs that can build:
edit `pairs` from the isomorph classes of the release's tier-4 cells (batch.iso_key; ice_cream_drop has no garden form, and blocked_hose and
paint_tracks none outside the garden), the roomier target first. Try the previous release's seed first when the cell's templates are the same.
Stops when the set holds a T4_*_iso.json; several lists can run side by side. Writes scenes<TAG>/isomorph_summary_t4.json."""
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
pairs = [("street", "park"), ("playground", "park"), ("park", "street"), ("park", "playground"), ("street", "playground"), ("playground", "street")]
lib = Library()
for seed in [int(x) for x in sys.argv[1].split(",")]:
    for a, b in pairs:
        if glob.glob(OUT + "/T4_*_iso.json"):
            print("FOUND", flush=True); sys.exit()
        rec_a = json.load(open(os.path.join(OUT, names[a] + ".json")))
        t0 = time.time()
        r = build_isomorph(lib, rec_a, b, seed, OUT, log=lambda *x: None)
        fl = r.get("failed") or []
        placed = sum(1 for n in fl if n.startswith("knob"))
        print("ISO", names[a], b, seed, "->", r.get("name"), "placed notes", placed, json.dumps(r.get("isomorph_check", fl[-3:]))[:200], f"{time.time() - t0:.0f}s", flush=True)
        if r.get("name"):
            json.dump([{"A": names[a], "B": r["name"], "check": r["isomorph_check"], "failed": None}],
                      open(os.path.join(OUT, "isomorph_summary_t4.json"), "w"), indent=1)
            print("FOUND", flush=True); sys.exit()
print("ISO_T4_END", flush=True)
