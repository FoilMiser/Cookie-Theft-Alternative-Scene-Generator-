"""carry_over.py SRC OUT [name,name,...] : a like-for-like release (v0.57). Every record of SRC (the last release's `scenes` or `probes`) is
built again under THIS release's placement revision from its own regeneration data: the same base seed, the same history of template
use, the same forced set and the same number of tries. A picture that this release's drawings and rules do not touch comes back to the
pixel; one whose drawing changed comes back with the same plan and the new drawing; one that a new rule or a new box stops on its seed
goes on to the next try of its own search, and if none places it is reported FAILED and has to be found by hand (forced_cell.py,
more_probes.py). An isomorph is built again from its source's new record, with its own seed.

Each record's regeneration data is its own, so nothing cascades: in the showcase pass a cell that moves changes the history of template
use for every cell after it, and the probes follow the set (RUNBOOK, Lessons, v0.55).

Prints, for each record, SAME (to the pixel), DRAWN (same name, templates and cast, other pixels), MOVED (same name and templates, a
figure moved by more than 12 units or another cast), OTHER (another seed or other templates) or FAILED, and writes OUT/carry_over.json.
The summaries of SRC (showcase_summary.json, isomorph_summary.json) are copied with the entries of renamed records rewritten."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import glob, json, shutil, time
sys.path.insert(0, ROOT); os.chdir(ROOT)
from PIL import Image, ImageChops
from scenegen import generate as G
from scenegen import scene as SCN
from scenegen.batch import build_isomorph
from scenegen.library import Library

src, out = sys.argv[1], sys.argv[2]
only = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else None
REV = SCN.PLACEMENT_REV
os.makedirs(out, exist_ok=True)
# (a dry run before the release's cast and library exist: CARRY_CAST and CARRY_LIB name a trial cast and a scratch library)
lib = Library(cast_dir=os.environ["CARRY_CAST"], lib_dir=os.environ["CARRY_LIB"]) if os.environ.get("CARRY_CAST") else Library()
recs = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(os.path.join(src, "T*.json")))]
recs.sort(key=lambda r: 1 if r["regen"].get("isomorph_of") else 0)          # sources before their isomorphs
log_p = os.path.join(out, "carry_over.json")
state = json.load(open(log_p)) if os.path.exists(log_p) else {}


def same_pixels(a, b):
    return ImageChops.difference(Image.open(a).convert("RGB"), Image.open(b).convert("RGB")).getbbox() is None


for r0 in recs:
    name = r0["name"]
    if only and name not in only:
        continue
    if name in state and state[name]["verdict"] != "FAILED" and os.path.exists(os.path.join(out, state[name]["new"] + ".png")):
        continue
    g = r0["regen"]
    SCN.PLACEMENT_REV = REV
    t0 = time.time()
    why = None
    try:
        if g.get("isomorph_of"):
            a_new = state.get(g["isomorph_of"], {}).get("new")
            if not a_new:
                state[name] = {"verdict": "FAILED", "new": None, "why": "its source has no new record"}
                print(name, "FAILED: its source", g["isomorph_of"], "has no new record", flush=True)
                continue
            rec = build_isomorph(lib, json.load(open(os.path.join(out, a_new + ".json"), encoding="utf-8")), r0["setting"], g["seed"], out, log=lambda *a: None)
            if isinstance(rec, tuple):
                rec = rec[0]
            if isinstance(rec, dict) and "failed" in rec:
                why, rec = sorted(set(rec["failed"]))[:6], None
        else:
            G.USAGE.clear(); G.USAGE.update(g["usage"])
            rec, _, tried = G.build_one(lib, r0["tier"], r0["setting"], g["base_seed"], out, forced=g.get("forced"), require_band=g["require_band"],
                                        max_tries=g["max_tries"], placements=g["placements"], log=lambda *a: None)
            if rec is None:
                why = [str(x)[:200] for x in tried[-2:]]
    except Exception as e:
        import traceback
        traceback.print_exc()
        rec, why = None, [repr(e)[:300]]
    if rec is None:
        state[name] = {"verdict": "FAILED", "new": None, "why": why}
        print(name, "FAILED", why, f"{time.time() - t0:.0f}s", flush=True)
        json.dump(state, open(log_p, "w"), indent=1)
        continue
    new = rec["name"]
    p_new = os.path.join(out, new + ".json")
    if r0.get("probe") and not rec.get("probe"):
        rec = json.load(open(p_new, encoding="utf-8"))
        rec["probe"] = r0["probe"]
        json.dump(rec, open(p_new, "w"), indent=1)
    same_t = [t["id"] for t in rec["templates"]] == [t["id"] for t in r0["templates"]]
    v0 = sorted((e.get("asset") or {}).get("variant", "") for e in r0["elements"] if e.get("asset"))
    v1 = sorted((e.get("asset") or {}).get("variant", "") for e in rec["elements"] if e.get("asset"))
    b0 = {e["id"]: e.get("bbox") for e in r0["elements"] if e.get("bbox")}
    moved = [e["id"] for e in rec["elements"] if e.get("bbox") and e["id"] in b0 and max(abs(x - y) for x, y in zip(e["bbox"], b0[e["id"]])) > 12]
    if new != name or not same_t:
        verdict = "OTHER"
    elif same_pixels(os.path.join(src, name + ".png"), os.path.join(out, new + ".png")):
        verdict = "SAME"
    elif moved or v0 != v1:
        verdict = "MOVED"
    else:
        verdict = "DRAWN"
    state[name] = {"verdict": verdict, "new": new, "templates_same": same_t, "moved": moved[:8], "cast_same": v0 == v1}
    print(name, verdict, "->", new, "" if same_t else "TEMPLATES DIFFER", "moved %d %s" % (len(moved), moved[:4]) if moved else "", f"{time.time() - t0:.0f}s", flush=True)
    json.dump(state, open(log_p, "w"), indent=1)

json.dump(state, open(log_p, "w"), indent=1)
import collections
print("CARRY_END", dict(collections.Counter(v["verdict"] for v in state.values())))
if not only:
    ren = {k: v["new"] for k, v in state.items() if v["new"]}
    f = os.path.join(src, "showcase_summary.json")
    if os.path.exists(f):
        rows = []
        for row in json.load(open(f, encoding="utf-8")):
            n = ren.get(row["name"])
            if n and n != row["name"]:
                r = json.load(open(os.path.join(out, n + ".json"), encoding="utf-8"))
                row = dict(row, name=n, predicted=r["predicted"], counts=r["counts"], attempts=r.get("attempts", row.get("attempts")), base_seed=r["regen"]["base_seed"])
            if n:
                rows.append(row)
        json.dump(rows, open(os.path.join(out, "showcase_summary.json"), "w"), indent=1)
    f = os.path.join(src, "isomorph_summary.json")
    if os.path.exists(f):
        txt = open(f, encoding="utf-8").read()
        for k, v in sorted(ren.items(), key=lambda kv: -len(kv[0])):
            if v != k:
                txt = txt.replace('"' + k + '"', '"' + v + '"')
        open(os.path.join(out, "isomorph_summary.json"), "w", encoding="utf-8").write(txt)
        print("summaries written; an isomorph whose record changed needs its check run again (tools/cycle/merge_iso.py)")
