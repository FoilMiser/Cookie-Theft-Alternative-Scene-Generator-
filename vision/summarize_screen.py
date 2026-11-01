"""Summarize scored blind screens into vision/screen_summary.json for the site and README.

    python vision/summarize_screen.py vision/v04:scenes_v04 vision/v05:scenes_v05 vision/v06:scenes,probes

Each argument is a screen folder, optionally followed by the folder(s) holding its scene records
(needed for the per-template breakdown). Probe pictures (records marked "probe") count toward the
per-template breakdown only; the headline figures cover the set.
"""
import json
import os
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


out = {}
for arg in sys.argv[1:]:
    d, _, sd = arg.partition(":")
    out[os.path.basename(d.rstrip("/"))] = summarize(d, sd or None)
out["note"] = ("Readers were AI models given only the picture (no key); a separate model scored their descriptions. "
               "Contradictions are scored as caught when the reader called the thing wrong or impossible.")
json.dump(out, open(os.path.join(os.path.dirname(sys.argv[1].partition(":")[0].rstrip("/")), "screen_summary.json"), "w"), indent=1)
print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "by_template"} if isinstance(v, dict) else v for k, v in out.items()}, indent=1))
