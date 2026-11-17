"""(v0.56's own script: its pictures, arms and paths are written in. Edit them.)
bench_round2.py : the second round of v0.56's whole-picture bench (vision/isolation_v056/bench2), for what the first left open.
  bird   three scenes of round 1's new pictures, each built three times on its seed under revision 50 (tpdb_work/v056/bench/build_R2.py
         bird): the bird pulling a slice (arm B), the larger bird pecking (arm C), v0.55's bird (arm O); four readers a picture;
  photo  three scenes with the photographer drawn from the side (build_R2.py photo; arm P); two readers a picture;
  hose   round 1's four pictures of arm B built again with no water at the reel and nothing else changed (bench_build.py N; arm N);
         two readers a picture, as arm B had.
Twelve readers. Each has the three bird scenes, one in each arm, the arms turned from reader to reader, and one or two of the others;
no reader has a scene twice. Writes the blind pictures under shuffled numbers, the map outside the folder
(tpdb_work/v056/maps/bench2_map.json) and one prompt a reader: the screen's own reader prompt."""
import collections, json, os, random, shutil
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP, PR, W = "vision/isolation_v056/bench2", "tpdb_work/v056/maps/bench2_map.json", "tpdb_work/v056/bench2_prompts", "tpdb_work/v056/bench/"
BIRD = ["T3_playground_s56110", "T3_street_s56111", "T3_park_s56112"]
PHOTO = ["T3_playground_s56103", "T3_street_s56105", "T3_park_s57122"]
HOSE = ["T3_garden_s16013", "T3_garden_s23013", "T3_garden_s23033", "T4_garden_s552986"]
N = 12
rng = random.Random(5657)
readers = [[] for _ in range(N)]
for r in range(N):
    for i, n in enumerate(BIRD):
        arm = "BCO"[(i + r) % 3]
        readers[r].append((n, arm, f"{W}sc_R2/bird_{arm}/{n}.png", ["bird"]))
extras = ([(n, "P", f"{W}sc_R2/photo/{n}.png", ["photo"]) for n in PHOTO] + [(n, "N", f"{W}sc_N/{n}.png", ["hose"]) for n in HOSE]) * 2
for k, e in enumerate(extras):
    readers[k % N].append(e)
out_rows = []
for i, r in enumerate(readers, 1):
    assert len({x[0] for x in r}) == len(r), i
    for n, arm, src, rows in r:
        assert os.path.exists(src), src
        out_rows.append({"name": n, "arm": arm, "reader": i, "src": src, "rows": rows})
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
for rd in range(1, N + 1):
    mine = sorted(r["pic"] for r in out_rows if r["reader"] == rd)
    sz = len(mine)
    h = head.replace("Look at 7 cartoon", f"Look at {sz} cartoon").replace("only the 7 image", f"only the {sz} image")
    t = tail.replace(f"{ROOT}/vision/v09/desc_pic_NN.md", f"{ROOT}/{OUT}/desc_pic_NNN.md").replace("just the 7 file", f"just the {sz} file") \
        .replace("(NN = the picture number)", "(NNN = the picture number, as in the image's name)")
    assert "/v09/" not in t and " 7 " not in h + t
    open(f"{PR}/reader_{rd}.txt", "w", encoding="utf-8", newline="\n").write(
        h + "Images (open each with the Read tool):\n" + "\n".join(f"{ROOT}/{OUT}/blind/{p}.png" for p in mine) + "\n\n" + t)
c = collections.Counter((r["rows"][0], r["arm"], r["name"]) for r in out_rows)
print(len(out_rows), "readings by", N, "readers of", collections.Counter(collections.Counter(r["reader"] for r in out_rows).values()))
for k in sorted(c):
    print("  ", k, c[k])
