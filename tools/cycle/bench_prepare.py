"""(v0.53's own script, kept in tools/cycle as the model for the next whole-scene bench with two questions on one set of readers: its picks, arms and paths are written in. Edit them.)
bench_prepare.py : v0.53's whole-scene bench (vision/isolation_v053/who), two questions on one set of nine readers, eight pictures each.

Who: eighteen of v0.52's pictures of the woman in purple in three arms: O as screened, FC her figure fuller and a cardigan for the tee, FL her figure
fuller and a skirt to below the knee for the trousers. Six pictures a reader, two of every arm, no picture twice (age_scenes.py's deal).
Wheel: three of v0.52's four wheelbarrows with a square wheel (pic_11, pic_18, pic_102; the tier-4 garden's did not build again) in two arms, O as screened and W the wheel larger. Two
barrows a reader, both of one arm: four readers have O and five have W, so a reading carried from a reader's first barrow to the second stays
inside its arm. Count by reader as well as by picture.
Writes the blind pictures under shuffled numbers, the map outside the folder, and one prompt a reader: the screen's own reader prompt."""
import collections, json, os, random, shutil
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP, PR = "vision/isolation_v053/who", "tpdb_work/v053/maps/who_map.json", "tpdb_work/v053/who_prompts"
km = json.load(open("vision/v052/key_map.json"))


def src(pic, arm):
    name = km[pic]
    if arm == "O":
        return next(f"{d}/{name}.png" for d in ("scenes", "probes") if os.path.exists(f"{d}/{name}.json"))
    f = f"tpdb_work/v053/who/sc_{arm}/{name}.png"
    assert os.path.exists(f), f
    return f


rows = []
picks = ["pic_19", "pic_23", "pic_25", "pic_42", "pic_44", "pic_45", "pic_47", "pic_51", "pic_61", "pic_64", "pic_71", "pic_72", "pic_74", "pic_77",
         "pic_80", "pic_82", "pic_91", "pic_98"]
random.Random(53).shuffle(picks)
arms = ("O", "FC", "FL")
na, B = 3, 6
for i, pic in enumerate(picks):
    for a, arm in enumerate(arms):
        rows.append({"bench": "who", "pick": pic, "arm": arm, "reader": (i // B) * na + (i + a) % na + 1})
# (pic_73, the tier-4 garden, did not build again with the larger wheel: three barrows)
pairs = {"O": [("pic_11", "pic_18"), ("pic_102", "pic_11"), ("pic_18", "pic_102"), ("pic_11", "pic_102")],
         "W": [("pic_11", "pic_18"), ("pic_102", "pic_11"), ("pic_18", "pic_102"), ("pic_102", "pic_18"), ("pic_11", "pic_102")]}
for rd in range(1, 10):
    arm = "O" if rd in (1, 3, 5, 7) else "W"
    k = [1, 3, 5, 7].index(rd) if arm == "O" else [2, 4, 6, 8, 9].index(rd)
    for pic in pairs[arm][k]:
        rows.append({"bench": "wheel", "pick": pic, "arm": arm, "reader": rd})
for r in rows:
    r["name"] = km[r["pick"]]
    r["src"] = src(r["pick"], r["arm"])
random.Random(5353).shuffle(rows)
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
