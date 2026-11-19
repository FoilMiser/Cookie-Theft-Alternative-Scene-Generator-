"""(v0.57's own script: its arms and paths are written in. Edit them.)
bench_round2.py : the second round of v0.57's whole-picture bench (vision/isolation_v057/bench2), for what the first left open.
  H  five new pictures of the game of catch under revision 51, the catcher cast young and the taller of the two throwing
     (tpdb_work/v057/bench/sc_H, from bench/build_H.py), two readers each;
  E  the heavy seesaw's five pictures with the seat drawn where its rider sits and the man without his book (bench_build.py E), two
     readers each;
  D  the five pan pictures with the dark hollow pan and an unused watering can on the grass beside the holder (bench_build.py D), four
     readers each;
  C  the same five with the dark hollow pan alone (round 1's arm C, read again), two readers each.
A reader who takes the pan for a watering can does so in every pan picture it is given (round 1), so a reader has pan pictures of one arm
only: eight readers have arm D's and four have arm C's. No reader has a scene twice. Writes the blind pictures under shuffled numbers,
the map outside the folder (tpdb_work/v057/maps/bench2_map.json) and one prompt a reader: the screen's own reader prompt."""
import collections, glob, json, os, random, shutil
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP, PR, W = "vision/isolation_v057/bench2", "tpdb_work/v057/maps/bench2_map.json", "tpdb_work/v057/bench2_prompts", "tpdb_work/v057/bench/"
km = json.load(open("vision/v056/key_map.json"))
PAN = [km["pic_%02d" % p] for p in (22, 36, 53, 56, 114)]
SEE = [km["pic_%02d" % p] for p in (10, 26, 51, 92, 100)]
HH = sorted(os.path.basename(f)[:-5] for f in glob.glob(W + "sc_H/T*.json"))
rng = random.Random(5758)
N_D, N_C = 8, 4
readers = [[] for _ in range(N_D + N_C)]


def deal(slots, pool):
    rng.shuffle(slots)
    for s in slots:
        free = [i for i in pool if all(x[0] != s[0] for x in readers[i])]
        i = min(free, key=lambda i: (sum(1 for x in readers[i] if x[1] == s[1]), len(readers[i]), rng.random()))
        readers[i].append(s)


deal([(n, "D", f"{W}sc_D/{n}.png", "pan") for n in PAN for _ in range(4)], list(range(N_D)))
deal([(n, "C", f"{W}sc_C/{n}.png", "pan") for n in PAN for _ in range(2)], list(range(N_D, N_D + N_C)))
rest = [(n, "E", f"{W}sc_E/{n}.png", "seesaw_heavy") for n in SEE for _ in range(2)] + [(n, "H", f"{W}sc_H/{n}.png", "catch") for n in HH for _ in range(2)]
rng.shuffle(rest)
for s in rest:
    free = [i for i in range(len(readers)) if all(x[0] != s[0] for x in readers[i])]
    i = min(free, key=lambda i: (len(readers[i]), sum(1 for x in readers[i] if x[1] == s[1]), rng.random()))
    readers[i].append(s)
out_rows = []
for i, r in enumerate(readers, 1):
    for n, arm, src, row in r:
        assert os.path.exists(src), src
        out_rows.append({"name": n, "arm": arm, "reader": i, "src": src, "rows": [row]})
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
head, rest_ = tpl.split("Images (open each with the Read tool):\n", 1)
tail = rest_[rest_.index("For each picture"):]
os.makedirs(PR, exist_ok=True)
for rd in range(1, len(readers) + 1):
    mine = sorted(r["pic"] for r in out_rows if r["reader"] == rd)
    sz = len(mine)
    h = head.replace("Look at 7 cartoon", f"Look at {sz} cartoon").replace("only the 7 image", f"only the {sz} image")
    t = tail.replace(f"{ROOT}/vision/v09/desc_pic_NN.md", f"{ROOT}/{OUT}/desc_pic_NNN.md").replace("just the 7 file", f"just the {sz} file") \
        .replace("(NN = the picture number)", "(NNN = the picture number, as in the image's name)")
    assert "/v09/" not in t and (sz == 7 or " 7 " not in h + t)
    open(f"{PR}/reader_{rd}.txt", "w", encoding="utf-8", newline="\n").write(
        h + "Images (open each with the Read tool):\n" + "\n".join(f"{ROOT}/{OUT}/blind/{p}.png" for p in mine) + "\n\n" + t)
    print(rd, sz, " ".join(p[4:] for p in mine), dict(collections.Counter(r["arm"] for r in out_rows if r["reader"] == rd)))
print(len(out_rows), "readings", dict(collections.Counter(r["arm"] for r in out_rows)))
print("no reader has a scene twice:", all(len({x["name"] for x in out_rows if x["reader"] == rd}) == sum(1 for x in out_rows if x["reader"] == rd) for rd in range(1, len(readers) + 1)))
print("no reader has both pan arms:", all(len({x["arm"] for x in out_rows if x["reader"] == rd and x["arm"] in "CD"}) <= 1 for rd in range(1, len(readers) + 1)))
