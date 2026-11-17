"""(v0.56's own script, kept in tools/cycle as the model for the next whole-picture bench: its arms and paths are written in. Edit them.)
bench_build.py ARM name,name,... [SLICE/OF] : v0.56's whole-picture bench. Builds v0.55's pictures again, each on its own record's plan only
(same base seed, same forced set, revision 49; an isomorph through its source), into tpdb_work/v056/bench/sc_ARM, with the trial cast and
v0.56's drawings of the scene made to act at revision 49 (TPDB_REV56=49) and nothing else: TPDB_ONLY56 names the drawing switches, so that
the placement rules of revision 50 stay off and a picture stays where it was unless a new drawing's own box moves it.
ARM B: the trial cast (tpdb_work/v056/bench/out_B) and every drawing switch at its first value (the bicycle leaning on its post, the hose
       with v0.55's swelling).
ARM C: the alternatives, for the pictures that hold them: the wheelbarrow's open square wheel, the bicycle held by its owner, the hose
       pressed flat with no swelling, the thief bird's size alone, the seesaw's seat backs with the child's cupped hands (cast out_C), the
       red lead.
ARM L: the bicycle leaning on its post and nothing else, with v0.55's cast: picture 51, which must hold still round its bicycle.
ARM O: nothing changed (a check that a record rebuilds as it was).
A picture that does not place on its record's own plan is reported as FAILED and left out. The library of an arm starts as a copy of
lib055 without the variants whose drawing changed; they render on demand from the arm's cast. With SLICE/OF (2/5) only every OFth picture
from the SLICEth is built, so that five runs can share an arm."""
import json, os, re, shutil, sys, time
ROOT = "E:/Cognitive_Test_Scene_Creator"
sys.path.insert(0, ROOT); os.chdir(ROOT)
arm, picks = sys.argv[1], [p for p in sys.argv[2].split(",") if p]
if len(sys.argv) > 3:
    a_, n_ = (int(x) for x in sys.argv[3].split("/"))
    picks = picks[a_ - 1::n_]
W = "tpdb_work/v056/bench/"
DRAW = "BARROW,BARROWCOL,BIKE,STEAL,STEALAT,HOSE,DRIP,SEEP,LOWEND,TILT,STALKBIRD,LEAD,PAINT,TRAY,ROLLER,SEEDLING,BREAD,PARCEL,SPRAY,HOSEBED,HOSERUN," \
       "KITE,UPW,BOXHAND,TRAIL,LOSTCOL,SPLAT,BASKET,BANK,SUN"
ARMS = {
    "O": ({}, "assets/cast/out055"),
    "B": ({"TPDB_REV56": "49", "TPDB_ONLY56": DRAW, "TPDB_BIKE56": "L", "TPDB_HOSE56": "N"}, W + "out_B"),
    "L": ({"TPDB_REV56": "49", "TPDB_ONLY56": "BIKE", "TPDB_BIKE56": "L"}, "assets/cast/out055"),
    "C": ({"TPDB_REV56": "49", "TPDB_ONLY56": DRAW, "TPDB_BIKE56": "H", "TPDB_BARROW56": "C", "TPDB_HOSE56": "B", "TPDB_STEAL56": "C",
           "TPDB_LOWEND56": "C", "TPDB_LEAD56": "C"}, W + "out_C"),
    # round 2: arm B again with no water at the reel (the seep), and nothing else changed (arm B's library)
    "N": ({"TPDB_REV56": "49", "TPDB_ONLY56": DRAW, "TPDB_BIKE56": "L", "TPDB_HOSE56": "N", "TPDB_SEEP56": "O", "TPDB_BARROW56": "B",
           "TPDB_LEAD56": "B", "TPDB_STALKBIRD56": "B", "TPDB_UPW56": "B", "TPDB_TRAIL56": "B"}, W + "out_B"),
}
# (round 1's arm B was built before the bench's defaults were set: it had the wheelbarrow's solid square, the long lead, the bird turned
#  from the cat, the rising streaks and the short trail, which the "B" above no longer names. To build it again, name them as arm N does.)
env, cast_dir = ARMS[arm]
os.environ.update(env)
# the poses whose drawing changed in the trial cast: every person's, the three skirted figures' seated ones, the animals'
POSES = {"paint", "kneel_plant", "water_pan", "bucket_hat", "feed_birds", "feed_birds_low", "hang_washing", "point_up", "cone_dropped", "sit_swing",
         "hose_inspect", "seesaw_low", "seesaw_low_read", "seesaw_stuck_call", "stalk_paw", "sleep_paws_turn", "sit_wait", "read", "sit_read", "walk_read_open"}
SKIRT = {"sit", "sit_clap", "sit_drink", "sit_feed_birds", "sit_ice_cream", "sit_read", "sit_swing", "seesaw_stuck", "seesaw_stuck_call", "seesaw_low",
         "seesaw_low_read", "slide_down"}


def changed(f):
    if "__" not in f:
        return False
    fam, pose, expr = f.split("__")[:3]
    pose = pose.split("~")[0]
    return pose in POSES or (fam in ("person.mei", "person.rosa", "person.nia") and pose in SKIRT) or (fam.startswith("animal.dog") and expr == "sleepy")


lib_dir, out = W + "lib_" + ("B" if arm == "N" else arm), W + "sc_" + arm
if not os.path.exists(lib_dir):
    os.makedirs(lib_dir, exist_ok=True)
    n = k = 0
    for f in os.listdir("assets/cast/lib055"):
        if f.startswith("."):
            continue
        if arm not in ("O", "L") and changed(f):
            k += 1
            continue
        shutil.copy2("assets/cast/lib055/" + f, lib_dir + "/" + f); n += 1
    print("seeded", lib_dir, n, "files, left out", k, flush=True)
os.makedirs(out, exist_ok=True)
from scenegen.library import Library
from scenegen import generate as G
from scenegen import scene as SCN
from scenegen.batch import build_isomorph
from scenegen.planner import plan
from scenegen.scene import PlacementError
lib = Library(cast_dir=cast_dir, lib_dir=lib_dir)
km = json.load(open("vision/v055/key_map.json"))
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
