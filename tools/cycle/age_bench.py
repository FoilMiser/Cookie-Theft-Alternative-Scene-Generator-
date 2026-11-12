"""age_bench.py LIST.json OUT_FOLDER LABEL=RENDER_FOLDER [LABEL=RENDER_FOLDER ...] : the age bench (v0.49; vision/isolation_v049.md).
What would a reader call this person, and how old do they look? LIST.json is a list of [family, pose, expression, yaw] (v0.49: eight grown or
nearly grown people, each standing at three-quarter and walking in side view); each RENDER_FOLDER holds those variants of one cast as
<family>__<pose>__<expression>__y<yaw>.png, rendered at the release's 400 px per metre. Every cast's figures are drawn at 0.45 of that size in
strips of four different people numbered 1 to 4, the strips of all casts shuffled together. Writes OUT_FOLDER/strip_N.png and
OUT_FOLDER/prompt_N.txt (give each prompt to a fresh reader, who writes OUT_FOLDER/who_N.md), and the map of which strip is which cast to
<WORK>/age_map_<name of OUT_FOLDER>.json, outside the folder the readers are sent to. Count with age_tally.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK  # noqa: E402
import json, random
from PIL import Image, ImageDraw, ImageFont
L = json.load(open(sys.argv[1]))
out = os.path.abspath(sys.argv[2]).replace("\\", "/").rstrip("/") + "/"
casts = [a.split("=", 1) for a in sys.argv[3:]]
os.makedirs(out, exist_ok=True)
try:
    font = ImageFont.truetype("arial.ttf", 20)
except OSError:
    font = ImageFont.load_default()
rnd = random.Random(4907)
strips, mp = [], {}
for label, folder in casts:
    figs = L[:]
    rnd.shuffle(figs)
    groups = [[] for _ in range(max(1, len(L) // 4))]
    for f in figs:      # strips of four, no person twice in one
        g = min((g for g in groups if all(x[0] != f[0] for x in g)), key=len)
        g.append(f)
    strips += [(label, folder, g) for g in groups]
rnd.shuffle(strips)
for n, (label, folder, g) in enumerate(strips, 1):
    ims = []
    for fam, pose, ex, yaw in g:
        im = Image.open(os.path.join(folder, "%s__%s__%s__y%03d.png" % (fam, pose, ex, int(yaw)))).convert("RGBA")
        im = im.crop(im.getbbox())
        ims.append(im.resize((round(im.width * 0.45), round(im.height * 0.45)), Image.LANCZOS))
    H = max(i.height for i in ims) + 50
    sheet = Image.new("RGB", (190 * len(ims), H), (232, 236, 228))
    d = ImageDraw.Draw(sheet)
    for i, im in enumerate(ims):
        sheet.paste(im, (i * 190 + (190 - im.width) // 2, H - 40 - im.height), im)
        d.text((i * 190 + 88, H - 30), str(i + 1), fill=(20, 20, 20), font=font)
    sheet.save(out + "strip_%d.png" % n)
    mp[n] = {"cast": label, "figures": ["%s__%s__y%03d" % (f, p, int(y)) for f, p, _, y in g]}
    T = f"""You are taking part in a picture-legibility check. The image {out}strip_{n}.png shows four cartoon people, numbered 1 to 4, drawn small, the size they would have in a larger picture. The four are unrelated.

Look at that one image with the Read tool, as it opens: do not crop, zoom or enlarge it. Do not open any other file and do not search the folder.

Write the file {out}who_{n}.md with, for each of the four people in turn:
(a) what you would call this person in a word or two if you were describing the picture (for example: a man, a woman, a boy, a girl, a teenager, an old man, an old woman);
(b) roughly how old the person looks: a child, a teenager, a young adult, middle-aged, or older;
(c) what, if anything, is on the face or the head: glasses, a moustache, a beard, a hat, or nothing;
(d) how sure you are of (a): sure, fairly sure, or unsure, and what else the person could be.

Write what you see, not what you guess was meant. When the file is written, reply with just its path.
"""
    open(out + "prompt_%d.txt" % n, "w", encoding="utf-8", newline="\n").write(T)
mpath = os.path.join(WORK, "age_map_%s.json" % os.path.basename(out.rstrip("/")))
json.dump(mp, open(mpath, "w"), indent=1)
print(len(strips), "strips; map", mpath)
