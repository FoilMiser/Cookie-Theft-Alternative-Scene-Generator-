"""iso_one.py SRC_NAME TARGET SEED OUT : one isomorph call into a scratch folder, to price a placement switch that is read from the environment.
Run it twice, the switch on and off (`TPDB_EDGE49=O python tools/cycle/iso_one.py T4_park_s728923 street 164111 <WORK>/iso_o`), on last
release's isomorph and its own seed: v0.49 learned in half a minute from this what 361 calls of the wide search had not said, that the edge
rule and not the cast kept the tier-4 isomorph from building. SRC_NAME is a record of scenes<TAG> (or of scenes, after the swap)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, TAG  # noqa: E402
import json, time
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.batch import build_isomorph
from scenegen.library import Library
src, target, seed, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
os.makedirs(out, exist_ok=True)
rec = json.load(open(next(p for p in (f"scenes{TAG}/{src}.json", f"scenes/{src}.json") if os.path.exists(p))))
t0 = time.time()
r = build_isomorph(Library(), rec, target, seed, out, log=lambda *x: None)
print("ISO1", src, target, seed, "->", r.get("name"), json.dumps(r.get("failed") or [])[:300], "%ds" % (time.time() - t0), flush=True)
