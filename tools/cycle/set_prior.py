"""Rewrite the planner's PRIOR block from <WORK>/calibration<TAG>.json (run calib_wrap.py first)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, re, sys
sys.path.insert(0, ROOT)
C = json.load(open(os.path.join(WORK, f"calibration{TAG}.json")))
p = os.path.join(ROOT, "scenegen", "planner.py"); s = open(p).read()
from scenegen.planner import PRIOR
inf_lines, con = [], []
for t, rows in PRIOR.items():
    if rows[0][0] == "inference":
        ty, chain, sal, d, r, key = rows[0]
        c = C.get(t, {}).get("inference")
        if c:
            sal, d, r, chain = c["s_mean"], c["d_mean"], c["r"], c["chain"]
        inf_lines.append(f'    "{t}": [("inference", {chain}, {sal:.2f}, {d:.3f}, {r}, "{key}")],')
    else:
        key = rows[0][5]
        c = C.get(t, {}).get("contradiction_notice")
        sal = c["s_mean"] if c else rows[0][2]
        con.append(f'("{t}", {sal:.2f}, "{key}")')
a = s.index("PRIOR = {")
b = s.index("TYPICAL_LOAD")
new = ("PRIOR = {   # (type, chain, salience z, separation, cues - 1, key word); measured by calibrate (v0.22 calibration.json)\n"
       + "\n".join(inf_lines) + "\n}\nfor _cid, _s, _k in [" + ",\n                     ".join(con) + "]:\n"
       + '    PRIOR[_cid] = [("contradiction_notice", 0, _s, 0.0, 0, _k), ("contradiction_explain", 1, _s, 0.0, 0, _k)]\n')
s = s[:a] + new + s[b:]
open(p, "w").write(s)
print(new)
