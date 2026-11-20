"""(v0.58's own script, kept in tools/cycle as the model for the next whole-picture bench: its arms and paths are written in. Edit them.)
bench_build.py ARM name,name,... [SLICE/OF] : v0.58's whole-picture bench. Builds v0.57's pictures again, each on its own record's plan only
(same base seed, same forced set, revision 51; an isomorph through its source), into tpdb_work/v058/bench/sc_ARM, with v0.58's drawings of
the scene made to act at revision 51 (TPDB_REV58=51) and nothing else: TPDB_ONLY58 names the switches of the arm, so that a picture stays
where it was unless a new drawing's own box or rule moves it. An arm is its switches, its cast and the poses that its cast draws anew
(ARMS below). Arm O changes nothing (a check that a record rebuilds as it was).
A picture that does not place on its record's own plan is reported as FAILED and left out. The library of an arm starts as a copy of
lib057 without the variants whose drawing changed; they render on demand from the arm's cast. With SLICE/OF (2/5) only every OFth picture
from the SLICEth is built, so that several runs can share an arm."""
import json, os, re, shutil, sys, time
ROOT = "E:/Cognitive_Test_Scene_Creator"
sys.path.insert(0, ROOT); os.chdir(ROOT)
arm, picks = sys.argv[1], [p for p in sys.argv[2].split(",") if p]
if len(sys.argv) > 3:
    a_, n_ = (int(x) for x in sys.argv[3].split("/"))
    picks = picks[a_ - 1::n_]
W = "tpdb_work/v058/bench/"
C57 = "assets/cast/out057"
# arm: (environment, cast folder, poses the cast draws anew, library folder's name)
DRAW = "BARROW,SEATFIT,RIDE,KITEREEL,CATCHRAIL"
POSES58 = ["seesaw_low_look", "seesaw_low", "seesaw_stuck_call", "seesaw_high", "kite_lost", "kite_dropped"]
ARMS = {
    "O": [{}, C57, [], "O"],
    # round 1. B: the trial cast (out_B: out057 with tomas, dev, leo, nia and kai built again: the man on his seat, the stuck child leaning
    # back with both fists on the handle, the plain seesaw's raised rider, the kite's child with the reel in a lowered hand) and every
    # drawing of the scene (the barrow's wheel with the bicycle's hub and spokes, the seat's pad, the reel's line, the ball off a rail);
    # C: the alternatives (cast out_C: the stuck child bent forward and feeling for the ground; the barrow's wheel at the bicycle's size;
    # the reel lying on the grass)
    "B": [{"TPDB_REV58": "51", "TPDB_ONLY58": DRAW}, W + "out_B", POSES58, "B"],
    "C": [{"TPDB_REV58": "51", "TPDB_ONLY58": DRAW, "TPDB_BARROW58": "C", "TPDB_KITEREEL58": "C"}, W + "out_C", POSES58, "C"],
    # round 2. E: the new man on his seat with v0.57's child (cast out_E: out_B with nia and kai built with TPDB_STUCK58=O)
    "E": [{"TPDB_REV58": "51", "TPDB_ONLY58": DRAW}, W + "out_E", POSES58, "E"],
}
env, cast_dir, poses, libname = ARMS[arm]
os.environ.update(env)
POSES = set(poses)


def changed(f):
    if "__" not in f:
        return False
    return f.split("__")[1].split("~")[0] in POSES


lib_dir, out = W + "lib_" + libname, W + "sc_" + arm
if not os.path.exists(lib_dir):
    os.makedirs(lib_dir, exist_ok=True)
    n = k = 0
    for f in os.listdir("assets/cast/lib057"):
        if f.startswith("."):
            continue
        if changed(f):
            k += 1
            continue
        shutil.copy2("assets/cast/lib057/" + f, lib_dir + "/" + f); n += 1
    print("seeded", lib_dir, n, "files, left out", k, flush=True)
os.makedirs(out, exist_ok=True)
from scenegen.library import Library
from scenegen import generate as G
from scenegen import scene as SCN
from scenegen.batch import build_isomorph
from scenegen.planner import plan
from scenegen.scene import PlacementError
lib = Library(cast_dir=cast_dir, lib_dir=lib_dir)
km = json.load(open("vision/v057/key_map.json"))
for pic in picks:
    name = km.get(pic, pic)
    if os.path.exists(f"{out}/{name}.json"):
        continue
    src = next(f"{d}/{name}.json" for d in ("scenes", "probes") if os.path.exists(f"{d}/{name}.json"))
    r0 = json.load(open(src, encoding="utf-8"))
    g = r0["regen"]
    SCN.PLACEMENT_REV = g.get("placement_rev", 1)
    t0 = time.time()
    try:
        if g.get("isomorph_of"):
            rec_a = json.load(open(os.path.join(os.path.dirname(src), g["isomorph_of"] + ".json")))
            rec = build_isomorph(lib, rec_a, r0["setting"], g["seed"], out, log=lambda *a: None)
            why = None
            if isinstance(rec, tuple):
                rec = rec[0]
            if isinstance(rec, dict) and "failed" in rec:
                why, rec = [sorted(set(rec["failed"]))], None
            if rec is not None and rec["name"] != name:
                # (the isomorph search went on to another mapping: not this picture)
                for ext in (".json", ".png", ".svg", "_gray.png", "_thumb.png"):
                    if os.path.exists(f"{out}/{rec['name']}{ext}"):
                        os.remove(f"{out}/{rec['name']}{ext}")
                why, rec = [f"came back as {rec['name']}"], None
        else:
            G.USAGE.clear(); G.USAGE.update(g["usage"])
            k = (int(re.search(r"_s(\d+)", name).group(1)) - g["base_seed"]) // 1000      # the record is the plan of its base seed's (k+1)th try
            for j in range(k):          # (the plans of the tries before it are drawn again and not built: they failed for the record)
                try:
                    plan(r0["tier"], r0["setting"], g["base_seed"] + 1000 * j, lib, g.get("forced"))
                except PlacementError:
                    pass
            rec, _, why = G.build_one(lib, r0["tier"], r0["setting"], g["base_seed"] + 1000 * k, out, forced=g.get("forced"), require_band=g["require_band"],
                                      max_tries=1, placements=g["placements"], log=lambda *a: None)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(pic, name, "ERROR", repr(e)[:300], flush=True)
        continue
    if rec is None:
        print(pic, name, "FAILED on its own plan:", str(why[-1] if why else why)[:300], f"{time.time() - t0:.0f}s", flush=True)
        continue
    b0 = {e["id"]: e.get("bbox") for e in r0["elements"] if e.get("bbox")}
    moved = [e["id"] for e in rec["elements"] if e.get("bbox") and e["id"] in b0 and max(abs(x - y) for x, y in zip(e["bbox"], b0[e["id"]])) > 12]
    same_t = [t["id"] for t in rec["templates"]] == [t["id"] for t in r0["templates"]]
    fam0 = sorted((e.get("asset") or {}).get("family", "") for e in r0["elements"] if e.get("asset"))
    fam1 = sorted((e.get("asset") or {}).get("family", "") for e in rec["elements"] if e.get("asset"))
    print(pic, name, "OK", "templates same" if same_t else "TEMPLATES DIFFER", "cast same" if fam0 == fam1 else "CAST DIFFERS",
          "layout", r0.get("layout"), "->", rec.get("layout"), "moved %d" % len(moved), moved[:5], f"{time.time() - t0:.0f}s", flush=True)
print("BUILD_END", arm)
