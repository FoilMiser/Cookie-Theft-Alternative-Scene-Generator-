"""Summarize scored blind screens into vision/screen_summary.json for the site and README.

    python vision/summarize_screen.py vision/v04:scenes_v04 vision/v05:scenes_v05 vision/v06:scenes,probes

Each argument is a screen folder, optionally followed by the folder(s) holding its scene records
(needed for the per-template breakdown). Probe pictures (records marked "probe") count toward the
per-template breakdown only; the headline figures cover the set.
"""
import glob
import json
import os
import re
import sys

TYPES = {"entity": "entity", "action": "action", "inference": "inference",
         "contradiction_notice": "contradiction", "contradiction_explain": "contradiction"}


def record(dirs, name):
    for sd in dirs:
        f = os.path.join(sd, name + ".json")
        if os.path.exists(f):
            return json.load(open(f))
    return None


def by_template(d, dirs, scores):
    """Mean score of every template's action, inference and contradiction items (setting entities left out)."""
    km = json.load(open(os.path.join(d, "key_map.json")))
    out = {}
    for pic, name in km.items():
        r = record(dirs, name)
        if r is None:
            continue
        for it in r["items"]:
            t = it.get("template")
            if not t or t == "setting":
                continue
            v = scores.get(pic, {}).get("items", {}).get(it["id"], {}).get("score", 0)
            v = 0.0 if isinstance(v, str) else float(v)
            o = out.setdefault(t, {"all": [], "meaning": []})
            o["all"].append(v)
            if it["type"] in ("inference", "contradiction_notice", "contradiction_explain"):
                o["meaning"].append(v)
    return {t: {"items": len(o["all"]), "mean": round(sum(o["all"]) / len(o["all"]), 3),
                "meaning_items": len(o["meaning"]),
                "meaning_mean": round(sum(o["meaning"]) / len(o["meaning"]), 3) if o["meaning"] else None}
            for t, o in sorted(out.items())}


def remarks(d):
    """The readers' own remarks per picture: the bullets of each description's "unsure" section, counted directly, over every
    screened picture. Unlike the oddities, it does not depend on how much a scorer logs (v0.24: 83% of them, v0.23: 22%).
    v0.26: a bullet that only says nothing is wrong is no remark ("Nothing is floating or passing through anything else": 25 of
    v0.25's 428, 2 of v0.24's 408, which made v0.25's rise look like 11% where the remarks themselves rose 5%)."""
    n = []
    for f in glob.glob(os.path.join(d, "desc_pic_*.md")):
        parts = re.split(r"(?i)unsure or ambiguous", open(f, encoding="utf-8").read(), maxsplit=1)
        bullets = re.findall(r"(?m)^\s*(?:[-*]|\d+\.)\s+(.*)$", parts[1]) if len(parts) > 1 else []
        n.append(sum(1 for b in bullets if not re.match(r"(?i)(nothing|no (other )?(object|thing|element)s?\b|i see nothing|apart from\b.*nothing)", b.lstrip("*_ "))))
    return round(sum(n) / len(n), 2) if n else None


def summarize(d, scenes_dir=None):
    scores = json.load(open(os.path.join(d, "scores.json")))
    keys = json.load(open(os.path.join(d, "keys.json")))
    km = json.load(open(os.path.join(d, "key_map.json")))
    dirs = scenes_dir.split(",") if scenes_dir else []
    probes = {pic for pic, name in km.items() if dirs and (record(dirs, name) or {}).get("probe")}
    by, mis, odd, n = {}, 0, 0, 0
    for pic, k in keys.items():
        if pic in probes:
            continue
        sc = scores.get(pic, {})
        for it in k["items"]:
            r = sc.get("items", {}).get(it["id"], {})
            v = r.get("score", 0)
            if v == "misread" or isinstance(v, str):
                mis += 1
                v = 0.0
            by.setdefault(TYPES[it["type"]], []).append(float(v))
            n += 1
        odd += len(sc.get("unintended", []))
    mean = {t: round(sum(v) / len(v), 3) for t, v in by.items()}
    allv = [x for v in by.values() for x in v]
    mean["overall"] = round(sum(allv) / len(allv), 3)
    res = {"pictures": len(keys) - len(probes), "items": n, "mean": mean, "misreads": mis, "oddities": odd}
    if probes:
        res["probes"] = {"pictures": len(probes), "oddities": sum(len(scores.get(p, {}).get("unintended", [])) for p in probes)}
    if dirs:
        res["by_template"] = by_template(d, dirs, scores)
    return res


args = [a for a in sys.argv[1:] if a != "--add"]
path = os.path.join(os.path.dirname(args[0].partition(":")[0].rstrip("/")), "screen_summary.json")
# --add: keep the earlier screens' figures (their scene records are in their own releases, not in this package)
out = json.load(open(path)) if "--add" in sys.argv else {}
out.pop("note", None)
for arg in args:
    d, _, sd = arg.partition(":")
    out[os.path.basename(d.rstrip("/"))] = summarize(d, sd or None)
for k, v in out.items():
    v["remarks"] = remarks(os.path.join(os.path.dirname(path), k))
out["note"] = ("Readers were AI models given only the picture (no key); a separate model scored their descriptions. "
               "Contradictions are scored as caught when the reader called the thing wrong or impossible.")
json.dump(out, open(path, "w", newline="\n"), indent=1)
print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "by_template"} if isinstance(v, dict) else v for k, v in out.items()}, indent=1))
