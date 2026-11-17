"""(v0.56's own script: its rows, arms and paths are written in. Edit them.)
bench_prepare.py [N_PER_ROW] : v0.56's whole-picture bench (vision/isolation_v056/bench). v0.55's pictures in up to four arms:
  O  as v0.55 screened them (scenes, probes);
  B  built again on the record's own plan with the trial cast and v0.56's drawings of the scene (tools/cycle/bench_build.py B);
  C  the alternatives, for the pictures that hold them (bench_build.py C);
  L  the bicycle leaning on its post and nothing else changed, v0.55's cast (bench_build.py L): picture 51, eight readers, against eight of O;
  F  pictures built for the bench where v0.55's would not build again (tpdb_work/v056/bench/sc_F), no arm O.
The pictures are chosen row by row: for every row of the list (a template, or a figure's pose) the pictures of v0.55 that hold it and
came back in arm B with the same templates and cast, up to N_PER_ROW a row (default 4), those first that serve the most rows. Every
chosen picture is read by one reader in arm O and two in arm B; a picture of arm C or F by two; no reader has a picture twice in any
arm, and a reader has at most eight pictures. Writes the blind pictures under shuffled numbers, the map outside the folder
(tpdb_work/v056/maps/bench_map.json, with the rows each picture serves), and one prompt a reader: the screen's own reader prompt."""
import collections, glob, json, os, random, shutil, sys
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
OUT, MAP, PR, W = "vision/isolation_v056/bench", "tpdb_work/v056/maps/bench_map.json", "tpdb_work/v056/bench_prompts", "tpdb_work/v056/bench/"
NPER = int(sys.argv[1]) if len(sys.argv) > 1 else 4
km = json.load(open("vision/v055/key_map.json"))
inv = {v: k for k, v in km.items()}


def rec0(name):
    return json.load(open(next(f"{d}/{name}.json" for d in ("scenes", "probes") if os.path.exists(f"{d}/{name}.json")), encoding="utf-8"))


def rows_of(r):
    """The rows of the list that a record of v0.55 holds."""
    t = {x["id"] for x in r["templates"]}
    v = [(e["asset"]["family"], e["asset"]["variant"].split("__")[1].split("~")[0]) for e in r["elements"] if e.get("asset")]
    ids = {e["id"] for e in r["elements"]}
    out = set()
    if "square_wheel" in t:
        out.add("bike" if r["setting"] in ("street", "playground") else "barrow")
    for a, b in (("bird_steals", "bird"), ("blocked_hose", "hose"), ("seesaw_heavy", "seesaw_heavy"), ("seesaw", "seesaw_play"), ("dog_wants_walk", "lead"),
                 ("cat_stalks_bird", "cat"), ("dog_sleeping", "sleep"), ("sprinkler_package", "parcel"), ("kite_in_tree", "kite"), ("water_upward", "upward"),
                 ("floating_box", "box"), ("play_catch", "trail"), ("paint_fence", "paint"), ("paint_tracks", "paint"), ("plant_flowers", "plant"),
                 ("ducks_bread", "bread"), ("feed_birds", "feed"), ("rain_coming", "point"), ("ice_cream_drop", "cone"), ("swing", "swing"),
                 ("hang_laundry", "hang"), ("pan_watering", "pan"), ("lost_balloon", "lostcol"), ("picnic", "picnic"), ("about_to_trip", "trip"),
                 ("fishing", "pond"), ("ducks_swimming", "pond"), ("ladder_nothing", "ladder")):
        if a in t:
            out.add(b)
    if any(f in ("person.mei", "person.rosa", "person.nia") and p.startswith(("sit", "seesaw", "slide")) and p != "sit_ground" for f, p in v):
        out.add("skirt")
    if "pond" in ids and any(f.startswith("person.") for f, p in v):
        out.add("pond")
    return out


ok_b = {}
for f in sorted(glob.glob(W + "bb_B_*.log")):
    for line in open(f, encoding="utf-8", errors="replace"):
        p = line.split()
        if len(p) > 3 and p[0].startswith("pic_") and p[2] == "OK" and "templates same" in line and "cast same" in line:
            ok_b[p[1]] = True
names = sorted(n for n in ok_b if os.path.exists(f"{W}sc_B/{n}.png"))
rows = {n: rows_of(rec0(n)) for n in names}
need = collections.Counter()
chosen = []
allrows = sorted({r for v in rows.values() for r in v})
rng = random.Random(5656)
while True:
    short = {r for r in allrows if need[r] < NPER and any(r in rows[n] for n in names if n not in chosen)}
    if not short:
        break
    best = max((n for n in names if n not in chosen), key=lambda n: (len(rows[n] & short), -len(rows[n]), rng.random()))
    if not rows[best] & short:
        break
    chosen.append(best)
    for r in rows[best]:
        need[r] += 1
slots = []
for n in chosen:
    slots += [(n, "O", next(f"{d}/{n}.png" for d in ("scenes", "probes") if os.path.exists(f"{d}/{n}.png")))] + [(n, "B", f"{W}sc_B/{n}.png")] * 2
for f in sorted(glob.glob(W + "sc_C/T*.json")):
    n = os.path.basename(f)[:-5]
    slots += [(n, "C", f"{W}sc_C/{n}.png")] * 2
for f in sorted(glob.glob(W + "sc_F/T*.json")):
    n = os.path.basename(f)[:-5]
    slots += [(n, "F", f"{W}sc_F/{n}.png")] * 2
P51 = km["pic_51"]
slots = [s for s in slots if s[0] != P51]
slots += [(P51, "O", f"scenes/{P51}.png")] * 8 + [(P51, "L", f"{W}sc_L/{P51}.png")] * 8
for s in slots:
    assert os.path.exists(s[2]), s
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
        out_rows.append({"name": n, "pick": inv.get(n, ""), "arm": arm, "reader": i, "src": src, "rows": sorted(rows.get(n) or (rows_of(json.load(open(src[:-4] + ".json", encoding="utf-8")))))})
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
print(len(chosen), "pictures chosen;", len(out_rows), "readings", dict(c), "by", n_readers, "readers of", collections.Counter(collections.Counter(r["reader"] for r in out_rows).values()))
print("rows covered:", {r: need[r] for r in allrows})
print("no reader has a picture twice:", all(len({x["name"] for x in out_rows if x["reader"] == rd}) == sum(1 for x in out_rows if x["reader"] == rd) for rd in range(1, n_readers + 1)))
