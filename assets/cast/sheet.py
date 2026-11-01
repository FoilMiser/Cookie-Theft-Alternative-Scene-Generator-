"""Lay rendered variants side by side on a light background, scaled to a common height."""
import sys, json, glob, os
from PIL import Image
def sheet(paths, out, h=520, bg=(238, 242, 233), gap=18, cols=None):
    ims = []
    for p in paths:
        im = Image.open(p).convert('RGBA')
        k = h / 770
        im = im.resize((max(1, int(im.width * k)), max(1, int(im.height * k))), Image.LANCZOS)
        ims.append(im)
    cols = cols or len(ims)
    rows = [ims[i:i + cols] for i in range(0, len(ims), cols)]
    W = max(sum(i.width for i in r) + gap * (len(r) + 1) for r in rows)
    H = sum(max(i.height for i in r) + gap for r in rows) + gap
    S = Image.new('RGBA', (W, H), bg + (255,))
    y = gap
    for r in rows:
        rh = max(i.height for i in r); x = gap
        for i in r:
            S.alpha_composite(i, (x, y + rh - i.height)); x += i.width + gap
        y += rh + gap
    S.convert('RGB').save(out)
    return S.size
if __name__ == '__main__':
    print(sheet(sys.argv[2:], sys.argv[1]))
