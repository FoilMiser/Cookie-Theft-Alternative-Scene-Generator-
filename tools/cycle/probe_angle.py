"""probe_angle.py [N] : the probe pass stratified by angle (from v0.39; revision 40 adds the birds, so the table is templates.yaw_table()).
Every animal template of the table gets at least N screened pictures (default 2) at each of its yaws, the yaw forced through forced["yaws"]
and kept in the record, so the probe rebuilds exactly. Run after probes.py; must end SHORT {}."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections
import glob
import json
import os
import sys

sys.path.insert(0, ROOT)
os.chdir(ROOT)
from scenegen import templates as TT
from scenegen.generate import build_one
from scenegen.library import Library
from scenegen.planner import USAGE

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2
OUT = f"probes{TAG}"
kind_of = {c.id: k for k, lst in (("events", TT.EVENTS), ("modules", TT.MODULES), ("contradictions", TT.CONTRADICTIONS)) for c in lst}


def yaws_of(r):
    els = {e["id"]: e for e in r["elements"]}
    got = set()
    for it in r["items"]:
        t = it.get("template")
        if t not in TT.yaw_table():
            continue
        for i in it.get("elements", []):
            a = els.get(i, {}).get("asset") or {}
            if a.get("family", "").startswith("animal."):
                got.add((t, int(a["variant"].rsplit("__y", 1)[1])))
    return got


def count():
    c = collections.Counter()
    for f in glob.glob(f"scenes{TAG}/T*.json") + glob.glob(OUT + "/T*.json"):
        if f.endswith("summary.json"):
            continue
        for k in yaws_of(json.load(open(f))):
            c[k] += 1
    return c


lib = Library()
seed = 40500
cnt = count()
want = [(t, y) for t, ys in TT.yaw_table().items() for y in ys if (t, y) not in TT.UNPLACED]
print("BEFORE", {f"{t}@{y}": cnt[(t, y)] for t, y in want}, flush=True)
COMPANY = {"garden": "sweep", "park": "ice_cream", "street": "read_bench", "playground": "ice_cream"}
for t, y in want:
    tries = 0
    while cnt[(t, y)] < N and tries < 6:
        tries += 1
        settings = [s for s in ("park", "garden", "street", "playground") if s in TT.ALL_TEMPLATES[t].settings]
        st = settings[(tries - 1) % len(settings)]
        forced = {kind_of[t]: [t], "yaws": {t: y}}
        comp = COMPANY[st]
        if comp != t and comp not in forced.get("events", []) and not (t == "ice_cream_drop" and comp == "ice_cream"):
            forced.setdefault("events", []).append(comp)
        seed += 1
        USAGE.clear()
        rec, sc, fin = build_one(lib, 3, st, seed, OUT, forced=forced, require_band=False, max_tries=6, log=lambda *a: None)
        if not rec:
            print("FAIL", t, y, st, json.dumps(fin)[:200], flush=True)
            continue
        p = os.path.join(OUT, rec["name"] + ".json")
        r = json.load(open(p))
        r["probe"] = True
        json.dump(r, open(p, "w"), indent=1)
        got = yaws_of(r)
        if (t, y) not in got:
            print("WRONG YAW", rec["name"], t, y, sorted(got), flush=True)
        for k in got:
            cnt[k] += 1
        print("PROBE", rec["name"], t, y, sorted(got), flush=True)
print("SHORT", {f"{t}@{y}": cnt[(t, y)] for t, y in want if cnt[(t, y)] < N}, flush=True)
