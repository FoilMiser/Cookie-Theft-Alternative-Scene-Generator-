"""(v0.58's own script: its rows, arms and paths are written in. Edit them.)
bench_prepare.py : v0.58's whole-picture bench (vision/isolation_v058/bench). v0.57's pictures in up to three arms:
  O  as v0.57 screened them (scenes, probes): the screen's own reading (arm S, printed by bench_tally.py) stands beside these;
  B  built again on the record's own plan with the trial cast and v0.58's drawings of the scene (tools/cycle/bench_build.py B);
  C  the alternatives, for the rows that have one (bench_build.py C).
The design is v0.57's second round from the start (RUNBOOK, Lessons, v0.57): A READER HAS A ROW'S PICTURES IN ONE ARM ONLY, so that a
reader's habit of naming or doubting a thing is counted once, and the arms cross between the rows (reader i has row r in arm (i + r) mod 3).
Fifteen readers of eight pictures: two of each row with three arms, one of each row with two. Every picture of a three-arm row is read
twice in each arm where the row has five pictures. No reader has a scene twice. Writes the blind pictures under shuffled numbers, the map
outside the folder (tpdb_work/v058/maps/bench_map.json, with each picture's row), and one prompt a reader: the screen's own reader prompt."""
import collections, json, os, random, shutil
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP, PR, W = "vision/isolation_v058/bench", "tpdb_work/v058/maps/bench_map.json", "tpdb_work/v058/bench_prompts", "tpdb_work/v058/bench/"
km = json.load(open("vision/v057/key_map.json"))
N_READERS = 15
ROWS3 = collections.OrderedDict([            # rows with arms O, B, C: v0.57's pictures (numbers of its screen), two a reader
    ("barrow", [38, 40, 130, 28, 49]),
    ("heavy", [9, 15, 24, 52, 90]),
    ("kite", [21, 64, 76, 97, 115, 136]),
])
ROWS2 = collections.OrderedDict([            # rows with arms O, B: one a reader
    ("plain", [7, 58, 73, 79, 96]),
    ("catch", [101, 134]),
])
allp = [p for v in list(ROWS3.values()) + list(ROWS2.values()) for p in v]
assert len(allp) == len(set(allp)), "a picture serves one row"


def name(p):
    return km["pic_%02d" % p]


def src(n, arm):
    if arm == "O":
        return next(f"{d}/{n}.png" for d in ("scenes", "probes") if os.path.exists(f"{d}/{n}.png"))
    return f"{W}sc_{arm}/{n}.png"


readers = [[] for _ in range(N_READERS)]
for ri, (row, pics) in enumerate(ROWS3.items()):
    for ai, arm in enumerate("OBC"):
        mine = [i for i in range(N_READERS) if "OBC"[(i + ri) % 3] == arm]
        for j, i in enumerate(mine):
            for k in (0, 1):
                p = pics[(2 * j + k + 2 * ai) % len(pics)]
                readers[i].append((name(p), arm, row, p))
for ri, (row, pics) in enumerate(ROWS2.items()):
    arm_of = (lambda i: "B" if i % 2 == 0 else "O") if ri == 0 else (lambda i: "B" if (i // 2) % 2 == 0 else "O")
    seen = collections.Counter()
    for i in range(N_READERS):
        arm = arm_of(i)
        p = pics[seen[arm] % len(pics)]
        seen[arm] += 1
        readers[i].append((name(p), arm, row, p))
out_rows = []
for i, r in enumerate(readers, 1):
    assert len(r) == 8 and len({x[0] for x in r}) == 8, (i, r)
    for n, arm, row, p in r:
        s = src(n, arm)
        assert os.path.exists(s), s
        out_rows.append({"name": n, "pick": "pic_%02d" % p, "arm": arm, "reader": i, "src": s, "rows": [row]})
rng = random.Random(5858)
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
print(len(set(r["name"] for r in out_rows)), "pictures of v0.57;", len(out_rows), "readings", dict(collections.Counter(r["arm"] for r in out_rows)), "by", N_READERS, "readers")
print("by row and arm:", {row: dict(collections.Counter(r["arm"] for r in out_rows if row in r["rows"])) for row in list(ROWS3) + list(ROWS2)})
print("readings a picture and arm:", dict(collections.Counter(collections.Counter((r["name"], r["arm"]) for r in out_rows).values())))
print("a reader's arms by row:", {i: "".join(sorted({(r["rows"][0][0] + r["arm"]) for r in out_rows if r["reader"] == i})) for i in (1, 2, 3)})
