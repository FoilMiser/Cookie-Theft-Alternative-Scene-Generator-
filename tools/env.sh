# Source this from Git Bash (Windows) or bash (Linux) before any command in RUNBOOK.md:
#     source tools/env.sh
# Activates .venv (`python -m venv .venv && pip install -r requirements.txt` makes it), reads and writes text as
# UTF-8 on Windows too, and sets the release being built and the scratch folder (see tools/cycle/cfg.py).
TPDB_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && { pwd -W 2>/dev/null || pwd; })   # (Git Bash: a path Windows Python can read)
export TPDB_ROOT
if [ -f "$TPDB_ROOT/.venv/Scripts/activate" ]; then . "$TPDB_ROOT/.venv/Scripts/activate"; else . "$TPDB_ROOT/.venv/bin/activate"; fi
export PYTHONUTF8=1
export TPDB_VER=${TPDB_VER:-0.48}
export TPDB_WORK=${TPDB_WORK:-$TPDB_ROOT/tpdb_work}
# The scripts and the runbook say python3; on Windows that name is the Microsoft Store stub.
python3() { python "$@"; }
export -f python3
