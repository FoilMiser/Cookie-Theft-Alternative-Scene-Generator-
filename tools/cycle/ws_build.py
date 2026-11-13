"""(v0.51's own script, kept in tools/cycle as the model for the next whole-scene bench: its picks, arms and paths are written in. Edit them.)
ws_build.py ARM pic,pic,... : the whole-scene bench of v0.51. Rebuilds v0.50's records (vision/v050/key_map.json) from each record's own
regen (same base seed, same forced set, revision 47) with the trial cast tpdb_work/v051/bench/out_b3 into tpdb_work/v051/ws/sc_ARM.
ARM D: the trial cast, the scene as v0.50 drew it. ARM C: that, and templates.CATCH51 "C" acting from revision 47 (the ball early on its
dashed arc). The library starts as a copy of lib050's variants of what the trial cast does not change."""
import glob, json, os, shutil, sys, time
ROOT = "E:/Cognitive_Test_Scene_Creator"
sys.path.insert(0, ROOT); os.chdir(ROOT)
arm, picks = sys.argv[1], sys.argv[2].split(",")
W = "tpdb_work/v051/"
lib_dir, out = W + "bench/lib_B3", W + "ws/sc_" + arm
if not os.path.exists(lib_dir):
    os.makedirs(lib_dir)
    n = 0
    for f in os.listdir("assets/cast/lib050"):
        v = f.split("__")
        if f.startswith(".") or v[0] in ("person.ben", "person.tomas") or (v[0].startswith("person.") and len(v) > 1 and v[1] in ("throw_ball", "catch", "paint")):
            continue
        shutil.copy2("assets/cast/lib050/" + f, lib_dir + "/" + f); n += 1
    print("seeded", lib_dir, n, "files", flush=True)
os.makedirs(out, exist_ok=True)
from scenegen.library import Library
from scenegen import generate as G
import scenegen.templates as T
if arm == "C":
    T.CATCH51, T.CATCH51_REV = "C", 47
lib = Library(cast_dir=W + "bench/out_b3", lib_dir=lib_dir)
km = json.load(open("vision/v050/key_map.json"))
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
