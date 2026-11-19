"""(v0.57's own script: its rows, arms and paths are written in. Edit them.)
bench_prepare.py : v0.57's whole-picture bench (vision/isolation_v057/bench). v0.56's pictures in up to four arms:
  O  as v0.56 screened them (scenes, probes), one fresh reader each: the screen's own reading is the arm's other one;
  B  built again on the record's own plan with the trial cast and v0.57's drawings of the scene (tools/cycle/bench_build.py B), two readers;
  C  the alternatives, for the pictures that hold them (bench_build.py C): the pan with a dark inside, and the heavy seesaw's man
     without his book, looking up at the child; two readers;
  P  v0.55's deep pan in v0.56's pictures (bench_build.py P), three readers each;
  F  new pictures of the game of catch built under revision 51 (tpdb_work/v057/bench/sc_F), two readers each, and
  G  the same forced sets on the same seeds with v0.56's flight (sc_G), one reader each.
The pictures are named by row below (a picture may serve several rows). No reader has a picture's scene twice in any arm, and a reader
has at most eight pictures. Writes the blind pictures under shuffled numbers, the map outside the folder
(tpdb_work/v057/maps/bench_map.json, with the rows each picture serves), and one prompt a reader: the screen's own reader prompt."""
import collections, glob, json, os, random, shutil, sys
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP, PR, W = "vision/isolation_v057/bench", "tpdb_work/v057/maps/bench_map.json", "tpdb_work/v057/bench_prompts", "tpdb_work/v057/bench/"
km = json.load(open("vision/v056/key_map.json"))
ROWS = {            # row: v0.56's pictures (numbers of its screen)
    "catch": [45, 86, 116],
    "pan": [22, 36, 53, 56, 114],
    "seesaw_heavy": [10, 26, 51, 92, 100],
    "pond": [57, 72, 118, 62],
    "wind": [66, 126, 95],
    "kite": [18, 82, 97, 110],
    "grey": [65, 106, 80],
}
ARM_C = {"pan", "seesaw_heavy"}          # rows with an alternative
ARM_P = [22, 36, 53]                     # v0.55's pan comes back on these three only
rows_of = collections.defaultdict(set)
for row, pics in ROWS.items():
    for p in pics:
        rows_of[km["pic_%02d" % p]].add(row)
inv = {v: k for k, v in km.items()}


def src0(n):
    return next(f"{d}/{n}.png" for d in ("scenes", "probes") if os.path.exists(f"{d}/{n}.png"))


slots = []
for n, rs in sorted(rows_of.items()):
    slots += [(n, "O", src0(n))] + [(n, "B", f"{W}sc_B/{n}.png")] * 2
    if rs & ARM_C:
        slots += [(n, "C", f"{W}sc_C/{n}.png")] * 2
for p in ARM_P:
    n = km["pic_%02d" % p]
    slots += [(n, "P", f"{W}sc_P/{n}.png")] * 3
fnames = {}
for arm, k in (("F", 2), ("G", 1)):
    for f in sorted(glob.glob(f"{W}sc_{arm}/T*.json")):
        n = os.path.basename(f)[:-5]
        fnames[n] = "catch"
        slots += [(n, arm, f"{W}sc_{arm}/{n}.png")] * k
for s in slots:
    assert os.path.exists(s[2]), s
rng = random.Random(5757)
rng.shuffle(slots)
slots.sort(key=lambda s: -sum(1 for x in slots if x[0] == s[0]))          # the pictures with the most readings are dealt first
n_readers = -(-len(slots) // 8)
readers = [[] for _ in range(n_readers)]
for s in slots:
    free = [r for r in readers if len(r) < 8 and all(x[0] != s[0] for x in r)]
    r = min(free, key=lambda r: (len(r), rng.random()))
    r.append(s)
out_rows = []
for i, r in enumerate(readers, 1):
    for n, arm, src in r:
        out_rows.append({"name": n, "pick": inv.get(n, ""), "arm": arm, "reader": i, "src": src, "rows": sorted(rows_of.get(n) or [fnames[n]])})
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
for rd in range(1, n_readers + 1):
    mine = sorted(r["pic"] for r in out_rows if r["reader"] == rd)
    sz = len(mine)
    h = head.replace("Look at 7 cartoon", f"Look at {sz} cartoon").replace("only the 7 image", f"only the {sz} image")
    t = tail.replace(f"{ROOT}/vision/v09/desc_pic_NN.md", f"{ROOT}/{OUT}/desc_pic_NNN.md").replace("just the 7 file", f"just the {sz} file") \
        .replace("(NN = the picture number)", "(NNN = the picture number, as in the image's name)")
    assert "/v09/" not in t and (sz == 7 or " 7 " not in h + t)
    open(f"{PR}/reader_{rd}.txt", "w", encoding="utf-8", newline="\n").write(
        h + "Images (open each with the Read tool):\n" + "\n".join(f"{ROOT}/{OUT}/blind/{p}.png" for p in mine) + "\n\n" + t)
c = collections.Counter(r["arm"] for r in out_rows)
print(len(rows_of), "pictures of v0.56 and", len(fnames), "new;", len(out_rows), "readings", dict(c), "by", n_readers, "readers of",
      dict(collections.Counter(collections.Counter(r["reader"] for r in out_rows).values())))
print("by row and arm:", {row: dict(collections.Counter(r["arm"] for r in out_rows if row in r["rows"])) for row in list(ROWS)})
print("no reader has a scene twice:", all(len({x["name"] for x in out_rows if x["reader"] == rd}) == sum(1 for x in out_rows if x["reader"] == rd) for rd in range(1, n_readers + 1)))
