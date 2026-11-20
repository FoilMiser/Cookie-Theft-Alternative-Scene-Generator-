"""(v0.58's own script: its rows, arms and paths are written in. Edit them.)
bench_round2.py : the second round of v0.58's whole-picture bench (vision/isolation_v058/bench2), for what the first round left open.
Three rows, two arms each, sixteen readers of eight pictures, a reader's pictures of a row all of one arm, and the arms crossed between
the rows (reader i has the barrow's arm i mod 2, the kite's (i div 2) mod 2 and the seesaw's (i div 4) mod 2):
  barrow  O  v0.57's picture, the barrow parked            H  the barrow wheeled by a grown figure (BARROW_H: the picture that stands for it)
  kite    B  the reel in a lowered hand (bench/sc_B)        C  the reel on the grass (bench/sc_C)
  heavy   E  the new man with v0.57's child (bench/sc_E)    B  the new man with the child who leans back, both fists on the handle (sc_B)
Two barrow pictures, three kite pictures and three seesaw pictures a reader; no reader has a scene twice. Writes the blind pictures under
shuffled numbers, the map outside the folder (tpdb_work/v058/maps/bench2_map.json) and one prompt a reader: the screen's reader prompt."""
import collections, json, os, random, shutil
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP, PR, W = "vision/isolation_v058/bench2", "tpdb_work/v058/maps/bench2_map.json", "tpdb_work/v058/bench2_prompts", "tpdb_work/v058/bench/"
km = json.load(open("vision/v057/key_map.json"))
N_READERS = 16
ROWS = collections.OrderedDict([            # row: (v0.57's pictures, pictures a reader, arms)
    ("barrow", ([38, 40, 130, 28, 49], 2, "OH")),
    ("kite", ([21, 64, 76, 97, 115, 136], 3, "BC")),
    ("heavy", ([9, 15, 24, 52, 90], 3, "EB")),
])
# the held barrow: v0.57's picture -> the picture that stands for it in arm H (the same record built again with the holder, or the same
# forced set built new under revision 52 where the record's own plan had no room for a figure more)
BARROW_H = json.load(open("tpdb_work/v058/bench/barrow_H.json"))


def name(p):
    return km["pic_%02d" % p]


def src(n, arm, row):
    if arm == "O":
        return next(f"{d}/{n}.png" for d in ("scenes", "probes") if os.path.exists(f"{d}/{n}.png"))
    if arm == "H":
        return BARROW_H[n]
    return f"{W}sc_{arm}/{n}.png"


readers = [[] for _ in range(N_READERS)]
for ri, (row, (pics, per, arms)) in enumerate(ROWS.items()):
    seen = collections.Counter()
    for i in range(N_READERS):
        arm = arms[(i >> ri) & 1]
        k = seen[arm]
        seen[arm] += 1
        for j in range(per):
            p = pics[(per * k + j) % len(pics)]
            readers[i].append((name(p), arm, row, p))
out_rows = []
for i, r in enumerate(readers, 1):
    assert len(r) == 8 and len({x[0] for x in r}) == 8, (i, r)
    for n, arm, row, p in r:
        s = src(n, arm, row)
        assert os.path.exists(s), s
        out_rows.append({"name": n, "pick": "pic_%02d" % p, "arm": arm, "reader": i, "src": s, "rows": [row]})
rng = random.Random(585802)
rng.shuffle(out_rows)
if os.path.exists(OUT + "/blind"):
    raise SystemExit("blind folder exists: " + OUT)
os.makedirs(OUT + "/blind")
for k, r in enumerate(out_rows, 1):
    r["pic"] = "pic_%03d" % k
    shutil.copyfile(r["src"], f"{OUT}/blind/{r['pic']}.png")
os.makedirs(os.path.dirname(MAP), exist_ok=True)
json.dump(out_rows, open(MAP, "w"), indent=1)
tpl = open("tools/cycle/prompts/reader_template.txt", encoding="utf-8").read().replace("/home/claude/tpdb", ROOT)
head, rest = tpl.split("Images (open each with the Read tool):\n", 1)
tail = rest[rest.index("For each picture"):]
os.makedirs(PR, exist_ok=True)
for rd in range(1, N_READERS + 1):
    mine = sorted(r["pic"] for r in out_rows if r["reader"] == rd)
    sz = len(mine)
    h = head.replace("Look at 7 cartoon", f"Look at {sz} cartoon").replace("only the 7 image", f"only the {sz} image")
    t = tail.replace(f"{ROOT}/vision/v09/desc_pic_NN.md", f"{ROOT}/{OUT}/desc_pic_NNN.md").replace("just the 7 file", f"just the {sz} file") \
        .replace("(NN = the picture number)", "(NNN = the picture number, as in the image's name)")
    assert "/v09/" not in t and (sz == 7 or " 7 " not in h + t)
    open(f"{PR}/reader_{rd}.txt", "w", encoding="utf-8", newline="\n").write(
        h + "Images (open each with the Read tool):\n" + "\n".join(f"{ROOT}/{OUT}/blind/{p}.png" for p in mine) + "\n\n" + t)
print(len(out_rows), "readings by", N_READERS, "readers;", "by row and arm:",
      {row: dict(collections.Counter(r["arm"] for r in out_rows if row in r["rows"])) for row in ROWS})
print("readings a picture and arm:", dict(collections.Counter(collections.Counter((r["name"], r["arm"]) for r in out_rows).values())))
print("readers by arms (barrow, kite, heavy):", dict(collections.Counter("".join(sorted({r["rows"][0][0] + r["arm"] for r in out_rows if r["reader"] == i})) for i in range(1, N_READERS + 1))))
for rd in range(1, N_READERS + 1):
    print("R%d:" % rd, " ".join(sorted(r["pic"] for r in out_rows if r["reader"] == rd)))
