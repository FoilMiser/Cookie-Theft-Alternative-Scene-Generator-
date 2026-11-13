"""(v0.52's own script, kept in tools/cycle as the model for the next bench of how a figure is drawn: its sets, its prompt and its paths are
written in. Edit them.)
fig_pairs.py ROUND A_DIR B_DIR A_NAME B_NAME [SETS.json] : a blind pair bench of two drawings of the same figures.

For every set of four views in SETS (default: the six sets below) two sheets are made, one with A_DIR's renders as row a and B_DIR's as
row b and one the other way round; each sheet has the upper part of every figure large and, under it, the whole figure at the size it has
in a picture. Sheets go to vision/isolation_v052/<ROUND>/pair_N.png in a shuffled order, the prompts to tpdb_work/v052/prompts/<ROUND>_N.txt,
and the map (which row is which, in which sheet) to tpdb_work/v052/maps/<ROUND>_map.json, outside the folder a reviewer may see."""
import json, os, random, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = "E:/Cognitive_Test_Scene_Creator/"
W = ROOT + "tpdb_work/v052/"
rnd, adir, bdir, aname, bname = sys.argv[1:6]
SETS = {
    "tee_stand_1": [("ben", "stand", 0, "a man from the front"), ("ben", "stand", 45, "the same man turned"), ("ben", "stand", 90, "the same man from the side"),
                    ("ana", "stand", 180, "a woman from behind")],
    "tee_stand_2": [("kai", "stand", 0, "a child from the front"), ("mei", "stand", 45, "a woman in a dress, turned"), ("nia", "stand", 90, "a girl from the side"),
                    ("dev", "stand", 45, "a bearded man, turned")],
    "tee_up": [("ben", "wave", 45, "a man waving"), ("ana", "reach_up", 45, "a woman reaching up"), ("kai", "point_up", 90, "a child pointing up, from the side"),
               ("ben", "hang_washing", 45, "a man with both arms raised")],
    "tee_work": [("mei", "catch", 90, "a woman with both arms held out, from the side"), ("dev", "sweep", 45, "a man sweeping"),
                 ("ana", "throw_ball", 90, "a woman who has just thrown, from the side"), ("nia", "push", 90, "a girl pushing, from the side")],
    "long_stand": [("leo", "stand", 0, "a teenager in a hooded top, from the front"), ("rosa", "stand", 45, "an older woman in a cardigan, turned"),
                   ("tomas", "stand", 90, "an older man in a waistcoat, from the side"), ("jo", "stand", 45, "a worker in a safety vest, turned")],
    "long_act": [("leo", "wave", 45, "a teenager waving"), ("rosa", "reach_up", 45, "an older woman reaching up"), ("tomas", "sweep", 45, "an older man sweeping"),
                 ("leo", "catch", 90, "a teenager with both arms held out, from the side")],
}
if len(sys.argv) > 6:
    SETS = json.load(open(sys.argv[6]))
PPM = 800.0
BIG, FRAC = 640, 0.62
try:
    FONT = ImageFont.truetype("arial.ttf", 44)
except OSError:
    FONT = ImageFont.load_default()


def tile(d, v):
    f = "%s/person.%s__%s__neutral__y%03d.png" % (d, v[0], v[1], v[2])
    im = Image.open(f).convert("RGBA")
    im = im.crop(im.getbbox())
    up = im.crop((0, 0, im.width, round(im.height * FRAC)))
    s = BIG / up.height
    big = up.resize((round(up.width * s), BIG), Image.LANCZOS)
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
            im.paste(big, (x + (cw - big.width) // 2, y), big)
            im.paste(small, (x + (cw - small.width) // 2, y + BIG + 16 + sh - small.height), small)
        if ri == 0:
            d.line((0, rh, im.width, rh), fill=(150, 150, 150), width=3)
    im.save(out)
    return im.size


PROMPT = """You are reviewing drawings for a set of cartoon pictures. The image {img} shows the same four figures drawn two ways: row a above and row b below. Under each large drawing the same figure is shown whole, at the size it has in a picture. The figures are the same in both rows, left to right: {who}. Only the upper arms, the shoulders and the sleeves differ between the rows.

Look at that one image with the Read tool. Do not open any other file and do not search or list the folder.

Write your review to {out} with the Write tool, with these parts:

1. In two or three sentences, how the two rows differ.
2. For each of the four figures, left to right: which row draws its upper arms, shoulders and sleeves better (a, b or no difference) and one sentence of reason.
3. The faults of row a, and the faults of row b, in how the upper arms, the shoulders and the sleeves are drawn, each as a short list that names the figure. Add anything else in a figure that looks wrong to you.
4. Which row you would choose for a friendly, clear cartoon style, and how sure you are (sure, fairly sure, or a toss-up).

Write what you see in the drawing, not what you guess the artist meant. When the file is written, reply on one line with your choice (a or b), how sure you are, and the count of figures you gave to a, to b and to no difference.
"""

out_dir = ROOT + "vision/isolation_v052/" + rnd
os.makedirs(out_dir, exist_ok=True)
os.makedirs(W + "prompts", exist_ok=True)
os.makedirs(W + "maps", exist_ok=True)
jobs = [(name, order) for name in SETS for order in (0, 1)]
random.Random("v052" + rnd).shuffle(jobs)
m = {}
for i, (name, order) in enumerate(jobs, 1):
    views = SETS[name]
    top, bot = (adir, bdir) if order == 0 else (bdir, adir)
    img = "%s/pair_%d.png" % (out_dir, i)
    size = sheet(views, W + top, W + bot, img)
    m[str(i)] = {"set": name, "a": aname if order == 0 else bname, "b": bname if order == 0 else aname, "views": views}
    open(W + "prompts/%s_%d.txt" % (rnd, i), "w", encoding="utf-8", newline="\n").write(
        PROMPT.format(img=img, who="; ".join(v[3] for v in views), out="%s/review_%d.md" % (out_dir, i)))
    print(i, name, m[str(i)]["a"], m[str(i)]["b"], size)
json.dump(m, open(W + "maps/%s_map.json" % rnd, "w"), indent=1)
