"""Apply the legibility gate to a scored blind screen.

    python vision/gate.py vision/v07 scenes,probes

A template passes when its scored items (setting entities left out) average at least 0.9, it appeared
in at least two screened pictures, and none of its items was misread. Writes <screen>/gate.json.
"""
import collections
import json
import os
import sys

MEAN, PICTURES = 0.9, 2


def record(dirs, name):
    for d in dirs:
        f = os.path.join(d, name + ".json")
        if os.path.exists(f):
            return json.load(open(f))
    return None


def gate(screen, dirs):
    km = json.load(open(os.path.join(screen, "key_map.json")))
    sc = json.load(open(os.path.join(screen, "scores.json")))
    vals, pics, mis = collections.defaultdict(list), collections.defaultdict(set), collections.Counter()
    for pic, name in km.items():
        r = record(dirs, name)
        if r is None:
            continue
        for it in r["items"]:
            t = it.get("template")
            if not t or t == "setting":
                continue
            v = sc.get(pic, {}).get("items", {}).get(it["id"], {}).get("score", 0)
            if isinstance(v, str):
                mis[t] += 1
                v = 0.0
            vals[t].append(float(v))
            pics[t].add(pic)
    out = {}
    for t in sorted(vals):
        m = sum(vals[t]) / len(vals[t])
        status = "pass" if m >= MEAN and len(pics[t]) >= PICTURES and mis[t] == 0 else (
            "too_few" if m >= MEAN and mis[t] == 0 else "fail")
        out[t] = {"mean": round(m, 3), "items": len(vals[t]), "pictures": len(pics[t]), "misreads": mis[t], "status": status}
    return out


if __name__ == "__main__":
    screen, dirs = sys.argv[1], sys.argv[2].split(",")
    g = gate(screen, dirs)
    json.dump(g, open(os.path.join(screen, "gate.json"), "w"), indent=1)
    c = collections.Counter(v["status"] for v in g.values())
    print(dict(c))
    for t, v in g.items():
        if v["status"] != "pass":
            print(t, v)
