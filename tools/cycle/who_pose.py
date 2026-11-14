"""who_pose.py TAG FAMILY 'clothes regex' : per picture of a screen, the figure's pose and yaw, its reader, and the first word for a person in
the first inventory line that names its clothes."""
import json, os, re, sys, glob, collections
os.chdir("E:/Cognitive_Test_Scene_Creator")
tag, fam, pat = sys.argv[1], sys.argv[2], re.compile(sys.argv[3], re.I)
km = json.load(open(f"vision/v{tag}/key_map.json"))
reader = {}
for f in glob.glob(f"tpdb_work/v{tag}prompts/reader_*.txt"):
    n = re.search(r"reader_(\d+)", f).group(1)
    for p in re.findall(r"pic_\d+", open(f, encoding="utf-8").read()):
        reader[p] = n
sc, pr = ("scenes", "probes") if tag == sys.argv[4] else (f"scenes_v{tag}", f"probes_v{tag}")
by = collections.defaultdict(collections.Counter)
for pic, name in sorted(km.items()):
    f = next(p for p in (f"{sc}/{name}.json", f"{pr}/{name}.json") if os.path.exists(p))
    r = json.load(open(f))
    es = [e for e in r["elements"] if (e.get("asset") or {}).get("family") == fam]
    if not es:
        continue
    v = es[0]["asset"]["variant"].split("__")
    s = open(f"vision/v{tag}/desc_{pic}.md", encoding="utf-8").read()
    inv = s[s.lower().find("inventory"):]
    lines = [l.strip() for l in inv.splitlines() if pat.search(l)]
    l = lines[0] if lines else "(no line)"
    w = re.findall(r"\b(young woman|woman|lady|girl|teenager|teen|boy|young man|man|child|kid|person|adult)\b", l.lower())
    w0 = w[0] if w else "?"
    by[v[1]][w0] += 1
    print(pic, "r" + reader.get(pic, "?"), v[1], v[3], "%.2f" % es[0]["asset"]["scale"], w0, "|", l[:110])
for p, c in sorted(by.items()):
    print(p, dict(c))
