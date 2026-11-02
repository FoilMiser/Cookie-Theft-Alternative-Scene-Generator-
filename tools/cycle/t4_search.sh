#!/usr/bin/env bash
# t4_search.sh SETTING FIRST_SEED BASE : a tier-4 cell for SETTING into scenes<TAG>, trying FIRST_SEED (the previous
# release's base seed, from its scenes/showcase_summary.json) first, then 44 seeds BASE + k*991 + 13. Stops as soon as the
# cell exists (so two searches for one cell, or the showcase pass, never both add one).
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
eval "$(python3 -c "import sys; sys.path.insert(0,'$HERE'); from cfg import ROOT,TAG; print(f'ROOT={ROOT}; TAG={TAG}')")"
cd "$ROOT"
st=$1; first=$2; base=$3
seeds=$(python3 -c "print(','.join(['$first'] + [str($base+k*991+13) for k in range(1,45)]))")
python3 "$HERE/search_open.py" $st 4 $seeds scenes$TAG
