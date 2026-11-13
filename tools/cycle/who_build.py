"""(v0.52's own script, kept in tools/cycle as the model for the next whole-scene bench of a cast: its arms and paths are written in. Edit them.)
who_build.py ARM pic,pic,... : the whole-scene bench of v0.52. Rebuilds v0.51's records (vision/v051/key_map.json) from each record's own
regen (same base seed, same forced set, revision 48) with a trial cast into tpdb_work/v052/who/sc_ARM.
ARM B: the cast with the new sleeves and v0.51's sweeper (who/out_B). ARM S: that cast with the upright sweeper (who/out_S).
A library starts as a copy of lib051's animals; every person is rendered again from the trial cast."""
import json, os, shutil, sys, time
ROOT = "E:/Cognitive_Test_Scene_Creator"
sys.path.insert(0, ROOT); os.chdir(ROOT)
arm, picks = sys.argv[1], sys.argv[2].split(",")
W = "tpdb_work/v052/who/"
lib_dir, out = W + "lib_" + arm, W + "sc_" + arm
if not os.path.exists(lib_dir):
    os.makedirs(lib_dir, exist_ok=True)
    n = 0
    for f in os.listdir("assets/cast/lib051"):
        if f.startswith(".") or f.startswith("person."):
            continue
        shutil.copy2("assets/cast/lib051/" + f, lib_dir + "/" + f); n += 1
    print("seeded", lib_dir, n, "files", flush=True)
os.makedirs(out, exist_ok=True)
from scenegen.library import Library
from scenegen import generate as G
lib = Library(cast_dir=W + "out_" + arm, lib_dir=lib_dir)
km = json.load(open("vision/v051/key_map.json"))
for pic in picks:
    name = km[pic]
    if os.path.exists(f"{out}/{name}.json"):
        continue
    src = next(p for p in (f"scenes/{name}.json", f"probes/{name}.json") if os.path.exists(p))
    r0 = json.load(open(src, encoding="utf-8"))
    t0 = time.time()
    try:
        rec, _, why = G.regenerate(lib, src, out)
    except Exception as e:
        print(pic, name, "ERROR", repr(e)[:300], flush=True)
        continue
    if rec is None:
        print(pic, name, "FAILED", str(why)[:300], flush=True)
        continue
    same_t = [t["id"] for t in rec["templates"]] == [t["id"] for t in r0["templates"]]
    fam0 = sorted((e.get("asset") or {}).get("variant", "") for e in r0["elements"] if e.get("asset"))
    fam1 = sorted((e.get("asset") or {}).get("variant", "") for e in rec["elements"] if e.get("asset"))
    print(pic, name, "->", rec["name"], "templates same" if same_t else "TEMPLATES DIFFER", "cast same" if fam0 == fam1 else "CAST DIFFERS",
          f"{time.time() - t0:.0f}s", flush=True)
