"""(v0.55's own script: its picks, arms and paths are written in. Edit them.)
bench_prepare.py : v0.55's whole-scene bench (vision/isolation_v055/bench): eighteen of v0.54's pictures that hold a seated figure, each in two
arms, O as v0.54 screened it and B built again from its own record with the trial cast (the seated lower body in stiff pieces, the feet under
the knees: tpdb_work/v055/bench/sc_SB, tools/cycle/bench_build.py SB).
Twelve readers, six pictures each, three of each arm and no picture twice; every picture is read by two readers in each arm. The pictures lie
in a ring and a reader has six in a row, the first three of one arm and the next three of the other, the arms the other way round for the
second six readers. Writes the blind pictures under shuffled numbers, the map outside the folder, and one prompt a reader: the screen's own
reader prompt."""
import collections, json, os, random, shutil
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP, PR = "vision/isolation_v055/bench", "tpdb_work/v055/maps/bench_map.json", "tpdb_work/v055/bench_prompts"
SB = "tpdb_work/v055/bench/sc_SB"
km = json.load(open("vision/v054/key_map.json"))
# (in a ring: no two pictures of one event side by side, so that a reader has at most two of an event, one in each arm at the most often)
PICKS = ["pic_29", "pic_46", "pic_22", "pic_64", "pic_94", "pic_55", "pic_40", "pic_38", "pic_77", "pic_06", "pic_17", "pic_57",
         "pic_16", "pic_27", "pic_11", "pic_79", "pic_07", "pic_71"]
rows = []
for rd in range(12):
    first, second = ("O", "B") if rd < 6 else ("B", "O")
    for j in range(6):
        pick = PICKS[(3 * rd + j) % 18]
        arm = first if j < 3 else second
        name = km[pick]
        f = f"{SB}/{name}.png" if arm == "B" else next(f"{d}/{name}.png" for d in ("scenes", "probes") if os.path.exists(f"{d}/{name}.json"))
        assert os.path.exists(f), f
        rows.append({"pick": pick, "name": name, "arm": arm, "reader": rd + 1, "src": f})
random.Random(5555).shuffle(rows)
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
    c = collections.Counter(r["arm"] for r in mine_r)
    print("reader", rd, sz, "pictures", dict(c), "pictures all different:", len({r["name"] for r in mine_r}) == sz)
c = collections.Counter((r["pick"], r["arm"]) for r in rows)
print("every picture twice in each arm:", set(c.values()) == {2}, len(c))
print(len(rows), "pictures in", OUT + "/blind;", "map", MAP)
