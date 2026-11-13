"""age_scenes.py prepare OUT MAP.json PICKS.json ARM=FOLDER[,FOLDER] ... : the age bench in whole scenes (v0.50).
age_scenes.py tally OUT MAP.json

The cut-out age bench (age_bench.py) sits at its ceiling: figures alone were called grown whatever the cast, and the same figures in whole
scenes were called a girl or a boy first in one picture of five. This bench reads whole scenes. PICKS is a list of the last screen's picture
ids (vision/v<PREV>/key_map.json); each ARM is a cast, and its FOLDERs hold the same records built with it (the first arm is usually the last
release's own scenes,probes). `prepare` copies every picture of every arm into OUT/blind under a shuffled number, writes MAP (outside OUT,
so that no reader can open it) and one prompt a reader into <WORK>/who_prompts: the screen's own reader prompt, eight pictures each, two of
every arm, and no picture twice for one reader (with four arms and 32 picks: sixteen readers). `tally` counts, by who_cmp.py's rule, how
each grown figure was called in the first inventory line that names its clothes."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import collections, json, random, re, shutil
os.chdir(ROOT)
mode, OUT, MAP = sys.argv[1], sys.argv[2], sys.argv[3]
PAT = {"person.ana": r"purple (top|t-?shirt|shirt|tee|blouse|sweater|jumper)", "person.mei": r"yellow (sun)?dress",
       "person.ben": r"red (t-?shirt|shirt|top|tee)", "person.dev": r"green (t-?shirt|shirt|top|tee)"}
WORD = re.compile(r"\b(young woman|woman|lady|girl|teenager|teen|boy|young man|man|child|kid|person|adult)\b")
YOUNG = {"girl", "boy", "teenager", "teen", "child", "kid"}

if mode == "prepare":
    picks = json.load(open(sys.argv[4]))
    arms = [a.split("=") for a in sys.argv[5:]]
    km = json.load(open(f"vision/v{PREV}/key_map.json"))
    random.Random(50).shuffle(picks)
    na = len(arms)
    assert len(picks) % (2 * na) == 0, "the picks must fill whole blocks of twice the number of arms"
    B = 2 * na
    rows = []
    for i, pic in enumerate(picks):
        name = km[pic]
        for a, (arm, folders) in enumerate(arms):
            src = next(f"{d}/{name}.png" for d in folders.split(",") if os.path.exists(f"{d}/{name}.json"))
            rows.append({"pick": pic, "name": name, "arm": arm, "src": src, "reader": (i // B) * na + (i + a) % na + 1})
    random.Random(5050).shuffle(rows)
    os.makedirs(OUT + "/blind", exist_ok=True)
    for n, r in enumerate(rows, 1):
        r["pic"] = "pic_%03d" % n
        shutil.copyfile(r["src"], f"{OUT}/blind/{r['pic']}.png")
    json.dump(rows, open(MAP, "w"), indent=1)
    tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts", "reader_template.txt")).read().replace("/home/claude/tpdb", ROOT)
    head, rest = tpl.split("Images (open each with the Read tool):\n", 1)
    tail = rest[rest.index("For each picture"):]
    os.makedirs(f"{WORK}/who_prompts", exist_ok=True)
    for rd in sorted({r["reader"] for r in rows}):
        mine = sorted(r["pic"] for r in rows if r["reader"] == rd)
        sz = len(mine)
        h = head.replace("Look at 7 cartoon", f"Look at {sz} cartoon").replace("only the 7 image", f"only the {sz} image")
        t = tail.replace(f"{ROOT}/vision/v09/desc_pic_NN.md", f"{ROOT}/{OUT}/desc_pic_NNN.md").replace("just the 7 file", f"just the {sz} file")             .replace("(NN = the picture number)", "(NNN = the picture number, as in the image's name)")
        assert "/v09/" not in t
        txt = h + "Images (open each with the Read tool):\n" + "\n".join(f"{ROOT}/{OUT}/blind/{p}.png" for p in mine) + "\n\n" + t
        open(f"{WORK}/who_prompts/reader_{rd}.txt", "w", encoding="utf-8").write(txt)
        c = collections.Counter(r["arm"] for r in rows if r["reader"] == rd)
        print("reader", rd, sz, "pictures", dict(c), "picks all different:", len({r["pick"] for r in rows if r["reader"] == rd}) == sz)
    print(len(rows), "pictures in", OUT + "/blind;", "map", MAP)
else:
    rows = json.load(open(MAP))
    tot = collections.defaultdict(collections.Counter); young = collections.defaultdict(collections.Counter)
    none = collections.defaultdict(collections.Counter); lines_ = []
    for r in rows:
        f = r["src"][:-4] + ".json"
        rec = json.load(open(f))
        fams = {(e.get("asset") or {}).get("family") for e in rec["elements"]}
        dp = f"{OUT}/desc_{r['pic']}.md"
        if not os.path.exists(dp):
            print("no description:", r["pic"]); continue
        s = open(dp, encoding="utf-8").read()
        inv = s[s.lower().find("inventory"):]
        for fam, pat in PAT.items():
            if fam not in fams:
                continue
            tot[r["arm"]][fam] += 1
            ls = [l.strip() for l in inv.splitlines() if re.search(pat, l, re.I)]
            if not ls:
                none[r["arm"]][fam] += 1
                continue
            w = WORD.findall(ls[0].lower())
            y = bool(w and w[0] in YOUNG)
            young[r["arm"]][fam] += y
            lines_.append((r["arm"], fam.split(".")[1], r["pick"], r["pic"], "YOUNG" if y else "grown", ls[0][:150]))
    if len(sys.argv) > 4:
        for l in sorted(lines_):
            print(" | ".join(l))
    for arm in tot:
        print(arm.ljust(4), {f.split(".")[1]: "%d of %d%s" % (young[arm][f], tot[arm][f], " (no line %d)" % none[arm][f] if none[arm][f] else "") for f in PAT},
              "| all four:", sum(young[arm].values()), "of", sum(tot[arm].values()))
