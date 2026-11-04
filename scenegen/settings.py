"""Four deliberately generic settings: a back garden, a park, a pedestrian street and a playground.

Each setting is a fixed layout of drawn features plus the slots the generator fills:
  walk       rectangles where a standing character's ground point may go
  blocked    rectangles (per feature) where ground points may not go
  anchors    named places templates attach to (seats, perches, the clothesline, tree canopies, water)
  entities   features that can be scored as content items, with accepted names and a key word
  fillers    optional unscored objects used to hold visual clutter inside the tier band
Features are optional where a template may need them (a swing, a clothesline, a pond) and
switched on only when a template asks for them or the clutter band needs them.

z order: everything standing on the ground is drawn in order of its ground y (painter's order),
so characters and features interleave correctly; flat things (sky, lawn, path, pond) come first.
"""
import math

from . import draw as D
from .draw import C, sz

SETTINGS = ("garden", "park", "street", "playground")


def E(text, accepted, key, kind="entity"):
    return {"text": text, "accepted": accepted, "key": key, "kind": kind}


REEL30 = "B"   # the reel when nobody has the hose: O a stub, B the end hanging with its nozzle on (and none when somebody has it)


class SettingInstance:
    def __init__(self, sid, sky):
        self.id = sid
        self.sky = sky
        self.elements = []
        self.anchors = {}
        self.walk = []
        self.blocked = []
        self.entities = {}
        self.filler_slots = []
        self.features = set()
        self.horizon = 600
        self.soft = []          # ground features nobody should stand in or just in front of (flower beds, blankets)

    def add(self, eid, label, svg, z, role="setting", bbox=None, entity=None, blocked=None):
        self.elements.append({"id": eid, "label": label, "svg": svg, "z": z, "role": role, "bbox": bbox, "kind": "svg"})
        if entity:
            self.entities[eid] = dict(entity, element=eid)
        if blocked:
            self.blocked.append(tuple(blocked))
        return eid

    def filler(self, sid, x, y, label, fn, blocked=None, needs=None):
        """Register an optional filler; fn(x, y) -> (svg, bbox); needs(scene) -> bool says whether it makes sense here."""
        self.filler_slots.append({"id": sid, "x": x, "y": y, "label": label, "fn": fn, "blocked": blocked, "needs": needs})

    # ground helpers -------------------------------------------------------
    def in_soft(self, x, y):
        return any(r[0] <= x <= r[2] and r[1] <= y <= r[3] for r in self.soft)

    def walkable(self, x, y, margin=0):
        if not any(r[0] + margin <= x <= r[2] - margin and r[1] <= y <= r[3] for r in self.walk):
            return False
        if self.in_soft(x, y):
            return False
        return not any(r[0] <= x <= r[2] and r[1] <= y <= r[3] for r in self.blocked)


DARK_SCALE = {"value": 1.0}


def sky_layer(S, sky, horizon, sun_at=(1450, 120), clouds=((640, 120, 0.7), (900, 160, 0.55)), dark=((600, 115, 1.05), (850, 90, 1.0), (1035, 150, 0.75))):
    k = DARK_SCALE["value"]
    if k != 1.0:
        mx = sum(x for x, _, _ in dark) / len(dark)
        dark = tuple((mx + (x - mx) * k, y * (0.6 + 0.4 * k), s * k) for x, y, s in dark)
    col = C["sky"] if sky == "clear" else C["sky_dull"]
    S.add("sky", "Sky", D.rect(-10, -10, D.W + 20, horizon + 30, col, 0, 0), -100, "background")
    if sky == "clear":
        S.add("sun", "Sun", D.sun(*sun_at), -99, "setting", (sun_at[0] - 95, sun_at[1] - 95, sun_at[0] + 95, sun_at[1] + 95),
              entity=E("It is a sunny day", ["sun", "sunny", "sunshine", "nice day", "sunny day"], "sun"))
        S.add("clouds_white", "Small white clouds", "".join(D.puff(x, y, s, C["white"]) for x, y, s in clouds), -98, "setting",
              (min(x for x, _, _ in clouds) - 90, 40, max(x for x, _, _ in clouds) + 90, 220),
              entity=E("There are a few white clouds", ["clouds", "white clouds", "a few clouds", "fluffy clouds"], "clouds"))
    else:
        S.add("clouds_dark", "Dark clouds rolling in", "".join(D.puff(x, y, s, C["cloud_dark"]) for x, y, s in dark), -98, "scored",
              (min(x for x, _, _ in dark) - 120, 20, max(x for x, _, _ in dark) + 120, 230),
              entity=E("Dark clouds are coming", ["dark clouds", "storm clouds", "clouds", "cloudy", "storm", "gray clouds"], "clouds"))
        S.anchors["dark_clouds_box"] = (min(x for x, _, _ in dark) - 90, 40, max(x for x, _, _ in dark) + 90, 200)


# ======================================================================= garden
def laundry_svg(blow=0, lines=True, short=False):
    """The jeans and the striped towel pegged on the garden line. blow (v0.14, -1 or 1): swung out with a gust, the hems
    lifted and carried downwind, with short wind lines past them (hanging straight down in a gust that blew a hat away,
    "the washing on the line is not moving at all"). v0.15: a fraction of that for a breeze (a kite flying beside
    washing that hung straight down: "the kite flies high (needs wind) but the washing hangs straight down"), and
    lines=False leaves out the wind lines."""
    if not blow:
        laundry = ""
        x0 = 652
        laundry += D.poly([(x0, line_y(x0)), (x0 + 58, line_y(x0 + 58)), (x0 + 60, line_y(x0) + 120), (x0 + 36, line_y(x0) + 120),
                           (x0 + 29, line_y(x0) + 40), (x0 + 22, line_y(x0) + 120), (x0 - 2, line_y(x0) + 120)], C["blue"])
        if short:
            # v0.21: the jeans alone, so the person pinning up a shirt has no towel behind her head ("a yellow shirt on the
            # line behind the woman's head can read as part of her clothing")
            for px in (656, 704):
                laundry += D.rect(px - 3, line_y(px) - 9, 7, 16, C["wood_light"], 1, D.OW * 0.6)
            return laundry
        x0 = 724
        laundry += D.rect(x0, line_y(x0 + 25) - 2, 52, 92, C["yellow"], 3)
        for k_ in range(3):
            laundry += D.line(x0 + 4, line_y(x0 + 25) + 20 + k_ * 24, x0 + 48, line_y(x0 + 25) + 20 + k_ * 24, C["red"], 6)
        for px in (656, 704, 728, 772):
            laundry += D.rect(px - 3, line_y(px) - 9, 7, 16, C["wood_light"], 1, D.OW * 0.6)
        return laundry
    tan = math.tan(math.radians(28))

    def sw(px, py, top):
        d = py - top
        return (px + blow * d * tan, top + d * 0.84)
    laundry = ""
    x0 = 652
    jeans = [(x0, line_y(x0)), (x0 + 58, line_y(x0 + 58)), (x0 + 60, line_y(x0) + 120), (x0 + 36, line_y(x0) + 120),
             (x0 + 29, line_y(x0) + 40), (x0 + 22, line_y(x0) + 120), (x0 - 2, line_y(x0) + 120)]
    laundry += D.poly([sw(px, py, line_y(px) if i < 2 else line_y(x0)) for i, (px, py) in enumerate(jeans)], C["blue"])
    x0 = 724
    top = line_y(x0 + 25) - 2
    towel = [(x0, top), (x0 + 52, top), (x0 + 52, top + 92), (x0, top + 92)]
    laundry += D.poly([sw(px, py, top) for px, py in towel], C["yellow"])
    for k_ in range(3):
        yy = line_y(x0 + 25) + 20 + k_ * 24
        a, b = sw(x0 + 4, yy, top), sw(x0 + 48, yy, top)
        laundry += D.line(a[0], a[1], b[0], b[1], C["red"], 6)
    for px in (656, 704, 728, 772):
        laundry += D.rect(px - 3, line_y(px) - 9, 7, 16, C["wood_light"], 1, D.OW * 0.6)
    if not lines:
        return laundry
    # two short wind lines blowing past the washing
    sg = 1 if blow > 0 else -1
    for gx, gy in (((700, 372), (770, 352)) if blow > 0 else ((770, 372), (700, 352))):
        L = 46
        laundry += f'<path d="M {D.P(gx, gy)} q {sg * L / 2:.1f} -8 {sg * L:.1f} 0 t {sg * L:.1f} -10" fill="none" stroke="{C["white"]}" stroke-width="4.5" stroke-linecap="round" stroke-opacity="0.95"/>'
    return laundry


def line_y(x):
    t = (x - 630) / 320
    return (1 - t) ** 2 * 396 + 2 * (1 - t) * t * 440 + t * t * 396


def _rev():
    from . import scene as _SCN
    return _SCN.PLACEMENT_REV


def path_edges(left, right, y0=640, y1=1010, step=10):
    """Sample two cubic Bezier edges of a winding path into (y, left x, right x) rows."""
    def pts(c):
        out = []
        for i in range(121):
            t = i / 120
            out.append(tuple((1 - t) ** 3 * c[0][k] + 3 * (1 - t) ** 2 * t * c[1][k] + 3 * (1 - t) * t * t * c[2][k] + t ** 3 * c[3][k] for k in (0, 1)))
        return out

    def x_at(curve, y):
        best = min(curve, key=lambda q: abs(q[1] - y))
        return best[0]
    L, R = pts(left), pts(right)
    return [(y, x_at(L, y), x_at(R, y)) for y in range(y0, y1 + 1, step)]


def on_path(anchor, x, y, margin=0.0):
    """True if (x, y) lies on a path whose anchor carries sampled edges (v0.8)."""
    rows = anchor.get("edges") if anchor else None
    if not rows:
        return True
    row = min(rows, key=lambda r: abs(r[0] - y))
    if abs(row[0] - y) > 15:
        return False
    return row[1] + margin <= x <= row[2] - margin


def build_garden(features, sky):
    S = SettingInstance("garden", sky)
    S.horizon = 600
    S.features = set(features)
    sky_layer(S, sky, 600)
    S.add("ground", "Lawn", D.rect(-10, 600, D.W + 20, 410, C["grass"], 0, 0), -90, "background")
    S.add("tree_line", "Trees beyond the fence", D.tree_line(452, step=64), -96, "background", (-10, 380, 1610, 455))
    # tree behind the fence
    tsvg, tinfo = D.tree(420, 450, 0.92, trunk_h=150)
    S.add("tree", "Tree behind the fence", tsvg, 440, "setting", tinfo["bbox"], entity=E("There is a tree", ["tree", "trees"], "tree"))
    S.anchors["tree"] = tinfo
    if "feeder" in features and _rev() >= 13:
        # v0.15: the bird table stands on the lawn, its post down to the grass in front of the fence (its post ran down
        # behind the fence: "the birdhouse pole disappears behind the fence; unclear which garden it is in"); by the
        # fence on the right (beside the gate when the swing set stands there; never over the flower bed, where it stood in
        # the way of the water and the people at the bed)
        fx = 1405 if "swing" in features else 1245
        f = D.stroke(D.poly_d([(fx, 652), (fx, 352)]), C["wood"], 9) + D.rect(fx - 27, 330, 54, 26, C["wood_light"], 3)
        f += D.poly([(fx - 35, 332), (fx, 305), (fx + 35, 332)], C["roof"]) + D.line(fx - 23, 360, fx + 23, 360, D.OUT, 4)
        # a round entrance hole and a little perch peg under it (a plain box on a post could be "a garden lamp or lantern")
        f += D.circ(fx, 342, 6.5, C["charcoal"]) + D.line(fx - 7, 352, fx + 7, 352, C["wood"], 3)
        f += D.ell(fx, 652, 16, 5, C["grass_dark"], 0)
        S.add("feeder", "Bird table on a post", f, 652, "setting", (fx - 40, 300, fx + 40, 656),
              entity=E("There is a bird feeder", ["bird feeder", "feeder", "birdhouse", "bird house", "bird table"], "feeder"),
              blocked=(fx - 22, 636, fx + 22, 668))
        S.anchors["feeder_perch"] = (fx + 5, 331, 652)       # x, y, depth y for scale
    elif "feeder" in features:
        f = D.stroke(D.poly_d([(1245, 440), (1245, 352)]), C["wood"], 8) + D.rect(1218, 330, 54, 26, C["wood_light"], 3)
        f += D.poly([(1210, 332), (1245, 305), (1280, 332)], C["roof"]) + D.line(1222, 360, 1268, 360, D.OUT, 4)
        S.add("feeder", "Bird feeder on a pole", f, 441, "setting", (1205, 300, 1285, 440),
              entity=E("There is a bird feeder", ["bird feeder", "feeder", "birdhouse", "bird house"], "feeder"))
        S.anchors["feeder_perch"] = (1250, 331, 440)       # x, y, depth y for scale
    fence = ""
    x = 310
    while x < D.W + 10:
        if not (1440 <= x < 1560):
            fence += D.poly([(x, 440), (x + 22, 428), (x + 44, 440), (x + 44, 615), (x, 615)], C["wood_light"], D.OW * 0.8)
        x += 46
    fence += D.rect(300, 480, 1140, 16, C["wood"], 2, D.OW * 0.8) + D.rect(300, 565, 1140, 16, C["wood"], 2, D.OW * 0.8)
    fence += D.rect(1560, 480, 60, 16, C["wood"], 2, D.OW * 0.8) + D.rect(1560, 565, 60, 16, C["wood"], 2, D.OW * 0.8)
    for bx in (1560, 1600):
        fence += D.poly([(bx, 440), (bx + 22, 428), (bx + 44, 440), (bx + 44, 615), (bx, 615)], C["wood_light"], D.OW * 0.8)
    fence += D.rect(1442, 432, 116, 183, C["wood"], 4) + D.line(1442, 432, 1558, 615, D.OUT, 4) + D.circ(1540, 525, 7, C["charcoal"])
    S.add("fence", "Wooden fence with a gate", fence, 615, "setting", (300, 428, 1610, 615), entity=E("There is a fence", ["fence", "wooden fence", "gate"], "fence"))
    S.anchors["fence_top"] = {"y": 437, "x0": 340, "x1": 1420, "depth": 612}
    S.anchors["balloon_max_y"] = 265      # a loose balloon's string ends well above the fence top, not on it
    S.anchors["no_float"] = [(1442, 432, 1558, 615)]      # the gate: nothing hangs in the air in front of it
    house =D.rect(-10, 230, 320, 545, C["wall"], 0) + D.poly([(-20, 238), (340, 238), (250, 120), (-20, 120)], C["roof"])
    house += D.rect(40, 320, 100, 110, C["sky"], 4) + D.line(90, 320, 90, 430) + D.line(40, 375, 140, 375)
    house += D.rect(175, 560, 90, 215, C["blue"], 4) + D.circ(250, 670, 6, C["yellow"]) + D.rect(160, 765, 120, 16, C["gray"], 2)
    S.add("house", "Back of the house", house, 781, "setting", (-10, 120, 340, 781),
          entity=E("It is the back yard of a house", ["house", "home", "backyard", "back yard", "yard", "garden"], "house"),
          blocked=(-10, 600, 335, 800))
    path = D.flat(D.poly_d([(1448, 615), (1556, 615), (1560, 1010), (1250, 1010)], True), C["path"])
    path += f'<path d="M 1448 615 L 1250 1010 M 1556 615 L 1560 1010" fill="none" stroke="{D.OUT}" stroke-width="{D.OW * 0.8}"/>'
    STONES = [(1500, 660, 26), (1470, 740, 32), (1440, 830, 38), (1405, 935, 44)]
    if _rev() >= 8:
        # v0.10: a paved path, its slabs' joints across it (a giant fork sweeping among stepping stones
        # read as digging, and a stone showed behind a lying dog's back)
        STONES = []
        for jy in (668, 728, 798, 880, 972):
            xl = 1448 + (1250 - 1448) * (jy - 615) / 395 + 3
            xr = 1556 + 4 * (jy - 615) / 395 - 3
            path += D.line(xl, jy, xr, jy, C["path_edge"], 2.5 + (jy - 615) / 160)
    for (sx, sy, rx) in STONES:
        path += D.ell(sx, sy, rx, rx * 0.35, C["path_edge"], D.OW * 0.6)
    S.add("path", "Stone path to the gate" if _rev() < 8 else "Paved path to the gate", path, -80, "setting", (1250, 615, 1560, 1000))
    S.anchors["path"] = {"x0": 1300, "x1": 1540, "y0": 660, "y1": 990,
                         # v0.10: the stepping stones (revision 8 keeps animals and the swept dust off them)
                         "stones": [(sx - rx, sy - rx * 0.35, sx + rx, sy + rx * 0.35) for sx, sy, rx in STONES],
                         # v0.8: the path's real edges (y, left x, right x), so "on the path" means on it
                         "edges": [(y, 1448 + (1250 - 1448) * (y - 615) / 395, 1556 + 4 * (y - 615) / 395) for y in range(620, 1011, 10)]}
    S.walk = [(330, 650, 1560, 992)]
    if "clothesline" in features:
        cl = D.rect(624, 390, 13, 315, C["wood"], 3) + D.rect(944, 390, 13, 315, C["wood"], 3)
        cl += D.rect(608, 384, 45, 11, C["wood"], 3) + D.rect(928, 384, 45, 11, C["wood"], 3)
        cl += f'<path d="M 630 396 Q 790 440 950 396" fill="none" stroke="{D.OUT}" stroke-width="3.5"/>'
        S.add("clothesline", "Clothesline", cl, 705, "setting", (608, 384, 973, 705), blocked=(600, 680, 660, 730))
        S.blocked.append((920, 680, 980, 730))
        S.anchors["clothesline"] = {"x0": 650, "x1": 930, "fn": line_y, "depth": 705}
    if "laundry" in features and "clothesline" in features:
        short = _rev() >= 19 and "laundry_short" in features
        laundry = laundry_svg(short=short)
        S.add("laundry", "Clothes hanging on the line", laundry, 706, "setting", (650, 396, 715, 520) if short else (650, 396, 780, 560),
              entity=E("Clothes are hanging on the line", ["clothes", "laundry", "washing", "clothesline", "clothes line", "towel", "pants"], "laundry"))
    if "swing" in features:
        # v0.15: the frame stands 55 px further from the path (its right legs stood on the paving: "the swing set's legs
        # stand on the paved path rather than the grass")
        dx = -55 if _rev() >= 13 else 0
        sw = D.stroke(D.poly_d([(1098 + dx, 845), (1140 + dx, 468)]), C["slate"], 12) + D.stroke(D.poly_d([(1176 + dx, 845), (1140 + dx, 468)]), C["slate"], 12)
        sw += D.stroke(D.poly_d([(1292 + dx, 845), (1330 + dx, 468)]), C["slate"], 12) + D.stroke(D.poly_d([(1368 + dx, 845), (1330 + dx, 468)]), C["slate"], 12)
        sw += D.stroke(D.poly_d([(1130 + dx, 470), (1340 + dx, 470)]), C["slate"], 13)
        S.add("swing", "Swing set", sw, 846, "setting", (1090 + dx, 460, 1378 + dx, 850),
              entity=E("There is a swing set", ["swing", "swings", "swing set"], "swing"), blocked=(1070 + dx, 760, 1400 + dx, 930))
        S.anchors["swing"] = {"seat": (1234 + dx, 772), "rope_top": ((1205 + dx, 476), (1262 + dx, 476)), "depth": 846, "seat_w": 84}
        empty = D.line(1205 + dx, 476, 1205 + dx, 772, D.OUT, 4) + D.line(1262 + dx, 476, 1262 + dx, 772, D.OUT, 4) + D.rect(1192 + dx, 768, 84, 13, C["red"], 3)
        S.add("swing_seat", "Empty swing seat", empty, 845, "setting", (1190 + dx, 470, 1278 + dx, 782))
    if "flowers" in features:
        fb, bb = D.flowerbed(445, 800, 1.0)
        S.add("flowers", "Flower bed", fb, 836, "setting", bb, entity=E("There is a flower bed", ["flowers", "flower bed", "flowerbed", "garden"], "flowers"),
              blocked=(300, 755, 590, 850))
        S.anchors["flowers"] = {"center": (445, 780), "bbox": bb, "stand_left": (610, 820), "stand_right": (290, 830), "depth": 836}
        S.soft.append((bb[0] - 30, bb[3] - 20, bb[2] + 30, bb[3] + 90))
    if "hose_reel" in features:
        reel = D.rect(282, 800, 40, 70, C["charcoal"], 4) + D.circ(302, 820, 30, C["hose"])
        reel += "".join(f'<circle cx="302" cy="820" r="{r}" fill="none" stroke="{D.OUT}" stroke-width="2"/>' for r in (24, 18))
        reel += D.circ(302, 820, 9, C["gray"])
        if _rev() < 28 or REEL30 == "O":
            reel += D.hose_path([(326, 834), (350, 866), (330, 868)], 0.9)
        S.add("hose_reel", "Hose reel", reel, 870, "setting", (274, 792, 330, 870), blocked=(260, 790, 340, 890))
        if _rev() >= 28 and REEL30 != "O":
            # revision 28: the end of the hose hangs off the reel with its nozzle on, and goes when someone has the hose ("only a short stub of hose joined to nothing"; "a short second stub of hose curls by the reel")
            # (as short as the old stub, "more like a stub or a hook than a usable length of hose": so a loose coil of it on the grass)
            tail = D.hose_path([(326, 834), (352, 858), (360, 882), (366, 904), (392, 900)], 0.9)
            tail += D.poly([(391, 894), (392, 906), (420, 903), (420, 899)], C["yellow"], D.OW * 0.6)
            S.add("hose_tail", "End of the hose", tail, 871, "setting", (326, 830, 422, 912), blocked=(340, 860, 424, 914))
        S.anchors["hose_reel"] = (302, 848)
    if "bench" in features:
        # slim back slats on posts above a deeper seat (seat and back drawn alike read as a picnic table)
        b = D.rect(52, 806, 9, 56, C["wood"], 2) + D.rect(219, 806, 9, 56, C["wood"], 2)
        b += D.rect(44, 808, 192, 9, C["wood_light"], 3) + D.rect(44, 828, 192, 9, C["wood_light"], 3)
        b += D.poly([(46, 852), (234, 852), (240, 860), (40, 860)], C["wood"], D.OW * 0.8)
        b += D.rect(40, 858, 200, 15, C["wood_light"], 3)
        b += D.rect(55, 873, 14, 55, C["wood"], 2) + D.rect(212, 873, 14, 55, C["wood"], 2)
        S.add("bench", "Garden bench", b, 928, "setting", (40, 806, 240, 928), entity=E("There is a bench", ["bench", "seat"], "bench"),
              blocked=(20, 820, 260, 992))
        S.anchors["bench"] = {"seat_y": 861, "x0": 70, "x1": 210, "depth": 928, "front_y": 960}
    # filler slots
    # v0.15: the bushes stand on the lawn in front of the fence (drawn just behind its foot, only their lower half showed
    # below the boards: "looks cut off ... its top half hidden by the fence though it is on the lawn side")
    by_ = 648 if _rev() >= 13 else None
    S.filler("bush_left", 360, by_ or 615, "Bush", lambda x, y: (D.bush(x, y, 0.9), (x - 70, y - 60, x + 70, y + 30)))
    S.filler("bush_mid", 1010, by_ or 612, "Bush", lambda x, y: (D.bush(x, y, 0.85), (x - 66, y - 56, x + 66, y + 28)))
    # by the fence, off the path (pots standing on the stepping stones read as odd)
    S.filler("pots", 1130, 700, "Flower pots", lambda x, y: (D.pot(x, y, C["grass_dark"]) + D.pot(x + 60, y - 20, "#4fae4a"), (x - 30, y - 90, x + 90, y)), (1090, 650, 1230, 720))
    S.filler("wheelbarrow", 920, 975, "Wheelbarrow", lambda x, y: D.wheelbarrow(x, y, 1.0, both=_rev() >= 7, bracket=_rev() >= 10, low=_rev() >= 15, stand=_rev() >= 18), (890, 940, 1080, 990))
    S.filler("watering_can", 1210, 960, "Watering can", lambda x, y: (D.poly([(x - 25, y - 55), (x + 25, y - 55), (x + 20, y), (x - 20, y)], C["teal"]) +
                                                                       D.stroke(D.poly_d([(x - 22, y - 35), (x - 60, y - 60)]), C["teal"], 8) +
                                                                       D.stroke(f"M {x - 15} {y - 55} Q {x} {y - 82} {x + 18} {y - 55}", C["teal"], 6), (x - 66, y - 84, x + 28, y)), (1150, 930, 1250, 975),
             # revision 6: not a second can beside someone watering with one (two cans read as odd)
             # (revision 18: nor beside the frying pan; revision 19: nor beside a hose, "both a hose and an unused watering can")
             needs=lambda sc: _rev() < 6 or not any(t.id in (("water_flowers", "water_upward", "pan_watering", "hose_water", "blocked_hose", "sprinkler_package") if _rev() >= 19
                                                           else ("water_flowers", "water_upward", "pan_watering") if _rev() >= 18
                                                           else ("water_flowers", "water_upward")) for t in sc.templates))
    # v0.7: kibble in the bowl, so it reads as a pet's bowl and not a red disc or a frisbee
    S.filler("dog_bowl", 1100, 968, "Dog bowl", lambda x, y: (D.ell(x, y, 30, 11, C["red"]) + D.ell(x, y - 6, 24, 6, "#8a2a2a", D.OW * 0.6)
                                                         + "".join(D.circ(x + dx, y - 7 + dy, 3.4, C["wood"], D.OW * 0.35) for dx, dy in ((-12, 0), (-5, -2), (3, 1), (10, -1), (-8, 2), (6, -3), (14, 1))),
                                                         (x - 32, y - 14, x + 32, y + 12)), (1070, 950, 1130, 985),
             # revision 19: and only beside one ("a full food bowl with no pet near it", "far from the dog")
             needs=lambda sc: any(f.startswith(("animal.dog", "animal.cat")) for f in sc.fams) and
                              (_rev() < 19 or any(a.family.startswith(("animal.dog", "animal.cat")) and not a.m["variant"].get("airborne")
                                                  and abs(a.X - 1100) < 260 and abs(a.Y - 968) < 170 for a in sc.assets.values())))
    if "clothesline" in features:
        S.filler("basket", 890, 708, "Laundry basket", lambda x, y: D.laundry_basket(x, y), (840, 690, 945, 720))
    return S


# ======================================================================= park
def build_park(features, sky):
    S = SettingInstance("park", sky)
    S.horizon = 520
    S.features = set(features)
    sky_layer(S, sky, 520, sun_at=(1430, 110), clouds=((520, 120, 0.65), (860, 90, 0.5)), dark=((520, 110, 1.05), (800, 80, 1.0), (1040, 140, 0.75)))
    S.add("hills", "Hills in the distance", D.hills(440), -97, "setting", (-10, 360, 1610, 560),
          entity=E("There are hills in the distance", ["hills", "hill", "mountains", "countryside"], "hills"))
    S.add("tree_line", "Trees in the distance", D.tree_line(540), -96, "background", (-10, 440, 1610, 545))
    S.add("ground", "Grass", D.rect(-10, 520, D.W + 20, 490, C["grass"], 0, 0), -90, "background")
    path = D.flat("M 1040 1010 C 1100 860 1300 760 1200 640 C 1150 580 1180 545 1220 522 L 1262 522 C 1240 548 1220 585 1262 640 C 1380 770 1220 880 1240 1010 Z", C["path"])
    path += f'<path d="M 1040 1010 C 1100 860 1300 760 1200 640 C 1150 580 1180 545 1220 522 M 1262 522 C 1240 548 1220 585 1262 640 C 1380 770 1220 880 1240 1010" fill="none" stroke="{D.OUT}" stroke-width="{D.OW * 0.8}"/>'
    S.add("path", "Path", path, -80, "setting", (1040, 520, 1330, 1000), entity=E("There is a path", ["path", "walkway", "trail", "footpath", "sidewalk"], "path"))
    S.anchors["path"] = {"x0": 1100, "x1": 1260, "y0": 640, "y1": 990, "edges": path_edges(
        ((1040, 1010), (1100, 860), (1300, 760), (1200, 640)), ((1240, 1010), (1220, 880), (1380, 770), (1262, 640)))}
    S.add("pond", "Pond", D.pond(470, 650, 330, 78), -70, "setting", (130, 560, 810, 730),
          entity=E("There is a pond", ["pond", "lake", "water"], "pond"))
    S.blocked.append((100, 560, 840, 800))     # keep feet well clear of the water's edge
    S.anchors["pond"] = {"center": (470, 650), "rx": 330, "ry": 78,
                         "swim": [(300, 640), (420, 672), (560, 628), (660, 662), (380, 612), (250, 676), (520, 700)],
                         "shore": [(860, 700), (850, 745), (95, 740), (700, 835), (560, 840), (360, 840)]}
    # just in front of the water: anyone standing here has their legs over the pond and looks as if wading
    S.soft.append((140, 728, 800, 852))
    tsvg, tinfo = D.tree_with_branch(1400, 760, sz(760), side=-1, smooth=_rev() >= 6)
    S.add("tree", "Big tree", tsvg, 760, "setting", tinfo["bbox"], entity=E("There is a big tree", ["tree", "trees", "big tree"], "tree"),
          blocked=(1350, 730, 1450, 800))
    S.blocked.append((1250, 560, 1570, 760))      # behind the big tree, where the canopy would hide a person
    S.anchors["tree"] = tinfo
    t2, i2 = D.tree(110, 575, sz(575) * 0.85, trunk_h=130)
    S.add("tree_small", "Small tree", t2, 575, "setting", i2["bbox"], blocked=(70, 555, 150, 600))
    S.anchors["tree_small"] = i2
    ls, li = D.lamp(930, 640, sz(640), 520)
    S.add("lamp", "Lamp post", ls, 640, "setting", li["bbox"], entity=E("There is a lamp post", ["lamp post", "lamp", "street light", "light post", "lamppost"], "lamp"),
          blocked=(905, 620, 955, 660))
    S.anchors["lamp_top"] = (li["top"][0], li["top"][1] + 2, 640)
    S.walk = [(30, 560, 1570, 992)]
    if "bench" in features:
        s = sz(830)
        bs, bi = D.bench(1080, 830, s, 210)
        S.add("bench", "Park bench", bs, 830, "setting", bi["bbox"], entity=E("There is a park bench", ["bench", "park bench", "seat"], "bench"),
              blocked=(bi["bbox"][0] - 20, 800, bi["bbox"][2] + 20, 900))
        S.anchors["bench"] = {"seat_y": bi["seat_y"], "x0": bi["x0"], "x1": bi["x1"], "depth": 830, "front_y": 880, "back_y": bi["bbox"][1] + 8}
    if "flowers" in features:
        fb, bb = D.flowerbed(300, 900, sz(900), n=7, rx=115)
        S.add("flowers", "Flower bed", fb, 936, "setting", bb, entity=E("There are flowers", ["flowers", "flower bed", "flowerbed"], "flowers"),
              blocked=(160, 840, 440, 950))
        S.anchors["flowers"] = {"center": (300, 870), "bbox": bb, "stand_left": (500, 930), "stand_right": (110, 930), "depth": 936}
        S.soft.append((bb[0] - 30, bb[1] + 40, bb[2] + 30, 1000))
    if "blanket" in features:
        bl, bb = D.blanket(660, 880, sz(880))
        S.add("blanket", "Picnic blanket", bl, -60, "setting", bb, entity=E("There is a picnic blanket", ["blanket", "picnic", "picnic blanket"], "picnic"))
        S.anchors["blanket"] = {"spots": [(600, 885), (720, 870)], "bbox": bb}
        S.soft.append((bb[0] - 10, bb[1] - 10, bb[2] + 10, bb[3] + 40))
    S.filler("bush_l", 60, 640, "Bush", lambda x, y: (D.bush(x, y, 0.8), (x - 62, y - 52, x + 62, y + 26)))
    S.filler("bush_r", 1540, 650, "Bush", lambda x, y: (D.bush(x, y, 0.8), (x - 62, y - 52, x + 62, y + 26)))
    S.filler("bush_b", 860, 560, "Bush", lambda x, y: (D.bush(x, y, 0.6), (x - 46, y - 40, x + 46, y + 20)))
    S.filler("bin", 978, 652, "Bin", lambda x, y: (D.bin_(x, y, sz(y)), (x - 32 * sz(y), y - 82 * sz(y), x + 32 * sz(y), y)), (950, 630, 1010, 670))
    S.filler("rock", 840, 960, "Rock", lambda x, y: D.rock(x, y), (790, 935, 890, 985))
    S.filler("bush_f", 1590, 960, "Bush", lambda x, y: (D.bush(x, y, 0.9), (x - 70, y - 60, x + 70, y + 30)), (1520, 920, 1600, 995))
    S.filler("bin_p2", 30, 980, "Bin", lambda x, y: (D.bin_(x, y, sz(y)), (x - 32 * sz(y), y - 82 * sz(y), x + 32 * sz(y), y)), (0, 945, 65, 995))
    return S


# ======================================================================= street
def build_street(features, sky):
    S = SettingInstance("street", sky)
    S.horizon = 600
    S.anchors["balloon_max_y"] = 255      # a loose balloon's string ends above the shop awnings
    S.features = set(features)
    sky_layer(S, sky, 600, sun_at=(1470, 80), clouds=((620, 70, 0.55), (980, 50, 0.45)), dark=((520, 70, 0.95), (820, 50, 0.9), (1100, 80, 0.7)))
    bld = D.facade(-10, 380, 170, 600, C["wall"], C["roof"], awning=C["red"], door_at=0.70)
    bld += D.facade(380, 760, 240, 600, C["wall2"], C["teal"], awning=None, door_at=0.35, windows=2)
    bld += D.facade(760, 1180, 130, 600, C["wall3"], C["slate"], awning=C["green"], door_at=0.62, windows=2)
    bld += D.facade(1180, 1610, 205, 600, C["wall4"], C["purple"], awning=C["orange"], door_at=0.25, windows=2)
    # v0.10: the shop awnings (revision 8 keeps an upward stream and flying birds clear of them)
    S.anchors["awnings"] = [(-18, 450, 394, 484), (752, 450, 1194, 484), (1172, 450, 1624, 484)]
    S.add("buildings", "Row of shops", bld, -95, "setting", (-10, 116, 1610, 600),
          entity=E("It is a street with shops", ["shops", "stores", "buildings", "street", "town", "city", "shop"], "shops"))
    pav = D.rect(-10, 600, D.W + 20, 410, C["paving"], 0, 0)
    for yy in (640, 690, 750, 820, 900, 990):
        pav += D.line(-10, yy, D.W + 10, yy, C["paving_line"], 2.5)
    for xx in range(-1200, 2900, 160):
        # lines converging on the vanishing point (800, -402)
        t0 = (600 + 402) / 1402.0
        x_top = 800 + (xx - 800) * t0
        pav += D.line(x_top, 600, xx, 1000, C["paving_line"], 2.5)
    pav += D.rect(-10, 596, D.W + 20, 10, C["gray"], 0, D.OW * 0.6)
    S.add("ground", "Paved street", pav, -90, "background", (-10, 596, 1610, 1000),
          entity=E("They are on a sidewalk", ["sidewalk", "pavement", "street", "plaza", "road"], "sidewalk"))
    ts, ti = D.tree_with_branch(300, 800, sz(800), side=1, smooth=_rev() >= 6)
    ts = ts + D.tree_planter(300, 806, sz(800))
    S.add("tree", "Street tree", ts, 800, "setting", ti["bbox"], entity=E("There is a tree", ["tree", "trees"], "tree"), blocked=(230, 770, 370, 830))
    S.blocked.append((170, 630, 430, 800))        # behind the tree
    S.anchors["tree"] = ti
    ls, li = D.lamp(1120, 700, sz(700), 540)
    S.add("lamp", "Street lamp", ls, 700, "setting", li["bbox"], entity=E("There is a street lamp", ["lamp post", "lamp", "street light", "light post", "lamppost"], "lamp"),
          blocked=(1090, 680, 1150, 720))
    S.anchors["lamp_top"] = (li["top"][0], li["top"][1] + 2, 700)
    S.walk = [(30, 630, 1570, 992)]
    if "stall" in features:
        st, si = D.fruit_stall(1400, 720, sz(720))
        S.add("stall", "Fruit stand", st, 720, "setting", si["bbox"], entity=E("There is a fruit stand", ["fruit stand", "fruit", "market", "stall", "fruit stall", "market stall"], "fruit"),
              blocked=(si["bbox"][0], 640, si["bbox"][2], 745))
        S.anchors["stall"] = si
    if "bench" in features:
        s = sz(770)
        bs, bi = D.bench(760, 770, s, 210)
        S.add("bench", "Bench", bs, 770, "setting", bi["bbox"], entity=E("There is a bench", ["bench", "seat"], "bench"),
              blocked=(bi["bbox"][0] - 20, 740, bi["bbox"][2] + 20, 830))
        S.anchors["bench"] = {"seat_y": bi["seat_y"], "x0": bi["x0"], "x1": bi["x1"], "depth": 770, "front_y": 820, "back_y": bi["bbox"][1] + 8}
    if "bicycle" in features:
        bk, bb = D.bicycle(540, 690, sz(690), rack=True, wide=_rev() >= 10)
        S.add("bicycle", "Parked bicycle", bk, 690, "setting", bb, entity=E("There is a bicycle", ["bike", "bicycle", "cycle"], "bike"), blocked=(bb[0] - 10, 630, bb[2] + 10, 712))
    if "flowers" in features:
        S.add("flowers", "Flower planter", D.planter(1000, 660, sz(660)), 660, "setting", (1000 - 64 * sz(660), 600, 1000 + 64 * sz(660), 660),
              entity=E("There are flowers", ["flowers", "flower box", "planter", "plants"], "flowers"), blocked=(920, 640, 1080, 680))
        S.anchors["flowers"] = {"center": (1000, 630), "bbox": (930, 600, 1070, 660), "stand_left": (1150, 690), "stand_right": (860, 690), "depth": 660,
                                "soil_y": 660 - 46 * sz(660) + 5}      # the top of the box, where the stream lands
        S.soft.append((910, 660, 1090, 720))
    S.filler("planter_a", 640, 640, "Planter", lambda x, y: (D.planter(x, y, sz(y)), (x - 64 * sz(y), y - 80 * sz(y), x + 64 * sz(y), y)), (570, 625, 710, 660))
    S.filler("bin_s", 1240, 930, "Bin", lambda x, y: (D.bin_(x, y, sz(y), C["slate"]), (x - 32 * sz(y), y - 82 * sz(y), x + 32 * sz(y), y)), (1205, 900, 1275, 950))
    S.filler("cafe", 160, 930, "Café table and chairs", lambda x, y: D.cafe_table(x, y, sz(y)), (60, 890, 260, 955))
    S.filler("pot_s", 1540, 950, "Flower pot", lambda x, y: (D.pot(x, y, C["grass_dark"], sz(y)), (x - 30, y - 90, x + 30, y)), (1505, 910, 1570, 970))
    S.filler("crates", 1560, 760, "Crates", lambda x, y: (D.crate(x - 20, y, sz(y) * 0.8)[0], (x - 60, y - 80, x + 40, y)), (1500, 730, 1590, 780))
    S.filler("planter_b", 860, 645, "Planter", lambda x, y: (D.planter(x, y, sz(y)), (x - 64 * sz(y), y - 80 * sz(y), x + 64 * sz(y), y)), (790, 630, 930, 665))
    S.filler("cafe_b", 480, 960, "Café table and chairs", lambda x, y: D.cafe_table(x, y, sz(y)), (380, 925, 580, 990))
    S.filler("bin_b", 120, 700, "Bin", lambda x, y: (D.bin_(x, y, sz(y), C["green"]), (x - 32 * sz(y), y - 82 * sz(y), x + 32 * sz(y), y)), (85, 670, 155, 720))
    S.filler("pot_s2", 60, 980, "Flower pot", lambda x, y: (D.pot(x, y, "#4fae4a", sz(y)), (x - 30, y - 90, x + 30, y)), (30, 945, 95, 995))
    S.filler("bike_rack", 1000, 975, "Parked bicycle", lambda x, y: D.bicycle(x, y, sz(y), col=C["red"], rack=True, wide=_rev() >= 10), (900, 940, 1100, 995))
    return S


# ======================================================================= playground
def build_playground(features, sky):
    S = SettingInstance("playground", sky)
    S.horizon = 560
    S.features = set(features)
    sky_layer(S, sky, 560, sun_at=(240, 110), clouds=((760, 110, 0.6), (1080, 80, 0.5)), dark=((560, 100, 1.0), (840, 75, 1.0), (1100, 130, 0.75)))
    S.add("tree_line", "Trees behind the playground", D.tree_line(560, step=66), -96, "background", (-10, 470, 1610, 565))
    S.add("ground", "Grass", D.rect(-10, 560, D.W + 20, 450, C["grass"], 0, 0), -90, "background")
    # revision 14: the railing as tall as a real one at its depth, about 0.85 m (drawn 0.4 m tall, a woman standing at it
    # was "drawn about four times the fence height, looming over the hedge")
    rtop = 618 - 0.85 * D.ppm(616) if _rev() >= 14 else 560
    rail = D.railing(rtop, 618, mids=(0.36, 0.68) if _rev() >= 14 else None)
    S.add("fence", "Railing around the playground", rail, 618, "setting", (-10, rtop - 6, 1610, 618),
          entity=E("There is a railing around the playground", ["fence", "railing", "playground fence"], "fence"))
    S.anchors["fence_top"] = {"y": rtop - 4, "x0": 60, "x1": 1540, "depth": 616}
    tsvg, tinfo = D.tree_with_branch(1460, 700, sz(700), side=-1, smooth=_rev() >= 6)
    S.add("tree", "Big tree", tsvg, 700, "setting", tinfo["bbox"], entity=E("There is a big tree", ["tree", "trees", "big tree"], "tree"),
          blocked=(1410, 670, 1510, 730))
    S.blocked.append((1300, 620, 1610, 700))      # behind the big tree
    S.anchors["tree"] = tinfo
    S.walk = [(30, 630, 1570, 992)]
    if "slide" in features:
        sl, si = D.slide(230, 720, sz(720), f=1, ladder2=_rev() >= 10)
        S.add("slide", "Slide", sl, 720, "setting", si["bbox"], entity=E("There is a slide", ["slide", "playground slide", "slide"], "slide"),
              blocked=(si["bbox"][0] - 10, 630, si["bbox"][2] + 10, 750))     # on and behind the slide
        S.anchors["slide"] = si
    if "swing" in features:
        s = sz(690)
        x0, x1, top = 640, 900, 690 - 300 * s
        sw = D.stroke(D.poly_d([(x0 - 30 * s, 690), (x0, top)]), C["slate"], 11 * s) + D.stroke(D.poly_d([(x0 + 30 * s, 690), (x0, top)]), C["slate"], 11 * s)
        sw += D.stroke(D.poly_d([(x1 - 30 * s, 690), (x1, top)]), C["slate"], 11 * s) + D.stroke(D.poly_d([(x1 + 30 * s, 690), (x1, top)]), C["slate"], 11 * s)
        sw += D.stroke(D.poly_d([(x0 - 8, top + 2), (x1 + 8, top + 2)]), C["slate"], 12 * s)
        S.add("swing", "Swing set", sw, 690, "setting", (x0 - 40, top - 8, x1 + 40, 692), entity=E("There is a swing set", ["swing", "swings", "swing set"], "swing"),
              blocked=(x0 - 50, 630, x1 + 50, 760))
        seat = (770, 690 - 95 * s)
        S.anchors["swing"] = {"seat": seat, "rope_top": ((seat[0] - 28 * s, top + 6), (seat[0] + 28 * s, top + 6)), "depth": 690, "seat_w": 76 * s}
        empty = D.line(seat[0] - 28 * s, top + 6, seat[0] - 28 * s, seat[1], D.OUT, 3.5) + D.line(seat[0] + 28 * s, top + 6, seat[0] + 28 * s, seat[1], D.OUT, 3.5)
        empty += D.rect(seat[0] - 38 * s, seat[1] - 4, 76 * s, 11, C["red"], 3)
        S.add("swing_seat", "Empty swing seat", empty, 689, "setting", (seat[0] - 40 * s, top, seat[0] + 40 * s, seat[1] + 8))
    if "seesaw" in features:
        # revision 6: an empty seesaw rests with one end on the ground (level, it read as balanced on air)
        from . import scene as _SCN
        ss, si = D.seesaw(1185, 860, sz(860), tilt=-math.degrees(math.asin(82 / 212)) if _SCN.PLACEMENT_REV >= 6 else 0.0)
        S.anchors["seesaw"] = {"cx": 1185, "base_y": 860, "depth": 860}
        S.add("seesaw", "Seesaw", ss, 860, "setting", si["bbox"], entity=E("There is a seesaw", ["seesaw", "see-saw", "teeter-totter"], "seesaw"),
              blocked=(si["bbox"][0] - 20, 790, si["bbox"][2] + 20, 900))
    if "sandbox" in features:
        sb, si = D.sandbox(400, 935, sz(935))
        S.add("sandbox", "Sandbox", sb, -60, "setting", si["bbox"], entity=E("There is a sandbox", ["sandbox", "sandpit", "sand pit", "sand"], "sand"))
        S.anchors["sandbox"] = si
        S.soft.append((si["bbox"][0] - 10, si["bbox"][1] - 10, si["bbox"][2] + 10, 1000))
    if "bench" in features:
        s = sz(680)
        bs, bi = D.bench(1170, 680, s, 200)
        S.add("bench", "Bench", bs, 680, "setting", bi["bbox"], entity=E("There is a bench", ["bench", "seat"], "bench"),
              blocked=(bi["bbox"][0] - 20, 630, bi["bbox"][2] + 20, 740))
        S.anchors["bench"] = {"seat_y": bi["seat_y"], "x0": bi["x0"], "x1": bi["x1"], "depth": 680, "front_y": 728, "back_y": bi["bbox"][1] + 8}
    S.filler("bush_pl", 1330, 640, "Bush", lambda x, y: (D.bush(x, y, 0.75), (x - 58 * 0.75 * 1.2, y - 50, x + 58, y + 24)))
    S.filler("bin_pl", 560, 650, "Bin", lambda x, y: (D.bin_(x, y, sz(y)), (x - 32 * sz(y), y - 82 * sz(y), x + 32 * sz(y), y)), (530, 630, 590, 670))
    # in from the corners (a ball and a rock in the very corners looked dropped there by nobody)
    # (from revision 5 no ball lies on the grass with nobody playing with it)
    S.filler("ball_pl", 1470, 930, "Ball on the grass", lambda x, y: (D.ball(x, y - 18, 18, C["yellow"]), (x - 20, y - 38, x + 20, y + 2)), (1440, 905, 1505, 950),
             needs=lambda sc: __import__("scenegen.scene", fromlist=["PLACEMENT_REV"]).PLACEMENT_REV < 5)
    S.filler("rock_pl", 150, 940, "Rock", lambda x, y: D.rock(x, y, 0.8), (110, 915, 200, 960))
    S.filler("bush_pl2", 40, 650, "Bush", lambda x, y: (D.bush(x, y, 0.8), (x - 62, y - 52, x + 62, y + 26)))
    # revision 6: in the sandbox, not on the grass beside it (three readers saw toys "left behind")
    from . import scene as _SCN
    if _SCN.PLACEMENT_REV >= 6:
        S.filler("pail_pl", 500, 912, "Sand pail and spade", lambda x, y: D.sand_pail(x, y, 0.85), None,
                 needs=lambda sc: "sandbox" in sc.features and not any(t.id == "sandbox" for t in sc.templates))
    else:
        S.filler("pail_pl", 640, 985, "Sand pail and spade", lambda x, y: D.sand_pail(x, y, 1.0), (610, 960, 690, 995),
                 needs=lambda sc: "sandbox" in sc.features and not any(t.id == "sandbox" for t in sc.templates))
    return S


BUILDERS = {"garden": build_garden, "park": build_park, "street": build_street, "playground": build_playground}

# features each setting can offer, and which are on by default
FEATURES = {
    "garden": {"default": {"flowers"}, "optional": {"feeder", "clothesline", "laundry", "swing", "hose_reel", "bench", "flowers"}},
    "park": {"default": set(), "optional": {"bench", "flowers", "blanket"}},
    "street": {"default": {"stall"}, "optional": {"stall", "bench", "bicycle", "flowers"}},
    "playground": {"default": {"slide"}, "optional": {"slide", "swing", "seesaw", "sandbox", "bench"}},
}


def build(sid, features=(), sky="clear"):
    return BUILDERS[sid](set(features) | FEATURES[sid]["default"], sky)
