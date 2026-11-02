#!/usr/bin/env bash
# build_set.sh : the showcase pass into scenes<TAG>, then a seed search for any tier-1 to tier-3 cell it missed.
# Tier-4 cells are searched separately with t4_search.sh (one setting at a time, the previous release's seed first).
# Env: TPDB_VER (e.g. 0.24), TPDB_ROOT, TPDB_WORK (see cfg.py).
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
eval "$(python3 -c "import sys; sys.path.insert(0,'$HERE'); from cfg import ROOT,TAG; print(f'ROOT={ROOT}; TAG={TAG}')")"
cd "$ROOT"
python3 - <<PY
import sys
sys.path.insert(0, "$ROOT")
from scenegen import batch
batch.run_showcase("scenes$TAG")
PY
for cell in garden:1 garden:2 garden:3 park:1 park:2 park:3 street:1 street:2 street:3 playground:1 playground:2 playground:3; do
  st=${cell%%:*}; t=${cell##*:}
  if ! ls scenes$TAG/T${t}_${st}_s*.json 2>/dev/null | grep -v _iso >/dev/null; then
    echo "MISSING $st $t"
    base=$(python3 -c "import sys; sys.path.insert(0,'.'); from scenegen.batch import SHOWCASE; print([s for a,b,s in SHOWCASE if a=='$st' and b==$t][0])")
    python3 "$HERE/search_cell.py" $st $t $((base+100)),$((base+200)),$((base+300)),$((base+400)),$((base+500)),$((base+600)),$((base+700)),$((base+800)),$((base+911)),$((base+921)),$((base+931)),$((base+941)) assets/cast/lib$TAG scenes$TAG
  fi
done
echo SHOWCASE_PASS_DONE
