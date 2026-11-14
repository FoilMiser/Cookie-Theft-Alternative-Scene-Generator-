"""(v0.55's own script: its sets, its prompt and its paths are written in. Edit them.)
fig_pairs.py ROUND A_DIR B_DIR A_NAME B_NAME [SETS.json] : a blind pair bench of two drawings of the same seated figures.

For every set of four views in SETS (default: the six sets below) two sheets are made, one with A_DIR's renders as row a and B_DIR's as
row b and one the other way round; each sheet has every figure whole and large and, under it, the same figure at the size it has in a
picture. Sheets go to vision/isolation_v055/<ROUND>/pair_N.png in a shuffled order, the prompts to tpdb_work/v055/prompts/<ROUND>_N.txt,
and the map (which row is which, in which sheet) to tpdb_work/v055/maps/<ROUND>_map.json, outside the folder a reviewer may see.
With RENDER_LIST=path the views of the sets are written there as a render list and nothing else is done."""
import json, os, random, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = "E:/Cognitive_Test_Scene_Creator/"
W = ROOT + "tpdb_work/v055/"
SETS = {
    "bench_trousers": [("ben", "sit_read", "neutral", 45, "a man reading on a seat"), ("ana", "sit_ice_cream", "happy", 45, "a woman eating an ice cream on a seat"),
                       ("tomas", "sit_drink", "smile", 45, "an older man with a drink on a seat"), ("leo", "sit_read", "neutral", 45, "a teenager reading on a seat")],
    "bench_bare": [("mei", "sit_read", "neutral", 45, "a woman in a dress reading on a seat"), ("rosa", "sit_ice_cream", "smile", 45, "an older woman in a skirt eating an ice cream on a seat"),
                   ("kai", "sit_ice_cream", "happy", 45, "a child in shorts eating an ice cream on a seat"), ("nia", "sit_drink", "content", 45, "a girl in a dress with a drink on a seat")],
    "side_trousers": [("ben", "sit_read", "neutral", 90, "a man reading on a seat, from the side"), ("dev", "sit", "smile", 90, "a bearded man sitting, from the side"),
                      ("jo", "sit_read", "neutral", 90, "a worker in a safety vest reading on a seat, from the side"), ("tomas", "sit", "smile", 90, "an older man sitting, from the side")],
    "side_bare": [("kai", "sit", "smile", 90, "a child in shorts sitting, from the side"), ("nia", "sit", "smile", 90, "a girl in a dress sitting, from the side"),
                  ("mei", "sit_read", "neutral", 90, "a woman in a dress reading on a seat, from the side"), ("rosa", "sit", "smile", 90, "an older woman in a skirt sitting, from the side")],
    "seesaw": [("dev", "seesaw_low_read", "neutral", 90, "a bearded man reading, sitting on the low end of a seesaw"),
               ("tomas", "seesaw_low_read", "neutral", 90, "an older man reading, sitting on the low end of a seesaw"),
               ("nia", "seesaw_stuck_call", "calling", 90, "a girl sitting on the high end of a seesaw, her legs hanging"),
               ("kai", "seesaw_stuck_call", "calling", 90, "a child sitting on the high end of a seesaw, the legs hanging")],
    "play": [("kai", "sit_swing", "happy", 0, "a child on a swing, from the front"), ("nia", "sit_swing", "laughing", 0, "a girl on a swing, from the front"),
             ("kai", "slide_down", "smile", 90, "a child sliding down a slide, from the side"), ("nia", "slide_down", "smile", 90, "a girl sliding down a slide, from the side")],
}
if os.environ.get("RENDER_LIST"):
    rows = sorted({("person." + v[0], v[1], v[2], v[3]) for s in SETS.values() for v in s})
    json.dump([list(r) for r in rows], open(os.environ["RENDER_LIST"], "w"))
    print(len(rows), "views")
    sys.exit(0)
rnd, adir, bdir, aname, bname = sys.argv[1:6]
if len(sys.argv) > 6:
    SETS = json.load(open(sys.argv[6]))
PPM = 800.0
BIG = 600
try:
    FONT = ImageFont.truetype("arial.ttf", 44)
except OSError:
    FONT = ImageFont.load_default()


def tile(d, v):
    f = "%s/person.%s__%s__%s__y%03d.png" % (d, v[0], v[1], v[2], v[3])
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


PROMPT = """You are reviewing drawings for a set of cartoon pictures. The image {img} shows the same four seated figures drawn two ways: row a above and row b below. Under each large drawing the same figure is shown at the size it has in a picture. The figures are the same in both rows, left to right: {who}. The seat itself is not drawn. Only the lower body differs between the rows: the seat of the figure, the thighs, the knees, the lower legs and where the feet are.

Look at that one image with the Read tool. Do not open any other file and do not search or list the folder.

Write your review to {out} with the Write tool, with these parts:

1. In two or three sentences, how the two rows differ.
2. For each of the four figures, left to right: which row draws its seated lower body better (a, b or no difference) and one sentence of reason.
3. The faults of row a, and the faults of row b, in how the seat, the thighs, the knees, the lower legs and the feet are drawn, each as a short list that names the figure. Add anything else in a figure that looks wrong to you.
4. Which row you would choose for a friendly, clear cartoon style, and how sure you are (sure, fairly sure, or a toss-up).

Write what you see in the drawing, not what you guess the artist meant. When the file is written, reply on one line with your choice (a or b), how sure you are, and the count of figures you gave to a, to b and to no difference.
"""

out_dir = ROOT + "vision/isolation_v055/" + rnd
os.makedirs(out_dir, exist_ok=True)
os.makedirs(W + "prompts", exist_ok=True)
os.makedirs(W + "maps", exist_ok=True)
jobs = [(name, order) for name in SETS for order in (0, 1)]
random.Random("v055" + rnd).shuffle(jobs)
m = {}
for i, (name, order) in enumerate(jobs, 1):
    views = SETS[name]
    top, bot = (adir, bdir) if order == 0 else (bdir, adir)
    img = "%s/pair_%d.png" % (out_dir, i)
    size = sheet(views, W + top, W + bot, img)
    m[str(i)] = {"set": name, "a": aname if order == 0 else bname, "b": bname if order == 0 else aname, "views": views}
    open(W + "prompts/%s_%d.txt" % (rnd, i), "w", encoding="utf-8", newline="\n").write(
        PROMPT.format(img=img, who="; ".join(v[4] for v in views), out="%s/review_%d.md" % (out_dir, i)))
    print(i, name, m[str(i)]["a"], m[str(i)]["b"], size)
json.dump(m, open(W + "maps/%s_map.json" % rnd, "w"), indent=1)
