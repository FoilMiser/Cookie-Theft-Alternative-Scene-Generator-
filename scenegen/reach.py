"""Which cast poses the templates can ask for at the current placement revision.

Every template's bind() is run many times in every setting and sky it allows, and the poses it requests
are collected. A cast action that no template reaches is a spare: built and rendered like the others, but
in no generated picture and never screened.

    python -m scenegen.reach --out reach.json
"""
import argparse
import json
from collections import defaultdict

from . import scene as SCN
from .library import Library
from .templates import ALL_TEMPLATES


def reachable(lib=None, seeds=80):
    """Casting depends on who other events have already taken (a seesaw ride falls back to a teenager when both
    children are busy), so half the binds run with a random part of the cast already in use."""
    import random
    lib = lib or Library()
    reach = defaultdict(set)
    people = sorted(lib.people())
    animals = sorted(f for f, d in lib.families.items() if d["class"] == "animal")
    for tid, cls in ALL_TEMPLATES.items():
        for st in cls.settings:
            for sky in ("clear", "dark"):
                if not cls.feasible(st, sky):
                    continue
                for seed in range(seeds):
                    sc = SCN.Scene(3, st, seed * 7 + 1, lib, sky=sky)
                    if seed % 2:
                        r = random.Random(seed)
                        sc.fams = {f for f in people + animals if r.random() < 0.45}
                    try:
                        cls(sc).bind()
                    except Exception:
                        continue
                    for v in sc.variants:
                        reach[v[1]].add(tid)
    return {p: sorted(t) for p, t in sorted(reach.items())}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="reach.json")
    a = ap.parse_args()
    r = reachable()
    json.dump(r, open(a.out, "w"), indent=1)
    print(len(r), "poses reachable")


if __name__ == "__main__":
    main()
