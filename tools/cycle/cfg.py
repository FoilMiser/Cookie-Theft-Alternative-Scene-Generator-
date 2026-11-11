"""Shared settings for the release-cycle scripts in tools/cycle (see RUNBOOK.md at the repo root).

    TPDB_VER   the release being built, e.g. 0.24 (default below); TAG is its folder suffix ("024")
    TPDB_ROOT  the package root (default: two folders above this file)
    TPDB_WORK  a scratch folder for logs, variant lists and prompts (default: <ROOT>/../tpdb_work)
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("TPDB_ROOT", os.path.dirname(os.path.dirname(HERE)))
WORK = os.environ.get("TPDB_WORK", os.path.join(os.path.dirname(ROOT), "tpdb_work"))
VER = os.environ.get("TPDB_VER", "0.47")
MINOR = int(VER.split(".")[1])
TAG = f"0{MINOR}"              # scenes024, probes024, lib024, out024, gallery024, vision/v024
PREV = f"0{MINOR - 1}"         # the release before
os.makedirs(WORK, exist_ok=True)
