import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import os, sys, json, glob, time
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.batch import build_isomorph
from scenegen.library import Library
OUT = f"scenes{TAG}"
names = {}
for f in glob.glob(OUT + "/T*.json"):
    r = json.load(open(f))
    if not r.get("isomorph_of"):
        names[(r["setting"], r["tier"])] = r["name"]
GROUPS_X = [[(("park", 3), st, sd) for sd in (8104, 9104, 10104, 11104, 12104, 13104) for st in ("street", "playground", "garden")] +
            [(("playground", 3), st, sd) for sd in (8104, 9104, 10104, 11104, 12104, 13104) for st in ("park", "street", "garden")]]
GROUPS_Y = [[(("garden", 3), st, sd) for sd in (6102, 7102, 8102, 9102, 10102, 11102) for st in ("park", "street", "playground")] +
            [(("street", 2), st, sd) for sd in (6109, 7109, 8109, 9109) for st in ("park", "playground", "garden")]]
GROUPS = [[(("park", 2), "street", 6109), (("park", 2), "playground", 6109), (("garden", 2), "street", 6109), (("park", 2), "street", 7109), (("garden", 2), "park", 7109)],
          [(("street", 3), "garden", 6102), (("street", 3), "park", 6102), (("street", 3), "playground", 6102), (("garden", 3), "park", 7102), (("garden", 3), "street", 7102), (("street", 3), "park", 8102)],
          [(("park", 3), "street", 6104), (("playground", 3), "park", 6104), (("playground", 3), "street", 6104), (("park", 3), "playground", 6104), (("park", 3), "street", 7104)],
          [(("playground", 2), "garden", 6118), (("playground", 2), "park", 6118), (("garden", 2), "playground", 6118), (("playground", 2), "park", 7118), (("street", 2), "park", 7118)],
          [(("playground", 4), "park", 6111), (("park", 4), "street", 6111), (("park", 4), "playground", 6111), (("garden", 4), "park", 6111), (("playground", 4), "park", 7111), (("street", 4), "park", 7111)]]
GROUPS = GROUPS_X if os.environ.get('ISO_X') else GROUPS_Y if os.environ.get('ISO_Y') else GROUPS
SEL = [int(x) for x in sys.argv[1].split(',')] if len(sys.argv) > 1 else list(range(len(GROUPS)))
SUMF = sys.argv[2] if len(sys.argv) > 2 else 'isomorph_summary.json'
GROUPS = [g for i, g in enumerate(GROUPS) if i in SEL]
lib = Library()
res = []
used = set()
for g in GROUPS:
    for (st, tier), setting, seed in g:
        a = names.get((st, tier))
        if not a or a in used:
            continue
        rec_a = json.load(open(os.path.join(OUT, a + ".json")))
        t0 = time.time()
        r = build_isomorph(lib, rec_a, setting, seed, OUT, log=lambda *x: None)
        print("ISO", a, setting, "->", r.get("name"), json.dumps(r.get("isomorph_check", r.get("failed")))[:160], f"{time.time() - t0:.0f}s", flush=True)
        if r.get("name"):
            used.add(a)
            res.append({"A": a, "B": r["name"], "check": r["isomorph_check"], "failed": None})
            json.dump(res, open(os.path.join(OUT, SUMF), "w"), indent=1)
            break
print("ISO_END", flush=True)
