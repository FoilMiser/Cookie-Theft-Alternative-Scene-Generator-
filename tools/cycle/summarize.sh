#!/usr/bin/env bash
# summarize.sh : add this release's screen to vision/screen_summary.json. Run after the folder swap (scenes<PREV> ->
# scenes_v<PREV>, scenes<TAG> -> scenes; the same for probes) and after merging scores_a/b/c into scores.json.
set -u
HERE=$(cd "$(dirname "$0")" && { pwd -W 2>/dev/null || pwd; })   # (Git Bash: a path Windows Python can read)
eval "$(python3 -c "import sys; sys.path.insert(0,'$HERE'); from cfg import ROOT,TAG; print(f'ROOT={ROOT}; TAG={TAG}')")"
cd "$ROOT"
python3 vision/summarize_screen.py --add vision/v$TAG:scenes,probes
