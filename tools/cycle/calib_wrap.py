"""Run scenegen.calibrate against a scratch copy of the variant library (so lib6 keeps only set variants)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import os, sys, shutil
sys.path.insert(0, ROOT); os.chdir(ROOT)
S = WORK
LC = os.path.join(ROOT, "assets", "cast", "lib" + TAG)
os.makedirs(LC, exist_ok=True)
from scenegen import library as L
L.Library.__init__.__defaults__ = (L.CAST_DIR, LC, 10)
from scenegen import calibrate
calibrate.run(2, 3, os.path.join(S, f"calibration{TAG}.json"), None)
