"""Scene under construction: cast binding, placement helpers, elements and items.

Templates call these helpers in two phases:
  bind(sc)   choose families and the variants they need (no geometry yet)
  place(sc)  position everything from the rendered manifests, add drawn extras and items
"""
import math
import random

import numpy as np

from . import draw as D
from .library import Placed, looks_at, vid
from .settings import build as build_setting

ADULTS = ("adult", "older_adult")
GROWN = ("adult", "older_adult", "teen")
KIDS = ("child",)
YOUNG = ("child", "teen")


CLOSED_EYES = ("content", "happy", "laughing", "sleepy")
EYES_MAY_CLOSE = {"jump", "jump_tuck", "cheer", "sit_swing", "clap", "sit_clap", "sit_ground", "eat_apple", "sit_apple", "eat_ice_cream",
                  "sit_ice_cream", "walk_ice_cream", "drink", "sit_drink", "lie_down"}
# v0.15 (revision 13): poses that bow the head over a task; their "focused" face, half-lidded and seen from above,
# read as closed eyes ("the sweeping boy's eyes look closed or squinting"), so they look on with the plain face
HEAD_DOWN_TASKS = {"sweep", "rake", "sweep_giant_fork", "dig_lift", "kneel_plant", "water_plants", "water_pan", "hose_spray",
                   "paint", "push", "sand_build", "feed_birds_low", "fish", "hang_washing", "photo"}
# v0.16 (revision 14): readers bow the head over the page in the same way ("the boy's eyes look closed or downcast ...
# reading intently ... or dozing"), so they too read with the plain, open-eyed face
READING_POSES = {"sit_read", "walk_read_open", "walk_read", "seesaw_low_read", "read", "sit_air_read"}
# v0.16 (revision 14): poses that walk or run somewhere; the ground just ahead of the leading foot stays clear of other
# events' people, animals and things ("child walking toward the ladder might bump into it", "girl and dog walking toward
# the hose ... might trip over it": an unintended "about to happen" beside the real ones)
WALK_POSES = {"walk", "walk_dog", "walk_bag", "walk_box", "walk_basket", "walk_balloon", "walk_ice_cream", "walk_umbrella",
              "run", "push", "carry_box", "carry_bag"}

# where free-standing characters prefer to go: big, near the front in Tier 1; smaller, further
# back in Tier 4 (cue size is one of the model's radicals)
FRONT_BIAS = {1: 0.65, 2: 0.40, 3: 0.12, 4: -0.30}


class PlacementError(Exception):
    pass


# Placement revision. 1 = the rules the first v0.5 pictures were made with; 2 adds the structure check
# below at placement time (a person may not be put where a slide, swing, tree, bench, lamp or other
# standing structure would cover or back their head, or cross their body), plus three template fixes;
# 3 keeps the air under a lost balloon's string free of other people and paints the fence boards
# themselves (not a see-through panel over the fence); 4 (v0.6) adds clearance around heads and hands,
# keeps people's bodies out of structures they do not use, and keeps the air under a loose string clear
# of structures as well as people; 5 (v0.7) redraws the six templates the v0.6 screen could not read
# (fork sweeping, heavy seesaw, bird stealing, feeding the birds, lost balloon, jumping) and keeps
# owner-less props, free-standing bicycles and aimless photographers out of the pictures; 6 (v0.8)
# redraws the giant fork as cutlery and fixes the other templates the v0.7 screen could not read
# (stalking cat, dog wanting a walk, bird stealing, sandbox, grazing goat, waving, lost balloon, rain
# coming) plus the seesaw tilt, the sand toys and the paint-track paws; 7 (v0.9) redraws the four
# templates the v0.8 screen could not read (heavy seesaw, dog begging, about to trip, lost balloon) and
# fixes the oddities it reported (sprinkler without a hose, painting without paint, a wheelbarrow with
# one handle, a swing rider off the seat, matching balls of different events, standing on the slide);
# 8 (v0.10) redraws the dropped ice cream and fixes the placements the v0.9 screen and its retest
# found (a fork sweeping on stepping stones, a floating box by the house, a walker and a fence cat by the
# clothesline, a bird over a roofline, an upward stream at an awning, the child at the foot of the slide,
# a small sleeping cat, the duck and the bread) and the oddities it reported (a stepping stone behind a
# lying dog, an outsized sandwich, a teenager on a seesaw barely tipped, a photographer from behind);
# 9 (v0.11) fixes the five templates the v0.10 screen could not read (a waver at the house corner, the
# ball in the tree beside a blowing hat, a kite drawn in front of the canopy, a storm pointer under a
# tree, a play bow facing a wheelbarrow) and the oddities it reported (the smaller child down on the
# seesaw, a basket over the sitter's legs, the dustpan apart from the heap, a hat against the wind);
# 10 (v0.12) redraws the five templates the v0.11 screen could not read (a kick read as a bat, a digger
# read as resting, a play bow read as a stretch, a floating box low against the fence, a square wheel
# read as a box in front of the wheel), each refined on its own before going back into the scenes, and
# fixes the oddities it reported (a detached slide ladder, a squashed bicycle, outsized
# pecking birds, people on the pond's edge, a dog behind the house corner), with ground shadows under
# the wheelbarrow, the bicycle and the kicked ball; inspecting the set added the play bow and the square-wheeled
# object off the sandbox, the blanket and the pond's rim, the hole inside the picture, and the storm pointer
# apart from anything up in a tree or the sky.
# 11 (v0.13) redraws the one template the v0.12 screen could not read (an animal on the hose read as "on or
# right next to" it, the stopped water as "not turned on yet") and the half points and oddities it reported
# (a stalking cat "or just running past", sleeping pets read as collapsed, a floating box's far shadow, a kicked
# ball heading for a child, a throw arcing at a cat on the fence, leaves pasted on a kite, a gust with balloons
# hanging still, a square-wheeled bicycle with no stand, a girl at the seesaw's raised end, a long pram handle,
# a child kneeling on the sandbox rim, a fence bird keyed as pecking the ground), each refined on its own first;
# the design tests added the hose's ground run kept clear of feet, open ground round a curled-up sleeper, the
# sleeping dog nearer the front, the pram clear of the market stall and the gust stripping leaves off the tree;
# inspecting the set added the flying kite clear of the clouds, nobody beside the ladder that leans on nothing,
# and no perched bird on the branch of a tree with something caught in it.
# 12 (v0.14) redraws the three templates the v0.13 screen could not read (a stalking cat read as "running toward"
# the bird beside a passing girl, a girl stuck up on the seesaw read as "nothing wrong there", a child's wave read as
# "waving or listening") and the oddities it reported (a girl seemingly on an empty seesaw, a square-wheeled bicycle
# standing on its own, wind that moved only the hat, a ball drawn on top of the tree, a kite string meeting the tail,
# the black cat asleep, an outsized dropped scoop, a lead round the dog's middle), each refined on its own first.
# 13 (v0.15) aims the wave only at someone going about their day and fixes the v0.14 oddities (a bucket beside the
# walker's line, still washing beside a kite, the garden's bush, bird table and swing frame, hoses across paths, closed eyes
# on chores, a lost balloon of another child's colour, a bird in a crown with no branch, sleepers in the street).
# 14 (v0.16) fixes the three templates the v0.15 screen failed (a stalking cat with a second cat on its fence and a
# pointing hand beside it, a girl stuck on the seesaw read as playing, a fence bird under the clothesline) and the
# oddities it reported (people at the back too big for the playground's railing, unrelated figures over each other's
# feet, walkers heading into other events' things, a catch arcing over the catcher, readers' downcast eyes).
# 15 (v0.17): the v0.16 screen's oddities (the sprinkler's drops above the box it soaks, a bird on the playground
# railing in front of the slide, a pram's lane stopping short of figures just behind it, figures touching a bench or the
# pond's rim at the same depth, things cut off by the picture's edge) and a photographer only ever with someone to
# photograph; inspecting the set added no empty picnic blanket and the sprinkler's spray kept off the blanket.
# 16 (v0.18): the v0.17 screen's failure and oddities: a waving hand kept clear of the backdrop's outlines and no waver at
# the far back (a small girl's raised hand on the hedge line read as "holding a string"), a body gap between figures of
# different events at the same depth (two "squashed together, one partly inside the other"), the ground behind a catcher
# kept clear, fillers well inside the frame, and a duck's wake kept off figures; inspecting the set added no sprinkler
# under the storm clouds of a rain warning, a fishing line and its float kept off figures, and no picnic in a picture
# with the soaked box.
# 17 (v0.19): the v0.18 screen's four failures and its oddities: no reader walking with a book under a gust of wind and
# none at the far back (open pages beside wind lines read as "a newspaper ... or papers in the wind"), the stalking cat on
# the fence close to a bird perched there (well over a cat's length off, it read as walking along the fence), no hose
# reel beside the frying pan (beside a reel it read as "a hose nozzle"), motion lines behind a runner ("striding or
# jogging"); a gap between a person and the thin parts of standing structures and the stall's legs (a woman "tightly
# overlapping the lamp post", a photographer "inside the swing frame"), the begging dog clear of the eater's legs, the
# child under a ball stuck in a tree, the kicked ball just ahead of the foot, the painted boards in front of the brush,
# and water from a hose or sprinkler drawn unbroken (dashed, it was "a dotted line"); inspecting the set added no hand
# over the stall's crates of fruit (a runner's hand on the apples looked like snatching one), and a runner and the
# runner's motion lines clear of the stall; and searching the set, never the playground's seesaw with its bench (the
# seesaw stands right in front of it, so with the gap from thin parts nobody could sit there).
# 18 (v0.20): the v0.19 screen's four failures and its oddities: no ice-cream eater beside the dropped ice cream
# (walking toward the boy who dropped his, "maybe to share it"), and no runner either ("could have bumped the child");
# no bird above or beside a jumper's raised hands (read as reaching for it); no watering can left on the lawn beside the
# frying pan, and the water from a can, a pan or a hose landing inside the flower bed; the garden's wheelbarrow standing
# on its wheel and legs ("very flat ... no visible legs"); the blown empty swing seat inside its frame; the dug hole
# clear of the path, the leaning ladder clear of the pond and animals' feet clear of the sandbox frame.
# 19 (v0.21): the v0.20 screen's oddities: no road worker in the hi-vis vest in a home garden; a dog bowl only beside a
# dog or cat; heads clear of the washing on the line, and no fence painted behind it; no hose reel beside a watering
# can, no spare can beside a hose, one hose per picture, and a can's water further into the bed; people and animals
# clear of the pond's cattails and rim; figures of different events up to about 80 px apart in depth kept off each
# other's heads; and a kick's line clear of the sandpit and of people further off.
# 20 (v0.22): the v0.21 screen's three failures and its oddities: no frying pan in the street (held against a grey shop
# door at a planter it read as "a grey watering can"); a jumper clear of standing structures behind (in front of the
# fruit stall he read as standing with his arms up); a leaning ladder whose top rises above the lawn's far edge, clear of
# other uprights' feet (on open grass it read as "standing ... or lying flat"); nobody's feet over another event's thing
# on the ground (a boy's foot on a wheelbarrow's handles: "about to trip over" them); nothing on the ground ahead of a
# reading walker past the obstacle meant for her (a sleeping cat, a bicycle), no flower bed or rock anywhere on a
# runner's line, and a kick's line clear of people further back too; and a sprinkler's hose that never runs straight
# off the bottom of the picture ("like a stiff pipe"), nor across the legs of anyone just in front of it (added after
# inspecting the probes: a begging dog drawn as if standing on it). A jumper also stays in the front half of the ground
# (design tests: at the back the gap under the feet was too small to read).
# 21 (v0.23): the v0.22 screen's oddities: the reading walker's obstacle a full step ahead of her leading toe (25 px ahead
# it lay "to the side of / slightly ahead of" her); no runner and other mover heading straight at each other on one line
# (a runner and a woman with a pram "might bump into each other"); no duck at an angler's float or on the line ("might go
# for the bait or get tangled in the line"). After the design tests: a runner's lane deeper behind her line (a cat stalking a
# bird just outside it was what she seemed to run at), and no duck facing an angler's float; and after their second round, a
# runner 50 px clear of any other mover beside her on her line (running past a man with a pram, "almost touching").
# 22 (v0.24): the v0.23 screen's oddities: a sleeping animal clear of any walker's feet on both sides, not only ahead of
# him (a cat 50 px behind a walking man's back foot, "right by his feet, so he could trip over it or step on it"); and in
# the park and on the playground, nobody on the ground in the last strip before the horizon (a figure there was "drawn as
# large as foreground people ... as if walking on the hilltop", four pictures, all with the feet within 75 px of it).
# 23 (v0.25): the v0.24 screen's oddities, each chosen on the bench (vision/isolation_v025.md): the bird at the sandwich 0.8 of its
# size and the sandwich smaller with it ("about as big as the sandwich", "a blue kettle or jug"); and the newspaper drawn behind the
# dog with no paws painted over it, so the dog's own paws rest on it ("white gloved hands", "stuck onto" the paper).
# 24 (v0.26): the v0.25 screen, each drawing chosen on the bench (vision/isolation_v026.md): a heap of leaves at the sweeper's broom ("no visible
# rubbish or leaf pile for the old man to sweep"); the dog at the door with open eyes ("with its eyes shut", its wish never stated); a heaped
# sandcastle, back from the sandbox's front rim ("a cardboard or wooden model", "its base seems to overlap the wooden frame"); bread-coloured
# crumbs ("small stones or tiny fish"); a pale photo on the newspaper with no outline ("a dark square ... something the paw is holding"); and
# nobody up against a lamp post, in front of it or beside it ("the post looks almost as if it grows out of his shoulder").
# 25 (v0.27): the v0.26 screen, each drawing chosen on the bench (vision/isolation_v027.md): a hose rising to the fist from just under it, from the ground close by ("seems to end
# at a rounded tip near her hip", "like a stiff loop standing in the air"); a lumpy heap of soil ("a neat flat-bottomed dome", "a thin brown arch"); two short drips on the soaked
# box (running down its front they read as slats: "a wooden crate"); nobody sitting on air at a path's edge ("sitting in mid-air or on the edge of the path"); and a duck's wake
# kept on the water ("wake lines run past the pond edge onto the grass").
# 26 (v0.28): the v0.27 screen's one failure and its named oddities, each drawing chosen on the bench (vision/isolation_v028.md): the begging dog at the end of the bench the eater sits nearest, its gaze on the
# food, and nobody else near it, now or later ("could be hers, begging from her bag", "or be watching the kite"); shadows from the figure's own footprint ("a very wide oval, much wider than the puppy"); one shadow
# under the whole seesaw and its riders further in ("the girl has none of her own", "almost past it"); a burst splat for the fallen ice cream ("a pink hat or a pink frisbee", "flying saucer"), the dog's mouth over it;
# no walking with closed eyes ("Walking with eyes shut is slightly odd"); a beach ball on a branch that grows from a fork at the top of the trunk ("a blue planet-like sphere", "a small bare branch drawn on top of the
# crown"), and a bird's branch the same way; and one bin to a picture ("two bins so close to each other seem like more bins than the scene needs").
# Every record stores the revision it was made with, so it can be rebuilt exactly.
# 27 (v0.29): the v0.28 screen's failures and named oddities, each drawing chosen on the bench (vision/isolation_v029.md): the sleeping dog lying three-quarters with its chin on its paws ("sniffing the grass, lying
# down, or curled up asleep"); the duck with its head bent over a crumb, so eating is drawn ("swimming towards those crumbs"); the dog beside the door and turned to it, its lead hanging from its mouth, its tail in ("sits
# with a red lead in its mouth"); a wide box across the walker's line, a little nearer ("might pass beside it"); a slack hose, and one line from the fist to the ground ("like a rigid pipe", "could read as a post"); a
# slimmer swelling with no highlight on the stopped hose ("a separate slug-shaped object"); a fish on a limb, well out from the trunk ("pasted onto the leaves"); and rules for readings that excused a contradiction: no
# ladder within 160 px of a lamp post ("meant to lean on the lamp post"), no soaked box with a second box ("the two boxes look similar"), no bucket on the head under storm clouds ("a makeshift rain hat").
# 28 (v0.30): the v0.29 screen's named oddities, each drawing chosen on the bench (vision/isolation_v030.md): the hose hanging from the fist as a rope hangs and running on up to the fist in front of the figure, for the
# square piece over the joint ("seems to stop at about waist height, then the part at her hands starts again"); the fish's limb with no other arm, and so no tuft ("looks detached from the rest of the crown"); the
# thrown crumbs only on the water ("several crumbs lie on the grass past the pond edge"); and the end of the hose lying on the grass with its nozzle on, when nobody has the hose, and gone when somebody has
# ("only a short stub of hose joined to nothing", "a short second stub of hose curls by the reel").
# 29 (v0.31) seats a seesaw's riders astride the plank, the far leg behind it and the rest in front, and raised so the hips rest on it ("the man's legs appear to go through or around the plank"); the castle further from the
# spade, so the hand and the spade show ("the hand and castle merge a little"); the reel down and to the left, off the bed's edge ("partly overlapping the edge of the flower bed"); and no washing under storm clouds ("taking it down because of the coming storm").
PLACEMENT_REV = 29
WORKER = "person.jo"
BACK_STRIP = 90   # revision 22: the strip of open ground behind the horizon line that people on the ground keep out of


def head_box(p):
    """Revision 19: the box round a person's head, from the head-top, eye and mouth anchors (the raised arms left out)."""
    b = p.bbox()
    h = b[3] - b[1]
    if not (p.has_anchor("head_top") and p.has_anchor("mouth")):
        return (b[0], b[1], b[2], b[1] + 0.25 * h)
    ht, mo = p.anchor("head_top"), p.anchor("mouth")
    xs = [ht[0], mo[0]] + [p.anchor(k)[0] for k in ("eye_L", "eye_R") if p.has_anchor(k)]
    cx = (min(xs) + max(xs)) / 2
    w = max(0.16 * h, max(xs) - min(xs) + 0.08 * h)
    return (cx - w / 2, ht[1], cx + w / 2, mo[1] + 0.05 * h)
LEISURE7 = {"about_to_trip"}
LEISURE = {"ball_in_tree", "balloon", "bird_steals", "bucket_hat", "carry_bag", "dog_begs", "drink_bench", "ducks_bread",
           "feed_birds", "fishing", "fly_kite", "hang_laundry", "ice_cream", "ice_cream_drop", "jump", "kick_ball", "kite_in_tree",
           "lost_balloon", "photo", "picnic", "play_catch", "push_stroller", "read_bench", "run", "sitting_on_air", "walk_dog"}
_MASKS, _THIN = {}, {}


def structure_masks(S, exempt=()):
    """Union mask and thin-stroke mask (half resolution, unmirrored) of the setting's standing structures."""
    from . import compose as K
    import numpy as np
    keys = []
    for e in S.elements:
        if e["role"] in K.BACKGROUND_ROLES or e["id"] in K.BACKDROP_IDS or e["id"] in exempt or not e.get("svg"):
            continue
        k = (e["id"], hash(e["svg"]))
        if k not in _MASKS:
            m = K.alpha_mask(dict(e, kind="svg"), False)
            _MASKS[k] = m
            _THIN[k] = K.thin_part(m)
        keys.append(k)
    if not keys:
        return None, None
    return np.logical_or.reduce([_MASKS[k] for k in keys]), np.logical_or.reduce([_THIN[k] for k in keys])


_OUTLINES = {}


def backdrop_outlines(S):
    """Revision 16: where the setting's backdrop draws its dark outlines (hill and hedge lines, the ground's edge, fence
    tops, roofs, awnings, windows, the path's edges), as a half-resolution mask of the composited backdrop."""
    from . import compose as K
    import numpy as np
    els = [(i, e) for i, e in enumerate(S.elements) if e.get("svg") and (e["role"] in K.BACKGROUND_ROLES or e["id"] in K.BACKDROP_IDS)]
    key = tuple((e["id"], hash(e["svg"])) for _, e in els)
    if key not in _OUTLINES:
        body = "".join(e["svg"] for _, e in sorted(els, key=lambda q: (q[1]["z"], q[0])))
        im = np.asarray(K.render_png(K.svg_doc(body), int(D.W * K.MASK_SCALE)).convert("RGB")).astype(int)
        _OUTLINES[key] = (im < 60).all(axis=2)
    return _OUTLINES[key]


class Scene:
    def __init__(self, tier, setting_id, seed, lib, sky="clear"):
        self.tier, self.setting_id, self.seed, self.lib, self.sky = tier, setting_id, seed, lib, sky
        self.rng = random.Random(seed)
        self.S = None
        self.features = set()
        self.assets = {}        # eid -> Placed
        self.svgs = {}          # eid -> element dict
        self.items = []
        self.events = []        # one per template instance (scene load)
        self.fams = set()
        self.variants = []
        self.consumed = set()   # setting entities used as a template's object
        self.checks = {}
        self.templates = []
        self.n_eid = 0
        self.mirror_scene = False
        self.knob = 0           # inference difficulty knob: -1 easier cues, 0 default, +1 harder cues
        self.legib_ok = set()   # (element, person) pairs allowed to overlap: the bench someone sits on, the line they hang washing on
        self.keepout = []
        self.airzones = []
        self.groundzones = []
        self.no_dog = []
        self.ev_of = {}

    def reset_layout(self, seed):
        """Forget every placement (keep the cast and variants) so the layout can be tried again."""
        self.assets, self.svgs, self.items, self.events = {}, {}, [], []
        self.consumed, self.checks = set(), {}
        self.legib_ok = set()
        self.strings = []
        self.stalk_spans = []   # revision 12: the ground between a stalking cat and its bird, kept free of strings
        self.keepout = []       # revision 4: ground boxes no one's feet may stand in (a sprinkler and its spray)
        self.airzones = []      # revision 4: boxes of air no person or animal may enter (around a floating box)
        self.sprayzones = []    # revision 19: (box, depth) of a sprinkler's spray: no person or animal in front of it
        self.floats, self.fish_lines = [], []   # revision 21: anglers' floats and lines, kept clear of ducks
        self.groundthings = []  # revision 20: (box, owner) things of an event lying or standing on the ground: no one else's feet on them
        self.no_dog = []        # revision 6: ground no dog may enter (around a stalking cat)
        self.groundzones = []   # revision 9: boxes nothing placed later may enter, drawn objects included (around the dropped ice cream)
        self.point_lines = []   # revision 14: a pointing hand's line to what it points at, kept clear of people and animals
        self.lanes = []         # revision 14: (box, owner) the ground just ahead of a walker, kept clear of other events
        self.placing = None     # revision 14: the template instance being placed
        self.ev_of = {}         # element id -> the event that drew it
        self.n_eid = 0
        self.rng = random.Random(seed)

    # ------------------------------------------------------------ binding
    def eid(self, base):
        self.n_eid += 1
        return f"{base}_{self.n_eid}"

    def person(self, kinds=None, avoid=(), prefer=()):
        # revision 6: the road worker in the hi-vis vest is cast only in work and outdoor chores (at a
        # picnic, pushing a pram or walking a dog the outfit read as odd)
        if PLACEMENT_REV >= 6 and getattr(self, "binding", None) in LEISURE:
            avoid = tuple(avoid) + (WORKER,)
        # revision 7: nor reading a book as he walks along (the worker "reading or writing in a small red book")
        if PLACEMENT_REV >= 7 and getattr(self, "binding", None) in LEISURE7:
            avoid = tuple(avoid) + (WORKER,)
        # revision 19: nor anywhere in the home garden (painting the fence or pointing at the clouds, "a road worker in a
        # hi-vis vest ... out of place in a home garden")
        if PLACEMENT_REV >= 19 and self.setting_id == "garden":
            avoid = tuple(avoid) + (WORKER,)
        pool = [f for f in self.lib.people(kinds) if f not in self.fams and f not in avoid]
        if not pool:
            raise PlacementError(f"no free person of kind {kinds}")
        if prefer and PLACEMENT_REV >= 4:
            pref = [f for f in pool if f in prefer]
            pool = pref or pool
        f = self.rng.choice(sorted(pool))
        self.fams.add(f)
        return f

    def animal(self, kinds, prefer=()):
        pool = [f for f in self.lib.animals(kinds) if f not in self.fams]
        if PLACEMENT_REV >= 12 and list(kinds) == ["cat"] and "cat_sleeping" in getattr(self, "picked_ids", ()):
            # revision 12: the sleeping cat is always the orange one, whose closed eyes show (when another event had
            # taken it, the small black cat asleep was "hard to make out: cat/kitten or small black dog"); every other
            # cat event leaves it free
            if getattr(self, "binding", None) == "cat_sleeping":
                pool = [f for f in pool if f == "animal.cat_02"]
            else:
                pool = [f for f in pool if f != "animal.cat_02"]
        if not pool:
            raise PlacementError(f"no free animal of kind {kinds}")
        if prefer and PLACEMENT_REV >= 5:
            pref = [f for f in pool if f in prefer]
            if pref:
                pool = pref
        f = self.rng.choice(sorted(pool))
        self.fams.add(f)
        return f

    def need(self, fam, pose, expr, yaw):
        # closed or squeezed-shut eyes hide what someone is looking at: keep them for moments of pure
        # feeling (jumping, swinging, a treat) and open the eyes for every task
        if PLACEMENT_REV >= 14 and fam.startswith("person.") and expr in ("focused", "content", "smile") and pose in READING_POSES:
            expr = "neutral"
        if fam.startswith("person.") and expr in CLOSED_EYES and pose not in EYES_MAY_CLOSE:
            expr = "smile"
        if PLACEMENT_REV >= 26 and fam.startswith("person.") and expr in CLOSED_EYES and pose == "walk_ice_cream":
            expr = "smile"      # revision 26: "Walking with eyes shut is slightly odd"
        if PLACEMENT_REV >= 13 and fam.startswith("person.") and expr == "focused" and pose in HEAD_DOWN_TASKS:
            expr = "neutral"
        v = (fam, pose, expr, int(yaw))
        self.variants.append(v)
        return v

    def name(self, fam):
        return self.lib.label(fam)["everyday_name"]

    def names(self, fam):
        return self.lib.label(fam)["accepted_names"]

    # ------------------------------------------------------------ geometry
    def placed(self, v, X, Y, mirror=False, depth_y=None, eid=None, role="scored"):
        return Placed(self.lib, vid(*v), X, Y, mirror, depth_y, eid, role)

    def mirror_for(self, v, want):
        """Mirror flag so the variant faces `want` (+1 right, -1 left)."""
        p = self.placed(v, 0, 800)
        f = p.facing()
        return f != 0 and f != want

    def scored_boxes(self, ignore=()):
        out = []
        for k, p in self.assets.items():
            if k not in ignore and p.role == "scored":
                out.append((k, p.bbox(), p.z))
        for k, e in self.svgs.items():
            if k not in ignore and e["role"] == "scored" and e.get("bbox"):
                out.append((k, e["bbox"], e["z"]))
        return out

    @staticmethod
    def overlap(a, b):
        w = min(a[2], b[2]) - max(a[0], b[0])
        h = min(a[3], b[3]) - max(a[1], b[1])
        if w <= 0 or h <= 0:
            return 0.0
        inter = w * h
        return inter / max(1.0, min((a[2] - a[0]) * (a[3] - a[1]), (b[2] - b[0]) * (b[3] - b[1])))

    def fits(self, bbox, ignore=(), limit=0.12, margin=8):
        if bbox[0] < margin or bbox[2] > D.W - margin or bbox[1] < margin or bbox[3] > D.H - 4:
            return False
        for k, b, _ in self.scored_boxes(ignore):
            if self.overlap(bbox, b) > limit:
                return False
        p = getattr(bbox, "asset", None)
        if p is not None and PLACEMENT_REV >= 2 and p.family.startswith("person.") and not self.clear_of_structures(p):
            return False
        if p is not None and PLACEMENT_REV >= 4 and p.family.startswith("animal.") and not self.animal_clear(p):
            return False
        if p is not None and PLACEMENT_REV >= 6 and not self.bird_gap(p, bbox, ignore):
            return False
        if p is not None and PLACEMENT_REV >= 18 and p.family.startswith("animal.bird"):
            # revision 18: no bird over or beside a jumper's raised hands (a boy jumping below a perched bird read as
            # reaching for it)
            for z in getattr(self, "no_bird", ()):
                if min(bbox[2], z[2]) > max(bbox[0], z[0]) and min(bbox[3], z[3]) > max(bbox[1], z[1]):
                    return False
        if p is not None and PLACEMENT_REV >= 18 and p.family.startswith("animal.") and not p.m["variant"].get("airborne") \
                and "sandbox" not in getattr(self, "exempt", ()):
            # revision 18: an animal's feet clear of the sandbox frame (a dog's back foot on it)
            sb = next((e["bbox"] for e in self.S.elements if e["id"] == "sandbox" and e.get("bbox")), None)
            if sb is not None:
                feet = (bbox[0], bbox[3] - 0.22 * (bbox[3] - bbox[1]), bbox[2], bbox[3])
                if min(feet[2], sb[2] + 8) > max(feet[0], sb[0] - 8) and min(feet[3], sb[3] + 6) > max(feet[1], sb[1] - 6):
                    return False
        if p is not None and PLACEMENT_REV >= 19 and (p.family.startswith("person.") or p.family.startswith("animal.")) \
                and not p.m["variant"].get("airborne") and "__swim__" not in p.v and not self.clear_of_pond_v19(bbox, p):
            return False
        if p is not None and PLACEMENT_REV >= 19 and p.family.startswith("person.") and "laundry" not in getattr(self, "exempt", ()):
            # revision 19: a head clear of the washing on the line (a shirt behind a man's head read as "part of his
            # outfit")
            lb = next((e["bbox"] for e in self.S.elements if e["id"] == "laundry" and e.get("bbox")), None)
            if lb is not None:
                hd = head_box(p)
                if min(hd[2], lb[2] + 10) > max(hd[0], lb[0] - 10) and min(hd[3], lb[3] + 10) > max(hd[1], lb[1] - 10):
                    return False
        if p is not None and PLACEMENT_REV >= 19 and (p.family.startswith("person.") or p.family.startswith("animal.")) \
                and not p.m["variant"].get("airborne"):
            # revision 19: nobody standing in front of a sprinkler's spray (a goat just in front of the arcs looked as if it
            # were grazing in the spray)
            for k, ky in getattr(self, "sprayzones", ()):
                if p.Y > ky and min(bbox[2], k[2]) > max(bbox[0], k[0]) and min(bbox[3], k[3]) > max(bbox[1], k[1]):
                    return False
        if p is not None and PLACEMENT_REV >= 20 and (p.family.startswith("person.") or p.family.startswith("animal.")) \
                and not p.m["variant"].get("airborne"):
            # revision 20: nobody's feet on another event's thing on the ground (a boy's foot over a wheelbarrow's handles
            # read as "about to trip over / run into" them)
            own = getattr(self, "placing", None)
            if self.feet_on_things(bbox, own):
                return False
        if p is not None and PLACEMENT_REV >= 21 and p.family.startswith("person.") and not self.headon_ok(p):
            # revision 21: no runner and other mover heading straight at each other on one line (a runner and a woman
            # pushing a pram 60 px apart in depth, facing each other, "might bump into each other if neither moves")
            return False
        if p is not None and PLACEMENT_REV >= 21 and p.family.startswith("animal.duck") and not self.clear_of_floats(bbox, p):
            # revision 21: no duck at an angler's float or line ("the duck might go for the bait or get tangled in the line"),
            # and none facing the float ("the duck is facing toward the float, so it may be about to swim over to it")
            return False
        if p is not None and PLACEMENT_REV >= 22 and self.sleeper_by_feet(p):
            return False
        if p is not None and PLACEMENT_REV >= 22 and p.family.startswith("person.") and self.setting_id in ("park", "playground") \
                and not p.m["variant"].get("airborne") and abs(p.Y - p.depth_y) <= 30 and p.Y < self.S.horizon + BACK_STRIP:
            return False
        if p is not None and PLACEMENT_REV >= 6 and p.family.startswith("animal.dog"):
            for z in getattr(self, "no_dog", ()):
                if min(bbox[2], z[2]) > max(bbox[0], z[0]) and min(bbox[3], z[3]) > max(bbox[1], z[1]):
                    return False
        if p is not None and PLACEMENT_REV >= 8 and p.family.startswith("animal.") and not p.m["variant"].get("airborne"):
            # revision 8: no animal on or against a stepping stone (a stone behind a lying dog's back read
            # as a saddle drawn over it)
            for st in self.S.anchors.get("path", {}).get("stones", ()):
                if min(bbox[2], st[2] + 6) > max(bbox[0], st[0] - 6) and min(bbox[3], st[3] + 6) > max(bbox[1], st[1] - 6):
                    return False
        if p is not None and PLACEMENT_REV >= 9 and p.family.startswith("person.") and not self.clear_of_house_edges(bbox):
            return False
        if p is not None and PLACEMENT_REV >= 10 and p.family.startswith("animal.") and not p.m["variant"].get("airborne") \
                and not self.clear_of_house_edges(bbox):
            # revision 10: animals too (a play-bowing dog's back end "cut off by the house wall")
            return False
        if p is not None and PLACEMENT_REV >= 10 and p.family.startswith("person.") and "pond" not in getattr(self, "exempt", ()) \
                and not self.clear_of_pond_edge(bbox):
            return False
        if PLACEMENT_REV >= 9:
            for k in getattr(self, "groundzones", ()):
                if min(bbox[2], k[2]) > max(bbox[0], k[0]) and min(bbox[3], k[3]) > max(bbox[1], k[1]):
                    return False
        if p is not None and PLACEMENT_REV >= 9 and self.strings:
            # revision 9: nothing placed after a kite stands on its string (a cat walking the fence where a
            # flying kite's string crossed it)
            for (ax, ay), (bx, by) in self.strings:
                n = max(2, int(math.hypot(bx - ax, by - ay) / 12))
                if any(bbox[0] - 8 <= ax + (bx - ax) * t / n <= bbox[2] + 8 and bbox[1] - 8 <= ay + (by - ay) * t / n <= bbox[3] + 8
                       for t in range(n + 1)):
                    return False
        if p is not None and PLACEMENT_REV >= 12 and (p.family.startswith("person.") or p.family.startswith("animal.")) \
                and "seesaw" in self.S.anchors and not ({"seesaw", "bench"} & set(getattr(self, "exempt", ()))):
            # revision 12: nobody stands at the seesaw's plank or its ends, ridden or not (by an empty seesaw a girl
            # "could look as if she is standing on it", a man "might be sitting in front of the seesaw's low end"); people
            # at the bench behind it are left to the bench's own rules
            sb = next((e["bbox"] for e in self.S.elements if e["id"] == "seesaw" and e.get("bbox")), None)
            if sb is not None:
                s_ = D.sz(self.S.anchors["seesaw"]["depth"])
                room = (sb[0] - 45 * s_, sb[1] - 30 * s_, sb[2] + 45 * s_, sb[3] + 15 * s_)
                if min(bbox[2], room[2]) > max(bbox[0], room[0]) and min(bbox[3], room[3]) > max(bbox[1], room[1]):
                    return False
        if p is not None and PLACEMENT_REV >= 4:
            for k in getattr(self, "airzones", ()):
                if min(bbox[2], k[2]) > max(bbox[0], k[0]) and min(bbox[3], k[3]) > max(bbox[1], k[1]):
                    return False
        if p is not None and PLACEMENT_REV >= 4 and getattr(self, "keepout", None):
            feet = (bbox[0], bbox[3] - 0.25 * (bbox[3] - bbox[1]), bbox[2], bbox[3])
            for k in self.keepout:
                if min(feet[2], k[2]) > max(feet[0], k[0]) and min(feet[3], k[3]) > max(feet[1], k[1]):
                    return False
        if PLACEMENT_REV >= 14 and not self.rev14_ok(bbox, p):
            return False
        return True

    # ------------------------------------------------------------ revision 14
    LANE_STRUCT = ("lamp", "tree", "tree_small", "stall", "swing", "swing_seat", "slide", "seesaw", "feeder", "hose_reel", "bench",
                   "clothesline", "sandbox", "pond", "bike_rack", "bicycle")

    def rev14_ok(self, bbox, p):
        """Revision 14: nothing of another event in the ground just ahead of a walker; no person or animal across a
        pointing hand's line to what it points at; and no person or animal over the feet of one of another event, nor
        with its own feet under one (a goat grazing over a woman's feet stood "partly through her legs")."""
        own = getattr(self, "placing", None)
        for z, who in getattr(self, "lanes", ()):
            if who is not own and min(bbox[2], z[2]) > max(bbox[0], z[0]) and min(bbox[3], z[3]) > max(bbox[1], z[1]):
                return False
        if p is None or not (p.family.startswith("person.") or p.family.startswith("animal.")):
            return True
        if PLACEMENT_REV >= 24 and p.family.startswith("person."):
            # revision 24: nobody up against a lamp post, in front of it or beside it, whatever the depth ("the post looks almost as if
            # it grows out of his shoulder", "she almost looks attached to it", "her foot and the post's base are almost touching")
            for e in self.S.elements:
                if e["id"] == "lamp" and e.get("bbox"):
                    cx = (e["bbox"][0] + e["bbox"][2]) / 2
                    m = 8 + 22 * D.sz(p.Y)
                    if bbox[0] - m < cx < bbox[2] + m:
                        return False
        g = (bbox[0] - 34, bbox[1] - 34, bbox[2] + 34, bbox[3] + 34)
        for a, b, who in getattr(self, "point_lines", ()):
            if who is own:
                continue
            n = max(2, int(math.hypot(b[0] - a[0], b[1] - a[1]) / 10))
            if any(g[0] <= a[0] + (b[0] - a[0]) * t / n <= g[2] and g[1] <= a[1] + (b[1] - a[1]) * t / n <= g[3] for t in range(n + 1)):
                return False
        if (p.family.startswith("animal.") and p.m["variant"].get("airborne")) or abs(p.Y - p.depth_y) > 30:
            return True
        for k, a in self.assets.items():
            if a is p or k not in self.ev_of or not (a.family.startswith("person.") or a.family.startswith("animal.")):
                continue
            # (only figures standing on the ground: a cat on the fence top or a bird on a lamp has no feet on the lawn)
            if (a.family.startswith("animal.") and a.m["variant"].get("airborne")) or abs(a.Y - a.depth_y) > 30:
                continue
            ab = a.bbox()
            if self.over_feet(bbox, ab) or self.over_feet(ab, bbox):
                return False
            if PLACEMENT_REV >= 16 and abs(a.Y - p.Y) < 40 * D.sz(p.Y) and min(bbox[2], ab[2]) + 6 > max(bbox[0], ab[0]) \
                    and min(bbox[3], ab[3]) > max(bbox[1], ab[1]):
                # revision 16: and figures of different events at the same depth stand apart, not in each other (a man
                # reading as he walked and a catcher beside him were "squashed together, one partly inside the other")
                return False
            if PLACEMENT_REV >= 19 and abs(a.Y - p.Y) < 80 * D.sz(p.Y):
                # revision 19: and up to about 80 px apart in depth, the nearer figure off the farther one's head and shoulders
                # (a dog walker 60 px in front of a reading man "overlap closely"; a goat behind a man "attached to his
                # shoulder")
                far_q, near_b = (a, bbox) if a.Y < p.Y else (p, ab)
                fb = far_q.bbox()
                hd = head_box(far_q) if far_q.family.startswith("person.") else (fb[0], fb[1], fb[2], fb[1] + 0.35 * (fb[3] - fb[1]))
                hd = (hd[0], hd[1], hd[2], hd[3] + 0.12 * (fb[3] - fb[1]))      # and the shoulders
                if min(near_b[2], hd[2]) > max(near_b[0], hd[0]) and min(near_b[3], hd[3]) > max(near_b[1], hd[1]):
                    return False
        if PLACEMENT_REV >= 15 and "bench" not in getattr(self, "exempt", ()):
            # revision 15: and no feet on, under or just behind a bench of the setting at the same depth (a man whose feet
            # met the bench's back edge was "standing behind it or partly overlapping it"; a dog by the door "on the
            # doorstep behind the bench or perched on top of the bench")
            for e in self.S.elements:
                if e["id"] == "bench" and e.get("bbox"):
                    eb = e["bbox"]
                    grown = (eb[0] - 6, eb[1], eb[2] + 6, eb[3] + 14)
                    if self.over_feet(grown, bbox):
                        return False
        return True

    @staticmethod
    def over_feet(a, b):
        """Revision 14: box a meets the feet of the figure in box b (its lowest sixth, a little in from the sides)."""
        w, h = b[2] - b[0], b[3] - b[1]
        f = (b[0] + 0.12 * w, b[3] - 0.16 * h, b[2] - 0.12 * w, b[3] + 4)
        return min(a[2], f[2]) > max(a[0], f[0]) and min(a[3], f[3]) > max(a[1], f[1])

    def lane(self, p):
        """Revision 14: the ground just ahead of a walker's leading foot (a pram pusher's reaches past the pram)."""
        pose = p.v.split("__")[1]
        if pose not in WALK_POSES or abs(p.Y - p.depth_y) > 30:
            return None
        f = p.facing()
        if f == 0:
            return None
        s = D.sz(p.Y)
        b = p.bbox()
        front = b[2] if f > 0 else b[0]
        if p.family.startswith("person.") and p.has_anchor("foot_L") and p.has_anchor("foot_R"):
            front = f * max(p.anchor("foot_L")[0] * f, p.anchor("foot_R")[0] * f)
        L = (300 if pose == "push" else 230 if pose == "run" else 170) * s
        x0, x1 = sorted((front + f * 4, front + f * L))
        # revision 15: a pram's lane also takes in the ground a little behind its own line, where the tall pram passes in
        # front of whoever stands there (a pram "heading toward the birds and the man feeding them" 80 px behind it)
        back = 90 if (pose == "push" and PLACEMENT_REV >= 15) else 26
        if pose == "run" and PLACEMENT_REV >= 18:
            # revision 18: a runner's lane longer, and deeper behind and in front of its line (running at a bench, a woman
            # "might come close to him or trip over his feet" 115 px behind her line; running at two children, she seemed
            # to run "toward the jumping girl")
            x0, x1 = sorted((front + f * 4, front + f * 300 * s))
            # revision 21: deeper still behind (a runner whose lane ended 25 px short of a cat stalking a bird behind her line
            # seemed to be running "toward the cat and bird, perhaps to stop the cat")
            back = 220 if PLACEMENT_REV >= 21 else 150
            return (max(0.0, x0), p.Y - back * s, min(float(D.W), x1), p.Y + 50 * s)
        return (max(0.0, x0), p.Y - back * s, min(float(D.W), x1), p.Y + 16 * s)

    def feet_on_things(self, bbox, own=None, pad=8):
        """Revision 20: the feet box of a figure's bbox meets a thing of another event on the ground."""
        h = bbox[3] - bbox[1]
        feet = (bbox[0], bbox[3] - 0.14 * h, bbox[2], bbox[3] + 4)
        for b, who in getattr(self, "groundthings", ()):
            if who is own:
                continue
            if min(feet[2], b[2] + pad) > max(feet[0], b[0] - pad) and min(feet[3], b[3] + pad) > max(feet[1], b[1] - pad):
                return True
        return False

    def headon_ok(self, p):
        """Revision 21: a runner and anyone else moving (walking, pushing, running) do not face each other on one line."""
        pose = p.v.split("__")[1]
        if pose not in WALK_POSES:
            return True
        f = p.facing()
        if not f:
            return True
        s = D.sz(p.Y)
        for k, q in self.assets.items():
            if q is p or k not in self.ev_of or not getattr(q, "family", "").startswith("person."):
                continue
            pq = q.v.split("__")[1]
            if pq not in WALK_POSES or "run" not in (pose, pq):
                continue
            if abs(q.Y - p.Y) < 60 * s:
                # and a runner keeps a clear gap from any other mover beside her on her line (running past a man with a pram
                # "side by side and almost touching but moving in opposite directions")
                a_, b_ = p.bbox(), q.bbox()
                if max(a_[0], b_[0]) - min(a_[2], b_[2]) < 50 * s:
                    return False
            fq = q.facing()
            if not fq or (fq > 0) == (f > 0):
                continue
            if abs(q.Y - p.Y) > 90 * s:
                continue
            if (q.X - p.X) * f > 0:          # the other is ahead of this one, and (facing back) this one ahead of it
                return False
        return True

    def feet_zone(self, q):
        """Revision 22: the ground round a walker's feet, on both sides of him and in depth."""
        s = D.sz(q.Y)
        b = q.bbox()
        x0, x1 = b[0], b[2]
        if q.has_anchor("foot_L") and q.has_anchor("foot_R"):
            xs = (q.anchor("foot_L")[0], q.anchor("foot_R")[0])
            x0, x1 = min(xs), max(xs)
        return (x0 - 170 * s, q.Y - 70 * s, x1 + 170 * s, q.Y + 50 * s)

    def sleeper_by_feet(self, p):
        """Revision 22: p is a sleeping animal at the feet of another event's walker, or a walker with another event's
        sleeping animal at its feet. (An event's own animal is not in ev_of until the event is placed.)"""
        pose = p.v.split("__")[1]
        if p.family.startswith("animal.") and pose.startswith("sleep"):
            return any(k in self.ev_of and q.family.startswith("person.") and q.v.split("__")[1] in WALK_POSES
                       and self.overlap(self.feet_zone(q), p.bbox()) > 0 for k, q in self.assets.items())
        if p.family.startswith("person.") and pose in WALK_POSES:
            return any(k in self.ev_of and q.family.startswith("animal.") and q.v.split("__")[1].startswith("sleep")
                       and self.overlap(self.feet_zone(p), q.bbox()) > 0 for k, q in self.assets.items())
        return False

    def clear_of_floats(self, bbox, p=None, gap=60):
        """Revision 21: a box clear of every angler's float and line (floats: (x, y) points, lines: (a, b) segments); a duck
        given as p also faces away from every float."""
        g = (bbox[0] - gap, bbox[1] - gap * 0.6, bbox[2] + gap, bbox[3] + gap * 0.6)
        for (x, y) in getattr(self, "floats", ()):
            if g[0] <= x <= g[2] and g[1] <= y <= g[3]:
                return False
            if p is not None and self.faces_toward(p, x):
                return False
        for a, b in getattr(self, "fish_lines", ()):
            n = max(2, int(math.hypot(b[0] - a[0], b[1] - a[1]) / 10))
            if any(bbox[0] - 14 <= a[0] + (b[0] - a[0]) * t / n <= bbox[2] + 14 and bbox[1] - 14 <= a[1] + (b[1] - a[1]) * t / n <= bbox[3] + 14
                   for t in range(n + 1)):
                return False
        return True

    @staticmethod
    def faces_toward(p, x):
        """Revision 21: p (an animal or person) is turned toward the point at image x."""
        f = p.facing()
        b = p.bbox()
        return bool(f) and (x - (b[0] + b[2]) / 2) * f > 0

    def lanes_ok(self, *ps):
        """Revision 14: each walker's lane is clear of other events' people, animals and things, and of standing
        structures (a pram "heads straight into the lamp post")."""
        own = getattr(self, "placing", None)
        if PLACEMENT_REV < 14 or (own is not None and own.id == "about_to_trip"):
            return True
        for p in ps:
            z = self.lane(p)
            if z is None:
                continue
            if any(k in self.ev_of and self.overlap(z, a.bbox()) > 0 for k, a in self.assets.items()):
                return False
            if any(k in self.ev_of and e.get("bbox") and e["role"] in ("scored", "filler", "setting") and self.overlap(z, e["bbox"]) > 0
                   for k, e in self.svgs.items()):
                return False
            if PLACEMENT_REV >= 18 and p.v.split("__")[1] == "run":
                # (the deeper part of a runner's lane is for people, animals and things; a structure is in the way only on
                # the runner's own line)
                s_ = D.sz(p.Y)
                z = (z[0], p.Y - 26 * s_, z[2], p.Y + 16 * s_)
                # and no flower bed or rock on that line (a runner heading straight into the park's flower bed)
                low = tuple(e["id"] for e in self.S.elements if e["id"] == "flowers" or e["id"].startswith("filler_"))
                zl = z
                if PLACEMENT_REV >= 20:
                    # revision 20: anywhere on that line up to the picture's edge (a runner 400 px short of the flower bed
                    # was "heading straight for the flower bed and about to trample it")
                    f_ = p.facing() or 1
                    zl = (z[0], z[1], float(D.W), z[3]) if f_ > 0 else (0.0, z[1], z[2], z[3])
                if low and not self.setting_clear(zl, only=low):
                    return False
            if not self.setting_clear(z, only=self.LANE_STRUCT):
                return False
        return True

    def add_lanes(self, *ps):
        own = getattr(self, "placing", None)
        if PLACEMENT_REV < 14 or (own is not None and own.id == "about_to_trip"):
            return
        for p in ps:
            z = self.lane(p)
            if z is not None:
                self.lanes.append((z, own))

    def bird_gap(self, p, bbox, ignore=(), gap=14):
        """Revision 6: a songbird keeps a gap from the people of other events, and they from it (a blue
        bird drawn against a kite-flyer's shoulder read as a cap)."""
        mine = p.family
        if not (mine.startswith("person.") or mine.startswith("animal.bird")):
            return True
        g = (bbox[0] - gap, bbox[1] - gap, bbox[2] + gap, bbox[3] + gap)
        for k, a in self.assets.items():
            if k in ignore or k not in self.ev_of or a is p:
                continue
            other = a.family
            if (mine.startswith("person.") and other.startswith("animal.bird")) or (mine.startswith("animal.bird") and other.startswith("person.")):
                b = a.bbox()
                if min(g[2], b[2]) > max(g[0], b[0]) and min(g[3], b[3]) > max(g[1], b[1]):
                    return False
        return True

    def path_clear(self, pts, r=4):
        """True if no standing structure lies within r mask pixels of any of the points (full-resolution px)."""
        from . import compose as K
        U, _ = structure_masks(self.S, getattr(self, "exempt", ()))
        if U is None:
            return True
        k = K.MASK_SCALE
        for x, y in pts:
            xi, yi = int(x * k), int(y * k)
            y0, y1, x0, x1 = max(0, yi - r), min(U.shape[0], yi + r + 1), max(0, xi - r), min(U.shape[1], xi + r + 1)
            if y1 > y0 and x1 > x0 and U[y0:y1, x0:x1].any():
                return False
        return True

    def touch_clear(self, p, U, touch_px=12, c=3):
        """Revision 4: nobody touches a standing structure their event does not use, with any part of
        the body (a man sitting on air with his back against a tree trunk seemed to lean on it; a camera
        against a trunk; feet against the end of a seesaw)."""
        from . import compose as K
        from scipy.ndimage import binary_dilation
        m = K.asset_mask(p, False)
        ys, xs = np.nonzero(m)
        if not ys.size:
            return True
        y0, y1 = max(0, ys.min() - c), min(m.shape[0], ys.max() + c + 1)
        x0, x1 = max(0, xs.min() - c), min(m.shape[1], xs.max() + c + 1)
        ring = binary_dilation(m[y0:y1, x0:x1], iterations=c)
        return int((ring & U[y0:y1, x0:x1]).sum()) <= touch_px

    def animal_clear(self, p, touch_px=8):
        """Revision 4: an animal on the ground keeps a clearance from every standing structure its event
        does not use (a lamp post seemed to stand on a dog's back, a dog's nose touched the end of the
        slide, a cat behind a bench seemed to lie on top of it)."""
        from . import compose as K
        from scipy.ndimage import binary_dilation
        if p.m["variant"].get("airborne") or not self.S.walkable(p.X, p.Y):
            return True
        U, _ = structure_masks(self.S, getattr(self, "exempt", ()))
        if U is None:
            return True
        m = K.asset_mask(p, False)
        ys, xs = np.nonzero(m)
        if not ys.size:
            return True
        c = K.CLEAR_PX
        y0, y1 = max(0, ys.min() - c), min(m.shape[0], ys.max() + c + 1)
        x0, x1 = max(0, xs.min() - c), min(m.shape[1], xs.max() + c + 1)
        ring = binary_dilation(m[y0:y1, x0:x1], iterations=c)
        return int((ring & U[y0:y1, x0:x1]).sum()) <= touch_px

    def on_element(self, eid, x, y):
        """True if (x, y) falls on the drawn setting element `eid` (the path, say)."""
        from . import compose as K
        for e in self.S.elements:
            if e["id"] == eid and e.get("svg"):
                k = (e["id"], hash(e["svg"]))
                if k not in _MASKS:
                    _MASKS[k] = K.alpha_mask(dict(e, kind="svg"), False)
                    _THIN[k] = K.thin_part(_MASKS[k])
                m = _MASKS[k]
                xi, yi = int(x * K.MASK_SCALE), int(y * K.MASK_SCALE)
                return 0 <= yi < m.shape[0] and 0 <= xi < m.shape[1] and bool(m[yi, xi])
        return False

    def air_clear(self, box, max_px=6, use_exempt=False):
        """True if no standing structure of the setting reaches into `box` (full-resolution px); with
        use_exempt, the structures the current event uses are left out."""
        from . import compose as K
        U, _ = structure_masks(self.S, getattr(self, "exempt", ()) if use_exempt else ())
        if U is None:
            return True
        sc_ = K.MASK_SCALE
        x0, y0 = max(0, int(box[0] * sc_)), max(0, int(box[1] * sc_))
        x1, y1 = min(U.shape[1], int(box[2] * sc_) + 1), min(U.shape[0], int(box[3] * sc_) + 1)
        if x1 <= x0 or y1 <= y0:
            return True
        return int(U[y0:y1, x0:x1].sum()) <= max_px

    SKY_SKIP = ("sky", "ground", "path", "pond", "blanket", "sandbox")

    def setting_clear(self, box, only=None, skip=SKY_SKIP, max_px=2):
        """Revision 8: True if no element of the setting (backdrops such as the house, buildings and
        clouds included, unlike air_clear) has drawn pixels inside `box`; `only` limits the check to
        those element ids."""
        from . import compose as K
        sc_ = K.MASK_SCALE
        x0, y0 = max(0, int(box[0] * sc_)), max(0, int(box[1] * sc_))
        for e in self.S.elements:
            if not e.get("svg") or (only is not None and e["id"] not in only) or (only is None and e["id"] in skip):
                continue
            b = e.get("bbox")
            if b and (b[2] < box[0] or b[0] > box[2] or b[3] < box[1] or b[1] > box[3]):
                continue
            k = (e["id"], hash(e["svg"]))
            if k not in _MASKS:
                _MASKS[k] = K.alpha_mask(dict(e, kind="svg"), False)
                _THIN[k] = K.thin_part(_MASKS[k])
            m = _MASKS[k]
            x1, y1 = min(m.shape[1], int(box[2] * sc_) + 1), min(m.shape[0], int(box[3] * sc_) + 1)
            if x1 > x0 and y1 > y0 and int(m[y0:y1, x0:x1].sum()) > max_px:
                return False
        return True

    def outline_clear(self, box, max_px=2):
        """Revision 16: True if no outline of the setting's backdrop runs through `box` (a waving hand on the dark line
        of the hedge behind it read as "holding a string")."""
        from . import compose as K
        m = backdrop_outlines(self.S)
        sc_ = K.MASK_SCALE
        x0, y0 = max(0, int(box[0] * sc_)), max(0, int(box[1] * sc_))
        x1, y1 = min(m.shape[1], int(box[2] * sc_) + 1), min(m.shape[0], int(box[3] * sc_) + 1)
        if x1 <= x0 or y1 <= y0:
            return True
        return int(m[y0:y1, x0:x1].sum()) <= max_px

    def clear_of_pond_edge(self, box):
        """Revision 10: nobody stands with the feet on the pond's front rim (a man overlapping the edge of
        the pond, a woman "about to step into the water")."""
        for e in self.S.elements:
            if e["id"] != "pond" or not e.get("bbox"):
                continue
            b = e["bbox"]
            fx = (box[0] + box[2]) / 2
            if b[0] - 10 < fx < b[2] + 10 and b[3] - 30 < box[3] < b[3] + 28:
                return False
        return True

    def clear_of_pond_v19(self, box, p):
        """Revision 19: a person or animal clear of the pond's cattails (one "poking up just behind the young person's head",
        others "at his hip"), and with the feet not on or inside its rim at the sides either ("overlaps the right edge of the
        pond ... he may be standing in or at the water")."""
        A = self.S.anchors.get("pond")
        if not A or "center" not in A:
            return True
        (cx, cy), rx, ry = A["center"], A["rx"], A["ry"]
        base = cy + 0.25 * ry
        for d0, d1 in ((-0.92, -0.86), (0.88, 0.93)):
            z = (cx + d0 * rx - 26, base - 64, cx + d1 * rx + 26, base + 8)
            if min(box[2], z[2]) > max(box[0], z[0]) and min(box[3], z[3]) > max(box[1], z[1]):
                return False
        if "pond" in getattr(self, "exempt", ()):
            return True
        fx, fy = (box[0] + box[2]) / 2, box[3]
        return ((fx - cx) / (rx * 1.08)) ** 2 + ((fy - cy) / (ry * 1.25)) ** 2 > 1.0

    def clear_of_house_edges(self, box, margin=18):
        """Revision 9: a person stands either wholly in front of the house wall or clear of it, never across
        its side edge (a waver whose raised hand met the house corner read as peeking round it)."""
        for e in self.S.elements:
            if e["id"] != "house" or not e.get("bbox"):
                continue
            b = e["bbox"]
            if box[1] >= b[3]:
                continue
            for edge in (b[0] + 5, b[2] - 5):
                if 8 < edge < D.W - 8 and box[0] - margin < edge < box[2] + margin:
                    return False
        return True

    def clear_of_setting(self, box, ids, margin=0):
        """Revision 8: True if `box`, grown by `margin`, meets none of the bounding boxes of the setting
        elements `ids` (or of the boxes listed under those anchor names)."""
        g = (box[0] - margin, box[1] - margin, box[2] + margin, box[3] + margin)
        boxes = [e["bbox"] for e in self.S.elements if e["id"] in ids and e.get("bbox")]
        for i in ids:
            a = self.S.anchors.get(i)
            if isinstance(a, list):
                boxes += a
        return not any(min(g[2], b[2]) > max(g[0], b[0]) and min(g[3], b[3]) > max(g[1], b[1]) for b in boxes)

    def clear_of_structures(self, p, head_limit=0.10, cross_px=30):
        """The legibility rules (compose.legibility) checked against the setting's standing structures
        while placing, so a layout is not built only to be thrown away at the end."""
        from . import compose as K
        import numpy as np
        U, TH = structure_masks(self.S, getattr(self, "exempt", ()))
        m = K.asset_mask(p, False)
        m_full = m
        if U is None:
            if PLACEMENT_REV < 4:
                return True
            U = TH = np.zeros_like(m)
        sc_ = K.MASK_SCALE
        ht, em = p.anchor("head_top"), p.eye_mid()
        r = max(6.0, (em[1] - ht[1]) * 1.30)
        hx = (ht[0] + em[0]) / 2
        X0, X1 = int(max(0, hx - r) * sc_), int(min(D.W, hx + r) * sc_) + 1
        Y0, Y1 = int(max(0, ht[1]) * sc_), int((ht[1] + 2.15 * r) * sc_) + 1
        head = m[Y0:Y1, X0:X1]
        npx = int(head.sum())
        if npx >= 12 and int((head & U[Y0:Y1, X0:X1]).sum()) / npx > head_limit:
            return False
        if PLACEMENT_REV >= 4:
            body_px = int(m.sum())
            hands = [p.anchor(h) for h in ("hand_L_grip", "hand_R_grip") if p.has_anchor(h)]
            if not K.clearance_ok(m, TH, (X0, Y0, X1, Y1), hands):
                return False
            # nor may a hand come within 18 px of any structure the event does not use (a raised hand
            # against a tree's foliage read as touching it)
            c = K.CLEAR_PX + 3
            for hx, hy in hands:
                cx, cy = int(hx * sc_), int(hy * sc_)
                if int(U[max(0, cy - c):cy + c + 1, max(0, cx - c):cx + c + 1].sum()) > 3:
                    return False
            # nobody's feet or hands against another person's head, either way round
            c = K.PERSON_CLEAR_PX
            for q in self.assets.values():
                if q is p or q.id == p.id or not q.family.startswith("person."):
                    continue
                mq = K.asset_mask(q, False)
                if int(mq[max(0, Y0 - c):Y1 + c, max(0, X0 - c):X1 + c].sum()) > 25:
                    return False
                qt, qe = q.anchor("head_top"), q.eye_mid()
                qr = max(6.0, (qe[1] - qt[1]) * 1.30)
                qx = (qt[0] + qe[0]) / 2
                qX0, qX1 = int(max(0, qx - qr) * sc_), int(min(D.W, qx + qr) * sc_) + 1
                qY0, qY1 = int(max(0, qt[1]) * sc_), int((qt[1] + 2.15 * qr) * sc_) + 1
                if int(m[max(0, qY0 - c):qY1 + c, max(0, qX0 - c):qX1 + c].sum()) > 25:
                    return False
        rows = np.nonzero(m.any(axis=1))[0]
        legs_m = K.legs_of(m)
        if rows.size:
            cut = int(rows.max() - 0.07 * (rows.max() - rows.min()))
            m = m.copy()
            m[cut:, :] = False
        if PLACEMENT_REV >= 4 and body_px and int((U & m).sum()) > K.BODY_LIMIT * body_px:
            return False
        if PLACEMENT_REV >= 4 and not self.touch_clear(p, U):
            return False
        if PLACEMENT_REV >= 4 and not self.legs_clear(p, legs_m):
            return False
        if PLACEMENT_REV >= 17:
            # revision 17: a gap between a person and the thin parts (poles, legs, rails) of standing structures the
            # event does not use: a woman "tightly overlapping the lamp post", a photographer "inside the swing frame"
            from scipy.ndimage import binary_dilation
            if int((TH & binary_dilation(m_full, iterations=4)).sum()) > 4:
                return False
            if not self.clear_of_stall(p):
                return False
        return int((TH & m).sum()) <= cross_px

    def clear_of_stall(self, p):
        """Revision 17: nobody stands among the market stall's legs: anyone across its width stands well in front of it
        (a man against the stall's back legs)."""
        if "stall" in getattr(self, "exempt", ()):
            return True
        bb = p.bbox()
        for e in self.S.elements:
            if e["id"] == "stall" and e.get("bbox"):
                b = e["bbox"]
                if min(bb[2], b[2] + 8) > max(bb[0], b[0] - 8) and bb[3] < b[3] + 40 * D.sz(b[3]):
                    return False
                # no hand over the crates of fruit (a runner's hand on the apples looked like snatching one)
                s_ = D.sz(b[3])
                top = b[3] - 96 * s_
                for h in ("hand_L_grip", "hand_R_grip"):
                    if p.has_anchor(h):
                        hx, hy = p.anchor(h)
                        if b[0] - 10 <= hx <= b[2] + 10 and top - 40 * s_ - 8 <= hy <= top + 6:
                            return False
        return True

    def legs_clear(self, p, legs):
        """Revision 4: no standing structure drawn in front of a person may cover their legs or feet
        (someone standing just behind a bench seemed to be stepping onto it)."""
        from . import compose as K
        ex = getattr(self, "exempt", ())
        for e in self.S.elements:
            if e["role"] in K.BACKGROUND_ROLES or e["id"] in K.BACKDROP_IDS or e["id"] in ex or not e.get("svg"):
                continue
            if e["z"] <= p.z:
                continue
            k = (e["id"], hash(e["svg"]))
            if k not in _MASKS:
                _MASKS[k] = K.alpha_mask(dict(e, kind="svg"), False)
                _THIN[k] = K.thin_part(_MASKS[k])
            if int((_MASKS[k] & legs).sum()) > K.LEGS_PX:
                return False
        return True

    def feet_free(self, X, Y, min_dx=60, min_dy=55):
        for p in self.assets.values():
            if p.m["variant"].get("airborne"):
                continue
            if abs(p.X - X) < min_dx * D.sz(Y) and abs(p.Y - Y) < min_dy:
                return False
        return True

    def spots(self, x_range=None, y_range=None, n=60, near=None, dist=None):
        """Candidate ground points: walkable, uncrowded, optionally near a point at a distance range (px)."""
        x0, x1 = x_range or (110, D.W - 110)
        y0, y1 = y_range or (self.S.horizon + 50, D.H - 12)
        out = []
        tries = 0
        while len(out) < n and tries < n * 30:
            tries += 1
            if near is not None and dist is not None:
                a = self.rng.uniform(0, 2 * math.pi)
                r = self.rng.uniform(*dist)
                X, Y = near[0] + math.cos(a) * r, near[1] + math.sin(a) * r * 0.35
            else:
                X, Y = self.rng.uniform(x0, x1), self.rng.uniform(y0, y1)
            if not (x0 <= X <= x1 and y0 <= Y <= y1):
                continue
            if not self.S.walkable(X, Y) or self.S.in_soft(X, Y):
                continue
            if not self.feet_free(X, Y):
                continue
            out.append((X, Y))
        # prefer open ground away from others (up to a point), toward the middle and front of the picture
        others = [(p.X, p.Y) for p in self.assets.values()]
        h0 = self.S.horizon + 50

        def pref(q):
            o = min([math.hypot(q[0] - a[0], (q[1] - a[1]) * 2.2) for a in others] or [400.0])
            centre = 1 - abs(q[0] - D.W / 2) / (D.W / 2)
            front = (q[1] - h0) / max(1.0, D.H - h0)
            return (min(o, 380) / 380) * 1.0 + 0.55 * centre + FRONT_BIAS.get(self.tier, 0.3) * front + self.rng.uniform(0, 0.45)
        out.sort(key=lambda q: -pref(q))
        return out

    def put(self, eid, v, X, Y, mirror=False, depth_y=None, role="scored", limit=0.12, ignore=(), check=True):
        p = self.placed(v, X, Y, mirror, depth_y, eid, role)
        if check and not self.fits(p.bbox(), ignore, limit):
            return None
        self.assets[eid] = p
        return p

    def try_put(self, eid, v, candidates, want_face=None, limit=0.12, ignore=(), accept=None):
        """Place v at the first candidate ground point that fits (and passes accept(p))."""
        for X, Y in candidates:
            mirror = False
            if want_face is not None:
                w = want_face(X, Y) if callable(want_face) else want_face
                mirror = self.mirror_for(v, w)
            p = self.placed(v, X, Y, mirror, None, eid)
            if not self.fits(p.bbox(), ignore, limit):
                continue
            if accept and not accept(p):
                continue
            if PLACEMENT_REV >= 14 and not self.lanes_ok(p):
                continue
            self.assets[eid] = p
            self.add_lanes(p)
            return p
        return None

    def svg(self, eid, label, svg, z, bbox, role="scored"):
        self.svgs[eid] = {"id": eid, "label": label, "svg": svg, "z": z, "bbox": bbox, "role": role, "kind": "svg"}
        return eid

    def remove(self, *eids):
        for e in eids:
            self.assets.pop(e, None)
            self.svgs.pop(e, None)

    # ------------------------------------------------------------ items
    def item(self, kind, text, accepted, key, elements, animate=False, chain=0, cues=None, effect=None, domain=None, template=None, event=None):
        it = {"id": f"i{len(self.items) + 1:02d}", "type": kind, "text": text, "accepted": accepted, "key": key,
              "elements": list(elements), "animate": bool(animate), "chain": chain, "cues": list(cues or []),
              "effect": list(effect or []), "domain": domain, "template": template, "event": event}
        self.items.append(it)
        return it

    def gaze_ok(self, p, box):
        ok, why = looks_at(p, box)
        return ok
