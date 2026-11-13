"""yield_set.py N SETTING FIRST_SEED TIER 'FORCED JSON' ['FORCED JSON' ...] [SWITCH=VALUE ...] [BAND=0] : does a forced template set place, and
does it land in its tier's band? build_one's own loop (seeds FIRST_SEED, +1000, ...; 14 layouts each) without the saving, so it answers in
seconds once the variants are in the library (variants that are not are rendered). A forced set is JSON:
  '{"modules": ["lost_balloon"], "contradictions": ["bucket_hat"], "events": ["bird_perched", "dog_playing"]}'
SWITCH=VALUE sets a module switch of scenegen.templates, draw or library for the run (TRIP47=B), to price a placement rule on a whole set.
BAND=0 leaves the band out (does it place at all?). Per seed it prints OK<layout>, no (with the first estimates that missed the band) or plan
(the set cannot be cast: a template not feasible in the setting, two templates wanting one animal, more child templates than children), and
then how often each reason failed a layout."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, time
sys.path.insert(0, ROOT); os.chdir(ROOT)
from scenegen.library import Library
from scenegen.planner import plan, realize, finalize, quick_estimate, near_band, PlacementError, USAGE
import scenegen.difficulty as DF
import scenegen.draw as D0
import scenegen.library as L0
import scenegen.templates as T0

n, st, first, tier = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
sets, BAND = [], True
for a in sys.argv[5:]:
    if a.startswith("{"):
        sets.append(a)
        continue
    k, v = a.split("=")
    if k == "BAND":
        BAND = v != "0"
        continue
    for m in (T0, D0, L0):
        if hasattr(m, k):
            setattr(m, k, v)
            break
    else:
        raise SystemExit("no switch " + k)
# (BENCH_CAST and BENCH_LIB, as for the isolation bench: a scratch library, so that pricing a rule before the release has a library of its
#  own renders nothing into the last release's)
lib = Library(**({"cast_dir": os.environ["BENCH_CAST"]} if os.environ.get("BENCH_CAST") else {}), **({"lib_dir": os.environ["BENCH_LIB"]} if os.environ.get("BENCH_LIB") else {}))
for fj in sets:
    forced = json.loads(fj)
    t0 = time.time()
    out = []
    WHY = {}

    def why(w):
        w = str(w)[:44]
        WHY[w] = WHY.get(w, 0) + 1

    for i in range(n):
        seed = first + 1000 * i
        USAGE.clear()
        T0.YAW_FORCE.clear()
        try:
            sc = plan(tier, st, seed, lib, forced)
        except PlacementError as e:
            out.append(f"{seed}:plan({str(e)[:40]})")
            continue
        lib.ensure(sc.variants, log=lambda *a: None)
        knob = 0
        Tb = DF.TIERS[tier]
        got = None
        est = []
        for r in range(14):
            sc.reset_layout(seed * 31 + r)
            sc.knob = knob
            ok, w = realize(sc)
            if not ok:
                why(w)
                continue
            pcq, piq = quick_estimate(sc)
            if BAND and not near_band(tier, pcq, piq):
                est.append((None if pcq is None else round(pcq, 2), None if piq is None else round(piq, 2)))
                why("estimate")
                if Tb["pi"] and piq is not None:
                    if piq > Tb["pi"][1]:
                        knob = min(1, knob + 1)
                    elif piq < Tb["pi"][0]:
                        knob = max(-1, knob - 1)
                continue
            fin = finalize(sc)
            if not fin["checks"]["occlusion_and_size"][0]:
                why("occlusion")
                continue
            if not fin["checks"]["legibility"][0]:
                why("legibility")
                continue
            if BAND and not fin["checks"]["clutter_band"][0]:
                why("clutter")
                continue
            if BAND and not all(fin["bands"].values()):
                why("band " + ",".join(k for k, v in fin["bands"].items() if not v))
                est.append(("fin", round(fin["pc"][0], 2), None if fin["pi"][0] is None else round(fin["pi"][0], 2)))
                continue
            got = r
            break
        out.append(f"{seed}:{'no' + str(est[:2]) if got is None else 'OK' + str(got)}")
    print(st, tier, fj, flush=True)
    print("  ", " ".join(out), f"{time.time() - t0:.0f}s", flush=True)
    print("   why:", json.dumps(dict(sorted(WHY.items(), key=lambda x: -x[1])))[:600], flush=True)
