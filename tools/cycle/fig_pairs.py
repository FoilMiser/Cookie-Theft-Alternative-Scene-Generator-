"""(v0.56's own script: its prompt and its paths are written in. Edit them.)
fig_pairs.py ROUND A_DIR B_DIR A_NAME B_NAME SETS.json : a blind pair bench of two drawings of the same figures (people or animals).

SETS.json is {"set name": [[family, pose, expression, yaw, "who the figure is"], ...four views...], ...}; the caption says who the figure is
and not what it does, since the review also asks what each figure is doing in each row. For every set two sheets are made, one with A_DIR's
renders as row a and B_DIR's as row b and one the other way round; each sheet has every figure whole and large and, under it, the same figure
at the size it has in a picture. A_DIR and B_DIR are folders of renders at 800 px per metre (TPDB_PPM=800), given from the repository's root.
Sheets go to vision/isolation_v056/<ROUND>/pair_N.png in a shuffled order, the prompts to tpdb_work/v056/prompts/<ROUND>_N.txt, and the map
(which row is which, in which sheet) to tpdb_work/v056/maps/<ROUND>_map.json, outside the folder a reviewer may see.
With RENDER_LIST=path the views of the sets are written there as a render list and nothing else is done."""
import json, os, random, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = "E:/Cognitive_Test_Scene_Creator/"
W = ROOT + "tpdb_work/v056/"
SETS = json.load(open(sys.argv[6] if not os.environ.get("RENDER_LIST") else sys.argv[1]))
if os.environ.get("RENDER_LIST"):
    rows = sorted({(v[0], v[1], v[2], v[3]) for s in SETS.values() for v in s})
    json.dump([list(r) for r in rows], open(os.environ["RENDER_LIST"], "w"))
    print(len(rows), "views")
    sys.exit(0)
rnd, adir, bdir, aname, bname = sys.argv[1:6]
PPM = 800.0
BIG = 600
try:
    FONT = ImageFont.truetype("arial.ttf", 44)
except OSError:
    FONT = ImageFont.load_default()


def tile(d, v):
    f = "%s/%s__%s__%s__y%03d.png" % (d, v[0], v[1], v[2], v[3])
    im = Image.open(f).convert("RGBA")
    im = im.crop(im.getbbox())
    s = min(BIG / im.height, 1.15 * BIG / im.width)
    big = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    k = 0.45 * 400 / PPM
    small = im.resize((max(1, round(im.width * k)), max(1, round(im.height * k))), Image.LANCZOS)
    return big, small


def sheet(views, top, bot, out):
    rows = [[tile(top, v) for v in views], [tile(bot, v) for v in views]]
    cw = max(max(t[0].width, t[1].width) for r in rows for t in r) + 40
    sh = max(t[1].height for r in rows for t in r)
    rh = BIG + sh + 50
    im = Image.new("RGB", (90 + cw * len(views), rh * 2 + 10), (232, 236, 228))
    d = ImageDraw.Draw(im)
    for ri, r in enumerate(rows):
        y = ri * rh + 6
        d.text((24, y + BIG // 2 - 30), "ab"[ri], fill=(30, 30, 30), font=FONT)
        for ci, (big, small) in enumerate(r):
            x = 90 + ci * cw
            im.paste(big, (x + (cw - big.width) // 2, y + BIG - big.height), big)
            im.paste(small, (x + (cw - small.width) // 2, y + BIG + 16 + sh - small.height), small)
        if ri == 0:
            d.line((0, rh, im.width, rh), fill=(150, 150, 150), width=3)
    im.save(out)
    return im.size


PROMPT = """You are reviewing drawings for a set of cartoon pictures. The image {img} shows the same {n} figures drawn two ways: row a above and row b below. Under each large drawing the same figure is shown at the size it has in a picture. The figures are the same in both rows, left to right: {who}. What a figure stands on, sits on or works at is not drawn, only the figure and what it holds.

Look at that one image with the Read tool. Do not open any other file and do not search or list the folder.

Write your review to {out} with the Write tool, with these parts:

1. In two or three sentences, how the two rows differ.
2. For each figure, left to right: what the figure is doing as row a draws it and as row b draws it (a few words each, what you see and not what you guess the artist meant); then which row draws it better (a, b or no difference) and one sentence of reason.
3. The faults of row a, and the faults of row b, each as a short list that names the figure: anything that looks wrong, unclear or hard to make out, at the large size or at the small one.
4. Which row you would choose for a friendly, clear cartoon style, and how sure you are (sure, fairly sure, or a toss-up).

When the file is written, reply on one line with your choice (a or b), how sure you are, and the count of figures you gave to a, to b and to no difference.
"""

out_dir = ROOT + "vision/isolation_v056/" + rnd
os.makedirs(out_dir, exist_ok=True)
os.makedirs(W + "prompts", exist_ok=True)
os.makedirs(W + "maps", exist_ok=True)
jobs = [(name, order) for name in SETS for order in (0, 1)]
random.Random("v056" + rnd).shuffle(jobs)
m = {}
for i, (name, order) in enumerate(jobs, 1):
    views = SETS[name]
    top, bot = (adir, bdir) if order == 0 else (bdir, adir)
    img = "%s/pair_%d.png" % (out_dir, i)
    size = sheet(views, ROOT + top, ROOT + bot, img)
    m[str(i)] = {"set": name, "a": aname if order == 0 else bname, "b": bname if order == 0 else aname, "views": views}
    open(W + "prompts/%s_%d.txt" % (rnd, i), "w", encoding="utf-8", newline="\n").write(
        PROMPT.format(img=img, n={2: "two", 3: "three", 4: "four", 5: "five"}[len(views)], who="; ".join(v[4] for v in views), out="%s/review_%d.md" % (out_dir, i)))
    print(i, name, m[str(i)]["a"], m[str(i)]["b"], size)
json.dump(m, open(W + "maps/%s_map.json" % rnd, "w"), indent=1)
