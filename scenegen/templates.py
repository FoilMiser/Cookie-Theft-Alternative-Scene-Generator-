"""Scene templates: simple events, inference modules and contradictions.

Every template is setting-agnostic where it can be: it names the features it needs (a bench,
flowers, a tree, a pond), casts its roles from the library, places them from the rendered
manifests, adds any drawn extras (water, a ball in a tree, paw prints) and declares its items:

  entity / action          content items (read straight off the picture)
  inference                a cause, prediction or intention, with its chain length and cues
  contradiction_notice     "something is wrong with ..."   } one contradiction = one inference unit,
  contradiction_explain    "... because ..."               } scored as two items

Item text uses the everyday name of whoever fills the role; `accepted` lists what scorers accept.
"""
import math

from . import draw as D
from . import scene as SCN
from .draw import C, sz
from .scene import ADULTS, GROWN, KIDS, YOUNG, PlacementError

# events that draw a ball of their own (revision 7 keeps the trip obstacle from being a second one)
BALL_EVENTS = {"play_catch", "kick_ball", "ball_in_tree"}

ALL = ("garden", "park", "street", "playground")
PG = ("playground",)


def art(name):
    return "an" if name[0] in "aeiou" else "a"


class T:
    id = "base"
    kind = "event"            # event | inference | contradiction
    settings = ALL
    needs = {}                # setting -> set of features
    sky = None                # None (any) | "clear" | "dark"
    units = 0                 # inference units
    content = 1               # content items this template adds
    uses = ()                 # setting entities it consumes as its object
    exclusive = ()            # resources it occupies (bench, swing, hose_reel, tree_canopy, ...)
    domain = None

    def __init__(self, sc):
        self.sc = sc
        self.ev = None

    @classmethod
    def feasible(cls, setting, sky):
        if setting not in cls.settings:
            return False
        if cls.sky and cls.sky != sky:
            return False
        return True

    @classmethod
    def features(cls, setting):
        n = cls.needs.get(setting, cls.needs.get("*", set()))
        return set(n)

    def bind(self):
        raise NotImplementedError

    def place(self):
        raise NotImplementedError

    # helpers
    def who(self, fam):
        return self.sc.name(fam), self.sc.names(fam)

    def act(self, fam, text, what, key, elements):
        n, names = self.who(fam)
        return self.sc.item("action", f"{art(n).capitalize()} {n} is {text}", {"who": names, "what": what}, key, elements,
                            animate=True, template=self.id, event=self.ev)

    def ent(self, text, accepted, key, elements, animate=False):
        return self.sc.item("entity", text, accepted, key, elements, animate=animate, template=self.id, event=self.ev)

    def inf(self, text, accepted, key, chain, cues, effect, elements=None):
        return self.sc.item("inference", text, accepted, key, elements or cues, chain=chain, cues=cues, effect=effect,
                            template=self.id, event=self.ev)

    def contra(self, notice, explain, accepted_n, accepted_e, key, elements, chain=1):
        self.sc.item("contradiction_notice", notice, accepted_n, key, elements, chain=0, cues=elements, effect=elements,
                     domain=self.domain, template=self.id, event=self.ev)
        self.sc.item("contradiction_explain", explain, accepted_e, key, elements, chain=chain, cues=elements, effect=elements,
                     domain=self.domain, template=self.id, event=self.ev)

    def stand_spots(self, y_range=None, x_range=None, n=80):
        return self.sc.spots(x_range, y_range, n)

    def k3(self, easy, mid, hard):
        """Pick a radical's value from the scene's difficulty knob (-1 easier, 0, +1 harder)."""
        return {-1: easy, 0: mid, 1: hard}[max(-1, min(1, self.sc.knob))] if self.kind != "event" else mid

    def face_to(self, tx):
        return lambda X, Y: 1 if tx > X else -1

    def place_with(self, eid, v, cands, want_face=None, extras=None, limit=0.12, xlimit=0.06, ground_extras=True):
        """Place v at the first candidate where it fits AND every extra it will draw fits.
        extras(p) returns a list of bboxes (or None to reject the spot); the template keeps
        whatever it computed there for drawing once the spot is accepted."""
        sc = self.sc
        for X, Y in cands:
            mirror = False
            if want_face is not None:
                w = want_face(X, Y) if callable(want_face) else want_face
                mirror = sc.mirror_for(v, w)
            p = sc.placed(v, X, Y, mirror, None, eid)
            if not sc.fits(p.bbox(), limit=limit):
                continue
            boxes = extras(p) if extras else []
            if boxes is None:
                continue
            if any(not sc.fits(bb, limit=xlimit, ignore=(eid,)) for bb in boxes):
                continue
            # revision 4: what the person draws (a stroller, a paper) keeps clear of standing structures
            # (a lamp post passed through a stroller's handle)
            if SCN.PLACEMENT_REV >= 4 and any(not sc.air_clear(bb, 6, use_exempt=True) for bb in boxes):
                continue
            # things set down on the ground must stand on open, walkable ground (not in the sandbox,
            # the flower bed or the pond)
            if ground_extras and any(not sc.S.walkable((bb[0] + bb[2]) / 2, bb[3] - 2) or sc.S.in_soft((bb[0] + bb[2]) / 2, bb[3] - 2) for bb in boxes):
                continue
            # revision 14: a walker's lane clear of other events and of standing structures
            if SCN.PLACEMENT_REV >= 14 and not sc.lanes_ok(p):
                continue
            sc.assets[eid] = p
            sc.add_lanes(p)
            return p
        return None


def anchor_or(p, name, default):
    return p.anchor(name) if p.has_anchor(name) else default


def seg_cross(p1, p2, q1, q2):
    """Do segments p1-p2 and q1-q2 cross (used to keep two kite strings apart)?"""
    def o(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    d1, d2, d3, d4 = o(q1, q2, p1), o(q1, q2, p2), o(p1, p2, q1), o(p1, p2, q2)
    return (d1 > 0) != (d2 > 0) and (d3 > 0) != (d4 > 0)


# ============================================================================ simple events
class WalkDog(T):
    id = "walk_dog"
    key = "dog"

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.d = sc.animal(["dog"])
        self.vp = sc.need(self.p, "walk_dog", sc.rng.choice(["smile", "content", "happy"]), 90)
        self.vd = sc.need(self.d, "walk", sc.rng.choice(["happy", "neutral"]), 90)

    def place(self):
        sc = self.sc
        want = sc.rng.choice([1, -1])
        ep, ed = sc.eid("walker"), sc.eid("dog")
        for X, Y in self.stand_spots(n=120):
            p = sc.placed(self.vp, X, Y, sc.mirror_for(self.vp, want), eid=ep)
            if not sc.fits(p.bbox()):
                continue
            lx, ly = p.anchor("leash_end")
            d = None
            # (revision 12: the dog a little further ahead or nearer when that lets the lead clear its back)
            for gap in ((150, 185, 120) if SCN.PLACEMENT_REV >= 12 else (150,)):
                dX = X + want * gap * sz(Y)
                d = sc.placed(self.vd, dX, Y + 6, sc.mirror_for(self.vd, want), eid=ed)
                if not sc.S.walkable(dX, Y + 6) or not sc.fits(d.bbox()):
                    d = None
                    continue
                cx, cy = d.anchor("collar")
                mx = (lx + cx) / 2
                qy = max(ly, cy) + 30 * sz(Y)
                if SCN.PLACEMENT_REV >= 12:
                    # revision 12: the lead sags only as far as it can without crossing the dog's body on its way to the
                    # collar (sagging over the dog's back it "attaches around its middle/back rather than the collar")
                    qy = self.lead_sag(d, (lx, ly), (mx, cx, cy), Y)
                    if qy is None:
                        d = None
                        continue
                break
            if d is None:
                continue
            if SCN.PLACEMENT_REV >= 4:
                # the leash may not cross a pole or a tree trunk (the dog read as tied to the lamp post)
                pts = [((1 - t) ** 2 * lx + 2 * (1 - t) * t * mx + t * t * cx, (1 - t) ** 2 * ly + 2 * (1 - t) * t * qy + t * t * cy)
                       for t in [i / 16 for i in range(17)]]
                if not sc.path_clear(pts):
                    continue
            # revision 14: the ground ahead of the dog and of its walker clear of other events (a dog on a lead heading
            # straight at a woman reading her way along read as facing her, not where its owner walks)
            if SCN.PLACEMENT_REV >= 14 and not sc.lanes_ok(p, d):
                continue
            sc.assets[ep], sc.assets[ed] = p, d
            sc.add_lanes(p, d)
            leash = f'<path d="M {D.P(lx, ly)} Q {D.P(mx, qy)} {D.P(cx, cy)}" fill="none" stroke="{C["red"]}" stroke-width="{3.5 * sz(Y):.1f}"/>'
            el = sc.svg(sc.eid("leash"), "Leash", leash, Y + 7, (min(lx, cx), min(ly, cy, qy), max(lx, cx), max(ly, cy) + 30), "scored")
            self.act(self.p, "walking a dog", ["walking a dog", "walking the dog", "dog on a leash", "taking the dog for a walk"], "dog", [ep, ed, el])
            return True
        return False


def _lead_sag(self, d, hand, mid, Y):
    """Revision 12: the deepest sag (of a few) at which the lead's curve stays off the dog's body short of the collar;
    None if even a taut lead would cross it."""
    from . import compose as K
    lx, ly = hand
    mx, cx, cy = mid
    m = K.asset_mask(d, False)
    k = K.MASK_SCALE
    s = sz(Y)
    for qy in (max(ly, cy) + 30 * s, max(ly, cy) + 14 * s, max(ly, cy), (ly + cy) / 2):
        bad = False
        for i in range(1, 15):
            t = i / 16
            px, py = (1 - t) ** 2 * lx + 2 * (1 - t) * t * mx + t * t * cx, (1 - t) ** 2 * ly + 2 * (1 - t) * t * qy + t * t * cy
            if math.hypot(px - cx, py - cy) < 12 * s:
                continue
            xi, yi = int(px * k), int(py * k)
            if m[max(0, yi - 1):yi + 2, max(0, xi - 1):xi + 2].any():
                bad = True
                break
        if not bad:
            return qy
    return None


WalkDog.lead_sag = _lead_sag


def in_bed(sc, pt, deep=False):
    """Revision 18: True if pt lies well inside the soil ellipse of a garden or park flower bed (the street's planter, a
    box, keeps the earlier rule). Revision 19, deep: a can's water in the back two thirds of it (a shower ending in the
    front of the bed still landed "at the front edge of the flower bed, possibly missing the flowers")."""
    if sc.setting_id not in ("garden", "park"):
        return True
    b = sc.S.anchors["flowers"]["bbox"]
    s = (b[3] - b[1]) / 136.0
    cx, cy, rx, ry = (b[0] + b[2]) / 2, b[3] - 36 * s, (b[2] - b[0]) / 2 - 24 * s, 36 * s - 7 * s
    if deep and pt[1] > cy + 0.35 * ry:
        return False
    return ((pt[0] - cx) / rx) ** 2 + ((pt[1] - cy) / ry) ** 2 <= 1.0


class WaterFlowers(T):
    id = "water_flowers"
    needs = {"*": {"flowers"}}
    uses = ("flowers",)
    # revision 19: no watering by can in a picture with a hose (a reel "unused right beside him"; with the blocked hose the
    # planner dropped the reel the hose needs)
    exclusive = ("flowers",) + (("hose_reel",) if SCN.PLACEMENT_REV >= 19 else ())
    upward = False
    pose = "water_plants"
    stream_cap = 230.0

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.vp = sc.need(self.p, self.pose, sc.rng.choice(["focused", "content", "smile"]), 90)

    def place(self):
        sc = self.sc
        F = sc.S.anchors["flowers"]
        bb = F["bbox"]
        ep = sc.eid("waterer")
        sides = [("stand_left", 1), ("stand_right", -1)]
        sc.rng.shuffle(sides)
        for key, _ in sides:
            sx, sy = F[key]
            want = 1 if F["center"][0] > sx else -1
            cands = [(sx + dx, sy + dy) for dx in (0, -20, 20, -40, 40) for dy in (0, 15, -15, 30)]
            if SCN.PLACEMENT_REV >= 2:      # a step further from the bed (clear of a clothesline post)
                cands += [(sx - want * d, sy + dy) for d in (65, 90) for dy in (0, 15, 30)]
            if SCN.PLACEMENT_REV >= 5:
                # revision 5: or in front of the bed, nearer the viewer, pouring over its front edge (the
                # clothesline post beside the garden bed left no room at its side for a can or a pan held
                # out over the flowers, so with a clothesline nobody could water them)
                cands += [(sx + want * d, bb[3] + dy) for dy in (95, 110, 125) for d in (20, 40, 60, 80)]
            for X, Y in cands:
                if not sc.S.walkable(X, Y):
                    continue
                p = sc.placed(self.vp, X, Y, sc.mirror_for(self.vp, want), eid=ep)
                if not sc.fits(p.bbox(), limit=0.15):
                    continue
                sp = p.anchor("spout")
                aim = p.anchor("spout_aim")
                length = self.k3(200, 150, 115) if self.upward else 150
                if not self.upward and SCN.PLACEMENT_REV >= 4:
                    # revision 4: the stream is as long as it takes to reach the soil (a fixed length
                    # carried it past the flower box onto the pavement)
                    target_y = bb[3] - 0.35 * (bb[3] - bb[1])
                    if SCN.PLACEMENT_REV >= 5 and "soil_y" in F:
                        target_y = F["soil_y"]      # the top of a raised box, not its front face
                    shortest = 60.0
                    if SCN.PLACEMENT_REV >= 5 and Y > bb[3] + 50:
                        # standing in front, the can is held about as low as the bed's front edge: a short
                        # stream onto the front of the bed
                        target_y, shortest = F.get("soil_y", bb[3] - 12), 30.0
                    cap = self.stream_cap if SCN.PLACEMENT_REV >= 6 else 230.0
                    length = max(shortest, min(cap, (target_y - sp[1]) / (0.85 * sz(Y))))
                if self.upward and SCN.PLACEMENT_REV >= 8:
                    # revision 8: one unbroken stream whose top ends in open air, clear of awnings, lamps
                    # and posts, shortened if need be (a stream reaching an awning read as dripping from it)
                    got = None
                    for L in (length, length * 0.86, length * 0.74):
                        st_ = D.water_stream(sp, (aim[0] - sp[0], aim[1] - sp[1]), sz(Y), L, upward=True, splash=True, solid=True)
                        b_ = st_[1]
                        top = (b_[0] - 10, b_[1] - 16, b_[2] + 10, (b_[1] + sp[1]) / 2)
                        g_ = (top[0] - 10, top[1] - 10, top[2] + 10, top[3])
                        if sc.clear_of_setting(top, ("awnings",), 18) and \
                                sc.setting_clear(top, skip=sc.SKY_SKIP + ("buildings", "fence", "flowers", "hills", "tree_line", "clouds_white", "clouds_dark", "sun")) and \
                                not any(min(g_[2], b[2]) > max(g_[0], b[0]) and min(g_[3], b[3]) > max(g_[1], b[1])
                                        for k_, q_ in sc.assets.items() if k_ != ep for b in (q_.bbox(),)):
                            got = st_
                            break
                    if not got:
                        continue
                    stream, sbb, end = got
                    # and nobody placed later stands in it (a jumping child's feet at its top seemed its source)
                    sc.airzones.append(g_)
                else:
                    # (revision 14: from a can, a shower of drops; from a pan, a pour thinning as it falls; dashed, the water read as
                    # "chunky linked blobs, like a chain or bubbles", and drawn solid on the bench, as "a solid bent tube, hose or rod")
                    stream, sbb, end = D.water_stream(sp, (aim[0] - sp[0], aim[1] - sp[1]), sz(Y), length, upward=self.upward,
                                                      splash=SCN.PLACEMENT_REV >= 4,
                                                      style=(("pour" if self.id == "pan_watering" else "shower") if SCN.PLACEMENT_REV >= 14 else None))
                if not self.upward and not (bb[0] - 40 <= end[0] <= bb[2] + 40):
                    continue
                # revision 4: the water lands on the soil, not in front of the bed or on the path
                if not self.upward and SCN.PLACEMENT_REV >= 4 and not (bb[0] + 18 <= end[0] <= bb[2] - 18 and end[1] <= bb[3] - 6):
                    continue
                # revision 18: well inside the soil of a garden or park bed (at its front edge it read as "lands at the
                # front edge of the bed / on the grass rather than on the flowers")
                if not self.upward and SCN.PLACEMENT_REV >= 18 and not in_bed(sc, end, deep=SCN.PLACEMENT_REV >= 19 and self.id == "water_flowers"):
                    continue
                sc.assets[ep] = p
                sc.legib_ok.add(("flowers", ep))
                # the water lands on the flowers, so it is drawn in front of them
                ew = sc.svg(sc.eid("water"), "Water from the can", stream, max(Y, F["depth"]) + 1, sbb, "scored")
                self.items(ep, ew)
                return True
        return False

    def items(self, ep, ew):
        self.act(self.p, "watering the flowers", ["watering the flowers", "watering the plants", "watering the garden", "watering can"], "flowers", [ep, ew])


class HoseWater(T):
    id = "hose_water"
    settings = ("garden",)
    needs = {"garden": {"hose_reel", "flowers"}}
    exclusive = ("hose_reel", "flowers")
    uses = ("flowers",)

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.vp = sc.need(self.p, "hose_spray", sc.rng.choice(["content", "smile", "focused"]), 90)

    def place(self):
        sc = self.sc
        F = sc.S.anchors["flowers"]
        ep = sc.eid("hoser")
        cands = [(F["stand_left"][0] + dx, F["stand_left"][1] + dy) for dx in (40, 80, 120, 0) for dy in (10, 40, 70)]
        if SCN.PLACEMENT_REV >= 4:      # more room to step clear of a clothesline post
            cands += [(F["stand_left"][0] + dx, F["stand_left"][1] + dy) for dx in (160, 200, -40) for dy in (10, 40, 70, 100)]
        for X, Y in cands:
            if not sc.S.walkable(X, Y):
                continue
            p = sc.placed(self.vp, X, Y, sc.mirror_for(self.vp, -1), eid=ep)
            if not sc.fits(p.bbox(), limit=0.15):
                continue
            sc.assets[ep] = p
            sc.legib_ok.add(("flowers", ep))
            rx, ry = sc.S.anchors["hose_reel"]
            hx, hy = p.anchor("hose_in")
            if SCN.PLACEMENT_REV >= 17:
                # revision 17: the hose comes up to the hand from the ground in front of the waterer, a body width from
                # the legs (run up behind the hand it passed "very tightly behind/around the old man's legs")
                s_ = sz(Y)
                hose = D.hose_path([(rx, ry), (rx + 60, Y + 40), ((rx + hx) / 2 - 30, Y + 34), (hx - 85 * s_, Y + 12), (hx, hy)], s_)
            else:
                hose = D.hose_path([(rx, ry), (rx + 60, Y + 40), ((rx + X) / 2 + 40, Y + 30), (hx + 40, hy + 120), (hx, hy)], sz(Y))
            # revision 19: the hose drawn in front of the flower bed (behind it, the bed hid a fifth of it and the event
            # could only be placed where a clothesline post pushed the waterer away from the bed)
            hd = max(Y - 1, F["depth"] + 0.5) if SCN.PLACEMENT_REV >= 19 else Y - 1
            eh = sc.svg(sc.eid("hose"), "Garden hose", hose, hd, (rx, min(hy, ry), hx + 40, Y + 45), "scored")
            nz, aim = p.anchor("nozzle"), p.anchor("nozzle_aim")
            if SCN.PLACEMENT_REV >= 4:
                # revision 4: the spray reaches the soil of the bed and is drawn in front of the flowers
                # (drawn behind them, half of it was hidden and the event never passed the rules)
                bb = F["bbox"]
                length = max(80.0, min(300.0, (bb[3] - 0.35 * (bb[3] - bb[1]) - nz[1]) / (0.85 * sz(Y))))
                got = None
                # revision 18: the jet carried on until it lands inside the bed's soil (stopped at the height of the
                # flowers, it "lands at the front edge of the bed / on the grass")
                for k_ in ((1.0, 1.12, 1.25, 1.4, 1.55) if SCN.PLACEMENT_REV >= 18 else (1.0,)):
                    st_ = D.water_stream(nz, (aim[0] - nz[0], aim[1] - nz[1]), sz(Y), length * k_, splash=True,
                                         style="jet" if SCN.PLACEMENT_REV >= 17 else None)
                    if SCN.PLACEMENT_REV < 18 or in_bed(sc, st_[2]):
                        got = st_
                        break
                if got is None:
                    sc.remove(ep, eh)       # (this spot's waterer and hose taken back)
                    continue
                stream, sbb, end_ = got
                ew = sc.svg(sc.eid("spray"), "Water spraying", stream, max(Y, F["depth"]) + 1, sbb, "scored")
            else:
                stream, sbb, _ = D.water_stream(nz, (aim[0] - nz[0], aim[1] - nz[1]), sz(Y), 260)
                ew = sc.svg(sc.eid("spray"), "Water spraying", stream, Y + 1, sbb, "scored")
            self.act(self.p, "watering the flowers with a hose", ["watering with a hose", "spraying water", "hosing the flowers", "watering the garden"], "hose", [ep, eh, ew])
            return True
        return False


class Sweep(T):
    id = "sweep"
    pose = "sweep"
    text = ("sweeping", ["sweeping", "sweeping the path", "sweeping the ground", "broom"], "sweeping")

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.vp = sc.need(self.p, self.pose, sc.rng.choice(["focused", "neutral", "content"]), 45)

    @classmethod
    def feasible(cls, setting, sky):
        # revision 6: sweeping needs a hard surface (a broom on the playground's grass read as odd)
        if SCN.PLACEMENT_REV >= 6 and setting == "playground":
            return False
        return super().feasible(setting, sky)

    def place(self):
        sc = self.sc
        A = sc.S.anchors.get("path")
        cands = self.stand_spots(x_range=(A["x0"], A["x1"]), y_range=(A["y0"], A["y1"])) if A else []
        if not (SCN.PLACEMENT_REV >= 6 and A):
            cands += self.stand_spots()
        ep = sc.eid("sweeper")
        rev24 = SCN.PLACEMENT_REV >= 24 and D.SWEEP26 != "O" and type(self) is Sweep

        def heap(q):
            # revision 24: something swept, at the broom's head, on the ground (all four v0.25 pictures: "no visible rubbish or leaf
            # pile for the old man to sweep"; one reader "could be sweeping, or pausing to watch")
            tx, _ = q.anchor("broom_tip")
            s_ = sz(q.Y)
            f_ = 1 if tx > q.X else -1
            return D.sweep_heap(tx + f_ * 34 * s_, q.Y + 6 * s_, s_, f_, D.SWEEP26)
        accept = (lambda q: sc.fits(heap(q)[1], limit=0.05, ignore=(ep,))) if rev24 else None
        p = sc.try_put(ep, self.vp, cands, want_face=sc.rng.choice([1, -1]), accept=accept)
        if not p:
            return False
        self.items(ep)
        if rev24:
            hs, hb = heap(p)
            sc.svg(sc.eid("sweepheap"), "What has been swept", hs, p.Y + 2, hb, "scored")
        return True

    def items(self, ep):
        t, what, key = self.text
        self.act(self.p, t, what, key, [ep])


class Rake(T):
    id = "rake"
    settings = ("garden", "park")

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.vp = sc.need(self.p, "rake", sc.rng.choice(["focused", "neutral", "content"]), 45)

    def place(self):
        sc = self.sc
        ep = sc.eid("raker")

        def pile(p):
            f = p.facing() or 1
            s = sz(p.Y)
            if p.has_anchor("rake_head"):
                rx_, ry_ = p.anchor("rake_head")
                self.pile = (rx_ + f * 46 * s, p.Y + 16 * s)
            else:
                self.pile = (p.X + f * 90 * s, p.Y + 22 * s)
            lx, ly = self.pile
            return [(lx - 60 * s, ly - 20 * s, lx + 60 * s, ly + 20 * s)]
        p = self.place_with(ep, self.vp, self.stand_spots(), want_face=sc.rng.choice([1, -1]), extras=pile)
        if not p:
            return False
        s = sz(p.Y)
        lx, ly = self.pile
        leaves = ""
        for i in range(14):
            a = i * 2.4
            dx, dy = math.cos(a) * (8 + i * 3) * s, math.sin(a) * (3 + i) * s * 0.5
            leaves += D.ell(lx + dx, ly + dy, 9 * s, 5 * s, [C["leaf_green"], C["leaf_brown"], C["grass_dark"], C["khaki"]][i % 4], D.OW * 0.5, rot=a * 40)
        el = sc.svg(sc.eid("leaves"), "Pile of leaves", leaves, p.Y + 22 * s, (lx - 60 * s, ly - 20 * s, lx + 60 * s, ly + 20 * s), "scored")
        self.act(self.p, "raking leaves", ["raking", "raking leaves", "rake", "cleaning up leaves", "raking grass"], "raking", [ep, el])
        return True


class Dig(T):
    id = "dig"
    settings = ("garden", "park")

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        # revision 10: bent over the spade, lifting a spadeful of earth (pose dig_lift; the upright spade
        # beside the legs read as "leaning on the spade ... tired or unwell")
        self.vp = sc.need(self.p, "dig_lift" if SCN.PLACEMENT_REV >= 10 else "dig", sc.rng.choice(["determined", "focused"]), 45)

    def place(self):
        sc = self.sc
        ep = sc.eid("digger")
        if SCN.PLACEMENT_REV >= 10:
            return self.place10(ep)

        def mound(p):
            f = p.facing() or 1
            s = sz(p.Y)
            self.m = (p.X + f * 110 * s, p.Y + 10 * s)
            mx, my = self.m
            # revision 4: a hole is dug in the grass, never in the path
            if SCN.PLACEMENT_REV >= 4 and any(sc.on_element("path", x, y) for x, y in ((mx, my), (mx - f * 66 * s, my), (p.X, p.Y))):
                return None
            return [(mx - 50 * s, my - 46 * s, mx + 50 * s, my)]
        p = self.place_with(ep, self.vp, self.stand_spots(), want_face=sc.rng.choice([1, -1]), extras=mound)
        if not p:
            return False
        s = sz(p.Y)
        mx, my = self.m
        f = p.facing() or 1
        hx_ = mx - f * 66 * s
        mound = D.ell(hx_, my + 2 * s, 34 * s, 9 * s, C["hole"], D.OW * 0.8)
        mound += D.shape(f"M {D.P(mx - 50 * s, my)} Q {D.P(mx, my - 46 * s)} {D.P(mx + 50 * s, my)} Z", C["soil"])
        em = sc.svg(sc.eid("soil"), "Hole and pile of dirt", mound, p.Y + 10 * s, (min(mx - 50 * s, hx_ - 34 * s), my - 46 * s, max(mx + 50 * s, hx_ + 34 * s), my + 11 * s), "scored")
        self.act(self.p, "digging", ["digging", "digging a hole", "shoveling", "using a shovel", "spade"], "digging", [ep, em])
        return True


def _dig_place10(self, ep):
    """Revision 10: the hole right under the spade's blade, the pile of earth just beyond it."""
    sc = self.sc

    def hole(p):
        f = p.facing() or 1
        s = sz(p.Y)
        bx = p.anchor("spade")[0] if p.has_anchor("spade") else p.X + f * 90 * s
        self.h = (bx + f * 6 * s, p.Y + 6 * s)
        # (the pile overlaps the hole's far rim: set apart, it "looks a bit pasted on")
        self.m = (bx + f * 72 * s, p.Y + 8 * s)
        hx, hy = self.h
        mx, my = self.m
        if any(sc.on_element("path", x, y) for x, y in ((hx, hy), (mx, my), (p.X, p.Y))):
            return None
        box = (min(hx - 36 * s, mx - 46 * s), my - 40 * s, max(hx + 36 * s, mx + 46 * s), my + 10 * s)
        # revision 18: the whole hole and pile off the path (one overlapped the path's edge)
        if SCN.PLACEMENT_REV >= 18 and not sc.setting_clear((box[0] - 10, hy - 14 * s, box[2] + 10, box[3] + 6), only=("path",)):
            return None
        # the whole hole inside the picture (at the bottom edge its near rim was cut off by the frame)
        if hy + 12 * s > D.H - 6:
            return None
        # and clear of every standing structure (a hole dug at the foot of a clothesline post "suggests the
        # post is about to be undermined")
        if not sc.setting_clear((box[0] - 20, box[1] - 10, box[2] + 20, box[3] + 10), only=HAT_STRUCT9 + ("hose_reel", "bench", "fence")):
            return None
        return [box[:3] + (my,)]
    p = self.place_with(ep, self.vp, self.stand_spots(), want_face=sc.rng.choice([1, -1]), extras=hole)
    if not p:
        return False
    s = sz(p.Y)
    hx, hy = self.h
    mx, my = self.m
    svg = D.ell(hx, hy, 36 * s, 10 * s, C["hole"], D.OW * 0.8)
    svg += D.shape(f"M {D.P(mx - 46 * s, my)} Q {D.P(mx, my - 40 * s)} {D.P(mx + 46 * s, my)} Z", C["soil"])
    bb = (min(hx - 36 * s, mx - 46 * s), my - 40 * s, max(hx + 36 * s, mx + 46 * s), my + 10 * s)
    em = sc.svg(sc.eid("soil"), "Hole and pile of dirt", svg, p.Y - 1, bb, "scored")
    self.act(self.p, "digging", ["digging", "digging a hole", "shoveling", "using a shovel", "spade"], "digging", [ep, em])
    return True


Dig.place10 = _dig_place10


class PlantFlowers(T):
    id = "plant_flowers"
    settings = ("garden", "park")
    needs = {"*": {"flowers"}}
    uses = ("flowers",)
    exclusive = ("flowers",)

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.vp = sc.need(self.p, "kneel_plant", sc.rng.choice(["focused", "content"]), 90)

    def place(self):
        sc = self.sc
        F = sc.S.anchors["flowers"]
        ep = sc.eid("planter")
        for key in ("stand_left", "stand_right"):
            sx, sy = F[key]
            want = 1 if F["center"][0] > sx else -1
            def potbox(p, want=want):
                tx, ty = p.anchor("trowel_tip")
                s = sz(p.Y)
                x = tx + want * 30 * s
                return [(x - 24 * s, p.Y - 60 * s, x + 24 * s, p.Y + 8 * s)]
            p = self.place_with(ep, self.vp, [(sx + dx, sy + dy) for dx in (0, 30, -30) for dy in (10, 30, -10)], want_face=want, limit=0.2, extras=potbox, xlimit=0.3, ground_extras=False)
            if p:
                sc.legib_ok.add(("flowers", ep))
                tx, ty = p.anchor("trowel_tip")
                s = sz(p.Y)
                pot = D.pot(tx + want * 30 * s, p.Y + 8 * s, C["pink"], s * 0.8)
                eo = sc.svg(sc.eid("pot"), "Flower pot", pot, p.Y + 8 * s, (tx + want * 30 * s - 24 * s, p.Y - 60 * s, tx + want * 30 * s + 24 * s, p.Y + 8 * s), "scored")
                self.act(self.p, "planting flowers", ["planting flowers", "planting", "gardening", "kneeling in the garden"], "planting", [ep, eo])
                return True
        return False


class Carry(T):
    id = "carry_box"
    exclusive = ("box_prop",)     # never beside a floating box: two alike boxes read as one thrown
    pose, text = "walk_box", ("carrying a box", ["carrying a box", "holding a box", "moving a box", "box"], "box")
    kinds = GROWN

    def bind(self):
        sc = self.sc
        self.p = sc.person(self.kinds)
        self.vp = sc.need(self.p, self.pose, sc.rng.choice(["neutral", "smile", "content"]), 90)

    def place(self):
        sc = self.sc
        ep = sc.eid("carrier")
        if not sc.try_put(ep, self.vp, self.stand_spots(), want_face=sc.rng.choice([1, -1])):
            return False
        t, what, key = self.text
        self.act(self.p, t, what, key, [ep])
        return True


class CarryBag(Carry):
    id = "carry_bag"
    exclusive = ()
    settings = ("street", "park")
    pose, text = "walk_bag", ("carrying a shopping bag", ["carrying a bag", "shopping", "shopping bag", "holding a bag"], "bag")


class BenchSit(T):
    id = "read_bench"
    needs = {"*": {"bench"}}
    uses = ("bench",)
    exclusive = ("bench",)
    pose, exprs = "sit_read", ("content", "focused")
    text = ("reading on the bench", ["reading", "reading a book", "sitting on the bench", "sitting and reading"], "reading")
    kinds = None

    def bind(self):
        sc = self.sc
        self.p = sc.person(self.kinds)
        self.vp = sc.need(self.p, self.pose, sc.rng.choice(self.exprs), 45)

    def seat(self, ep, frac=None):
        sc = self.sc
        B = sc.S.anchors["bench"]
        fr = [frac] if frac is not None else [0.3, 0.7, 0.5]
        for t in fr:
            x = B["x0"] + (B["x1"] - B["x0"]) * t
            for want in (1, -1):
                p = sc.placed(self.vp, 0, 0, sc.mirror_for(self.vp, want), depth_y=B["depth"] + 3, eid=ep)
                p.move_anchor_to("seat", (x, B["seat_y"]))
                if sc.fits(p.bbox(), limit=0.15):
                    sc.assets[ep] = p
                    sc.legib_ok.add(("bench", ep))
                    return p
        return None

    def place(self):
        sc = self.sc
        ep = sc.eid("sitter")
        if not self.seat(ep):
            return False
        t, what, key = self.text
        self.act(self.p, t, what, key, [ep])
        return True


class DrinkBench(BenchSit):
    id = "drink_bench"
    pose, exprs = "sit_drink", ("content", "smile")
    text = ("sitting on the bench with a drink", ["drinking", "having coffee", "drinking tea", "sitting on the bench", "cup", "mug"], "drinking")


class Picnic(T):
    id = "picnic"
    settings = ("park",)
    needs = {"park": {"blanket"}}
    uses = ("blanket",)
    # revision 16: never in the same picture as the sprinkler soaking a box (the soaked box beside a picnic basket could be
    # the picnic's own, and the picnic about to be soaked)
    exclusive = ("blanket",) + (("lawn_spray",) if SCN.PLACEMENT_REV >= 16 else ())
    # v0.15 (revision 13): no picnic under storm clouds ("stormy sky but ... people are picnicking")
    sky = "clear" if SCN.PLACEMENT_REV >= 13 else None

    def bind(self):
        sc = self.sc
        self.p = sc.person(None)
        self.vp = sc.need(self.p, "sit_ground", sc.rng.choice(["happy", "content", "smile"]), 45)

    def place(self):
        sc = self.sc
        A = sc.S.anchors["blanket"]
        ep = sc.eid("picnicker")
        for (x, y) in A["spots"]:
            p = sc.placed(self.vp, x, y, sc.rng.random() < 0.5, eid=ep)
            if sc.fits(p.bbox(), limit=0.15):
                sc.assets[ep] = p
                s = sz(y)
                bx = x + (1 if not p.mirror else -1) * 95 * s
                if SCN.PLACEMENT_REV >= 9:
                    # revision 9: on the far side from the legs, clear of the feet (drawn over the shins it
                    # seemed to pass through them)
                    feet = [p.anchor(a)[0] for a in ("foot_L", "foot_R") if p.has_anchor(a)]
                    if feet:
                        fx_ = sum(feet) / len(feet)
                        side = -1 if fx_ > x else 1
                        bx = x + side * 78 * s
                bk = D.shape(f"M {D.P(bx - 34 * s, y - 40 * s)} L {D.P(bx + 34 * s, y - 40 * s)} L {D.P(bx + 26 * s, y)} L {D.P(bx - 26 * s, y)} Z", C["wood_light"])
                bk += D.ell(bx, y - 40 * s, 36 * s, 8 * s, C["wood"], D.OW * 0.8)
                bk += f'<path d="M {D.P(bx - 26 * s, y - 42 * s)} Q {D.P(bx, y - 84 * s)} {D.P(bx + 26 * s, y - 42 * s)}" fill="none" stroke="{D.OUT}" stroke-width="5"/>'
                eb = sc.svg(sc.eid("basket"), "Picnic basket", bk, y + 1, (bx - 36 * s, y - 84 * s, bx + 36 * s, y), "scored")
                self.act(self.p, "having a picnic", ["having a picnic", "picnic", "sitting on a blanket", "sitting on the grass"], "picnic", [ep, eb])
                return True
        return False


class FlyKite(T):
    id = "fly_kite"
    settings = ("park", "garden", "playground")
    # v0.15 (revision 13): never with the gust that blows a hat away, whose wind could blow the other way
    exclusive = ("sky_kite",) + (("wind",) if SCN.PLACEMENT_REV >= 13 else ())

    def bind(self):
        sc = self.sc
        self.p = sc.person(YOUNG)
        self.vp = sc.need(self.p, "fly_kite", sc.rng.choice(["happy", "laughing", "smile"]), 90)

    def place(self):
        sc = self.sc
        ep = sc.eid("kiteflyer")
        for X, Y in self.stand_spots(n=100):
            want = 1 if X < 800 else -1
            p = sc.placed(self.vp, X, Y, sc.mirror_for(self.vp, want), eid=ep)
            if not sc.fits(p.bbox()):
                continue
            sx, sy = p.anchor("string_end")
            kx, ky = sx + want * sc.rng.uniform(260, 380), sc.rng.uniform(110, 210)
            if any(seg_cross((sx, sy), (kx, ky + 10), a, b) for a, b in getattr(sc, "strings", [])):
                continue
            # (revision 12: the tail streams downwind, away from the string, which is tied at the spars' crossing)
            # (and the kite leans into the wind, its lower point and tail away from the flyer: leaning the other way, its
            # lower spar lay along the string's last stretch)
            ksvg, kinfo = D.kite(kx, ky, 0.9, sc.rng.choice([C["yellow"], C["orange"]]), rot=-want * 20 if SCN.PLACEMENT_REV >= 12 else want * 20,
                                 wind=want if SCN.PLACEMENT_REV >= 12 else 0)   # purple is the stuck kite's colour
            if not sc.fits(kinfo["bbox"]):
                continue
            bx, by = kinfo["bridle"]
            if SCN.PLACEMENT_REV >= 4:
                # revision 4: the string and the kite keep clear of lamp posts, trees and frames (a string
                # passing the lamp head read as snagged on it)
                cx_, cy_ = (sx + bx) / 2 + want * 40, (sy + by) / 2 + 60
                pts = [((1 - t) ** 2 * sx + 2 * (1 - t) * t * cx_ + t * t * bx, (1 - t) ** 2 * sy + 2 * (1 - t) * t * cy_ + t * t * by)
                       for t in (k / 30 for k in range(3, 31))]
                kb = kinfo["bbox"]
                if not sc.air_clear((kb[0] - 8, kb[1] - 8, kb[2] + 8, kb[3] + 8), 2) or \
                        not all(sc.air_clear((qx - 6, qy - 6, qx + 6, qy + 6), 0) for qx, qy in pts):
                    continue
                # revision 11: the kite in open sky, clear of the clouds and the sun (a kite against a cloud's
                # underside seemed to hang from it)
                if SCN.PLACEMENT_REV >= 11 and not sc.setting_clear((kb[0] - 18, kb[1] - 18, kb[2] + 18, kb[1] + (kb[3] - kb[1]) * 0.45),
                                                                    only=("clouds_white", "clouds_dark", "sun")):
                    continue
                # revision 12: nor between a stalking cat and its bird
                if SCN.PLACEMENT_REV >= 12 and any(z[0] <= qx <= z[2] and z[1] <= qy <= z[3] for qx, qy in pts for z in getattr(sc, "stalk_spans", [])):
                    continue
                # revision 8: nor past anything of another event (a string beside a floating box seemed to
                # hold it up)
                if SCN.PLACEMENT_REV >= 8 and any(b[0] - 14 <= qx <= b[2] + 14 and b[1] - 14 <= qy <= b[3] + 14
                                                  for qx, qy in pts[3:] for _, b, _ in sc.scored_boxes(ignore=(ep,))):
                    continue
            sc.assets[ep] = p
            string = f'<path d="M {D.P(sx, sy)} Q {D.P((sx + bx) / 2 + want * 40, (sy + by) / 2 + 60)} {D.P(bx, by)}" fill="none" stroke="{D.OUT}" stroke-width="2.2"/>'
            ek = sc.svg(sc.eid("kite"), "Kite", (ksvg + string) if SCN.PLACEMENT_REV >= 12 else (string + ksvg), 1500, kinfo["bbox"], "scored")
            sc.strings = getattr(sc, "strings", []) + [((sx, sy), (bx, by))]
            if SCN.PLACEMENT_REV >= 13:
                # revision 13: the washing on the garden line lifts a little in the breeze that flies the kite
                from .settings import laundry_svg
                for e in sc.S.elements:
                    if e["id"] == "laundry" and e.get("svg"):
                        e["svg"] = laundry_svg(0.45 * want, lines=False)
                        b = e["bbox"]
                        e["bbox"] = (min(b[0], 620), b[1], max(b[2], 820), b[3])
            self.act(self.p, "flying a kite", ["flying a kite", "kite"], "kite", [ep, ek])
            return True
        return False


class Balloon(T):
    id = "balloon"
    settings = ("park", "street", "playground")
    # v0.13 (revision 11): never under the gust that blows a hat away (balloons hanging still beside it, "the
    # balloons, tree and awnings are unaffected by the gust")
    exclusive = ("calm_balloon",) if SCN.PLACEMENT_REV >= 11 else ()

    def bind(self):
        sc = self.sc
        self.p = sc.person(KIDS)
        pose = sc.rng.choice(["balloon", "walk_balloon"])
        self.vp = sc.need(self.p, pose, sc.rng.choice(["happy", "smile", "laughing"]), 90 if (SCN.PLACEMENT_REV >= 13 and pose == "walk_balloon") else 45)   # (revision 13: walking side on)

    def place(self):
        sc = self.sc
        ep = sc.eid("balloonkid")
        if not sc.try_put(ep, self.vp, self.stand_spots(), want_face=sc.rng.choice([1, -1])):
            return False
        self.act(self.p, "holding a balloon", ["holding a balloon", "balloon", "has a balloon"], "balloon", [ep])
        return True


class Swing(T):
    id = "swing"
    settings = ("garden",)
    needs = {"garden": {"swing"}}
    uses = ("swing",)
    exclusive = ("swing",)

    def bind(self):
        sc = self.sc
        self.p = sc.person(KIDS)
        # revision 7: facing the viewer, between the two ropes (turned three-quarters, one rope ran
        # through the child's head and the feet stuck out past the seat)
        self.vp = sc.need(self.p, "sit_swing", sc.rng.choice(["happy", "laughing", "smile"]), 0 if SCN.PLACEMENT_REV >= 7 else 45)

    def place(self):
        sc = self.sc
        A = sc.S.anchors["swing"]
        ep = sc.eid("swinger")
        sx, sy = A["seat"]
        for mirror in (False, True):
            p = sc.placed(self.vp, 0, 0, mirror, depth_y=A["depth"] - 1, eid=ep)
            p.move_anchor_to("seat", (sx, sy - 4))
            if sc.fits(p.bbox(), limit=0.15):
                sc.assets[ep] = p
                break
        else:
            return False
        sc.S.elements = [e for e in sc.S.elements if e["id"] != "swing_seat"]
        sc.legib_ok.add(("swing", ep))
        (t1, t2) = A["rope_top"]
        rl, rr = p.anchor("rope_L"), p.anchor("rope_R")
        left, right = sorted([rl, rr])
        # (revision 13: from the hands down to the ends of the seat, outside the hips, so the ropes show running on down to
        # the seat: tucked behind the child, they seemed to stop at the hands and the seat "looks unattached")
        se = 40 if SCN.PLACEMENT_REV >= 13 else 30
        ropes = D.line(t1[0], t1[1], left[0], left[1], D.OUT, 4) + D.line(left[0], left[1], sx - se, sy, D.OUT, 4)
        ropes += D.line(t2[0], t2[1], right[0], right[1], D.OUT, 4) + D.line(right[0], right[1], sx + se, sy, D.OUT, 4)
        seat = D.rect(sx - 42, sy - 4, 84, 13, C["red"], 3)
        if SCN.PLACEMENT_REV >= 9:
            # revision 9: two motion arcs behind the seat, along the swing's path (a still, straight swing
            # "doesn't seem to be swinging")
            d_ = sc.rng.choice([1, -1])
            pivot = ((t1[0] + t2[0]) / 2, t1[1])
            R0 = sy - pivot[1]
            for k_, (dr, a0, a1) in enumerate(((0, 9, 20), (-16, 10, 18))):
                R_ = R0 + dr
                pts_ = [(pivot[0] + d_ * R_ * math.sin(math.radians(a)), pivot[1] + R_ * math.cos(math.radians(a))) for a in (a0, (a0 + a1) / 2, a1)]
                seat += f'<path d="M {D.P(*pts_[0])} Q {D.P(*pts_[1])} {D.P(*pts_[2])}" fill="none" stroke="{D.OUT}" stroke-width="2.6" stroke-linecap="round" stroke-opacity="0.7"/>'
        sc.svg(sc.eid("swingseat"), "Swing seat and ropes", ropes + seat, A["depth"] - 2, (sx - 45, t1[1], sx + 45, sy + 10), "setting")
        self.act(self.p, "on the swing", ["on the swing", "swinging", "playing on the swing", "sitting on a swing"], "swing", [ep])
        return True


class HangLaundry(T):
    id = "hang_laundry"
    settings = ("garden",)
    needs = {"garden": {"clothesline", "laundry"}}
    uses = ("laundry",)
    exclusive = ("clothesline",) + (("calm_laundry",) if SCN.PLACEMENT_REV >= 11 else ())   # nor with the gust

    def bind(self):
        sc = self.sc
        # revision 5: a grown-up only (the teenager cannot reach the line without floating off the ground,
        # so a picture that cast him here could never be placed)
        self.p = sc.person(ADULTS if SCN.PLACEMENT_REV >= 5 else GROWN)
        self.vp = sc.need(self.p, "hang_washing", sc.rng.choice(["focused", "content", "neutral"]), 90)

    def place_rev1(self):
        """Placement revision 1 (kept so the first v0.5 records rebuild exactly): the shirt was drawn
        behind the clothesline and the hung clothes, so this almost never passed the occlusion rule."""
        sc = self.sc
        A = sc.S.anchors["clothesline"]
        ep = sc.eid("hanger")
        for x in (860, 820, 880, 840):
            for want in (1, -1):
                p = sc.placed(self.vp, x, A["depth"], sc.mirror_for(self.vp, want), eid=ep)
                hl, hr = p.anchor("hand_L_grip"), p.anchor("hand_R_grip")
                hx = (hl[0] + hr[0]) / 2
                ty = A["fn"](hx) + 8
                p.Y += ty - (hl[1] + hr[1]) / 2
                p.set_depth(A["depth"])
                if p.Y < A["depth"] - 30 or p.Y > A["depth"] + 60 or not sc.fits(p.bbox(), limit=0.2):
                    continue
                sc.assets[ep] = p
                sc.legib_ok |= {("clothesline", ep), ("laundry", ep)}
                hl, hr = p.anchor("hand_L_grip"), p.anchor("hand_R_grip")
                x0, x1 = min(hl[0], hr[0]), max(hl[0], hr[0])
                if x1 - x0 < 46:
                    x0, x1 = x1 - 8, x1 + 50
                yt = A["fn"]((x0 + x1) / 2)
                shirt = D.poly([(x0 - 4, yt), (x1 + 4, yt), (x1 + 18, yt + 24), (x1 + 2, yt + 32), (x1 - 2, yt + 88), (x0 + 2, yt + 88), (x0 - 2, yt + 32), (x0 - 18, yt + 24)], C["white"])
                es = sc.svg(sc.eid("shirt"), "Shirt being pinned up", shirt, p.Y - 1, (x0 - 18, yt, x1 + 18, yt + 88), "scored")
                self.act(self.p, "hanging up laundry", ["hanging laundry", "hanging clothes", "hanging up the washing", "pinning clothes", "clothesline"], "laundry", [ep, es])
                return True
        return False

    def place(self):
        if SCN.PLACEMENT_REV < 2:
            return self.place_rev1()
        sc = self.sc
        A = sc.S.anchors["clothesline"]
        ep = sc.eid("hanger")
        lo, hi = 790, 936          # free stretch of line: right of the hung clothes, left of the far post

        def pose_at(x, want):
            p = sc.placed(self.vp, x, A["depth"], sc.mirror_for(self.vp, want), eid=ep)
            hl, hr = p.anchor("hand_L_grip"), p.anchor("hand_R_grip")
            p.Y += A["fn"]((hl[0] + hr[0]) / 2) + 8 - (hl[1] + hr[1]) / 2
            p.set_depth(A["depth"])
            hl, hr = p.anchor("hand_L_grip"), p.anchor("hand_R_grip")
            f = 1 if (hl[0] + hr[0]) / 2 >= p.anchor("mouth")[0] else -1
            b = p.bbox()
            s = max(0.7, min(1.3, (b[3] - b[1]) / 260))
            hx = max(hl[0], hr[0]) if f > 0 else min(hl[0], hr[0])
            xn = hx + f * 10 * s
            x0, x1 = sorted((xn, xn + f * 56 * s))
            return p, s, x0, x1

        for c in ((852, 842, 864, 876) + ((888, 900, 830) if SCN.PLACEMENT_REV >= 19 else ())):
            for want in (1, -1):
                # the hands pin the near shoulder of the shirt; the shirt hangs ahead of the person on
                # the free part of the line, clear of the face, the hung clothes and the posts
                p, s, x0, x1 = pose_at(860, want)
                p, s, x0, x1 = pose_at(860 + c - (x0 + x1) / 2, want)
                sl, sh = 18 * s, 88 * s
                b = p.bbox()
                if x0 - sl < lo or x1 + sl > hi or b[0] < 645 or b[2] > (962 if SCN.PLACEMENT_REV >= 19 else 936):
                    # (revision 19: she may stand just past the far post, so that facing back along the line her head is
                    # clear of the clothes already hung)
                    continue
                if p.Y < A["depth"] - 30 or p.Y > A["depth"] + 60 or not sc.fits(b, limit=0.2):
                    continue
                if SCN.PLACEMENT_REV >= 19:
                    # revision 19: her head clear of the clothes already hung (a yellow shirt behind her head "can read as part
                    # of her clothing")
                    lb = next((e["bbox"] for e in sc.S.elements if e["id"] == "laundry" and e.get("bbox")), None)
                    hd = SCN.head_box(p)
                    if lb is not None and min(hd[2], lb[2] + 8) > max(hd[0], lb[0] - 8) and min(hd[3], lb[3] + 8) > max(hd[1], lb[1] - 8):
                        continue
                p.z = A["depth"] + 2          # in front of the line and the hung clothes
                sc.assets[ep] = p
                yt = A["fn"]((x0 + x1) / 2)
                shirt = D.poly([(x0 - 4 * s, yt), (x1 + 4 * s, yt), (x1 + sl, yt + 24 * s), (x1 + 2 * s, yt + 32 * s), (x1 - 2 * s, yt + sh),
                                (x0 + 2 * s, yt + sh), (x0 - 2 * s, yt + 32 * s), (x0 - sl, yt + 24 * s)], C["white"])
                pegs = "".join(D.rect(x - 2 * s, yt - 4 * s, 4 * s, 9 * s, C["wood_light"], 1, D.OW * 0.6) for x in (x0 + 2 * s, x1 - 2 * s))
                es = sc.eid("shirt")
                sc.svg(es, "Shirt being pinned up", shirt + pegs, A["depth"] + 1.5, (x0 - sl, yt - 4 * s, x1 + sl, yt + sh), "scored")
                sc.legib_ok |= {("clothesline", ep), ("laundry", ep), (es, ep)}
                self.act(self.p, "hanging up laundry", ["hanging laundry", "hanging clothes", "hanging up the washing", "pinning clothes", "clothesline"], "laundry", [ep, es])
                return True
        return False


class PlayCatch(T):
    id = "play_catch"
    content = 2

    def bind(self):
        sc = self.sc
        self.a = sc.person(YOUNG)
        self.b = sc.person(YOUNG + ("adult",))
        self.va = sc.need(self.a, "throw_ball", sc.rng.choice(["happy", "determined", "smile"]), 90)
        self.vb = sc.need(self.b, "catch", sc.rng.choice(["happy", "surprised", "smile"]), 90)

    def place(self):
        sc = self.sc
        ea, eb = sc.eid("thrower"), sc.eid("catcher")
        for X, Y in self.stand_spots(n=100):
            gap = sc.rng.uniform(300, 430) * sz(Y)
            want = 1 if X < 800 else -1
            Xb, Yb = X + want * gap, Y + sc.rng.uniform(-25, 25)
            if not sc.S.walkable(Xb, Yb):
                continue
            pa = sc.placed(self.va, X, Y, sc.mirror_for(self.va, want), eid=ea)
            pb = sc.placed(self.vb, Xb, Yb, sc.mirror_for(self.vb, -want), eid=eb)
            if not (sc.fits(pa.bbox()) and sc.fits(pb.bbox()) and sc.overlap(pa.bbox(), pb.bbox()) < 0.05):
                continue
            s = sz(Y)
            rx_, ry_ = pa.anchor("release") if pa.has_anchor("release") else pa.anchor("hand_R_grip")
            gl, gr = pb.anchor("hand_L_grip"), pb.anchor("hand_R_grip")
            cx, cy = (gl[0] + gr[0]) / 2, (gl[1] + gr[1]) / 2
            ctrl = ((rx_ + cx) / 2, min(ry_, cy) - 230 * s)
            t = 0.52
            if SCN.PLACEMENT_REV >= 14:
                # revision 14: a lower arc, the ball past its top and coming down toward the catcher's hands (at the top
                # of a high arc, "already above the man's hands, so it may sail over his head")
                ctrl = ((rx_ + cx) / 2, min(ry_, cy) - 150 * s)
                t = 0.72

            def bez(t):
                return ((1 - t) ** 2 * rx_ + 2 * (1 - t) * t * ctrl[0] + t * t * cx, (1 - t) ** 2 * ry_ + 2 * (1 - t) * t * ctrl[1] + t * t * cy)
            bx, by = bez(t)
            r = 15 * s
            if not sc.fits((bx - r * 2, by - r * 2, bx + r * 2, by + r * 2), limit=0.02, ignore=(ea, eb)):
                continue
            # revision 4: the whole flight from hand to hand stays clear of trees, lamps and frames
            # (a path into a canopy read as a throw that would end in the tree)
            if SCN.PLACEMENT_REV >= 4 and not all(sc.air_clear((qx - 4, qy - 4, qx + 4, qy + 4), 0) for qx, qy in (bez(k / 24) for k in range(2, 23))):
                continue
            # revision 14: and never over the pond (a throw across it "could fall short into the water")
            if SCN.PLACEMENT_REV >= 14 and "pond" in sc.S.anchors and not all(
                    sc.setting_clear((qx - 6, qy - 6, qx + 6, qy + 6), only=("pond",)) for qx, qy in (bez(k / 24) for k in range(0, 25))):
                continue
            if SCN.PLACEMENT_REV >= 14 and "pond" in sc.S.anchors and not sc.setting_clear((min(X, Xb), min(Y, Yb) - 30, max(X, Xb), max(Y, Yb) + 10), only=("pond",)):
                continue
            if SCN.PLACEMENT_REV >= 8:
                # revision 8: the flight clear of everyone else, and kept clear of later placements (a kite
                # flyer placed beside the ball seemed to be throwing it or about to be hit)
                fl = [bez(k / 24) for k in range(1, 24)]
                zone = (min(q[0] for q in fl) - r, min(q[1] for q in fl) - 2 * r, max(q[0] for q in fl) + r, max(q[1] for q in fl) + r)
                mg = 60 * s if SCN.PLACEMENT_REV >= 11 else 10
                # (revision 11: a wider margin; a ball arcing just past a cat on the fence "arcs toward the fence
                # top and the cat")
                if any(min(zone[2], b[2]) + mg > max(zone[0], b[0]) - mg and min(zone[3], b[3]) + mg > max(zone[1], b[1]) - mg
                       and any(b[0] - mg <= qx <= b[2] + mg and b[1] - mg <= qy <= b[3] + mg for qx, qy in fl)
                       for k_, q_ in sc.assets.items() if k_ not in (ea, eb) for b in (q_.bbox(),)):
                    continue
            if SCN.PLACEMENT_REV >= 9:
                # revision 9: nobody stands between the two players, and no kite string crosses the flight (a
                # kite holder under the ball's arc, her string through it, made three people one tangle)
                lo, hi = sorted([pa.X, pb.X])
                if any(q_.family.startswith("person.") and lo - 20 < q_.X < hi + 20 and abs(q_.Y - (Y + Yb) / 2) < 160
                       for k_, q_ in sc.assets.items() if k_ not in (ea, eb)):
                    continue
                if any(math.hypot(qx - (ax + (bx2 - ax) * u / 12), qy - (ay + (by2 - ay) * u / 12)) < 30
                       for (ax, ay), (bx2, by2) in getattr(sc, "strings", []) for u in range(13) for qx, qy in fl):
                    continue
            if SCN.PLACEMENT_REV >= 16:
                # revision 16: and nobody just behind the catcher, where a missed ball would go (a man reading beside the
                # catcher: the ball "could hit the reading old man instead of reaching the catcher")
                cb = pb.bbox()
                behind = (cb[2], cb[1], cb[2] + 110 * s, cb[3]) if want > 0 else (cb[0] - 110 * s, cb[1], cb[0], cb[3])
                if any(min(behind[2], b[2]) > max(behind[0], b[0]) and min(behind[3], b[3]) > max(behind[1], b[1])
                       for k_, q_ in sc.assets.items() if k_ not in (ea, eb) for b in (q_.bbox(),)):
                    continue
            sc.assets[ea], sc.assets[eb] = pa, pb
            if SCN.PLACEMENT_REV >= 16:
                sc.airzones.append(behind)
            if SCN.PLACEMENT_REV >= 8:
                m_ = 60 * s if SCN.PLACEMENT_REV >= 11 else 0
                sc.airzones.append((min(q[0] for q in fl) - 12 - m_, min(q[1] for q in fl) - 2 * r - 8 - m_,
                                    max(q[0] for q in fl) + 12 + m_, max(q[1] for q in fl) + r))
            if SCN.PLACEMENT_REV >= 9:
                # and the ground between and just beside them stays free of later placements (a photographer
                # placed right against the thrower)
                ba, bb_ = pa.bbox(), pb.bbox()
                sc.airzones.append((min(ba[0], bb_[0]) - 40 * s, min(ba[1], bb_[1]), max(ba[2], bb_[2]) + 40 * s, max(ba[3], bb_[3])))
            # dotted trail from the hand to the ball: the ball has just left the thrower's hand
            trail = " ".join(D.P(*bez(k / 10 * (t - 0.08))) for k in range(11))
            arc = f'<path d="M {trail}" fill="none" stroke="{D.OUT}" stroke-width="2.4" stroke-dasharray="5 9" stroke-linecap="round" stroke-opacity="0.65"/>'
            eb_ = sc.svg(sc.eid("ball"), "Ball in the air", arc + D.ball(bx, by, r), max(Y, Yb) + 1, (bx - r, by - r, bx + r, by + r), "scored")
            self.act(self.a, "throwing a ball", ["throwing a ball", "throwing", "playing catch", "playing ball"], "ball", [ea, eb_])
            self.act(self.b, "catching the ball", ["catching the ball", "catching", "playing catch", "playing ball"], "ball", [eb])
            return True
        return False


class KickBall(T):
    id = "kick_ball"
    settings = ("park", "garden", "playground")

    def bind(self):
        sc = self.sc
        if SCN.PLACEMENT_REV >= 10:
            # revision 10: a low kick at the ball on the ground (pose kick_low), by a child in shorts or
            # trousers (a straight leg out from under a skirt read as "a wooden bat with a yellow end")
            # (revision 14: the teenager first, whose face shows side on; under the boy's curls the head "faces left ... the
            # torso and the outstretched arm point right ... as if kicking backward")
            self.p = sc.person(YOUNG, avoid=("person.nia",), prefer=("person.leo",) if SCN.PLACEMENT_REV >= 14 else ())
            self.vp = sc.need(self.p, "kick_low", sc.rng.choice(["happy", "determined"]), 90)
            return
        self.p = sc.person(YOUNG)
        self.vp = sc.need(self.p, "kick", sc.rng.choice(["happy", "determined"]), 90)

    def place(self):
        sc = self.sc
        ep = sc.eid("kicker")
        rev10 = SCN.PLACEMENT_REV >= 10

        def ballpos(p):
            f = p.facing() or 1
            s = sz(p.Y)
            fx, fy = max([p.anchor("foot_L"), p.anchor("foot_R")], key=lambda q: q[0] * f)
            if rev10:
                # revision 10: the ball on the ground at the toe of the kicking foot (a ball level with
                # the hip seemed to hover), and the kicker in the front half of the picture, as large as
                # the people around (small and far back, the kick read as a bat)
                if p.Y < 740:
                    return None
                self.b = (fx + f * 34 * s, p.Y - 15 * s)
                if SCN.PLACEMENT_REV >= 17:
                    # revision 17: the ball against the toe of the kicking foot (a little ahead of it on the ground, the
                    # foot seemed "stretched past/over the ball ... a swing-and-miss")
                    toe = self.toe(p, f)
                    if toe:
                        r_ = 17 * s
                        self.b = (toe[0] + f * 0.80 * r_, min(toe[1] + 0.15 * r_, p.Y - r_))
                # the ground ahead of the ball, where it is going, is clear of everything else (a ball kicked
                # into the square-wheeled wheelbarrow, or at a play-bowing dog with its own ball)
                bx_, by_ = self.b
                self.kz = (min(bx_ - 20 * s, bx_ + f * 150 * s), by_ - 50 * s, max(bx_ + 20 * s, bx_ + f * 150 * s), p.Y + 25 * s)
                if self.kz[0] < 30 or self.kz[2] > D.W - 30:
                    return None
                pb_ = p.bbox()
                room = (pb_[0] - 45 * s, pb_[1], pb_[2] + 45 * s, pb_[3] + 40 * s)
                if any(sc.overlap(room, q.bbox()) > 0 for k_, q in sc.assets.items() if k_ != ep):
                    return None
                if any(sc.overlap(self.kz, q.bbox()) > 0 for q in sc.assets.values()) or \
                        any(sc.overlap(self.kz, e["bbox"]) > 0 for e in sc.svgs.values() if e.get("bbox") and e["role"] in ("scored", "filler")):
                    return None
                if SCN.PLACEMENT_REV >= 11:
                    # revision 11: further ahead, the line the ball will roll along keeps clear of every person
                    # and animal and of trees and play equipment (a ball kicked toward a child at the sandbox
                    # "may be heading for the child"; another "flying toward the tree or the girl")
                    far = self.far = (min(bx_, bx_ + f * 420 * s), by_ - 120 * s, max(bx_, bx_ + f * 420 * s), p.Y + 60 * s)
                    if any(sc.overlap(far, q.bbox()) > 0 for k_, q in sc.assets.items() if k_ != ep):
                        return None
                    if SCN.PLACEMENT_REV >= 14:
                        # revision 14: and clear of other events' things too, and of people further back in the kick's
                        # direction ("the kicked ball may be heading toward the painter and the paint tin")
                        wide = self.wide = (far[0], by_ - 300 * s, far[2], far[3])
                        if any(sc.overlap(wide, q.bbox()) > 0 for k_, q in sc.assets.items() if k_ != ep and q.family.startswith(("person.", "animal."))
                               and not q.m["variant"].get("airborne")):
                            return None
                        if any(sc.overlap(far, e["bbox"]) > 0 for e in sc.svgs.values() if e.get("bbox") and e["role"] in ("scored", "filler")):
                            return None
                    near = (min(bx_, bx_ + f * 260 * s), by_ - 40 * s, max(bx_, bx_ + f * 260 * s), p.Y + 20 * s)
                    if not sc.setting_clear(near, only=("tree", "tree_small", "sandbox", "slide", "swing", "seesaw", "bench", "lamp", "pond")):
                        return None
                    if SCN.PLACEMENT_REV >= 19:
                        # revision 19: further on, the ball's line clear of the sandpit and of anyone on the ground (a ball
                        # kicked from across the playground "heading toward the girl and her sandcastle")
                        line = (min(bx_, bx_ + f * 760 * s), by_ - (320 if SCN.PLACEMENT_REV >= 20 else 120) * s, max(bx_, bx_ + f * 760 * s), p.Y + 60 * s)
                        # (revision 20: higher up the picture too: a ball kicked across a garden "flying toward the woman and
                        # the washing" behind)
                        if not sc.setting_clear(line, only=("sandbox",)):
                            return None
                        if any(sc.overlap(line, q.bbox()) > 0 for k_, q in sc.assets.items() if k_ != ep and q.family.startswith(("person.", "animal."))
                               and not q.m["variant"].get("airborne")):
                            return None
                return [(self.b[0] - 17 * s, self.b[1] - 17 * s, self.b[0] + 17 * s, self.b[1] + 17 * s)]
            self.b = (fx + f * 34 * s, fy - 14 * s)
            return [(self.b[0] - 17 * s, self.b[1] - 17 * s, self.b[0] + 17 * s, self.b[1] + 17 * s)]
        p = self.place_with(ep, self.vp, self.stand_spots(), want_face=sc.rng.choice([1, -1]), extras=ballpos)
        if not p:
            return False
        s = sz(p.Y)
        bx, by = self.b
        shadow_y = by + 15 * s if SCN.PLACEMENT_REV < 17 else p.Y - 1 * s
        # revision 5: an orange ball (two alike blue balls, one kicked and one up a tree, read as one)
        bc = C["orange"] if SCN.PLACEMENT_REV >= 5 else C["blue"]
        bsvg = D.ball(bx, by, 17 * s, bc)
        if rev10:
            # v0.12: the ball's own ground shadow ("the ball has no shadow ... it isn't obvious whether the
            # ball is resting on the grass or has just lifted off")
            bsvg = D.shadow(bx, shadow_y, 30 * s) + bsvg
            sc.groundzones.append(self.kz)      # nothing placed later lands there either, drawn objects included
            if SCN.PLACEMENT_REV >= 11:
                sc.airzones.append(self.far)    # and no person or animal placed later stands in the ball's way
            if SCN.PLACEMENT_REV >= 14:
                sc.airzones.append(self.wide)   # nor further back in the kick's direction
            pb = p.bbox()
            sc.airzones.append((pb[0] - 45 * s, pb[1], pb[2] + 45 * s, pb[3] + 20 * s))   # and room around the kicker
            # two swing arcs behind the kicking foot: the leg is swinging forward into the ball, the toe
            # at the ball (a ball just ahead of a still foot read as walking past it, or a back-heel)
            f = p.facing() or 1
            fx_, fy_ = max([p.anchor("foot_L"), p.anchor("foot_R")], key=lambda q: q[0] * f)
            if p.has_anchor("seat"):
                # v0.12: the arcs follow the foot's swing about the hip, behind and below the raised foot
                # (drawn up the back of a raised leg they hung from the shin: "an untied shoelace")
                sx_, sy_ = p.anchor("seat")
                R = math.hypot(fx_ - sx_, fy_ - sy_)
                th = math.degrees(math.atan2(fy_ - sy_, fx_ - sx_))
                for k_, rf in enumerate((0.97, 0.80)):
                    t0 = th + f * (10 + 4 * k_)
                    t1 = th + f * (44 - 6 * k_)
                    t1 = min(t1, 94.0) if f > 0 else max(t1, 86.0)
                    pts = [(sx_ + R * rf * math.cos(math.radians(t0 + (t1 - t0) * i / 8)),
                            sy_ + R * rf * math.sin(math.radians(t0 + (t1 - t0) * i / 8))) for i in range(9)]
                    bsvg += f'<path d="{D.poly_d(pts)}" fill="none" stroke="{D.OUT}" stroke-width="{2.4 * s:.1f}" stroke-linecap="round" stroke-opacity="0.75"/>'
            else:
                for k_ in range(2):
                    o = (14 + 11 * k_) * s
                    a0 = (fx_ - f * o, fy_ + 2 * s)
                    a1 = (fx_ - f * (o + 26 * s), fy_ - (30 + 6 * k_) * s)
                    c_ = (fx_ - f * (o + 22 * s), fy_ - 2 * s)
                    bsvg += f'<path d="M {D.P(*a0)} Q {D.P(*c_)} {D.P(*a1)}" fill="none" stroke="{D.OUT}" stroke-width="{2.4 * s:.1f}" stroke-linecap="round" stroke-opacity="0.75"/>'

        eb = sc.svg(sc.eid("ball"), "Ball", bsvg, p.Y + 2, (bx - 17 * s, by - 17 * s, bx + 17 * s, by + 17 * s), "scored")
        self.act(self.p, "kicking a ball", ["kicking a ball", "playing soccer", "playing football", "kicking"], "ball", [ep, eb])
        return True


    @staticmethod
    def toe(p, f):
        """Revision 17: the tip of the kicking foot, the figure's frontmost outline point in its lowest third."""
        from . import compose as K
        import numpy as np
        m = K.asset_mask(p, False)
        b = p.bbox()
        y0 = int((b[3] - 0.33 * (b[3] - b[1])) * K.MASK_SCALE)
        sub = m[y0:int(b[3] * K.MASK_SCALE) + 1]
        ys, xs = np.nonzero(sub)
        if xs.size == 0:
            return None
        i = int(np.argmax(xs * f))
        cols = xs * f == xs[i] * f
        return (xs[i] / K.MASK_SCALE, (y0 + float(np.mean(ys[cols]))) / K.MASK_SCALE)


class Jump(T):
    id = "jump"

    def bind(self):
        sc = self.sc
        self.p = sc.person(YOUNG)
        # revision 5: a star jump, legs spread and feet well off the ground (the low jump read as kneeling)
        self.vp = sc.need(self.p, "jump_tuck" if SCN.PLACEMENT_REV >= 5 else "jump", sc.rng.choice(["laughing", "happy"]), 45)

    def place(self):
        sc = self.sc
        ep = sc.eid("jumper")
        accept = None
        if SCN.PLACEMENT_REV >= 14:
            # revision 14: never jumping under the washing line (read as "jumping up toward the washing line, perhaps
            # to grab the clothes")
            cl = sc.S.anchors.get("clothesline")
            if isinstance(cl, dict):
                accept = lambda p: not (cl["x0"] - 60 <= p.X <= cl["x1"] + 60 and p.Y < cl["depth"] + 180)
        if SCN.PLACEMENT_REV >= 18:
            # revision 18: no bird over or beside the raised hands, now or later (a boy jumping just below a bird perched
            # on the fence read as "jumping with his arms up near a blue bird", reaching for it)
            base = accept

            def accept(p, base=base):
                if base and not base(p):
                    return False
                z = self.bird_zone(p)
                return not any(q.family.startswith("animal.bird") and min(q.bbox()[2], z[2]) > max(q.bbox()[0], z[0])
                               and min(q.bbox()[3], z[3]) > max(q.bbox()[1], z[1]) for q in sc.assets.values())
        if SCN.PLACEMENT_REV >= 20:
            # revision 20: no standing structure behind the jumper (in front of the fruit stall, his feet over its table
            # legs, a teenager jumping for joy read as standing "with both arms up ... cheering, stretching or dancing")
            base20 = accept

            def accept(p, base=base20):
                if base and not base(p):
                    return False
                b, s_ = p.bbox(), sz(p.Y)
                return sc.setting_clear((b[0] - 24 * s_, b[1], b[2] + 24 * s_, b[3] + 40 * s_), only=sc.LANE_STRUCT + ("house", "planter"))
        # (revision 20: and in the front half of the ground, where the gap under the feet is big enough to see: at the back,
        # by the playground's fence or the street's shop fronts, the jump read as "jumping or cheering ... or just a loosely
        # placed shadow"; in front it read as "jumping in the air with both arms raised" in the test scenes)
        spots = self.stand_spots(y_range=(sc.S.horizon + 200, 970)) if SCN.PLACEMENT_REV >= 20 else self.stand_spots()
        p = sc.try_put(ep, self.vp, spots, want_face=sc.rng.choice([1, -1]), accept=accept)
        if not p:
            return False
        if SCN.PLACEMENT_REV >= 18:
            sc.no_bird = list(getattr(sc, "no_bird", [])) + [self.bird_zone(p)]
        self.act(self.p, "jumping for joy", ["jumping", "jumping for joy", "excited", "happy", "cheering"], "jumping", [ep])
        return True

    @staticmethod
    def bird_zone(p):
        b, s = p.bbox(), sz(p.Y)
        h = b[3] - b[1]
        return (b[0] - 130 * s, b[1] - 260 * s, b[2] + 130 * s, b[1] + 0.45 * h)


class Photo(T):
    id = "photo"
    settings = ("park", "street", "playground")

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        # revision 8: a three-quarter view (seen from behind, the head read as "a plain dark round shape")
        self.vp = sc.need(self.p, "photo", sc.rng.choice(["focused", "smile"]), 45 if SCN.PLACEMENT_REV >= 8 else 90)

    def place(self):
        sc = self.sc
        target = {"park": "pond", "street": "stall", "playground": "slide"}[sc.setting_id]
        tb = next((e["bbox"] for e in sc.S.elements if e["id"] == target), None) or (700, 600, 900, 700)
        tx = (tb[0] + tb[2]) / 2
        ep = sc.eid("photographer")
        if SCN.PLACEMENT_REV >= 5:
            # revision 5: the camera points at someone already in the picture, at a sensible distance,
            # and the gaze check confirms it (readers asked what the photographer was photographing)
            subjects = [q for k, q in sc.assets.items() if q.role == "scored" and q.family.startswith(("person.", "animal."))
                        and not q.m["variant"].get("airborne")]
            for X, Y in (self.stand_spots(n=150) if subjects else []):
                near = [q for q in subjects if 220 <= abs(q.X - X) <= 650 and abs(q.Y - Y) <= 140]
                if not near:
                    continue
                q = min(near, key=lambda q: abs(abs(q.X - X) - 380))
                p = sc.placed(self.vp, X, Y, sc.mirror_for(self.vp, 1 if q.X > X else -1), eid=ep)
                if not sc.fits(p.bbox()):
                    continue
                qb = q.bbox()
                if not sc.gaze_ok(p, (qb[0] - 20, qb[1] - 30, qb[2] + 20, qb[3] + 10)):
                    continue
                if SCN.PLACEMENT_REV >= 15:
                    # revision 15: nothing standing between the lens and the subject (a lamp post "almost in front of the
                    # lens ... blocking his shot")
                    hx, hy = p.anchor("head_top") if p.has_anchor("head_top") else (X, Y - 300 * sz(Y))
                    hy += 40 * sz(Y)
                    tx_, ty_ = (qb[0] + qb[2]) / 2, qb[1] + 0.35 * (qb[3] - qb[1])
                    if not all(sc.setting_clear((hx + (tx_ - hx) * t / 12 - 8, hy + (ty_ - hy) * t / 12 - 8, hx + (tx_ - hx) * t / 12 + 8,
                                                 hy + (ty_ - hy) * t / 12 + 8), only=("lamp", "tree", "tree_small", "slide", "swing", "stall"))
                               for t in range(1, 12)):
                        continue
                sc.assets[ep] = p
                sc.checks[f"{ep}_photographs_{q.id}"] = True
                self.act(self.p, "taking a photo", ["taking a picture", "taking a photo", "photographing", "camera"], "camera", [ep])
                return True
            if subjects or SCN.PLACEMENT_REV >= 15:
                # revision 15: never a photographer with nobody to photograph (alone in a probe, with the camera on the
                # pond, he "holds binoculars or a camera up to his face ... at nothing visible")
                return False
            # nobody else in the picture (a forced test plan): the camera faces the setting's landmark
        if not sc.try_put(ep, self.vp, self.stand_spots(), want_face=self.face_to(tx)):
            return False
        self.act(self.p, "taking a photo", ["taking a picture", "taking a photo", "photographing", "camera"], "camera", [ep])
        return True


class Fishing(T):
    id = "fishing"
    exempt_extra = ("pond",)      # revision 10: stands at the water's edge on purpose
    settings = ("park",)

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.vp = sc.need(self.p, "fish", sc.rng.choice(["content", "focused", "sleepy"]), 90)

    def place(self):
        sc = self.sc
        A = sc.S.anchors["pond"]
        ep = sc.eid("fisher")
        for (x, y) in A["shore"]:
            want = 1 if A["center"][0] > x else -1
            p = sc.try_put(ep, self.vp, [(x, y), (x + 20, y + 10), (x - 20, y + 10)], want_face=want, limit=0.15)
            if p:
                tx, ty = p.anchor("rod_tip")
                wx = tx + want * 30
                cx, cy, rx, ry = A["center"][0], A["center"][1], A["rx"], A["ry"]
                wy = cy + ry * 0.2
                if SCN.PLACEMENT_REV >= 16:
                    # revision 16: the line and its float clear of every other figure, and kept clear of later ones (a man
                    # feeding the ducks stood with the float at his hand: "the fishing float lands right beside the man and
                    # near the crumbs")
                    lz = (min(tx, wx) - 40, ty - 10, max(tx, wx) + 40, wy + 24)
                    if any(min(lz[2], b[2]) > max(lz[0], b[0]) and min(lz[3], b[3]) > max(lz[1], b[1])
                           for k_, q_ in sc.assets.items() if k_ != ep for b in (q_.bbox(),)):
                        sc.remove(ep)
                        continue
                    sc.airzones.append(lz)
                if SCN.PLACEMENT_REV >= 21:
                    # revision 21: no duck at the float or on the line, now or later ("a duck swimming close to the float, so the
                    # duck might go for the bait or get tangled in the line")
                    if any(getattr(q_, "family", "").startswith("animal.duck") and
                           ((lambda b: b[0] - 60 <= wx <= b[2] + 60 and b[1] - 36 <= wy <= b[3] + 36)(q_.bbox()) or sc.faces_toward(q_, wx))
                           for k_, q_ in sc.assets.items() if k_ != ep):
                        sc.remove(ep)
                        sc.airzones.pop()
                        continue
                    sc.floats.append((wx, wy))
                    sc.fish_lines.append(((tx, ty), (wx, wy)))
                line = f'<path d="M {D.P(tx, ty)} Q {D.P(wx, (ty + wy) / 2)} {D.P(wx, wy)}" fill="none" stroke="{D.OUT}" stroke-width="2"/>'
                line += D.circ(wx, wy - 4, 6, C["red"], D.OW * 0.6)
                line += f'<ellipse cx="{wx:.1f}" cy="{wy + 4:.1f}" rx="18" ry="5" fill="none" stroke="{C["white"]}" stroke-width="2.5"/>'
                el = sc.svg(sc.eid("line"), "Fishing line", line, -65, (min(tx, wx) - 18, ty, max(tx, wx) + 18, wy + 10), "scored")
                self.act(self.p, "fishing", ["fishing", "fishing in the pond", "fishing rod", "catching fish"], "fishing", [ep, el])
                return True
        return False


class FeedBirds(T):
    id = "feed_birds"
    settings = ("park", "street")
    content = 1

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        # revision 5: the seed hand held low toward the birds, head bowed to them (with the head level the
        # feeder seemed to face whatever was behind the birds, and a leaking bag was read instead)
        self.vp = sc.need(self.p, "feed_birds_low" if SCN.PLACEMENT_REV >= 5 else "feed_birds", sc.rng.choice(["smile", "content", "happy"]), 90)
        self.b1 = sc.animal(["songbird"])
        self.vb1 = sc.need(self.b1, "peck", "neutral", 90)
        self.vb2 = None
        try:
            self.b2 = sc.animal(["songbird"])
            self.vb2 = sc.need(self.b2, "peck", "neutral", 90)
        except PlacementError:
            pass

    def place(self):
        sc = self.sc
        ep = sc.eid("feeder_person")
        want = sc.rng.choice([1, -1])
        if SCN.PLACEMENT_REV >= 4:
            # revision 4: a spot is only taken if the first bird fits in front of the hand (feeding
            # with no bird there read as scattering seed at nothing)
            # (the bird stands just past the feeder's reach, so it never sits inside the feeder's box)
            def bird_fits(p):
                bx = self._bird_x(p, self.vb1, 0)
                b = sc.placed(self.vb1, bx, p.Y + 6, sc.mirror_for(self.vb1, -(p.facing() or want)))
                ok = (sc.fits(b.bbox(), limit=0.3) and sc.overlap(b.bbox(), p.bbox()) <= 0.3
                      and sc.S.walkable(b.X, b.Y))
                if ok and SCN.PLACEMENT_REV >= 5:
                    # the bowed head points at the bird (within 40 degrees; the bird is at the feeder's
                    # feet, steeper than any gaze ray drawn from the eyes)
                    from .library import gaze_angle_to
                    bb_ = b.bbox()
                    ok = gaze_angle_to(p, ((bb_[0] + bb_[2]) / 2, (bb_[1] + bb_[3]) / 2)) <= 40
                return ok
            p = sc.try_put(ep, self.vp, self.stand_spots(), want_face=want, accept=bird_fits)
        else:
            p = sc.try_put(ep, self.vp, self.stand_spots(), want_face=want)
        if not p:
            return False
        f = p.facing() or want
        s = sz(p.Y)
        sx, sy = p.anchor("seed_from")
        seeds = "".join(D.circ(sx + f * (20 + i * 9) * s, p.Y + (i % 3) * 4 * s - 2, 2.5 * s, C["khaki"], D.OW * 0.3) for i in range(8))
        # a trail of seeds falling from the open hand: what the hand is doing (an empty hand read as
        # holding a brush or a sanding block)
        for i in range(7):
            t = (i + 0.5) / 7
            fx_ = sx + f * (8 + 46 * t) * s
            fy_ = sy + (p.Y - sy) * (t ** 1.6) + (3 if i % 2 else -3) * s
            seeds += D.circ(fx_, fy_, 3 * s, C["khaki"], D.OW * 0.35)
        eids = [ep]
        for k, (vb, dx) in enumerate([(self.vb1, 70), (self.vb2, 125)]):
            if vb is None:
                continue
            bx = self._bird_x(p, vb, k) if SCN.PLACEMENT_REV >= 4 else p.X + f * dx * s
            b = sc.put(sc.eid("bird"), vb, bx, p.Y + 6 + k * 6, sc.mirror_for(vb, -f), limit=0.3)
            if b and SCN.PLACEMENT_REV >= 10:
                # revision 10: smaller, as flying birds became in v0.10 (pecking birds read as "about
                # knee height ... could be chickens"), keeping the size rule's 3% of the width
                bb_ = b.bbox()
                if (bb_[2] - bb_[0]) * 0.72 >= 0.031 * D.W:
                    b.k *= 0.72
            if b:
                eids.append(b.id)
            elif k == 0 and SCN.PLACEMENT_REV >= 4:
                sc.remove(ep)
                return False
        sc.svg(sc.eid("seeds"), "Seeds", seeds, p.Y + 1, (min(sx, sx + f * 100 * s), sy - 6, max(sx, sx + f * 100 * s), p.Y + 10), "setting")
        self.act(self.p, "feeding the birds", ["feeding the birds", "feeding pigeons", "throwing seeds", "feeding birds", "birds"], "birds", eids)
        return True


def _feed_bird_x(self, p, vb, k):
    """Revision 4: x of the k-th bird, its near edge a fifth of its width inside the feeder's reach."""
    sc = self.sc
    f = p.facing() or 1
    s = sz(p.Y)
    pb = p.bbox()
    b = sc.placed(vb, 0, p.Y + 6 + k * 6, sc.mirror_for(vb, -f))
    bb = b.bbox()
    w = bb[2] - bb[0]
    if f > 0:
        x = pb[2] - 0.2 * w - bb[0]
    else:
        x = pb[0] + 0.2 * w - bb[2]
    return x + f * k * 0.85 * w


FeedBirds._bird_x = _feed_bird_x


class IceCream(T):
    id = "ice_cream"
    settings = ("park", "street", "playground")
    # revision 18: never with the dropped ice cream (a teenager eating hers walked toward the boy who dropped his,
    # "maybe to share it")
    exclusive = ("drop_vs_eat",) if SCN.PLACEMENT_REV >= 18 else ()

    def bind(self):
        sc = self.sc
        self.p = sc.person(None)
        pose = sc.rng.choice(["eat_ice_cream", "walk_ice_cream"])
        # revision 13: walking seen side on (turned three-quarters, the stride crossed the legs in a scissor shape under a
        # skirt: "an awkward or impossible stride")
        self.vp = sc.need(self.p, pose, sc.rng.choice(["happy", "content", "smile"]), 90 if (SCN.PLACEMENT_REV >= 13 and pose == "walk_ice_cream") else 45)

    def place(self):
        sc = self.sc
        ep = sc.eid("icecream")
        if not sc.try_put(ep, self.vp, self.stand_spots(), want_face=sc.rng.choice([1, -1])):
            return False
        self.act(self.p, "eating an ice cream", ["eating ice cream", "ice cream cone", "having an ice cream", "eating a cone"], "ice cream", [ep])
        return True


class PaintFence(T):
    id = "paint_fence"
    settings = ("garden",)
    exclusive = ("fence_paint",)

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.vp = sc.need(self.p, "paint", sc.rng.choice(["focused", "content"]), 90)

    def place(self):
        sc = self.sc
        A = sc.S.anchors["fence_top"]
        ep = sc.eid("painter")
        for x in sc.rng.sample(range(420, 1300, 40), 18):
            p = sc.placed(self.vp, x, 668, sc.mirror_for(self.vp, sc.rng.choice([1, -1])), eid=ep)
            rx, ry = p.anchor("roller")
            # slide so the roller touches the fence (fence front is at depth 615)
            if not (440 < ry < 600) or not sc.fits(p.bbox(), limit=0.15):
                continue
            sc.assets[ep] = p
            self.paint_x = rx
            if SCN.PLACEMENT_REV >= 3:
                stripe = self.painted_boards(rx, ry, p.facing() or 1)
            else:       # revision 1-2: a see-through panel that read as a blue sheet hung on the fence
                stripe = f'<rect x="{rx - 60:.1f}" y="{ry - 40:.1f}" width="60" height="{600 - ry + 40:.1f}" fill="{C["paint"]}" fill-opacity="0.85"/>'
                if p.facing() < 0:
                    stripe = f'<rect x="{rx:.1f}" y="{ry - 40:.1f}" width="60" height="{600 - ry + 40:.1f}" fill="{C["paint"]}" fill-opacity="0.85"/>'
            es = sc.svg(sc.eid("paintstripe"), "Freshly painted boards", stripe, 616, (rx - 60, ry - 40, rx + 60, 600), "scored")
            if SCN.PLACEMENT_REV >= 7:
                # revision 7: a tin of paint at the painter's feet, behind him, or ahead if a post is in the way
                f0, s0 = p.facing() or 1, sz(668)
                for dx in (-58, 64, -88, 92):
                    tin, tbb = D.paint_tin(x + f0 * dx * s0, 680, s0 * 1.3)
                    if sc.air_clear((tbb[0] - 4, tbb[1], tbb[2] + 4, tbb[3])) and sc.fits(tbb, limit=0.05, ignore=(ep,)):
                        sc.svg(sc.eid("painttin"), "Tin of paint", tin, 680, tbb, "prop")
                        break
            self.p_el = (ep, es)
            self.act(self.p, "painting the fence", ["painting the fence", "painting", "paint roller", "painting the wall"], "paint", [ep, es])
            return True
        return False

    @staticmethod
    def painted_boards(rx, ry, f):
        """Two boards just ahead of the roller in solid paint, and the board under the roller painted from
        the roller down: paint on the fence boards themselves, not a panel over the fence, and on the side
        away from the painter's body so it stays in view."""
        x0, step, w = 310, 46, 44                      # the garden fence's boards (settings.build_garden)
        k0 = int((rx - x0) // step)
        out, full = "", []
        for k in (k0 + f, k0 + 2 * f):
            bx = x0 + k * step
            if 310 <= bx <= 1394:
                full.append(bx)
                out += D.poly([(bx, 440), (bx + 22, 428), (bx + 44, 440), (bx + 44, 615), (bx, 615)], C["paint"], D.OW * 0.8)
        cx = x0 + k0 * step
        top = max(ry - 30, 444)
        out += D.rect(cx, top, w, 615 - top, C["paint"], 0, D.OW * 0.8)
        # the rails across the painted boards are painted too
        for y in (480, 565):
            xs = full + ([cx] if top <= y else [])
            if xs:
                lo, hi = min(xs) - 1, max(xs) + w + 1
                out += D.rect(lo, y, hi - lo, 16, "#3557a8", 2, D.OW * 0.8)
        return out


class Run(T):
    id = "run"
    settings = ("park", "street", "playground")
    exclusive = ("drop_vs_run",) if SCN.PLACEMENT_REV >= 18 else ()

    def bind(self):
        sc = self.sc
        self.p = sc.person(("adult", "teen"))
        self.vp = sc.need(self.p, "run", sc.rng.choice(["determined", "happy", "focused"]), 90)

    def place(self):
        sc = self.sc
        ep = sc.eid("runner")
        want = sc.rng.choice([1, -1])
        got = {}

        def accept(p):
            if SCN.PLACEMENT_REV < 17:
                return True
            # revision 17: motion lines streaming back from the runner (without them a runner on the grass read as
            # "striding or jogging", "walking briskly")
            svg, bb = self.speed_lines(p, want)
            if not sc.fits(bb, limit=0.03, ignore=(ep,)) or not sc.air_clear(bb, 6):
                return False
            # (and off the pond: drawn on the water, the lines made a runner on the shore "running in or out of the water";
            # and the runner and the lines clear of the fruit stall: lines on its counter looked like marks on the wood, and a
            # man running from the stall like one who had snatched something from it)
            if not sc.setting_clear(bb, only=("pond", "stall")) or not sc.setting_clear(p.bbox(), only=("stall",)):
                return False
            got["lines"] = (svg, bb)
            return True
        if not sc.try_put(ep, self.vp, self.stand_spots(), want_face=want, accept=accept):
            return False
        if "lines" in got:
            svg, bb = got["lines"]
            sc.airzones.append(bb)      # and nobody placed later stands in them
            sc.svg(sc.eid("speedlines"), "Motion lines behind the runner", svg, sc.assets[ep].Y + 1, bb, "setting")
        self.act(self.p, "running", ["running", "jogging", "out for a run", "exercising"], "running", [ep])
        return True

    @staticmethod
    def speed_lines(p, want):
        """Three short lines trailing from the runner's back at shoulder, waist and hip height, each starting a few
        pixels behind the outline at its height."""
        from . import compose as K
        import numpy as np
        b, s = p.bbox(), sz(p.Y)
        h = b[3] - b[1]
        m = K.asset_mask(p, False)
        svg, xs, ys = "", [], []
        for fy, L, off in ((0.27, 40, 7), (0.40, 54, 9), (0.53, 36, 7)):
            y = b[1] + fy * h
            row = m[min(m.shape[0] - 1, int(y * K.MASK_SCALE))]
            cols = np.nonzero(row)[0]
            if cols.size:
                back = (cols.min() if want > 0 else cols.max()) / K.MASK_SCALE
            else:
                back = b[0] if want > 0 else b[2]
            x0 = back - want * off * s
            x1 = x0 - want * L * s
            svg += f'<path d="M {D.P(x0, y)} L {D.P(x1, y)}" fill="none" stroke="{D.OUT}" stroke-width="{2.6 * s:.1f}" stroke-linecap="round" stroke-opacity="0.75"/>'
            xs += [x0, x1]
            ys.append(y)
        return svg, (min(xs) - 3, min(ys) - 4, max(xs) + 3, max(ys) + 4)


class Wave(T):
    id = "wave"

    def bind(self):
        sc = self.sc
        self.p = sc.person(None)
        # revision 12: a child waves facing us, the arm up and out to the side clear of the head (turned three-quarters,
        # a child's raised hand sat by the head or the bun of hair: "waving or listening", "holding a phone to her ear")
        yaw = 0 if (SCN.PLACEMENT_REV >= 12 and sc.lib.kind(self.p) == "child") else 45
        self.vp = sc.need(self.p, "wave", sc.rng.choice(["smile", "happy"]), yaw)

    def place(self):
        sc = self.sc
        ep = sc.eid("waver")
        if SCN.PLACEMENT_REV >= 6:
            return self.place_at_someone(ep)
        if not sc.try_put(ep, self.vp, self.stand_spots(), want_face=sc.rng.choice([1, -1])):
            return False
        self.act(self.p, "waving", ["waving", "waving hello", "saying hello", "waving goodbye"], "waving", [ep])
        return True

    def place_at_someone(self, ep):
        """Revision 6: wave toward another person in the picture, with two short motion arcs beside the
        raised hand (one raised arm on its own read as leaning, waving or scratching the head)."""
        sc = self.sc
        others = [q for k, q in sc.assets.items() if q.family.startswith("person.")]
        rev13 = SCN.PLACEMENT_REV >= 13
        if rev13:
            # revision 13: wave only at someone simply going about their day (the person of a plain event), never at
            # someone in the middle of a mishap or a puzzle (an older man waving toward a woman whose hose had stopped,
            # a goat on it, read as "scratching his head ... looking puzzled": the mishap he faced made the raised
            # hand a reaction to it)
            tpl = {t.ev: t for t in sc.templates if t.ev}
            calm = {k for k in sc.assets if tpl.get(sc.ev_of.get(k)) is not None and tpl[sc.ev_of[k]].kind == "event"
                    and tpl[sc.ev_of[k]].id != self.id}
            others = [q for k, q in sc.assets.items() if q.family.startswith("person.") and k in calm]
            if not others:
                return False
            odd = [b for k, b, _ in sc.scored_boxes(ignore=(ep,)) if tpl.get(sc.ev_of.get(k)) is not None and tpl[sc.ev_of[k]].kind != "event"]
        for X, Y in self.stand_spots(n=160 if rev13 else 120):
            if SCN.PLACEMENT_REV >= 16 and Y < 650:
                # revision 16: no waver at the far back, where the waving hand is a few pixels across (a small girl far
                # back on a park path, her hand on the hedge line, was "holding a string ... or just a wave")
                continue
            if others:
                tgt = min(others, key=lambda q: abs(q.X - X) + 3 * abs(q.Y - Y))
                if not (180 <= abs(tgt.X - X) <= 700 and abs(tgt.Y - Y) <= 160):
                    continue
                want = 1 if tgt.X > X else -1
                if rev13:
                    # and nothing of a mishap or a puzzle between the waver and that person, or right behind the waver
                    s_ = sz(Y)
                    tb = tgt.bbox()
                    lo, hi = (X - 70 * s_, tb[2]) if tgt.X > X else (tb[0], X + 70 * s_)
                    corridor = (lo, min(tb[1], Y - 190 * s_), hi, max(tb[3], Y) + 10 * s_)
                    if any(sc.overlap(corridor, b) > 0 for b in odd):
                        continue
            else:
                want = sc.rng.choice([1, -1])
            p = sc.placed(self.vp, X, Y, sc.mirror_for(self.vp, want), eid=ep)
            if not sc.fits(p.bbox()):
                continue
            hands = [p.anchor(k) for k in ("hand_R_grip", "hand_L_grip") if p.has_anchor(k)]
            if not hands:
                continue
            hx, hy = min(hands, key=lambda h: h[1])       # the raised hand
            s = sz(Y)
            side = 1 if hx >= p.X else -1
            arcs = ""
            if SCN.PLACEMENT_REV >= 12:
                # revision 12: one arc on each side of the hand, as it swings to and fro (two arcs on one side of a hand
                # by the head read as sound: "waving or listening", "snapping her fingers or calling out")
                # (short arcs, well apart: two long ones closed round the hand into "a faint thin circle or ring", "a small
                # green round object")
                for sd in (1, -1):
                    r = 24 * s
                    c_, s_ = math.cos(math.radians(32)), math.sin(math.radians(32))
                    arcs += f'<path d="M {D.P(hx + sd * r * c_, hy - r * s_)} A {r:.1f} {r:.1f} 0 0 {1 if sd > 0 else 0} {D.P(hx + sd * r * c_, hy + r * s_)}" fill="none" stroke="{D.OUT}" stroke-width="{2.4 * s:.1f}" stroke-linecap="round" stroke-opacity="0.75"/>'
                abb = (hx - 27 * s, hy - 15 * s, hx + 27 * s, hy + 15 * s)
            else:
                for k in range(2):
                    r = (16 + 9 * k) * s
                    cxa = hx + side * 4 * s
                    arcs += f'<path d="M {D.P(cxa + side * r * 0.5, hy - r * 0.87)} A {r:.1f} {r:.1f} 0 0 {1 if side > 0 else 0} {D.P(cxa + side * r * 0.5, hy + r * 0.87)}" fill="none" stroke="{D.OUT}" stroke-width="{2.4 * s:.1f}" stroke-linecap="round" stroke-opacity="0.75"/>'
                abb = (hx - 4 * s if side > 0 else hx - 34 * s, hy - 24 * s, hx + 34 * s if side > 0 else hx + 4 * s, hy + 24 * s)
            if not sc.fits(abb, limit=0.03, ignore=(ep,)) or not sc.air_clear(abb, 6):
                continue
            if SCN.PLACEMENT_REV >= 16 and not sc.outline_clear((hx - 36 * s, hy - 30 * s, hx + 36 * s, hy + 30 * s)):
                # revision 16: the hand and its motion arcs against plain ground, wall or sky, never on a line of the
                # backdrop (the hedge line running from a raised hand read as a string she was holding)
                continue
            if SCN.PLACEMENT_REV >= 9:
                # revision 9: nothing of another event in the air above the raised hand, and no kite string near
                # it (a woman waving under the kite caught in the tree seemed to reach for it)
                col = (hx - 90 * s, 0, hx + 90 * s, hy)
                if any(sc.overlap(col, b) > 0 for k, b, _ in sc.scored_boxes(ignore=(ep,))):
                    continue
                # nor a tree over it (a woman waving under the tree with the fish in it)
                if not sc.setting_clear(col, only=("tree", "tree_small")):
                    continue
                if any(math.hypot(ax + (bx - ax) * t / 10 - hx, ay + (by - ay) * t / 10 - hy) < 60 * s
                       for (ax, ay), (bx, by) in getattr(sc, "strings", []) for t in range(11)):
                    continue
            sc.assets[ep] = p
            if SCN.PLACEMENT_REV >= 9:
                # revision 9: and no one placed later stands against the waver (a catcher reaching out right in
                # front of a waving man made the two read as one group)
                pb = p.bbox()
                sc.airzones.append((min(pb[0], abb[0]) - 40 * s, min(pb[1], abb[1]), max(pb[2], abb[2]) + 40 * s, pb[3]))
            sc.svg(sc.eid("wavelines"), "Motion lines by the waving hand", arcs, Y + 1, abb, "setting")
            self.act(self.p, "waving", ["waving", "waving hello", "saying hello", "waving goodbye", "waving at someone"], "waving", [ep])
            return True
        return False


# ---------------------------------------------------------------- animal events
class AnimalEvent(T):
    kinds, pose, exprs, yaw = ("dog",), "sleep", ("sleepy",), 90
    text = ("A dog is sleeping", ["dog sleeping", "dog lying down", "sleeping dog", "dog resting", "dog"], "dog")

    def bind(self):
        sc = self.sc
        # (revision 11: a sleeping cat is the orange one, whose closed eyes show; on the black cat curled small the
        # face was a dark blob)
        self.a = sc.animal(list(self.kinds), prefer=("animal.cat_02",) if (SCN.PLACEMENT_REV >= 11 and self.id == "cat_sleeping") else ())
        pose, yaw = self.pose, self.yaw
        if SCN.PLACEMENT_REV >= 11 and self.id in ("dog_sleeping", "cat_sleeping"):
            # revision 11: curled up asleep, facing out, the closed eyes and the head on the paws in view (lying
            # stretched out flat, seen from the side, a sleeping cat or dog "could also be read as collapsed")
            # (a cat curled face-on was too small to see: cats curl up with a short round trunk, turned 45 degrees)
            pose, yaw = ("sleep_tuck", 45) if self.id == "cat_sleeping" else ("sleep_ball", 0)
        self.va = sc.need(self.a, pose, sc.rng.choice(self.exprs), yaw)

    def spot(self):
        return self.stand_spots()

    def place(self):
        sc = self.sc
        ea = sc.eid(self.id)
        sleeper = SCN.PLACEMENT_REV >= 11 and self.id in ("dog_sleeping", "cat_sleeping")

        def room(p):
            """Revision 11: a curled-up sleeper lies on its own, with open ground around it (a sleeping cat right at
            the foot of a parked bicycle read as "the bike might topple onto the cat"; another lay across a hose)."""
            m = 45 * sz(p.Y)
            b = p.bbox()
            box = (b[0] - m, b[1] - m, b[2] + m, b[3] + m * 0.6)
            if any(min(box[2], q.bbox()[2]) > max(box[0], q.bbox()[0]) and min(box[3], q.bbox()[3]) > max(box[1], q.bbox()[1]) for q in sc.assets.values()):
                return False
            if any(e.get("bbox") and e["role"] != "background" and sc.overlap(box, e["bbox"]) > 0 for e in sc.svgs.values()):
                return False
            return sc.setting_clear(box, only=SLEEP_STRUCT11)
        p = sc.try_put(ea, self.va, self.spot(), want_face=sc.rng.choice([1, -1]), limit=0.15, accept=room if sleeper else None)
        if not p:
            return False
        if sleeper:
            m = 45 * sz(p.Y)
            b = p.bbox()
            sc.groundzones.append((b[0] - m, b[1] - m, b[2] + m, b[3] + m * 0.6))
        t, acc, key = self.text
        self.ent(t.replace("dog", sc.name(self.a)) if "dog" in t else t, acc, key, [ea], animate=True)
        self.sc.items[-1]["type"] = "action"
        return True


SLEEP_STRUCT11 = ("clothesline", "laundry", "swing", "swing_seat", "feeder", "lamp", "tree", "tree_small", "stall", "bench", "slide", "seesaw",
                  "bicycle", "hose_reel", "sandbox", "blanket", "flowers", "pond")


class DogSleeping(AnimalEvent):
    id = "dog_sleeping"
    # v0.15 (revision 13): nor a sleeping dog (as the cat)
    settings = ("garden", "park", "playground") if SCN.PLACEMENT_REV >= 13 else ALL

    def spot(self):
        # revision 11: curled up small, nearer the front so it is drawn larger, like the sleeping cat (curled
        # far back by the pond, a puppy "looks asleep or sniffing")
        if SCN.PLACEMENT_REV >= 11:
            return self.stand_spots(y_range=(self.sc.S.horizon + 230, 960))
        return self.stand_spots()


class CatSleeping(AnimalEvent):
    id = "cat_sleeping"
    # v0.15 (revision 13): no sleeper on the open pavement of the street (drawn near the front so it reads, it lay "out in
    # the middle of a busy pavement"; by the shopfronts it is too small to read)
    settings = ("garden", "park", "playground") if SCN.PLACEMENT_REV >= 13 else ALL
    kinds, pose, exprs, yaw = ("cat",), "sleep", ("sleepy",), 45
    text = ("A cat is sleeping", ["cat sleeping", "cat lying down", "sleeping cat", "cat napping", "cat curled up", "cat"], "cat")

    def bind(self):
        # revision 8: curled up with the tail round the body, nearer the front so it is drawn larger (a
        # small cat lying stretched out in a busy park read as "crouched low")
        if SCN.PLACEMENT_REV >= 8:
            self.pose, self.yaw = "sleep_curl", 90
        super().bind()

    def spot(self):
        if SCN.PLACEMENT_REV >= 8:
            # (revision 11: and up from the bottom edge, which cut the curled-up sleeper's shadow)
            return self.stand_spots(y_range=(self.sc.S.horizon + 230, 960 if SCN.PLACEMENT_REV >= 11 else 985))
        return self.stand_spots()


class GoatGrazing(AnimalEvent):
    id = "goat_grazing"
    settings = ("garden", "park")
    kinds, pose, exprs, yaw = ("goat",), "sniff", ("neutral", "happy"), 90
    text = ("A goat is eating grass", ["goat eating", "goat eating grass", "goat grazing", "goat"], "goat")

    def bind(self):
        # revision 6: muzzle down in the grass with a tuft in its mouth (sniffing read as "about to butt")
        if SCN.PLACEMENT_REV >= 6:
            self.pose = "graze"
        super().bind()

    def place(self):
        if not super().place():
            return False
        if SCN.PLACEMENT_REV >= 6:
            sc = self.sc
            ea = [k for k in sc.assets if k.startswith(self.id)][-1]
            a = sc.assets[ea]
            mx, my = a.anchor("mouth")
            s = sz(a.Y)
            f = 1 if mx > a.X else -1
            blades = ""
            for k, (dx, h, lean) in enumerate(((-9, 22, -5), (-4, 28, -2), (1, 24, 3), (6, 30, 6), (11, 20, 8), (-13, 16, -8))):
                bx_, by_ = mx + dx * s, a.Y + 2 * s
                blades += f'<path d="M {D.P(bx_ - 2.2 * s, by_)} Q {D.P(bx_ + lean * 0.5 * s, by_ - h * 0.6 * s)} {D.P(bx_ + lean * s, by_ - h * s)} Q {D.P(bx_ + lean * 0.4 * s + 1.5 * s, by_ - h * 0.5 * s)} {D.P(bx_ + 2.2 * s, by_)} Z" fill="{C["grass_dark"]}" stroke="{D.OUT}" stroke-width="{D.OW * 0.35:.1f}"/>'
            # a few blades hanging from the mouth
            for k, (ang, ln) in enumerate(((-30, 16), (-5, 20), (20, 15))):
                r = math.radians(ang)
                ex, ey = mx + f * math.sin(r) * ln * s, my + math.cos(r) * ln * s
                blades += f'<path d="M {D.P(mx, my)} L {D.P(ex, ey)}" stroke="{C["grass_dark"]}" stroke-width="{3.2 * s:.1f}" stroke-linecap="round"/>'
            sc.svg(sc.eid("grasstuft"), "Grass at the goat's mouth", blades, a.Y + 2, (mx - 18 * s, min(my, a.Y - 32 * s), mx + 20 * s, a.Y + 4 * s), "setting")
        return True

    def spot(self):
        out = self.stand_spots()
        if SCN.PLACEMENT_REV >= 4:      # grazing on grass, not on the path
            out = [(X, Y) for X, Y in out if not self.sc.on_element("path", X, Y) and not self.sc.on_element("path", X + 50 * sz(Y), Y)
                   and not self.sc.on_element("path", X - 50 * sz(Y), Y)]
        return out


class DogPlaying(AnimalEvent):
    id = "dog_playing"
    settings = ("park", "garden", "playground")
    kinds, pose, exprs, yaw = ("dog",), "play_bow", ("happy",), 90
    text = ("A dog is playing", ["dog playing", "playful dog", "dog wants to play", "dog"], "dog")

    def place(self):
        if SCN.PLACEMENT_REV < 9:
            return super().place()
        # revision 9: the play bow faces a person nearby or open ground, never an object (a bow facing a
        # wheelbarrow read as sniffing it)
        sc = self.sc
        ea = sc.eid(self.id)
        people = [q for q in sc.assets.values() if q.family.startswith("person.")]
        for X, Y in self.spot():
            near = [q for q in people if 120 <= abs(q.X - X) <= 450 and abs(q.Y - Y) <= 120]
            # (with nobody near, toward the middle of the picture first: a bow facing the frame edge faced nothing)
            wants = [1 if near[0].X > X else -1] if near else ([1, -1] if X < D.W / 2 else [-1, 1])
            for want in wants:
                d = sc.placed(self.va, X, Y, sc.mirror_for(self.va, want), eid=ea)
                b = d.bbox()
                if not sc.fits(b, limit=0.15) or not sc.S.walkable(X, Y):
                    continue
                s = sz(Y)
                front = (b[2], b[1], b[2] + 130 * s, b[3]) if want > 0 else (b[0] - 130 * s, b[1], b[0], b[3])
                if front[0] < 30 or front[2] > D.W - 30:
                    continue
                if any(sc.overlap(front, e["bbox"]) > 0 for e in sc.svgs.values() if e["role"] in ("scored", "filler") and e.get("bbox")) or \
                        any(sc.overlap(front, q.bbox()) > 0 for q in sc.assets.values() if not q.family.startswith("person.")) or \
                        not sc.setting_clear(front, skip=sc.SKY_SKIP + ("fence", "hills", "tree_line", "buildings", "house", "clouds_white", "clouds_dark", "sun")):
                    continue
                # revision 10: the paws and the ground ahead off the sandbox and the picnic blanket (ground the
                # clearance check lets people stand by), and the feet off the pond's rim (a dog bowing with
                # its front half over the sandbox's frame, the ball in the sand)
                if SCN.PLACEMENT_REV >= 10:
                    u = (min(b[0], front[0]) - 10, b[1], max(b[2], front[2]) + 10, b[3] + 26)
                    if not sc.setting_clear(u, only=("sandbox", "blanket")) or not sc.clear_of_pond_edge(b):
                        continue
                sc.assets[ea] = d
                sc.airzones.append(front)       # kept clear of later placements and fillers too
                if SCN.PLACEMENT_REV >= 10:
                    sc.groundzones.append(front)    # revision 10: drawn objects too (a later wheelbarrow)
                eids = [ea]
                if SCN.PLACEMENT_REV >= 10:
                    # revision 10: a toy ball on the ground between the front paws, and two wag arcs by the
                    # raised tail (with nothing to play with, the bow read as "a stretch or play-bow")
                    pf = [d.anchor(k) for k in ("paw_FL", "paw_FR") if d.has_anchor(k)]
                    px = (max if want > 0 else min)(q[0] for q in pf) if pf else (b[2] if want > 0 else b[0])
                    r_ = 13 * s
                    tx, ty = px + want * (r_ + 4 * s), Y - r_ + 2 * s
                    toy = D.circ(tx, ty, r_, "#c9de3c")   # a tennis-ball green, unlike every other ball
                    toy += f'<path d="M {D.P(tx - r_ * 0.75, ty - r_ * 0.5)} Q {D.P(tx, ty + r_ * 0.15)} {D.P(tx + r_ * 0.75, ty - r_ * 0.5)}" fill="none" stroke="{C["white"]}" stroke-width="{2.6 * s:.1f}"/>'
                    rear = b[0] if want > 0 else b[2]
                    for k_ in range(2):
                        R_ = (14 + 9 * k_) * s
                        cx_, cy_ = rear + want * 8 * s, b[1] + 22 * s
                        toy += f'<path d="M {D.P(cx_ - want * R_ * 0.9, cy_ - R_ * 0.45)} Q {D.P(cx_ - want * R_ * 1.15, cy_ + R_ * 0.1)} {D.P(cx_ - want * R_ * 0.9, cy_ + R_ * 0.6)}" fill="none" stroke="{D.OUT}" stroke-width="{2.4 * s:.1f}" stroke-linecap="round" stroke-opacity="0.75"/>'
                    sc.svg(sc.eid("toyball"), "Toy ball by the dog", toy, Y + 1, (tx - r_, ty - r_, tx + r_, ty + r_), "setting")
                t, acc, key = self.text
                self.ent(t.replace("dog", sc.name(self.a)), acc, key, eids, animate=True)
                self.sc.items[-1]["type"] = "action"
                return True
        return False


class BirdPerched(T):
    id = "bird_perched"

    def bind(self):
        sc = self.sc
        self.b = sc.animal(["songbird"])
        self.vb = sc.need(self.b, sc.rng.choice(["perch", "sing"]), sc.rng.choice(["neutral", "sing"]), 90)

    def perches(self):
        S = self.sc.S
        out = []
        if "fence_top" in S.anchors:
            A = S.anchors["fence_top"]
            for x in range(A["x0"], A["x1"], 60):
                out.append((x, A["y"], A["depth"], "the fence", "fence"))
        if "lamp_top" in S.anchors:
            x, y, d = S.anchors["lamp_top"]
            out.append((x, y, d + 1, "the lamp post", "lamp"))
        if "tree" in S.anchors and "branch" in S.anchors["tree"]:
            x, y = S.anchors["tree"]["branch"]
            out.append((x, y, S.anchors["tree"]["bbox"][3] + 1, "a branch", "branch"))
        return out

    def place(self):
        sc = self.sc
        per = self.perches()
        sc.rng.shuffle(per)
        eb = sc.eid("bird")
        # revision 11: not on the tree's branch when something is caught up in that tree or someone points up (a red
        # bird on the branch beside a ball stuck in the crown, which a child pointed up at)
        busy = SCN.PLACEMENT_REV >= 11 and any("tree_canopy" in getattr(t, "exclusive", ()) for t in sc.templates if t is not self)
        for x, y, d, where, key in per:
            if busy and key == "branch":
                continue
            # revision 9: not near a cat (a perched bird with a cat walking the fence toward it read as stalked)
            if SCN.PLACEMENT_REV >= 9 and any(q.family.startswith("animal.cat") and abs(q.X - x) < 380 for q in sc.assets.values()):
                continue
            p = sc.placed(self.vb, x, y, sc.rng.random() < 0.5, depth_y=d, eid=eb)
            # revision 14: not on the stretch of fence behind the clothesline, the bird table or the swing (a bird on the
            # fence just under the line read as "perched on the line"), as the cats on the fence are kept
            if SCN.PLACEMENT_REV >= 14 and key == "fence" and not sc.clear_of_setting(p.bbox(), ("clothesline", "laundry", "feeder", "swing"), 30):
                continue
            # revision 15: and on the playground's railing, clear of the slide, the swing frame, the seesaw and the tree (a
            # bird on the railing where the slide's platform stands in front of it read as "on top of the slide")
            if SCN.PLACEMENT_REV >= 15 and key == "fence" and not sc.clear_of_setting(p.bbox(), ("slide", "swing", "swing_seat", "seesaw", "tree", "tree_small"), 30):
                continue
            if sc.fits(p.bbox(), limit=0.05):
                sc.assets[eb] = p
                self.where = where
                if SCN.PLACEMENT_REV >= 13 and key == "branch":
                    # revision 13: the end of the branch shows under the bird's feet, out from the crown (the limb runs up
                    # behind the leaves, and the bird seemed to sit on them: "in the leafy canopy with no visible branch")
                    T_ = sc.S.anchors["tree"]
                    side = 1 if x >= T_["canopy"][0] else -1
                    ws = sz(d) * 0.9
                    pb = p.bbox()
                    fy = pb[3] - 1
                    x0, x1 = x - side * 52 * ws, x + side * 30 * ws
                    twig = D.stroke(f"M {D.P(x0, fy + 8 * ws)} Q {D.P((x0 + x1) / 2, fy + 1 * ws)} {D.P(x1, fy - 3 * ws)}", C["wood"], 8 * ws)
                    sc.svg(sc.eid("perch"), "End of the branch under the bird", twig, d - 0.2,
                           (min(x0, x1) - 6, fy - 16 * ws, max(x0, x1) + 6, fy + 12 * ws), "setting")
                    # (the branch comes out from among the leaves: a cluster of leaves over its inner end, and a few more
                    # over the crown, as over the ball and the kite caught in a tree; drawn alone on the leaves, the branch
                    # "floats inside the canopy ... pasted onto the green leaf mass")
                    cx_, cy_ = x0 + side * 4 * ws, fy + 6 * ws
                    r_ = 15 * ws
                    over = [[(cx_, cy_, r_), (cx_ - side * 0.9 * r_, cy_ + 0.4 * r_, 0.8 * r_), (cx_ + side * 0.2 * r_, cy_ - 0.8 * r_, 0.7 * r_)]]
                    tex = _crown_texture(T_, (min(x0, x1) - 20, fy - 40 * ws, max(x0, x1) + 20, fy + 20 * ws), 1.0)
                    sc.svg(sc.eid("crownleaves"), "Leaves on the tree", _leaf_clusters(T_, (tex or [])[:3] + over, "pb%d" % abs(int(x))),
                           d - 0.1, T_["bbox"], "background")
                it = self.ent(f"A bird is sitting on {where}", ["bird", "bird on the " + key, "little bird", "bird sitting", "bird singing"], "bird", [eb], animate=True)
                it["type"] = "action"
                return True
        return False


class DucksSwimming(T):
    id = "ducks_swimming"
    settings = ("park",)

    def bind(self):
        sc = self.sc
        self.d = sc.animal(["duck"])
        self.vd = sc.need(self.d, "swim", "neutral", 90)

    def place(self):
        sc = self.sc
        A = sc.S.anchors["pond"]
        slots = list(A["swim"])
        sc.rng.shuffle(slots)
        ed = sc.eid("duck")
        for x, y in slots:
            p = sc.placed(self.vd, x, y, sc.rng.random() < 0.5, eid=ed)
            if sc.fits(p.bbox(), limit=0.05):
                sc.assets[ed] = p
                it = self.ent("A duck is swimming in the pond", ["duck", "duck swimming", "ducks", "duck in the pond", "duck in the water"], "duck", [ed], animate=True)
                it["type"] = "action"
                return True
        return False


class BirdsFlying(T):
    id = "birds_flying"
    # v0.12 (revision 10): never with the storm pointer, who could be pointing at the birds
    exclusive = ("sky_birds",) if SCN.PLACEMENT_REV >= 10 else ()

    def bind(self):
        sc = self.sc
        self.b = sc.animal(["songbird"])
        self.vb = sc.need(self.b, "fly", "neutral", 90)

    def place(self):
        sc = self.sc
        eb = sc.eid("flyingbird")
        rev8 = SCN.PLACEMENT_REV >= 8
        for _ in range(80 if rev8 else 40):
            if rev8:
                # revision 8: smaller (flying birds were larger than life), in open sky clear of rooflines,
                # awnings, trees, clouds and kites (a bird crossing a roof edge read as perched on it)
                x, y = sc.rng.uniform(120, 1480), sc.rng.uniform(60, 300)
                p = sc.placed(self.vb, x, y, sc.rng.random() < 0.5, depth_y=900, eid=eb)
            else:
                x, y = sc.rng.uniform(150, 1450), sc.rng.uniform(130, 300)      # high in the open sky
                p = sc.placed(self.vb, x, y, sc.rng.random() < 0.5, depth_y=1060, eid=eb)
            p.z = -50          # drawn in the sky layer, in front of clouds and behind everything on the ground
            sun = next((e["bbox"] for e in sc.S.elements if e["id"] == "sun"), None)
            if sun and sc.overlap(p.bbox(), sun) > 0:
                continue
            if rev8:
                b = p.bbox()
                g = (b[0] - 24, b[1] - 24, b[2] + 24, b[3] + 24)
                if not sc.setting_clear(g) or any(sc.overlap(g, q) > 0 for _, q, _ in sc.scored_boxes()):
                    continue
            if sc.fits(p.bbox(), limit=0.02):
                sc.assets[eb] = p
                it = self.ent("A bird is flying", ["bird flying", "bird in the sky", "bird", "flying bird"], "bird", [eb], animate=True)
                it["type"] = "action"
                return True
        return False


class CatOnFence(T):
    id = "cat_on_fence"
    settings = ("garden",)
    # v0.16 (revision 14): never with a stalking cat (a second cat walking the fence behind the stalking one made the
    # stalker "just walking along" too)
    exclusive = ("second_cat",) if SCN.PLACEMENT_REV >= 14 else ()

    def bind(self):
        sc = self.sc
        self.c = sc.animal(["cat"])
        self.vc = sc.need(self.c, "walk", sc.rng.choice(["neutral", "happy"]), 90)

    def place(self):
        sc = self.sc
        A = sc.S.anchors["fence_top"]
        ec = sc.eid("fencecat")
        for x in sc.rng.sample(range(A["x0"] + 40, A["x1"] - 40, 30), 20):
            p = sc.placed(self.vc, x, A["y"], sc.rng.random() < 0.5, depth_y=A["depth"], eid=ec)
            # revision 8: clear of the clothesline (a cat on the fence behind it read as walking the line),
            # the bird table's post and the swing frame
            if SCN.PLACEMENT_REV >= 8 and not sc.clear_of_setting(p.bbox(), ("clothesline", "laundry", "feeder", "swing"), 30):
                continue
            # revision 9: no bird near it (a cat walking the fence toward a bird perched on it read as stalking it)
            if SCN.PLACEMENT_REV >= 9 and any("bird" in q.family and abs(q.X - x) < 380 for q in sc.assets.values()):
                continue
            if sc.fits(p.bbox(), limit=0.05):
                sc.assets[ec] = p
                it = self.ent("A cat is walking along the fence", ["cat on the fence", "cat walking", "cat", "cat on top of the fence"], "cat", [ec], animate=True)
                it["type"] = "action"
                return True
        return False


# ---------------------------------------------------------------- v0.5 events (playground and more)
class SeesawPlay(T):
    id = "seesaw"
    settings = PG
    needs = {"playground": {"seesaw"}}
    uses = ("seesaw",)
    # the playground seesaw stands in front of the bench: a dog begging at the bench end had nowhere to sit
    exclusive = ("seesaw", "bench_front")
    content = 2

    def bind(self):
        sc = self.sc
        pa = pb = "sit"
        if SCN.PLACEMENT_REV >= 8:
            # revision 8: two children of a size where they are free; a teenager with a child sits on the
            # low end with the feet on the ground, the child up high holding on (a teenager on a seesaw
            # barely tipped, the end off the ground, looked wrong)
            picked = []
            for _ in range(2):
                try:
                    picked.append(sc.person(KIDS))
                except PlacementError:
                    picked.append(sc.person(YOUNG))
            self.a, self.b = picked
            wa, wb = (sc.lib.kind(f) for f in (self.a, self.b))
            if wa != wb:
                pa, pb = ("seesaw_low", "seesaw_stuck") if wa == "teen" else ("seesaw_stuck", "seesaw_low")
        else:
            self.a, self.b = sc.person(YOUNG), sc.person(YOUNG)
        self.va = sc.need(self.a, pa, sc.rng.choice(["happy", "laughing", "smile"]), 90)
        self.vb = sc.need(self.b, pb, sc.rng.choice(["happy", "laughing", "smile"]), 90)

    def ride(self, tilt, ea, eb, va, vb):
        """Redraw the seesaw at `tilt` and sit the two riders on its ends, facing each other."""
        sc = self.sc
        A = sc.S.anchors["seesaw"]
        s = sz(A["depth"])
        svg, info = D.seesaw(A["cx"], A["base_y"], s, tilt=tilt)
        placed = []
        for eid, v, end, want in ((ea, va, "left", 1), (eb, vb, "right", -1)):
            p = sc.placed(v, 0, 0, sc.mirror_for(v, want), depth_y=A["depth"] + 2, eid=eid)
            seat = info["seats"][end]
            p.move_anchor_to("seat", (seat[0], seat[1] - D.RIDE24["seesaw"] * s) if SCN.PLACEMENT_REV >= 22 else seat)
            if not sc.fits(p.bbox(), limit=0.15):
                return None
            if SCN.PLACEMENT_REV >= 7 and p.has_anchor("foot_L") and p.has_anchor("foot_R"):
                # revision 7: the low rider's shadow under the feet, not under the seat point
                p.shadow_x = (p.anchor("foot_L")[0] + p.anchor("foot_R")[0]) / 2
            placed.append(p)
        if SCN.PLACEMENT_REV >= 11:
            # revision 11: nobody else stands at the seesaw, now or later (a girl beside the raised end "could
            # look as if standing on the plank")
            sb = info["bbox"]
            room = (sb[0] - 45 * s, sb[1] - 30 * s, sb[2] + 45 * s, sb[3] + 15 * s)
            if any(sc.overlap(room, q.bbox()) > 0 for k_, q in sc.assets.items() if k_ not in (ea, eb)):
                return None
        for e in sc.S.elements:
            if e["id"] == "seesaw":
                e["svg"], e["bbox"] = svg, info["bbox"]
        sc.assets[ea], sc.assets[eb] = placed
        sc.legib_ok |= {("seesaw", ea), ("seesaw", eb)}
        if SCN.PLACEMENT_REV >= 11:
            sc.airzones.append(room)
        return placed

    def place(self):
        sc = self.sc
        ea, eb = sc.eid("seesawkid"), sc.eid("seesawkid")
        tilt = sc.rng.choice([-7, -4, 4, 7])
        if SCN.PLACEMENT_REV >= 6:
            # revision 6: the heavier rider's end is the low one (a teenager up in the air with a small
            # child down on the ground read as the wrong way round); two children of a size may tip either way
            wa, wb = (sc.lib.kind(f) for f in (self.a, self.b))
            order = {"child": 0, "teen": 1, "adult": 2, "older_adult": 2}
            if order.get(wa, 1) != order.get(wb, 1):
                tilt = abs(tilt) if order.get(wa, 1) > order.get(wb, 1) else -abs(tilt)
                if SCN.PLACEMENT_REV >= 8:
                    tilt = math.copysign(math.degrees(math.asin(82 / 212)), tilt)      # the low end on the ground
            elif SCN.PLACEMENT_REV >= 9:
                # revision 9: two children of a kind: the bigger one's end is the low one (the bigger boy up
                # and the smaller girl down "looks off")
                ha = sc.placed(self.va, 0, 800).bbox(); hb = sc.placed(self.vb, 0, 800).bbox()
                tilt = abs(tilt) if (ha[3] - ha[1]) >= (hb[3] - hb[1]) else -abs(tilt)
        if not self.ride(tilt, ea, eb, self.va, self.vb):
            return False
        self.act(self.a, "playing on the seesaw", ["playing on the seesaw", "on the seesaw", "seesawing", "teeter-totter"], "seesaw", [ea])
        self.act(self.b, "playing on the seesaw", ["playing on the seesaw", "on the seesaw", "seesawing", "teeter-totter"], "seesaw", [eb])
        return True


class SandboxPlay(T):
    id = "sandbox"
    settings = PG
    needs = {"playground": {"sandbox"}}
    uses = ("sandbox",)
    exclusive = ("sandbox",)

    def bind(self):
        sc = self.sc
        self.p = sc.person(KIDS)
        # revision 6: kneeling at the castle, patting it with a spade (sitting beside it read as resting)
        pose = "sand_build" if SCN.PLACEMENT_REV >= 6 else "sit_ground"
        self.vp = sc.need(self.p, pose, sc.rng.choice(["happy", "smile", "focused"]), 45)

    def place(self):
        sc = self.sc
        A = sc.S.anchors["sandbox"]
        ep = sc.eid("sandkid")
        inner = A["inner"]
        if SCN.PLACEMENT_REV >= 6:
            return self.place_building(A, ep, inner)
        y0, y1 = inner[0][1] + 30, inner[2][1] - 4
        for _ in range(40):
            Y = sc.rng.uniform(y0, y1)
            t = (Y - inner[0][1]) / max(1, inner[3][1] - inner[0][1])
            xl = inner[0][0] + (inner[3][0] - inner[0][0]) * t + 40
            xr = inner[1][0] + (inner[2][0] - inner[1][0]) * t - 40
            X = sc.rng.uniform(xl, xr)
            p = sc.placed(self.vp, X, Y, sc.rng.random() < 0.5, eid=ep)
            if not sc.fits(p.bbox(), limit=0.15):
                continue
            s = sz(Y)
            f = p.facing() or 1
            cx_ = X + f * 120 * s
            if not (xl - 30 <= cx_ <= xr + 30):
                continue
            castle, cbb = D.sandcastle(cx_, Y + 6 * s, s, heaped=SCN.PLACEMENT_REV >= 24)
            pail, pbb = D.sand_pail(X - f * 80 * s, Y + 10 * s, s * 0.9)
            sc.assets[ep] = p
            ec = sc.svg(sc.eid("sandcastle"), "Sandcastle", castle + pail, Y + 6, (min(cbb[0], pbb[0]), cbb[1], max(cbb[2], pbb[2]), Y + 12 * s), "scored")
            self.act(self.p, "building a sandcastle in the sandbox", ["building a sandcastle", "playing in the sand", "playing in the sandbox", "sandcastle"], "sandcastle", [ep, ec])
            return True
        return False


def _sandbox_place_building(self, A, ep, inner):
    """Revision 6: the child kneels in the sandbox with the castle right under the spade."""
    sc = self.sc
    # (revision 24: and back from the front rim, castle and all: "its base seems to overlap the wooden frame")
    y0, y1 = inner[0][1] + 30, inner[2][1] - (26 if SCN.PLACEMENT_REV >= 24 else 4)
    for _ in range(60):
        Y = sc.rng.uniform(y0, y1)
        t = (Y - inner[0][1]) / max(1, inner[3][1] - inner[0][1])
        xl = inner[0][0] + (inner[3][0] - inner[0][0]) * t + 30
        xr = inner[1][0] + (inner[2][0] - inner[1][0]) * t - 30
        X = sc.rng.uniform(xl, xr)
        p = sc.placed(self.vp, X, Y, sc.rng.random() < 0.5, eid=ep)
        if not sc.fits(p.bbox(), limit=0.15):
            continue
        s = sz(Y)
        f = p.facing() or 1
        tx, ty = p.anchor("spade_tip") if p.has_anchor("spade_tip") else (X + f * 60 * s, Y - 30 * s)
        cs = s * 0.85
        # the castle stands just beyond the spade, its near wall under the blade
        cx_ = tx + f * 26 * cs
        if not (xl - 20 <= cx_ <= xr + 20):
            continue
        castle, cbb = D.sandcastle(cx_, Y + 4 * s, cs, heaped=SCN.PLACEMENT_REV >= 24)
        if SCN.PLACEMENT_REV >= 11:
            # revision 11: the child and the castle wholly inside the sand, clear of the frame (a child whose
            # legs reached over the edge: "unclear whether kneeling inside it or on the rim")
            pb = p.bbox()
            if min(pb[0], cbb[0]) < xl - 30 + 6 or max(pb[2], cbb[2]) > xr + 30 - 6:
                continue
        sc.assets[ep] = p
        ec = sc.svg(sc.eid("sandcastle"), "Sandcastle", castle, Y + 6, cbb, "scored")
        self.act(self.p, "building a sandcastle in the sandbox", ["building a sandcastle", "making a sandcastle", "playing in the sand", "playing in the sandbox", "digging in the sand", "sandcastle"], "sandcastle", [ep, ec])
        return True
    return False


SandboxPlay.place_building = _sandbox_place_building


class SlidePlay(T):
    id = "slide"
    settings = PG
    needs = {"playground": {"slide"}}
    uses = ("slide",)
    exclusive = ("slide",)

    def bind(self):
        sc = self.sc
        self.p = sc.person(KIDS)
        self.at_top = sc.rng.random() < 0.5
        if SCN.PLACEMENT_REV >= 8:
            self.at_top = False     # revision 8: always on the way down the chute (below)
        if self.at_top and SCN.PLACEMENT_REV >= 7:
            # revision 7: sitting at the top of the chute, ready to go down (standing up there with the
            # arms raised "looks a bit unsafe")
            self.vp = sc.need(self.p, "sit", sc.rng.choice(["happy", "laughing"]), 90)
        elif self.at_top:
            self.vp = sc.need(self.p, "cheer", sc.rng.choice(["happy", "laughing"]), 45)
        elif SCN.PLACEMENT_REV >= 8:
            # revision 8: half way down the chute, legs out along it and arms up (sitting at its foot read
            # as "has just come down the slide or is simply resting")
            self.vp = sc.need(self.p, "slide_down", sc.rng.choice(["happy", "laughing"]), 90)
        else:
            self.vp = sc.need(self.p, "sit_ground", sc.rng.choice(["happy", "laughing", "surprised"]), 90)

    def place(self):
        sc = self.sc
        A = sc.S.anchors["slide"]
        ep = sc.eid("slidekid")
        if self.at_top and SCN.PLACEMENT_REV >= 7:
            x, y = A["platform"]
            f = 1 if A["bottom"][0] > x else -1
            s = sz(A["depth"])
            p = sc.placed(self.vp, 0, 0, sc.mirror_for(self.vp, f), depth_y=A["depth"] + 1, eid=ep)
            p.move_anchor_to("seat", (x + f * 44 * s, y + 4 * s))
            if not sc.fits(p.bbox(), limit=0.2):
                return False
            sc.assets[ep] = p
            sc.legib_ok.add(("slide", ep))
            self.act(self.p, "sitting at the top of the slide, about to go down", ["at the top of the slide", "about to slide down", "on the slide", "playing on the slide"], "slide", [ep])
            return True
        if self.at_top:
            x, y = A["platform"]
            p = sc.placed(self.vp, x, y, sc.rng.random() < 0.5, depth_y=A["depth"] + 1, eid=ep)
            if not sc.fits(p.bbox(), limit=0.2):
                return False
            sc.assets[ep] = p
            sc.legib_ok.add(("slide", ep))
            self.act(self.p, "standing at the top of the slide", ["at the top of the slide", "on the slide", "playing on the slide", "cheering"], "slide", [ep])
            return True
        if SCN.PLACEMENT_REV >= 8 and "chute" in A:
            (x0, y0), (x1, y1) = A["chute"]
            f = 1 if x1 > x0 else -1
            for t in (0.48, 0.40, 0.56):
                p = sc.placed(self.vp, 0, 0, sc.mirror_for(self.vp, f), depth_y=A["depth"] + 1, eid=ep)
                drop = D.RIDE24["slide"] if SCN.PLACEMENT_REV >= 22 else 8 if SCN.PLACEMENT_REV >= 9 else 3
                p.move_anchor_to("seat", (x0 + (x1 - x0) * t, y0 + (y1 - y0) * t + drop * sz(A["depth"])))
                if sc.fits(p.bbox(), limit=0.2):
                    break
            else:
                return False
            sc.assets[ep] = p
            sc.legib_ok.add(("slide", ep))
            self.act(self.p, "sliding down the slide", ["going down the slide", "sliding down", "sliding", "on the slide", "playing on the slide"], "slide", [ep])
            return True
        x, y = A["bottom"]
        p = sc.placed(self.vp, 0, 0, sc.mirror_for(self.vp, 1), depth_y=A["depth"] + 1, eid=ep)
        p.move_anchor_to("seat", (x - 30 * sz(y), y - 26 * sz(y)))
        if not sc.fits(p.bbox(), limit=0.2):
            return False
        sc.assets[ep] = p
        sc.legib_ok.add(("slide", ep))
        self.act(self.p, "sliding down the slide", ["going down the slide", "sliding", "on the slide", "playing on the slide"], "slide", [ep])
        return True


class PushStroller(T):
    id = "push_stroller"
    settings = ("park", "street", "playground")

    def bind(self):
        sc = self.sc
        self.p = sc.person(ADULTS)
        self.vp = sc.need(self.p, "push", sc.rng.choice(["smile", "neutral", "focused"]), 90)

    def place(self):
        sc = self.sc
        ep = sc.eid("pusher")

        def pram(p):
            f = p.facing() or 1
            s = sz(p.Y)
            g = ((p.anchor("push_L")[0] + p.anchor("push_R")[0]) / 2, (p.anchor("push_L")[1] + p.anchor("push_R")[1]) / 2)
            x = g[0] + f * (84 if SCN.PLACEMENT_REV >= 11 else 104) * s
            self.pr = D.stroller(x, p.Y + 4, s, f, grip=g, short=SCN.PLACEMENT_REV >= 11, face=SCN.PLACEMENT_REV >= 14)
            b = self.pr[1]["bbox"]
            if SCN.PLACEMENT_REV >= 11 and not sc.setting_clear((b[0] - 12, b[1] - 12, b[2] + 12, b[3] + 6), only=("stall",)):
                return None     # revision 11: clear of the market stall (a pram "partly inside or under the stall")
            return [b]
        p = self.place_with(ep, self.vp, self.stand_spots(), want_face=sc.rng.choice([1, -1]), extras=pram)
        if not p:
            return False
        svg, info = self.pr
        es = sc.svg(sc.eid("stroller"), "Baby stroller", svg, p.Y + 4, info["bbox"], "scored")
        self.act(self.p, "pushing a baby in a stroller", ["pushing a stroller", "pushing a pram", "pushing a baby carriage", "baby", "walking with a baby", "buggy"], "stroller", [ep, es])
        return True


EVENTS = [WalkDog, WaterFlowers, HoseWater, Sweep, Rake, Dig, PlantFlowers, Carry, CarryBag, BenchSit, DrinkBench, Picnic, FlyKite,
          Balloon, Swing, HangLaundry, PlayCatch, KickBall, Jump, Photo, Fishing, FeedBirds, IceCream, PaintFence, Run, Wave,
          DogSleeping, CatSleeping, GoatGrazing, DogPlaying, BirdPerched, DucksSwimming, BirdsFlying, CatOnFence,
          SeesawPlay, SandboxPlay, SlidePlay, PushStroller]
for _c in EVENTS:
    _c.kind = "event"


# ============================================================================ inference modules
class BlockedHose(T):
    id = "blocked_hose"
    kind = "inference"
    settings = ("garden",)
    needs = {"garden": {"hose_reel"}}
    exclusive = ("hose_reel",)
    units, content = 1, 3

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.a = sc.animal(["dog", "goat"])
        self.vp = sc.need(self.p, "hose_inspect", "puzzled", 90)
        self.va = sc.need(self.a, "stand", sc.rng.choice(["neutral", "happy"]), 90)

    def place(self):
        sc = self.sc
        rx, ry = sc.S.anchors["hose_reel"]
        ep, ea = sc.eid("hoseman"), sc.eid("hoseanimal")
        for X, Y in self.stand_spots(x_range=(560, 1250), y_range=(760, 960), n=120):
            p = sc.placed(self.vp, X, Y, sc.mirror_for(self.vp, -1), eid=ep)
            if not sc.fits(p.bbox()):
                continue
            # the animal stands on the hose between the reel and the man, facing him
            ax = rx + (X - rx) * sc.rng.uniform(*self.k3((0.62, 0.72), (0.45, 0.62), (0.30, 0.45)))
            ay = Y + sc.rng.uniform(20, 50)
            if not sc.S.walkable(ax, ay):
                continue
            a = sc.placed(self.va, ax, ay, sc.mirror_for(self.va, 1), eid=ea)
            if not sc.fits(a.bbox()) or sc.overlap(a.bbox(), p.bbox()) > 0.08:
                continue
            sc.assets[ep], sc.assets[ea] = p, a
            paw = a.anchor("paw_FR") if a.anchor("paw_FR")[1] >= a.anchor("paw_FL")[1] else a.anchor("paw_FL")
            if SCN.PLACEMENT_REV >= 11:
                # revision 11: the near back foot, the first the water from the reel meets, pinches the hose
                paw = a.anchor("paw_BR") if a.anchor("paw_BR")[1] >= a.anchor("paw_BL")[1] else a.anchor("paw_BL")
            hx, hy = p.anchor("hose_in")
            s = sz(Y)
            pinch = (paw[0], paw[1] - 2)
            if SCN.PLACEMENT_REV >= 11:
                fp = a.anchor("paw_FR") if a.anchor("paw_FR")[1] >= a.anchor("paw_FL")[1] else a.anchor("paw_FL")
                hose, hb = _pinched_hose(sc, (rx, ry), pinch, fp[0], (hx, hy), Y, s)
                eh = sc.svg(sc.eid("hose"), "Garden hose, pinched under the paw", hose, ay - 1, hb, "scored")
                # and no one placed later lies or stands on the hose's run along the ground (a sleeping cat lay
                # across the slack hose at the holder's feet)
                sc.keepout.append((hb[0], pinch[1] - 30 * s, hb[2], max(pinch[1], Y) + 30 * s))
            else:
                hose = D.hose_path([(rx, ry), (rx + 40, ay + 40), (pinch[0] - 90 * s, pinch[1] + 6), pinch, pinch], 1.0)
                hose += D.hose_path([pinch, (pinch[0] + 110 * s, pinch[1] - 4), ((pinch[0] + hx) / 2 + 30, Y + 20), (hx + 60 * s, hy + 110 * s), (hx, hy)], 0.8)
                eh = sc.svg(sc.eid("hose"), "Garden hose, pinched under the paw", hose, ay - 1, (rx, min(hy, ry), hx + 60, ay + 45), "scored")
            nx, ny = p.anchor("nozzle")
            drip = D.drops(nx, ny + 16 * s, s * 1.5, 1)
            en = sc.svg(sc.eid("drip"), "Single drip from the dry nozzle", drip, Y + 2, (nx - 14 * s, ny, nx + 14 * s, ny + 34 * s), "scored")
            pn, pnames = self.who(self.p)
            an = sc.name(self.a)
            self.act(self.p, "holding a hose, looking into the nozzle", ["holding a hose", "looking at the hose", "looking into the nozzle", "puzzled", "confused"], "hose", [ep, eh])
            it = self.ent(f"The {an} is standing on the hose", [f"{an} standing on the hose", f"{an} on the hose", "stepping on the hose"], an, [ea], animate=True)
            it["type"] = "action"
            it2 = self.ent("No water is coming out", ["no water", "water isn't coming out", "hose isn't working", "nothing coming out", "hose is dry"], "hose", [en])
            it2["type"] = "action"
            it2["cues"] = [en, ep]      # the drip is tiny; the man peering into the nozzle is a second cue (spec worked example)
            self.inf(f"The {an} is blocking the water by standing on the hose",
                     [f"the {an} is stepping on the hose so the water can't come out", "the hose is pinched", "blocking the water", "that's why there's no water"],
                     "water", 2, cues=[ea, en, ep], effect=[en])
            return True
        return False


def _pinched_hose(sc, reel, pinch, front_x, hand, Y, s):
    """Revision 11: the hose from the reel runs full and round up to the back foot, swelling more and more as it
    nears the foot, is squashed flat under the foot, and runs on thin and slack to the nozzle, draped from the
    hand in a long curve (drawn the same thickness all along, the stopped water read as "the water simply
    hasn't been turned on yet", and the animal as "on or right next to the hose"; a separate swelling read as
    "a hose connector or a puddle", and the hose rising straight to the hand as "a pole")."""
    rx, ry = reel
    px, py = pinch
    hx, hy = hand
    f = 1 if rx > px else -1                       # the side of the foot the water comes from
    # upstream: from the reel along the ground to the start of the swelling
    x0 = px + f * 96 * s
    up = D.hose_path([(rx, ry), (rx - f * 20, py + 6 * s), (x0, py + 1 * s)], 1.0)
    # the swelling: water held back by the foot, the hose growing fatter toward the foot and then nipped in
    # under it, its top rounded up off the ground, with a highlight along it
    prof = [(x0 + f * 8 * s, 4.5, 0.0)]          # (starting back over the hose's own end, so no seam shows)
    n = 48
    hmax = 14.5 * s
    for i in range(n + 1):
        t = i / n
        x = x0 + (px - f * 3 * s - x0) * t          # (the egg's end runs in under the foot, so the foot is on it)
        # swelling quickly into a long round egg that ends against the foot (growing slowly all the way to the foot,
        # the swelling read as "a cone shape, like a nozzle", "a second nozzle or a coupling")
        if t <= 0.80:
            g = math.sin(math.pi / 2 * min(1.0, t / 0.55)) ** 0.8
            hw = 4.5 + (hmax - 4.5) * g
        else:
            g = 1.0
            hw = max(2.6 * s, hmax * math.sqrt(max(0.0, 1.0 - ((t - 0.80) / 0.20) ** 2)))
        prof.append((x, hw, g))
    cyh = py + 1 * s
    ow = D.OW * 0.8

    def outline(extra):
        # (the fill starts a little further back than its edge, so the two starts leave no seam across the hose)
        pr = prof if extra else [(prof[0][0] + f * 3 * s,) + tuple(prof[0][1:])] + prof[1:]
        tp = [(x, cyh - (hw * (1 + 0.25 * g) + extra)) for x, hw, g in pr]
        bt = [(x, cyh + (hw * (1 - 0.25 * g) + extra)) for x, hw, g in pr]
        return "M " + " L ".join(D.P(*q) for q in tp + bt[::-1]) + " Z"
    bulge = f'<path d="{outline(ow)}" fill="{D.OUT}" stroke="{D.OUT}" stroke-width="1" stroke-linejoin="round"/>'
    bulge += f'<path d="{outline(0)}" fill="{C["hose"]}"/>'
    hl = [(x, cyh - hw * (1 + 0.25 * g) * 0.62) for x, hw, g in prof[int(n * 0.30):int(n * 0.72)]]
    bulge += D.stroke("M " + " L ".join(D.P(*q) for q in hl), "#4fa3bd", 3.0 * s, 0)
    # squashed flat under the foot: a wide thin band
    flat = D.ell(px, py + 1 * s, 16 * s, 2.6 * s, C["hose"], D.OW * 0.7)
    # downstream: thin and slack along the ground under the animal and past its front feet, then draped up to
    # the nozzle in a long curve (never behind the animal's body)
    gx = front_x - f * 46 * s
    gr = hx + f * 60 * s                          # where the hose leaves the ground
    if f * (gx - gr) < 0:
        gr = gx
    # (from the ground it rises in a soft curve bowed back toward the holder, so it hangs from the hand; bowed out
    # toward the animal it seemed to loop round it: "the dog stands inside the loop of hose")
    hm = (hx - f * 30 * s, hy + (py - hy) * 0.52)
    down = D.hose_path([(px - f * 10 * s, py + 1 * s), (front_x, py + 7 * s), (gx, py + 5 * s), ((gx + gr) / 2, py + 6 * s), (gr, py + 4 * s),
                        (hm[0] - f * 2 * s, py - 2 * s), hm, (hx - f * 16 * s, hy + (py - hy) * 0.15), (hx, hy)], 0.5)
    svg = up + down + bulge + flat
    xs = [rx, x0, gx, gr, hx]
    bb = (min(xs) - 12, min(ry, hy) - 10, max(xs) + 12, max(py, Y) + 30 * s)
    return svg, bb


class RainComing(T):
    id = "rain_coming"
    kind = "inference"
    sky = "dark"
    units, content = 1, 2
    uses = ("clouds_dark",)
    # v0.11: never with the wind (wind lines beside the pointer read as the storm already blowing), nor with a
    # flying kite (a pointer at the clouds read as "maybe at the kite"); v0.12 (revision 10): nor with anything
    # up in a tree's canopy (a fish, a ball, a kite) or in the sky (flying birds, a balloon floating away), which
    # a raised finger could be pointing at (a pointer at the clouds with a red bird overhead)
    exclusive = ("wind", "sky_kite") + (("tree_canopy", "sky_birds", "sky_balloon") if SCN.PLACEMENT_REV >= 10 else ())

    def bind(self):
        sc = self.sc
        self.p = sc.person(None)
        # revision 9: always worried (surprise did not say what was coming)
        self.vp = sc.need(self.p, "point_up", "worried" if SCN.PLACEMENT_REV >= 9 else sc.rng.choice(["worried", "surprised"]), 45)

    def place(self):
        sc = self.sc
        box = sc.S.anchors["dark_clouds_box"]
        cx = (box[0] + box[2]) / 2
        ep = sc.eid("skywatcher")
        cands = self.stand_spots(n=120)
        cands.sort(key=lambda q: -q[1])
        accept = lambda p: sc.gaze_ok(p, box) or p.facing() == (1 if cx > p.X else -1)
        if SCN.PLACEMENT_REV >= 6:
            # revision 6: placed after the other events, and only where the pointing line to the clouds
            # passes clear of everything else (a pointer read as pointing at a ball in a tree or at a cat
            # on the fence)
            accept = lambda p: (sc.gaze_ok(p, box) or p.facing() == (1 if cx > p.X else -1)) and self.line_clear(p, box)
        if SCN.PLACEMENT_REV >= 9:
            # revision 9: and not under or beside a tree (a child pointing up beside the tree with a fish in it
            # read as pointing at the fish)
            acc6 = accept
            accept = lambda p: acc6(p) and sc.setting_clear((p.bbox()[0] - 70, 0, p.bbox()[2] + 70, p.bbox()[3]), only=("tree", "tree_small"))
        p = sc.try_put(ep, self.vp, cands, want_face=self.face_to(cx), accept=accept)
        if not p:
            return False
        sc.checks[f"{ep}_looks_at_clouds"] = sc.gaze_ok(p, box)
        self.ent("Dark clouds are coming", ["dark clouds", "storm clouds", "clouds", "cloudy", "storm", "gray sky"], "clouds", ["clouds_dark"])
        self.act(self.p, "pointing up at the sky", ["pointing at the sky", "pointing at the clouds", "pointing up", "looking up", "worried"], "pointing", [ep])
        self.inf("It is about to rain", ["it's going to rain", "a storm is coming", "rain is coming", "it might rain", "going to get wet"],
                 "rain", 1, cues=["clouds_dark", ep], effect=["clouds_dark"])
        return True


RAIN_STRUCT9 = ("lamp", "stall", "tree", "tree_small", "clothesline", "laundry", "swing", "swing_seat", "slide", "seesaw", "feeder",
                "hose_reel", "house", "bench")


def _rain_line_clear(self, p, box, corridor=18, half_angle=28.0):
    sc = self.sc
    if SCN.PLACEMENT_REV >= 9:
        # revision 9: a wider cone and corridor (a pointer aimed above a floating box was read as pointing at it)
        corridor, half_angle = 24, 36.0
    # the pointing arm's anchors (a mirrored sprite swaps the L/R names)
    side = next((s for s in ("L", "R") if p.has_anchor(f"fingertip_{s}")), None)
    if side and p.has_anchor(f"hand_{side}_grip") and p.has_anchor("chest"):
        # the line the drawn arm points along (hand to fingertip and chest to fingertip, averaged), from the
        # fingertip up to the cloud bank: it must reach the clouds, and nothing scored may lie within
        # half_angle of it short of the top of the cloud bank or within corridor px of it (a pointer at the clouds read as
        # pointing at a bird on the lamp post when the arm was aimed between the two)
        tip, hand, chest = p.anchor(f"fingertip_{side}"), p.anchor(f"hand_{side}_grip"), p.anchor("chest")

        def unit(a, b):
            dx, dy = b[0] - a[0], b[1] - a[1]
            n = math.hypot(dx, dy) or 1.0
            return dx / n, dy / n
        u1, u2 = unit(hand, tip), unit(chest, tip)
        ux, uy = u1[0] + u2[0], u1[1] + u2[1]
        n = math.hypot(ux, uy) or 1.0
        ux, uy = ux / n, uy / n
        if uy > -0.3 or box[3] >= tip[1]:
            return False
        dcl = (box[3] - tip[1]) / uy
        xh = tip[0] + ux * dcl
        if not (box[0] - 30 <= xh <= box[2] + 30):
            return False
        ray = [(tip[0] + ux * s, tip[1] + uy * s) for s in range(10, int(dcl) + 1, 10)]
        dfar = (box[1] - tip[1]) / uy   # up to the top of the cloud bank: a bird level with the clouds counts
        for k, b, _ in sc.scored_boxes(ignore=(getattr(p, "id", None),)):
            if "cloud" in k:
                continue
            g = (b[0] - corridor, b[1] - corridor, b[2] + corridor, b[3] + corridor)
            if any(g[0] <= x <= g[2] and g[1] <= y <= g[3] for x, y in ray):
                return False
            for qx in (b[0], (b[0] + b[2]) / 2, b[2]):
                for qy in (b[1], (b[1] + b[3]) / 2, b[3]):
                    dx, dy = qx - tip[0], qy - tip[1]
                    d = math.hypot(dx, dy) or 1.0
                    if d < dfar and math.degrees(math.acos(max(-1.0, min(1.0, (dx * ux + dy * uy) / d)))) < half_angle:
                        return False
        if SCN.PLACEMENT_REV >= 9:
            # revision 9: the fingertip and the first stretch of the line clear of standing structures (a hand
            # ending at the corner of the produce stall read as pointing at it), and the whole line clear of
            # kite strings
            near = [tip] + [q for q in ray if math.hypot(q[0] - tip[0], q[1] - tip[1]) <= 220]
            for x, y in near:
                if not sc.setting_clear((x - 16, y - 16, x + 16, y + 16), only=RAIN_STRUCT9):
                    return False
            for (ax, ay), (bx, by) in getattr(sc, "strings", []):
                n = max(2, int(math.hypot(bx - ax, by - ay) / 10))
                spts = [(ax + (bx - ax) * k / n, ay + (by - ay) * k / n) for k in range(n + 1)]
                if any(math.hypot(x - qx, y - qy) < 26 for x, y in ray for qx, qy in spts):
                    return False
        return True
    hand = p.anchor("hand_L_grip") if p.has_anchor("hand_L_grip") else p.anchor("head_top")
    tx, ty = (box[0] + box[2]) / 2, box[3]
    # aim at the nearest point of the cloud bank's bottom edge
    tx = min(max(hand[0], box[0]), box[2]) if box[0] <= hand[0] <= box[2] else (box[0] + 40 if hand[0] < box[0] else box[2] - 40)
    n = max(2, int(math.hypot(tx - hand[0], ty - hand[1]) / 10))
    pts = [(hand[0] + (tx - hand[0]) * k / n, hand[1] + (ty - hand[1]) * k / n) for k in range(1, n + 1)]
    for k, b, _ in sc.scored_boxes(ignore=(getattr(p, "id", None),)):
        g = (b[0] - corridor, b[1] - corridor, b[2] + corridor, b[3] + corridor)
        if any(g[0] <= x <= g[2] and g[1] <= y <= g[3] for x, y in pts):
            return False
    return True


RainComing.line_clear = _rain_line_clear


class CatStalksBird(T):
    id = "cat_stalks_bird"
    kind = "inference"
    units, content = 1, 2
    exclusive = ("second_cat",) if SCN.PLACEMENT_REV >= 14 else ()

    def bind(self):
        sc = self.sc
        self.c = sc.animal(["cat"])
        self.b = sc.animal(["songbird"])
        self.on_fence = sc.setting_id == "garden" and sc.rng.random() < 0.6
        # revision 6: a low, flat stalking crouch, belly to the ground and tail straight back (the old
        # crouch read as running)
        # revision 11: frozen mid-step with a front paw lifted, the hind legs bunched (crawling on four
        # outstretched legs it read as "creeping or running toward" the bird, "or just running past")
        self.vc = sc.need(self.c, "stalk_paw" if SCN.PLACEMENT_REV >= 11 else ("stalk" if SCN.PLACEMENT_REV >= 6 else "crouch"), "alert", 90)
        if SCN.PLACEMENT_REV >= 17 and self.on_fence:
            # revision 17: on the fence the bird sits perched (pecking at the fence top it was "in an awkward pose with
            # its wing up")
            self.vb = sc.need(self.b, "perch", "neutral", 90)
        else:
            self.vb = sc.need(self.b, "peck" if not self.on_fence else sc.rng.choice(["peck", "perch"]), "neutral", 90)

    def place(self):
        sc = self.sc
        ec, eb = sc.eid("stalkcat"), sc.eid("stalkbird")
        if self.on_fence:
            A = sc.S.anchors["fence_top"]
            xs = list(range(A["x0"] + 60, A["x1"] - 200, 30))
            sc.rng.shuffle(xs)
            for x in xs[:20]:
                want = sc.rng.choice([1, -1])
                c = sc.placed(self.vc, x, A["y"], sc.mirror_for(self.vc, want), depth_y=A["depth"], eid=ec)
                # (revision 17: closer on the fence; well over a cat's length off, the cat read as "walking along the top
                # of the fence ... toward the blue bird")
                bx = x + want * sc.rng.uniform(*(self.k3((120, 150), (135, 170), (150, 190)) if SCN.PLACEMENT_REV >= 17
                                                 else self.k3((110, 160), (150, 260), (260, 360))))
                if not (A["x0"] < bx < A["x1"]):
                    continue
                b = sc.placed(self.vb, bx, A["y"], sc.mirror_for(self.vb, -want), depth_y=A["depth"], eid=eb)
                if SCN.PLACEMENT_REV >= 12:
                    # revision 12: the cat and its bird on the fence clear of the clothesline, the bird table and the swing,
                    # as the cat walking the fence is (between the line's posts the stalking cat seemed to be on the line)
                    span = (min(c.bbox()[0], b.bbox()[0]), min(c.bbox()[1], b.bbox()[1]), max(c.bbox()[2], b.bbox()[2]), max(c.bbox()[3], b.bbox()[3]))
                    if not sc.clear_of_setting(span, ("clothesline", "laundry", "feeder", "swing"), 30):
                        continue
                if SCN.PLACEMENT_REV >= 12:
                    span = self.span_ok(c, b)
                    if span is None:
                        continue
                if sc.fits(c.bbox(), limit=0.05) and sc.fits(b.bbox(), limit=0.05) and sc.gaze_ok(c, b.bbox()):
                    sc.assets[ec], sc.assets[eb] = c, b
                    if SCN.PLACEMENT_REV >= 12:
                        sc.stalk_spans = getattr(sc, "stalk_spans", []) + [span]
                    return self.items(ec, eb, "on the fence")
            return False
        near = 0.75 if SCN.PLACEMENT_REV >= 6 else 1.0      # revision 6: nearer the bird
        for X, Y in self.stand_spots(n=150):
            want = sc.rng.choice([1, -1])
            c = sc.placed(self.vc, X, Y, sc.mirror_for(self.vc, want), eid=ec)
            if not sc.fits(c.bbox()):
                continue
            if SCN.PLACEMENT_REV >= 6 and not self.dog_free(c):
                continue
            bx, by = X + want * sc.rng.uniform(*self.k3((110, 160), (150, 240), (240, 330))) * sz(Y) * near, Y + sc.rng.uniform(-12, 12)
            if not sc.S.walkable(bx, by):
                continue
            b = sc.placed(self.vb, bx, by, sc.mirror_for(self.vb, -want), eid=eb)
            if not sc.fits(b.bbox(), limit=0.05):
                continue
            ok = sc.gaze_ok(c, (b.bbox()[0] - 10, b.bbox()[1] - 30, b.bbox()[2] + 10, b.bbox()[3] + 10))
            if ok and SCN.PLACEMENT_REV >= 12:
                # revision 12: the cat and its bird have the ground to themselves, now and later: nobody walks past them
                # and nothing stands by them (beside a girl walking by, the cat was "running toward the red bird" or
                # "just running past the girl")
                s = sz(Y)
                cb, bb_ = c.bbox(), b.bbox()
                room = (min(cb[0], bb_[0]) - 110 * s, min(cb[1], bb_[1]) - 150 * s, max(cb[2], bb_[2]) + 110 * s, max(cb[3], bb_[3]) + 40 * s)
                tight = (min(cb[0], bb_[0]) - 40 * s, min(cb[1], bb_[1]) - 20 * s, max(cb[2], bb_[2]) + 40 * s, max(cb[3], bb_[3]) + 25 * s)
                if any(sc.overlap(room, q.bbox()) > 0 for q in sc.assets.values()) or \
                        any(sc.overlap(tight, e["bbox"]) > 0 for e in sc.svgs.values() if e.get("bbox") and e["role"] in ("scored", "filler")):
                    continue
                span = self.span_ok(c, b)
                if span is None:
                    continue
            if ok:
                sc.assets[ec], sc.assets[eb] = c, b
                if SCN.PLACEMENT_REV >= 6:
                    sc.no_dog.append(self.zone(c))
                if SCN.PLACEMENT_REV >= 12:
                    sc.airzones.append(room)
                    sc.groundzones.append(tight)
                    sc.stalk_spans = getattr(sc, "stalk_spans", []) + [span]
                return self.items(ec, eb, "")
        return False

    def span_ok(self, c, b):
        """Revision 12: no kite or balloon string passes between the cat and its bird (a kite string run down between
        them on the fence top); the span is kept for strings drawn later."""
        sc = self.sc
        cb, bb_ = c.bbox(), b.bbox()
        span = (min(cb[0], bb_[0]) - 10, min(cb[1], bb_[1]) - 30, max(cb[2], bb_[2]) + 10, max(cb[3], bb_[3]) + 10)
        for (ax, ay), (bx, by) in getattr(sc, "strings", []):
            n = max(2, int(math.hypot(bx - ax, by - ay) / 10))
            if any(span[0] <= ax + (bx - ax) * t / n <= span[2] and span[1] <= ay + (by - ay) * t / n <= span[3] for t in range(n + 1)):
                return None
        return span

    def zone(self, c):
        cb, s = c.bbox(), sz(c.Y)
        if SCN.PLACEMENT_REV >= 12:
            # revision 12: no dog anywhere at the cat's depth, across the whole picture (a dog walked toward the cat from
            # across the street "might be about to lunge or chase"; still so when kept twice as far off)
            return (0, cb[1] - 90 * s, 1600, cb[3] + 60 * s)
        return (cb[0] - 170 * s, cb[1] - 60 * s, cb[2] + 170 * s, cb[3] + 40 * s)

    def dog_free(self, c):
        """Revision 6: no dog near the stalking cat (a cat crouched by a passing dog read as fleeing it)."""
        z = self.zone(c)
        return not any(a.family.startswith("animal.dog") and min(a.bbox()[2], z[2]) > max(a.bbox()[0], z[0]) and min(a.bbox()[3], z[3]) > max(a.bbox()[1], z[1])
                       for a in self.sc.assets.values())

    def items(self, ec, eb, where):
        sc = self.sc
        cn, bn = sc.name(self.c), sc.name(self.b)
        sc.checks[f"{ec}_looks_at_bird"] = True
        it = self.ent(f"A {cn} is crouching low{(' ' + where) if where else ''}", ["cat crouching", "cat hiding", "cat sneaking", "cat ready to pounce", "cat watching"], "cat", [ec], animate=True)
        it["type"] = "action"
        # (revision 11: a bird pecking on the fence top is keyed there; keyed as "pecking at the ground", a reader
        # who saw it on the fence lost the point)
        peck_at = "on the fence" if (where and SCN.PLACEMENT_REV >= 11) else "at the ground"
        it = self.ent(f"A {bn} is pecking {peck_at}" if self.vb[1] == "peck" else f"A {bn} is sitting {where or 'nearby'}",
                      ["bird", "bird eating", "bird pecking", "little bird"], "bird", [eb], animate=True)
        it["type"] = "action"
        self.inf("The cat is about to catch the bird", ["the cat wants to catch the bird", "the cat is going to pounce", "the cat is hunting the bird", "the cat is stalking the bird"],
                 "cat", 1, cues=[ec, eb], effect=[eb])
        return True


class StuckInTree(T):
    id = "ball_in_tree"
    kind = "inference"
    units, content = 1, 2
    # v0.11: never with the wind (a reach for the ball beside a hat blowing away read as surprise at the wind)
    exclusive = ("tree_canopy", "wind")
    thing = "ball"

    def bind(self):
        sc = self.sc
        self.p = sc.person(YOUNG)
        pose = sc.rng.choice(["point_up", "reach_up"])
        if SCN.PLACEMENT_REV >= 17 and self.thing == "ball":
            # revision 17: the child points up at the ball (both arms raised, the reach read as "cheering, stretching or
            # waving")
            pose = "point_up"
        self.vp = sc.need(self.p, pose, sc.rng.choice(["sad", "puzzled", "worried"]), 45)

    def draw_thing(self, x, y):
        r = self.k3(31, 27, 25)      # at least 3% of the canvas width across, the size rule for a scored thing
        if SCN.PLACEMENT_REV >= 12 and self.thing == "ball":
            # revision 12: caught among the leaves: a twig across its lower side and leaf clusters over two of its edges,
            # like the kite's (drawn whole on the crown it "could be read as drawn on top of the tree rather than stuck in
            # it", "a balloon or round ornament")
            T_ = self.sc.S.anchors["tree"]
            # (the branch passes behind the ball, under it, and the clusters cover only slivers of its rim, so it stays
            # round: a twig across its lower half made it a blue cap with a brim)
            svg = D.stroke(D.poly_d([(x - 1.7 * r, y + 1.25 * r), (x - 0.3 * r, y + 0.92 * r), (x + 1.6 * r, y + 0.70 * r)]), C["wood"], 0.24 * r)
            svg += D.ball(x, y, r, C["blue"])
            lobes = [[(x - 1.22 * r, y - 0.52 * r, 0.44 * r), (x - 1.52 * r, y - 0.05 * r, 0.36 * r), (x - 0.85 * r, y - 1.02 * r, 0.32 * r)],
                     [(x + 1.24 * r, y + 0.30 * r, 0.42 * r), (x + 1.50 * r, y - 0.18 * r, 0.34 * r)]]
            svg += _leaf_clusters(T_, lobes, "bc%d%d" % (abs(int(x)), abs(int(y))))
            return svg, (x - r, y - r, x + r, y + r)
        return D.ball(x, y, r, C["blue"]), (x - r, y - r, x + r, y + r)

    def place(self):
        sc = self.sc
        T_ = sc.S.anchors["tree"]
        slots = list(T_["slots"][:4])
        under = SCN.PLACEMENT_REV >= 9 and self.thing == "ball" and (self.vp[1] == "reach_up" or SCN.PLACEMENT_REV >= 17)
        if under:
            # revision 9: a child reaching up stands under the ball, so the ball sits out on a side of the
            # canopy (a reach toward a ball "up and to the left of her, not directly above" was hedged)
            slots = [T_["slots"][i] for i in (0, 1, 4, 5)]
        if SCN.PLACEMENT_REV >= 9:
            # revision 9: clear of the house (a ball on the canopy's edge by the wall could be "floating in front
            # of the foliage")
            def off_house(q):
                b = self.draw_thing(*q)[1]
                return sc.setting_clear((b[0] - 30, b[1] - 30, b[2] + 30, b[3] + 30), only=("house",))
            slots = [q for q in slots if off_house(q)] or slots
        sc.rng.shuffle(slots)
        x, y = slots[0]
        svg, bb = self.draw_thing(x, y)
        tree_base = T_["bbox"][3]
        eo = sc.svg(sc.eid(self.thing + "intree"), f"{self.thing.capitalize()} stuck in the tree", svg, tree_base + 0.5, bb, "scored")
        if SCN.PLACEMENT_REV >= 12 and self.thing == "ball":
            # revision 12: and leaf clusters of the same kind spread over the crown, as with the kite
            tex = _crown_texture(T_, bb, 1.0)
            if tex:
                sc.svg(sc.eid("crownleaves"), "Leaves on the tree", _leaf_clusters(T_, tex, "ct%d" % abs(int(x))), tree_base + 0.3, T_["bbox"], "background")
        ep = sc.eid("treekid")
        cands = self.stand_spots(x_range=(x - 320, x + 320), y_range=(tree_base + 10, min(990, tree_base + 220)), n=120)
        tx = T_["canopy"][0]
        # stand beside the trunk, not right in front of it, so the child's head is clear of the tree
        cands = [q for q in cands if abs(q[0] - tx) > 95 * sz(q[1])]
        if under:
            # (revision 17: the pointing child too stands on the ball's side of the trunk, below it: "beside the trunk,
            # not under the stuck ball", "nowhere near the ball")
            cands = [q for q in cands if (q[0] - tx) * (x - tx) > 0 and abs(q[0] - x) <= (110 if self.vp[1] == "point_up" else 70)]
        cands.sort(key=lambda q: abs(q[0] - x))
        box = (bb[0] - 30, bb[1] - 30, bb[2] + 30, bb[3] + 30)
        ctr = ((bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2)
        rev14 = SCN.PLACEMENT_REV >= 14
        # revision 14: the raised hand and its line up to the ball clear of every person and animal (a teenager's
        # finger "right next to" a cat on the fence: "pointing at the black cat ... or at the blue ball")
        pc = (lambda p: self.point_clear(p, ctr)) if rev14 else (lambda p: True)
        p = sc.try_put(ep, self.vp, cands, want_face=self.face_to(x), accept=lambda p: sc.gaze_ok(p, box) and pc(p))
        if not p:
            p = sc.try_put(ep, self.vp, cands, want_face=self.face_to(x), accept=pc)
            if not p:
                sc.remove(eo)
                return False
            sc.checks[f"{ep}_looks_at_{self.thing}"] = False
        else:
            sc.checks[f"{ep}_looks_at_{self.thing}"] = True
        if rev14:
            sc.point_lines.append((self.tip(p), ctr, sc.placing))
        self.items(ep, eo, p)
        return True

    def tip(self, p):
        """The raised hand: the pointing fingertip, else the higher hand."""
        side = next((s_ for s_ in ("L", "R") if p.has_anchor(f"fingertip_{s_}")), None)
        if side:
            return p.anchor(f"fingertip_{side}")
        hands = [p.anchor(a) for a in ("hand_L_grip", "hand_R_grip") if p.has_anchor(a)]
        return min(hands, key=lambda q: q[1]) if hands else p.anchor("head_top")

    def point_clear(self, p, ctr):
        """Revision 14: no other person or animal within reach of the raised hand or of its line up to the thing."""
        sc = self.sc
        tx, ty = self.tip(p)
        s = sz(p.Y)
        n = max(2, int(math.hypot(ctr[0] - tx, ctr[1] - ty) / 10))
        pts = [(tx + (ctr[0] - tx) * t / n, ty + (ctr[1] - ty) * t / n) for t in range(n + 1)]
        for q in sc.assets.values():
            if q is p or not (q.family.startswith("person.") or q.family.startswith("animal.")):
                continue
            b = q.bbox()
            g = (b[0] - 22, b[1] - 22, b[2] + 22, b[3] + 22)
            if any(g[0] <= x_ <= g[2] and g[1] <= y_ <= g[3] for x_, y_ in pts):
                return False
            # (and nothing close round the hand itself)
            cx_, cy_ = min(max(tx, b[0]), b[2]), min(max(ty, b[1]), b[3])
            if math.hypot(cx_ - tx, cy_ - ty) < 60 * s:
                return False
        return True

    def items(self, ep, eo, p):
        n = self.sc.name(self.p)
        self.act(self.p, "pointing up at the tree" if self.vp[1] == "point_up" else "reaching up toward the tree",
                 ["pointing at the tree", "reaching up", "looking up at the tree", "sad", "upset"], "tree", [ep])
        self.ent("There is a ball up in the tree", ["ball in the tree", "ball", "ball up in the branches"], "ball", [eo])
        self.inf(f"The {n}'s ball is stuck in the tree", ["the ball got stuck in the tree", "the ball is stuck", "they can't get the ball down", "the ball is caught in the tree"],
                 "stuck", 1, cues=[eo, ep], effect=[eo])


LEAF_HI, LEAF_EDGE = "#4f9e46", "#2d6a2b"


def _crown_clip(tree, cid):
    return f'<defs><clipPath id="{cid}">' + "".join(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="{max(0.5, r - D.OW * 0.6):.1f}"/>' for a, b, r in tree["parts"]) + "</clipPath></defs>"


def _leaf_clusters(tree, clusters, cid):
    """Revision 11: clusters of leaves on a crown, a lighter green with a thin darker-green edge, clipped to the
    crown (a few on the crown, and the ones over a thing caught in it)."""
    body = ""
    for parts in clusters:
        body += "".join(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="{r:.1f}" fill="{LEAF_HI}" stroke="{LEAF_EDGE}" stroke-width="2.6"/>' for a, b, r in parts)
        body += "".join(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="{max(0.5, r - 1.6):.1f}" fill="{LEAF_HI}"/>' for a, b, r in parts)
    return _crown_clip(tree, cid) + f'<g clip-path="url(#{cid})">{body}</g>'


def _crown_texture(tree, avoid, k):
    """Revision 11: three or four leaf clusters spread over the crown, clear of `avoid` (the clusters over a kite
    caught in the crown are then of a piece with the tree; drawn alone over the kite, clumps of leaves "look
    pasted on top")."""
    cx, cy, R = tree["canopy"]
    spots = [(cx + 0.38 * R, cy - 0.50 * R), (cx - 0.58 * R, cy + 0.10 * R), (cx + 0.62 * R, cy + 0.38 * R), (cx - 0.12 * R, cy + 0.52 * R),
             (cx - 0.40 * R, cy - 0.58 * R), (cx + 0.15 * R, cy - 0.05 * R)]
    out = []
    for x, y in spots:
        r = 0.17 * R
        if x + 2 * r > avoid[0] - 10 and x - 2 * r < avoid[2] + 10 and y + 2 * r > avoid[1] - 10 and y - 2 * r < avoid[3] + 10:
            continue
        out.append([(x, y, r), (x + 0.9 * r, y + 0.35 * r, 0.75 * r), (x - 0.85 * r, y + 0.4 * r, 0.7 * r)])
        if len(out) == 4:
            break
    return out


def _leaf_spray(cx, cy, r, k, n, phase=0.0):
    """Revision 11: a spray of small pointed leaves around (cx, cy), two greens, thin outlines, short twigs
    between them: foliage in front of a thing caught in a tree."""
    svg = ""
    golden = 2.39996
    for i in range(n):
        t = (i + 0.5) / n
        a = i * golden + phase
        d = r * math.sqrt(t)
        x, y = cx + d * math.cos(a), cy + d * math.sin(a) * 0.8
        ang = math.degrees(a) + 35 * math.sin(i * 1.7)
        col = C["grass_dark"] if i % 3 else "#4f9e46"
        L, W = 13 * k, 6 * k
        ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        p0 = (x - ca * L, y - sa * L)
        p1 = (x + ca * L, y + sa * L)
        n0 = (x - sa * W, y + ca * W)
        n1 = (x + sa * W, y - ca * W)
        svg += D.shape(f"M {D.P(*p0)} Q {D.P(*n0)} {D.P(*p1)} Q {D.P(*n1)} {D.P(*p0)} Z", col, D.OW * 0.45)
    return svg


class KiteInTree(StuckInTree):
    id = "kite_in_tree"
    settings = ("park", "garden", "playground")
    thing = "kite"

    def bind(self):
        sc = self.sc
        self.p = sc.person(YOUNG)
        self.vp = sc.need(self.p, "fly_kite", sc.rng.choice(["sad", "puzzled", "worried"]), 90)

    def draw_thing(self, x, y):
        if SCN.PLACEMENT_REV >= 9:
            # revision 9: tipped askew with a clump of leaves over its top corner and the tail hanging limp,
            # so it is caught in the branches (drawn whole in front of the canopy it read as "flying there or
            # caught")
            k = self.k3(1.1, 0.85, 0.68)
            ksvg, info = D.kite(x, y, k, C["purple"], rot=-52)
            a = math.radians(-52)
            tx, ty = x + 50 * k * math.sin(a), y - 50 * k * math.cos(a)        # the kite's top point
            # a twig across the kite, from the canopy to its top corner, and a second clump over its lower
            # corner, so it sits inside the branches (one clump on the top corner still read "flying in front
            # of the tree, or caught")
            lx, ly = x + (-34 * math.cos(a)) * k, y + (-34 * math.sin(a)) * k         # the kite's left corner
            if SCN.PLACEMENT_REV >= 11:
                # (revision 11: the twig starts in the clump over the kite's corner, not out on the open crown, where
                # it showed in bits between the clumps)
                ksvg += D.stroke(D.poly_d([(lx - 10 * k, ly + 8 * k), (x - 4 * k, y + 2 * k), (tx + 4 * k, ty + 6 * k)]), C["wood"], 6 * k)
            else:
                ksvg += D.stroke(D.poly_d([(lx - 30 * k, ly + 26 * k), (x - 4 * k, y + 2 * k), (tx + 4 * k, ty + 6 * k)]), C["wood"], 6 * k)
            if SCN.PLACEMENT_REV >= 11:
                # revision 11: the same clumps of leaves, but drawn as the crown itself: its own green, no outline
                # where they lie on the crown, an outline only where they cross the kite or the twig, and nothing
                # outside the crown (outlined all round, the clumps "look pasted on top" of the kite; sprays of
                # small leaves read as "spiky scribbles or starbursts"; a kite hung from the crown's rim, half behind
                # it, read as "flying just beside or behind the tree")
                T_ = self.sc.S.anchors["tree"]
                lobes = [[(tx - 8 * k, ty - 4 * k, 26 * k), (tx + 20 * k, ty + 10 * k, 20 * k), (tx - 26 * k, ty + 16 * k, 17 * k)],
                         [(lx - 10 * k, ly + 8 * k, 19 * k), (lx - 30 * k, ly + 26 * k, 16 * k)]]
                ksvg += _leaf_clusters(T_, lobes, "kc%d%d" % (abs(int(x)), abs(int(y))))
            else:
                ksvg += D.blob([(tx - 8 * k, ty - 4 * k, 26 * k), (tx + 20 * k, ty + 10 * k, 20 * k), (tx - 26 * k, ty + 16 * k, 17 * k)], C["grass_dark"])
                ksvg += D.blob([(lx - 10 * k, ly + 8 * k, 19 * k), (lx - 30 * k, ly + 26 * k, 16 * k)], C["grass_dark"])
            self.bridle = info["bridle"]
            return ksvg, info["bbox"]
        ksvg, info = D.kite(x, y, self.k3(1.1, 0.85, 0.68), C["purple"], rot=-28)
        self.bridle = info["bridle"]
        return ksvg, info["bbox"]

    def place(self):
        sc = self.sc
        T_ = sc.S.anchors["tree"]
        slots = list(T_["slots"][:3])
        if SCN.PLACEMENT_REV >= 9:
            # revision 9: the kite and its leaves clear of the house (a kite on the canopy's edge was half hidden
            # behind the roof, its leaves drawn over the wall)
            def off_house(q):
                b = self.draw_thing(*q)[1]
                return sc.setting_clear((b[0] - 34, b[1] - 34, b[2] + 34, b[3] + 20), only=("house",))
            slots = [q for q in slots if off_house(q)] or slots
        x, y = sc.rng.choice(slots)
        svg, bb = self.draw_thing(x, y)
        tree_base = T_["bbox"][3]
        ep = sc.eid("kitekid")
        cands = self.stand_spots(x_range=(x - 520, x + 520), y_range=(tree_base + 10, 990), n=150)
        cands = [c for c in cands if abs(c[0] - x) > 160]
        cands.sort(key=lambda q: abs(abs(q[0] - x) - 330))
        bx, by = self.bridle

        def string_clear(p):
            """Revision 9: the slack string passes clear of everyone else (a string run past a man hanging
            out the washing seemed to be his)."""
            if SCN.PLACEMENT_REV < 9:
                return True
            sx, sy = p.anchor("string_end")
            cx_, cy_ = (sx + bx) / 2, max(sy, by) + 60
            pts = [((1 - t) ** 2 * sx + 2 * (1 - t) * t * cx_ + t * t * bx, (1 - t) ** 2 * sy + 2 * (1 - t) * t * cy_ + t * t * by) for t in (k / 24 for k in range(2, 23))]
            if any(q.bbox()[0] - 12 <= px <= q.bbox()[2] + 12 and q.bbox()[1] - 12 <= py <= q.bbox()[3] + 12
                   for q in sc.assets.values() for px, py in pts):
                return False
            # (revision 12: nor between a stalking cat and its bird)
            if SCN.PLACEMENT_REV >= 12 and any(z[0] <= px <= z[2] and z[1] <= py <= z[3] for px, py in pts for z in getattr(sc, "stalk_spans", [])):
                return False
            # and clear of standing structures, short of the canopy (a string run past a clothesline post seemed
            # to pass through it)
            return all(sc.setting_clear((px - 14, py - 14, px + 14, py + 14), only=KITE_STRUCT9) for px, py in pts[:-4])
        p = sc.try_put(ep, self.vp, cands, want_face=self.face_to(x),
                       accept=lambda p: not any(seg_cross(p.anchor("string_end"), (bx, by), a, b) for a, b in getattr(sc, "strings", [])) and string_clear(p))
        if not p:
            return False
        eo = sc.svg(sc.eid("kiteintree"), "Kite caught in the tree", svg, tree_base + 0.5, bb, "scored")
        if SCN.PLACEMENT_REV >= 11:
            # revision 11: leaf clusters of the same kind spread over the crown
            tex = _crown_texture(T_, bb, self.k3(1.1, 0.85, 0.68))
            if tex:
                sc.svg(sc.eid("crownleaves"), "Leaves on the tree", _leaf_clusters(T_, tex, "ct%d" % abs(int(x))), tree_base + 0.3, T_["bbox"], "background")
        sx, sy = p.anchor("string_end")
        sc.strings = getattr(sc, "strings", []) + [((sx, sy), (bx, by))]
        if SCN.PLACEMENT_REV >= 9:
            # revision 9: the string hangs slack, sagging below the straight line (a taut string said flying)
            cy_ = max(sy, by) + 60
            string = f'<path d="M {D.P(sx, sy)} Q {D.P((sx + bx) / 2, cy_)} {D.P(bx, by)}" fill="none" stroke="{D.OUT}" stroke-width="2.4"/>'
            es = sc.svg(sc.eid("kitestring"), "Kite string", string, p.Y + 0.5, (min(sx, bx), min(sy, by), max(sx, bx), max(sy, by) + 32), "scored")
        else:
            string = f'<path d="M {D.P(sx, sy)} Q {D.P((sx + bx) / 2, min(sy, by) - 40)} {D.P(bx, by)}" fill="none" stroke="{D.OUT}" stroke-width="2.4"/>'
            es = sc.svg(sc.eid("kitestring"), "Kite string", string, p.Y + 0.5, (min(sx, bx), min(sy, by) - 40, max(sx, bx), max(sy, by)), "scored")
        self.act(self.p, "holding a kite string", ["holding a kite", "flying a kite", "pulling the string", "sad", "upset"], "kite", [ep, es])
        self.ent("A kite is caught in the tree", ["kite in the tree", "kite", "kite stuck"], "kite", [eo])
        self.inf("The kite got stuck in the tree", ["the kite is stuck in the tree", "the kite got caught", "they can't get the kite down", "the kite is tangled in the branches"],
                 "stuck", 1, cues=[eo, es, ep], effect=[eo])
        return True


KITE_STRUCT9 = ("lamp", "stall", "clothesline", "laundry", "swing", "swing_seat", "slide", "seesaw", "feeder", "hose_reel", "bench", "house")


class IceCreamDrop(T):
    id = "ice_cream_drop"
    kind = "inference"
    settings = ("park", "street", "playground")
    # revision 18: no other ice cream eaten and no runner in the picture (the jogger "could have bumped the child and
    # knocked the ice cream off")
    exclusive = ("drop_vs_eat", "drop_vs_run", "drop_vs_bench_eat") if SCN.PLACEMENT_REV >= 18 else ()
    units, content = 1, 3

    def bind(self):
        sc = self.sc
        self.p = sc.person(KIDS)
        if SCN.PLACEMENT_REV >= 8:
            # revision 8: the empty cone held out and tipped toward the viewer, the other hand to the face,
            # the head bent to the scoop on the ground (a cone held to the mouth read as being eaten, and
            # nobody could tell it was empty); the brown dog (the white dog's head merged with the scoop)
            self.d = sc.animal(["dog"], prefer=("animal.dog_01",))
            self.vp = sc.need(self.p, "cone_dropped", "sad", 45)
        else:
            self.d = sc.animal(["dog"])
            self.vp = sc.need(self.p, "hold_cone", sc.rng.choice(["sad", "scared", "worried"]), 45)
        self.vd = sc.need(self.d, "sniff", sc.rng.choice(["happy", "neutral"]), 90)

    def place(self):
        if SCN.PLACEMENT_REV >= 8:
            return self.place8()
        sc = self.sc
        ep, ed = sc.eid("conekid"), sc.eid("lickdog")
        for X, Y in self.stand_spots(n=120):
            p = sc.placed(self.vp, X, Y, sc.rng.random() < 0.5, eid=ep)
            if not sc.fits(p.bbox()):
                continue
            s = sz(Y)
            side = sc.rng.choice([1, -1])
            sx, sy = X + side * 95 * s, Y + 22 * s
            if not sc.S.walkable(sx, sy):
                continue
            splat, sbb = D.dropped_scoop(sx, sy, s * self.k3(1.5, 1.15, 0.95))
            # the dog's mouth goes to the splat
            d = sc.placed(self.vd, 0, 0, sc.mirror_for(self.vd, -side), eid=ed)
            d.X, d.Y = sx, sy - 2
            mx, my = d.anchor("mouth")
            # the muzzle reaches the far edge of the splat, so most of the ice cream stays in view
            # (revision 2: measured from the splat's own size, which shrinks on harder pictures)
            reach = 24 * s if SCN.PLACEMENT_REV < 2 else (sbb[2] - sbb[0]) / 2 - (4 * s if SCN.PLACEMENT_REV < 4 else -3 * s)
            d.X += sx + side * reach - mx
            d.set_depth(sy - 2)
            if not sc.S.walkable(d.X, d.Y) or not sc.fits(d.bbox(), limit=0.15):
                continue
            sc.assets[ep], sc.assets[ed] = p, d
            es = sc.svg(sc.eid("splat"), "Ice cream on the ground", splat, sy - 3, sbb, "scored")
            n = sc.name(self.p)
            dn = sc.name(self.d)
            self.act(self.p, "holding an empty cone, looking upset", ["holding an empty cone", "crying", "sad", "upset", "empty cone"], "cone", [ep])
            self.ent("Ice cream is lying on the ground", ["ice cream on the ground", "dropped ice cream", "ice cream fell", "ice cream"], "ice cream", [es])
            it = self.ent(f"A {dn} is licking the ice cream", [f"{dn} eating the ice cream", f"{dn} licking it", f"{dn} sniffing the ice cream"], dn, [ed], animate=True)
            it["type"] = "action"
            self.inf(f"The {n} dropped the ice cream", [f"the {n} dropped the ice cream", "the ice cream fell off the cone", "dropped it", "lost the ice cream"],
                     "dropped", 1, cues=[es, ep, ed], effect=[es])
            return True
        return False


def _ice_cream_place8(self):
    """Revision 8: the scoop lies on the ground right under the empty cone, clear of the feet, and the
    dog comes at it from the far side."""
    sc = self.sc
    ep, ed = sc.eid("conekid"), sc.eid("lickdog")
    for X, Y in self.stand_spots(n=150):
        p = sc.placed(self.vp, X, Y, sc.rng.random() < 0.5, eid=ep)
        if not sc.fits(p.bbox()) or not p.has_anchor("cone_top"):
            continue
        s = sz(Y)
        cx, _ = p.anchor("cone_top")
        side = 1 if cx >= X else -1
        k = s * self.k3(1.5, 1.15, 0.95)
        # revision 12: a smaller scoop in the same puddle (full size it was "about as big as the dog's head")
        ball = 0.7 if SCN.PLACEMENT_REV >= 12 else 1.0
        _, sbb0 = D.dropped_scoop(0, 0, k, ball=ball)
        half = (sbb0[2] - sbb0[0]) / 2
        feet = [p.anchor(a)[0] for a in ("foot_L", "foot_R") if p.has_anchor(a)] or [X]
        edge = max(feet) + 10 * s if side > 0 else min(feet) - 10 * s
        sx = max(cx, edge + half) if side > 0 else min(cx, edge - half)
        if abs(sx - cx) > 0.9 * half:   # the cone must still be above the scoop
            continue
        sy = Y + 12 * s
        if not sc.S.walkable(sx, sy):
            continue
        splat, sbb = D.dropped_scoop(sx, sy, k, ball=ball)
        # the dog's nose meets the far side of the scoop (its head over the scoop merged with it)
        d = sc.placed(self.vd, sx, sy - 2, sc.mirror_for(self.vd, -side), eid=ed)
        db = d.bbox()
        d.X += sx + side * 14 * k - (db[0] if side > 0 else db[2])
        if not sc.S.walkable(d.X, d.Y) or not sc.fits(d.bbox(), limit=0.15):
            continue
        if not sc.fits(sbb, limit=0.05, ignore=()):
            continue
        if SCN.PLACEMENT_REV >= 9:
            # revision 9: the child, the scoop and the dog stand apart from everyone else, and stay so (a man
            # sweeping right behind the dog could be sweeping up the ice cream; a wheelbarrow against its tail)
            bs = [p.bbox(), d.bbox(), sbb]
            grp = (min(b[0] for b in bs) - 50 * s, min(b[1] for b in bs), max(b[2] for b in bs) + 50 * s, max(b[3] for b in bs) + 12 * s)
            if any(sc.overlap(grp, q.bbox()) > 0 for q in sc.assets.values()) or \
                    any(sc.overlap(grp, e["bbox"]) > 0 for e in sc.svgs.values() if e.get("bbox") and e["role"] in ("scored", "filler")):
                continue
            sc.groundzones.append(grp)
        sc.assets[ep], sc.assets[ed] = p, d
        es = sc.svg(sc.eid("splat"), "Ice cream on the ground", splat, sy - 3, sbb, "scored")
        n = sc.name(self.p)
        dn = sc.name(self.d)
        self.act(self.p, "holding an empty cone, looking down at the ice cream on the ground, upset",
                 ["holding an empty cone", "looking at the dropped ice cream", "sad", "upset", "empty cone", "crying"], "cone", [ep])
        self.ent("Ice cream is lying on the ground", ["ice cream on the ground", "dropped ice cream", "ice cream fell", "ice cream", "scoop on the ground"], "ice cream", [es])
        it = self.ent(f"A {dn} is licking the ice cream", [f"{dn} eating the ice cream", f"{dn} licking it", f"{dn} sniffing the ice cream"], dn, [ed], animate=True)
        it["type"] = "action"
        self.inf(f"The {n} dropped the ice cream", [f"the {n} dropped the ice cream", "the ice cream fell off the cone", "dropped it", "lost the ice cream"],
                 "dropped", 1, cues=[es, ep, ed], effect=[es])
        return True
    return False


IceCreamDrop.place8 = _ice_cream_place8


class AboutToTrip(T):
    id = "about_to_trip"
    kind = "inference"
    units, content = 1, 2
    # revision 17: never under the windy hat's gust (an open book beside wind lines read as "a newspaper, a map, or
    # struggling to hold papers in the wind")
    exclusive = ("calm_reader",) if SCN.PLACEMENT_REV >= 17 else ()

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        # revision 7: a bigger book held open with its pages showing (the small book seen edge-on read as a phone)
        self.vp = sc.need(self.p, "walk_read_open" if SCN.PLACEMENT_REV >= 7 else "walk_read", "focused", 90)
        self.obj = sc.rng.choice(["bucket", "ball", "box"])
        if SCN.PLACEMENT_REV >= 4 and self.obj == "box" and "floating_box" in getattr(sc, "picked_ids", ()):
            self.obj = "bucket"     # one box in a picture with a floating box
        if SCN.PLACEMENT_REV >= 7 and self.obj == "ball" and set(getattr(sc, "picked_ids", ())) & BALL_EVENTS:
            self.obj = "bucket"     # revision 7: no second ball like the one in another event

    def place(self):
        sc = self.sc
        ep = sc.eid("reader")
        for X, Y in self.stand_spots(n=150):
            if SCN.PLACEMENT_REV >= 17 and Y < 650:
                continue    # revision 17: not at the far back, where the obstacle in her path "has no obvious owner or purpose"
            want = 1 if X < 800 else -1
            p = sc.placed(self.vp, X, Y, sc.mirror_for(self.vp, want), eid=ep)
            if not sc.fits(p.bbox()):
                continue
            # revision 8: away from the clothesline (between its posts the open book read as laundry)
            if SCN.PLACEMENT_REV >= 8 and not sc.clear_of_setting(p.bbox(), ("clothesline", "laundry"), 40):
                continue
            s = sz(Y)
            ox, oy = X + want * sc.rng.uniform(*self.k3((80, 100), (95, 130), (150, 200))) * s, Y + 4
            if SCN.PLACEMENT_REV >= 13:
                # revision 13: the obstacle stands squarely on the line of the leading foot (a few pixels in front of the
                # walker's line read as "slightly to one side": "he may walk into it, or he may just pass it")
                feet = [p.anchor(k) for k in ("foot_L", "foot_R") if p.has_anchor(k)]
                if feet:
                    # (never behind the walker's own ground line, which kept it off the walkable ground at the back)
                    oy = max(Y, max(feet, key=lambda q: q[0] * want)[1])
            col = sc.rng.choice([C["blue"], C["red"]]) if self.obj == "bucket" else None
            gap = sc.rng.uniform(45, 85) * s if SCN.PLACEMENT_REV >= 21 else 0.0

            def draw_obj(ox):
                if self.obj == "bucket":
                    svg, bb = D.bucket(ox, oy, s * 0.95, col)
                    return svg, bb, "a bucket", ["bucket", "pail"], "bucket"
                if self.obj == "ball":
                    r = 24 * s
                    return D.ball(ox, oy - r, r, C["red"]), (ox - r, oy - 2 * r, ox + r, oy), "a ball", ["ball", "a ball on the ground"], "ball"
                svg, bb = D.crate(ox, oy, s * 0.7)
                return svg, bb, "a box", ["box", "crate", "a box in the way"], "box"
            svg, bb, label, acc, key = draw_obj(ox)
            if SCN.PLACEMENT_REV >= 21:
                # revision 21: the obstacle a full step ahead of the leading toe, squarely on her line (25 px ahead of it, the box
                # lay "to the side of / slightly ahead of" her: "she might trip over it, or ... simply walk past it")
                feet = [p.anchor(k) for k in ("foot_L", "foot_R") if p.has_anchor(k)]
                toe = max((q[0] for q in feet), key=lambda v: v * want) if feet else (p.bbox()[2] if want > 0 else p.bbox()[0])
                near = bb[0] if want > 0 else bb[2]
                ox += toe + want * gap - near
                svg, bb, label, acc, key = draw_obj(ox)
            if not sc.S.walkable(ox, oy):
                continue
            if not sc.fits(bb, limit=0.05):
                continue
            # revision 8: the obstacle clear of the clothesline too (a bucket by its post went with the washing)
            if SCN.PLACEMENT_REV >= 8 and not sc.clear_of_setting(bb, ("clothesline", "laundry"), 30):
                continue
            if SCN.PLACEMENT_REV >= 7:
                # revision 7: the obstacle stands alone in the walker's path: nothing else scored around
                # it or between it and the walker (a box beside another person was not linked to the walker)
                zone = (bb[0] - 60 * s, bb[1] - 40 * s, bb[2] + 60 * s, bb[3] + 20 * s)
                lane = (min(X, ox), Y - 50 * s, max(X, ox), Y + 12 * s)
                if any(sc.overlap(b, z) > 0 for _, b, _ in sc.scored_boxes(ignore=(ep,)) for z in (zone, lane)):
                    continue
                # and in front of no bench, stall or other structure (a box drawn over a bench's back read as on the bench)
                if not sc.air_clear((bb[0] - 10, bb[1], bb[2] + 10, bb[3] + 26)):
                    continue
            beyond = None
            if SCN.PLACEMENT_REV >= 20:
                # revision 20: and nothing else on the ground further along her way, now or later (past the bucket, readers
                # had a reading walker "step on the sleeping cat" or "trip over the bicycle" too)
                far = bb[2] if want > 0 else bb[0]
                x0_, x1_ = sorted((far, far + want * 380 * s))
                beyond = (max(0.0, x0_), Y - 110 * s, min(float(D.W), x1_), Y + 40 * s)
                if any(sc.overlap(b, beyond) > 0 for _, b, _ in sc.scored_boxes(ignore=(ep,))):
                    continue
                if not sc.setting_clear(beyond, only=sc.LANE_STRUCT):
                    continue
            sc.assets[ep] = p
            if beyond is not None:
                sc.lanes.append((beyond, self))
                sc.groundthings.append((bb, self))
            if SCN.PLACEMENT_REV >= 7:
                # and nobody placed later stands beside the obstacle or in the lane (a kicker placed next
                # to the bucket made it hers)
                sc.airzones.append(zone)
                sc.keepout.append(lane)
            eo = sc.svg(sc.eid("obstacle"), f"{label} in the way", svg, oy, bb, "scored")
            n = sc.name(self.p)
            self.act(self.p, "reading while walking", ["reading while walking", "walking and reading", "not looking where he's going", "reading a book"], "reading", [ep])
            self.ent(f"There is {label} on the ground in front of {art(n)} {n}", acc, key, [eo])
            self.inf(f"The {n} is going to trip over {label}", [f"going to trip over the {key}", "going to fall", "will bump into it", "isn't looking where they're going"],
                     "trip", 1, cues=[ep, eo], effect=[eo])
            return True
        return False


class DogBegs(T):
    id = "dog_begs"
    kind = "inference"
    needs = {"*": {"bench"}}
    uses = ("bench",)
    exclusive = ("bench", "bench_front") + (("drop_vs_bench_eat",) if SCN.PLACEMENT_REV >= 18 else ())
    units, content = 1, 2

    def bind(self):
        sc = self.sc
        self.p = sc.person(None)
        self.food = sc.rng.choice(["sit_apple", "sit_ice_cream"])
        if SCN.PLACEMENT_REV >= 7:
            self.food = "sit_ice_cream"     # revision 7: an apple read as a cherry or a clown nose
        self.vp = sc.need(self.p, self.food, sc.rng.choice(["content", "smile", "happy"]), 45)
        self.d = sc.animal(["dog"])
        # revision 7: sitting square with the head tipped up at the food (the upright sit read as rearing up,
        # standing and looking up as just watching)
        self.vd = sc.need(self.d, "beg" if SCN.PLACEMENT_REV >= 7 else sc.rng.choice(["sit", "look_up"]), "happy", 90)

    def place(self):
        sc = self.sc
        B = sc.S.anchors["bench"]
        ep, ed = sc.eid("eater"), sc.eid("beggar")
        for frac in (0.35, 0.65):
            p = BenchSit.seat(self, ep, frac)
            if not p:
                continue
            spots = [(side, 40, 0) for side in (1, -1)]
            if SCN.PLACEMENT_REV >= 2:          # a step further out when the bench end is taken
                spots += [(side, 75, 28) for side in (1, -1)]
            if SCN.PLACEMENT_REV >= 4:          # or in front of the bench end, still looking up at the food
                spots += [(side, 20, 60) for side in (1, -1)] + [(side, 110, 50) for side in (1, -1)]
            for side, dx, dy in spots:
                x = (B["x1"] + dx) if side > 0 else (B["x0"] - dx)
                y = B["front_y"] + dy
                d = sc.placed(self.vd, x, y, sc.mirror_for(self.vd, -side), eid=ed)
                if not sc.fits(d.bbox(), limit=0.12, ignore=(ep,)):
                    continue
                if SCN.PLACEMENT_REV >= 17:
                    # revision 17: the dog clear of the eater's legs (its paws "overlap the woman's legs and the bench
                    # (cramped)")
                    db, pb = d.bbox(), p.bbox()
                    if min(db[2], pb[2]) + 8 > max(db[0], pb[0]) and min(db[3], pb[3]) > max(db[1], pb[1]):
                        continue
                gx = p.anchor("hand_R_grip")
                box = (gx[0] - 70, gx[1] - 80, gx[0] + 70, gx[1] + 50)
                if not sc.gaze_ok(d, (p.bbox()[0], p.bbox()[1], p.bbox()[2], p.bbox()[3])):
                    continue
                sc.assets[ed] = d
                n, dn = sc.name(self.p), sc.name(self.d)
                food = "an apple" if self.food == "sit_apple" else "an ice cream"
                self.act(self.p, f"sitting on the bench eating {food}", ["eating", "sitting on the bench", f"eating {food}", "snack"], "eating", [ep])
                if SCN.PLACEMENT_REV >= 7:
                    # revision 7: the begging itself (readers saw the sitting beg as "stretching up on its hind legs to beg")
                    it = self.ent(f"A {dn} is begging beside the bench, looking up at the food", [f"{dn} begging", f"{dn} looking up", f"{dn} sitting up", f"{dn} stretching up toward the food", f"{dn} watching the food"], dn, [ed], animate=True)
                else:
                    it = self.ent(f"A {dn} is sitting by the bench, looking up", [f"{dn} sitting", f"{dn} watching", f"{dn} looking up", f"{dn} waiting"], dn, [ed], animate=True)
                it["type"] = "action"
                self.inf(f"The {dn} wants some of the food", [f"the {dn} is begging", f"the {dn} wants a bite", "wants the food", "hoping for a treat"],
                         "begging", 1, cues=[ed, ep], effect=[ep])
                sc.checks[f"{ed}_looks_at_food"] = True
                return True
            sc.remove(ep)
        return False


def _crosses_path(sc, pts):
    """Revision 13: True if the polyline runs over the setting's path (garden and park paths carry their edges)."""
    from .settings import on_path
    A = sc.S.anchors.get("path")
    if not isinstance(A, dict) or not A.get("edges"):
        return False
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        for k in range(13):
            x, y = ax + (bx - ax) * k / 12, ay + (by - ay) * k / 12
            if y >= A["edges"][0][0] - 5 and on_path(A, x, y, margin=-10):
                return True
    return False


class SprinklerPackage(T):
    id = "sprinkler_package"
    kind = "inference"
    settings = ("garden", "park")
    # v0.15 (revision 13): no sprinkler running under storm clouds (pointed out as odd)
    sky = "clear" if SCN.PLACEMENT_REV >= 13 else None
    exclusive = ("lawn_spray",) if SCN.PLACEMENT_REV >= 16 else ()
    # revision 19: one hose per picture (the sprinkler's hose running off the picture's edge beside a second, blocked one
    # left "unclear water source")
    exclusive += ("hose_reel",) if SCN.PLACEMENT_REV >= 19 else ()
    units, content = 1, 2

    def bind(self):
        pass

    def place(self):
        sc = self.sc
        for X, Y in self.stand_spots(y_range=(sc.S.horizon + 120, 960), n=80):
            toward = 1 if X < 800 else -1
            s = sz(Y)
            dist = self.k3(170, 250, 340)
            px, py = X + toward * dist * s, Y + 10
            if not sc.S.walkable(px, py):
                continue
            if SCN.PLACEMENT_REV >= 15:
                # revision 15: the longest arc comes down on the box's lid, and the box shows it is soaked (drops drawn
                # above the lid "could be water coming out of the box"); in the park the sprinkler stands on the lawn,
                # never on the path ("an odd thing to find in a park")
                if _crosses_path(sc, [(X - 24 * s, Y), (X + 24 * s, Y)]) or _crosses_path(sc, [(px - 40 * s, py), (px + 46 * s, py)]):
                    continue
                lid = (px + 6 * s, py - 56 * s)
                spr, arcs, sbb = D.sprinkler(X, Y, s * self.k3(1.25, 1.0, 0.85), toward, dist, land=lid, solid=SCN.PLACEMENT_REV >= 17)
            else:
                spr, arcs, sbb = D.sprinkler(X, Y, s * self.k3(1.25, 1.0, 0.85), toward, dist, solid=SCN.PLACEMENT_REV >= 17)
            pk, pbb = D.package(px, py, s)
            if not (sc.fits(sbb, limit=0.08) and sc.fits(pbb, limit=0.05)):
                continue
            if SCN.PLACEMENT_REV >= 15 and not (sc.clear_of_setting(sbb, ("blanket",), margin=12) and sc.clear_of_setting(pbb, ("blanket",), margin=12)):
                # revision 15: the spray and the box off the picnic blanket (a blanket under the arcs, its corner on the box)
                continue
            if SCN.PLACEMENT_REV >= 4:
                ko = (sbb[0] - 10, sbb[1], sbb[2] + 10, sbb[3] + 8)

                def in_spray(q):
                    b = q.bbox()
                    f0, f1 = b[3] - 0.25 * (b[3] - b[1]), b[3]
                    return min(b[2], ko[2]) > max(b[0], ko[0]) and min(f1, ko[3]) > max(f0, ko[1])
                if any(in_spray(q) for q in sc.assets.values()):
                    continue
            if SCN.PLACEMENT_REV >= 19:
                # revision 19: and nobody already standing in front of the spray or the box (a goat just in front of the
                # arcs read as grazing in it)
                fz = (min(sbb[0], pbb[0]) - 10, min(sbb[1], pbb[1]), max(sbb[2], pbb[2]) + 10, max(sbb[3], pbb[3]) + 14)

                def in_front(q):
                    b = q.bbox()
                    return (q.family.startswith("person.") or q.family.startswith("animal.")) and not q.m["variant"].get("airborne") \
                        and q.Y > Y and min(b[2], fz[2]) > max(b[0], fz[0]) and min(b[3], fz[3]) > max(b[1], fz[1])
                if any(in_front(q) for q in sc.assets.values() if hasattr(q, "family")):
                    continue
            hose = ""
            if SCN.PLACEMENT_REV >= 7:
                # revision 7: a hose from the sprinkler off the nearer side of the picture, away from the
                # spray (a sprinkler with no hose read as odd); nobody may stand on it
                sk = s * self.k3(1.25, 1.0, 0.85)
                edge = -20 if toward > 0 else D.W + 20
                x0 = X - toward * 18 * sk
                n = max(2, int(abs(edge - x0) / 160))
                pts = [(x0, Y - 4 * sk)]
                for i in range(1, 2 * n + 1):
                    t = i / (2 * n)
                    pts.append((x0 + (edge - x0) * t, Y + 6 * sk + (12 * sk if i % 2 else 0) + 10 * sk * t))
                if len(pts) % 2 == 0:
                    pts.append((edge, Y + 16 * sk))
                band = (min(x0, edge), Y - 10 * sk, max(x0, edge), Y + 34 * sk)
                if SCN.PLACEMENT_REV >= 13 and _crosses_path(sc, pts):
                    # revision 13: the hose never runs across a path (a hose across the paving "could trip" someone);
                    # it runs off the bottom of the picture instead, or the sprinkler goes elsewhere
                    # (revision 20: no longer off the bottom, where it rose from the edge "like a stiff pipe": elsewhere)
                    if SCN.PLACEMENT_REV >= 20:
                        continue
                    yb = D.H + 20
                    n = max(2, int((yb - Y) / 120))
                    pts = [(x0, Y - 4 * sk)] + [(x0 - toward * (14 * sk if i % 2 else 0) - toward * 30 * sk * i / n, Y + (yb - Y) * i / n)
                                                 for i in range(1, n + 1)]
                    if _crosses_path(sc, pts):
                        continue
                    band = (min(q[0] for q in pts) - 10 * sk, Y - 10 * sk, max(q[0] for q in pts) + 10 * sk, yb)
                feet = lambda q: (q.bbox()[0], q.bbox()[3] - 0.15 * (q.bbox()[3] - q.bbox()[1]), q.bbox()[2], q.bbox()[3])
                if SCN.PLACEMENT_REV >= 20:
                    # revision 20: nor across the legs of anyone in front of it (a begging dog 40 px in front of the hose
                    # was drawn with the hose running under its body, as if standing on it)
                    feet = lambda q: (q.bbox()[0], q.bbox()[3] - 0.4 * (q.bbox()[3] - q.bbox()[1]), q.bbox()[2], q.bbox()[3] + 4)
                if any(sc.overlap(feet(q), band) > 0 for q in sc.assets.values()):
                    continue
                hose = D.hose_path(pts, sk * 0.8)
            es = sc.svg(sc.eid("sprinkler"), "Sprinkler spraying", hose + spr + arcs, Y, sbb, "scored")
            if SCN.PLACEMENT_REV >= 7:
                sc.keepout.append(band)
            if SCN.PLACEMENT_REV >= 4:      # nobody stands on the sprinkler or in its spray
                sc.keepout.append((sbb[0] - 10, sbb[1], sbb[2] + 10, sbb[3] + 8))
            if SCN.PLACEMENT_REV >= 19:
                sc.sprayzones.append(((min(sbb[0], pbb[0]) - 10, min(sbb[1], pbb[1]), max(sbb[2], pbb[2]) + 10, max(sbb[3], pbb[3]) + 14), Y))
            wet = D.wet_marks(px, py, s) if SCN.PLACEMENT_REV >= 15 else D.drops(px, py - 70 * s, s, 3)
            if SCN.PLACEMENT_REV >= 15:
                pbb = (pbb[0] - 18 * s, pbb[1], pbb[2] + 18 * s, pbb[3] + 10 * s)
                ep = sc.svg(sc.eid("package"), "Package on the grass", D.ell(px + 6 * s, py + 2 * s, 53 * s, 9 * s, C["water_light"], D.OW * 0.5) + pk + wet, py, pbb, "scored")
            else:
                ep = sc.svg(sc.eid("package"), "Package on the grass", pk + wet, py, pbb, "scored")
            it = self.ent("A sprinkler is spraying water", ["sprinkler", "water spraying", "sprinkler is on"], "sprinkler", [es])
            it["type"] = "action"
            self.ent("A package is sitting on the grass", ["package", "box", "parcel", "delivery"], "package", [ep])
            self.inf("The package is going to get soaked", ["the package is getting wet", "the box will get wet", "the water will ruin the package", "someone should move the package"],
                     "wet", 1, cues=[es, ep], effect=[ep])
            return True
        return False


class PaintTracks(T):
    id = "paint_tracks"
    kind = "inference"
    settings = ("garden",)
    exclusive = ("fence_paint",)
    units, content = 1, 3

    def bind(self):
        self.pf = PaintFence(self.sc)
        self.pf.ev = None
        self.pf.bind()
        # revision 6: the white dog, whose blue paws show (and the brown dog is left for the door)
        self.d = self.sc.animal(["dog"], prefer=("animal.dog_02",) if SCN.PLACEMENT_REV >= 6 else ())
        self.vd = self.sc.need(self.d, "walk", "happy", 90)

    def place(self):
        sc = self.sc
        self.pf.ev = self.ev
        if not self.pf.place():
            return False
        ep, es = self.pf.p_el
        p = sc.assets[ep]
        s = sz(p.Y)
        f = p.facing() or 1
        tx, ty = p.X - f * 95 * s, p.Y + 30 * s
        tray, tbb = D.paint_tray(tx, ty, s)
        ed = sc.eid("paintdog")
        for dist in self.k3((260, 300, 330), (330, 400, 460, 280), (480, 540, 420)):
            dx = tx - f * dist * s
            dy = ty + 60 * s
            if not sc.S.walkable(dx, dy):
                continue
            d = sc.placed(self.vd, dx, dy, sc.mirror_for(self.vd, -f), eid=ed)
            if not sc.fits(d.bbox(), limit=0.08):
                continue
            if SCN.PLACEMENT_REV >= 14 and not sc.lanes_ok(d):
                continue
            sc.assets[ed] = d
            sc.add_lanes(d)
            et = sc.svg(sc.eid("tray"), "Paint tray", tray, ty, tbb, "scored")
            pts = []
            n = 7
            hx = d.X + f * 40 * s
            for i in range(n):
                t = (i + 1) / (n + 1)
                pts.append((tx + (hx - tx) * t, ty + 6 * s + (dy - ty) * t))
            prints = D.paw_prints(pts, lambda y: sz(y) * 1.35)
            epr = sc.svg(sc.eid("prints"), "Paint paw prints", prints, ty + 1, (min(tx, hx) - 10, ty - 10, max(tx, hx) + 10, dy + 10), "scored")
            if SCN.PLACEMENT_REV >= 6:
                # revision 6: paint on the dog's paws too (white paws leaving blue prints read as odd)
                dabs = "".join(D.ell(ax, ay - 2.5 * s, 7.5 * s, 4.5 * s, C["paint"], D.OW * 0.5)
                               for ax, ay in (d.anchor(k) for k in ("paw_FL", "paw_FR", "paw_BL", "paw_BR") if d.has_anchor(k)))
                if dabs:
                    sc.svg(sc.eid("paintpaws"), "Paint on the dog's paws", dabs, d.Y + 3, d.bbox(), "setting")
            dn = sc.name(self.d)
            it = self.ent(f"A {dn} is walking away from the paint", [f"{dn} walking", f"{dn}", f"{dn} with paint on its feet"], dn, [ed], animate=True)
            it["type"] = "action"
            self.ent("There are paw prints in paint on the grass", ["paw prints", "footprints", "paint prints", "blue prints", "tracks"], "footprints", [epr, et])
            self.inf(f"The {dn} stepped in the paint and left footprints", [f"the {dn} walked through the paint", f"the {dn} stepped in the tray", "the dog made the footprints", "paint on the dog's paws"],
                     "paint", 2, cues=[ed, epr, et], effect=[epr])
            return True
        sc.remove(ep, es)
        sc.items = [i for i in sc.items if i["template"] != self.id]
        return False


HAT_STRUCT9 = ("lamp", "stall", "tree", "tree_small", "clothesline", "laundry", "swing", "swing_seat", "slide", "seesaw", "feeder", "house")


class WindyHat(T):
    id = "windy_hat"
    kind = "inference"
    # v0.13 (revision 11): never with things that would show the same gust and do not, balloons on strings and
    # washing being hung out ("the wind blows the hat away but the laundry ... unaffected")
    exclusive = ("wind",) + (("calm_balloon", "calm_lost_balloon", "calm_laundry") if SCN.PLACEMENT_REV >= 11 else ()) \
        + (("calm_reader",) if SCN.PLACEMENT_REV >= 17 else ())
    settings = ("park", "street", "garden")
    units, content = 1, 2

    def bind(self):
        sc = self.sc
        # revision 6: someone bareheaded loses the hat (a man still wearing his own cap read as the
        # owner of neither)
        # (revision 22: the teenager now wears a cap too)
        self.p = sc.person(GROWN, avoid=("person.jo", "person.tomas", "person.leo") if SCN.PLACEMENT_REV >= 22 else ("person.jo", "person.tomas") if SCN.PLACEMENT_REV >= 6 else ())
        self.vp = sc.need(self.p, "reach_up", sc.rng.choice(["surprised", "scared"]), 45)

    def place(self):
        sc = self.sc
        ep = sc.eid("hatperson")
        for X, Y in self.stand_spots(n=120):
            want = sc.rng.choice([1, -1])
            p = sc.placed(self.vp, X, Y, sc.mirror_for(self.vp, want), eid=ep)
            if not sc.fits(p.bbox()):
                continue
            hx, hy = p.anchor("head_top")
            s = sz(Y)
            cx, cy = hx + want * 105 * s, hy - 95 * s
            cols = [C["blue"], C["red"], C["orange"]]
            if SCN.PLACEMENT_REV >= 12:
                # revision 12: not the colour of a cap someone in the picture is wearing (a blue cap blowing away beside a
                # man in a blue-grey cap "might have been meant as his")
                worn = {"person.tomas": C["blue"], "person.jo": C["orange"]}
                if SCN.PLACEMENT_REV >= 22:
                    worn["person.leo"] = C["red"]
                cols = [c_ for c_ in cols if c_ not in {worn[f] for f in sc.fams if f in worn}] or cols
            svg, bb = D.cap(cx, cy, s * self.k3(1.45, 1.1, 0.85), sc.rng.choice(cols), rot=want * 35)
            if not sc.fits(bb, limit=0.05):
                continue
            # revision 6: the hat flies in open air, clear of lamp posts and trees (a cap over the top of a
            # lamp post read as caught on it)
            if SCN.PLACEMENT_REV >= 6 and not sc.air_clear(bb, 10):
                continue
            if SCN.PLACEMENT_REV >= 9:
                # revision 9: the hat and the band the wind lines cross clear of every standing structure (a cap
                # over the corner of the produce stall's awning sat on it, the wind lines across the awning
                # read as its stripes; lines across the clothesline)
                band = tuple(sorted([hx - want * 205 * s, cx]))
                if not sc.setting_clear((bb[0] - 14, bb[1] - 14, bb[2] + 14, bb[3] + 14), only=HAT_STRUCT9) or \
                        not sc.setting_clear((band[0], hy - 95 * s, band[1], hy - 20 * s), only=HAT_STRUCT9):
                    continue
                if SCN.PLACEMENT_REV >= 12:
                    # revision 12: and clear of every other person and animal (a cat on the fence "seems to sit in the wind
                    # lines next to the cap"), and nobody downwind of the cap, now or later (blowing toward a man sweeping the
                    # path it "could be the man's cap blown toward him")
                    gb = (min(band[0], bb[0]) - 20, min(hy - 95 * s, bb[1]) - 20, max(band[1], bb[2]) + 20, hy - 10 * s)
                    dw = (bb[2] if want > 0 else bb[0] - 300 * s, bb[1] - 40 * s, bb[2] + 300 * s if want > 0 else bb[0], Y + 10)
                    if any(k_ != ep and (sc.overlap(gb, q.bbox()) > 0 or sc.overlap(dw, q.bbox()) > 0) for k_, q in sc.assets.items()):
                        continue
                    self.downwind = dw
                    self.gustband = gb
            ok = sc.gaze_ok(p, (bb[0] - 40, bb[1] - 40, bb[2] + 40, bb[3] + 40))
            sc.assets[ep] = p
            sc.checks[f"{ep}_looks_at_hat"] = ok
            gusts = ""
            if SCN.PLACEMENT_REV >= 9:
                # revision 9: the wind lines run from behind the person on past the head toward the hat, and
                # the leaves fly ahead of them on the hat's side (short lines behind the person, with the hat
                # on the other side, read as the hat "going the opposite way to the wind")
                for k in range(3):
                    gx, gy = hx - want * (200 - 20 * k) * s, hy - (30 + 26 * k) * s
                    L = (abs(cx - gx) - 40 * s) / 2
                    gusts += f'<path d="M {D.P(gx, gy)} q {want * L / 2:.1f} {-10 * s:.1f} {want * L:.1f} 0 t {want * L:.1f} {-12 * s:.1f}" fill="none" stroke="{C["white"]}" stroke-width="{5 * s:.1f}" stroke-linecap="round" stroke-opacity="0.95"/>'
                gusts += D.blowing_leaves(hx + want * 30 * s, hy - 30 * s, cx - want * 20 * s, cy + 30 * s, s, 3)
            else:
                for k in range(3):
                    gx, gy = hx - want * (230 - 25 * k) * s, hy - (36 + 30 * k) * s
                    gusts += f'<path d="M {D.P(gx, gy)} q {want * 32 * s:.1f} {-10 * s:.1f} {want * 64 * s:.1f} 0 t {want * 60 * s:.1f} 0" fill="none" stroke="{C["white"]}" stroke-width="{5 * s:.1f}" stroke-linecap="round" stroke-opacity="0.95"/>'
                gusts += D.blowing_leaves(hx - want * 200 * s, hy - 10 * s, cx - want * 30 * s, cy + 20 * s, s, 4)
            if SCN.PLACEMENT_REV >= 9:
                # revision 9: no one placed later stands against the person who lost the hat (a catcher with his
                # arms out beside him made two people reaching up side by side)
                pb = p.bbox()
                sc.airzones.append((pb[0] - 50 * s, pb[1], pb[2] + 50 * s, pb[3]))
            if SCN.PLACEMENT_REV >= 11 and "tree" in sc.S.anchors and "canopy" in sc.S.anchors["tree"]:
                # revision 11: the same gust strips a few leaves off the tree, blowing the same way (the wind
                # lines and leaves by the hat alone: "the trees ... show no sign of wind, so the gust looks like
                # it is confined to the area around the cap")
                self.tree_gust(want)
            if SCN.PLACEMENT_REV >= 12:
                sc.airzones += [self.downwind, self.gustband]
                # revision 12: the washing on the line swings out with the same gust, and wind lines cross the open sky
                # elsewhere in the picture ("the washing on the line is not moving at all"; "nobody else's hair or
                # clothes is blowing")
                self.blow_laundry(want)
                self.sky_breeze(want, (min(hx - want * 235 * s, cx) - 60, max(hx - want * 235 * s, cx) + 60))
            eh = sc.svg(sc.eid("flyinghat"), "Hat blowing away", svg, Y + 1, bb, "scored")
            gx0, gx1 = sorted([hx - want * 235 * s, cx])
            sc.svg(sc.eid("gusts"), "Wind lines and blowing leaves", gusts, Y + 1, (gx0, cy - 10 * s, gx1, hy + 20 * s), "setting")
            n = sc.name(self.p)
            self.act(self.p, "reaching up for a hat", ["reaching for the hat", "trying to catch the hat", "surprised", "reaching up"], "hat", [ep])
            self.ent("A hat is flying through the air", ["hat in the air", "hat flying", "flying hat", "cap", "hat"], "hat", [eh])
            self.inf(f"The wind blew the {n}'s hat off", ["the wind blew the hat off", "it's windy", "the hat blew away", "the wind took the hat"],
                     "wind", 2, cues=[eh, ep], effect=[eh])
            return True
        return False


    def blow_laundry(self, want):
        """Revision 12: the jeans and towel on the garden line swung out downwind, with wind lines above the line; an
        empty swing seat swung out the same way ("the clothes and the cap are blowing hard, but the swing seat hangs
        perfectly still")."""
        from .settings import laundry_svg
        for e in self.sc.S.elements:
            if e["id"] == "laundry" and e.get("svg"):
                e["svg"] = laundry_svg(want)
                b = e["bbox"]
                e["bbox"] = (min(b[0], 600), 340, max(b[2], 880), b[3])
            if e["id"] == "swing_seat" and e.get("svg") and "swing" in self.sc.S.anchors:
                (ax, ay), (bx, by) = self.sc.S.anchors["swing"]["rope_top"]
                px, py = (ax + bx) / 2, (ay + by) / 2
                if SCN.PLACEMENT_REV >= 18:
                    # revision 18: the seat pushed a little downwind and tilted, its ropes following, so it stays inside
                    # the frame (swung out 16 degrees it "overlaps (or passes through)" the frame's leg)
                    A = self.sc.S.anchors["swing"]
                    sx_, sy_ = A["seat"]
                    w_ = A.get("seat_w", 84)
                    cx_, cy_ = sx_ + 6 * want, sy_ + 1
                    phi = math.radians(10 * want)
                    ex_, ey_ = 0.5 * w_ * math.cos(phi), 0.5 * w_ * math.sin(phi)
                    lt, rt = ((ax, ay), (bx, by)) if ax < bx else ((bx, by), (ax, ay))
                    svg_ = D.line(lt[0], lt[1], cx_ - ex_, cy_ - ey_, D.OUT, 4) + D.line(rt[0], rt[1], cx_ + ex_, cy_ + ey_, D.OUT, 4)
                    svg_ += f'<g transform="rotate({math.degrees(phi):.1f} {cx_:.1f} {cy_:.1f})">' + D.rect(cx_ - w_ / 2, cy_ - 4, w_, 13, C["red"], 3) + '</g>'
                    e["svg"] = svg_
                    b = e["bbox"]
                    e["bbox"] = (min(b[0], cx_ - w_ / 2 - 4), b[1], max(b[2], cx_ + w_ / 2 + 4), max(b[3], cy_ + abs(ey_) + 12))
                else:
                    e["svg"] = f'<g transform="rotate({-16 * want} {px:.1f} {py:.1f})">{e["svg"]}</g>'
                    b = e["bbox"]
                    L = b[3] - py
                    e["bbox"] = (b[0] - 0.3 * L, b[1], b[2] + 0.3 * L, b[3])

    def sky_breeze(self, want, avoid_x):
        """Revision 12: up to two wind lines in open sky away from the hat, clear of clouds, the sun, buildings, trees and
        anything drawn in the air."""
        sc = self.sc
        top = 60
        bot = sc.S.horizon - 70
        if bot - top < 60:
            return
        cands = [(x, y) for x in (180, 430, 690, 950, 1210, 1430) for y in (top + 30, (top + bot) / 2, bot - 20)]
        sc.rng.shuffle(cands)
        drawn = []
        for x, y in cands:
            if avoid_x[0] - 140 <= x <= avoid_x[1] + 140:
                continue
            if any(abs(x - a) < 330 for a, _ in drawn):
                continue
            L = 64
            svg = ""
            for dx, dy in ((0, 0), (want * 26, 20)):
                svg += f'<path d="M {D.P(x - want * L + dx, y + dy)} q {want * L / 2:.1f} -10 {want * L:.1f} 0 t {want * L:.1f} -12" fill="none" stroke="{C["white"]}" stroke-width="4.5" stroke-linecap="round" stroke-opacity="0.95"/>'
            bb = (x - L - 36, y - 26, x + L + 36, y + 32)
            if not sc.setting_clear((bb[0] - 20, bb[1] - 20, bb[2] + 20, bb[3] + 20)):
                continue
            if any(sc.overlap((bb[0] - 30, bb[1] - 30, bb[2] + 30, bb[3] + 30), b) > 0 for _, b, _ in sc.scored_boxes()):
                continue
            if any(min(bb[2], z[2]) > max(bb[0], z[0]) and min(bb[3], z[3]) > max(bb[1], z[1]) for z in sc.airzones):
                continue
            drawn.append((x, y))
            sc.svg(sc.eid("breeze"), "Wind lines", svg, 0, bb, "setting")
            sc.airzones.append(bb)
            if len(drawn) == 2:
                break

    def tree_gust(self, want):
        """Revision 11: leaves streaming off the downwind side of the crown and a short wind line past it, in open
        air clear of every person, animal and structure (else nothing is drawn)."""
        sc = self.sc
        T_ = sc.S.anchors["tree"]
        tcx, tcy, R = T_["canopy"]
        s = sz(T_["bbox"][3])
        x0, y0 = tcx + want * 0.92 * R, tcy - 0.15 * R
        x1, y1 = tcx + want * (R + 150 * s), tcy + 0.05 * R
        svg = D.blowing_leaves(x0, y0, x1, y1, s, 4)
        lx0, ly = tcx + want * 0.55 * R, tcy - 0.55 * R
        L = 70 * s
        svg += f'<path d="M {D.P(lx0, ly)} q {want * L / 2:.1f} {-8 * s:.1f} {want * L:.1f} 0 t {want * L:.1f} {-10 * s:.1f}" fill="none" stroke="{C["white"]}" stroke-width="{4.5 * s:.1f}" stroke-linecap="round" stroke-opacity="0.95"/>'
        xs = sorted([x0, x1, lx0, lx0 + want * 2 * L])
        bb = (xs[0] - 12 * s, min(ly, y0) - 22 * s, xs[-1] + 12 * s, max(y0, y1) + 22 * s)
        if bb[0] < 0 or bb[2] > D.W:
            return
        if any(min(bb[2], q.bbox()[2]) > max(bb[0], q.bbox()[0]) and min(bb[3], q.bbox()[3]) > max(bb[1], q.bbox()[1]) for q in sc.assets.values()):
            return
        if not sc.setting_clear(bb, only=tuple(x for x in HAT_STRUCT9 if x != "tree")):
            return
        sc.svg(sc.eid("treegust"), "Leaves blowing off the tree", svg, T_["bbox"][3] + 0.6, bb, "setting")
        sc.airzones.append(bb)


class BirdSteals(T):
    id = "bird_steals"
    kind = "inference"
    needs = {"*": {"bench"}}
    uses = ("bench",)
    exclusive = ("bench",)
    units, content = 1, 2

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.vp = sc.need(self.p, "sit_read", "focused", 45)
        # revision 5: the blue bird (a red bird against the tomato and crust read as a tipped-over cup)
        self.b = sc.animal(["songbird"], prefer=("animal.bird_02",))
        self.vb = sc.need(self.b, "peck", "neutral", 90)

    def place(self):
        sc = self.sc
        B = sc.S.anchors["bench"]
        ep, eb = sc.eid("benchreader"), sc.eid("thief")
        for frac, side in ((0.3, 1), (0.7, -1)):
            p = BenchSit.seat(self, ep, frac)
            if not p:
                continue
            s = sz(B["depth"])
            fx = (B["x0"] + (B["x1"] - B["x0"]) * (frac + side * 0.38))
            fy = B["seat_y"] - 2
            sty = 6 if SCN.PLACEMENT_REV >= 6 else 5
            # revision 8: the bold sandwich looked outsized; revision 23: smaller still with the smaller bird ("very large compared
            # with the man and the bird", overlapping his thigh)
            ss = s * (0.72 if SCN.PLACEMENT_REV >= 23 else 0.8 if SCN.PLACEMENT_REV >= 8 else 1.0)
            sw, sbb = D.sandwich(fx, fy, ss, style=sty)
            b = sc.placed(self.vb, fx + side * 34 * s, fy, sc.mirror_for(self.vb, -side), depth_y=B["depth"] + 4, eid=eb)
            if SCN.PLACEMENT_REV >= 4:
                # the beak touches the sandwich's near end (the bird stood beside it before); a pecking
                # bird looks down, so its facing is taken from where the beak is
                for mir in (False, True):
                    b = sc.placed(self.vb, fx + side * 60 * s, fy, mir, depth_y=B["depth"] + 4, eid=eb)
                    if SCN.PLACEMENT_REV >= 23:
                        b.k *= D.BIRD25
                    if (b.anchor("mouth")[0] - b.X) * side < 0:
                        break
                # the bird's front edge meets the sandwich's near end, so the lowered beak is at it
                bb_ = b.bbox()
                front = bb_[0] if side > 0 else bb_[2]
                b.X += (sbb[2] if side > 0 else sbb[0]) - side * 5 * s - front
            if not sc.fits(b.bbox(), limit=0.15, ignore=(ep,)):
                sc.remove(ep)
                continue
            sc.assets[eb] = b
            if SCN.PLACEMENT_REV >= 5:
                # a bite torn out of the near end, the torn-off piece in the beak and crumbs on the seat
                sw, sbb = D.sandwich(fx, fy, ss, bitten=side, style=sty)
                mx, my = b.anchor("mouth")
                sw += D.bread_bit(mx, my + 3 * s, ss, side)
                sw += "".join(D.circ(fx + side * (36 + 9 * i) * ss, fy - 2 * s, 2.2 * s, C["cream"], D.OW * 0.4) for i in range(3))
                sbb = (min(sbb[0], mx - 14 * s), min(sbb[1], my - 10 * s), max(sbb[2], mx + 14 * s), sbb[3])
            # revision 4: the beak goes into the sandwich, so the sandwich is drawn over it
            es = sc.svg(sc.eid("sandwich"), "Sandwich on the bench", sw, B["depth"] + 3.5, sbb, "scored")
            n, bn = sc.name(self.p), sc.name(self.b)
            self.act(self.p, "reading on the bench", ["reading", "reading a book", "sitting on the bench", "not paying attention"], "reading", [ep])
            it = self.ent(f"A {bn} is pecking at a sandwich on the bench", [f"{bn} eating the sandwich", f"{bn} on the bench", "bird pecking", "sandwich"], "sandwich", [eb, es], animate=True)
            it["type"] = "action"
            self.inf(f"The {bn} is stealing the sandwich while the {n} is busy reading", ["the bird is stealing the food", "she doesn't notice the bird", "the bird is eating her lunch", "he isn't watching his sandwich"],
                     "stealing", 2, cues=[eb, ep], effect=[es])
            return True
        return False


class LostBalloon(T):
    id = "lost_balloon"
    # v0.12 (revision 10): never with the storm pointer, who could be pointing at the balloon
    exclusive = ("sky_balloon",) if SCN.PLACEMENT_REV >= 10 else ()
    exclusive += ("calm_lost_balloon",) if SCN.PLACEMENT_REV >= 11 else ()     # nor with the gust (above)
    kind = "inference"
    settings = ("park", "street", "garden", "playground")
    units, content = 1, 2

    def bind(self):
        sc = self.sc
        self.p = sc.person(KIDS)
        # revision 5: an open-mouthed upset face (a worried face read as cheering)
        exprs = ["scared", "sad"] if SCN.PLACEMENT_REV >= 5 else ["sad", "scared", "worried"]
        # revision 7: holding a bunch of balloons in one hand and reaching up with the other for the one
        # that got away (one balloon above a reaching child was always "let go, or just floating past")
        self.vp = sc.need(self.p, "balloon_reach" if SCN.PLACEMENT_REV >= 7 else "reach_up", sc.rng.choice(exprs), 45)

    def place(self):
        sc = self.sc
        if SCN.PLACEMENT_REV >= 7:
            return _lost_balloon_place7(self)
        ep = sc.eid("balloonlost")
        for X, Y in self.stand_spots(n=120):
            want = sc.rng.choice([1, -1])
            p = sc.placed(self.vp, X, Y, sc.mirror_for(self.vp, want), eid=ep)
            if not sc.fits(p.bbox()):
                continue
            hx, hy = p.anchor("head_top")
            s = sz(Y)
            f = p.facing() or want
            if SCN.PLACEMENT_REV >= 6:
                # revision 6: just out of reach, the end of the string a little above the child's
                # fingers and drifting away (high in the sky, three readers found it "far from the child"
                # and twice the reaching read as cheering)
                hands = [p.anchor(k) for k in ("hand_L_grip", "hand_R_grip") if p.has_anchor(k)]
                htop = min(h[1] for h in hands) if hands else hy - 40 * s
                hxm = sum(h[0] for h in hands) / len(hands) if hands else hx
                send = (hxm + f * sc.rng.uniform(16, 36) * s, htop - sc.rng.uniform(30, 50) * s)
                bs = self.k3(1.15, 0.95, 0.8)
                bx, by = send[0] + f * 26 * s, send[1] - (38 + 95) * bs * s
                if by < 70:
                    continue
                svg, bb = D.balloon(bx, by, bs * s, sc.rng.choice([C["red"], C["yellow"], C["purple"]]), string_to=send)
            else:
                bx = hx + f * sc.rng.uniform(70, 170) * s
                # high in the sky: well above the child and above the fence, hedge or shop awnings behind
                by = min(hy - sc.rng.uniform(250, 340) * s, sc.S.horizon - sc.rng.uniform(220, 300))
                if SCN.PLACEMENT_REV >= 4 and "balloon_max_y" in sc.S.anchors:
                    by = min(by, sc.S.anchors["balloon_max_y"])      # the string must end clear of the awnings
                if by < 70:
                    continue
                svg, bb = D.balloon(bx, by, self.k3(1.25, 0.95, 0.75), sc.rng.choice([C["red"], C["yellow"], C["purple"]]),
                                    string_to=(bx - f * 18, by + 115 * s), string_len=90)
            # revision 3: keep the air under the loose string free, so the string never seems to end
            # at someone else's head or hat (it read as that person's balloon)
            res = bb if SCN.PLACEMENT_REV < 3 else (bb[0] - 14 * s, bb[1], bb[2] + 14 * s, bb[3] + 110 * s)
            if SCN.PLACEMENT_REV >= 6:
                res = (bb[0] - 14 * s, bb[1], bb[2] + 14 * s, bb[3])
            elif SCN.PLACEMENT_REV >= 4:
                # and the column of air between the balloon and the child, so no one else stands under
                # it reaching up (a second child there read as the owner)
                res = (min(res[0], hx - 30 * s), res[1], max(res[2], hx + 30 * s), max(res[3], hy - 10 * s))
            if not sc.fits(res, limit=0.03):
                continue
            # the loose string may not end at anything at all (a clothesline, a lamp, a roof): from
            # revision 4 the air under it must be clear of the setting's structures too
            if SCN.PLACEMENT_REV >= 4 and not sc.air_clear(res):
                continue
            if SCN.PLACEMENT_REV >= 9 and not sc.setting_clear((bb[0] - 40 * s, bb[1] - 20 * s, bb[2] + 40 * s, bb[3]), only=HAT_STRUCT9):
                # revision 9: well clear of standing structures, not just off them (a balloon floating beside
                # the lamp post's head could be caught on it)
                continue
            if SCN.PLACEMENT_REV >= 9:
                # and of everyone else (a balloon just escaped beside a catcher's legs)
                g9 = (bb[0] - 50 * s, bb[1] - 30 * s, bb[2] + 50 * s, bb[3] + 30 * s)
                if any(sc.overlap(g9, q.bbox()) > 0 for q in sc.assets.values() if q.family.startswith("person.")):
                    continue
            if SCN.PLACEMENT_REV >= 5:
                # nothing else to react to close by: no animal or other person beside the child (one
                # reaching up next to a goat read as cheering at the goat)
                pb = p.bbox()
                zone = (pb[0] - 150 * s, pb[1] - 40 * s, pb[2] + 150 * s, pb[3] + 30 * s)
                if any(min(q.bbox()[2], zone[2]) > max(q.bbox()[0], zone[0]) and min(q.bbox()[3], zone[3]) > max(q.bbox()[1], zone[1])
                       for q in sc.assets.values()):
                    continue
                sc.airzones.append(zone)
            sc.assets[ep] = p
            if SCN.PLACEMENT_REV >= 4:
                sc.airzones.append(res)     # and no one placed later stands under the string
            if SCN.PLACEMENT_REV >= 9:
                sc.airzones.append((bb[0] - 50 * s, bb[1] - 30 * s, bb[2] + 50 * s, bb[3] + 30 * s))   # nor beside the balloon
            sc.checks[f"{ep}_looks_at_balloon"] = sc.gaze_ok(p, (bb[0] - 30, bb[1] - 30, bb[2] + 30, bb[3] + 30))
            eb = sc.svg(sc.eid("loosebal"), "Balloon floating away", svg, 1500, res, "scored")   # high in the air: drawn over everything
            n = sc.name(self.p)
            self.act(self.p, "reaching up, upset", ["reaching up", "crying", "upset", "sad", "trying to catch the balloon"], "reaching", [ep])
            self.ent("A balloon is floating up into the sky", ["balloon flying away", "balloon in the sky", "balloon", "floating balloon"], "balloon", [eb])
            self.inf(f"The {n} let go of the balloon", ["the child lost the balloon", "the balloon got away", "let go of the string", "the balloon flew away from them"],
                     "lost", 1, cues=[eb, ep], effect=[eb])
            return True
        return False


def _lost_balloon_place7(self):
    """Revision 7: a bunch of two balloons on strings gathered in the hand held out behind, and a third
    rising just out of reach of the other hand, its string trailing down toward the fingers."""
    sc = self.sc
    ep = sc.eid("balloonlost")
    for X, Y in self.stand_spots(n=140):
        want = sc.rng.choice([1, -1])
        p = sc.placed(self.vp, X, Y, sc.mirror_for(self.vp, want), eid=ep)
        if not sc.fits(p.bbox()):
            continue
        s = sz(Y)
        f = p.facing() or want
        bs = self.k3(1.05, 0.9, 0.8)
        hold = p.anchor("strings_at") if p.has_anchor("strings_at") else p.anchor("hand_R_grip")
        hands = [p.anchor(k) for k in ("hand_L_grip", "hand_R_grip") if p.has_anchor(k)]
        reach = min(hands, key=lambda h: h[1])
        hx, hy = p.anchor("head_top")
        cols = [C["red"], C["yellow"], C["purple"], C["blue"]]
        sc.rng.shuffle(cols)
        if SCN.PLACEMENT_REV >= 13 and cols[2] == C["yellow"] and any(v[1] in ("balloon", "walk_balloon") for v in sc.variants):
            # revision 13: the balloon that got away is never the colour of another child's balloon (the yellow one
            # held elsewhere: the loose yellow balloon "could belong to someone other than the girl")
            cols[2], cols[0] = cols[0], cols[2]
        # the bunch, above and behind the holding hand
        rise = sc.rng.uniform(150, 175) * bs * s
        b1 = (hold[0] - f * 8 * s, hold[1] - rise)
        b2 = (hold[0] - f * 58 * bs * s, hold[1] - rise + 34 * bs * s)
        bunch, bbb = "", None
        for (bx_, by_), col in ((b2, cols[1]), (b1, cols[0])):
            g, gb = D.balloon(bx_, by_, bs * s, col, string_to=hold)
            bunch += g
            bbb = gb if bbb is None else (min(bbb[0], gb[0]), min(bbb[1], gb[1]), max(bbb[2], gb[2]), max(bbb[3], gb[3]))
        # the strings may not cross the head
        hc = (hx, hy + 30 * s)
        if any(_seg_near((bx_, by_ + 38 * bs * s), hold, hc, 34 * s) for bx_, by_ in (b1, b2)):
            continue
        # the loose one: just out of reach above the reaching hand, drifting away
        send = (reach[0] + f * sc.rng.uniform(10, 24) * s, reach[1] - sc.rng.uniform(28, 42) * s)
        lx, ly = send[0] + f * 24 * s, send[1] - (38 + 92) * bs * s
        if ly < 70 or min(b1[1], b2[1]) - 36 * bs * s < 40:
            continue
        loose, lbb = D.balloon(lx, ly, bs * s, cols[2], string_to=send)
        if sc.overlap(lbb, bbb) > 0:
            continue
        res = (lbb[0] - 14 * s, lbb[1], lbb[2] + 14 * s, lbb[3])
        if not sc.fits(res, limit=0.03) or not sc.fits(bbb, limit=0.03, ignore=(ep,)):
            continue
        if not sc.air_clear(res) or not sc.air_clear(bbb):
            continue
        pb = p.bbox()
        zone = (pb[0] - 150 * s, pb[1] - 40 * s, pb[2] + 150 * s, pb[3] + 30 * s)
        if any(min(q.bbox()[2], zone[2]) > max(q.bbox()[0], zone[0]) and min(q.bbox()[3], zone[3]) > max(q.bbox()[1], zone[1])
               for q in sc.assets.values()):
            continue
        # nor in front of the fruit stall: a balloon over the stall seemed tied to it, and the reaching
        # hand seemed to take fruit from the crates
        stall = sc.S.anchors.get("stall")
        if stall and any(sc.overlap(b, stall["bbox"]) > 0 for b in (zone, res, bbb)):
            continue
        sc.airzones.append(zone)
        sc.assets[ep] = p
        sc.airzones += [res, bbb]
        sc.checks[f"{ep}_looks_at_balloon"] = sc.gaze_ok(p, (lbb[0] - 30, lbb[1] - 30, lbb[2] + 30, lbb[3] + 30))
        eh = sc.svg(sc.eid("heldbal"), "Balloons held by the child", bunch, 1499, bbb, "scored")
        eb = sc.svg(sc.eid("loosebal"), "Balloon floating away", loose, 1500, res, "scored")
        n = sc.name(self.p)
        self.act(self.p, "holding balloons and reaching up for one, upset", ["reaching up", "holding balloons", "upset", "sad", "trying to catch the balloon"], "reaching", [ep, eh])
        self.ent("A balloon is floating up into the sky", ["balloon flying away", "balloon in the sky", "balloon floating away", "floating balloon"], "balloon", [eb])
        self.inf(f"The {n} let go of one of the balloons", ["one balloon got away", "lost one of the balloons", "the balloon slipped away",
                                                           "let go of the string", "one floated away from the bunch"],
                 "lost", 1, cues=[eb, ep, eh], effect=[eb])
        return True
    return False


def _seg_near(a, b, c, r):
    """Does the segment a-b pass within r of point c?"""
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy or 1.0
    t = max(0.0, min(1.0, ((c[0] - ax) * dx + (c[1] - ay) * dy) / L))
    return math.hypot(ax + t * dx - c[0], ay + t * dy - c[1]) < r


class DucksBread(T):
    id = "ducks_bread"
    exempt_extra = ("pond",)      # revision 10: stands at the water's edge on purpose
    kind = "inference"
    settings = ("park",)
    units, content = 1, 2

    def bind(self):
        sc = self.sc
        self.p = sc.person(None)
        self.vp = sc.need(self.p, "feed_birds", sc.rng.choice(["smile", "happy", "content"]), 90)
        self.d = sc.animal(["duck"])
        self.vd = sc.need(self.d, "swim", "neutral", 90)

    def place(self):
        sc = self.sc
        A = sc.S.anchors["pond"]
        ep, ed = sc.eid("duckfeeder"), sc.eid("hungryduck")
        for (x, y) in A["shore"]:
            want = 1 if A["center"][0] > x else -1
            p = sc.try_put(ep, self.vp, [(x, y), (x + 25, y + 15)], want_face=want, limit=0.15)
            if not p:
                continue
            sx, sy = p.anchor("seed_from")
            for (dx, dy) in sorted(A["swim"], key=lambda q: abs(q[0] - (x + want * 220))):
                d = sc.placed(self.vd, dx, dy, sc.mirror_for(self.vd, -want), eid=ed)
                if (dx - x) * want < 80 or not sc.fits(d.bbox(), limit=0.05):
                    continue
                if SCN.PLACEMENT_REV >= 16:
                    # revision 16: the wake's lines and the water just past them clear of every figure, and kept clear of
                    # later ones (the wake ran "to just above the man's head" of a picnicker on the shore)
                    wz = tuple(sorted((dx + want * 20, dx + want * 120))) 
                    wz = (wz[0], dy - 20, wz[1], dy + 50)
                    if any(min(wz[2], b[2]) > max(wz[0], b[0]) and min(wz[3], b[3]) > max(wz[1], b[1])
                           for k_, q_ in sc.assets.items() if k_ not in (ep, ed) for b in (q_.bbox(),)):
                        continue
                    sc.airzones.append(wz)
                sc.assets[ed] = d
                # (revision 24: bread-coloured; the orange-brown bits "could be food ... or small stones or tiny fish")
                crumb_c = C["cream"] if SCN.PLACEMENT_REV >= 24 else C["wood_light"]
                crumbs = "".join(D.ell(sx + want * (30 + i * 22), sy + 30 + (i % 2) * 18 + i * 10, 6, 4, crumb_c, D.OW * 0.5) for i in range(5))
                # the wake trails behind the duck, on the side away from the shore it swims to
                wake = f'<path d="M {D.P(dx + want * 30, dy + 4)} q {want * 30:.1f} 6 {want * 60:.1f} 14 M {D.P(dx + want * 30, dy + 8)} q {want * 26:.1f} 14 {want * 50:.1f} 26" fill="none" stroke="{C["white"]}" stroke-width="3"/>'
                if SCN.PLACEMENT_REV >= 8:
                    # revision 8: crumbs already floating on the water just ahead of the duck's bill (the duck
                    # "swimming toward the food" was not said to be coming to eat it)
                    db = d.bbox()
                    front = db[0] if want > 0 else db[2]
                    crumbs += "".join(D.ell(front - want * (8 + i * 15), dy - 3 + (i % 2) * 4, 6, 3.5, crumb_c, D.OW * 0.5) for i in range(3))
                ec = sc.svg(sc.eid("crumbs"), "Bread crumbs flying toward the water", crumbs + wake, -64, (min(sx, dx) - 40, sy, max(sx, dx) + 40, dy + 30), "scored")
                if SCN.PLACEMENT_REV >= 4:      # the wake now trails on the far side of the duck
                    sc.svgs[ec]["bbox"] = (min(sx, dx - 100), sy, max(sx, dx + 100), dy + 30)
                self.act(self.p, "throwing bread to the ducks", ["feeding the ducks", "throwing bread", "feeding the birds", "bread"], "bread", [ep, ec])
                it = self.ent("A duck is swimming toward the shore", ["duck", "duck swimming", "ducks in the pond"], "duck", [ed], animate=True)
                it["type"] = "action"
                self.inf("The duck is coming to eat the bread", ["the duck wants the bread", "the ducks are hungry", "the duck is swimming over for food"],
                         "hungry", 1, cues=[ed, ec], effect=[ec])
                return True
            sc.remove(ep)
        return False


# ---------------------------------------------------------------- v0.5 inference modules
class SeesawHeavy(SeesawPlay):
    """A grown-up sits on the low end of the seesaw; a child is stuck high in the air on the other end."""
    id = "seesaw_heavy"
    kind = "inference"
    units, content = 1, 2

    def bind(self):
        sc = self.sc
        # the biggest grown-ups and the smallest child make the weight difference plain to see
        if SCN.PLACEMENT_REV >= 7:
            # revision 7: a plainly grown, heavy man (the youngest man read as "a boy"), sitting on the low
            # end reading, while the child up in the air calls out: ordinary seesaws now tip toward the
            # heavier rider too, so the tilt alone no longer says that anyone is stuck
            self.a = sc.person(ADULTS, avoid=("person.ben",), prefer=("person.dev", "person.tomas"))
            self.b = sc.person(KIDS, prefer=("person.nia",))
            self.va = sc.need(self.a, "seesaw_low_read", sc.rng.choice(["content", "focused"]), 90)
            # revision 12: the girl's legs hang straight down, her face turned to us, one hand gripping the handle and
            # the other arm reaching out to the man (bent over the handle with her knees bent, her face showed only
            # hair: "sits on the raised end ... nothing looks wrong there")
            # (revision 14: always calling, the mouth open toward us; v0.16 bench: with her head turned along the plank to
            # look down at him, her face was hidden)
            self.vb = sc.need(self.b, "seesaw_stuck_call" if SCN.PLACEMENT_REV >= 12 else "seesaw_stuck",
                              "calling" if SCN.PLACEMENT_REV >= 14 else sc.rng.choice(["calling", "scared"]), 90)
            return
        self.a = sc.person(ADULTS, prefer=("person.dev", "person.ben"))
        self.b = sc.person(KIDS, prefer=("person.nia",))
        if SCN.PLACEMENT_REV >= 5:
            # revision 5: the grown-up sits low and at ease with arms crossed; the child, high up, grips
            # the handle with both hands, legs dangling, looking down worried (the tilt alone was
            # described but never explained by weight)
            self.va = sc.need(self.a, "seesaw_low", sc.rng.choice(["content", "smile", "bored"]), 90)
            self.vb = sc.need(self.b, "seesaw_stuck", sc.rng.choice(["scared", "worried"]), 90)
        else:
            self.va = sc.need(self.a, "sit_ground", sc.rng.choice(["smile", "bored", "neutral"]), 90)
            self.vb = sc.need(self.b, "sit", sc.rng.choice(["scared", "worried", "surprised"]), 90)

    def place(self):
        sc = self.sc
        ea, eb = sc.eid("heavyend"), sc.eid("stuckkid")
        A = sc.S.anchors["seesaw"]
        tilt = self.k3(21, 19, 17)
        if SCN.PLACEMENT_REV >= 5:
            tilt = math.degrees(math.asin(82 / 212))      # the low end resting on the ground
        # the grown-up takes the low end (left when the right end is up), the child the high end
        if not self.ride(tilt, ea, eb, self.va, self.vb):
            return False
        an, bn = sc.name(self.a), sc.name(self.b)
        if SCN.PLACEMENT_REV >= 12:
            # revision 12: short swing arcs by her dangling feet: kicking her legs, stuck up there
            # (v0.16 bench: without them, three of three readers saw nothing wrong: "the tilt makes sense", "she seems to be
            # smiling")
            q = sc.assets[eb]
            if q.has_anchor("foot_L") and q.has_anchor("foot_R") and q.has_anchor("seat"):
                s = sz(A["depth"])
                sx_, sy_ = q.anchor("seat")
                kick, xs, ys = "", [], []
                for f_ in ("foot_L", "foot_R"):
                    fx, fy = q.anchor(f_)
                    R = math.hypot(fx - sx_, fy - sy_) + 9 * s
                    a0 = math.atan2(fy - sy_, fx - sx_)
                    p0 = (sx_ + R * math.cos(a0 - 0.30), sy_ + R * math.sin(a0 - 0.30))
                    p1 = (sx_ + R * math.cos(a0 + 0.30), sy_ + R * math.sin(a0 + 0.30))
                    kick += f'<path d="M {D.P(*p0)} A {R:.1f} {R:.1f} 0 0 1 {D.P(*p1)}" fill="none" stroke="{D.OUT}" stroke-width="{2.4 * s:.1f}" stroke-linecap="round" stroke-opacity="0.75"/>'
                    xs += [p0[0], p1[0]]; ys += [p0[1], p1[1]]
                sc.svg(sc.eid("kicklines"), "Motion lines by the dangling feet", kick, A["depth"] + 3, (min(xs) - 4, min(ys) - 4, max(xs) + 4, max(ys) + 4), "setting")
        if SCN.PLACEMENT_REV >= 7:
            self.act(self.a, "sitting on the low end of the seesaw, reading", ["sitting on the seesaw", "reading on the seesaw", "sitting on the low end", "reading a book"], "seesaw", [ea])
            self.act(self.b, "stuck up in the air on the seesaw, calling out", ["up in the air", "stuck at the top", "calling out", "shouting", "scared", "can't get down"], "air", [eb])
            self.inf(f"The {an} is much heavier, so the {bn} is stuck up in the air",
                     [f"the {an} is too heavy", "the grown-up is heavier", "the child can't get down", "stuck because he is sitting on the other end",
                      "the seesaw won't go up and down", "too heavy for the seesaw", "he isn't noticing she's stuck"],
                     "heavy", 1, cues=[eb, ea], effect=[eb])
            return True
        self.act(self.a, "sitting on the low end of the seesaw", ["sitting on the seesaw", "on the seesaw", "sitting on the ground end"], "seesaw", [ea])
        self.act(self.b, "stuck up in the air on the seesaw", ["up in the air", "stuck at the top", "on the seesaw", "scared", "can't get down"], "air", [eb])
        self.inf(f"The {an} is much heavier, so the {bn} is stuck up in the air",
                 [f"the {an} is too heavy", "the grown-up is heavier", "the child can't get down", "the seesaw won't go up and down", "too heavy for the seesaw"],
                 "heavy", 1, cues=[eb, ea], effect=[eb])
        return True


class DogWantsWalk(T):
    """A dog sits by the back door with its leash in its mouth."""
    id = "dog_wants_walk"
    kind = "inference"
    settings = ("garden",)
    exclusive = ("door",)
    units, content = 1, 1

    def bind(self):
        sc = self.sc
        # revision 6: the larger brown dog (the small white dog sitting at the door read as a cat)
        self.d = sc.animal(["dog"], prefer=("animal.dog_01",) if SCN.PLACEMENT_REV >= 6 else ())
        # facing the viewer: compact, so it fits on the step in front of the door
        # revision 24: open eyes (the happy face closes them: "with its eyes shut", "its eyes are shut, which could mean happy or asleep",
        # and its wish for a walk went unstated, the gate's lowest template in v0.25)
        self.vd = sc.need(self.d, "sit", "neutral" if SCN.PLACEMENT_REV >= 24 else sc.rng.choice(["happy", "neutral"]), 0)

    def place(self):
        sc = self.sc
        ed = sc.eid("waitingdog")
        rev14 = SCN.PLACEMENT_REV >= 14
        for X in ((190, 180, 200, 175, 210, 225, 240) if rev14 else (225, 240, 255, 210, 270)):
            Y = 806
            d = sc.placed(self.vd, X, Y, False, eid=ed)
            if not sc.fits(d.bbox(), limit=0.10):
                continue
            if rev14:
                # revision 14: the dog's head clear of the door knob (drawn at its ear, the knob read as "an ear tag" or
                # "a tag or ball")
                b = d.bbox()
                if b[0] - 18 <= 250 <= b[2] + 18 and b[1] - 18 <= 670 <= b[3] + 18:
                    continue
            mx, my = d.anchor("mouth")
            s = sz(Y)
            # leash: from the mouth down to a loop lying on the ground
            gy = Y + 6
            lx = mx + 46 * s
            leash = f'<path d="M {D.P(mx, my)} C {D.P(mx + 6 * s, my + 40 * s)} {D.P(lx - 30 * s, gy - 4)} {D.P(lx, gy - 2)}" fill="none" stroke="{D.OUT}" stroke-width="{6 * s + 2:.1f}" stroke-linecap="round"/>'
            leash += f'<path d="M {D.P(mx, my)} C {D.P(mx + 6 * s, my + 40 * s)} {D.P(lx - 30 * s, gy - 4)} {D.P(lx, gy - 2)}" fill="none" stroke="{C["red"]}" stroke-width="{6 * s:.1f}" stroke-linecap="round"/>'
            leash += D.ell(lx + 18 * s, gy - 2, 20 * s, 7 * s, "none", D.OW * 0.6) + f'<ellipse cx="{lx + 18 * s:.1f}" cy="{gy - 2:.1f}" rx="{20 * s:.1f}" ry="{7 * s:.1f}" fill="none" stroke="{C["red"]}" stroke-width="{4 * s:.1f}"/>'
            el_bb = (mx - 10, my - 6, lx + 42 * s, gy + 8)
            if not sc.fits(el_bb, limit=0.05, ignore=(ed,)):
                continue
            sc.assets[ed] = d
            el = sc.svg(sc.eid("leash"), "Leash in the dog's mouth", leash, Y + 1, el_bb, "scored")
            dn = sc.name(self.d)
            it = self.ent(f"A {dn} is sitting by the door with its leash in its mouth",
                          [f"{dn} with a leash", f"{dn} holding a leash", f"{dn} by the door", "leash in its mouth"], "leash", [ed, el], animate=True)
            it["type"] = "action"
            self.inf(f"The {dn} wants to go for a walk", [f"the {dn} wants a walk", "wants to go out", "waiting to be taken for a walk", "asking for a walk"],
                     "walk", 1, cues=[ed, el, "house"], effect=[ed])
            return True
        return False


MODULES = [BlockedHose, RainComing, CatStalksBird, StuckInTree, KiteInTree, IceCreamDrop, AboutToTrip, DogBegs, SprinklerPackage,
           PaintTracks, WindyHat, BirdSteals, LostBalloon, DucksBread, SeesawHeavy, DogWantsWalk]
for _c in MODULES:
    _c.kind = "inference"


# ============================================================================ contradictions
class WaterUpward(WaterFlowers):
    id = "water_upward"
    kind = "contradiction"
    domain = "physical"
    upward = True
    units, content = 1, 1

    def items(self, ep, ew):
        self.act(self.p, "watering the flowers", ["watering the flowers", "watering the plants", "watering can"], "flowers", [ep])
        self.contra("Something is wrong with the water from the watering can",
                    "The water is going up into the air instead of falling down onto the flowers",
                    ["the water is weird", "something's wrong with the water", "that's not right"],
                    ["water going up", "water going the wrong way", "water should fall down", "water flowing upward"], "water", [ew])


class PanWatering(WaterFlowers):
    id = "pan_watering"
    kind = "contradiction"
    domain = "functional"
    pose = "water_pan"
    # revision 6: a short pour from the pan (a long steady stream read as coming from a hose)
    stream_cap = 120.0
    units, content = 1, 1
    # revision 17: no hose and no hose reel in the picture (beside the reel the pan read as "a hose nozzle or watering wand")
    exclusive = ("flowers",) + (("hose_reel",) if SCN.PLACEMENT_REV >= 17 else ())

    @classmethod
    def feasible(cls, setting, sky):
        # revision 20: not in the street, where the planter stands in front of a slate-grey shop door: held up against it
        # at the planter's height, the pan read as "a grey watering can" (in the garden and the park, over a flower bed on
        # the ground, it read as a frying pan in every screened picture)
        if SCN.PLACEMENT_REV >= 20 and setting == "street":
            return False
        return super().feasible(setting, sky)

    def items(self, ep, ew):
        self.act(self.p, "watering the flowers", ["watering the flowers", "watering the plants", "pouring water"], "flowers", [ep, ew])
        self.contra("Something is wrong with what the person is watering with",
                    "The person is watering the flowers with a frying pan instead of a watering can",
                    ["something odd about the pan", "that's strange", "the watering can is wrong"],
                    ["watering with a frying pan", "using a pan to water", "a pan isn't for watering"], "pan", [ep])


class SweepFork(Sweep):
    id = "sweep_fork"
    kind = "contradiction"
    domain = "functional"
    pose = "sweep_fork"
    units, content = 1, 1

    def bind(self):
        # revision 5: a giant dining fork swept low across the body (the upright fork read as a garden
        # fork someone leaned on); revision 6: a giant dinner fork with cutlery proportions (the thin
        # pole with a small head read as a rake), with open eyes on the task
        if SCN.PLACEMENT_REV >= 6:
            sc = self.sc
            self.pose = "sweep_giant_fork"
            self.p = sc.person(GROWN)
            self.vp = sc.need(self.p, self.pose, sc.rng.choice(["focused", "neutral"]), 45)
            return
        if SCN.PLACEMENT_REV >= 5:
            self.pose = "sweep_dinner_fork"
        super().bind()

    def pile_geom(self, p):
        """Revision 6: a heap of grey dust and grit swept ahead of the tines, a cloud of dust over it
        and sweep marks behind (leaves in v0.7 made it raking; the first heap was too small to see)."""
        fx, fy = p.anchor("fork_tip")
        s = sz(p.Y) * 1.7
        ms = sz(p.Y)
        f = 1 if fx > p.X else -1
        px = fx + f * 24 * s
        pile = "".join(f'<circle cx="{px + dx * s:.1f}" cy="{p.Y + dy * s:.1f}" r="{r * s:.1f}" fill="#b9b2a4" fill-opacity="0.55"/>'
                       for dx, dy, r in ((-14, -15, 8), (-1, -21, 10), (13, -16, 8), (22, -8, 6), (-22, -7, 5)))
        pile += (f'<path d="M {D.P(px - 22 * s, p.Y + 3 * s)} q {22 * s:.1f} {-18 * s:.1f} {44 * s:.1f} 0 z" fill="{C["gray"]}" '
                 f'stroke="{D.OUT}" stroke-width="{D.OW * 0.6:.1f}" stroke-linejoin="round"/>')
        for k, (dx, dy) in enumerate(((-12, -2), (-5, -6), (3, -3), (10, -7), (16, -1), (-1, 0), (7, 1), (-17, 1), (-8, -9), (12, -11))):
            pile += f'<circle cx="{px + dx * s:.1f}" cy="{p.Y + dy * s:.1f}" r="{(1.4 + (k % 3) * 0.5) * s:.1f}" fill="{C["brown"] if k % 2 else C["charcoal"]}"/>'
        if SCN.PLACEMENT_REV >= 8:
            # revision 8: no white chips (with them the heap read as rubble, the fork as breaking the path);
            # a dustpan waits beyond the heap
            pan, pbb = D.dustpan(px + f * (36 if SCN.PLACEMENT_REV >= 9 else 52) * s, p.Y + 2 * ms, ms * 1.25, f)   # revision 9: its lip at the heap
            pile += pan
        else:
            pile += D.poly([(px + 5 * s, p.Y - 9 * s), (px + 13 * s, p.Y - 11 * s), (px + 14 * s, p.Y - 5 * s), (px + 6 * s, p.Y - 4 * s)], C["white"], D.OW * 0.45)
            pile += D.poly([(px - 14 * s, p.Y - 4 * s), (px - 8 * s, p.Y - 7 * s), (px - 6 * s, p.Y - 2 * s)], C["white"], D.OW * 0.45)
        marks = "".join(f'<path d="M {D.P(fx - f * (12 + 10 * k) * ms, p.Y + (2 + 3 * k) * ms)} q {-f * 22 * ms:.1f} {-4 * ms:.1f} {-f * 46 * ms:.1f} 0" fill="none" stroke="{D.OUT}" stroke-width="2" stroke-opacity="0.45" stroke-linecap="round"/>' for k in range(3))
        bb = (min(px - 28 * s, fx - f * 80 * ms), p.Y - 32 * s, max(px + 30 * s, fx - f * 80 * ms), p.Y + 4 * ms)
        if SCN.PLACEMENT_REV >= 8:
            bb = (min(bb[0], pbb[0]), bb[1], max(bb[2], pbb[2]), max(bb[3], pbb[3]))
        return pile, marks, bb

    def place(self):
        if SCN.PLACEMENT_REV < 6:
            return super().place()
        # revision 6: on the path or pavement, with the dust heap ahead of the tines reserved as part of
        # the event (a heap that did not fit was simply left out, and a fork with nothing swept is a rake)
        from .settings import on_path
        sc = self.sc
        A = sc.S.anchors.get("path")
        if A:
            cands = [q for q in self.stand_spots(x_range=(A["x0"] - 60, A["x1"] + 60), y_range=(A["y0"], A["y1"]), n=120) if on_path(A, q[0], q[1], 14)]
        else:
            cands = self.stand_spots(n=100)
        ep = sc.eid("sweeper")

        def extras(p):
            fx, _ = p.anchor("fork_tip")
            if A and not on_path(A, fx, p.Y, 6):
                return None
            pb = self.pile_geom(p)[2]
            if SCN.PLACEMENT_REV >= 8 and A:
                # revision 8: the heap itself on the paving too (on the grass it read as a dug-up clod)
                f_ = 1 if fx > p.X else -1
                if not on_path(A, fx + f_ * 24 * sz(p.Y) * 1.7, p.Y, 10):
                    return None
            if SCN.PLACEMENT_REV >= 8:
                # revision 8: the tines and the dust on plain paving, clear of the stepping stones (sweeping
                # among the stones read as jabbing at them, a digging tool)
                for st in A.get("stones", ()) if A else ():
                    g = (st[0] - 14, st[1] - 12, st[2] + 14, st[3] + 12)
                    if sc.overlap(pb, g) > 0 or (g[0] <= fx <= g[2] and g[1] - 20 <= p.Y <= g[3] + 20):
                        return None
            return [pb]
        f0 = sc.rng.choice([1, -1])
        p = self.place_with(ep, self.vp, cands, want_face=f0, extras=extras, xlimit=0.08) or \
            self.place_with(ep, self.vp, cands, want_face=-f0, extras=extras, xlimit=0.08)
        if not p:
            return False
        self.items(ep)
        return True

    def items(self, ep):
        sc = self.sc
        if SCN.PLACEMENT_REV >= 6:
            pile, marks, bb = self.pile_geom(sc.assets[ep])
            sc.svg(sc.eid("sweptpile"), "Swept-up dust and grit", pile + marks, sc.assets[ep].Y + 1, bb, "setting")
            self.act(self.p, "sweeping", ["sweeping", "sweeping the path", "sweeping the ground", "cleaning"], "sweeping", [ep])
            self.contra("Something is wrong with what the person is sweeping with",
                        "The person is sweeping with a giant fork instead of a broom",
                        ["the broom is strange", "something's wrong with the broom", "that's odd", "a fork is not for sweeping"],
                        ["sweeping with a fork", "a fork instead of a broom", "you can't sweep with a fork", "a giant fork", "a huge dinner fork"], "fork", [ep])
            return
        if SCN.PLACEMENT_REV >= 5:
            # a small pile of leaves and dust pushed ahead of the tines, with sweep marks behind them
            p = sc.assets[ep]
            fx, fy = p.anchor("fork_tip")
            s = sz(p.Y)
            f = 1 if fx > p.X else -1
            px = fx + f * 30 * s
            # a loose heap of leaves with a puff of dust over it (on a pale base the heap read as a plate)
            pile = ""
            for i, (dx, dy, col) in enumerate(((-18, -3, "orange"), (-6, -9, "grass_dark"), (8, -4, "wood"), (2, 0, "orange"), (-12, 2, "grass_dark"),
                                                (16, -1, "yellow"), (-1, -14, "wood"), (12, -10, "orange"))):
                pile += D.ell(px + dx * s, p.Y + dy * s, 7.5 * s, 3.8 * s, C[col], D.OW * 0.5, rot=35 * (i - 3))
            pile = "".join(f'<circle cx="{px + dx * s:.1f}" cy="{p.Y + dy * s:.1f}" r="{r * s:.1f}" fill="#b9b2a4" fill-opacity="0.45"/>'
                           for dx, dy, r in ((-20, -18, 9), (-6, -24, 11), (10, -20, 9), (22, -12, 7))) + pile
            marks = "".join(f'<path d="M {D.P(fx - f * (14 + 10 * k) * s, p.Y + (2 + 3 * k) * s)} q {-f * 22 * s:.1f} {-4 * s:.1f} {-f * 46 * s:.1f} 0" fill="none" stroke="{D.OUT}" stroke-width="2" stroke-opacity="0.45" stroke-linecap="round"/>' for k in range(3))
            bb = (min(px - 32 * s, fx - f * 80 * s), p.Y - 16 * s, max(px + 32 * s, fx - f * 80 * s), p.Y + 14 * s)
            if sc.fits(bb, limit=0.08, ignore=(ep,)):
                sc.svg(sc.eid("sweptpile"), "Swept-up leaves and dust", pile + marks, p.Y + 1, bb, "setting")
        self.act(self.p, "sweeping", ["sweeping", "sweeping the path", "cleaning"], "sweeping", [ep])
        self.contra("Something is wrong with what the person is sweeping with",
                    "The person is sweeping with a giant fork instead of a broom",
                    ["the broom is strange", "something's wrong with the broom", "that's odd"],
                    ["sweeping with a fork", "a fork instead of a broom", "you can't sweep with a fork"], "fork", [ep])


class BucketHat(T):
    id = "bucket_hat"
    kind = "contradiction"
    domain = "functional"
    units, content = 1, 1

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.vp = sc.need(self.p, "bucket_hat", sc.rng.choice(["content", "smile", "neutral"]), 45)

    def place(self):
        sc = self.sc
        ep = sc.eid("buckethead")
        if not sc.try_put(ep, self.vp, self.stand_spots(), want_face=sc.rng.choice([1, -1])):
            return False
        self.act(self.p, "standing with hands on hips", ["standing", "standing there", "hands on hips"], "standing", [ep])
        self.contra("Something is wrong with what the person has on their head",
                    "The person is wearing a bucket as a hat",
                    ["funny hat", "something on his head", "that's strange"], ["bucket on the head", "wearing a bucket", "a bucket is not a hat"], "bucket", [ep])
        return True


class FloatingBox(T):
    id = "floating_box"
    kind = "contradiction"
    domain = "physical"
    exclusive = ("box_prop", "wind")     # nor under a gust of wind, which would explain it
    # not on the playground: its frames leave no clear air at eye level, and a box beside a slide or a
    # swing read as resting on it
    settings = ("garden", "park", "street")
    units, content = 1, 1

    def bind(self):
        pass

    def place(self):
        sc = self.sc
        for X, Y in self.stand_spots(y_range=(sc.S.horizon + 110, sc.S.horizon + 240), n=80):
            s = sz(Y)
            k = s * self.k3(1.35, 1.05, 0.85)
            # the box hangs at about eye level (the horizon), so its underside shows; lower down it
            # read as a box standing further back on the ground
            lift = max(120 * s, Y - (sc.S.horizon + 12))
            if SCN.PLACEMENT_REV >= 10 and "fence_top" in sc.S.anchors:
                # revision 10: in the garden the box hangs above the fence, against the trees beyond it
                # (with its bottom edge at the foot of the fence it read as "tipped over and resting at the
                # foot of the fence"; in front of the boards it could hang on them)
                lift = max(lift, Y - (sc.S.anchors["fence_top"]["y"] - 75))
                tl = [e["bbox"][1] for e in sc.S.elements if e["id"] == "tree_line" and e.get("bbox")]
                if SCN.PLACEMENT_REV >= 11 and tl:
                    # revision 11: and clear above the row of trees beyond the fence, in open sky (its lower edge on
                    # the treetops read as "resting at a tilt on top of the hedge")
                    lift = max(lift, Y - (min(tl) - 40 - 26 * k))
            # revision 11: no ground shadow under a box raised high (it read as a shadow with nothing above it)
            svg, bb = D.floating_crate(X, Y, k, lift=lift, col=sc.rng.choice([C["wood_light"], C["khaki"]]), tilt=sc.rng.choice([-1, 1]) * self.k3(16, 12, 9),
                                       ground_shadow=SCN.PLACEMENT_REV < 11 or lift < 160 * s)
            if bb[1] < 40 or not sc.fits((bb[0], bb[1], bb[2], Y), limit=0.03):
                continue
            if SCN.PLACEMENT_REV >= 4 and not sc.air_clear((bb[0] - 12, bb[1] - 12, bb[2] + 12, bb[3] + 12), 4):
                continue
            # revision 8: no kite or balloon string passing near it (it seemed to hang from the string)
            if SCN.PLACEMENT_REV >= 8 and any(bb[0] - 30 <= a[0] + (b[0] - a[0]) * k / 24 <= bb[2] + 30 and bb[1] - 30 <= a[1] + (b[1] - a[1]) * k / 24 <= bb[3] + 30
                                              for a, b in getattr(sc, "strings", []) for k in range(25)):
                continue
            # revision 8: well clear of the house and of every standing structure (beside the house corner
            # the box read as stuck in the wall)
            if SCN.PLACEMENT_REV >= 8 and not sc.setting_clear((bb[0] - 45, bb[1] - 45, bb[2] + 45, bb[3] + 30),
                                                               only=("house", "clothesline", "laundry", "swing", "swing_seat", "feeder", "lamp", "tree",
                                                                     "tree_small", "stall", "bench", "slide", "seesaw", "bicycle", "hose_reel")):
                continue
            # nor against a market stall, where it seemed to be sliding off the counter
            if SCN.PLACEMENT_REV >= 4 and any(e["id"] == "stall" and sc.overlap((bb[0] - 20, bb[1] - 20, bb[2] + 20, bb[3] + 20), e["bbox"]) > 0
                                              for e in sc.S.elements if e.get("bbox")):
                continue
            if SCN.PLACEMENT_REV >= 4:
                # nobody may stand close by, under it, or reach toward it (a child jumping beside it
                # seemed to have thrown it)
                zone = (bb[0] - 170 * s, bb[1] - 50 * s, bb[2] + 170 * s, Y + 260 * s)
                # nor in front of a gate, where it seemed to lean on it
                if any(min(bb[2] + 20, g[2]) > max(bb[0] - 20, g[0]) and min(bb[3] + 20, g[3]) > max(bb[1] - 20, g[1])
                       for g in sc.S.anchors.get("no_float", ())):
                    continue
                if any(min(q.bbox()[2], zone[2]) > max(q.bbox()[0], zone[0]) and min(q.bbox()[3], zone[3]) > max(q.bbox()[1], zone[1])
                       for q in sc.assets.values()):
                    continue
                sc.airzones.append(zone)
            eb = sc.svg(sc.eid("floatbox"), "Box floating in the air", svg, Y, bb, "scored")
            self.ent("There is a wooden box", ["box", "crate", "wooden box"], "box", [eb])
            self.contra("Something is wrong with the box",
                        "The box is floating in the air with nothing holding it up",
                        ["the box is weird", "something odd about the box", "that box"], ["floating box", "box in the air", "nothing holding it up", "box should fall"], "floating", [eb])
            return True
        return False


class SquareWheel(T):
    id = "square_wheel"
    kind = "contradiction"
    domain = "physical"
    settings = ("garden", "park", "street", "playground")
    units, content = 1, 1

    def bind(self):
        self.thing = "wheelbarrow" if self.sc.setting_id in ("garden", "park") else "bicycle"

    def place(self):
        sc = self.sc
        for X, Y in self.stand_spots(y_range=(sc.S.horizon + 120, 975), n=80):
            s = sz(Y)
            f = sc.rng.choice([1, -1])
            if self.thing == "wheelbarrow":
                svg, bb = D.wheelbarrow(X, Y, s * self.k3(1.5, 1.25, 1.05), square=True, f=f, both=SCN.PLACEMENT_REV >= 7, bracket=SCN.PLACEMENT_REV >= 10, low=SCN.PLACEMENT_REV >= 15,
                                        v20=SCN.PLACEMENT_REV >= 20)
                acc, key = ["wheelbarrow", "cart", "barrow"], "wheelbarrow"
            else:
                # (revision 12: its stand drawn in front, light grey against the dark square wheel; behind the wheel it went unseen
                # and the bicycle "stands upright by itself with no stand or rack". A rack hoop behind it was tried on the bench:
                # its legs on the square wheels made them "square wheel-holder frames that belong to the rack")
                svg, bb = D.bicycle(X, Y, s * self.k3(1.35, 1.1, 0.9), square=True, col=sc.rng.choice([C["red"], C["teal"]]), f=f, wide=SCN.PLACEMENT_REV >= 10,
                                    heavy_stand=SCN.PLACEMENT_REV >= 11, front_stand=SCN.PLACEMENT_REV >= 12)
                acc, key = ["bike", "bicycle"], "bike"
            if not sc.fits(bb, limit=0.03):
                continue
            # revision 4: standing free, against nothing (by a slide's ladder it seemed to lean on it)
            if SCN.PLACEMENT_REV >= 4 and not sc.air_clear((bb[0] - 12, bb[1] - 12, bb[2] + 12, bb[3]), 4):
                continue
            # revision 10: wholly on the path or wholly off it. The square wheel is open, and the path's edge
            # seen through it drew a round wheel inside a square ("the wheel sits inside a black square frame")
            if SCN.PLACEMENT_REV >= 10:
                on = {sc.on_element("path", bb[0] + (bb[2] - bb[0]) * i / 6, bb[1] + (bb[3] - bb[1]) * j / 4)
                      for i in range(7) for j in range(1, 5)}
                if len(on) > 1:
                    continue
                # and off the sandbox, the picnic blanket and the pond's rim, ground the clearance check lets
                # people stand by (a barrow's handles over a blanket, a bicycle's wheel over the sandbox's frame)
                if not sc.setting_clear((bb[0] - 10, bb[1], bb[2] + 10, bb[3] + 12), only=("sandbox", "blanket", "pond")):
                    continue
            if SCN.PLACEMENT_REV >= 20:
                # revision 20: nobody's feet on it (a boy's foot over its handles: "about to trip over / run into" them)
                own = getattr(sc, "placing", None)
                if any(self._feet_over(q, bb) for q in sc.assets.values()
                       if q.family.startswith(("person.", "animal.")) and not q.m["variant"].get("airborne")):
                    continue
                sc.groundthings.append((bb, own))
            ew = sc.svg(sc.eid("square"), f"{self.thing.capitalize()} with square wheels", svg, Y, bb, "scored")
            self.ent(f"There is {art(self.thing)} {self.thing}", acc, key, [ew])
            self.contra(f"Something is wrong with the {self.thing}",
                        f"The {self.thing} has square wheels, so it could not roll",
                        ["something's wrong with the wheels", "funny wheels", f"weird {key}"], ["square wheels", "the wheels aren't round", "it can't roll"], "wheel", [ew])
            return True
        return False


    @staticmethod
    def _feet_over(q, bb, pad=8):
        b = q.bbox()
        h = b[3] - b[1]
        feet = (b[0], b[3] - 0.14 * h, b[2], b[3] + 4)
        return min(feet[2], bb[2] + pad) > max(feet[0], bb[0] - pad) and min(feet[3], bb[3] + pad) > max(feet[1], bb[1] - pad)


class FishInTree(T):
    id = "fish_in_tree"
    kind = "contradiction"
    domain = "biological"
    exclusive = ("tree_canopy",)
    units, content = 1, 1

    def bind(self):
        pass

    def place(self):
        sc = self.sc
        T_ = sc.S.anchors["tree"]
        if "branch" in T_:
            x, y = T_["branch"]
            pts = [(x, y - 16)] + [(sx, sy) for sx, sy in T_["slots"][3:]]
        else:
            pts = list(T_["slots"][3:])
        for (x, y) in pts:
            svg, bb = D.fish(x, y, self.k3(1.25, 0.9, 0.7), C["orange"], f=sc.rng.choice([1, -1]))
            if not sc.fits(bb, limit=0.03):
                continue
            ef = sc.svg(sc.eid("treefish"), "Fish sitting in the tree", svg, T_["bbox"][3] + 0.6, bb, "scored")
            self.ent("There is a fish", ["fish", "a fish", "goldfish"], "fish", [ef])
            self.contra("Something is wrong in the tree",
                        "A fish is sitting up in the tree, but fish live in water",
                        ["something in the tree", "the tree looks odd", "what's that in the tree"], ["fish in a tree", "fish can't live in trees", "fish belong in water"], "fish", [ef])
            return True
        return False


class SittingOnAir(T):
    """Someone sits as if on a chair, but there is nothing under them."""
    id = "sitting_on_air"
    kind = "contradiction"
    domain = "physical"
    units, content = 1, 1

    def bind(self):
        sc = self.sc
        self.p = sc.person(GROWN)
        self.pose = sc.rng.choice(["sit_read", "sit_drink"])
        self.vp = sc.need(self.p, self.pose, sc.rng.choice(["focused", "smile", "neutral"]), 45)

    def place(self):
        sc = self.sc
        ep = sc.eid("airsitter")
        seats = [a for k, a in sc.S.anchors.items() if k in ("bench", "swing", "seesaw", "slide")]

        def clear(p):
            # well away from anything one could sit on, so nobody reads a hidden seat into it
            for a in seats:
                ax = a.get("x0", a.get("cx", a.get("seat", (0, 0))[0] if "seat" in a else a.get("platform", (0, 0))[0]))
                if abs(p.X - ax) < 300:
                    return False
            if SCN.PLACEMENT_REV >= 9:
                # revision 9: and clear of every standing structure (a sitter with his back to a clothesline
                # post seemed to lean on it)
                b = p.bbox()
                if not sc.setting_clear((b[0] - 24, b[1] - 10, b[2] + 24, b[3]), only=HAT_STRUCT9 + ("hose_reel", "bench", "stall")):
                    return False
            return True
        cands = [c for c in self.stand_spots(y_range=(sc.S.horizon + 180, 975), n=120)]
        p = sc.try_put(ep, self.vp, cands, want_face=sc.rng.choice([1, -1]), accept=clear)
        if not p:
            return False
        what = "reading" if self.pose == "sit_read" else "having a drink"
        self.act(self.p, f"sitting and {what}", [f"sitting and {what}", "sitting", what, "reading a book" if self.pose == "sit_read" else "drinking"], "sitting", [ep])
        self.contra("Something is wrong with how the person is sitting",
                    "The person is sitting on nothing: there is no chair or bench under them",
                    ["something odd about how they're sitting", "that person looks strange", "something's missing"],
                    ["sitting on nothing", "there's no chair", "sitting in the air", "invisible chair", "nothing to sit on"], "chair", [ep])
        return True


class LadderNothing(T):
    """A ladder stands leaning against nothing at all."""
    id = "ladder_nothing"
    kind = "contradiction"
    domain = "physical"
    # not on the playground: among its frames there was no open ground for it, and beside the slide it
    # read as the slide's own ladder
    settings = ("park",)
    units, content = 1, 1

    def bind(self):
        pass

    def place(self):
        sc = self.sc
        solid = [e["bbox"] for e in sc.S.elements if e["id"] in ("tree", "tree_small", "lamp", "slide", "swing", "bench", "house", "buildings") and e.get("bbox")]
        if SCN.PLACEMENT_REV >= 18:
            # revision 18: well clear of the bench, behind it too (its feet just behind the backrest, it could be read as
            # "propped on or just behind the bench")
            solid += [(b[0] - 40, b[1] - 80, b[2] + 40, b[3] + 20) for b in (e["bbox"] for e in sc.S.elements if e["id"] == "bench" and e.get("bbox"))]
        if SCN.PLACEMENT_REV >= 20:
            # revision 20: well clear of every other upright, its top too (on the open lawn, its top just below a lamp post's
            # foot, a ladder read as "standing up at a lean ... or lying flat on the grass")
            solid = [(b[0] - 30, b[1] - 30, b[2] + 30, b[3] + 30) for b in solid]
        for X, Y in self.stand_spots(y_range=(sc.S.horizon + 140, 960), n=200 if SCN.PLACEMENT_REV >= 20 else 100):
            s = sz(Y) * self.k3(1.2, 1.0, 0.85)
            lean = sc.rng.choice([12, 16, -12, -16])
            svg, bb = D.ladder(X, Y, s, lean=lean)
            if any(sc.overlap(bb, b) > 0 for b in solid):
                continue
            # revision 20: and its top up past the lawn's far edge, against the hedge and hills, so it plainly stands
            if SCN.PLACEMENT_REV >= 20 and bb[1] > sc.S.horizon - 20:
                continue
            if not sc.fits(bb, limit=0.03):
                continue
            # revision 18: nor over the pond (its top "appears to stick up into / overlap the pond area")
            if SCN.PLACEMENT_REV >= 18 and not sc.setting_clear((bb[0] - 12, bb[1] - 12, bb[2] + 12, bb[3]), only=("pond",)):
                continue
            if SCN.PLACEMENT_REV >= 11:
                # revision 11: nobody stands beside the ladder, now or later, where they could be holding it up (a
                # man waving right beside its top), as nobody stands by the floating box
                zone = (bb[0] - 110 * s, bb[1] - 30 * s, bb[2] + 110 * s, Y + 40 * s)
                if any(min(q.bbox()[2], zone[2]) > max(q.bbox()[0], zone[0]) and min(q.bbox()[3], zone[3]) > max(q.bbox()[1], zone[1])
                       for q in sc.assets.values()):
                    continue
                sc.airzones.append(zone)
            el = sc.svg(sc.eid("ladder"), "Ladder leaning on nothing", D.shadow(X + lean * 1.6 * s, Y, 80 * s) + svg, Y, bb, "scored")
            self.ent("There is a ladder", ["ladder", "a ladder", "step ladder"], "ladder", [el])
            self.contra("Something is wrong with the ladder",
                        "The ladder is leaning on nothing, so it should fall over",
                        ["the ladder is odd", "something strange about the ladder", "that ladder"],
                        ["leaning on nothing", "nothing holding it up", "it should fall", "not against anything", "ladder standing by itself"], "ladder", [el])
            return True
        return False


class DogReading(T):
    """A dog sits holding an open newspaper, reading it."""
    id = "dog_reading"
    kind = "contradiction"
    domain = "biological"
    units, content = 1, 1

    def bind(self):
        sc = self.sc
        # revision 9: the floppy-eared brown dog where it is free (the white dog's pointed ears read as a
        # goat's or a cat's)
        self.d = sc.animal(["dog"], prefer=("animal.dog_01",) if SCN.PLACEMENT_REV >= 9 else ())
        # revision 4: sitting up with the front paws raised, holding the paper (sitting with the paws
        # on the ground, the paper seemed to stand up by itself)
        self.hold = SCN.PLACEMENT_REV >= 4
        self.vd = sc.need(self.d, "sit_up_hold" if self.hold else "sit_look_down", "neutral", 90)

    def place(self):
        sc = self.sc
        ed = sc.eid("readingdog")

        def paper(d):
            f = d.facing() or 1
            s = sz(d.Y)
            if self.hold:
                (ax, ay), (bx, by) = d.anchor("paw_FL"), d.anchor("paw_FR")
                px, py = (ax + bx) / 2, (ay + by) / 2
                k = s * 1.05
                # the paper's near edge sits just under the paws; one paw grips its upper part, the other
                # its lower part, drawn over the paper
                svg, bb = D.newspaper(px + f * (74 * k / 2 - 5 * s), py + 8 * s, k, f, style=8 if SCN.PLACEMENT_REV >= 24 else 7 if SCN.PLACEMENT_REV >= 7 else 6)
                col = d.color_at("paw_FL")
                if SCN.PLACEMENT_REV >= 9:
                    col = C["white"]        # revision 9: white paws, like the feet (dark grey ones read as hands)
                if SCN.PLACEMENT_REV >= 23 and D.PAW25 != "O":
                    col = {"animal.dog_01": C["tan"]}.get(d.family, C["white"])
                if SCN.PLACEMENT_REV >= 23 and D.PAW25 == "C":
                    pass                    # revision 23: the dog's own paws rest on the paper, which is drawn behind it
                elif SCN.PLACEMENT_REV >= 7:
                    # revision 7: paws with toes, gripping the edge (plain round paws read as ring-binder holes)
                    for dy in (-8, 18):
                        cx_, cy_ = px + f * 1 * s, py + dy * s
                        svg += D.ell(cx_, cy_, 10 * s, 7.5 * s, col, D.OW * 0.8)
                        if SCN.PLACEMENT_REV >= 23 and D.PAW25 == "A":
                            continue
                        svg += "".join(D.line(cx_ + f * 3 * s, cy_ + t * s, cx_ + f * 9 * s, cy_ + t * 1.3 * s, D.OUT, 1.8 * s) for t in (-3.5, 0, 3.5))
                else:
                    svg += "".join(D.ell(px + f * 1 * s, py + dy * s, 8 * s, 6.5 * s, col, D.OW * 0.8) for dy in (-8, 18))
                self.np = (svg, bb)
                # a paper against a lamp post read as a notice pinned to it
                if not sc.air_clear((bb[0] - 10, bb[1] - 10, bb[2] + 10, bb[3] + 4), 4):
                    return None
                return [bb]
            mx, my = d.anchor("mouth")
            self.np = D.newspaper(mx + f * 14 * s, my + 44 * s, s * 1.05, f, style=7 if SCN.PLACEMENT_REV >= 7 else 6)
            return [self.np[1]]
        # revision 4: the paper keeps clear of every other scored thing (laid over a parcel, it read as part of it)
        xl = 0.05 if SCN.PLACEMENT_REV >= 4 else 0.3
        d = self.place_with(ed, self.vd, self.stand_spots(y_range=(sc.S.horizon + 150, 975)), want_face=sc.rng.choice([1, -1]), extras=paper, limit=0.12, xlimit=xl, ground_extras=False)
        if not d:
            return False
        svg, bb = self.np
        en = sc.svg(sc.eid("newspaper"), "Newspaper held by the dog", svg, d.Y - 1 if SCN.PLACEMENT_REV >= 23 and D.PAW25 == "C" else d.Y + 1, bb, "scored")
        dn = sc.name(self.d)
        it = self.ent(f"A {dn} is sitting up holding a newspaper", [f"{dn} sitting", f"{dn} with a newspaper", f"{dn} holding a paper"], "dog", [ed, en], animate=True)
        it["type"] = "action"
        self.contra(f"Something is wrong with the {dn}",
                    f"The {dn} is reading a newspaper, but dogs can't read",
                    [f"the {dn} is strange", f"something odd about the {dn}", "that's funny"],
                    ["dog reading", "dogs can't read", "a dog reading the paper", "reading the newspaper"], "newspaper", [ed, en])
        return True


CONTRADICTIONS = [WaterUpward, PanWatering, SweepFork, BucketHat, FloatingBox, SquareWheel, FishInTree, SittingOnAir, LadderNothing, DogReading]
for _c in CONTRADICTIONS:
    _c.kind = "contradiction"

# features each template needs, per setting (beyond the setting's defaults)
for _c in EVENTS + MODULES + CONTRADICTIONS:
    if not _c.needs:
        _c.needs = {}
TREE_SETTINGS = ("garden", "park", "street")
ALL_TEMPLATES = {c.id: c for c in EVENTS + MODULES + CONTRADICTIONS}

# phrase used when a template's main object is a setting entity: that entity is not scored separately


# static item signatures (type, chain) per template, used for counting combinations and for
# planning isomorphs before anything is placed; checked against the items templates really emit
A0, E0, I1, I2 = ("action", 0), ("entity", 0), ("inference", 1), ("inference", 2)
CN, CE = ("contradiction_notice", 0), ("contradiction_explain", 1)
SIG = {c.id: [A0] for c in EVENTS}
SIG["play_catch"] = [A0, A0]
SIG["seesaw"] = [A0, A0]
SIG.update({
    "blocked_hose": [A0, A0, A0, I2], "rain_coming": [E0, A0, I1], "cat_stalks_bird": [A0, A0, I1], "ball_in_tree": [A0, E0, I1],
    "kite_in_tree": [A0, E0, I1], "ice_cream_drop": [A0, E0, A0, I1], "about_to_trip": [A0, E0, I1], "dog_begs": [A0, A0, I1],
    "sprinkler_package": [A0, E0, I1], "paint_tracks": [A0, A0, E0, I2], "windy_hat": [A0, E0, I2], "bird_steals": [A0, A0, I2],
    "lost_balloon": [A0, E0, I1], "ducks_bread": [A0, A0, I1], "seesaw_heavy": [A0, A0, I1], "dog_wants_walk": [A0, I1],
    "sitting_on_air": [A0, CN, CE], "ladder_nothing": [E0, CN, CE], "dog_reading": [A0, CN, CE],
    "water_upward": [A0, CN, CE], "pan_watering": [A0, CN, CE], "sweep_fork": [A0, CN, CE], "bucket_hat": [A0, CN, CE],
    "floating_box": [E0, CN, CE], "square_wheel": [E0, CN, CE], "fish_in_tree": [E0, CN, CE],
})
