"""(v0.54's own script, kept in tools/cycle as the model for a whole-scene bench with three questions on one set of readers: its picks, arms and paths are written in. Edit them.)
bench_prepare.py : v0.54's whole-scene bench (vision/isolation_v054/bench), three questions on one set of twelve readers, six pictures each.

Bike: four bicycles with square wheels (v0.53's pic_51, pic_58 and pic_63, and one built for the bench; v0.53's fourth is an isomorph and did not build
again as the same picture) in two arms, O as screened and B the wheels larger (draw.WHEEL54).
Barrow: v0.53's four wheelbarrows (pic_41, pic_42, pic_68, pic_97) in two arms, O as screened and T with tread on the tyre (draw.TREAD54).
Read: six pictures of the man in the red shirt reading (v0.53's pic_29, pic_60 and pic_67, and three built for the bench in the park, the playground
and the street) in two arms, O as screened and B his head up (castlib.actions.READ54).
A reader has two pictures of each question, both of one arm, so that what a reader carries from the first to the second stays inside its arm; six
readers have each arm of each question, and the arms of the three questions are crossed. Count by reader as well as by picture.
Writes the blind pictures under shuffled numbers, the map outside the folder, and one prompt a reader: the screen's own reader prompt."""
import collections, json, os, random, shutil
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP, PR = "vision/isolation_v054/bench", "tpdb_work/v054/maps/bench_map.json", "tpdb_work/v054/bench_prompts"
B = "tpdb_work/v054/bench/"
km = json.load(open("vision/v053/key_map.json"))
ARM_DIR = {("bike", "B"): B + "sc_WB", ("barrow", "T"): B + "sc_TT", ("read", "B"): B + "sc_RB"}


def src(bench, pick, arm):
    name = km.get(pick, pick)
    if arm == "O":
        return name, next(f"{d}/{name}.png" for d in ("scenes", "probes", B + "sc_X") if os.path.exists(f"{d}/{name}.json"))
    f = f"{ARM_DIR[(bench, arm)]}/{name}.png"
    assert os.path.exists(f), f
    return name, f


PICKS = {"bike": ["pic_51", "pic_58", "pic_63", "T3_playground_s54401"],
         "barrow": ["pic_41", "pic_42", "pic_68", "pic_97"],
         "read": ["pic_29", "pic_60", "pic_67", "T3_park_s54102", "T3_playground_s54314", "T3_street_s54204"]}
P4 = [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)]
P6 = [(0, 3), (1, 4), (2, 5), (0, 4), (1, 5), (2, 3)]
ARMS = {"bike": "OBOBOBOBOBOB", "barrow": "OOTTOOTTOOTT", "read": "OBBOBOOBOBBO"}
rows = []
for bench in ("bike", "barrow", "read"):
    seen = collections.Counter()
    for rd in range(12):
        arm = ARMS[bench][rd]
        k = seen[arm]; seen[arm] += 1
        for i in (P6 if bench == "read" else P4)[k]:
            pick = PICKS[bench][i]
            name, f = src(bench, pick, arm)
            rows.append({"bench": bench, "pick": pick, "name": name, "arm": arm, "reader": rd + 1, "src": f})
random.Random(5454).shuffle(rows)
if os.path.exists(OUT + "/blind"):
    raise SystemExit("blind folder exists: " + OUT)
os.makedirs(OUT + "/blind")
for n, r in enumerate(rows, 1):
    r["pic"] = "pic_%03d" % n
    shutil.copyfile(r["src"], f"{OUT}/blind/{r['pic']}.png")
os.makedirs(os.path.dirname(MAP), exist_ok=True)
json.dump(rows, open(MAP, "w"), indent=1)
tpl = open("tools/cycle/prompts/reader_template.txt", encoding="utf-8").read().replace("/home/claude/tpdb", ROOT)
head, rest = tpl.split("Images (open each with the Read tool):\n", 1)
tail = rest[rest.index("For each picture"):]
os.makedirs(PR, exist_ok=True)
for rd in sorted({r["reader"] for r in rows}):
    mine = sorted(r["pic"] for r in rows if r["reader"] == rd)
    sz = len(mine)
    h = head.replace("Look at 7 cartoon", f"Look at {sz} cartoon").replace("only the 7 image", f"only the {sz} image")
    t = tail.replace(f"{ROOT}/vision/v09/desc_pic_NN.md", f"{ROOT}/{OUT}/desc_pic_NNN.md").replace("just the 7 file", f"just the {sz} file") \
        .replace("(NN = the picture number)", "(NNN = the picture number, as in the image's name)")
    assert "/v09/" not in t and " 7 " not in h + t
    txt = h + "Images (open each with the Read tool):\n" + "\n".join(f"{ROOT}/{OUT}/blind/{p}.png" for p in mine) + "\n\n" + t
    open(f"{PR}/reader_{rd}.txt", "w", encoding="utf-8").write(txt)
    mine_r = [r for r in rows if r["reader"] == rd]
    c = collections.Counter((r["bench"], r["arm"]) for r in mine_r)
    print("reader", rd, sz, "pictures", dict(c), "pictures all different:", len({r["name"] for r in mine_r}) == sz)
c = collections.Counter((r["bench"], r["arm"], r["pick"]) for r in rows)
print(sorted(c.items()))
print(len(rows), "pictures in", OUT + "/blind;", "map", MAP)
