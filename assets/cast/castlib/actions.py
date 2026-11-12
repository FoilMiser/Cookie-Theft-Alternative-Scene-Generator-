"""People actions: a lower-body posture plus an upper-body activity, with props built prop-first.

Props are built in world space at the moment the pose is set, then parented to a hand
(or head) bone, so they ride along exactly when the renderer applies that pose again.
Prop objects are named PROP_<action>_<part>; prop anchors ANCHOR_<name>@<action>.
The renderer shows only the current action's props and anchors.
"""
import math

import bpy  # noqa: F401
from mathutils import Matrix, Quaternion, Vector

import bmesh

from .core import Frame, _mesh_object, anchor, box, cyl, ellipsoid, flat_prism, frame_toward, half_ellipsoid, nrm, tube_mesh, upd
from .core import PALETTE as _PAL44

import colorsys as _cs44
import os as _os44

# v0.44 bench (figure-review-v043.md item 1, TPDB_PROP44): a prop the same colour as the clothes behind it vanishes into them: the yellow shopping bag
# on the woman in yellow's dress read as an apron panel, the teal watering can on the grandmother's teal cardigan, a pink scoop on a pink dress.
# "A": each such prop takes the first colour of its list whose hue is at least 20 degrees from every saturated garment the person wears (the clashes
# named are 0 degrees apart; at 40, the pink scoop by the red shirt went cream, pale on pale skin, and the cone's tip read as "a moustache or a
# chocolate smear" in both v0.44 design tests that drew it). "O": v0.43
PROP44 = _os44.environ.get("TPDB_PROP44", "A")  # v0.44 bench (vision/isolation_v044.md): A
# v0.44 bench (figure-review-v043.md item 2, TPDB_RUN44): running read as a lunge, the hips low and the back shoe planted flat behind, nothing off the
# ground. "A": the hips up, the back shin kicked up behind, the front foot a little off the ground, the lean 16 degrees, no sole under the raised
# foot. "O": v0.43
RUN44 = _os44.environ.get("TPDB_RUN44", "A")  # v0.44 bench (vision/isolation_v044.md): A
# v0.44 bench (figure-review-v043.md item 14, TPDB_THROW44): the throw's straight arm up and forward, its fingers together, read as pointing. "A": the
# follow-through, the throwing arm at shoulder height across the front of the body, the hand open with its palm to the viewer, the other arm back.
# "O": v0.43
THROW44 = _os44.environ.get("TPDB_THROW44", "O")  # v0.44: O (A looked no better than v0.43's; not benched)
# v0.44 bench (figure-review-v043.md item 6, TPDB_SPADE44): the sand spade's small red blade, apart from its blue handle, read as a floating red cross
# (a first-aid sign). "A": the handle runs into a blade twice the size with a pointed foot. "O": v0.43
SPADE44 = _os44.environ.get("TPDB_SPADE44", "A")  # v0.44 bench (vision/isolation_v044.md): A
# v0.44 bench (figure-review-v043.md item 15, TPDB_INSPECT44): looking into the hose's nozzle, the head tipped 20 degrees down hid the brows and the
# mouth, and the inference rests on the puzzled face. "A": the head level, turned 20 degrees toward the viewer. "O": v0.43
INSPECT44 = _os44.environ.get("TPDB_INSPECT44", "A")  # v0.44 bench (vision/isolation_v044.md): A
# v0.44 bench (figure-review-v043.md item 13, TPDB_CALL44): stuck up on the seesaw and calling out, both hands at the chest and a small "o" of a mouth
# read as nervous or praying. "A": one hand on the handle, the other cupped at a wider open mouth (face.CALL44). "O": v0.43
CALL44 = _os44.environ.get("TPDB_CALL44", "A")  # v0.44 bench (vision/isolation_v044.md): A
# v0.45 bench (vision/flaws_v044.md R1, TPDB_ICE45): the walking girl's ice cream was "a small pink thing", "a tiny pink dot", a sweet, a flower, a
# blown kiss: the cone, the colour of skin, hid in the fist and the scoop sat on the cheek. "A": the cone darker (wood) and longer above the fist, cone
# and scoop larger (half as big again on a child, whose props shrink with the body), the scoop below and in front of the mouth.
ICE45 = _os44.environ.get("TPDB_ICE45", "A")  # v0.45 bench (vision/isolation_v045.md): A
# v0.49 (TPDB_ICE49 "B"; flaws_v048.md R5): the scoop at the mouth. On v0.48's face the mouth is lower and a plain line, and the cone stopped a
# hand's width short of it: "she may be about to eat it or just carrying it", "he does not seem to be eating at this moment, just holding the
# cone up" (ice_cream 0.95 by the gate, 0.75 with its eight calls halved). "B": the scoop's near side a finger from the lips, its middle just
# under the mouth, and the head tipped twelve degrees to it for six. "O": v0.48's reach
ICE49 = _os44.environ.get("TPDB_ICE49", "B")
ICE49_PITCH = -12 if ICE49 == "B" else -6
# v0.45 bench (vision/flaws_v044.md R2, TPDB_CAM45): the camera at the eyes was once more "a camera (or binoculars)". "A": the camera larger, a prism
# hump in the middle of its top, a longer lens with a wide silver ring, and a strap hanging in a loop under it; a "flash" anchor for the scene.
CAM45 = _os44.environ.get("TPDB_CAM45", "A")  # v0.45 bench (vision/isolation_v045.md): A
# v0.45 bench (vision/flaws_v044.md O2, TPDB_SOLE45): a walker's tipped shoes show their sole plates edge on, longer than the shoe and pointed, grey
# under a dark shoe: "black ice skates". "H": no sole plate on a walker's feet (people.py has "A", the plate tucked under every shoe).
SOLE45 = _os44.environ.get("TPDB_SOLE45", "A")  # v0.45 bench (vision/isolation_v045.md): A
# v0.45 bench (look review of v0.44, TPDB_HOSE45): INSPECT44 "A" turned the head 20 degrees the wrong way, away from the viewer, and the cut-outs show
# the back of the head ("the single worst pose-versus-inference mismatch in the set"). "A": the head turned toward the viewer, as a profile pose's
# is, and a little down at the nozzle.
HOSE45 = _os44.environ.get("TPDB_HOSE45", "A")  # v0.45 bench (vision/isolation_v045.md): A
# v0.45 bench (look review, TPDB_TROWEL45): the planter's trowel was a thin plate seen edge on, a grey line under the fist ("no visible trowel", "the
# planting is not shown"). "A": a broad pointed blade seen from the side, pointing down at the soil, on a neck and a handle in a bright colour.
TROWEL45 = _os44.environ.get("TPDB_TROWEL45", "A")  # v0.45 bench (vision/isolation_v045.md): A
# v0.45 bench (look review, TPDB_PAINT45): the roller, a blue bar on the end of a pole, read as "a paddle". "A": a wire frame cranked up behind the
# roller and into its top end, and a cream cap at each end of the sleeve.
PAINT45 = _os44.environ.get("TPDB_PAINT45", "A")  # v0.45 bench (vision/isolation_v045.md): A
# v0.45 bench (look review, TPDB_BOX45): the carried box was the fence's colour to the digit (both wood_light) and sank into it. "A": khaki, with a
# brown tape.
BOX45 = _os44.environ.get("TPDB_BOX45", "A")  # v0.45 bench (vision/isolation_v045.md): A
# v0.45 bench (look review, TPDB_KITE45): the kite flyer's spool, a wood-coloured cylinder seen end on, was "a small tan ball with a brown dot", the
# fist's size and on two of the three children its colour. "A": a reel on a handle above the fist, two bright flanges and the wound string between.
KITE45 = _os44.environ.get("TPDB_KITE45", "A")  # v0.45 bench (vision/isolation_v045.md): A
# v0.47 bench (TPDB_HEAD47, people.py; TPDB_PROFILE): the head is fuller at the cheeks, so that a face turned 45 degrees keeps both eyes inside its
# outline, and its front is flatter: seen from the side the face shows no eye at all, and turned 35 degrees toward the viewer, as v0.27 to v0.46
# turned a profile's head, the far eye lies half under the outline. "B": a side view's head turns 48 degrees toward the viewer, the face a clean
# three-quarter one with both eyes whole; a pose with a thing held at the face turns from the waist, spine and chest half each, so the hands and
# the thing come round with the head. "O": v0.46 (35 degrees, a held thing's poses in pure profile)
HEAD47 = _os44.environ.get("TPDB_HEAD47", "B")
# v0.48 (direction bench, vision/isolation_v048.md): on the egg head (core.HEAD48) a side view's head turns 15 degrees toward the viewer, a
# profile with one eye, the nose and the mouth. Eight moving figures alone at 0.41 of full size, each read twice in v0.47's drawing, in the
# new head turned 48 degrees and in the new head turned 15: every one of the 48 answers had the way it goes, and the reader was "sure" of
# 4, 6 and 11 of 16; of the turned heads, "the face is close to three-quarter so it is slightly less clear", "torso is drawn fairly square
# to the viewer, which weakens it a little"
from .core import HEAD48 as _HEAD48
# (pair bench 2: at 15 degrees the reviewers of enlarged figures had the eye "on the very front edge of the face outline, partly cut off" and
# the face "blank". The side view's face is now its own, face.PROF48, and the head turns 22 degrees)
PROFILE47 = float(_os44.environ.get("TPDB_PROFILE", ("-22" if _HEAD48 == "B" else "-48") if HEAD47 == "B" else "-35"))
# v0.47 bench (vision/flaws_v046.md R2 and O6, TPDB_WALK47): a walker was read as heading the other way, "The box is behind him, so he is not about
# to trip on it." (v046 pic_82): the trailing leg was straight and its shoe, tipped 44 degrees, lay much like the leading one turned round. "B": the
# trailing foot up on its toe, the heel high and the knee bent, the shin sloping back; the leading leg reaches forward to a flat foot. "O": v0.46
WALK47 = _os44.environ.get("TPDB_WALK47", "B")
# v0.48 (vision/flaws_v047.md R1, TPDB_WALK48): `about_to_trip` failed two gates running on a walker read as going the other way, and the
# direction bench's readers still had of v0.47's walk "the back foot seems angled right, slightly ambiguous", "the back shoe points right".
# "B": the trailing foot tipped 46 degrees for 64 (tipped further, a shoe on its toe is a shoe pointing up and back), the leading foot
# coming down on its heel with the toe a little up, and the trunk leaning 7 degrees into the walk for 4. "O": v0.47's walk
# (bench round 1, vision/isolation_v048.md: with "B" one walker of four was again read as going the other way, "she is actually walking to the
# right, away from it". Both feet were on the ground in an A, the straight leg in front and the bent one behind, and a bent leg is the leg a
# reader takes to be swinging forward.) "C": the step itself: the rear leg straight and planted under the body, its heel just leaving the
# ground, and the leading leg lifted and bent, the knee forward and the foot off the ground with its toe up, about to come down; the trunk
# leans 8 degrees into it
# (bench round 2: "C" was put to six readers in the trip's cut-outs and left. Five had the walker standing, "stands on green grass ...
# holding an open book", "the pose reads two ways: walking forward while reading, or standing still with legs apart", and the lifted foot at
# the obstacle "resting his foot on it or about to kick it". The long stride is what says walking; "B" is the release's walk)
WALK48 = _os44.environ.get("TPDB_WALK48", "B")
# v0.47 bench (vision/flaws_v046.md O6, TPDB_RUN47): "The woman's running pose is a little stiff, with the back foot kicked up high" (v046 pic_31): the
# front leg was a straight post under the body. "B": the front knee bent and forward, the back shin lower behind, the hips a little lower. "O": v0.46
RUN47 = _os44.environ.get("TPDB_RUN47", "B")
# v0.47 bench (vision/flaws_v046.md O6, TPDB_SITG47; lo_sit_ground): sitting on the ground, both legs lay side by side, a little bent: "The boy's
# legs look slightly short or tucked, so it is hard to tell whether they are stretched out straight or bent." (v046 pic_90). "B": the far leg's
# knee drawn up with its foot flat on the ground, the near leg out along the ground and resting on its heel, toes up: at 45 the two legs cross
# and the near sole is a dark disc over the far foot (bench g1). "C": both legs out straight along the ground, a little apart, heels down, the
# feet tipped forward of upright so that their soles do not face the viewer (bench g3). "O": v0.46
SITG47 = _os44.environ.get("TPDB_SITG47", "C")


def _pcol(P, default, alts):
    """v0.44 (TPDB_PROP44): the prop's colour: the first of default and alts whose hue is at least 20 degrees from every saturated garment the person
    wears (shirt, trousers or dress, vest, cardigan's inner)."""
    if PROP44 != "A":
        return default
    spec = P.c.spec

    def hsv(key):
        h = _PAL44[key].lstrip("#")
        return _cs44.rgb_to_hsv(*(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)))
    worn = [spec[k] for k in ("shirt", "pants", "vest", "inner") if spec.get(k) in _PAL44 and not (k == "pants" and spec.get("bottom") == "dress")]
    worn = [hsv(k) for k in worn if hsv(k)[1] >= 0.30]
    for col in (default,) + tuple(alts):
        h0, s0, v0 = hsv(col)
        if s0 < 0.30 or all(min(abs(h0 - h), 1 - abs(h0 - h)) * 360 >= 20 for h, s, v in worn):
            return col
    return default


class Poser:
    def __init__(self, rig, ctx):
        self.rig, self.c = rig, ctx
        J, S, s = ctx.J, ctx.S, ctx.s
        self.J, self.S, self.s = J, S, s
        self.u = S * s
        self.A = (J["sh_z"] - J["wr_z"]) * S
        self.L = (J["hip"] - J["ankle"]) * S
        self.props = {}        # action -> [object names]
        self.anchors = {}      # action -> [anchor names]
        self.meta = {}         # action -> dict
        self.profile_face = {}  # v0.48 (face.PROF48): action -> True when a side view draws it with the side view's own face
        self.cur = None
        self.misses = {}
        self.hides = {}        # action -> base objects hidden while it shows (mittens swapped for open hands)

    # ---------------------------------------------------------- landmarks
    def lm(self, name):
        upd()
        r = self.rig
        if name in ("sh_L", "sh_R"):
            return r.head(f"upper_arm_{name[-1]}")
        if name == "pelvis":
            return r.head("spine")
        if name == "chest":
            return r.tail("spine")
        if name == "neck":
            return r.tail("chest")
        ob = bpy.data.objects[f"ANCHOR_{name}"]
        return ob.matrix_world.translation.copy()

    def grip(self, sd):
        return self.lm(f"hand_{sd}_grip")

    # ---------------------------------------------------------- body helpers
    def place_legs(self, feet, hint=(0, -1, 0.25)):
        J, S = self.J, self.S
        flat39 = __import__("os").environ.get("TPDB_SHOE39", "D") == "D"
        for sd, sg in (("L", 1), ("R", -1)):
            dx, dy, lift = feet[sd]
            tgt = Vector((sg * J["hip_x"] * S + dx * S, dy * S, J["ankle"] * S + lift * S))
            h = hint[sd] if isinstance(hint, dict) else hint
            self.rig.ik2(f"thigh_{sd}", f"shin_{sd}", tgt, h)
            if flat39 and abs(lift) < 1e-6:
                # v0.39 bench (TPDB_SHOE39 "D"): a planted foot along its rest direction, so the sole is flat on the ground (aimed 8.5 degrees
                # down from a rest of 21, every standing shoe was tipped toe-up, its heel below the ground)
                self.rig.aim_dir(f"foot_{sd}", (0, -J["toe"], 0.02 * J["s"] - J["ankle"]))
            else:
                self.rig.aim_dir(f"foot_{sd}", (0, -1, -0.15))

    def drop_hips_for(self, feet):
        J, S, L = self.J, self.S, self.L
        need = 0.0
        for sd, sg in (("L", 1), ("R", -1)):
            dx, dy, lift = feet[sd]
            h = Vector((sg * J["hip_x"] * S, 0, J["hip"] * S))
            t = Vector((sg * J["hip_x"] * S + dx * S, dy * S, J["ankle"] * S + lift * S))
            horiz = math.hypot(t.x - h.x, t.y - h.y)
            # v0.39 bench (TPDB_KNEE39 "B"): standing legs straightened to 0.97 of their length, not 0.985, so the knees are not locked
            maxv = math.sqrt(max(0.0, ((0.97 if __import__("os").environ.get("TPDB_KNEE39", "O") == "B" else 0.985) * L) ** 2 - horiz ** 2))
            need = max(need, (h.z - t.z) - maxv)
        return need

    def arms(self, targets):
        for sd, (tgt, hint) in targets.items():
            miss = self.rig.ik2(f"upper_arm_{sd}", f"forearm_{sd}", tgt, hint)
            if miss > 0.02 * self.u:
                self.misses.setdefault(self.cur, []).append(f"{sd} hand {miss:.3f} m short")
            d = self.rig.bone_dir(f"forearm_{sd}")
            self.rig.aim_dir(f"hand_{sd}", d)

    def torso(self, lean=0.0, side=0.0, head_pitch=0.0, head_turn=0.0, head_roll=0.0, drop=0.0, back=0.0):
        rig = self.rig
        rig.arm.pose.bones["hips"].location = (0, -drop, -back)
        upd()
        lr, sr = math.radians(lean), math.radians(side)
        rig.aim_dir("spine", (-math.sin(sr), -math.sin(lr), math.cos(lr)))
        rig.aim_dir("chest", (-math.sin(sr) * 0.5, -math.sin(lr) * 0.6, 1))
        rig.aim_dir("neck", (0, -math.sin(lr) * 0.3, 1))
        p = math.radians(head_pitch)
        roll = math.radians(head_roll)
        rig.aim_dir("head", (math.sin(roll), math.sin(p), math.cos(p)), twist=math.radians(head_turn))

    def rest_arm(self, sd, out=None, fwd=-0.04):
        sg = 1 if sd == "L" else -1
        # v0.46 bench (TPDB_ARM46 "B"): the resting arm nearer the body and straighter
        b46 = __import__("os").environ.get("TPDB_ARM46", "B") == "B"
        if out is None:
            out = 0.12 if b46 else 0.16
        return self.lm(f"sh_{sd}") + nrm((sg * out, fwd, -1)) * self.A * (0.985 if b46 else 0.97), (sg * 0.2, 0.6, 0)

    def hand_frame(self, sd, palm):
        """Fingers along the hand bone, palm facing `palm` (world), thumb on the thumb side."""
        sg = 1 if sd == "L" else -1
        w = self.rig.head(f"hand_{sd}")
        d = self.rig.bone_dir(f"hand_{sd}")
        n = Vector(palm)
        n = n - d * n.dot(d)
        if n.length < 1e-4:
            n = Vector((-sg, 0, 0)) - d * (-sg * d.x)
        n.normalize()
        t = (n.cross(d) * sg).normalized()
        return w, d, n, t

    def hand(self, sd, shape, palm=(0, -1, 0)):
        """Swap the mitten for an open hand, or add a pointing finger to it.

        Built in world space at the current pose and attached to the hand bone. Open hands hide
        the mitten (Hand_<sd>, Thumb_<sd>) for this action only."""
        k = self.c.k
        skin = self.c.spec["skin"]
        w, d, n, t = self.hand_frame(sd, palm)
        rot = Matrix((t, n, d)).transposed().to_quaternion()
        bone = f"hand_{sd}"
        if shape == "open":
            c = w + d * 0.054 * k
            self.prop(f"palm{sd}", ellipsoid(f"palm{sd}", c, (0.043 * k, 0.017 * k, 0.060 * k), skin, rot=rot), bone)
            for i, fx in enumerate((-0.026, -0.009, 0.009, 0.026)):
                # four short rounded finger tips past the palm, slightly spread, so the hand reads as open
                base = c + d * 0.036 * k + t * fx * k
                fd = (d + t * fx * 3.2).normalized()
                q = Vector((0, 0, 1)).rotation_difference(fd)
                ln = (0.030 if i in (1, 2) else 0.025) * k
                self.prop(f"fing{sd}{i}", ellipsoid(f"fing{sd}{i}", base + fd * ln * 0.55, (0.0105 * k, 0.0095 * k, ln), skin, rot=q), bone)
            tdir = (t * 0.80 + d * 0.50 + n * 0.12).normalized()
            base = c + t * 0.030 * k - d * 0.016 * k
            q = Vector((0, 0, 1)).rotation_difference(tdir)
            self.prop(f"thumb{sd}", ellipsoid(f"thumb{sd}", base + tdir * 0.022 * k, (0.0125 * k, 0.0125 * k, 0.027 * k), skin, rot=q), bone)
            self.hides.setdefault(self.cur, []).extend([f"Hand_{sd}", f"Thumb_{sd}"])
        elif shape == "point":
            # the mitten stays as a fist; an index finger sticks out along the arm
            base = w + d * 0.066 * k + t * 0.008 * k
            tip = w + d * 0.165 * k + t * 0.008 * k
            self.prop(f"index{sd}", cyl(f"index{sd}", base, tip, 0.0135 * k, skin, seg=14), bone)
            self.prop(f"indextip{sd}", ellipsoid(f"indextip{sd}", tip, (0.0135 * k, 0.0135 * k, 0.0135 * k), skin), bone)
            self.panchor(f"fingertip_{sd}", tip + d * 0.014 * k, bone)

    # ---------------------------------------------------------- props
    def prop(self, part, ob, bone="hand_R"):
        name = f"PROP_{self.cur}_{part}"
        ob.name = name
        self.rig.attach(ob, bone)
        ob.hide_render = True
        ob.hide_viewport = True
        self.props.setdefault(self.cur, []).append(name)
        return ob

    def panchor(self, name, loc, bone="hand_R"):
        anchor(self.rig, f"{name}@{self.cur}", loc, bone)
        self.anchors.setdefault(self.cur, []).append(name)

    def head_yaw(self):
        """Degrees the face is turned from straight ahead, toward the side view's camera (the figure's right)."""
        upd()
        pb = self.rig.arm.pose.bones["head"]
        f = (pb.matrix.to_3x3() @ pb.bone.matrix_local.to_3x3().inverted()) @ Vector((0, -1, 0))
        return math.degrees(math.atan2(-f.x, -f.y))

    # ---------------------------------------------------------- build
    def build(self, name, lower, upper, **meta):
        self.cur = name
        self.rig.reset()
        LOWER[lower](self, **meta.get("lower_args", {}))
        if upper:
            UPPER[upper](self)
        else:
            arms_rest(self)
        self.rig.key_pose(name)
        turn = PROFILE47
        # v0.48 (face.PROF48): which poses a side view draws with the side view's own face: those whose head, in the side view, is turned
        # no more than about 30 degrees toward the viewer (the twin's turn, or a turn the pose makes itself, as the ice-cream walker's does)
        own48 = self.head_yaw()
        if -4 <= own48 < 32:
            self.profile_face[name] = True
        if turn and HEAD47 == "B":
            # v0.47 (TPDB_HEAD47 "B"): see the switch. The twin brings the head to the turn, whatever the pose has turned it already (stuck up on
            # the seesaw and calling, the head is 40 degrees round); a head turned further, or turned away to look back, is left as posed
            own = self.head_yaw()
            turn = 0.0 if own >= -turn - 4 or own < -60 else turn + own
        if turn and HEAD47 == "B" and name in PROFILE_SKIP:
            for bn in ("spine", "chest"):
                pb = self.rig.arm.pose.bones[bn]
                pb.rotation_quaternion = pb.rotation_quaternion @ Quaternion((0, 1, 0), math.radians(turn / 2))
            upd()
            self.rig.key_pose(name + "__p")
        elif turn and name not in PROFILE_SKIP:
            # v0.27, chosen on the bench: a twin of the pose for full profile, the head turned a little toward the viewer (the eye sat on the head's outline: "face hidden",
            # "hard to read"; turning the head worked for the newspaper dog, isolation_v026.md). Not with a hand-held thing at the face, which it would leave behind
            pb = self.rig.arm.pose.bones["head"]
            pb.rotation_quaternion = pb.rotation_quaternion @ Quaternion((0, 1, 0), math.radians(turn))
            upd()
            self.rig.key_pose(name + "__p")
        self.meta[name] = dict(lower=lower, upper=upper, **{k: v for k, v in meta.items() if k != "lower_args"})
        # hide this action's props again for the next pose
        for n in self.props.get(name, []):
            bpy.data.objects[n].hide_render = True
            bpy.data.objects[n].hide_viewport = True
        return name


PROFILE_SKIP = ("photo", "drink", "sit_drink", "hose_inspect", "bucket_hat", "eat_ice_cream", "walk_ice_cream", "sit_ice_cream")


# ================================================================== lower bodies
STAND_FEET = {"L": (0.015, -0.055, 0.0), "R": (-0.015, 0.045, 0.0)}


# v0.48 (TPDB_STANCE48; pair bench 1, of v0.47's standing figure and v0.48's alike: "Feet: dark rounded blobs, no shape of a shoe"): standing, the
# feet are turned out by this many degrees each, as a person stands, so a front view shows each shoe's length and not its toe end on. 0: v0.47's
STANCE48 = float(_os44.environ.get("TPDB_STANCE48", "16"))


def turn_foot(P, sd, deg):
    """Turn a planted foot about the upright through its ankle (positive: the toe toward the figure's left)."""
    upd()
    pb = P.rig.arm.pose.bones[f"foot_{sd}"]
    M = pb.matrix.copy()
    h = M.translation.copy()
    pb.matrix = Matrix.Translation(h) @ Matrix.Rotation(math.radians(deg), 4, "Z") @ Matrix.Translation(-h) @ M
    upd()


def lo_stand(P, lean=0.0, head_pitch=0.0, head_turn=0.0, head_roll=0.0, side=0.0):
    # one foot a little ahead of the other: natural, and both legs show from the side
    feet = {sd: (dx, dy * P.s, lift) for sd, (dx, dy, lift) in STAND_FEET.items()}
    P.torso(lean=lean, head_pitch=head_pitch, head_turn=head_turn, head_roll=head_roll, side=side, drop=P.drop_hips_for(feet))
    P.place_legs(feet)
    if STANCE48:
        turn_foot(P, "L", STANCE48)
        turn_foot(P, "R", -STANCE48)


def lo_wide(P, lean=0.0, head_pitch=0.0):
    P.torso(lean=lean, head_pitch=head_pitch)
    P.place_legs({"L": (0.05, 0.0, 0.0), "R": (-0.05, 0.0, 0.0)})


def lo_walk(P, lean=4.0, head_pitch=0.0, head_turn=0.0):
    if WALK48 in ("B", "C") and WALK47 == "B" and lean == 4.0:
        lean = 7.0 if WALK48 == "B" else 8.0
    if WALK48 == "C" and WALK47 == "B":
        # (first trial: the rear foot 10 cm back with its heel lifting and the hips dropped for a long stride: both knees bent, a creeping walk)
        feet = {"L": (0.0, 0.070, 0.0), "R": (0.0, -0.165, 0.075 * P.s)}
        P.torso(lean=lean, drop=P.drop_hips_for({"L": feet["L"], "R": feet["L"]}), head_pitch=head_pitch, head_turn=head_turn)
        P.place_legs(feet, hint={"L": (0, -1, 0.05), "R": (0, -1, 0.75)})
        P.rig.aim_dir("foot_L", (0, -1, 0.02))                          # the rear foot flat under the body
        b = math.radians(14)
        P.rig.aim_dir("foot_R", (0, -math.cos(b), math.sin(b)))         # the leading toe up
        if SOLE45 == "H":
            P.hides.setdefault(P.cur, []).extend(["Sole_L", "Sole_R"])
        return
    foot = __import__("os").environ.get("TPDB_FOOT", "B")
    foot27 = foot in ("B", "C")
    feet = {"L": (0.0, 0.17, 0.02), "R": (0.0, -0.20, 0.0)}
    if foot27:
        # v0.27, chosen on the bench: the back heel lifted, on its toe, so the stride shows its direction (both feet flat, with a heel much like a toe:
        # "his head and arms face left", while "his legs and feet look like they stride towards the right")
        # v0.29 bench C: lifted less ("looks turned up")
        feet["L"] = (0.0, 0.15, (0.055 if foot == "B" else 0.036) * P.s)
    w47 = foot27 and WALK47 == "B"
    if w47:
        feet = {"L": (0.0, 0.17, 0.085 * P.s), "R": (0.0, -0.19, 0.0)}
    P.torso(lean=lean, drop=P.drop_hips_for(feet) + (0.012 * P.u if w47 else 0.0), head_pitch=head_pitch, head_turn=head_turn)
    P.place_legs(feet, hint={"L": (0, -1, -0.1), "R": (0, -1, 0.25)} if w47 else (0, -1, 0.25))
    if foot27:
        if w47:
            a = math.radians(46 if WALK48 == "B" else 64)
            P.rig.aim_dir("foot_L", (0, -math.cos(a), -math.sin(a)))
        else:
            P.rig.aim_dir("foot_L", (0, -0.72, -0.70) if foot == "B" else (0, -0.86, -0.50))
        if not (__import__("os").environ.get("TPDB_SHOE39", "D") == "D" and __import__("os").environ.get("TPDB_WALK40", "O") == "B"):
            # (v0.40, vision/flaws_v039.md O5, TPDB_WALK40 "B": the front foot is left as place_legs plants it, sole flat. Aimed level here, it sat
            # toe-up by the shoe's rest angle while the back foot tipped toe-down, and "The boy's feet point in different directions")
            P.rig.aim_dir("foot_R", (0, -1, 0.02))
    if w47 and WALK48 == "B":
        P.rig.aim_dir("foot_R", (0, -1, 0.02 + math.tan(math.radians(10))))
    if SOLE45 == "H":
        P.hides.setdefault(P.cur, []).extend(["Sole_L", "Sole_R"])      # v0.45 (TPDB_SOLE45)


def lo_run(P):
    if RUN44 == "A":
        # v0.44 (TPDB_RUN44): off the ground, the back shin kicked up behind, the front foot just lifted, the hips up, leaning into the run; the
        # raised back foot without its sole (a grey plate under a raised shoe)
        feet = {"L": (0.0, 0.20, 0.32), "R": (0.0, -0.24, 0.05)}
        r47 = RUN47 == "B"
        if r47:
            feet = {"L": (0.0, 0.34, 0.20), "R": (0.0, -0.22, 0.04)}
        P.torso(lean=16 if r47 else 16, drop=P.drop_hips_for(feet) + (0.06 * P.u if r47 else 0.0), head_pitch=4)
        P.place_legs(feet, hint={"L": (0, -1, -0.6), "R": (0, -1, 0.5)})
        if r47:
            a = math.radians(40)
            P.rig.aim_dir("foot_L", (0, math.cos(a) * 0.3, -math.sin(a)))
            P.rig.aim_dir("foot_R", (0, -1, -0.10))
        else:
            P.rig.aim_dir("foot_L", (0, 0.55, -0.83))
        P.hides.setdefault(P.cur, []).append("Sole_L")
        return
    feet = {"L": (0.0, 0.30, 0.16), "R": (0.0, -0.26, 0.0)}
    P.torso(lean=12, drop=P.drop_hips_for(feet) + 0.03 * P.u, head_pitch=4)
    P.place_legs(feet, hint={"L": (0, -1, -0.2), "R": (0, -1, 0.4)})


def lo_jump(P):
    feet = {"L": (0.02, 0.02, 0.17), "R": (-0.02, 0.02, 0.17)}
    P.torso(lean=2, drop=0.02 * P.u, head_pitch=10)
    P.place_legs(feet, hint=(0, -1, 0.5))


def lo_kick(P):
    feet = {"L": (0.01, 0.04, 0.0), "R": (-0.02, -0.42, 0.26)}
    P.torso(lean=-6, drop=0.02 * P.u, head_pitch=-14)
    P.place_legs(feet, hint={"L": (0, -1, 0.2), "R": (0, -1, 0.1)})


def lo_kick_low(P):
    """v0.12: the kicking foot low and forward, at the ball on the ground, the body leaning back over the
    planted foot (the high kick's straight leg, out from under a skirt, read as "a wooden bat")."""
    if KICK_REL:
        # v0.12, isolation round 5: the kicking foot raised and forward in proportion to the leg (a fixed lift
        # left a long-legged kicker's foot almost on the ground: "walking or stepping ... about to stumble")
        leg = P.J["hip"] - P.J["ankle"]
        feet = {"L": (0.015, 0.06, 0.0), "R": (-0.02, -KICK_FWD_F * leg, KICK_LIFT_F * leg)}
    else:
        feet = {"L": (0.015, 0.06, 0.0), "R": (-0.02, -0.36, 0.13)}
    P.torso(lean=-6, drop=P.drop_hips_for(feet), head_pitch=-26)
    P.place_legs(feet, hint={"L": (0, -1, 0.1), "R": (0, -1, 0.15)})


def lo_dig_lunge(P, lean=30.0, head_pitch=-12.0):
    """v0.12: digging stance, feet apart front and back, knees bent, bent forward over the spade."""
    feet = {"L": (0.03, -0.18, 0.0), "R": (-0.03, 0.17, 0.0)}
    P.torso(lean=lean, drop=P.drop_hips_for(feet) + 0.06 * P.u, back=0.02 * P.u, head_pitch=head_pitch)
    P.place_legs(feet, hint={"L": (0, -1, 0.6), "R": (0, -1, 0.6)})


def lo_sit(P, lean=-2.0, head_pitch=0.0):
    J, S, s = P.J, P.S, P.s
    drop = J["hip"] * S - J["knee"] * S
    # (v0.27: an adult's feet closer in, as the thigh is shorter: at 0.40 "he looks as if he is sliding")
    fwd = 0.32 if s == 1.0 and J["hip"] < 0.80 else 0.40
    feet = {"L": (0.02, -fwd * s, 0.0), "R": (-0.02, -fwd * s, 0.0)}
    P.torso(drop=drop, back=0.04 * S * s, lean=lean, head_pitch=head_pitch)
    P.place_legs(feet, hint=(0, -1, 1))


def lo_sit_swing(P):
    J, S, s = P.J, P.S, P.s
    drop = J["hip"] * S - J["knee"] * S
    feet = {"L": (0.02, -0.34 * s, 0.10 * s), "R": (-0.02, -0.38 * s, 0.06 * s)}
    P.torso(drop=drop, back=0.04 * S * s, lean=-4, head_pitch=6)
    P.place_legs(feet, hint=(0, -1, 1))


def lo_sit_ground(P):
    J, S, u = P.J, P.S, P.u
    drop = J["hip"] * S - 0.13 * u
    P.torso(drop=drop, back=0.0, lean=-14, head_pitch=4)
    if SITG47 == "C":
        # both legs out straight along the ground, a little apart, heels down and toes up
        dz = 0.13 * u - J["ankle"] * S
        reach = math.sqrt(max(0.0, P.L ** 2 - dz ** 2)) / S
        k, dx = 0.97, 0.05
        P.place_legs({"L": (dx, -(k - 0.03) * reach, 0.0), "R": (-dx, -k * reach, 0.0)}, hint=(0, -1, 1))
        for sd, sg in (("L", 1), ("R", -1)):
            P.rig.aim_dir("foot_" + sd, (sg * 0.12, -1.0, 0.6))
        return
    if SITG47 == "B":
        # v0.47 (TPDB_SITG47): see the switch. The near leg (R: the library draws this pose at 45 and 90) reaches 0.95 of the way the leg can
        dz = 0.13 * u - J["ankle"] * S
        out = 0.95 * math.sqrt(max(0.0, P.L ** 2 - dz ** 2)) / S
        P.place_legs({"L": (0.05, -0.40 * P.s, 0.0), "R": (-0.04, -out, 0.0)}, hint={"L": (0, -1, 1), "R": (-0.1, -1, 0.5)})
        P.rig.aim_dir("foot_R", (-0.18, -0.50, 1))
        return
    P.place_legs({"L": (0.03, -0.62 * P.s, 0.0), "R": (-0.03, -0.58 * P.s, 0.0)}, hint=(0, -1, 1))


def lo_crouch(P, head_pitch=20):
    feet = {"L": (0.04, -0.02, 0.0), "R": (-0.04, 0.02, 0.0)}
    P.torso(lean=30, drop=P.L * 0.42, back=0.10 * P.u, head_pitch=head_pitch)
    P.place_legs(feet, hint=(0, -1, 0.2))


def lo_kneel(P):
    u = P.u
    P.torso(lean=50, drop=P.L * 0.48, back=0.10 * u, head_pitch=-14)
    P.place_legs({"L": (0.02, 0.36 * P.s, 0.02), "R": (-0.03, -0.30 * P.s, 0.0)},
                 hint={"L": (0, -1, -0.6), "R": (0, -1, 1)})


def lo_lie(P):
    """Lying on the back, face up: rotate the whole body about the hips, then lower it."""
    rig, u = P.rig, P.u
    pb = rig.arm.pose.bones["hips"]
    upd()
    M = pb.matrix.copy()
    h = M.translation.copy()
    R = Matrix.Translation(h) @ Matrix.Rotation(math.radians(-90), 4, "X") @ Matrix.Translation(-h)
    lift = h.z - 0.115 * P.c.k
    pb.matrix = Matrix.Translation((0, 0, -lift)) @ R @ M
    upd()
    for sd, sg in (("L", 1), ("R", -1)):
        rig.aim_dir(f"thigh_{sd}", (sg * 0.06, -1, 0.02))
        rig.aim_dir(f"shin_{sd}", (sg * 0.04, -1, 0.0))
        rig.aim_dir(f"foot_{sd}", (sg * 0.1, -0.2, 1))
    rig.aim_dir("head", (0, 1, 0.12))


def lo_jump_tuck(P):
    """v0.7: a star jump, legs straight and spread wide, feet well off the ground (with the knees bent
    and the feet low, the v0.6 jump read as kneeling, and tucked feet behind read the same way)."""
    # v0.16: the whole body lifted 0.18 m with the legs straight and spread (with the hips left at standing height, feet
    # lifted 0.26 m bent the knees out into a squat in mid-air: a jumper "could be read as floating", "very high ... shadow
    # far below, nothing to jump off")
    lift = 0.18
    feet = {"L": (0.17, -0.02, lift), "R": (-0.17, -0.02, lift)}
    P.torso(lean=-2, drop=-lift * P.S, head_pitch=12)
    P.place_legs(feet, hint=(0, -1, 0.05))


def lo_sit_dangle(P):
    """Sitting high up with the legs hanging free and kicking: one foot forward, one tucked back."""
    J, S, s = P.J, P.S, P.s
    drop = J["hip"] * S - J["knee"] * S
    feet = {"L": (0.03, -0.30 * s, -0.04 * s), "R": (-0.03, -0.12 * s, -0.08 * s)}
    P.torso(drop=drop, back=0.04 * S * s, lean=8, head_pitch=-30)
    P.place_legs(feet, hint=(0, -1, 0.6))


def lo_sit_hang(P, head_pitch=-10.0, head_turn=-40.0):
    """v0.14: stuck high up: the legs hanging straight down, toes pointing down, one foot a little ahead, the
    head turned toward the viewer and level (the head bowed over the handle showed only the hair at 90 degrees,
    and knees bent with the feet tucked read as sitting comfortably: "nothing looks wrong there")."""
    J, S, s = P.J, P.S, P.s
    drop = J["hip"] * S - J["knee"] * S
    P.torso(drop=drop, back=0.04 * S * s, lean=6, head_pitch=head_pitch, head_turn=head_turn)
    P.place_legs({"L": (0.03, -0.16 * s, -0.14 * s), "R": (-0.03, -0.04 * s, -0.20 * s)}, hint=(0, -1, 0.6))
    for sd in ("L", "R"):
        P.rig.aim_dir(f"foot_{sd}", (0, -0.45, -1))


def lo_sit_low(P, lean=-10.0, head_pitch=2.0, feet=(0.15, -0.26)):
    """Sitting low (on the end of a plank resting on the ground) with knees up and feet planted,
    leaning back at ease."""
    J, S, u = P.J, P.S, P.u
    drop = J["hip"] * S - 0.20 * u
    P.torso(drop=drop, back=0.02 * u, lean=lean, head_pitch=head_pitch)
    # v0.8: feet planted wide and closer in, on either side of the plank (feet far ahead crossed the
    # rising plank and read as legs passing through it); v0.10: the reader's feet wider still and
    # nearer the seat (its shins still crossed the board)
    fx, fy = feet
    P.place_legs({"L": (fx, fy * P.s, 0.0), "R": (-fx, (fy - 0.02) * P.s, 0.0)}, hint=(0, -1, 1.4))


def lo_sit_slide(P, slope=34.0):
    """v0.10: sitting on a slide's chute on the way down: hips on the chute, legs straight out and
    down along it, the body upright."""
    J, S, u = P.J, P.S, P.u
    drop = J["hip"] * S - 0.13 * u
    P.torso(drop=drop, back=0.0, lean=-8, head_pitch=6)
    fy = 0.50 * P.s
    fz = 0.13 * P.s - fy * math.tan(math.radians(slope))
    lift = fz - J["ankle"]
    P.place_legs({"L": (0.04, -fy, lift), "R": (-0.04, -fy * 0.97, lift + 0.01 * P.s)}, hint=(0, -1, 1))


LOWER = {"stand": lo_stand, "wide": lo_wide, "walk": lo_walk, "run": lo_run, "jump": lo_jump, "kick": lo_kick,
         "kick_low": lo_kick_low, "dig_lunge": lo_dig_lunge,
         "sit": lo_sit, "sit_swing": lo_sit_swing, "sit_ground": lo_sit_ground, "crouch": lo_crouch,
         "kneel": lo_kneel, "lie": lo_lie, "jump_tuck": lo_jump_tuck, "sit_dangle": lo_sit_dangle, "sit_hang": lo_sit_hang, "sit_low": lo_sit_low,
         "sit_slide": lo_sit_slide}


# ================================================================== upper bodies (no props)
def arms_rest(P):
    P.arms({sd: P.rest_arm(sd) for sd in ("L", "R")})


def up_walk_swing(P):
    A = P.A
    P.arms({"R": (P.lm("sh_R") + nrm((-0.08, 0.40, -1)) * A * 0.95, (-0.2, 0.5, 0)),
            "L": (P.lm("sh_L") + nrm((0.08, -0.45, -1)) * A * 0.95, (0.2, 0.5, 0))})


def up_run_swing(P):
    u = P.u
    P.arms({"R": (P.lm("sh_R") + Vector((-0.03, 0.20, -0.30)) * u, (0, 1, -1)),
            "L": (P.lm("sh_L") + Vector((0.03, -0.28, -0.16)) * u, (0, 0.4, -1))})


def up_kick_swing(P):
    """v0.12: arms swinging against the kicking leg, one forward, one back and out (the arms held out to
    the sides came toward the viewer in side view and showed as stubs)."""
    u = P.u
    P.arms({"R": (P.lm("sh_R") + Vector((-0.10, -0.22, -0.26)) * u, (0, 1, -1)),
            "L": (P.lm("sh_L") + Vector((0.10, 0.30, -0.18)) * u, (0, 0.4, -1))})


def up_wave(P):
    # v0.8: a big, high wave: the hand up above the head and out to the side, forearm upright, open palm
    # facing forward (the hand at ear height read as scratching the head or leaning); clear of the head
    # at 0, 45 and 90 degrees
    d = Vector((-0.46, 0.10, 0.86))
    if P.c.spec.get("age") == "child":
        # v0.14: a child's arm is short for the big head, so the same aim left the hand by the ear, the motion
        # arcs beside it like sound ("either waving or listening to something"): the arm goes up and out on a
        # wider slant, the hand at the height of the top of the head and well clear of it
        d = nrm((-0.60, 0.05, 0.80))
    P.arms({"R": (P.lm("sh_R") + d * P.A, (-1, 0.2, -0.6)), "L": P.rest_arm("L")})
    P.hand("R", "open", palm=(0, -1, 0))


def up_point(P):
    # the far-side (left) arm points ahead and a little across, so at 45 and 90 degrees it shows
    # in front of the body instead of aiming at the camera
    P.arms({"L": (P.lm("sh_L") + nrm((0.18, -1, 0.10)) * P.A * 0.99, (1, 0.3, -0.6)), "R": P.rest_arm("R")})
    P.hand("L", "point")


def up_point_up(P):
    # far-side arm up and ahead of the face, index finger up
    P.arms({"L": (P.lm("sh_L") + nrm((0.20, -0.62, 0.76)) * P.A * 0.99, (1, 0.4, -0.5)), "R": P.rest_arm("R")})
    P.hand("L", "point")


def up_feel_rain(P):
    """v0.49 bench (flaws_v048.md R1; TPDB_RAIN49 "B", not chosen): a hand held out in front, palm up, for the first drop; the other arm
    at rest. The head looks up (the pose's head_pitch). The far arm, as in point_up: turned 45 degrees the near one, held forward, lies
    across the trunk."""
    u = P.u
    P.arms({"L": (P.lm("sh_L") + Vector((0.07, -0.33, -0.16)) * u, (0.6, 0.5, -1)), "R": P.rest_arm("R")})
    P.hand("L", "open", palm=(0, 0, 1))


def up_reach_up(P):
    A = P.A
    r40 = __import__("os").environ.get("TPDB_REACH40", "C")
    if r40 in ("B", "C"):
        # v0.40 (vision/flaws_v039.md R1): one hand up toward the hat, which flies up and ahead of the head on the side faced; with both arms up
        # the reader of the windy hat offered "throwing her hands up in alarm rather than reaching", as in v0.38. "B" the far hand up by the
        # chest, open (startled); "C" the far arm down at the side
        # (the far arm reaches: the near one, reaching up and ahead, crossed in front of the face at 45 like a hand shading the eyes)
        reach = P.lm("sh_L") + nrm((0.12, -0.62, 0.78)) * A * 0.995
        other = (P.lm("sh_R") + Vector((-0.02, -0.20, -0.12)) * P.u, (-1, 0.3, -0.8)) if r40 == "B" else P.rest_arm("R")
        P.arms({"L": (reach, (1, 0.5, -0.2)), "R": other})
        P.hand("L", "open", palm=(0, -0.3, 1))
        if r40 == "B":
            P.hand("R", "open", palm=(0, -1, 0.2))
        return
    # near (right) arm up and out to the side, far (left) arm up and ahead: both hands stay clear of
    # the head at 45 and 90 degrees
    P.arms({"R": (P.lm("sh_R") + nrm((-0.40, 0.16, 0.92)) * A * 0.995, (-1, 0.5, -0.2)),
            "L": (P.lm("sh_L") + nrm((0.18, -0.45, 0.88)) * A * 0.995, (1, 0.5, -0.2))})
    for sd in ("L", "R"):
        P.hand(sd, "open", palm=(0, -1, 0.2))


def up_hang_up(P):
    """Both hands raised ahead and up to the same height, as when pinning washing to a line."""
    A = P.A
    P.arms({"R": (P.lm("sh_R") + nrm((-0.04, -0.62, 0.78)) * A * 0.98, (-1, 0.3, -0.3)),
            "L": (P.lm("sh_L") + nrm((0.04, -0.62, 0.78)) * A * 0.98, (1, 0.3, -0.3))})
    for sd in ("L", "R"):
        P.hand(sd, "open", palm=(0, -1, 0.3))


def up_cheer(P):
    A = P.A
    P.arms({"R": (P.lm("sh_R") + nrm((-0.62, 0.22, 0.88)) * A * 0.99, (-1, 0.3, 0)),
            "L": (P.lm("sh_L") + nrm((0.50, -0.30, 0.90)) * A * 0.99, (1, 0.3, 0))})
    for sd in ("L", "R"):
        P.hand(sd, "open", palm=(0, -1, 0))


def up_slide_up(P):
    """v0.24 (bench TPDB_SLIDE=U): both arms up and ahead, the hands clear of the face in profile (out to the sides, as in
    cheer, they crossed it: "holding her head or hair", "covering the face"). The near arm low enough to pass under the chin
    (any steeper and it lies across a child's large head), the far arm higher, behind the head with the hand beyond the face;
    the palms to the side so the hands open toward the viewer (edge on, a hand read as "a stick, pencil or twig")."""
    A = P.A
    P.arms({"R": (P.lm("sh_R") + nrm((-0.10, -0.92, 0.38)) * A * 0.99, (-1, 0.3, -0.2)),
            "L": (P.lm("sh_L") + nrm((0.10, -0.72, 0.69)) * A * 0.99, (1, 0.3, -0.2))})
    for sd in ("L", "R"):
        P.hand(sd, "open", palm=(-1, 0, 0))


def up_slide_hold(P):
    """v0.24 bench (TPDB_SLIDE=H): both hands down at the sides of the chute, holding on."""
    u = P.u
    z = P.lm("pelvis").z - 0.02 * u
    P.arms({"R": (Vector((-0.20 * u, -0.10 * u, z)), (-1, 0.5, 0.1)), "L": (Vector((0.20 * u, -0.10 * u, z)), (1, 0.5, 0.1))})


def up_hands_on_hips(P):
    u = P.u
    z = P.lm("pelvis").z + 0.04 * u
    P.arms({"R": (Vector((-0.175 * u, 0.0, z)), (-1, 0.5, 0.1)), "L": (Vector((0.175 * u, 0.0, z)), (1, 0.5, 0.1))})


def up_shrug(P):
    u = P.u
    z = P.lm("pelvis").z + 0.20 * u
    P.arms({"R": (Vector((-0.36 * u, -0.16 * u, z)), (-0.3, 0.6, -1)), "L": (Vector((0.36 * u, -0.16 * u, z)), (0.3, 0.6, -1))})
    for sd in ("L", "R"):
        P.hand(sd, "open", palm=(0, 0, 1))


def up_hands_to_face(P):
    u = P.u
    m = P.lm("mouth")
    P.arms({"R": (m + Vector((-0.085, -0.06, 0.035)) * u, (-0.4, 0.2, -1)), "L": (m + Vector((0.085, -0.06, 0.035)) * u, (0.4, 0.2, -1))})
    for sd, sg in (("L", 1), ("R", -1)):
        P.hand(sd, "open", palm=(-sg, 0.6, 0))


def up_hold_front(P):
    u = P.u
    z = P.lm("pelvis").z + 0.14 * u
    P.arms({"R": (Vector((-0.06 * u, -0.30 * u, z)), (-1, 0.4, -0.6)), "L": (Vector((0.06 * u, -0.30 * u, z)), (1, 0.4, -0.6))})


def up_clap(P):
    # hands meet well out in front of the chest, palms together, elbows out
    u = P.u
    c = P.lm("chest")
    P.arms({"R": (c + Vector((-0.035, -0.36, 0.10)) * u, (-1, 0.1, -0.5)), "L": (c + Vector((0.035, -0.36, 0.10)) * u, (1, 0.1, -0.5))})
    for sd, sg in (("L", 1), ("R", -1)):
        P.hand(sd, "open", palm=(-sg, 0, 0))


def up_call_out(P):
    # far-side hand cupped just in front of the open mouth, clear of the face
    u = P.u
    m = P.lm("mouth")
    P.arms({"L": (m + Vector((0.05, -0.11, -0.03)) * u, (1, 0.3, -0.7)), "R": P.rest_arm("R")})
    P.hand("L", "open", palm=(-0.6, -0.3, 0))


def up_think(P):
    u = P.u
    m = P.lm("mouth")
    pel = P.lm("pelvis")
    # v0.47: the near elbow's hint was (-0.6, 0.4, -1), behind the trunk's side, and the upper arm lay in the chest's cloth: stray lines at the sleeve;
    # and the fist under the chin (it was at the mouth, 0.06 under the mouth's landmark, and covered it)
    P.arms({"R": (m + Vector((-0.01, -0.05, -0.13)) * u, (-0.7, -0.25, -1)),
            "L": (pel + Vector((-0.06, -0.17, 0.22)) * u, (1, 0.3, -0.6))})


def up_cross_arms(P):
    u = P.u
    c = P.lm("chest")
    P.arms({"R": (c + Vector((0.12, -0.15, -0.07)) * u, (-1, 0.2, -0.5)), "L": (c + Vector((-0.12, -0.17, -0.05)) * u, (1, 0.2, -0.5))})


def up_catch(P):
    u = P.u
    sz = P.lm("sh_R").z
    P.arms({"R": (Vector((-0.12 * u, -0.38 * u, sz + 0.06 * u)), (-1, 0.4, -0.6)), "L": (Vector((0.12 * u, -0.38 * u, sz + 0.06 * u)), (1, 0.4, -0.6))})
    for sd in ("L", "R"):
        P.hand(sd, "open", palm=(0, -1, 0.35))


def up_push(P):
    u = P.u
    z = P.lm("pelvis").z + 0.08 * u
    P.arms({"R": (Vector((-0.16 * u, -0.44 * u, z)), (-1, 0.5, -0.5)), "L": (Vector((0.16 * u, -0.44 * u, z)), (1, 0.5, -0.5))})
    for sd in ("L", "R"):
        P.panchor(f"push_{sd}", P.grip(sd), f"hand_{sd}")


def up_balance(P):
    A = P.A
    P.arms({"R": (P.lm("sh_R") + nrm((-1, 0.2, -0.15)) * A * 0.97, (0, 0.3, -1)),
            "L": (P.lm("sh_L") + nrm((1, -0.2, -0.05)) * A * 0.97, (0, 0.3, -1))})
    for sd in ("L", "R"):
        P.hand(sd, "open", palm=(0, 0, -1))


def up_ground_support(P):
    u = P.u
    pel = P.lm("pelvis")
    P.arms({"R": (pel + Vector((-0.22, 0.20, -0.08)) * u, (-0.4, 1, 0.3)), "L": (pel + Vector((0.22, 0.20, -0.08)) * u, (0.4, 1, 0.3))})


def up_lie_rest(P):
    rig = P.rig
    for sd, sg in (("L", 1), ("R", -1)):
        rig.aim_dir(f"upper_arm_{sd}", (sg * 0.30, -1, 0.05))
        rig.aim_dir(f"forearm_{sd}", (sg * 0.15, -1, 0.10))
        rig.aim_dir(f"hand_{sd}", (sg * 0.1, -1, 0.1))


def up_swing_hold(P):
    u = P.u
    # v0.15: the hands hold the ropes at chest height, elbows down by the sides (gripping at the shoulders, the arms
    # stuck out sideways past the ropes: "it is not clear that her hands are actually holding the chains")
    z = P.lm("pelvis").z + 0.30 * u
    P.arms({"R": (Vector((-0.15 * u, -0.06 * u, z)), (-0.7, 0.3, -1)), "L": (Vector((0.15 * u, -0.06 * u, z)), (0.7, 0.3, -1))})
    for sd in ("L", "R"):
        P.panchor(f"rope_{sd}", P.grip(sd), f"hand_{sd}")


def up_crouch_hands(P):
    u = P.u
    # hands resting on (just in front of) the knees
    kR = P.rig.head("thigh_R").lerp(P.rig.tail("thigh_R"), 0.70)
    kL = P.rig.head("thigh_L").lerp(P.rig.tail("thigh_L"), 0.70)
    P.arms({"R": (kR + Vector((0.0, -0.04, 0.05)) * u, (-0.6, 0.5, -0.6)), "L": (kL + Vector((0.0, -0.04, 0.05)) * u, (0.6, 0.5, -0.6))})


def up_crouch_reach(P):
    u = P.u
    z = P.J["hip"] * 0.72 * P.S
    P.arms({"R": (Vector((-0.10 * u, -0.44 * u, z + 0.03 * u)), (-0.8, 0.3, -0.5)), "L": (Vector((0.12 * u, -0.38 * u, z + 0.10 * u)), (0.8, 0.3, -0.5))})


def up_sit_rest(P):
    u = P.u
    z = P.lm("pelvis").z + 0.06 * u
    P.arms({"R": (Vector((-0.13 * u, -0.24 * u, z)), (-0.6, 0.5, -0.6)), "L": (Vector((0.13 * u, -0.24 * u, z)), (0.6, 0.5, -0.6))})


# ================================================================== upper bodies with props
def _hang_from(P, sd, drop_extra=0.0):
    """Arm hanging slightly out to the side, ready to carry something."""
    u = P.u
    sg = 1 if sd == "L" else -1
    tgt = P.lm(f"sh_{sd}") + Vector((sg * 0.12, -0.03, -1)).normalized() * P.A * 0.95
    return tgt, (sg * 0.2, 0.6, 0)


def up_water_can(P):
    u = P.u
    pel = P.lm("pelvis")
    P.arms({"R": (pel + Vector((-0.20, -0.30, 0.10)) * u, (-1, 0.5, -0.3)), "L": P.rest_arm("L")})
    g = P.grip("R")
    F = Frame.euler(g, rx=48)
    body_c = F.p(0, 0.01 * u, -0.13 * u)
    cc = _pcol(P, "teal", ("gray", "red", "blue"))      # v0.44 (TPDB_PROP44)
    P.prop("can", cyl("can", F.p(0, 0.01 * u, -0.215 * u), F.p(0, 0.01 * u, -0.045 * u), 0.085 * u, cc, seg=24))
    P.prop("handle", tube_mesh("handle", [F.p(0, 0.075 * u, -0.05 * u), F.p(0, 0.05 * u, 0.0), F.p(0, 0.0, 0.016 * u),
                                          F.p(0, -0.05 * u, 0.0), F.p(0, -0.075 * u, -0.05 * u)], 0.012 * u, cc))
    s0, s1 = F.p(0, -0.07 * u, -0.19 * u), F.p(0, -0.27 * u, -0.06 * u)
    P.prop("spout", cyl("spout", s0, s1, 0.018 * u, cc, r1=0.012 * u))
    d = (s1 - s0).normalized()
    P.prop("rose", cyl("rose", s1 - d * 0.005 * u, s1 + d * 0.03 * u, 0.014 * u, "gray", r1=0.032 * u))
    P.panchor("spout", s1 + d * 0.03 * u)
    P.panchor("spout_aim", s1 + d * 0.33 * u)


PAN_V019 = True
# v0.23 bench styles (TPDB_PAN; the release builds with D): "B" the arm held out from the body and the whole handle showing
# between the hand and the pan; "C" as B with the pan tipped forward to pour; "D" the pan seen from above at a slant,
# deeper, on a thicker handle about as long as the pan is wide (both bench readers: "a frying pan or saucepan"); "E" the
# v0.19 face-on pan on that handle ("the sprinkler head (rose) of a watering can ... or a frying pan"); "v19" the v0.19 pan
PAN_STYLE = __import__("os").environ.get("TPDB_PAN", "D")   # v0.23: D, chosen on the bench (isolation_v023.md)


def up_water_pan(P):
    """Watering with a frying pan. The pan's open face is turned toward the viewer (character's right,
    -X), so it reads as a round pan with a silver inside; edge-on it read as a hose wand."""
    u = P.u
    pel = P.lm("pelvis")
    if PAN_STYLE in ("B", "C", "D", "E"):
        _water_pan_v23(P, PAN_STYLE)
        return
    P.arms({"R": (pel + Vector((-0.20, -0.24, 0.20)) * u, (-1, 0.5, -0.3)), "L": P.rest_arm("L")})
    g = P.grip("R")
    R = 0.15 * u
    c = g + Vector((-0.02, -0.20, -0.03)) * u + Vector((0, -R, 0))
    # seen from above at a slant: the dark inside as an ellipse inside a deep rim (face-on, a silver
    # inside read as a magnifying glass)
    if PAN_V019:
        # v0.19: turned further toward the viewer with a grey inside under a black rim, and a shorter, stouter handle (on the
        # bench the squashed dark dish on a long thin handle read "(a) a frying pan ... or (b) the spout and rose of a
        # watering can")
        c = g + Vector((-0.02, -0.16, -0.03)) * u + Vector((0, -R, 0))
        n = nrm((-0.72, -0.18, 0.67))
        P.prop("handle", cyl("handle", g + Vector((0, 0.05, 0.0)) * u, c + Vector((0, R * 0.92, 0.02 * u)), 0.026 * u, "charcoal"))
        P.prop("grip", cyl("grip", g + Vector((0, 0.05, 0.0)) * u, g + Vector((0, -0.06, 0.0)) * u, 0.030 * u, "brown"))
        P.prop("pan", cyl("pan", c - n * 0.034 * u, c + n * 0.034 * u, R * 0.86, "charcoal", seg=36, r1=R))
        P.prop("panin", cyl("panin", c + n * 0.030 * u, c + n * 0.035 * u, R * 0.84, "gray", seg=36))
    else:
        n = nrm((-0.55, -0.20, 0.81))
        P.prop("handle", cyl("handle", g + Vector((0, 0.05, 0.0)) * u, c + Vector((0, R * 0.92, 0.02 * u)), 0.020 * u, "charcoal"))
        P.prop("grip", cyl("grip", g + Vector((0, 0.05, 0.0)) * u, g + Vector((0, -0.06, 0.0)) * u, 0.025 * u, "brown"))
        P.prop("pan", cyl("pan", c - n * 0.030 * u, c + n * 0.030 * u, R * 0.88, "charcoal", seg=36, r1=R))
        P.prop("panin", cyl("panin", c + n * 0.026 * u, c + n * 0.031 * u, R * 0.90, "slate", seg=36))
    rim = c + Vector((0, -R * 0.95, -0.02 * u))
    P.panchor("spout", rim)
    P.panchor("spout_aim", rim + Vector((0, -0.30, -0.14)) * u)


def _water_pan_v23(P, style):
    """v0.23: the pan held out from the body by the end of its handle, the whole handle showing between the hand and the
    pan (held close, the hand over a short handle, a v0.22 reader saw "a grey, round watering can ... no spout or handle")."""
    u = P.u
    pel = P.lm("pelvis")
    P.arms({"R": (pel + Vector((-0.22, -0.40, 0.25)) * u, (-1, 0.5, -0.3)), "L": P.rest_arm("L")})
    g = P.grip("R")
    R = 0.15 * u
    d = nrm((-0.06, -1.0, -0.10))                       # the handle runs forward from the fist, a little down
    # B, C: a long handle (0.25) showing beyond the fist; D, E (round 2): a handle about as long as the pan is wide, thicker
    L = (0.25 if style in ("B", "C") else 0.14) * u
    hr = (0.022 if style in ("B", "C") else 0.028) * u
    depth = 0.045 * u if style == "D" else 0.034 * u
    c = g + d * (L + R * 0.96)
    n = {"B": (-0.72, -0.18, 0.67), "C": (-0.70, -0.46, 0.55), "D": (-0.40, -0.12, 0.91), "E": (-0.72, -0.18, 0.67)}[style]
    n = nrm(n)
    P.prop("grip", cyl("grip", g - d * 0.05 * u, g + d * 0.05 * u, hr + 0.007 * u, "charcoal"))
    P.prop("handle", cyl("handle", g + d * 0.04 * u, c - d * R * 0.90, hr, "charcoal"))
    P.prop("pan", cyl("pan", c - n * depth, c + n * depth, R * 0.86, "charcoal", seg=36, r1=R))
    P.prop("panin", cyl("panin", c + n * (depth - 0.004 * u), c + n * (depth + 0.001 * u), R * 0.84, "gray", seg=36))
    # the pour leaves the far rim, the one tipped down and forward
    far = (d - n * d.dot(n)).normalized()
    rim = c + far * R * 0.95 + Vector((0, 0, -0.02 * u))
    P.panchor("spout", rim)
    P.panchor("spout_aim", rim + Vector((0, -0.30, -0.14)) * u)


def _nozzle(P, F, drop=0.22):
    """A hose end held in the fist: the hose runs in from below and behind, a short brass nozzle
    sticks out in front. No pistol grip, so it can never read as a gun. drop: how far the hose hangs below the fist before the
    template's drawn hose takes over (v0.40: longer for the far hand to hold)."""
    u = P.u
    noz27 = __import__("os").environ.get("TPDB_NOZ", "B") == "B"
    pts = [F.p(0, 0.13 * u, -0.16 * u), F.p(0, 0.09 * u, -0.06 * u), F.p(0, 0.04 * u, -0.005 * u), F.p(0, -0.025 * u, 0.012 * u)]
    if noz27:
        # v0.27, chosen on the bench: the hose hangs from the fist, below it and in plain sight (run in from behind, past the forearm, it "seems to end at a rounded tip near her hip")
        pts = [F.p(0, -0.012 * u, -0.22 * u), F.p(0, 0.012 * u, -0.11 * u), F.p(0, 0.026 * u, -0.02 * u), F.p(0, -0.025 * u, 0.012 * u)]
        if drop > 0.22:
            pts = [F.p(0, -0.024 * u, -drop * u)] + pts
    P.prop("hose", tube_mesh("hose", pts, 0.030 * u if noz27 else 0.022 * u, "hose"))
    P.prop("collar", cyl("collar", F.p(0, -0.020 * u, 0.012 * u), F.p(0, -0.050 * u, 0.014 * u), 0.026 * u, "yellow", seg=18))
    P.prop("tip", cyl("tip", F.p(0, -0.048 * u, 0.014 * u), F.p(0, -0.105 * u, 0.017 * u), 0.020 * u, "yellow", r1=0.011 * u, seg=18))
    tip = F.p(0, -0.108 * u, 0.017 * u)
    P.panchor("nozzle", tip)
    P.panchor("nozzle_aim", tip + F.d(0, -0.40, -0.10) * u)
    P.panchor("hose_in", (F.p(0, -0.024 * u, -drop * u) if drop > 0.22 else F.p(0, -0.012 * u, -0.22 * u)) if noz27 else F.p(0, 0.13 * u, -0.16 * u))


def up_hose_spray(P):
    u = P.u
    pel = P.lm("pelvis")
    P.arms({"R": (pel + Vector((-0.16, -0.32, 0.16)) * u, (-1, 0.5, -0.4)), "L": P.rest_arm("L")})
    _nozzle(P, Frame.euler(P.grip("R"), rx=14))


def up_hose_inspect(P):
    u = P.u
    eyes = (P.lm("eye_L") + P.lm("eye_R")) / 2
    tR = eyes + Vector((-0.03, -0.24, -0.13)) * u
    if __import__("os").environ.get("TPDB_HOSE40", "B") == "B":
        # v0.40 (vision/flaws_v039.md O3): the near hand holds the nozzle up to the face, the far hand the hose below it, elbow down. Both hands
        # together at the nozzle, the two white sleeves were "one long flat white shape stretched out to the nozzle"
        P.arms({"R": (tR, (-1, 0.3, -0.7))})
        g = P.grip("R")
        F = Frame(g, frame_toward(g, (eyes - g)).q)
        _nozzle(P, F, drop=0.46)
        P.arms({"L": (F.p(0, -0.02 * u, -0.36 * u), (1, 0.2, -1.0))})
        return
    P.arms({"R": (tR, (-1, 0.3, -0.7)), "L": (tR + Vector((0.08, 0.0, 0.04)) * u, (1, 0.3, -0.7))})
    g = P.grip("R")
    F = frame_toward(g, (eyes - g))
    F = Frame(g, F.q)
    _nozzle(P, F)


def _pole_grips(P, H, T, fr_L, fr_R, hintL=(1, 0.3, -0.6), hintR=(-1, 0.3, -0.6)):
    gL = H.lerp(T, fr_L)
    gR = H.lerp(T, fr_R)
    P.arms({"L": (gL, hintL), "R": (gR, hintR)})
    return gL, gR


def up_broom(P, tool="broom"):
    u = P.u
    pel = P.lm("pelvis")
    # the pole leans across the body: head on the floor out to the right and in front,
    # handle up by the left shoulder, so it reads as a sweep from every yaw
    H = pel + Vector((-0.36, -0.46, 0.0)) * u
    H.z = 0.06 * u
    T = pel + Vector((0.10, -0.27, 0.34)) * u
    _pole_grips(P, H, T, 0.92, 0.72)
    _broom_tool(P, H, T, tool)


def _broom_tool(P, H, T, tool):
    u = P.u
    d = (T - H).normalized()
    if tool == "broom":
        P.panchor("broom_tip", H - d * 0.07 * u)
        P.prop("stick", cyl("stick", H + d * 0.08 * u, T + d * 0.06 * u, 0.016 * u, "wood"))
        q = Vector((0, 0, 1)).rotation_difference(d)
        style = __import__("os").environ.get("TPDB_BROOM", "B")
        if style == "B":
            # v0.27, chosen on the bench: a dense corn broom. Bristles overlapping with no gaps, a straight cut edge and two bindings at the neck (the v0.26 fan's
            # separate bristles read as tines: "a long yellow-headed rake", the v0.26 screen's one misread; isolation_v027.md)
            ncam = nrm((-0.72, -0.62, 0.0))
            wb = ncam.cross(d).normalized()
            # (round 1's flare, 0.029 at the tips to 0.009 at the neck, was still "a yellow fanned head", "a broom or a fan rake": round 2 stands them nearly parallel)
            for i in range(-5, 6):
                P.prop(f"bristle{i + 5}", cyl(f"bristle{i + 5}", H - d * 0.12 * u + wb * (i * 0.0205 * u), H + d * 0.13 * u + wb * (i * 0.0125 * u), 0.024 * u, "yellow", seg=8, r1=0.020 * u))
            P.prop("band2", cyl("band2", H + d * 0.13 * u, H + d * 0.165 * u, 0.046 * u, "red"))
        elif style == "C":
            # v0.27 bench: a yard broom: a straight wooden block across the end of the pole, a short dense row of bristles below it
            ncam = nrm((-0.72, -0.62, 0.0))
            wb = ncam.cross(d).normalized()
            nb = d.cross(wb).normalized()
            qb = Matrix((wb, nb, d)).transposed().to_quaternion()
            P.prop("block", box("block", H + d * 0.055 * u, (0.44 * u, 0.055 * u, 0.055 * u), "wood", rot=qb, bevel=0.008 * u))
            for i in range(-7, 8):
                P.prop(f"bristle{i + 7}", cyl(f"bristle{i + 7}", H - d * 0.08 * u + wb * (i * 0.0285 * u), H + d * 0.04 * u + wb * (i * 0.0285 * u), 0.020 * u, "yellow", seg=6, r1=0.016 * u))
        elif style == "A":
            # v0.26, chosen on the bench: a fan of bristles, each outlined, with its flat face to the viewer (the plain yellow wedge had "no
            # visible bristles" and read as "a dustpan or scraper", in all four cut-outs of the first round; isolation_v026.md)
            ncam = nrm((-0.72, -0.62, 0.0))
            wb = ncam.cross(d).normalized()
            for i in range(-3, 4):
                P.prop(f"bristle{i + 3}", cyl(f"bristle{i + 3}", H - d * 0.08 * u + wb * (i * 0.048 * u), H + d * 0.09 * u + wb * (i * 0.014 * u), 0.027 * u, "yellow", seg=8, r1=0.014 * u))
        else:
            P.prop("bristles", cyl("bristles", H - d * 0.07 * u, H + d * 0.09 * u, 0.115 * u, "yellow", seg=4, r1=0.05 * u))
        if style != "C":
            P.prop("band", cyl("band", H + d * 0.07 * u if style != "B" else H + d * 0.185 * u, H + d * 0.11 * u if style != "B" else H + d * 0.22 * u, 0.04 * u, "red"))
    elif tool == "dinner_fork":
        # v0.7: a giant dining fork, not a garden fork. Its flat face is turned toward the viewer (the
        # character's right and front, as for the frying pan) so the cutlery outline shows: a flat
        # handle that flares to a rounded end, a narrow neck, a broad curved head and four slim, close
        # tines whose tips touch the ground. The pole is held low and diagonal, mid-sweep (upright with
        # its tines down, the v0.6 fork read as a garden fork someone leaned on).
        ncam = nrm((-0.72, -0.62, 0.0))
        w = ncam.cross(d)
        w.normalize()
        n = d.cross(w).normalized()
        q = Matrix((w, n, d)).transposed().to_quaternion()
        P.prop("stick", box("stick", H.lerp(T, 0.60), (0.052 * u, 0.018 * u, (T - H).length * 0.80), "silver", rot=q, bevel=0.006 * u))
        # (no flared handle end: by the shoulder it read as a spoon held to the face)
        P.prop("neck", box("neck", H + d * 0.24 * u, (0.030 * u, 0.016 * u, 0.12 * u), "silver", rot=q, bevel=0.005 * u))
        P.prop("shoulder", ellipsoid("shoulder", H + d * 0.13 * u, (0.088 * u, 0.017 * u, 0.045 * u), "silver", rot=q))
        P.prop("head", box("head", H + d * 0.08 * u, (0.175 * u, 0.017 * u, 0.06 * u), "silver", rot=q, bevel=0.008 * u))
        tips = []
        for i, x in enumerate((-0.066, -0.022, 0.022, 0.066)):
            b0 = H + d * 0.07 * u + w * x * u
            b1 = b0 - d * 0.10 * u
            tip = b1 - d * 0.05 * u + n * 0.025 * u
            P.prop(f"tine{i}", tube_mesh(f"tine{i}", [b0, b1, tip], 0.0105 * u, "silver"))
            tips.append(tip)
        mid = sum(tips, Vector()) / len(tips)
        P.panchor("fork_tip", Vector((mid.x, mid.y, 0.0)))
    elif tool == "fork":
        P.prop("stick", cyl("stick", H + d * 0.10 * u, T + d * 0.06 * u, 0.018 * u, "gray"))
        side = nrm(Vector((1, 0, 0)) - d * d.x)
        P.prop("neck", cyl("neck", H + d * 0.06 * u, H + d * 0.12 * u, 0.06 * u, "gray", r1=0.02 * u))
        P.prop("plate", box("plate", H + d * 0.05 * u, (0.20 * u, 0.025 * u, 0.04 * u), "gray", rot=Vector((0, 0, 1)).rotation_difference(d)))
        for i, x in enumerate((-0.075, -0.025, 0.025, 0.075)):
            base = H + d * 0.05 * u + side * x * u
            P.prop(f"tine{i}", cyl(f"tine{i}", base, base - d * 0.17 * u, 0.012 * u, "gray", r1=0.008 * u))
    elif tool == "rake":
        P.panchor("rake_head", Vector((H.x, H.y, 0.0)), "hand_R")
        P.prop("stick", cyl("stick", H + d * 0.02 * u, T + d * 0.06 * u, 0.016 * u, "wood"))
        side = nrm(Vector((1, 0, 0)) - d * d.x)
        P.prop("head", cyl("head", H - side * 0.19 * u, H + side * 0.19 * u, 0.018 * u, "gray"))
        for i in range(7):
            base = H + side * (-0.17 + i * 0.0567) * u
            P.prop(f"tine{i}", cyl(f"tine{i}", base, base + Vector((0, -0.03, -0.07)) * u, 0.008 * u, "gray"))


def up_sweep(P):
    up_broom(P, "broom")


def up_sweep_fork(P):
    up_broom(P, "fork")


def up_sweep_dinner_fork(P):
    """Sweeping with a giant dining fork held low, the tines dragging flat across the ground."""
    u = P.u
    pel = P.lm("pelvis")
    # the pole crosses the body: head on the ground out to the left and in front, handle end by the
    # right hip, so it lies diagonally across the picture at the 45-degree view the template uses
    H = pel + Vector((0.50, -0.50, 0.0)) * u
    T = pel + Vector((-0.14, -0.18, 0.36)) * u
    # lift the head so the tine tips (0.15 u below it along the pole) just touch the ground
    d = (T - H).normalized()
    H.z = d.z * 0.16 * u + 0.01 * u
    _pole_grips(P, H, T, 0.70, 0.93, hintL=(1, 0.3, -0.6), hintR=(-1, 0.5, -0.5))
    _broom_tool(P, H, T, "dinner_fork")


# v0.8: the giant fork as a piece of cutlery. A dinner fork's own proportions scaled to a person's
# height: four long parallel tines with clear gaps (a rake has many short ones, a fan rake spreads
# them), a head no wider than the tines, rounded shoulders down to a narrow neck, and a flat handle
# that widens to a rounded end. All lengths in u (about a metre for a grown-up), y from the tine tips.
FORK = dict(L=1.30, TL=0.30, TW=0.032, G=0.028, NW=0.046, NY=0.50, NL=0.10, EW=0.135, T=0.022)


def giant_fork_outline(L=1.30, TL=0.30, TW=0.032, G=0.028, NW=0.046, NY=0.50, NL=0.10, EW=0.135, **_):
    import math
    HW = 4 * TW + 3 * G
    body = TL + 0.06                      # where the solid head starts above the tines
    pts = [(-HW / 2, body)]
    for i in range(4):
        xl = -HW / 2 + i * (TW + G)
        xr = xl + TW
        # down the tine's left edge, a rounded point, up its right edge
        pts += [(xl, 0.035), (xl + 0.006, 0.012), (xl + TW / 2, 0.0), (xr - 0.006, 0.012), (xr, 0.035)]
        if i < 3:
            # the rounded top of the gap to the next tine
            pts += [(xr, TL - 0.012), (xr + G * 0.25, TL - 0.002), (xr + G * 0.5, TL), (xr + G * 0.75, TL - 0.002), (xr + G, TL - 0.012)]
    pts.append((HW / 2, body))
    # right shoulder: a rounded curve in to the neck
    for k in range(1, 7):
        t = k / 6
        x = (1 - t) ** 2 * (HW / 2) + 2 * (1 - t) * t * (HW / 2) + t * t * (NW / 2)
        y = (1 - t) ** 2 * body + 2 * (1 - t) * t * (NY - 0.02) + t * t * NY
        pts.append((x, y))
    # neck, then the handle widening to its rounded end
    hy0, hy1, er = NY + NL, L - EW / 2, EW / 2
    pts.append((NW / 2 + 0.002, hy0))
    for k in range(1, 9):
        t = k / 8
        pts.append((NW / 2 + 0.002 + (er - NW / 2 - 0.002) * (t ** 1.4), hy0 + (hy1 - hy0) * t))
    for k in range(1, 12):
        a = math.pi * k / 12
        pts.append((er * math.cos(a), hy1 + er * math.sin(a)))
    for k in range(8, 0, -1):
        t = k / 8
        pts.append((-(NW / 2 + 0.002 + (er - NW / 2 - 0.002) * (t ** 1.4)), hy0 + (hy1 - hy0) * t))
    pts.append((-(NW / 2 + 0.002), hy0))
    for k in range(6, 0, -1):
        t = k / 6
        x = (1 - t) ** 2 * (HW / 2) + 2 * (1 - t) * t * (HW / 2) + t * t * (NW / 2)
        y = (1 - t) ** 2 * body + 2 * (1 - t) * t * (NY - 0.02) + t * t * NY
        pts.append((-x, y))
    return pts


def giant_fork(P, G0, d, ncam=(-0.72, -0.62, 0.0), name="fork"):
    """Draw the giant fork with its tine tips at G0 and its axis along d (tips to handle end), the flat
    face turned toward ncam. Returns (point along the axis at a given y, w)."""
    u = P.u
    d = nrm(d)
    w = nrm(Vector(ncam).cross(d))
    n = d.cross(w).normalized()
    pts = giant_fork_outline(**FORK)
    P.prop(name, flat_prism(name, [(x * u, y * u) for x, y in pts], G0, w, d, n, FORK["T"] * u, "silver"))
    P.panchor("fork_tip", Vector((G0.x, G0.y, 0.0)))
    return (lambda y: G0 + d * (y * u)), w


def up_sweep_giant_fork(P):
    """Sweeping with a giant dining fork held like a broom: the four tines on the ground ahead and to
    the left, the flat face to the viewer, the handle up across the body to the right hand."""
    u = P.u
    pel = P.lm("pelvis")
    G0 = pel + Vector((0.56, -0.40, 0.0)) * u
    G0.z = 0.004 * u
    E = pel + Vector((-0.14, -0.16, 0.26)) * u
    d = nrm(E - G0)
    # hands first (a prop rides the hand it is attached to), then the fork between them
    P.arms({"L": (G0 + d * 0.92 * u, (1, 0.3, -0.6)), "R": (G0 + d * 1.16 * u, (-1, 0.5, -0.5))})
    giant_fork(P, G0, d)


def up_spade_pat(P):
    """v0.8: building a sandcastle: kneeling, a small spade in the right hand patting the top of the castle
    in front of the knees, the left hand smoothing its side (sitting beside the castle read as resting)."""
    u = P.u
    P.arms({"R": (Vector((-0.08 * u, -0.34 * u, 0.36 * u)), (-0.8, 0.4, -0.5)), "L": (Vector((0.10 * u, -0.33 * u, 0.33 * u)), (0.8, 0.4, -0.5))})
    g = P.grip("R")
    if SPADE44 == "A":
        # v0.44 (TPDB_SPADE44): the handle runs down into a blade twice the size, square at the top and pointed at the foot, its flat face turned
        # half to the viewer (seen at 45)
        top = g - Vector((0, 0.04, 0.09)) * u
        P.prop("handle", cyl("handle", g + Vector((0, 0.0, 0.05)) * u, top - Vector((0, 0.004, 0.02)) * u, 0.018 * u, "blue"))
        ax, ay = Vector((0.70, -0.70, 0.0)), Vector((0.0, -0.20, -0.98)).normalized()
        outline = [(-0.075, 0.0), (0.075, 0.0), (0.075, 0.11), (0.0, 0.17), (-0.075, 0.11)]
        P.prop("blade", flat_prism("blade", [(x * u, y * u) for x, y in outline], top, ax, ay, ax.cross(ay), 0.014 * u, "red"))
        P.panchor("spade_tip", top + ay * 0.17 * u)
        P.panchor("build_point", Vector((0.0, -0.44 * u, 0.0)))
        return
    P.prop("handle", cyl("handle", g + Vector((0, 0.0, 0.05)) * u, g - Vector((0, 0.03, 0.05)) * u, 0.018 * u, "blue"))
    P.prop("blade", box("blade", g - Vector((0, 0.05, 0.10)) * u, (0.08 * u, 0.014 * u, 0.08 * u), "red", bevel=0.01 * u))
    P.panchor("spade_tip", g - Vector((0, 0.06, 0.15)) * u)
    P.panchor("build_point", Vector((0.0, -0.44 * u, 0.0)))


def up_rake(P):
    up_broom(P, "rake")


def up_dig(P):
    u = P.u
    pel = P.lm("pelvis")
    B = pel + Vector((-0.08, -0.40, 0.0)) * u
    B.z = 0.10 * u
    T = pel + Vector((-0.02, -0.16, 0.20)) * u
    _pole_grips(P, B, T, 0.74, 1.0)
    d = (T - B).normalized()
    P.prop("shaft", cyl("shaft", B + d * 0.12 * u, T + d * 0.02 * u, 0.016 * u, "wood"))
    side = nrm(Vector((1, 0, 0)) - d * d.x)
    P.prop("thandle", cyl("thandle", T + d * 0.02 * u - side * 0.06 * u, T + d * 0.02 * u + side * 0.06 * u, 0.015 * u, "wood"))
    P.prop("blade", box("blade", B, (0.19 * u, 0.02 * u, 0.24 * u), "gray", rot=Vector((0, 0, 1)).rotation_difference(d)))


def up_dig_lift(P):
    """v0.12: lifting a spadeful of earth: the blade out in front at knee height, level, a clump of earth
    on it, the shaft rising back to both hands at the hip (the upright spade beside the legs, a hand at
    the chest, read as "leaning on the spade ... tired or unwell")."""
    u = P.u
    pel = P.lm("pelvis")
    B = pel + Vector((-0.04, -0.60, 0.0)) * u
    B.z = 0.17 * u
    T = pel + Vector((-0.10, -0.06, 0.06)) * u
    _pole_grips(P, B, T, 0.72, 0.96, hintL=(1, 0.2, -0.8), hintR=(-1, 0.4, -0.6))
    d = (T - B).normalized()
    side = nrm(Vector((1, 0, 0)) - d * d.x)
    P.prop("thandle", cyl("thandle", T + d * 0.03 * u - side * 0.06 * u, T + d * 0.03 * u + side * 0.06 * u, 0.015 * u, "wood"))
    if not SPADE_V2:
        P.prop("shaft", cyl("shaft", B + d * 0.10 * u, T + d * 0.03 * u, 0.016 * u, "wood"))
        # the blade lies nearly flat, pointing away, so it can hold the earth
        fwd = nrm(Vector((d.x, d.y, 0)) * -1)
        q = Vector((0, 0, 1)).rotation_difference(fwd)
        bc = B - fwd * 0.02 * u
        P.prop("blade", box("blade", bc, (0.19 * u, 0.02 * u, 0.25 * u), "gray", rot=q))
        P.prop("earth", ellipsoid("earth", bc + Vector((0, 0, 0.05)) * u - fwd * 0.01 * u, (0.10 * u, 0.09 * u, 0.06 * u), "soil"))
        P.panchor("spade", bc, "hand_L")
        return
    # v0.12, isolation round 3: the level grey plate read as "a flat plate or spatula", "not clearly joined
    # to the handle". Now a spade: a dark blade cut to a spade's outline (square heel, rounded point) that
    # starts at the end of the shaft, joined by a socket, its nose dipping toward the hole and its face
    # turned toward the viewer so the earth on it shows.
    P.prop("shaft", cyl("shaft", B + d * 0.07 * u, T + d * 0.03 * u, 0.016 * u, "wood"))
    P.prop("socket", cyl("socket", B - d * 0.005 * u, B + d * 0.10 * u, 0.028 * u, "slate", r1=0.019 * u))
    fwd = nrm(Vector((-d.x, -d.y, 0)))
    up = Vector((0, 0, 1))
    sd = nrm(up.cross(fwd))
    a, phi = math.radians(SPADE_PITCH), math.radians(SPADE_ROLL)
    zb = fwd * math.cos(a) - up * math.sin(a)
    n0 = up * math.cos(a) + fwd * math.sin(a)
    xb = sd * math.cos(phi) + n0 * math.sin(phi)
    yb = n0 * math.cos(phi) - sd * math.sin(phi)
    outline = [(-0.10, 0.0), (0.10, 0.0), (0.10, 0.16), (0.085, 0.205), (0.05, 0.24), (0.0, 0.262),
               (-0.05, 0.24), (-0.085, 0.205), (-0.10, 0.16)]
    P.prop("blade", flat_prism("blade", [(x * u, y * u) for x, y in outline], B, xb, zb, yb, 0.022 * u, "slate"))
    q = Matrix((xb, yb, zb)).transposed().to_quaternion()
    # a low heap of earth, two lumps so it cannot pass for a ball
    P.prop("earth", ellipsoid("earth", B + zb * 0.10 * u + yb * 0.035 * u, (0.088 * u, 0.042 * u, 0.080 * u), "soil", rot=q))
    P.prop("earth2", ellipsoid("earth2", B + zb * 0.165 * u + xb * 0.035 * u + yb * 0.03 * u, (0.05 * u, 0.034 * u, 0.05 * u), "soil", rot=q))
    P.panchor("spade", B + zb * 0.13 * u, "hand_L")


SPADE_V2, SPADE_PITCH, SPADE_ROLL = True, 22.0, 35.0
KICK_REL, KICK_FWD_F, KICK_LIFT_F = True, 0.85, 0.40


# v0.32 bench (TPDB_BOX; isolation_v032.md): "O" the hands pressed to the box's sides (in profile the near hand lies on its face, and the box held at the
# side read "as if it is half floating", v0.31); "U" the box carried higher on the forearms, the hands under it (the near hand at the box's corner by the body:
# "held by one hand at one corner"); "V" the near forearm under the whole box, the hand at its far corner ("as if the box rests on that hand"). v0.32: V
BOX32 = __import__("os").environ.get("TPDB_BOX", "V")


def up_carry_box(P):
    u = P.u
    pel = P.lm("pelvis")
    if BOX32 in ("U", "V"):
        if BOX32 == "U":
            C = pel + Vector((0, -0.29, 0.31)) * u
            P.arms({"R": (C + Vector((-0.11, 0.07, -0.16)) * u, (-1, 0.3, -1)), "L": (C + Vector((0.11, 0.07, -0.16)) * u, (1, 0.3, -1))})
        else:
            C = pel + Vector((0, -0.27, 0.27)) * u
            P.arms({"R": (C + Vector((-0.12, -0.06, -0.155)) * u, (-1, 0.5, -1)), "L": (C + Vector((0.12, -0.06, -0.155)) * u, (1, 0.5, -1))})
        P.prop("box", box("box", C, (0.36 * u, 0.30 * u, 0.26 * u), "khaki" if BOX45 == "A" else "wood_light"))
        P.prop("tape", box("tape", C + Vector((0, 0, 0.131)) * u, (0.36 * u, 0.06 * u, 0.004 * u), "brown" if BOX45 == "A" else "cream"))
        return
    C = pel + Vector((0, -0.27, 0.18)) * u
    P.arms({"R": (C + Vector((-0.19, 0.0, -0.03)) * u, (-1, 0.6, -0.4)), "L": (C + Vector((0.19, 0.0, -0.03)) * u, (1, 0.6, -0.4))})
    if BOX45 == "A":
        # v0.45 (TPDB_BOX45): see the switch; the tape runs over the top and down the side the viewer sees
        P.prop("box", box("box", C, (0.36 * u, 0.30 * u, 0.26 * u), "khaki"))
        P.prop("tape", box("tape", C + Vector((0, 0, 0.131)) * u, (0.364 * u, 0.07 * u, 0.004 * u), "brown"))
        for sg in (-1, 1):
            P.prop(f"tape{sg}", box(f"tape{sg}", C + Vector((sg * 0.181, 0, 0.085)) * u, (0.004 * u, 0.07 * u, 0.09 * u), "brown"))
        return
    P.prop("box", box("box", C, (0.36 * u, 0.30 * u, 0.26 * u), "wood_light"))
    P.prop("tape", box("tape", C + Vector((0, 0, 0.131)) * u, (0.36 * u, 0.06 * u, 0.004 * u), "cream"))


BAG_STYLE = __import__("os").environ.get("TPDB_BAG", "A")        # v0.25: A, chosen on the bench (isolation_v025.md); see _hang_bag
ROLLER_STYLE = __import__("os").environ.get("TPDB_ROLLER", "A")  # v0.25: A, chosen on the bench (isolation_v025.md); see up_paint


def _hang_bag(P, sd, kind):
    u = P.u
    P.arms({sd: _hang_from(P, sd), ("L" if sd == "R" else "R"): P.rest_arm("L" if sd == "R" else "R")})
    g = P.grip(sd)
    bone = f"hand_{sd}"
    if kind == "bag" and BAG_STYLE in ("A", "B"):
        # v0.25 bench (TPDB_BAG): the broad face along the walker's line, so a profile shows it (across the body, only its
        # narrow edge showed: "very long and thin for a shopping bag, could be a tag, folded paper"), with dark handles rising
        # to the hand in a V. A as tall as it is wide; B wider and shorter
        w, h = (0.25, 0.27) if BAG_STYLE == "A" else (0.33, 0.23)
        top = g - Vector((0, 0, 0.12 * u))
        P.prop("bag", box("bag", top - Vector((0, 0, h / 2 * u)), (0.10 * u, w * u, h * u), _pcol(P, "yellow", ("blue", "red", "green"))), bone)
        for y in (-0.075, 0.075):
            P.prop(f"strap{'a' if y < 0 else 'b'}", tube_mesh("strap", [top + Vector((0, y * u, 0)), g + Vector((0, y * 0.2 * u, 0.01 * u))], 0.010 * u, "charcoal"), bone)
    elif kind == "bag":
        top = g - Vector((0, 0, 0.09 * u))
        bc = _pcol(P, "yellow", ("blue", "red", "green"))
        P.prop("bag", box("bag", top - Vector((0, 0, 0.14 * u)), (0.24 * u, 0.11 * u, 0.28 * u), bc), bone)
        for x in (-0.06, 0.06):
            P.prop(f"strap{'a' if x < 0 else 'b'}", tube_mesh("strap", [top + Vector((x * u, 0, 0)), g + Vector((x * 0.3 * u, 0, 0.01 * u))], 0.008 * u, bc), bone)
    elif kind == "basket":
        top = g - Vector((0, 0, 0.14 * u))
        bowl = half_ellipsoid("basket", "wood_light")
        bowl.scale = (0.17 * u, 0.12 * u, 0.13 * u)
        bowl.location = top
        upd()
        P.prop("basket", bowl, bone)
        pts = [top + Vector((-0.16 * u, 0, 0)), top + Vector((-0.11 * u, 0, 0.10 * u)), g + Vector((0, 0, 0.012 * u)),
               top + Vector((0.11 * u, 0, 0.10 * u)), top + Vector((0.16 * u, 0, 0))]
        P.prop("handle", tube_mesh("handle", pts, 0.012 * u, "wood"), bone)
        P.prop("cloth", ellipsoid("cloth", top + Vector((0, 0, 0.01 * u)), (0.15 * u, 0.10 * u, 0.03 * u), "red"), bone)
    elif kind == "bucket":
        top = g - Vector((0, 0, 0.12 * u))
        P.prop("bucket", cyl("bucket", top - Vector((0, 0, 0.20 * u)), top, 0.085 * u, "blue", seg=24, r1=0.11 * u), bone)
        pts = [top + Vector((-0.11 * u, 0, 0)), top + Vector((-0.07 * u, 0, 0.08 * u)), g + Vector((0, 0, 0.012 * u)),
               top + Vector((0.07 * u, 0, 0.08 * u)), top + Vector((0.11 * u, 0, 0))]
        P.prop("handle", tube_mesh("handle", pts, 0.007 * u, "gray"), bone)


def up_carry_bag(P):
    _hang_bag(P, "R", "bag")


def up_carry_basket(P):
    _hang_bag(P, "R", "basket")


def up_carry_bucket(P):
    _hang_bag(P, "R", "bucket")


# v0.20: a red takeaway cup with a white lid and a straw at the lips (the white mug read as "something white held to her
# mouth, as if drinking or eating")
DRINK_V020 = True


def up_drink(P):
    """A big white mug held in front of the mouth and tipped toward it (reads as drinking, not a phone); from v0.20 a
    red takeaway cup with a white lid, its straw at the lips."""
    u = P.u
    m = P.lm("mouth")
    if DRINK_V020:
        # (round 2: a quarter bigger, the straw thicker: small at the back of a park it read as "white with a red top")
        g = 1.25
        C = m + Vector((0.0, -0.14, -0.17)) * u        # the cup's middle, below and in front of the mouth
        P.arms({"R": (C + Vector((-0.06, 0.0, -0.01)) * u, (-1, 0.4, -0.8)), "L": P.rest_arm("L")})
        P.prop("cup", cyl("cup", C + Vector((0, 0, -0.075 * g)) * u, C + Vector((0, 0, 0.065 * g)) * u, 0.040 * g * u, "red", seg=28, r1=0.052 * g * u))
        P.prop("sleeve", cyl("sleeve", C + Vector((0, 0, -0.020 * g)) * u, C + Vector((0, 0, 0.022 * g)) * u, 0.050 * g * u, "tan", seg=28, r1=0.054 * g * u))
        P.prop("lid", cyl("lid", C + Vector((0, 0, 0.062 * g)) * u, C + Vector((0, 0, 0.084 * g)) * u, 0.056 * g * u, "white", seg=28, r1=0.050 * g * u))
        top = C + Vector((0, 0, 0.084 * g)) * u
        P.prop("straw", cyl("straw", top - Vector((0, 0, 0.01)) * u, m + Vector((0.0, -0.012, -0.004)) * u, 0.011 * u, "yellow", seg=12))
        return
    C = m + Vector((0.0, -0.105, -0.045)) * u
    F = Frame.euler(C, rx=-34)
    P.arms({"R": (F.p(-0.095 * u, 0.0, -0.02 * u), (-1, 0.4, -0.8)), "L": P.rest_arm("L")})
    P.prop("mug", cyl("mug", F.p(0, 0, -0.065 * u), F.p(0, 0, 0.065 * u), 0.056 * u, "white", seg=28))
    P.prop("stripe", cyl("stripe", F.p(0, 0, -0.012 * u), F.p(0, 0, 0.022 * u), 0.0575 * u, "teal", seg=28))
    P.prop("handle", tube_mesh("handle", [F.p(-0.052 * u, 0, 0.04 * u), F.p(-0.092 * u, 0, 0.03 * u), F.p(-0.095 * u, 0, -0.03 * u),
                                          F.p(-0.052 * u, 0, -0.04 * u)], 0.012 * u, "white"))


def up_ice_cream(P):
    u = P.u
    m = P.lm("mouth")
    tgt = m + Vector((-0.03, -0.13, -0.11)) * u
    if __import__("os").environ.get("TPDB_ICE", "B") == "B":
        # v0.27, chosen on the bench: the scoop at the mouth (held up in front of the face: "looking at or eating it", "could be eating the ice cream or just holding it up")
        # (round 1's, a little higher: "smelling it like a flower", "the pink ball sits right at his nose and mouth")
        tgt = m + Vector((-0.02, -0.088, -0.128)) * u
    cone31 = __import__("os").environ.get("TPDB_CONE", "O") == "B"
    if ICE45 == "A":
        # v0.45 (TPDB_ICE45): see the switch
        k = {"child": 1.5, "teen": 1.32}.get(P.c.spec.get("age"), 1.2)
        rim, sr = 0.070 * k, 0.050 * k
        tgt = m + Vector((-0.02, -(0.050 + sr * 1.15), -(rim + sr * 0.62 + sr * 0.80 + 0.012))) * u
        if ICE49 == "B":
            # (a child's head is larger against its hand's reach: the scoop a little nearer still)
            # (round 1 of the bench, three readers of four: "pressed right against his face", "partly covers the mouth/nose": a finger
            # further off and lower, the scoop's top level with the mouth)
            gap = {"child": -0.002, "teen": 0.016}.get(P.c.spec.get("age"), 0.028)
            tgt = m + Vector((-0.012, -(gap + sr), -(rim + sr * 0.62 + sr * 0.62))) * u
        P.arms({"R": (tgt, (-1, 0.4, -0.8)), "L": P.rest_arm("L")})
        g = P.grip("R")
        P.prop("cone", cyl("cone", g + Vector((0, 0, rim)) * u, g + Vector((0, 0, -0.085)) * u, 0.043 * k * u, "wood", seg=20, r1=0.004 * u))
        P.prop("rim", cyl("rim", g + Vector((0, 0, rim)) * u, g + Vector((0, 0, rim - 0.012 * k)) * u, 0.046 * k * u, "wood_light", seg=20))
        P.prop("scoop", ellipsoid("scoop", g + Vector((0, 0, rim + sr * 0.62)) * u, (sr * u, sr * u, sr * 0.88 * u), "pink"))
        return
    if cone31:
        # v0.31 bench (isolation_v031.md), not chosen: the fist lower on a longer cone, the scoop where it was. Seated, both read as a cone; on the walker neither did: "I cannot see a clear cone or stick"
        tgt = tgt - Vector((0, 0, 0.042)) * u
    P.arms({"R": (tgt, (-1, 0.4, -0.8)), "L": P.rest_arm("L")})
    g = P.grip("R")
    if cone31:
        P.prop("cone", cyl("cone", g + Vector((0, 0, 0.095)) * u, g + Vector((0, 0, -0.055)) * u, 0.046 * u, "wood_light", r1=0.004 * u))
        P.prop("scoop", ellipsoid("scoop", g + Vector((0, 0, 0.130)) * u, (0.050 * u, 0.050 * u, 0.043 * u), "pink"))
        return
    P.prop("cone", cyl("cone", g + Vector((0, 0, 0.05)) * u, g + Vector((0, 0, -0.07)) * u, 0.040 * u, "wood_light", r1=0.004 * u))
    # (v0.44 screen: the scoop is not in TPDB_PROP44's rule. Cream against the girl in pink's dress it was "something small and white", "a sweet,
    # a dandelion clock", three half marks and ice_cream under the gate; pink, as in v0.43, read in full)
    P.prop("scoop", ellipsoid("scoop", g + Vector((0, 0, 0.085)) * u, (0.046 * u, 0.046 * u, 0.040 * u), "pink"))


def up_empty_cone(P):
    """Holding up an empty ice cream cone and looking at it: a big cone, its open top tipped toward the
    viewer so the empty inside shows (a small cone held low read as pointing)."""
    u = P.u
    m = P.lm("mouth")
    tgt = m + Vector((-0.08, -0.24, -0.10)) * u
    P.arms({"R": (tgt, (-1, 0.4, -0.8)), "L": P.rest_arm("L")})
    g = P.grip("R")
    ax = nrm((-0.40, -0.12, 1.0))
    if ICE45 == "A":
        # v0.45 (TPDB_ICE45): larger on a child, whose props shrink with the body
        u = u * {"child": 1.3, "teen": 1.15}.get(P.c.spec.get("age"), 1.0)
    top, tip = g + ax * 0.075 * u, g - ax * 0.13 * u
    P.prop("cone", cyl("cone", top, tip, 0.060 * u, "wood_light", seg=24, r1=0.006 * u))
    P.prop("hollow", cyl("hollow", top - ax * 0.002 * u, top + ax * 0.003 * u, 0.050 * u, "brown", seg=24))
    P.prop("drip", ellipsoid("drip", top + nrm((-0.2, -1, 0)) * 0.052 * u - ax * 0.02 * u, (0.012 * u, 0.012 * u, 0.022 * u), "pink"))
    P.panchor("cone_top", top)


def up_empty_cone_low(P):
    """v0.10: the empty cone held out to the side at chest height, away from the face, its open top
    tipped toward the viewer with a smear of ice cream on the rim; the other hand to the cheek (held to
    the mouth, the cone read as being eaten; held low and small, as pointing)."""
    u, A = P.u, P.A
    m = P.lm("mouth")
    P.arms({"R": (P.lm("sh_R") + nrm((-0.80, -0.38, -0.42)) * A * 0.93, (-0.4, 0.5, -1)),
            "L": (m + Vector((0.055, -0.075, 0.075)) * u, (0.4, 0.2, -1))})
    g = P.grip("R")
    ax = nrm((-0.30, -0.60, 1.0))
    if ICE45 == "A":
        # v0.45 (TPDB_ICE45): larger on a child, whose props shrink with the body
        u = u * {"child": 1.3, "teen": 1.15}.get(P.c.spec.get("age"), 1.0)
    top, tip = g + ax * 0.09 * u, g - ax * 0.18 * u
    P.prop("cone", cyl("cone", top, tip, 0.082 * u, "wood_light", seg=24, r1=0.007 * u))
    P.prop("hollow", cyl("hollow", top - ax * 0.002 * u, top + ax * 0.003 * u, 0.070 * u, "brown", seg=24))
    P.prop("drip", ellipsoid("drip", top + nrm((-0.3, -1, 0)) * 0.072 * u - ax * 0.02 * u, (0.015 * u, 0.015 * u, 0.027 * u), "pink"))
    P.panchor("cone_top", top)


def up_apple(P):
    u = P.u
    m = P.lm("mouth")
    tgt = m + Vector((-0.02, -0.10, -0.06)) * u
    P.arms({"R": (tgt, (-1, 0.4, -0.8)), "L": P.rest_arm("L")})
    g = P.grip("R")
    c = g + Vector((0, -0.01, 0.045)) * u
    P.prop("apple", ellipsoid("apple", c, (0.046 * u, 0.044 * u, 0.042 * u), "red"))
    P.prop("stem", cyl("stem", c + Vector((0, 0, 0.035)) * u, c + Vector((0.006, 0, 0.065)) * u, 0.005 * u, "brown"))
    P.prop("leaf", ellipsoid("leaf", c + Vector((0.016, 0, 0.058)) * u, (0.014 * u, 0.005 * u, 0.008 * u), "green"))


def up_read(P):
    u = P.u
    ch = P.lm("chest")
    C = ch + Vector((0, -0.27, 0.0)) * u
    # the book leans back (top away from the reader) so the pages face up toward the eyes;
    # from the front the viewer sees the cover
    F = Frame.euler(C, rx=38)
    P.arms({"R": (F.p(-0.17 * u, 0.012 * u, -0.07 * u), (-1, 0.5, -0.6)), "L": (F.p(0.17 * u, 0.012 * u, -0.07 * u), (1, 0.5, -0.6))})
    for side, sg in (("L", 1), ("R", -1)):
        q = F.q @ Quaternion((0, 0, 1), math.radians(sg * 14))
        Fp = Frame(F.p(sg * 0.085 * u, 0.0, 0.0), q)
        P.prop(f"page{side}", box(f"page{side}", Fp.o, (0.17 * u, 0.016 * u, 0.24 * u), "cream", rot=q))
        P.prop(f"cover{side}", box(f"cover{side}", Fp.p(0.003 * u * sg, -0.013 * u, 0.0), (0.178 * u, 0.010 * u, 0.25 * u), "red", rot=q))


def up_umbrella(P):
    """Umbrella held up beside the head (shaft clear of the face), eight-panel dome canopy."""
    u = P.u
    sh = P.lm("sh_R")
    tgt = sh + Vector((-0.10, -0.16, 0.02)) * u
    P.arms({"R": (tgt, (-1, 0.3, -0.8)), "L": P.rest_arm("L")})
    g = P.grip("R")
    base = g - Vector((0, 0, 0.12 * u))
    top = Vector((g.x * 0.85, g.y, P.lm("head_top").z + 0.36 * u))
    d = (top - base).normalized()
    P.prop("shaft", cyl("shaft", base, top, 0.011 * u, "charcoal"))
    P.prop("crook", tube_mesh("crook", [base, base - Vector((0, 0.025 * u, 0.05 * u)), base - Vector((0, 0.065 * u, 0.03 * u))], 0.013 * u, "charcoal"))
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=8, v_segments=10, radius=1.0)
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if v.co.z < -0.02], context="VERTS")
    can = _mesh_object("canopy", bm, "red", smooth=False)
    can.scale = (0.44 * u, 0.44 * u, 0.20 * u)
    can.location = top - d * 0.18 * u
    can.rotation_mode = "QUATERNION"
    can.rotation_quaternion = Vector((0, 0, 1)).rotation_difference(d) @ Quaternion((0, 0, 1), math.radians(22.5))
    upd()
    P.prop("canopy", can)
    P.prop("tip", cyl("tip", top + d * 0.01 * u, top + d * 0.06 * u, 0.012 * u, "charcoal"))


def up_throw(P):
    """Follow-through just after the release: throwing arm straight out ahead and up, hand open and
    empty, other arm back. The ball itself is drawn in flight by the scene, leaving from `release`."""
    u = P.u
    if THROW44 == "A":
        # v0.44 (TPDB_THROW44): the follow-through, the throwing arm swung down and across the front of the body, the palm open to the viewer,
        # the other arm swung back
        P.arms({"R": (P.lm("sh_R") + nrm((0.45, -0.72, -0.52)) * P.A * 0.97, (-1, 0.2, -0.8)),
                "L": (P.lm("sh_L") + nrm((0.20, 0.80, -0.45)) * P.A * 0.97, (0.2, -0.5, -0.4))})
        P.hand("R", "open", palm=(-1, -0.25, 0.1))
        w, d, n, t = P.hand_frame("R", (-1, -0.25, 0.1))
        P.panchor("release", w + d * 0.16 * u + n * 0.03 * u, "hand_R")
        return
    P.arms({"R": (P.lm("sh_R") + nrm((0.05, -0.85, 0.42)) * P.A * 0.99, (-1, 0.4, -0.6)),
            "L": (P.lm("sh_L") + nrm((0.25, 0.55, -0.80)) * P.A * 0.97, (0.2, -0.5, -0.4))})
    P.hand("R", "open", palm=(0, -1, -0.4))
    w, d, n, t = P.hand_frame("R", (0, -1, -0.4))
    P.panchor("release", w + d * 0.16 * u + n * 0.03 * u, "hand_R")


def _ball(P, c, r, bone="hand_R"):
    P.prop("ball", ellipsoid("ball", c, (r, r, r), "red"), bone)
    P.prop("band", ellipsoid("band", c, (r * 1.005, r * 0.32, r * 1.005), "white", rot=Quaternion((0, 0, 1), 0.4)), bone)


def up_hold_ball(P):
    u = P.u
    ch = P.lm("chest")
    C = ch + Vector((0, -0.25, -0.04)) * u
    r = 0.11 * u
    P.arms({"R": (C + Vector((-0.11, 0.0, -0.01)) * u, (-1, 0.5, -0.6)), "L": (C + Vector((0.11, 0.0, -0.01)) * u, (1, 0.5, -0.6))})
    _ball(P, C, r)


def up_kite(P):
    u = P.u
    P.arms({"R": (P.lm("sh_R") + nrm((-0.18, -0.55, 0.80)) * P.A * 0.95, (-0.6, 0.5, -0.4)), "L": P.rest_arm("L")})
    g = P.grip("R")
    if KITE45 == "A":
        # v0.45 (TPDB_KITE45): see the switch; the reel's axis along the forearm's line, up and forward, so it shows from the side at every angle
        ax = nrm((-0.05, -0.45, 1.0))
        k = u * {"child": 1.25, "teen": 1.1}.get(P.c.spec.get("age"), 1.0)
        col = _pcol(P, "red", ("blue", "orange", "purple"))
        P.prop("handle", cyl("handle", g - ax * 0.055 * k, g + ax * 0.060 * k, 0.014 * k, "brown"))
        P.prop("spool", cyl("spool", g + ax * 0.062 * k, g + ax * 0.150 * k, 0.034 * k, "cream", seg=20))
        for nm_, a0 in (("flange0", 0.052), ("flange1", 0.146)):
            P.prop(nm_, cyl(nm_, g + ax * a0 * k, g + ax * (a0 + 0.016) * k, 0.060 * k, col, seg=24))
        P.panchor("string_end", g + ax * 0.106 * k + Vector((0, -0.034, 0)) * k)
        return
    P.prop("spool", cyl("spool", g + Vector((-0.04, 0, 0)) * u, g + Vector((0.04, 0, 0)) * u, 0.030 * u, "wood_light"))
    P.panchor("string_end", g + Vector((0, -0.01, 0.02)) * u)


def up_balloon(P):
    """Holding a balloon out in front: the string rises clear of the face in side and three-quarter
    views (held in front of the chest, it ran straight down over the face)."""
    u = P.u
    ch = P.lm("chest")
    P.arms({"R": (ch + Vector((-0.05, -0.32, 0.10)) * u, (-1, 0.4, -0.7)), "L": P.rest_arm("L")})
    g = P.grip("R")
    b = Vector((g.x, g.y - 0.07 * u, P.lm("head_top").z + 0.40 * u))
    P.prop("string", tube_mesh("string", [g, g.lerp(b, 0.5) + Vector((0.03 * u, 0, 0)), b - Vector((0, 0, 0.17 * u))], 0.0045 * u, "outline"))
    bc = _pcol(P, "yellow", ("red", "blue"))      # v0.44 (TPDB_PROP44)
    P.prop("balloon", ellipsoid("balloon", b, (0.135 * u, 0.13 * u, 0.165 * u), bc))
    P.prop("knot", cyl("knot", b - Vector((0, 0, 0.18 * u)), b - Vector((0, 0, 0.155 * u)), 0.006 * u, bc, r1=0.018 * u))


def up_paint(P):
    u = P.u
    sh = P.lm("sh_R")
    head = Vector((-0.02 * u, -0.48 * u, sh.z + 0.18 * u))
    T = Vector((-0.04 * u, -0.10 * u, P.lm("pelvis").z + 0.12 * u))
    _pole_grips(P, T, head, 0.42, 0.10, hintL=(1, 0.3, -0.6), hintR=(-1, 0.3, -0.6))
    d = (head - T).normalized()
    P.prop("pole", cyl("pole", T - d * 0.05 * u, head - d * 0.04 * u, 0.014 * u, "wood"))
    if ROLLER_STYLE in ("A", "B"):
        # v0.25 bench (TPDB_ROLLER): the roller upright, its side to the viewer, a T on the end of the pole (its axis along the
        # line of sight left only its round end in view: "a small pale oval", "hardly seems to touch the fence"). B longer and fatter
        hl, rr = (0.15, 0.052) if ROLLER_STYLE == "A" else (0.19, 0.065)
        c = head + Vector((0, -0.05 * u, 0))
        if PAINT45 == "A":
            # v0.45 (TPDB_PAINT45): see the switch
            hl, rr = 0.125, 0.058
            e0 = head - d * 0.04 * u
            by = max(e0.y, c.y + (rr + 0.035) * u)
            zt = c.z + (hl + 0.05) * u
            P.prop("frame", tube_mesh("frame", [e0, Vector((e0.x, by, e0.z + 0.02 * u)), Vector((e0.x, by, zt)), Vector((c.x, c.y, zt)),
                                                Vector((c.x, c.y, c.z + hl * u))], 0.010 * u, "gray"))
            P.prop("roller", cyl("roller", c + Vector((0, 0, -hl * u)), c + Vector((0, 0, hl * u)), rr * u, "blue", seg=24))
            for nm_, sg in (("cap0", -1), ("cap1", 1)):
                P.prop(nm_, cyl(nm_, c + Vector((0, 0, sg * hl * u)), c + Vector((0, 0, sg * (hl + 0.016) * u)), rr * 0.80 * u, "cream", seg=24))
            P.panchor("roller", c + Vector((0, -rr * u, 0)))
            return
        P.prop("frame", cyl("frame", head - d * 0.04 * u, c, 0.012 * u, "gray"))
        P.prop("roller", cyl("roller", c + Vector((0, 0, -hl * u)), c + Vector((0, 0, hl * u)), rr * u, "blue"))
        P.panchor("roller", c + Vector((0, -rr * u, 0)))
        return
    P.prop("frame", cyl("frame", head - Vector((0.13 * u, 0, 0)) - d * 0.04 * u, head - d * 0.04 * u, 0.008 * u, "gray"))
    P.prop("roller", cyl("roller", head + Vector((-0.12 * u, -0.03 * u, 0)), head + Vector((0.12 * u, -0.03 * u, 0)), 0.042 * u, "blue"))
    P.panchor("roller", head + Vector((0, -0.06 * u, 0)))


def up_photo(P):
    u = P.u
    eyes = (P.lm("eye_L") + P.lm("eye_R")) / 2
    if CAM45 in ("A", "B"):
        # v0.45 (TPDB_CAM45): see the switch
        k = 1.22
        C = eyes + Vector((0, -0.062 - 0.040 * k, -0.020)) * u
        P.arms({"R": (C + Vector((-0.092 * k, 0.012, -0.030)) * u, (-1, 0.4, -0.7)), "L": (C + Vector((0.092 * k, 0.012, -0.030)) * u, (1, 0.4, -0.7))})
        ku = k * u
        P.prop("camera", box("camera", C - Vector((0, 0, 0.012 * ku)), (0.17 * ku, 0.066 * ku, 0.078 * ku), "charcoal"))
        P.prop("camtop", box("camtop", C + Vector((0, 0, 0.040 * ku)), (0.172 * ku, 0.068 * ku, 0.030 * ku), "silver"))
        P.prop("prism", box("prism", C + Vector((0, 0, 0.066 * ku)), (0.060 * ku, 0.060 * ku, 0.030 * ku), "silver"))
        P.prop("shutter", cyl("shutter", C + Vector((-0.060, 0, 0.054)) * ku, C + Vector((-0.060, 0, 0.068)) * ku, 0.013 * ku, "red", seg=14))
        P.prop("lens", cyl("lens", C - Vector((0, 0.030, 0.006)) * ku, C - Vector((0, 0.120, 0.006)) * ku, 0.047 * ku, "charcoal", seg=24))
        P.prop("lensring", cyl("lensring", C - Vector((0, 0.112, 0.006)) * ku, C - Vector((0, 0.126, 0.006)) * ku, 0.052 * ku, "silver", seg=24))
        P.prop("glass", cyl("glass", C - Vector((0, 0.122, 0.006)) * ku, C - Vector((0, 0.129, 0.006)) * ku, 0.034 * ku, "navy", seg=24))
        P.prop("glint", ellipsoid("glint", C - Vector((-0.012, 0.130, -0.008)) * ku, (0.009 * ku, 0.003 * ku, 0.009 * ku), "white"))
        P.prop("flash", box("flash", C + Vector((0.058, -0.004, 0.066)) * ku, (0.046 * ku, 0.040 * ku, 0.030 * ku), "silver"))
        P.prop("flashwin", box("flashwin", C + Vector((0.058, -0.026, 0.066)) * ku, (0.036 * ku, 0.004 * ku, 0.020 * ku), "white"))
        P.panchor("flash", C + Vector((0.058, -0.030, 0.066)) * ku)
        sc_ = _pcol(P, "red", ("yellow", "teal", "blue"))
        e0, e1 = C + Vector((-0.085, 0.0, 0.020)) * ku, C + Vector((0.085, 0.0, 0.020)) * ku
        lo = C + Vector((0, 0.010, -0.26)) * ku
        P.prop("strap", tube_mesh("strap", [e0, e0 + Vector((-0.012, 0.004, -0.10)) * ku, lo + Vector((-0.045, 0, 0.02)) * ku, lo,
                                            lo + Vector((0.045, 0, 0.02)) * ku, e1 + Vector((0.012, 0.004, -0.10)) * ku, e1], 0.0075 * ku, sc_))
        return
    C = eyes + Vector((0, -0.10, -0.015)) * u
    P.arms({"R": (C + Vector((-0.085, 0.015, -0.02)) * u, (-1, 0.4, -0.7)), "L": (C + Vector((0.085, 0.015, -0.02)) * u, (1, 0.4, -0.7))})
    # v0.17: a two-tone camera, a silver top over a black body, with one big lens ringed in silver and a flash on top (a
    # small dark box with a grey lens at the face read as "binoculars or a camera")
    P.prop("camera", box("camera", C - Vector((0, 0, 0.012 * u)), (0.17 * u, 0.066 * u, 0.078 * u), "charcoal"))
    P.prop("camtop", box("camtop", C + Vector((0, 0, 0.040 * u)), (0.172 * u, 0.068 * u, 0.034 * u), "silver"))
    P.prop("lens", cyl("lens", C - Vector((0, 0.030 * u, 0.004 * u)), C - Vector((0, 0.098 * u, 0.004 * u)), 0.044 * u, "charcoal", seg=24))
    P.prop("lensring", cyl("lensring", C - Vector((0, 0.094 * u, 0.004 * u)), C - Vector((0, 0.104 * u, 0.004 * u)), 0.047 * u, "silver", seg=24))
    P.prop("glass", cyl("glass", C - Vector((0, 0.100 * u, 0.004 * u)), C - Vector((0, 0.107 * u, 0.004 * u)), 0.030 * u, "navy", seg=24))
    P.prop("glint", ellipsoid("glint", C - Vector((-0.010, 0.108, -0.010)) * u, (0.008 * u, 0.003 * u, 0.008 * u), "white"))
    P.prop("flash", box("flash", C + Vector((-0.050, 0.0, 0.070)) * u, (0.050 * u, 0.044 * u, 0.030 * u), "silver"))
    P.prop("flashwin", box("flashwin", C + Vector((-0.050, -0.023, 0.070)) * u, (0.040 * u, 0.004 * u, 0.020 * u), "white"))


def up_flowers(P):
    u = P.u
    ch = P.lm("chest")
    P.arms({"R": (ch + Vector((-0.08, -0.44, -0.04)) * u, (-1, 0.2, -0.8)), "L": P.rest_arm("L")})
    g = P.grip("R")
    # a bouquet: green stems fanning out of a short paper wrap, separate blooms with leaves, so it
    # cannot read as an ice cream cone
    P.prop("wrap", cyl("wrap", g - Vector((0, 0, 0.06 * u)), g + Vector((0, 0, 0.07 * u)), 0.016 * u, "pink", r1=0.045 * u))
    # blooms on a dome, spread in both horizontal directions so the bunch fans out from every angle
    blooms = ((-0.075, 0.035, 0.22, "red"), (0.075, -0.035, 0.23, "yellow"), (0.0, 0.0, 0.29, "purple"), (0.035, 0.075, 0.18, "orange"),
              (-0.035, -0.075, 0.18, "white"), (0.08, 0.06, 0.15, "pink"), (-0.08, -0.06, 0.15, "red"))
    for i, (dx, dy, dz, col) in enumerate(blooms):
        c = g + Vector((dx, dy, dz)) * u
        P.prop(f"stem{i}", cyl(f"stem{i}", g + Vector((0, 0, 0.03 * u)), c, 0.0065 * u, "green"))
        P.prop(f"bloom{i}", ellipsoid(f"bloom{i}", c, (0.036 * u, 0.020 * u, 0.034 * u), col))
        P.prop(f"eye{i}", ellipsoid(f"eye{i}", c + Vector((0, -0.016, 0)) * u, (0.012 * u, 0.008 * u, 0.012 * u), "sun" if col != "yellow" else "orange"))
    for i, (dx, dz, a) in enumerate(((-0.05, 0.11, 0.7), (0.05, 0.12, -0.7))):
        P.prop(f"leaf{i}", ellipsoid(f"leaf{i}", g + Vector((dx, -0.004, dz)) * u, (0.016 * u, 0.008 * u, 0.040 * u), "green",
                                      rot=Quaternion((0, 1, 0), a)))


# v0.26 bench (TPDB_FEED): what the feeder holds, in six v0.25 pictures "a paper bag, a cup or a carton". O the cream bag with a
# rolled top. A a slice of bread, its broad face along the feeder's line so that a profile shows it. B a brown paper bag. v0.26: B, on
# the bench (isolation_v026.md: "a brown paper bag"; A was "a paper bag or packet", "a couple of sheets of paper").
FEED_STYLE = __import__("os").environ.get("TPDB_FEED", "B")


def _feed_prop(P, gL):
    u = P.u
    if FEED_STYLE == "A":
        # held by its lower edge, most of it above the fingers
        c = gL + Vector((0, -0.01 * u, 0.09 * u))
        P.prop("seedbag", box("seedbag", c, (0.05 * u, 0.25 * u, 0.25 * u), "tan", bevel=0.025 * u), "hand_L")
        P.prop("seedtop", box("seedtop", c, (0.075 * u, 0.205 * u, 0.205 * u), "cream", bevel=0.018 * u), "hand_L")
        return
    if FEED_STYLE == "B":
        P.prop("seedbag", box("seedbag", gL - Vector((0, 0, 0.09 * u)), (0.12 * u, 0.17 * u, 0.22 * u), "wood_light", bevel=0.008 * u), "hand_L")
        P.prop("seedtop", box("seedtop", gL + Vector((0, 0, 0.03 * u)), (0.125 * u, 0.175 * u, 0.035 * u), "wood", bevel=0.006 * u), "hand_L")
        return
    # a big paper bag of seed with a rolled top (a small box read as a brush or a sanding block)
    P.prop("seedbag", box("seedbag", gL - Vector((0, 0, 0.07 * u)), (0.15 * u, 0.10 * u, 0.20 * u), "cream", bevel=0.01 * u), "hand_L")
    P.prop("seedtop", box("seedtop", gL + Vector((0, 0, 0.035 * u)), (0.155 * u, 0.105 * u, 0.03 * u), "tan", bevel=0.008 * u), "hand_L")


def up_feed_birds(P):
    u = P.u
    pel = P.lm("pelvis")
    P.arms({"R": (pel + Vector((-0.14, -0.40, 0.14)) * u, (-1, 0.4, -0.6)), "L": (pel + Vector((0.10, -0.22, 0.14)) * u, (1, 0.4, -0.6))})
    gL = P.grip("L")
    _feed_prop(P, gL)
    P.panchor("seed_from", P.grip("R") - Vector((0, 0, 0.02 * u)))


def up_feed_birds_low(P):
    """v0.7: the seed hand held low and out toward the ground in front, the bag hand at the waist (with
    the hand at chest height and the head level, the feeder seemed to face whatever was behind the birds)."""
    u = P.u
    pel = P.lm("pelvis")
    P.arms({"R": (pel + Vector((-0.12, -0.34, 0.02)) * u, (-1, 0.4, -0.3)), "L": (pel + Vector((0.10, -0.20, 0.10)) * u, (1, 0.4, -0.6))})
    gL = P.grip("L")
    _feed_prop(P, gL)
    P.hand("R", "open", palm=(0, 0, -1))
    P.panchor("seed_from", P.grip("R") - Vector((0, 0, 0.03 * u)))


def up_balloon_reach(P):
    """v0.9: one hand holds the strings of a small bunch of balloons out in front (the balloons are
    drawn by the scene), the other arm reaches high for the one that got away."""
    A, u = P.A, P.u
    ch = P.lm("chest")
    # the holding arm out to the side and a little back, so the bunch rises behind the child and its
    # strings stay clear of the face and of the reaching arm
    P.arms({"R": (P.lm("sh_R") + nrm((-0.62, 0.30, -0.30)) * A * 0.96, (-0.3, 0.6, -0.8)),
            "L": (P.lm("sh_L") + nrm((0.16, -0.40, 0.90)) * A * 0.995, (1, 0.5, -0.2))})
    P.hand("L", "open", palm=(0, -1, 0.2))
    P.panchor("strings_at", P.grip("R") + Vector((0, -0.01, 0.02)) * u)


def up_read_open(P, rz=55.0, k=1.25):
    """v0.9: a bigger book held open and turned toward the near side, so the pages show in side view
    (edge-on in profile, the small red book read as a phone)."""
    u = P.u
    ch = P.lm("chest")
    C = ch + Vector((0, -0.30, -0.05)) * u
    F = Frame.euler(C, rx=48, rz=rz)
    w, h = 0.17 * k, 0.24 * k
    if __import__("os").environ.get("TPDB_BOOK", "B") == "B":
        # v0.27, chosen on the bench: the near hand under the book's outer corner, its forearm below the page and not across it ("the hand sticks out past its right edge as a small
        # rounded lump", "the forearm passes straight across the front of the book": four of four cut-outs); the far hand behind the far page
        P.arms({"R": (F.p(-(w * 0.86) * u, 0.028 * u, -(h / 2 + 0.018) * u), (-1, 0.5, -0.9)), "L": (F.p((w * 0.80) * u, 0.030 * u, -(h / 2 - 0.05) * u), (1, 0.5, -0.6))})
    else:
        P.arms({"R": (F.p(-(w + 0.005) * u, 0.012 * u, -0.07 * u), (-1, 0.5, -0.6)), "L": (F.p((w + 0.005) * u, 0.012 * u, -0.07 * u), (1, 0.5, -0.6))})
    for side, sg in (("L", 1), ("R", -1)):
        q = F.q @ Quaternion((0, 0, 1), math.radians(sg * 12))
        Fp = Frame(F.p(sg * (w / 2) * u, 0.0, 0.0), q)
        P.prop(f"page{side}", box(f"page{side}", Fp.o, (w * u, 0.016 * u, h * u), "cream", rot=q))
        P.prop(f"cover{side}", box(f"cover{side}", Fp.p(0.003 * u * sg, -0.013 * u, 0.0), ((w + 0.008) * u, 0.010 * u, (h + 0.01) * u), "red", rot=q))
        # three dark text bands on each page, so it reads as a book's open pages
        for i in range(3):
            P.prop(f"text{side}{i}", box(f"text{side}{i}", Fp.p(0.0, -0.009 * u * -1 + 0.0, (0.07 - i * 0.065) * k * u), (w * 0.72 * u, 0.004 * u, 0.012 * u), "charcoal", rot=q))


def up_grip_handle(P):
    """Both hands gripping a handle just in front of the chest, holding on tight."""
    u = P.u
    c = P.lm("chest")
    P.arms({"R": (c + Vector((-0.07, -0.20, -0.02)) * u, (-1, 0.3, -0.7)), "L": (c + Vector((0.07, -0.20, -0.02)) * u, (1, 0.3, -0.7))})
    P.panchor("handle", (P.grip("L") + P.grip("R")) / 2)


def up_grip_call(P):
    """v0.44 (TPDB_CALL44): stuck up on the seesaw and calling: the near hand on the handle in front of the chest, the far hand cupped just in front
    of the open mouth, clear of the face (both hands at the chest read as nervous or praying)."""
    u = P.u
    c = P.lm("chest")
    m = P.lm("mouth")
    P.arms({"R": (c + Vector((-0.07, -0.20, -0.02)) * u, (-1, 0.3, -0.7)), "L": (m + Vector((0.05, -0.11, -0.03)) * u, (1, 0.3, -0.7))})
    P.hand("L", "open", palm=(-0.6, -0.3, 0))
    P.panchor("handle", P.grip("R"))


def up_grip_reach(P):
    """v0.14: the far hand gripping the handle in front of the chest, the near arm reaching out and up toward the
    other end, the hand open: holding on and calling to the one below."""
    u = P.u
    c = P.lm("chest")
    P.arms({"R": (P.lm("sh_R") + nrm((-0.12, -0.78, 0.62)) * P.A * 0.98, (-1, 0.3, -0.5)), "L": (c + Vector((0.07, -0.20, -0.02)) * u, (1, 0.3, -0.7))})
    P.hand("R", "open", palm=(0, -1, 0.3))
    P.panchor("handle", P.grip("L"))


def up_walk_dog(P):
    u = P.u
    pel = P.lm("pelvis")
    P.arms({"R": (pel + Vector((-0.17, -0.26, 0.04)) * u, (-1, 0.5, -0.4)),
            "L": (P.lm("sh_L") + nrm((0.08, -0.40, -1)) * P.A * 0.95, (0.2, 0.5, 0))})
    g = P.grip("R")
    P.prop("loop", tube_mesh("loop", [g + Vector((0, 0.015, 0.03)) * u, g + Vector((0, -0.02, 0.0)) * u, g + Vector((0, 0.015, -0.03)) * u], 0.009 * u, "red"))
    P.panchor("leash_end", g + Vector((0, -0.02, -0.02)) * u)


def up_fish(P):
    u = P.u
    pel = P.lm("pelvis")
    gR = pel + Vector((-0.06, -0.22, 0.16)) * u
    gL = pel + Vector((0.02, -0.33, 0.24)) * u
    P.arms({"R": (gR, (-1, 0.5, -0.6)), "L": (gL, (1, 0.4, -0.6))})
    gR, gL = P.grip("R"), P.grip("L")
    d = (gL - gR).normalized()
    butt = gR - d * 0.14 * u
    tip = gR + d * 1.55 * u
    P.prop("rod", cyl("rod", butt, tip, 0.016 * u, "charcoal", r1=0.005 * u))
    P.prop("reel", cyl("reel", gR + d * 0.06 * u + Vector((0, 0, -0.03 * u)), gR + d * 0.06 * u + Vector((0, 0, -0.07 * u)), 0.03 * u, "gray"))
    P.panchor("rod_tip", tip)


# v0.20: a metal pail pulled down over the top of the head to the brows, with a rolled rim, two ridges and its wire
# handle hanging from the lugs at the rim (the blue bucket sitting on top read as "a tall blue hat ... or a fez")
BUCKET_V020 = "back"        # where the handle hangs: "back" of the head or "front" under the chin; None = v0.19


def up_bucket_hat(P):
    up_hands_on_hips(P)
    u, c = P.u, P.c
    ht = P.lm("head_top")
    hc = ht - Vector((0, 0, c.HR[2] + 0.02 * c.kh))
    if not BUCKET_V020:
        rim_z = hc.z + 0.085 * c.kh
        R = c.HR[0] * 1.10
        P.prop("bucket", cyl("bucket", Vector((hc.x, hc.y, rim_z)), Vector((hc.x, hc.y, rim_z + 0.24 * c.kh)), R, "blue", seg=28, r1=R * 0.78), "head")
        pts = [Vector((hc.x - R, hc.y, rim_z + 0.01 * c.kh)), Vector((hc.x - R * 1.04, hc.y - 0.03 * c.kh, rim_z - 0.06 * c.kh)),
               Vector((hc.x - R * 0.95, hc.y - 0.06 * c.kh, rim_z - 0.10 * c.kh))]
        P.prop("handle", tube_mesh("handle", pts, 0.008 * c.kh, "gray"), "head")
        return
    k = c.kh
    # (a cap or sun hat under the pail is hidden: the old man's cap brim stuck out from under it)
    hat = [n for n in ("HatDome", "HatBrim", "HatButton", "HatBand", "HatPom") if n in bpy.data.objects]
    if hat:
        P.hides.setdefault(P.cur, []).extend(hat)
    rim_z = hc.z + 0.050 * k
    if __import__("os").environ.get("TPDB_BUCKET36", "R") == "R":
        # v0.36: chosen on the bench with the moustache (vision/isolation_v036.md; TPDB_BUCKET36=O builds v0.35's). Sat higher on the head, so the hair at the temples shows below the rim (the grandfather's white hair was hidden,
        # and he was "a boy")
        rim_z = hc.z + 0.085 * k
    R = c.HR[0] * 1.20
    H = 0.27 * k
    top_r = R * 0.72        # (round 2: a stronger taper, one ridge and no lugs: with straight sides, two ridges and
    #                          side lugs it read as "a cooking pot" or "a stack of metal bowls")
    P.prop("bucket", cyl("bucket", Vector((hc.x, hc.y, rim_z)), Vector((hc.x, hc.y, rim_z + H)), R, "silver", seg=32, r1=top_r), "head")
    P.prop("rim", cyl("rim", Vector((hc.x, hc.y, rim_z - 0.012 * k)), Vector((hc.x, hc.y, rim_z + 0.016 * k)), R * 1.07, "gray", seg=32), "head")
    t = 0.30
    r_ = R + (top_r - R) * t
    z_ = rim_z + H * t
    P.prop("ridge", cyl("ridge", Vector((hc.x, hc.y, z_ - 0.007 * k)), Vector((hc.x, hc.y, z_ + 0.007 * k)), r_ * 1.025, "gray", seg=32), "head")
    lug_z = rim_z + 0.035 * k
    dy = 0.13 * k if BUCKET_V020 == "back" else -0.10 * k
    drop = 0.13 * k if BUCKET_V020 == "back" else 0.20 * k
    pts = [Vector((hc.x - R * 1.02, hc.y, lug_z)), Vector((hc.x - R * 0.85, hc.y + dy * 0.55, lug_z - drop * 0.6)),
           Vector((hc.x, hc.y + dy, lug_z - drop)), Vector((hc.x + R * 0.85, hc.y + dy * 0.55, lug_z - drop * 0.6)),
           Vector((hc.x + R * 1.02, hc.y, lug_z))]
    P.prop("handle", tube_mesh("handle", pts, 0.0085 * k, "charcoal"), "head")


def up_trowel(P):
    u = P.u
    pel = P.lm("pelvis")
    if TROWEL45 == "A":
        # v0.45 (TPDB_TROWEL45): see the switch
        P.arms({"R": (Vector((-0.10 * u, -0.40 * u, 0.31 * u)), (-0.8, 0.4, -0.5)), "L": (Vector((0.10 * u, -0.34 * u, 0.35 * u)), (0.8, 0.4, -0.5))})
        g = P.grip("R")
        ax = nrm((0, -0.38, -1.0))
        P.prop("handle", cyl("handle", g - ax * 0.050 * u, g + ax * 0.045 * u, 0.019 * u, _pcol(P, "red", ("orange", "yellow", "blue"))))
        P.prop("neck", cyl("neck", g + ax * 0.040 * u, g + ax * 0.090 * u, 0.009 * u, "gray"))
        P.prop("blade", cyl("blade", g + ax * 0.082 * u, g + ax * 0.246 * u, 0.056 * u, "silver", seg=20, r1=0.007 * u))
        P.panchor("trowel_tip", g + ax * 0.246 * u)
        return
    P.arms({"R": (Vector((-0.10 * u, -0.36 * u, 0.36 * u)), (-0.8, 0.4, -0.5)), "L": (Vector((0.10 * u, -0.34 * u, 0.35 * u)), (0.8, 0.4, -0.5))})
    g = P.grip("R")
    P.prop("handle", cyl("handle", g + Vector((0, 0, 0.04)) * u, g - Vector((0, 0, 0.03)) * u, 0.016 * u, "wood"))
    P.prop("blade", box("blade", g - Vector((0, 0.01, 0.09)) * u, (0.06 * u, 0.012 * u, 0.10 * u), "gray"))
    P.panchor("trowel_tip", g - Vector((0, 0.01, 0.14)) * u)


UPPER = {
    "walk_swing": up_walk_swing, "run_swing": up_run_swing, "wave": up_wave, "point": up_point, "point_up": up_point_up, "feel_rain": up_feel_rain,
    "reach_up": up_reach_up, "hang_up": up_hang_up, "cheer": up_cheer, "slide_up": up_slide_up, "slide_hold": up_slide_hold,
    "hands_on_hips": up_hands_on_hips, "shrug": up_shrug,
    "hands_to_face": up_hands_to_face, "hold_front": up_hold_front, "clap": up_clap, "call_out": up_call_out,
    "think": up_think, "cross_arms": up_cross_arms, "catch": up_catch, "push": up_push, "balance": up_balance,
    "ground_support": up_ground_support, "lie_rest": up_lie_rest, "swing_hold": up_swing_hold,
    "crouch_hands": up_crouch_hands, "crouch_reach": up_crouch_reach, "sit_rest": up_sit_rest,
    "water_can": up_water_can, "water_pan": up_water_pan, "hose_spray": up_hose_spray, "hose_inspect": up_hose_inspect,
    "sweep": up_sweep, "sweep_fork": up_sweep_fork, "rake": up_rake, "dig": up_dig, "dig_lift": up_dig_lift, "kick_swing": up_kick_swing, "carry_box": up_carry_box,
    "carry_bag": up_carry_bag, "carry_basket": up_carry_basket, "carry_bucket": up_carry_bucket, "drink": up_drink,
    "ice_cream": up_ice_cream, "apple": up_apple, "read": up_read, "umbrella": up_umbrella, "throw": up_throw,
    "hold_ball": up_hold_ball, "kite": up_kite, "balloon": up_balloon, "paint": up_paint, "photo": up_photo,
    "flowers": up_flowers, "feed_birds": up_feed_birds, "walk_dog": up_walk_dog, "fish": up_fish,
    "bucket_hat": up_bucket_hat, "trowel": up_trowel, "empty_cone": up_empty_cone, "empty_cone_low": up_empty_cone_low,
    "sweep_dinner_fork": up_sweep_dinner_fork, "sweep_giant_fork": up_sweep_giant_fork, "spade_pat": up_spade_pat, "feed_birds_low": up_feed_birds_low, "grip_handle": up_grip_handle, "grip_call": up_grip_call, "grip_reach": up_grip_reach, "balloon_reach": up_balloon_reach, "read_open": up_read_open,
}

# v0.18: the reading walker's head bent 20 degrees, not 30 (bent further, the dark-haired woman's face was hidden: "no
# visible face", "only a skin-coloured profile edge under dark hair")
WALK_READ_PITCH = -20
# v0.19: everyone else back at 30 degrees, as in v0.17, when every reading walker read as reading in six pictures (at 20
# the windy park's reader held "an open newspaper", "papers in the wind"); the bob keeps 20 for its face
WALK_READ_PITCH_OTHERS = -30

# name: (lower, lower_args, upper, description, tags)
#   description = how a healthy speaker would say it ("<who> is ...")
ACTIONS = [
    ("stand", "stand", {}, None, "standing", ["idle"]),
    ("walk", "walk", {}, "walk_swing", "walking", ["move"]),
    # (v0.44, TPDB_RUN44 "A": both feet off the ground, so the variant is airborne: the validator's ground rule does not apply, and its shadow is the
    # jumper's, a little lighter)
    ("run", "run", {}, "run_swing", "running", ["move", "airborne"] if RUN44 == "A" else ["move"]),
    ("kick_low", "kick_low", {}, "kick_swing", "kicking a ball along the ground", ["ball"]),
    ("wave", "stand", {"head_roll": -6, "side": -3}, "wave", "waving", ["social"]),
    ("point", "stand", {}, "point", "pointing", ["social", "look"]),
    ("point_up", "stand", {"head_pitch": 26}, "point_up", "pointing up at something", ["social", "look_up"]),
    ("reach_up", "stand", {"head_pitch": 16, "lean": -3}, "reach_up", "reaching up", ["reach"]),
    ("hang_washing", "stand", {"head_pitch": 18, "lean": -2}, "hang_up", "hanging up washing", ["reach", "chore"]),
    ("hands_on_hips", "wide", {"lean": -3}, "hands_on_hips", "standing with hands on hips", ["emotion"]),
    ("shrug", "stand", {"head_roll": 10, "head_pitch": 4}, "shrug", "shrugging", ["emotion"]),
    ("hands_to_face", "stand", {"head_pitch": -4, "lean": -4}, "hands_to_face", "holding their face", ["emotion"]),
    ("hold_front", "stand", {"head_pitch": -8}, "hold_front", "holding something", ["hold"]),
    ("clap", "stand", {"head_pitch": 4}, "clap", "clapping", ["emotion", "social"]),
    ("call_out", "stand", {"head_pitch": 4}, "call_out", "calling out to someone", ["social"]),
    ("think", "stand", {"head_pitch": 6, "head_roll": 6}, "think", "thinking", ["emotion"]),
    ("cross_arms", "wide", {}, "cross_arms", "standing with arms crossed", ["emotion"]),
    ("catch", "stand", {"head_pitch": 12}, "catch", "getting ready to catch", ["ball", "look_up"]),
    ("push", "walk", {"lean": 14}, "push", "pushing something", ["push"]),
    # (v0.47, TPDB_HEAD47 "B": 128 degrees, the back of the head from every side; at 95 the walker coming toward the viewer showed a face in
    # pure profile, which the new head draws with no eye)
    ("look_back", "walk", {"head_turn": 128 if HEAD47 == "B" else 95}, "walk_swing", "looking back over a shoulder", ["look"]),
    ("sit", "sit", {}, "sit_rest", "sitting", ["sit"]),
    ("sit_swing", "sit_swing", {}, "swing_hold", "sitting on a swing", ["sit", "swing"]),
    ("sit_ground", "sit_ground", {}, "ground_support", "sitting on the ground", ["sit", "ground"]),
    ("lie_down", "lie", {}, "lie_rest", "lying down", ["rest", "ground"]),
    ("crouch_reach", "crouch", {"head_pitch": 15}, "crouch_reach", "crouching and reaching out", ["low", "reach"]),
    ("kneel_plant", "kneel", {}, "trowel", "planting flowers", ["garden", "low"]),
    ("water_plants", "stand", {"lean": 6, "head_pitch": -22}, "water_can", "watering the plants", ["garden", "water"]),
    ("water_pan", "stand", {"lean": 6, "head_pitch": -22}, "water_pan", "watering the plants with a frying pan", ["garden", "water", "misuse"]),
    ("hose_spray", "stand", {"lean": 4, "head_pitch": -14}, "hose_spray", "spraying the hose", ["garden", "water", "hose"]),
    # (v0.44, TPDB_INSPECT44 "A": the head level and turned toward the viewer, so the puzzled brows and mouth show)
    # (v0.45, TPDB_HOSE45 "A": that turn was away from the viewer; toward the viewer now, as a profile pose's head)
    ("hose_inspect", "stand", {"head_pitch": -6, "head_turn": PROFILE47 if HEAD47 == "B" else -28, "lean": 4} if HOSE45 == "A" else
     {"head_pitch": 2, "head_turn": 20, "lean": 4} if INSPECT44 == "A" else {"head_pitch": -20, "lean": 4}, "hose_inspect",
     "looking into the hose nozzle", ["garden", "hose", "look"]),
    ("sweep", "stand", {"lean": 10, "head_pitch": -18}, "sweep", "sweeping", ["chore"]),
    ("rake", "stand", {"lean": 14, "head_pitch": -20}, "rake", "raking leaves", ["chore", "garden"]),
    ("dig_lift", "dig_lunge", {}, "dig_lift", "digging, lifting a spadeful of earth", ["chore", "garden"]),
    ("carry_box", "stand", {"lean": -4}, "carry_box", "carrying a box", ["carry"]),
    ("carry_bag", "stand", {}, "carry_bag", "carrying a shopping bag", ["carry", "shop"]),
    ("carry_basket", "stand", {}, "carry_basket", "carrying a basket", ["carry", "picnic"]),
    ("carry_bucket", "stand", {}, "carry_bucket", "carrying a bucket", ["carry"]),
    ("drink", "stand", {"head_pitch": 16, "lean": -3}, "drink", "drinking from a cup through a straw", ["food"]),
    ("eat_ice_cream", "stand", {"head_pitch": ICE49_PITCH}, "ice_cream", "eating an ice cream cone", ["food"]),
    ("eat_apple", "stand", {}, "apple", "eating an apple", ["food"]),
    ("look_up", "stand", {"head_pitch": 30, "lean": -4}, None, "looking up", ["look_up"]),
    ("read", "stand", {"head_pitch": -28}, "read", "reading a book", ["read"]),
    ("umbrella", "stand", {}, "umbrella", "holding an umbrella", ["rain"]),
    ("throw_ball", "walk", {"lean": 8, "head_pitch": 8}, "throw", "throwing a ball", ["ball"]),
    ("hold_ball", "stand", {"head_pitch": -4}, "hold_ball", "holding a ball", ["ball"]),
    ("fly_kite", "stand", {"head_pitch": 30, "lean": -3}, "kite", "flying a kite", ["kite", "look_up"]),
    ("balloon", "stand", {"head_pitch": 6}, "balloon", "holding a balloon", ["balloon"]),
    ("paint", "stand", {"lean": 4, "head_pitch": 8}, "paint", "painting", ["chore"]),
    ("photo", "stand", {}, "photo", "taking a photo", ["look"]),
    ("give_flowers", "stand", {"lean": 4}, "flowers", "giving flowers", ["social"]),
    ("feed_birds", "stand", {"lean": 8, "head_pitch": -24}, "feed_birds", "feeding the birds", ["birds"]),
    ("fish", "stand", {"head_pitch": -6}, "fish", "fishing", ["water"]),
    ("bucket_hat", "wide", {"lean": -3}, "bucket_hat", "wearing a bucket on their head", ["misuse"]),
    ("walk_bag", "walk", {}, "carry_bag", "walking with a shopping bag", ["carry", "shop", "move"]),
    ("walk_box", "walk", {"lean": -2}, "carry_box", "carrying a box", ["carry", "move"]),
    ("walk_umbrella", "walk", {}, "umbrella", "walking with an umbrella", ["rain", "move"]),
    ("walk_dog", "walk", {}, "walk_dog", "walking a dog", ["dog", "move"]),
    ("walk_balloon", "walk", {"head_pitch": 4}, "balloon", "walking with a balloon", ["balloon", "move"]),
    ("walk_ice_cream", "walk", {"head_pitch": ICE49_PITCH}, "ice_cream", "walking with an ice cream", ["food", "move"]),
    ("walk_basket", "walk", {}, "carry_basket", "carrying a basket", ["carry", "picnic", "move"]),
    ("sit_read", "sit", {"head_pitch": -26}, "read", "sitting and reading", ["sit", "read"]),
    ("sit_drink", "sit", {"head_pitch": 16}, "drink", "sitting with a drink", ["sit", "food"]),
    ("sit_ice_cream", "sit", {"head_pitch": ICE49_PITCH}, "ice_cream", "sitting and eating ice cream", ["sit", "food"]),
    ("sit_feed_birds", "sit", {"lean": 10, "head_pitch": -26}, "feed_birds", "sitting and feeding the birds", ["sit", "birds"]),
    ("sit_clap", "sit", {"head_pitch": 4}, "clap", "sitting and clapping", ["sit", "emotion"]),
    # v0.7
    ("sweep_giant_fork", "wide", {"lean": 20, "head_pitch": -24}, "sweep_giant_fork", "sweeping with a giant dinner fork", ["chore", "misuse"]),
    ("sand_build", "kneel", {}, "spade_pat", "building a sandcastle", ["play", "low"]),
    ("feed_birds_low", "stand", {"lean": 16, "head_pitch": -40}, "feed_birds_low", "feeding the birds", ["birds"]),
    ("jump_tuck", "jump_tuck", {}, "cheer", "doing a star jump for joy", ["move", "airborne", "emotion"]),
    ("seesaw_stuck", "sit_dangle", {}, "grip_handle", "up high on a seesaw, holding on", ["sit", "seesaw"]),
    ("seesaw_stuck_call", "sit_hang", {}, "grip_call" if CALL44 == "A" else "grip_handle", "stuck up in the air, holding on tight, calling out", ["sit", "seesaw"]),
    ("seesaw_low", "sit_low", {}, "cross_arms", "sitting on the low end of a seesaw", ["sit", "seesaw"]),
    # v0.9
    ("balloon_reach", "stand", {"head_pitch": 26, "lean": -3}, "balloon_reach", "holding balloons and reaching for one that got away", ["balloon", "reach"]),
    ("walk_read_open", "walk", {"head_pitch": WALK_READ_PITCH}, "read_open", "reading while walking", ["read", "move"]),
    # v0.32 bench (TPDB_LOW, with templates.LOW32): "O" knees up, the feet planted near the seat, so the near shin crosses the rising plank ("sitting on the
    # plank end or sitting just beside it with the plank behind his legs", v0.31); "X" the legs out along the ground under the plank; "F" the feet further out, for a
    # rider turned away from the plank, whose feet land past its end
    ("seesaw_low_read", "sit_low", {"head_pitch": -26, "lean": -4, "feet": {"O": (0.20, -0.19), "X": (0.17, -0.86), "F": (0.20, -0.30)}[__import__("os").environ.get("TPDB_LOW", "O")]},
     "read_open", "sitting on the low end of the seesaw, reading", ["sit", "seesaw", "read"]),
    # v0.10
    ("cone_dropped", "stand", {"head_pitch": -34, "head_roll": 4}, "empty_cone_low", "holding an empty cone, upset, looking down at the dropped ice cream", ["food", "emotion"]),
    # v0.24: U, chosen on the bench (isolation_v024.md); O the v0.23 arms, H hands holding the chute ("just sitting still")
    ("slide_down", "sit_slide", {}, {"U": "slide_up", "H": "slide_hold", "O": "cheer"}[__import__("os").environ.get("TPDB_SLIDE", "U")],
     "sliding down the slide with arms up", ["sit", "slide", "play", "emotion"]),
]


def _x_wave(d):
    def f(P):
        P.arms({"R": (P.lm("sh_R") + nrm(d) * P.A, (-1, 0.2, -0.6)), "L": P.rest_arm("L")})
        P.hand("R", "open", palm=(0, -1, 0))
    return f


def _x_dangle(feet, head_turn=0.0, head_pitch=-12.0, toe=(0, -0.45, -1)):
    def f(P):
        J, S, s = P.J, P.S, P.s
        drop = J["hip"] * S - J["knee"] * S
        P.torso(drop=drop, back=0.04 * S * s, lean=6, head_pitch=head_pitch, head_turn=head_turn)
        P.place_legs({sd: (dx, dy * s, lift * s) for sd, (dx, dy, lift) in feet.items()}, hint=(0, -1, 0.6))
        for sd in ("L", "R"):
            P.rig.aim_dir(f"foot_{sd}", toe)
    return f


def _x_grip_reach(reach=(-0.12, -0.78, 0.62)):
    def f(P):
        u = P.u
        c = P.lm("chest")
        P.arms({"R": (P.lm("sh_R") + nrm(reach) * P.A * 0.98, (-1, 0.3, -0.5)), "L": (c + Vector((0.07, -0.20, -0.02)) * u, (1, 0.3, -0.7))})
        P.hand("R", "open", palm=(0, -1, 0.3))
        P.panchor("handle", P.grip("L"))
    return f


def _x_grip_call():
    def f(P):
        u = P.u
        c = P.lm("chest")
        m = P.lm("mouth")
        P.arms({"R": (c + Vector((-0.07, -0.20, -0.02)) * u, (-1, 0.3, -0.7)), "L": (m + Vector((0.05, -0.11, -0.03)) * u, (1, 0.3, -0.7))})
        P.hand("L", "open", palm=(-0.6, -0.3, 0))
        P.panchor("handle", P.grip("R"))
    return f


def experimental_actions():
    """Pose experiments for the isolation bench (TPDB_PEXP set; never in a release build)."""
    import json, os
    out = []
    for i, d in enumerate(json.loads(os.environ["TPDB_PEXP"])):
        lo = d.get("lower")
        up = d.get("upper")
        lf = LOWER[lo] if isinstance(lo, str) else _x_dangle({k: tuple(v) for k, v in lo["feet"].items()}, lo.get("head_turn", 0.0), lo.get("head_pitch", -12.0), tuple(lo.get("toe", (0, -0.45, -1))))
        if isinstance(up, dict) and "wave" in up:
            uf = _x_wave(tuple(up["wave"]))
        elif isinstance(up, dict) and "gripcall" in up:
            uf = _x_grip_call()
        elif isinstance(up, dict) and "reach" in up:
            uf = _x_grip_reach(tuple(up["reach"]))
        else:
            uf = UPPER[up]
        LOWER[f"xl{i}"], UPPER[f"xu{i}"] = (lambda P, lf=lf, isstr=isinstance(lo, str), **kw: lf(P, **kw) if isstr else lf(P)), uf
        out.append((f"exp{i}", f"xl{i}", d.get("largs", {}) if isinstance(lo, str) else {}, f"xu{i}", "experiment", ["exp"]))
    return out


def make_people_actions(rig, ctx):
    P = Poser(rig, ctx)
    import os
    acts = ACTIONS + (experimental_actions() if os.environ.get("TPDB_PEXP") else [])
    if os.environ.get("TPDB_RAIN49") == "B":
        # v0.49 bench (vision/isolation_v049.md round 1; scenegen templates.RAIN49 "B"), not chosen: built only for that bench
        acts = acts + [("feel_rain", "stand", {"head_pitch": 26}, "feel_rain", "holding a hand out, palm up, and looking up", ["social", "look_up"])]
    if os.environ.get("TPDB_PEXP_ONLY"):
        acts = [a for a in acts if a[0].startswith("exp") or a[0] in ("stand", "walk")]
    for name, lower, largs, upper, desc, tags in acts:
        if name == "walk_read_open" and ctx.spec.get("hair") != "bob":
            largs = dict(largs, head_pitch=WALK_READ_PITCH_OTHERS)
        if name == "walk_ice_cream" and os.environ.get("TPDB_ICE", "B") == "B":
            # v0.27: this one is only drawn in full profile, so its head can turn in the pose itself, and the cone goes to the turned mouth
            largs = dict(largs, head_turn=PROFILE47)
        P.build(name, lower, upper, lower_args=largs, description=desc, tags=tags, airborne="airborne" in tags)
    rig.reset()
    return P
