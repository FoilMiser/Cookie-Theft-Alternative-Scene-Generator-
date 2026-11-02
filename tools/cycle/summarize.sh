#!/usr/bin/env bash
# summarize.sh : vision/screen_summary.json over every screen from v0.4 to the current one. Run after the folder swap
# (scenes<PREV> -> scenes_v<PREV>, scenes<TAG> -> scenes; the same for probes) and after merging scores_a/b/c into scores.json.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
eval "$(python3 -c "import sys; sys.path.insert(0,'$HERE'); from cfg import ROOT,TAG,MINOR; print(f'ROOT={ROOT}; TAG={TAG}; MINOR={MINOR}')")"
cd "$ROOT"
args="vision/v04:scenes_v04 vision/v05:scenes_v05"
for m in $(seq 6 $((MINOR-1))); do
  if [ $m -lt 10 ]; then v=0$m; else v=0$m; fi
  args="$args vision/v$v:scenes_v$v,probes_v$v"
done
python3 vision/summarize_screen.py $args vision/v$TAG:scenes,probes
