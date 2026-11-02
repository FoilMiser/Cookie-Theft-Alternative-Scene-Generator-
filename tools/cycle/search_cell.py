"""search9.py setting tier seeds libdir out : find a showcase seed for one (setting, tier) (batch rules, LOCAL_VARIETY honoured)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import os, sys, glob, time
sys.path.insert(0, ROOT); os.chdir(ROOT)
import scenegen.library as L
setting, tier, seeds, libdir, OUT = sys.argv[1], int(sys.argv[2]), [int(x) for x in sys.argv[3].split(",")], os.path.abspath(sys.argv[4]), sys.argv[5]
L.Library.__init__.__defaults__ = (L.CAST_DIR, libdir, 10)
from scenegen import batch
from scenegen.planner import USAGE
for seed in seeds:
    USAGE.clear()
    t0 = time.time()
    batch.SHOWCASE[:] = [(setting, tier, seed)]
    batch.run_showcase(OUT, [f"{setting}{tier}"])
    hits = [f for f in glob.glob(f"{OUT}/T{tier}_{setting}_s*.json") if not f.endswith("_iso.json")]
    print("seed", seed, f"{time.time() - t0:.0f}s", flush=True)
    if hits:
        print("OK", seed, hits, flush=True)
        break
print("SEARCH_END", flush=True)
