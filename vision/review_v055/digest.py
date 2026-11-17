"""digest.py : the last three screens side by side, picture by picture.

For every picture of the v0.55 screen: its templates, and for each of v0.53, v0.54 and v0.55 the reader's unsure lines, the scorer's
oddities, the judgement calls and the items under full marks. Says whether the picture is the earlier release's to the pixel.
Writes tpdb_work/review56/screens_digest.md and screens_digest.json. Run from the repo root."""
import glob, hashlib, json, os, re

SCREENS = ["v053", "v054", "v055"]
PICDIR = {"v053": ("scenes_v053", "probes_v053"), "v054": ("scenes_v054", "probes_v054"), "v055": ("scenes", "probes")}
OUT = "tpdb_work/review56"


def jload(p):
    return json.load(open(p, encoding="utf-8"))


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None


def png(v, name):
    for d in PICDIR[v]:
        p = os.path.join(d, name + ".png")
        if os.path.exists(p):
            return p
    return None


def unsure(v, pic):
    p = f"vision/{v}/desc_{pic}.md"
    if not os.path.exists(p):
        return []
    t = open(p, encoding="utf-8").read()
    m = re.search(r"^## Unsure[^\n]*\n(.*?)(?=^## |\Z)", t, re.S | re.M)
    if not m:
        return []
    return [l.strip() for l in m.group(1).splitlines() if l.strip()]


def calls(v):
    """pic -> [(id, target, why)] from the scorers' 'Judgement calls scored 1' tables"""
    out = {}
    for p in sorted(glob.glob(f"vision/{v}/scores_summary_*.md")):
        t = open(p, encoding="utf-8").read()
        m = re.search(r"^## Judgement calls[^\n]*\n(.*?)(?=^## |\Z)", t, re.S | re.M)
        if not m:
            continue
        for l in m.group(1).splitlines():
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if len(c) >= 4 and re.match(r"pic_\d+", c[0]):
                out.setdefault(c[0], []).append((c[1], c[2], c[3]))
    return out


maps = {v: jload(f"vision/{v}/key_map.json") for v in SCREENS}
inv = {v: {n: p for p, n in maps[v].items()} for v in SCREENS}
scores = {v: jload(f"vision/{v}/scores.json") for v in SCREENS}
keys = {v: jload(f"vision/{v}/keys.json") for v in SCREENS}
jc = {v: calls(v) for v in SCREENS}

names = [maps["v055"][p] for p in sorted(maps["v055"])]
dig, lines = {}, []
for name in names:
    rec = None
    for d in PICDIR["v055"]:
        q = os.path.join(d, name + ".json")
        if os.path.exists(q):
            rec = jload(q)
            where = d
    tids = [t["id"] for t in rec["templates"]]
    h = {v: md5(png(v, name)) if png(v, name) else None for v in SCREENS}
    same = {"v054": h["v054"] is not None and h["v054"] == h["v053"], "v055": h["v055"] == h["v054"]}
    e = {"name": name, "folder": where, "tier": rec["tier"], "setting": rec["setting"], "templates": tids, "screens": {}}
    kinds = ", ".join(f"{t['id']} [{t['kind']}]" for t in rec["templates"])
    lines.append(f"## {name}  ({where}; tier {rec['tier']} {rec['setting']}; {kinds})")
    for v in SCREENS:
        pic = inv[v].get(name)
        if not pic:
            lines.append(f"- {v}: not screened")
            continue
        sc = scores[v][pic]
        kk = {i["id"]: i for i in keys[v][pic]["items"]}
        low = [(i, kk[i]["type"], kk[i]["text"], x["score"], x.get("note", "")) for i, x in sorted(sc["items"].items()) if x["score"] != 1]
        tag = "" if v == "v053" else (" [same picture as before]" if same[v] else " [picture changed]")
        e["screens"][v] = {"pic": pic, "same_as_prev": same.get(v), "unsure": unsure(v, pic), "odd": sc.get("unintended", []),
                           "calls": jc[v].get(pic, []), "low": low}
        lines.append(f"### {v} {pic}{tag}")
        for u in e["screens"][v]["unsure"]:
            lines.append(f"  U {u}")
        for o in e["screens"][v]["odd"]:
            lines.append(f"  O {o}")
        for c in e["screens"][v]["calls"]:
            lines.append(f"  J {c[0]} {c[1]} :: {c[2]}")
        for l in low:
            lines.append(f"  L {l[0]} [{l[1]}] {l[2]} = {l[3]} :: {l[4]}")
    lines.append("")
    dig[name] = e
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "screens_digest.md"), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
json.dump(dig, open(os.path.join(OUT, "screens_digest.json"), "w", encoding="utf-8"), indent=1)
nu = sum(len(s["unsure"]) for e in dig.values() for s in e["screens"].values())
no = sum(len(s["odd"]) for e in dig.values() for s in e["screens"].values())
nj = sum(len(s["calls"]) for e in dig.values() for s in e["screens"].values())
nl = sum(len(s["low"]) for e in dig.values() for s in e["screens"].values())
print(len(dig), "pictures;", nu, "unsure lines;", no, "oddities;", nj, "calls;", nl, "items under full marks")
print("screened in all three:", sum(1 for e in dig.values() if len(e["screens"]) == 3))
print("same picture v053=v054:", sum(1 for e in dig.values() if e["screens"].get("v054", {}).get("same_as_prev")),
      "v054=v055:", sum(1 for e in dig.values() if e["screens"]["v055"]["same_as_prev"]))
