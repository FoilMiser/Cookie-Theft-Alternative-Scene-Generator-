"""shares.py : the reviewers' shares for the v0.56 quality check.

Writes tpdb_work/review56/list_set.txt, list_grey.txt, list_p1.txt to list_p3.txt (the 78 probes dealt round-robin by name) and the
cast library's sheets (lib/sheet_NN.png with lib/index.txt). Run from the repo root."""
import glob, json, os
from PIL import Image, ImageDraw

ROOT = "E:/Cognitive_Test_Scene_Creator"
OUT = "tpdb_work/review56"
os.makedirs(OUT + "/lib", exist_ok=True)


def line(folder, name, grey=False):
    r = json.load(open(f"{folder}/{name}.json", encoding="utf-8"))
    ev = ", ".join(f"{t['id']} [{t['kind']}]" for t in r["templates"])
    pic = f"{ROOT}/{folder}/{name}{'_gray' if grey else ''}.png"
    return f"{pic}  (record {folder}/{name}.json; tier {r['tier']} {r['setting']}; events: {ev})"


setn = sorted(os.path.basename(p)[:-5] for p in glob.glob("scenes/T*.json"))
prob = sorted(os.path.basename(p)[:-5] for p in glob.glob("probes/*.json"))
assert len(setn) == 21 and len(prob) == 78, (len(setn), len(prob))
open(f"{OUT}/list_set.txt", "w", encoding="utf-8", newline="\n").write("\n".join(line("scenes", n) for n in setn) + "\n")
open(f"{OUT}/list_grey.txt", "w", encoding="utf-8", newline="\n").write("\n".join(line("scenes", n, True) for n in setn) + "\n")
for k in range(3):
    part = prob[k::3]
    open(f"{OUT}/list_p{k + 1}.txt", "w", encoding="utf-8", newline="\n").write("\n".join(line("probes", n) for n in part) + "\n")
    print("p%d" % (k + 1), len(part))

# the library's sheets: one family after another, twelve sprites a sheet, every sprite at one scale (so sizes compare) on the grass's green
vs = sorted(os.path.basename(p)[:-5] for p in glob.glob("assets/cast/lib055/*.json"))
assert len(vs) == 355, len(vs)
COLS, ROWS, TW, TH, LAB = 6, 2, 300, 520, 44
idx, sheet, n = [], None, 0
for i, v in enumerate(vs):
    k = i % (COLS * ROWS)
    if k == 0:
        if sheet:
            sheet.save(f"{OUT}/lib/sheet_{n:02d}.png")
        n += 1
        sheet = Image.new("RGB", (COLS * TW, ROWS * (TH + LAB)), (126, 178, 96))
        d = ImageDraw.Draw(sheet)
    im = Image.open(f"assets/cast/lib055/{v}.png").convert("RGB")
    mk = Image.open(f"assets/cast/lib055/{v}.mask.png").convert("L")
    s = min(0.66, (TW - 12) / im.width, (TH - 12) / im.height)          # a person 711 px tall is drawn 469; small animals are not blown up
    im2 = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    mk2 = mk.resize(im2.size, Image.LANCZOS)
    x0, y0 = (k % COLS) * TW, (k // COLS) * (TH + LAB)
    sheet.paste(im2, (x0 + (TW - im2.width) // 2, y0 + TH - 6 - im2.height), mk2)
    d.rectangle([x0, y0 + TH, x0 + TW - 1, y0 + TH + LAB - 1], fill=(255, 255, 255))
    fam, rest = v.split("__", 1)
    d.text((x0 + 4, y0 + TH + 4), fam, fill=(0, 0, 0))
    d.text((x0 + 4, y0 + TH + 22), rest, fill=(0, 0, 0))
    idx.append(f"sheet_{n:02d} tile {k + 1} (row {k // COLS + 1}, column {k % COLS + 1}): {v}")
sheet.save(f"{OUT}/lib/sheet_{n:02d}.png")
open(f"{OUT}/lib/index.txt", "w", encoding="utf-8", newline="\n").write("\n".join(idx) + "\n")
print(n, "sheets")
