"""Crop named elements out of built pictures and lay them out on one sheet.

    python tools/cycle/crops.py OUT.png [SCALE] NAME:substr[:pad] NAME:substr ...

NAME is a record's name (looked for in scenes, probes, then any folder given by CROP_DIRS, comma-separated); substr is
matched against an element's id or label; every match is boxed together. A NAME with no match is cropped whole.
"""
import json, os, sys
from PIL import Image, ImageDraw

DIRS = [d for d in os.environ.get("CROP_DIRS", "scenes,probes").split(",") if d]


def find(name):
    for d in DIRS:
        p = os.path.join(d, name + ".json")
        if os.path.exists(p):
            return json.load(open(p, encoding="utf-8")), os.path.join(d, name + ".png")
    raise SystemExit("no record " + name)


def main():
    out = sys.argv[1]
    args = sys.argv[2:]
    scale = 1.0
    if args and args[0].replace(".", "").isdigit():
        scale = float(args.pop(0))
    tiles = []
    for a in args:
        parts = a.split(":")
        name, sub = parts[0], parts[1] if len(parts) > 1 else ""
        pad = int(parts[2]) if len(parts) > 2 else 40
        rec, png = find(name)
        im = Image.open(png).convert("RGB")
        bbs = [e["bbox"] for e in rec["elements"] if e.get("bbox") and sub and any(s_ in e["id"] or s_ in e.get("label", "") for s_ in sub.split("+"))]
        if bbs:
            b = (min(x[0] for x in bbs) - pad, min(x[1] for x in bbs) - pad, max(x[2] for x in bbs) + pad, max(x[3] for x in bbs) + pad)
            b = (max(0, int(b[0])), max(0, int(b[1])), min(im.width, int(b[2])), min(im.height, int(b[3])))
            im = im.crop(b)
        if scale != 1.0:
            im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
        tiles.append((a, im))
    W = 1900
    x = y = rowh = 0
    pos = []
    for a, im in tiles:
        if x + im.width > W and x > 0:
            x, y, rowh = 0, y + rowh + 26, 0
        pos.append((x, y))
        x += im.width + 10
        rowh = max(rowh, im.height)
    H = y + rowh + 26
    sheet = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(sheet)
    for (a, im), (px, py) in zip(tiles, pos):
        sheet.paste(im, (px, py + 16))
        d.text((px + 2, py + 2), a, fill="black")
    sheet.save(out)
    print(out, sheet.size, len(tiles))


main()
