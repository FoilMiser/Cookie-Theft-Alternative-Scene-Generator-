"""greyaudit.py : for every scored or cue element of the 99 pictures, the grey level of its largest fills against the grey of what is
around it. A rough audit: an element's own colours are those in its box that are not the outline's and not the surround's most common
colour; flagged when its largest own fill is within 12 grey levels of the surround. Run from the repo root."""
import glob, json, os, collections
from PIL import Image
OUTLINE = (38, 38, 46)
km = {n: p for p, n in json.load(open("vision/v055/key_map.json", encoding="utf-8")).items()}
rows = []
for f in sorted(glob.glob("scenes/T*.json")) + sorted(glob.glob("probes/*.json")):
    name = os.path.basename(f)[:-5]; folder = os.path.dirname(f)
    r = json.load(open(f, encoding="utf-8"))
    c = Image.open(f"{folder}/{name}.png").convert("RGB"); g = Image.open(f"{folder}/{name}_gray.png").convert("L")
    cp, gp = c.load(), g.load()
    for e in r["elements"]:
        b = e.get("bbox")
        if not b or e.get("role") not in ("scored", "cue", "prop"):
            continue
        x0, y0, x1, y1 = [int(v) for v in b]
        x0, y0, x1, y1 = max(0, x0), max(0, y0), min(1600, x1), min(1000, y1)
        if x1 - x0 < 6 or y1 - y0 < 6:
            continue
        ins = collections.Counter()
        for y in range(y0, y1, 2):
            for x in range(x0, x1, 2):
                ins[(cp[x, y], gp[x, y])] += 1
        ring = collections.Counter()
        P = 24
        for y in range(max(0, y0 - P), min(1000, y1 + P), 2):
            for x in range(max(0, x0 - P), min(1600, x1 + P), 2):
                if not (x0 <= x < x1 and y0 <= y < y1):
                    ring[(cp[x, y], gp[x, y])] += 1
        if not ring:
            continue
        (bc, bg), _ = ring.most_common(1)[0]
        own = [(k, n) for k, n in ins.most_common(8) if k[0] != OUTLINE and k[0] != bc]
        if not own:
            continue
        tot = sum(n for _, n in own)
        (oc, og), on = own[0]
        if abs(og - bg) <= 12 and on / tot >= 0.30:
            rows.append((abs(og - bg), km[name], name, e["id"], e.get("label", "")[:40], oc, og, bc, bg, round(on / tot, 2)))
by = collections.defaultdict(list)
for r_ in rows:
    key = "".join(ch for ch in r_[3] if not ch.isdigit()).rstrip("_")
    by[key].append(r_)
print(len(rows), "elements flagged in", len(set(r_[2] for r_ in rows)), "pictures")
for key, v in sorted(by.items(), key=lambda kv: -len(kv[1])):
    ex = sorted(v)[0]
    print("  %-16s %2d pictures; e.g. %s %s: own %s grey %d on %s grey %d (share %.2f) [%s]" % (key, len(v), ex[1], ex[4], ex[5], ex[6], ex[7], ex[8], ex[9], ",".join(sorted(set(x[1][4:] for x in v)))[:60]))
