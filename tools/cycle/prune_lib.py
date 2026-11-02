"""prune_lib.py : move every variant the set and probes do not use out of assets/cast/lib<TAG> (into <WORK>/lib<TAG>_pruned).

Run after verify_all.py (writes <WORK>/variants_used.json) and verify_probes.py (writes variants_used_probes<TAG>.json),
then validate: cd assets && python validate_assets.py cast/lib<TAG>  (move the validation_report.json it writes out of the
library before packaging)."""
import os, sys, json, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG  # noqa: E402

L = os.path.join(ROOT, "assets", "cast", "lib" + TAG)
keep = set(json.load(open(os.path.join(WORK, "variants_used.json")))) | set(json.load(open(os.path.join(WORK, f"variants_used_probes{TAG}.json"))))
dst = os.path.join(WORK, f"lib{TAG}_pruned")
os.makedirs(dst, exist_ok=True)
moved = kept = 0
vids = set()
for f in sorted(os.listdir(L)):
    for suf in (".mask.png", ".json", ".png"):        # variant ids contain dots: strip the known suffix, never split on "."
        if f.endswith(suf):
            v = f[: -len(suf)]
            break
    else:
        print("UNKNOWN", f)
        continue
    vids.add(v)
    if v in keep:
        kept += 1
    else:
        shutil.move(os.path.join(L, f), os.path.join(dst, f))
        moved += 1
print("keep", len(keep), "variants; files kept", kept, "moved", moved, "; missing from the library:", sorted(keep - vids))
