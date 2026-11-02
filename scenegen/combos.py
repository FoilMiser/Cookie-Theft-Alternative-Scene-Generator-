"""Count what the generator can make: template structures, radical signatures, cast assignments
and incidental variation, per setting and tier.

    python -m scenegen.combos [--out combos.json]

A *structure* is a set of templates (inference modules, contradictions, events) that fits a tier's
plan and can reach its content band with the setting's scorable features. Its *signature* (item
types with chain lengths, plus how many setting entities are scored) is what the difficulty model
sees; structures that share a signature are candidate isomorphs. *Cast* counts the ways to fill the
roles with distinct characters; *incidentals* are expression choices, which way each character
faces, whole-scene mirroring and optional features. Positions are continuous and not counted.
"""
import argparse
import itertools
import json
import math
from collections import Counter, defaultdict

from . import difficulty as DF
from . import templates as TP
from .planner import TIER_PLAN, feasible, is_animal_event
from .settings import FEATURES, build as build_setting

POOLS = {"GROWN": 8, "KIDS": 2, "YOUNG": 3, "ANY": 10, "ADULT_TEEN": 6, "YOUNG_ADULT": 8,
         "dog": 2, "cat": 2, "goat": 1, "songbird": 2, "duck": 1, "dog|goat": 3}
# roles per template: (pool, expression choices)
ROLES = {
    "walk_dog": [("GROWN", 3), ("dog", 2)], "water_flowers": [("GROWN", 3)], "hose_water": [("GROWN", 3)], "sweep": [("GROWN", 3)],
    "rake": [("GROWN", 3)], "dig": [("GROWN", 2)], "plant_flowers": [("GROWN", 2)], "carry_box": [("GROWN", 3)], "carry_bag": [("GROWN", 3)],
    "read_bench": [("ANY", 2)], "drink_bench": [("ANY", 2)], "picnic": [("ANY", 3)], "fly_kite": [("YOUNG", 3)], "balloon": [("KIDS", 6)],
    "swing": [("KIDS", 3)], "hang_laundry": [("GROWN", 3)], "play_catch": [("YOUNG", 3), ("YOUNG_ADULT", 3)], "kick_ball": [("YOUNG", 2)],
    "jump": [("YOUNG", 2)], "photo": [("GROWN", 2)], "fishing": [("GROWN", 3)], "feed_birds": [("GROWN", 3), ("songbird", 1), ("songbird", 1)],
    "ice_cream": [("ANY", 6)], "paint_fence": [("GROWN", 2)], "run": [("ADULT_TEEN", 3)], "wave": [("ANY", 2)],
    "dog_sleeping": [("dog", 1)], "cat_sleeping": [("cat", 1)], "goat_grazing": [("goat", 2)], "dog_playing": [("dog", 1)],
    "bird_perched": [("songbird", 4)], "ducks_swimming": [("duck", 1)], "birds_flying": [("songbird", 1)], "cat_on_fence": [("cat", 2)],
    "blocked_hose": [("GROWN", 1), ("dog|goat", 2)], "rain_coming": [("ANY", 2)], "cat_stalks_bird": [("cat", 1), ("songbird", 2)],
    "ball_in_tree": [("YOUNG", 6)], "kite_in_tree": [("YOUNG", 3)], "ice_cream_drop": [("KIDS", 3), ("dog", 2)], "about_to_trip": [("GROWN", 3)],
    "dog_begs": [("ANY", 6), ("dog", 2)], "sprinkler_package": [], "paint_tracks": [("GROWN", 2), ("dog", 1)], "windy_hat": [("GROWN", 2)],
    "bird_steals": [("GROWN", 1), ("songbird", 1)], "lost_balloon": [("KIDS", 6)], "ducks_bread": [("ANY", 3), ("duck", 1)],
    "water_upward": [("GROWN", 3)], "pan_watering": [("GROWN", 3)], "sweep_fork": [("GROWN", 3)], "bucket_hat": [("GROWN", 3)],
    "floating_box": [], "square_wheel": [], "fish_in_tree": [],
    "seesaw": [("YOUNG", 3), ("YOUNG", 3)], "sandbox": [("KIDS", 3)], "slide": [("KIDS", 5)], "push_stroller": [("ADULTS", 3)],
    "seesaw_heavy": [("ADULTS", 3), ("KIDS", 3)], "dog_wants_walk": [("dog", 2)],
    "sitting_on_air": [("GROWN", 6)], "ladder_nothing": [], "dog_reading": [("dog", 1)],
}
PEOPLE = {"GROWN": {"adult", "older_adult", "teen"}, "KIDS": {"child"}, "YOUNG": {"child", "teen"}, "ANY": {"adult", "older_adult", "teen", "child"},
          "ADULT_TEEN": {"adult", "teen"}, "YOUNG_ADULT": {"child", "teen", "adult"}, "ADULTS": {"adult", "older_adult"}}
CAST = {"adult": 5, "older_adult": 2, "teen": 1, "child": 2}
ANIMALS = {"dog": 2, "cat": 2, "goat": 1, "songbird": 2, "duck": 1}


def cast_assignments(roles):
    """Exact number of injective assignments of distinct characters to roles (backtracking)."""
    people = [k for k, n in CAST.items() for _ in range(n)]
    animals = [k for k, n in ANIMALS.items() for _ in range(n)]
    pr = [r for r, _ in roles if r in PEOPLE]
    ar = [r for r, _ in roles if r not in PEOPLE]

    def count(rs, pool, ok):
        used = [False] * len(pool)

        def go(i):
            if i == len(rs):
                return 1
            tot = 0
            for j, kind in enumerate(pool):
                if not used[j] and ok(rs[i], kind):
                    used[j] = True
                    tot += go(i + 1)
                    used[j] = False
            return tot
        return go(0)
    n_p = count(pr, people, lambda r, k: k in PEOPLE[r])
    n_a = count(ar, animals, lambda r, k: k in r.split("|"))
    return n_p * n_a


def entities_available(setting, feats, sky, consumed):
    inst = build_setting(setting, feats, sky)
    return len([e for e in inst.entities if e not in consumed])


def excl(c, setting):
    """A template's exclusive resources; from revision 17 the playground's seesaw templates also take the bench (the
    planner never puts the seesaw and the bench in front of which it stands in one picture)."""
    from . import scene as SCN
    if SCN.PLACEMENT_REV >= 17 and setting == "playground" and "seesaw" in c.features(setting):
        return tuple(c.exclusive) + ("bench",)
    return tuple(c.exclusive)


def event_dp(allowed, n_lo, n_hi, ex=lambda e: e.exclusive):
    """Count event subsets by (size, content) with at most one event per exclusive resource and at
    most two animal events."""
    st = {(0, 0, 0, frozenset()): 1}
    for e in allowed:
        nxt = dict(st)
        for (n, an, cont, res), cnt in st.items():
            if n >= n_hi:
                continue
            if set(ex(e)) & res:
                continue
            a2 = an + (1 if is_animal_event(e) else 0)
            if a2 > 2:
                continue
            key = (n + 1, a2, cont + e.content, res | frozenset(ex(e)))
            nxt[key] = nxt.get(key, 0) + cnt
        st = nxt
    out = Counter()
    for (n, an, cont, res), cnt in st.items():
        if n_lo <= n <= n_hi:
            out[(n, cont)] += cnt
    return out


def structures(setting, tier):
    """Yield (sky, base template ids, event count, event content, number of event subsets)."""
    plan = TIER_PLAN[tier]
    hi_c = DF.TIERS[tier]["content"][1]
    for sky in ("clear", "dark"):
        mods = [c for c in TP.MODULES if feasible(c, setting, sky)]
        cons = [c for c in TP.CONTRADICTIONS if feasible(c, setting, sky)]
        evs = [c for c in TP.EVENTS if feasible(c, setting, sky)]
        for units in range(plan["units"][0], plan["units"][1] + 1):
            for n_con in range(plan["contra"][0], min(units, plan["contra"][1]) + 1):
                n_mod = units - n_con
                for mset in itertools.combinations(mods, n_mod):
                    has_rain = any(c.id == "rain_coming" for c in mset)
                    if (sky == "dark") != has_rain:
                        continue
                    res = [r for c in mset for r in excl(c, setting)]
                    if len(res) != len(set(res)):
                        continue
                    for cset in itertools.combinations(cons, n_con):
                        res2 = res + [r for c in cset for r in excl(c, setting)]
                        if len(res2) != len(set(res2)):
                            continue
                        base = list(mset) + list(cset)
                        allowed = [e for e in evs if not set(excl(e, setting)) & set(res2)]
                        dp = event_dp(allowed, plan["events"][0], plan["load_max"] - units, lambda e: excl(e, setting))
                        for (n_ev, ev_content), cnt in dp.items():
                            content = sum(c.content for c in base) + ev_content
                            if content <= hi_c:
                                yield sky, tuple(c.id for c in base), n_ev, ev_content, cnt


def sample_multipliers(setting, tier, n=300, seed=1):
    """Mean cast assignments and incidental variants over structures the planner actually picks."""
    import random
    from .planner import balance_content, choose
    rng = random.Random(seed)
    cast, inc = [], []
    for _ in range(n):
        picked, sky = choose(tier, setting, rng)
        feats = set()
        for c in picked:
            feats |= c.features(setting)
        picked, feats = balance_content(tier, setting, sky, picked, feats, rng)
        roles = [r for c in picked for r in ROLES[c.id]]
        cast.append(cast_assignments(roles))
        v = 2
        for _, ne in roles:
            v *= ne * 2
        inc.append(v)
    return sum(cast) / len(cast), sum(inc) / len(inc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="combos.json")
    a = ap.parse_args()
    report = {}
    for setting in ("garden", "park", "street", "playground"):
        for tier in (1, 2, 3, 4):
            lo_c, hi_c = DF.TIERS[tier]["content"]
            n_struct, sigs = 0, Counter()
            ent_cache = {}
            for sky, ids, n_ev, ev_content, cnt in structures(setting, tier):
                feats = set()
                for i in ids:
                    feats |= TP.ALL_TEMPLATES[i].features(setting)
                consumed = {u for i in ids for u in TP.ALL_TEMPLATES[i].uses}
                key = (sky, frozenset(consumed))
                if key not in ent_cache:
                    ent_cache[key] = entities_available(setting, feats | FEATURES[setting]["optional"], sky, consumed)
                content = sum(TP.ALL_TEMPLATES[i].content for i in ids) + ev_content
                ks = [k for k in range(0, ent_cache[key] + 1) if lo_c <= content + k <= hi_c]
                if not ks:
                    continue
                n_struct += cnt
                base_sig = sorted(x for i in ids for x in TP.SIG[i] if x != ("action", 0) or True)
                for k in ks:
                    sig = tuple(sorted(base_sig + [("action", 0)] * ev_content + [("entity", 0)] * k))
                    sigs[sig] += cnt
            cast_m, inc_m = sample_multipliers(setting, tier)
            n_opt = len(FEATURES[setting]["optional"])
            total = n_struct * cast_m * inc_m * (2 ** n_opt)
            report[f"{setting}_T{tier}"] = {
                "setting": setting, "tier": tier,
                "structures": n_struct, "signatures": len(sigs),
                "largest_isomorph_pool": max(sigs.values()) if sigs else 0,
                "median_isomorph_pool": sorted(sigs.values())[len(sigs) // 2] if sigs else 0,
                "mean_cast_assignments": round(cast_m, 1), "mean_incidental_variants": round(inc_m, 1),
                "optional_feature_sets": 2 ** n_opt,
                "log10_scenes": round(math.log10(total), 1) if total > 0 else 0,
            }
            print(json.dumps(report[f"{setting}_T{tier}"]), flush=True)
    json.dump(report, open(a.out, "w"), indent=1)


if __name__ == "__main__":
    main()
