"""(v0.51's own script, kept in tools/cycle as the model for the next whole-scene bench: its picks, arms and paths are written in. Edit them.)
ws_prepare.py : the whole-scene bench of v0.51 (vision/isolation_v051/ws), two questions on one set of readers.

Catch: v0.50's two pictures in which a child's throw to a grown catcher was read the wrong way round (pic_79, pic_90), in three arms: O as
screened, D the trial cast's poses with v0.50's ball, C those poses with the ball early on its dashed arc. Twelve readers, each one picture
79 and one picture 90 from different arms: four readings of every (picture, arm).
Moustache: sixteen of v0.50's pictures of the man in the red shirt, arms O as screened and B the trial cast; readers 1 to 8 take four each,
two of each arm, no picture twice (age_scenes.py's deal).
Writes the blind pictures under shuffled numbers, the map outside the folder, and one prompt a reader: the screen's own reader prompt."""
import collections, json, os, random, shutil, sys
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP, PR = "vision/isolation_v051/ws", "tpdb_work/v051/maps/ws_map.json", "tpdb_work/v051/ws_prompts"
km = json.load(open("vision/v050/key_map.json"))


def src(pic, arm):
    name = km[pic]
    if arm == "O":
        return next(f"{d}/{name}.png" for d in ("scenes", "probes") if os.path.exists(f"{d}/{name}.json"))
    f = f"tpdb_work/v051/ws/sc_{'D' if arm in ('D', 'B') else arm}/{name}.png"
    assert os.path.exists(f), f
    return f


rows = []
pairs = [("O", "D"), ("O", "C"), ("D", "O"), ("D", "C"), ("C", "O"), ("C", "D")] * 2
for i, (a, b) in enumerate(pairs, 1):
    rows.append({"bench": "catch", "pick": "pic_79", "arm": a, "reader": i})
    rows.append({"bench": "catch", "pick": "pic_90", "arm": b, "reader": i})
picks = ["pic_09", "pic_18", "pic_31", "pic_34", "pic_37", "pic_40", "pic_43", "pic_52", "pic_55", "pic_60", "pic_69", "pic_70", "pic_72", "pic_73",
         "pic_76", "pic_89"]
random.Random(51).shuffle(picks)
for i, pic in enumerate(picks):
    for a, arm in enumerate(("O", "B")):
        rows.append({"bench": "moustache", "pick": pic, "arm": arm, "reader": (i // 4) * 2 + (i + a) % 2 + 1})
for r in rows:
    r["name"] = km[r["pick"]]
    r["src"] = src(r["pick"], r["arm"])
random.Random(5151).shuffle(rows)
os.makedirs(OUT + "/blind", exist_ok=True)
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
    print("reader", rd, sz, "pictures", dict(c), "pictures all different:", len({r["pick"] for r in mine_r}) == sz)
print(len(rows), "pictures in", OUT + "/blind;", "map", MAP)
