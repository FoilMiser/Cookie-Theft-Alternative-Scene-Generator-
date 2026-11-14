"""(v0.55's own script, kept in tools/cycle as the model for the next whole-scene bench of a trial cast: its arm and paths are written in. Edit them.)
bench_build.py ARM name,name,... : v0.55's whole-scene bench. Rebuilds v0.54's records from each record's own regen (same base seed, same forced
set, revision 49) into tpdb_work/v055/bench/sc_ARM.
ARM SB: v0.54's cast with the ten people built again (TPDB_SEAT55=B TPDB_SIT55=B: the seated lower body in stiff pieces, the feet under the knees);
the library starts as a copy of lib054 without the people's seated poses (those whose lower posture is in build_cast.SEATED55).
ARM O: nothing changed (a check that a record rebuilds as it was)."""
import json, os, shutil, sys, time
ROOT = "E:/Cognitive_Test_Scene_Creator"
sys.path.insert(0, ROOT); os.chdir(ROOT)
arm, picks = sys.argv[1], [p for p in sys.argv[2].split(",") if p]
W = "tpdb_work/v055/bench/"
SEATED55 = {"sit", "sit_swing", "sit_dangle", "sit_hang", "sit_low", "sit_slide"}
cat = json.load(open("assets/cast/out054/cast_catalog.json"))["actions"]
lib_dir, out = W + "lib_" + arm, W + "sc_" + arm
if not os.path.exists(lib_dir):
    os.makedirs(lib_dir, exist_ok=True)
    n = k = 0
    for f in os.listdir("assets/cast/lib054"):
        if f.startswith("."):
            continue
        pose = f.split("__")[1].split("~")[0] if f.startswith("person.") and "__" in f else None
        if arm == "SB" and pose and cat.get(pose, {}).get("lower") in SEATED55:
            k += 1
            continue
        shutil.copy2("assets/cast/lib054/" + f, lib_dir + "/" + f); n += 1
    print("seeded", lib_dir, n, "files, left out", k, flush=True)
os.makedirs(out, exist_ok=True)
from scenegen.library import Library
from scenegen import generate as G
lib = Library(cast_dir=(W + "out_SB") if arm == "SB" else "assets/cast/out054", lib_dir=lib_dir)
km = json.load(open("vision/v054/key_map.json"))
for pic in picks:
    name = km.get(pic, pic)
    if os.path.exists(f"{out}/{name}.json"):
        continue
    src = next(f"{d}/{name}.json" for d in ("scenes", "probes") if os.path.exists(f"{d}/{name}.json"))
    r0 = json.load(open(src, encoding="utf-8"))
    t0 = time.time()
    try:
        res = G.regenerate(lib, src, out)
        rec = res[0]
        if isinstance(rec, tuple):
            rec = rec[0]
        why = res[2] if len(res) > 2 else None
    except Exception as e:
        print(pic, name, "ERROR", repr(e)[:300], flush=True)
        continue
    if rec is None:
        print(pic, name, "FAILED", str(why)[:300], flush=True)
        continue
    same_t = [t["id"] for t in rec["templates"]] == [t["id"] for t in r0["templates"]]
    fam0 = sorted((e.get("asset") or {}).get("variant", "") for e in r0["elements"] if e.get("asset"))
    fam1 = sorted((e.get("asset") or {}).get("variant", "") for e in rec["elements"] if e.get("asset"))
    moved = 0
    b0 = {e["id"]: e.get("bbox") for e in r0["elements"] if e.get("bbox")}
    for e in rec["elements"]:
        b = e.get("bbox")
        if b and e["id"] in b0 and max(abs(x - y) for x, y in zip(b, b0[e["id"]])) > 12:
            moved += 1
    print(pic, name, "->", rec["name"], "templates same" if same_t else "TEMPLATES DIFFER", "cast same" if fam0 == fam1 else "CAST DIFFERS",
          "moved %d" % moved, f"{time.time() - t0:.0f}s", flush=True)
print("BUILD_END", arm)
