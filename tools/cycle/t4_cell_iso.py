"""t4_cell_iso.py SETTING OUT BASE [N_BASES] [ISO_SEEDS] : a tier-4 cell for SETTING that has an isomorph (v0.57).

The tier-4 isomorph needs a source whose templates each have a second form in another setting (batch.iso_map). v0.57's first new park
held three inferences of one class and had none anywhere, and the street's and the playground's cells had yielded none in 260 tries. So
this searches for the cell and its isomorph together: for each base seed (BASE + k*991 + 13, as t4_search.sh) it builds a free tier-4
cell as search_open.py does; if the cell's set can be cast in another setting it tries ISO_SEEDS seeds (default 30) of the isomorph in
each such setting; and it keeps the pair, or drops the cell and goes on. Everything is built in OUT, a scratch folder of this run's own:
several runs go side by side on other bases, and all stop when one has written OUT/../t4_cell_iso.found. Move the pair into scenes<TAG>
by hand, with the entry it prints for isomorph_summary_t4.json."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import glob, json, random, time
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.generate import build_one
from scenegen.batch import build_isomorph, iso_map
from scenegen.library import Library
from scenegen.planner import USAGE
from scenegen.scene import PlacementError
setting, OUT, base = sys.argv[1], sys.argv[2], int(sys.argv[3])
n_bases = int(sys.argv[4]) if len(sys.argv) > 4 else 30
n_iso = int(sys.argv[5]) if len(sys.argv) > 5 else 30
FLAG = os.path.join(os.path.dirname(OUT.rstrip("/")), "t4_cell_iso.found")
os.makedirs(OUT, exist_ok=True)
lib = Library()
targets = [s for s in ("street", "playground", "park", "garden") if s != setting]
for k in range(n_bases):
    if os.path.exists(FLAG):
        print("FOUND_ELSEWHERE", flush=True); break
    seed = base + k * 991 + 13
    USAGE.clear()
    t0 = time.time()
    rec, sc, fin = build_one(lib, 4, setting, seed, OUT, max_tries=40, log=lambda *a: None)
    if not rec:
        print("seed", seed, f"{time.time() - t0:.0f}s", "no cell", flush=True)
        continue
    ids = [t["id"] for t in rec["templates"]]
    can = []
    for tg in targets:
        ok = 0
        for j in range(6):
            try:
                iso_map(ids, tg, random.Random(j)); ok += 1
            except PlacementError:
                pass
        if ok:
            can.append(tg)
    print("seed", seed, f"{time.time() - t0:.0f}s", "CELL", rec["name"], ids, "can be cast in", can, flush=True)
    found = None
    for j in range(n_iso):
        for tg in can:
            if os.path.exists(FLAG):
                break
            t1 = time.time()
            r = build_isomorph(lib, rec, tg, 6111 + 1000 * j, OUT, log=lambda *x: None)
            if r.get("name"):
                found = r
                break
        if found or os.path.exists(FLAG):
            break
    if found:
        open(FLAG, "w").write(json.dumps({"A": rec["name"], "B": found["name"], "dir": OUT}))
        print("FOUND", rec["name"], "->", found["name"], json.dumps([{"A": rec["name"], "B": found["name"], "check": found["isomorph_check"], "failed": None}]), flush=True)
        break
    for f in glob.glob(os.path.join(OUT, rec["name"] + "*")):
        os.remove(f)
    print("   no isomorph in", n_iso, "seeds: cell dropped", f"{time.time() - t0:.0f}s", flush=True)
print("T4CI_END", flush=True)
