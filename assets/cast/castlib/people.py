"""People: skeleton, body, wardrobe, hair, hats, facial hair, face and anchors."""
import math
import random

import bpy  # noqa: F401
import bmesh
from mathutils import Quaternion, Vector

from .core import HEAD48, HEAD49, ISECT39, Rig, anchor, cut_field, cyl, ellipsoid, flatten_above, flatten_below, head_f, head_g, head_pt, link, mat, no_isect, open_branch, open_end, rest_shade, set_head, shell_over, skin_like, skin_object, smooth_curve, squircle, tube, tube_mesh, upd, _mesh_object
from .face import FACE48, MOUTH_DZ, PROF48, PROF48_MOUTH, Face, build_people_face, people_expression_states

# v0.23 (TPDB_HEAD; the release builds with B): the older man's fringe of hair kept to the back, and a fuller nose
HEAD_STYLE = __import__("os").environ.get("TPDB_HEAD", "B")   # v0.23: B (bench: both readers had him walking the right way)
# v0.39 bench switches (vision/isolation_v039.md), each "O" for v0.38's drawing:
# TPDB_SHOE39 "D": each shoe one piece (a heel and a toe ellipsoid read as two lobes, two shoes side by side as "three or four blobs"), a small round
#   heel and a toe reaching ahead of the leg, a flat sole and wider than the ankle, so it shows from the front; bare legs with a calf and a narrow
#   ankle (an even tube "straight into the shoe"); trouser legs ending a little lower and wider, over the shoe's top
# TPDB_MID39 "B": the shirt tucked into the trousers (its rounded hem pinched in above the waistband and a strip of trouser showed, so it read as
#   cropped), or for a hoodie, cardigan or vest hemmed lower over the waistband; a dress or skirt in one piece from the waist with a hem edge (two
#   lumps, "the waist is pinched and the dress looks like two stacked lumps"); a seat in profile; the hip filled when the thigh turns forward
# TPDB_MID39 "C": as "B" without the tuck (round 1: the tee tucked under a wider waistband read as "a hoop or rubber ring around his middle").
# TPDB_BELT39 "B": a flat belt band on the waistband that bends with the trousers (a rigid tube round the hips, "a dark tyre", "stacked dark bands")
SHOE39 = __import__("os").environ.get("TPDB_SHOE39", "D")  # v0.39 bench (vision/isolation_v039.md): D, one shoe, flat, toe forward
MID39 = __import__("os").environ.get("TPDB_MID39", "C")  # v0.39 bench (vision/isolation_v039.md): C, B without the tuck
BELT39 = __import__("os").environ.get("TPDB_BELT39", "O")  # v0.39 bench (vision/isolation_v039.md): O, the band read as "a hoop"
# v0.42 bench switches (figure-fixes-v041.md), each "O" for v0.41's drawing:
# TPDB_MID42 (item 3): MID39's seat and filled hip left a V across the front of the trousers, a "briefs" look (a contour where the hull folds
#   between the hip node and the leg). "B": the seat and the hip nodes set back and smaller, blended into the waist and thigh; "C": the seat set
#   back and no hip node
# TPDB_BELT42 (item 2): the tube belt read as a ring round the waist with a strip of trouser above it. "B": no belt under an untucked tee (the
#   tee's hem covers the waistband, as MID39 does for the hoodie and cardigan)
# TPDB_FOOT42 (item 6): front-view shoes round blobs with no toe, bare legs even pegs. "B": the toe longer and flatter, so it shows below the
#   cuff from the front, and a sole under it; a bare leg's calf fuller and set back, the knee and ankle narrower
MID42 = __import__("os").environ.get("TPDB_MID42", "C")  # v0.42 bench (vision/isolation_v042.md): C
BELT42 = __import__("os").environ.get("TPDB_BELT42", "B")  # v0.42 bench (vision/isolation_v042.md): B
FOOT42 = __import__("os").environ.get("TPDB_FOOT42", "B")  # v0.42 bench (vision/isolation_v042.md): B
# v0.45 bench (vision/flaws_v044.md O2, TPDB_SOLE45): the sole plate is longer than the shoe and pointed, and the shoe's flat underside is only
# seven-tenths of its length, so under a tipped shoe the plate stands clear of the toe and the heel like a blade: "black ice skates" under a walker's
# dark shoes. "A": the plate no longer than the flat underside and no wider than the shoe, dark under every shoe. (actions.py has "H".)
SOLE45 = __import__("os").environ.get("TPDB_SOLE45", "A")  # v0.45 bench (vision/isolation_v045.md): A
# v0.46 bench switches (vision/isolation_v046.md), each "O" for v0.45's drawing:
# TPDB_NECK46 "B": the necks under a scaled-down head (the two women's, 0.85 and 0.90, and ben's, 0.95). v0.43 raised the women's heads by
#   2.5 cm on a neck thinned with the smaller head, and a head scaled down rose off the shoulders besides, so the neck showing was twice the
#   others' and thinner: "a neck that is too long". A scaled-down head's chin sits where a full-size head's does, no neck is added, and the
#   neck keeps its full width.
# TPDB_ARM46 "B": a tee's sleeve ends nearer the arm's width and the bare arm is a little fuller (the sleeve stood off the arm like a shoulder
#   pad); the resting arm hangs nearer the body and straighter (actions.py: it hung a hand's width out from the hip, bent at the elbow)
# TPDB_CLEAN46 "B": no seam line at the wrist (hand and forearm are one skin: the line made a jointed doll's hand); the safety vest's two
#   silver bands lie on the vest all the way round (their width was measured from points that a thin slice of the vest often did not have,
#   so in profile they stood off the chest and the back like a hoop, and cut into the vest elsewhere in a zigzag of seam lines)
NECK46 = __import__("os").environ.get("TPDB_NECK46", "B")
CLEAN46 = __import__("os").environ.get("TPDB_CLEAN46", "B")
ARM46 = __import__("os").environ.get("TPDB_ARM46", "B")
# TPDB_COLLAR46 "B" (second round): every grown figure's neckline higher and neck fuller. The bench's reviewers called the grandmother's neck
#   "long and thin" and a man's "a thin stalk" in both casts: the top's neckline lay 5 cm under the chin round a neck a third of the head's
#   width, and where the shoulders were lowered (TPDB_ARM46) more of it showed. ("C": higher and fuller still, a trial.)
COLLAR46 = __import__("os").environ.get("TPDB_COLLAR46", "B")
# TPDB_MOUSTACHE46 "C" (after the second round; build_facial_hair): the moustache a smooth curve that follows the face, as thick as v0.45's
#   over most of its length and rounded off at its two ends. "B", the second round's, thinned from the middle on: on the grandfather a
#   reviewer found v0.45's "a little easier to see".
MOUSTACHE46 = __import__("os").environ.get("TPDB_MOUSTACHE46", "C")
# TPDB_MOUSTACHE47 "B" (vision/flaws_v046.md O1; build_facial_hair): the moustache lay on the mouth, as wide as the mouth and in the hair's own
# brown: "it could also be a smear of something (for example chocolate) on his face", "looks a little like a smudge" (pictures 9 and 92).
# "B": wider than the mouth, in two halves parted under the nose (nipped in at the middle), each half full over the mouth's corner and thinning
# to a point beside it, its lower edge clear of the mouth's line, and for brown hair a shade darker than the hair. "O": v0.46's
MOUSTACHE47 = __import__("os").environ.get("TPDB_MOUSTACHE47", "B")
COLLAR46_DZ = {"O": 0.0, "B": 0.014, "C": 0.022}[COLLAR46]
COLLAR46_NR = {"O": 0.054, "B": 0.062, "C": 0.068}[COLLAR46]
# v0.47 bench switches (vision/isolation_v047.md), each "O" for v0.46's drawing. One figure, the woman in the yellow dress, was drawn in
# fifty-two poses and angles and read by three reviewers of enlarged cut-outs, and the rest of the cast by two more; what two or more named:
# TPDB_SHOULDER47 "B": the shoulders slope. The top of every shirt was a flat line as wide as the chest with a shoulder's ball at each end
#   as high as the neckline ("Square coat-hanger shoulders", "a flat horizontal shelf right under the chin", "shoulder pads"). The shirt's top node is the
#   base of the neck, a new node under it is the line of the shoulders, and the shoulder's ball hangs from that, lower and smaller.
# TPDB_LIMB47 "B": arms and legs taper ("straight tubes of one width", "no elbows or wrists", "no knees or ankles"): the upper arm narrows
#   to the elbow, the forearm swells a little under it and narrows to a slim wrist; a bare leg's knee and ankle narrower and its calf
#   fuller; a trouser leg narrows to a cuff cut straight across (of its rounded end: "The bottoms balloon over the shoes").
# TPDB_HAND47 "B": the hand a mitten wider than the wrist from the side and flatter from the front, its thumb standing clear at the front
#   inner edge ("mitten blobs with one curl and no thumb").
# TPDB_SHOE47 "B": the shoe a wedge, highest at the ankle and falling to a rounded toe, flat underneath over nearly its whole length, on
#   a dark sole as long as that flat ("flat ovals or paddles with no toe, sole, heel or ankle", "a detached sole line").
# TPDB_HEM47 "B": a skirt's lower half turns with the thighs, each side with its own leg and the middle between them, so a stride pushes
#   the cloth and the hem stays one line (the bell hung from the hips, and a striding or kneeling leg came through its front: "the skirt
#   outline is torn where a leg exits"); seated, the cloth lies along the thighs ("the thighs are missing").
# TPDB_NOSE47 "B": no line where the nose passes into the face. From the front the nose was a closed ring ("an outlined ring", "a small ring
#   stuck on the outline"); now it is a bump with a shadow under it from the front and an open curve in a turned view, and the profile's
#   outer line still runs round it.
SHOULDER47 = __import__("os").environ.get("TPDB_SHOULDER47", "B")
LIMB47 = __import__("os").environ.get("TPDB_LIMB47", "B")
HAND47 = __import__("os").environ.get("TPDB_HAND47", "B")
SHOE47 = __import__("os").environ.get("TPDB_SHOE47", "B")
HEM47 = __import__("os").environ.get("TPDB_HEM47", "B")
# TPDB_SEAT47 "B": seated, a skirt is another object, a wrap of the two thighs (see the skirt below); "O" keeps the bell in every posture
SEAT47 = __import__("os").environ.get("TPDB_SEAT47", "B")
# TPDB_CARDI47 "B": a cardigan shows the top under it in a V below the collar and closes in a line down the front, its buttons on the line;
# "O" is v0.46's strip of the inner colour from collar to hem with the buttons beside it ("a plank", off the middle in a turned view)
CARDI47 = __import__("os").environ.get("TPDB_CARDI47", "B")
NOSE47 = __import__("os").environ.get("TPDB_NOSE47", "B")


# TPDB_HEAD47 "B": the head fuller between front and side. On a ball, an eye a third of the way round from the nose is at the outline of a
#   head turned 45 degrees, where the outer line covers half of it ("the far eye is clipped by the head outline", "the far eye sits right on the
#   head outline and is half cut off"), and the mouth's far end is under the same line. The head's level sections are squircles, |x|^n + |y|^n = r^n:
#   from the front, the back and the side its outline is the ball's, and turned 45 degrees the far cheek stands past the far eye.
HEAD47 = __import__("os").environ.get("TPDB_HEAD47", "B")
HN = 3.0 if HEAD47 == "B" else 2.0
# v0.48 (core.HEAD48 "B"): the head's half width, half depth and half height in units of its radius (v0.47: 1.04, 0.98, 0.96, or 0.99, 0.98,
# 1.00 for the two women with the narrower face), and how far its chin is lowered
HEAD48_R = tuple(float(x) for x in __import__("os").environ.get("TPDB_HEAD48_R", "0.92,0.97,1.06").split(","))
HEAD48_CHIN = __import__("os").environ.get("TPDB_HEAD48_CHIN", "")
# (pair bench 1, vision/isolation_v048.md: under the narrower jaw more of the neck shows, a child's most of all, "long and thin like a stalk, so
# the head looks perched on a stick". The chin is set lower by this much of the head's radius, a child's further, and a child's neck is fuller)
HEAD48_CHIN_KIND = {"adult": -0.04, "child": -0.14}
# TPDB_TORSO48 "B" (pair bench 1: "the shirt is very short and the trouser waist very high, so the upper body looks short against long legs",
# of four figures in v0.47's drawing and in v0.48's alike): a tee worn over trousers or shorts is hemmed at the hips, as the hoodie and the
# cardigan have been since v0.39, and not at the waist. "O": v0.47's short tee
TORSO48 = __import__("os").environ.get("TPDB_TORSO48", "B")


NECK49 = __import__("os").environ.get("TPDB_NECK49", "B")       # "O": the neck a piece of the skin's one mesh, as up to v0.48

# v0.52 (TPDB_SLEEVE52 "B"; vision/isolation_v052.md). Sam's brief was the upper arms, the shoulders and the sleeves. "O": v0.51's drawing.
#   What v0.51 drew. A tee's sleeve was a short cap that ended above the armpit in the hull's rounded end, narrower than the arm it held; the bare
#   arm is a part that draws no line where it passes into another, so the sleeve had no hem, the arm stepped out wider under it, and raised it
#   went up bare from a stub of cloth at the armpit. Reviewers of pairs, who did not know which row was which: "the puffed caps sit on the arm like small pads",
#   "The arm's rounded top sits flat on the shirt like a sticker.", "the raised arm comes almost straight out of the body like a tank top". A long sleeve
#   was one thick tube to a rounded end at the wrist: "sleeves are uniformly inflated, sausage-like tubes", "it reads as a puffed costume sleeve".
#   "B". The sleeve is cloth round the arm: a tee's runs 0.44 of the way to the elbow, as wide as this figure's own arm and four millimetres
#   more, tapering a little to its hem; the hem is cut straight across the arm and open (core.open_branch), with a lid just inside that draws
#   the line where the arm comes out, and it goes with the arm wherever the arm goes. A long sleeve has a node on the upper arm and tapers
#   from the shoulder to an open cuff above the wrist, the forearm coming out through the cuff's lid. The shoulder's ball is where v0.51 had it.
#   Three rounds of blind pairs, each pairing in both orders (isolation_v052/arms1 to arms3): the new drawing was chosen by 10 reviewers of 12,
#   10 of 12 and 4 of 6. The four sets of standing and working figures chose it in both orders every time; the two sets of raised arms and of
#   long sleeves in action chose whichever row was drawn below, three rounds of three. What the rounds changed: the first trial's sleeves were
#   as wide as a man's on every arm ("the sleeves flare out like wings, much wider than the arms") and longer, and its long sleeves thinner.
#   The Skin hull breaks at the node where the neck, the chest and the two shoulders meet when a shoulder's radius or place changes by a few
#   millimetres (one figure of ten, a plate of cloth through the chest): TPDB_HULLCHECK=1 prints each hull's count, and a count that
#   differs from the last build's is looked at on a sheet before anything else.
SLEEVE52 = __import__("os").environ.get("TPDB_SLEEVE52", "B")
# (the numbers of the drawing, in metres of a standard adult before the figure's own scale; TPDB_SLEEVE52_P, a JSON dict, changes some for a trial)
SLEEVE52_P = dict(ball_dx=0.014, ball_dz=0.035, ball_r=0.054, ls_ball_r=0.052, ball_w=0.45, ball_pow=0.0, up_w=0.10,
                  ss_f=0.44, ss_r=0.0515, ss_mid_f=0.24, ss_mid_r=0.0535, arm_f=0.30,
                  ls_up_f=0.30, ls_up=0.051, ls_el=0.047, ls_cuff=0.040, ls_f=0.08, stub_f=0.30, inset=0.004, lid_k=0.90, hem_k=0.95)
SLEEVE52_P.update(__import__("json").loads(__import__("os").environ.get("TPDB_SLEEVE52_P", "{}")))


def head49_shape(spec, kind):
    """v0.49 (core.HEAD49): the shape of this person's head. TPDB_HEAD49_SHAPE (bench) is a JSON dict of changes for everybody, or one per family
    name with "*" for the rest."""
    env = __import__("os").environ.get("TPDB_HEAD49_SHAPE")
    if env:
        d = __import__("json").loads(env)
        if any(isinstance(v, dict) for v in d.values()):
            d = d.get(spec.get("family"), d.get(kind, d.get("*")))
        return d
    return spec.get("head49", "child" if kind == "child" else "man")


def person_skeleton(kind):
    if kind == "child":
        return dict(ankle=0.05, knee=0.26, hip=0.48, pelvis=0.53, chest=0.71, neck=0.79, head_base=0.82,
                    head_c=0.950, head_r=0.140, sh_x=0.115, sh_z=0.765, el_z=0.615, wr_z=0.485, hand_len=0.055,
                    hip_x=0.065, toe=0.09, s=0.66)
    if __import__("os").environ.get("TPDB_BODY", "B") == "B":
        # v0.27, chosen on the bench: legs an eighth shorter, the rest of the figure lowered with them, the shin kept so a sitter's feet still reach the ground ("very long, thin legs and a small
        # torso", "long and thin relative to" the rest, on nearly every cut-out)
        L_ = 0.10
        return dict(ankle=0.07, knee=0.44, hip=0.84 - L_, pelvis=0.90 - L_, chest=1.16 - L_, neck=1.30 - L_, head_base=1.34 - L_,
                    head_c=1.485 - L_, head_r=0.158, sh_x=0.175, sh_z=1.245 - L_, el_z=1.005 - L_, wr_z=0.785 - L_, hand_len=0.075,
                    hip_x=0.09, toe=0.13, s=1.0)
    return dict(ankle=0.07, knee=0.45, hip=0.84, pelvis=0.90, chest=1.16, neck=1.30, head_base=1.34,
                head_c=1.485, head_r=0.158, sh_x=0.175, sh_z=1.245, el_z=1.005, wr_z=0.785, hand_len=0.075,
                hip_x=0.09, toe=0.13, s=1.0)


class PersonCtx:
    """Everything the action builder needs to know about a built person."""


def surface_points(obj):
    upd()
    dg = bpy.context.evaluated_depsgraph_get()
    oe = obj.evaluated_get(dg)
    me = oe.to_mesh()
    pts = [oe.matrix_world @ vv.co for vv in me.vertices]
    oe.to_mesh_clear()
    return pts


def front_y(pts, z, x=0.0, tol=0.02):
    near = [q for q in pts if abs(q.z - z) < tol and abs(q.x - x) < tol * 2]
    return min(q.y for q in near) if near else min(q.y for q in pts)


TORSO = {"hips", "spine", "chest", "neck"}


def build_person(spec):
    kind = "child" if spec["age"] in ("child",) else "adult"
    J = person_skeleton(kind)
    if spec.get("neck_add") and NECK46 == "O":
        # v0.43 (TPDB_ADULT43): a longer neck, the head raised with it
        J = dict(J, head_base=J["head_base"] + spec["neck_add"], head_c=J["head_c"] + spec["neck_add"])
    AF = bool(spec.get("adult_face"))
    S = spec.get("scale", 1.0)
    s = J["s"]
    HS = spec.get("head_scale", 1.0)

    def P(x, y, z):
        return Vector((x * S, y * S, z * S))

    root = link(bpy.data.objects.new("ROOT", None))
    sx, hx = J["sh_x"], J["hip_x"]
    bones = {
        "hips": (P(0, 0, J["pelvis"]), P(0, 0, J["pelvis"] + 0.08 * s), None),
        "spine": (P(0, 0, J["pelvis"]), P(0, 0, J["chest"]), "hips"),
        "chest": (P(0, 0, J["chest"]), P(0, 0, J["neck"]), "spine"),
        "neck": (P(0, 0, J["neck"]), P(0, 0, J["head_base"]), "chest"),
        "head": (P(0, 0, J["head_base"]), P(0, 0, J["head_base"] + 0.30 * s), "neck"),
    }
    for side, sg in (("L", 1), ("R", -1)):
        bones.update({
            f"upper_arm_{side}": (P(sg * sx, 0, J["sh_z"]), P(sg * (sx + 0.015 * s), 0, J["el_z"]), "chest"),
            f"forearm_{side}": (P(sg * (sx + 0.015 * s), 0, J["el_z"]), P(sg * (sx + 0.025 * s), 0, J["wr_z"]), f"upper_arm_{side}"),
            f"hand_{side}": (P(sg * (sx + 0.025 * s), 0, J["wr_z"]), P(sg * (sx + 0.028 * s), 0, J["wr_z"] - J["hand_len"]), f"forearm_{side}"),
            f"thigh_{side}": (P(sg * hx, 0, J["hip"]), P(sg * hx, -0.01 * s, J["knee"]), "hips"),
            f"shin_{side}": (P(sg * hx, -0.01 * s, J["knee"]), P(sg * hx, 0, J["ankle"]), f"thigh_{side}"),
            f"foot_{side}": (P(sg * hx, 0, J["ankle"]), P(sg * hx, -J["toe"], 0.02 * s), f"shin_{side}"),
        })
    rig = Rig(root, bones)

    hr = J["head_r"] * S * HS
    hc = P(0, 0, J["head_c"]) + Vector((0, 0, (HS - 1) * J["head_r"] * S * 0.6))
    HR = (hr * 1.04, hr * 0.98, hr * 0.96)
    if AF:
        HR = (hr * 0.99, hr * 0.98, hr * 1.00)      # v0.43 (TPDB_ADULT43): a narrower, taller face
    if NECK46 == "B" and HS < 1.0:
        # v0.46: the chin of a scaled-down head where a full-size head's is
        hc = P(0, 0, J["head_c"] - J["head_r"] * 0.96) + Vector((0, 0, HR[2]))
    HSH = set_head(head49_shape(spec, kind) if HEAD49 == "B" else None)     # v0.49 (core.HEAD49): this person's head
    if HEAD48 == "B":
        # v0.48 (core.HEAD48): taller than wide, with its chin where v0.47's was
        chin_z = hc.z - HR[2]
        HR = tuple(hr * a for a in (HSH["R"] if HEAD49 == "B" else HEAD48_R))
        # (v0.49, HSH["hy"]: the head carried forward of the neck by that share of its radius)
        hc = Vector((hc.x, hc.y - HSH.get("hy", 0.0) * hr, chin_z + HR[2] + (float(HEAD48_CHIN) if HEAD48_CHIN else HSH.get("chin", HEAD48_CHIN_KIND[kind])) * hr))
    sh = {sd: P(sg * sx, 0, J["sh_z"]) for sd, sg in (("L", 1), ("R", -1))}
    el = {sd: P(sg * (sx + 0.015 * s), 0, J["el_z"]) for sd, sg in (("L", 1), ("R", -1))}
    wr = {sd: P(sg * (sx + 0.025 * s), 0, J["wr_z"]) for sd, sg in (("L", 1), ("R", -1))}
    k = S * s if kind == "child" else S
    kh = k * HS

    B = dict(chest=1.0, waist=1.0, hips=1.0, depth=1.0, belly=0.0, limbs=1.0)
    B.update(spec.get("build", {}))
    if __import__("os").environ.get("TPDB_BODY", "B") == "B":
        B["limbs"] *= 1.14
    if __import__("os").environ.get("TPDB_BODY", "B") == "A":
        # v0.26 bench: fuller from the side (nearly every cut-out of the first round: "the torso is extremely thin from the side", "very long,
        # thin legs"). Tried and left: the readers' words did not move (isolation_v026.md)
        B["depth"] *= 1.22
        B["limbs"] *= 1.12
    pel, ch, nk = J["pelvis"], J["chest"], J["neck"]
    top, bottom = spec.get("top", "tee"), spec.get("bottom", "pants")
    long_sleeve = top in ("long", "hoodie", "cardigan") or spec.get("sleeves") == "long"
    top_col = spec["shirt"]
    dp = B["depth"]
    LB = B["limbs"]
    LA = LB * B.get("arms", 1.0)      # v0.48: the arms' own thickness (a woman's arms as thick as her legs: "thick tube")
    TI = 1.12

    # --- torso (shirt / dress top / cardigan / hoodie) ----------------------
    cdz = COLLAR46_DZ if kind == "adult" else 0.0
    verts = [P(0, 0, pel + 0.035 * s), P(0, 0, pel + 0.13 * s), P(0, 0, ch - 0.01 * s), P(0, 0, nk - 0.020 * s + cdz)]
    radii = [(0.142 * k * B["waist"] * 1.05 * TI, 0.108 * k * dp * TI), (0.132 * k * B["waist"] * TI, 0.104 * k * dp * TI),
             (0.160 * k * B["chest"] * TI, 0.116 * k * dp * TI), (0.128 * k * B["chest"] * TI, 0.086 * k * dp * TI)]
    tucked = MID39 == "B" and top in ("tee", "long", "vest") and bottom in ("pants", "shorts")
    hemmed = MID39 in ("B", "C") and top in ("hoodie", "cardigan") and not tucked
    if TORSO48 == "B" and MID39 == "C" and top == "tee" and bottom in ("pants", "shorts"):
        hemmed = True
    if MID39 in ("B", "C") and bottom == "dress":
        # (the dress's top narrows into its skirt at the waist, which carries on below as one piece)
        radii[0] = (0.128 * k * B["waist"] * TI, 0.100 * k * dp * TI)
    elif tucked:
        # the shirt's tail ends inside the waistband, narrower than it (at nearly the waistband's width it poked through in a zigzag)
        verts[0] = P(0, 0, pel + 0.050 * s)
        radii[0] = (0.136 * k * B["waist"] * TI, 0.102 * k * dp * TI)
    elif hemmed:
        # a hoodie or cardigan worn over the waistband: hemmed lower and a little wider, its edge flattened after baking
        verts[0] = P(0, 0, pel - 0.030 * s)
        radii[0] = (0.156 * k * max(B["waist"], B["hips"]) * TI, 0.118 * k * dp * TI)
    # the hem follows the hips so a forward lean bends the shirt at the waist instead of lifting it off the pants
    wts = [{"hips": 0.85, "spine": 0.15}, {"spine": 0.70, "hips": 0.30}, {"spine": 0.4, "chest": 0.6}, {"chest": 1.0}]
    edges = [(0, 1), (1, 2), (2, 3)]
    if B["belly"] > 0 and SHOULDER47 == "B":
        # v0.47: a belly is the waist node itself set forward and deeper, the hem a little with it. (As a node of its own in front of
        # the waist it was a side branch whose flat end frame became the shirt's front: measured, the front lay 3 cm inside the back.)
        bf47 = 0.026 * B["belly"]
        verts[1] = P(0, -bf47 * s, pel + 0.12 * s)
        radii[1] = (radii[1][0], radii[1][1] + bf47 * k)
        verts[0] = verts[0] + P(0, -bf47 * s * 0.45, 0)
        radii[0] = (radii[0][0], radii[0][1] + bf47 * k * 0.45)
    elif B["belly"] > 0:
        i0 = len(verts)
        verts.append(P(0, -0.060 * s * B["belly"], pel + 0.12 * s))
        radii.append((0.128 * k * B["waist"], 0.100 * k * dp))
        wts.append({"spine": 0.8, "hips": 0.2})
        edges.append((1, i0))
    if B.get("bust", 0.0) > 0:
        # v0.50 (specs.AGE50): a woman's bust is the chest node set forward and deeper, as the belly is the waist node. The back stays where it was
        bf50 = 0.030 * B["bust"]
        verts[2] = verts[2] + P(0, -bf50 * s, -0.012 * s)
        radii[2] = (radii[2][0], radii[2][1] + bf50 * k)
    iu = 3
    if SHOULDER47 == "B":
        # v0.47: the top node is the base of the neck, a little wider than the neck it surrounds, and a node under it carries the
        # shoulders, so the outline falls from the neck to the shoulder
        radii[3] = (0.082 * k * TI, 0.072 * k * dp * TI)
        iu = len(verts)
        verts.append(P(0, 0, J["sh_z"] - 0.050 * s)); radii.append((0.105 * k * B["chest"] * TI, 0.085 * k * dp * TI)); wts.append({"chest": 1.0})
        edges = [e for e in edges if e != (2, 3)] + [(2, iu), (iu, 3)]
    hems52 = {}
    for sd, sg in (("L", 1), ("R", -1)):
        i0 = len(verts)
        if SLEEVE52 != "O":
            # v0.52: the sleeve is cloth round the arm and wider than it, and it ends in a hem cut straight across the arm (open_branch, below)
            # (the sleeve is as wide as this figure's own arm and a little more: on the slimmer arms of the women and the girl the first trial's
            # sleeves, as wide as a man's, stood out "like wings"; the shoulder's ball goes half the way with the arm's width)
            q52 = SLEEVE52_P
            verts.append(sh[sd] + Vector((-sg * q52["ball_dx"] * k, 0, -q52["ball_dz"] * k)))
            radii.append(q52["ls_ball_r" if long_sleeve else "ball_r"] * k * LB * B.get("arms", 1.0) ** q52["ball_pow"])
            wts.append({"chest": q52["ball_w"], f"upper_arm_{sd}": 1 - q52["ball_w"]})
            edges.append((iu, i0))
            up52 = {"chest": q52["up_w"], f"upper_arm_{sd}": 1 - q52["up_w"]}
            if long_sleeve:
                cuff52 = wr[sd] + (el[sd] - wr[sd]) * q52["ls_f"]
                verts += [sh[sd].lerp(el[sd], q52["ls_up_f"]), el[sd], cuff52]
                # (a long sleeve keeps the garment's own width, whoever wears it: as wide as a slim arm only, the cardigan's raised sleeve was "a stick")
                radii += [q52["ls_up"] * k * LB, q52["ls_el"] * k * LB, q52["ls_cuff"] * k * LB]
                wts += [up52, {f"upper_arm_{sd}": 0.5, f"forearm_{sd}": 0.5}, {f"forearm_{sd}": 1.0}]
                hems52[sd] = (cuff52, (wr[sd] - el[sd]).normalized())
                edges += [(i0, i0 + 1), (i0 + 1, i0 + 2), (i0 + 2, i0 + 3)]
            else:
                verts += [sh[sd].lerp(el[sd], q52["ss_mid_f"]), sh[sd].lerp(el[sd], q52["ss_f"])]
                radii += [q52["ss_mid_r"] * k * LA, q52["ss_r"] * k * LA]
                wts += [up52, {f"upper_arm_{sd}": 1.0}]
                hems52[sd] = (verts[-1], (el[sd] - sh[sd]).normalized())
                edges += [(i0, i0 + 1), (i0 + 1, i0 + 2)]
            continue
        shp = sh[sd] + Vector((-sg * 0.006 * k, 0, 0.004 * k))
        if ARM46 == "B":
            # (the shoulder's ball lower and smaller: it stood above the neckline, a peak at each corner of the shirt from the front)
            shp = sh[sd] + Vector((-sg * 0.010 * k, 0, -0.012 * k))
        if SHOULDER47 == "B":
            shp = sh[sd] + Vector((-sg * 0.014 * k, 0, -0.035 * k))
        verts.append(shp); radii.append((0.054 if SHOULDER47 == "B" else 0.056 if ARM46 == "B" else 0.060) * k * LB)
        wts.append({"chest": 0.45, f"upper_arm_{sd}": 1 - 0.45})
        edges.append((iu, i0))
        if long_sleeve:
            verts += [el[sd], wr[sd] + (el[sd] - wr[sd]) * 0.08]
            radii += [0.048 * k * LB, 0.041 * k * LB] if LIMB47 == "B" else [0.052 * k * LB, 0.047 * k * LB]
            wts += [{f"upper_arm_{sd}": 0.5, f"forearm_{sd}": 0.5}, {f"forearm_{sd}": 1.0}]
            edges += [(i0, i0 + 1), (i0 + 1, i0 + 2)]
        else:
            verts.append(sh[sd].lerp(el[sd], 0.50)); radii.append((0.054 if ARM46 == "B" else 0.057) * k * LB); wts.append({f"upper_arm_{sd}": 1.0})
            edges.append((i0, i0 + 1))
    shell_cardi = top == "cardigan" and CARDI47 == "B" and SHOULDER47 == "B"
    shirt = skin_object("Shirt", verts, edges, radii, spec.get("inner", "cream") if shell_cardi else top_col, rig, wts)
    if hemmed:
        flatten_below(shirt, (pel - 0.022 * s) * S, spare=("upper_arm_", "forearm_", "hand_"))
    for sd, (hp52, hn52) in hems52.items():
        arm52 = (f"upper_arm_{sd}", f"forearm_{sd}", f"hand_{sd}")
        open_branch(shirt, hp52 - hn52 * 0.002 * k, hn52, rig, spec.get("inner", "cream") if shell_cardi else top_col, f"SleeveLid_{sd}",
                    lambda co, w, a=arm52, p=hp52, n=hn52: sum(w.get(b, 0.0) for b in a) > 0.5 and (co - p).dot(n) > -0.03 * k,
                    inset=SLEEVE52_P["inset"] * k, lid_k=SLEEVE52_P["lid_k"], hem_k=SLEEVE52_P["hem_k"])

    if top == "vest" and SHOULDER47 == "B":
        # v0.47: the vest is a shell of the shirt's own surface (core.shell_over), a centimetre off it: cut away at each arm where the
        # sleeve begins, below the collar, and in a V at the front, so the shirt shows at the neck and the sleeves come out of real
        # armholes. (Reviewers of v0.46: "a pasted rectangle", the strip of shirt down its front "a white plank".)
        hivis = spec.get("vest_style") == "hivis"
        ARMS47 = ("upper_arm_", "forearm_", "hand_")
        zt47 = (nk - 0.020 * s + cdz) * S
        zv47 = (ch + (0.040 if hivis else -0.030) * s) * S
        sl47 = (zt47 - zv47) / ((0.060 if hivis else 0.066) * k)
        arm47 = lambda co, w: sum(x for n, x in w.items() if n.startswith(ARMS47)) - 0.35
        # (the neck hole is a round one about the neck's axis, a little narrower than the shirt's own top, so a ring of collar shows)
        nx47, ny47 = 0.088 * k, 0.070 * k * dp
        hole47 = lambda co, w: min(1.0 - (co.x / nx47) ** 2 - (co.y / ny47) ** 2, (co.z - ch * S) * 20.0)
        cuts47 = [arm47, hole47, lambda co, w: (co.z - zv47) - sl47 * abs(co.x) - 3.0 * max(0.0, co.y + 0.03 * k)]
        off47 = (0.010 if hivis else 0.013) * k
        # (the line down a buttoned vest's front, from the V's point to the hem)
        line47 = None if hivis else (lambda a, b: abs(a.x) < 1e-5 and abs(b.x) < 1e-5 and a.y < 0 and b.y < 0 and max(a.z, b.z) <= zv47 + off47)
        vest = shell_over(shirt, "Vest", spec["vest"], rig, off47, cuts47, rim=0.6 * off47, mark=line47)
        vest_pts = surface_points(vest)
        z0, z1 = (pel + 0.05 * s) * S, (nk - 0.03 * s) * S
        if hivis:
            # two silver bands, each a strip of the same surface a little further out
            for i, zf in enumerate((0.24, 0.52)):
                zb, hh = z0 + (z1 - z0) * zf, 0.020 * k
                band = shell_over(shirt, f"VestBand{i}", "silver", rig, off47 + 0.004 * k,
                                  [arm47, lambda co, w, zb=zb, hh=hh: co.z - (zb + hh), lambda co, w, zb=zb, hh=hh: (zb - hh) - co.z], rim=0.002 * k)   # (a rim as deep as the clearance lay on the vest: its edge drew dashed)
                no_isect(band)
        else:
            for i in range(3):
                z = z0 + (zv47 - z0) * (0.20 + 0.27 * i)
                skin_like(ellipsoid(f"VestButton{i}", (0, front_y(vest_pts, z, 0.0, 0.03 * k) - 0.002 * k, z), (0.008 * k, 0.004 * k, 0.008 * k), "outline", rig, "spine"), vest, rig, TORSO)
    elif top == "vest":
        # a sleeveless layer over the shirt: wider than the shirt everywhere below the shoulders,
        # open down the front (a strip of shirt shows through) so it reads as a vest, not a bib
        vv = [P(0, 0, pel + 0.040 * s), P(0, 0, pel + 0.13 * s), P(0, 0, ch - 0.01 * s), P(0, 0, nk - 0.016 * s + cdz)]
        # v0.31 bench (isolation_v031.md): "B" wider than the shirt by enough that the shirt cannot come through (it did, and drew "a jagged edge against the white shirt"); "C" wider still
        vest31 = __import__("os").environ.get("TPDB_VEST", "B") if spec.get("vest_style") != "hivis" else "O"
        vk31 = {"O": (1.075, 1.10), "B": (1.12, 1.20), "C": (1.16, 1.28)}[vest31]
        vr = [(r[0] * vk31[0], r[1] * vk31[1]) for r in radii[:4]]
        vr[3] = (radii[3][0] * 1.16, radii[3][1] * 1.14) if vest31 == "O" else (radii[3][0] * 1.18, radii[3][1] * vk31[1])
        vw = wts[:4]
        ve = [(0, 1), (1, 2), (2, 3)]
        if B["belly"] > 0:
            vv.append(verts[4]); vr.append((radii[4][0] * (1.07 if vest31 == "O" else vk31[0]), radii[4][1] * vk31[1])); vw.append(wts[4])
            ve.append((1, len(vv) - 1))
        # shoulder straps: the vest runs over the top of each shoulder, so it reads as a garment and
        # not as a tube around the chest
        for sd, sg in (("L", 1), ("R", -1)):
            vv.append(sh[sd] + Vector((-sg * 0.030 * k, 0, 0.010 * k)))
            vr.append(0.066 * k * LB)
            vw.append({"chest": 0.55, f"upper_arm_{sd}": 0.45})
            ve.append((3, len(vv) - 1))
        vest = skin_object("Vest", vv, ve, vr, spec["vest"], rig, vw)
        vest_pts = surface_points(vest)
        z0, z1 = (pel + 0.05 * s) * S, (nk - 0.03 * s) * S
        if spec.get("vest_style") == "hivis":
            # safety vest: two flat silver stripes hugging the vest (ribbons, not ropes)
            for i, zf in enumerate((0.26, 0.62)):
                zb = z0 + (z1 - z0) * zf
                hh = 0.020 * k
                bm = bmesh.new()
                rows = []
                if CLEAN46 == "B":
                    from mathutils.bvhtree import BVHTree
                    upd()
                    bvh46 = BVHTree.FromObject(vest, bpy.context.evaluated_depsgraph_get())
                    c46 = sum((q for q in vest_pts if abs(q.z - zb) < 0.05 * S), Vector((0, 0, 0)))
                    n46 = max(1, sum(1 for q in vest_pts if abs(q.z - zb) < 0.05 * S))
                    c46 = Vector((c46.x / n46, c46.y / n46, 0))
                for zz in (zb - hh, zb + hh):
                    ring_pts = [q for q in vest_pts if abs(q.z - zz) < 0.012 * S] or vest_pts
                    row = []
                    for j in range(64):
                        a = j / 64 * 2 * math.pi
                        dirv = Vector((math.cos(a), math.sin(a), 0))
                        if CLEAN46 == "B":
                            # the vest's own surface in this direction at this height, by a ray from outside
                            o46 = Vector((c46.x, c46.y, zz)) + dirv * 1.0
                            hit = bvh46.ray_cast(o46, -dirv, 1.0)[0]
                            pt = (hit if hit is not None else Vector((c46.x, c46.y, zz)) + dirv * 0.15 * k) + dirv * 0.004 * k
                            row.append(bm.verts.new(Vector((pt.x, pt.y, zz))))
                            continue
                        rad = max((q.x * dirv.x + q.y * dirv.y for q in ring_pts if (q.x * dirv.x + q.y * dirv.y) > 0 and
                                   abs(q.x * dirv.y - q.y * dirv.x) < 0.02 * k), default=0.15 * k)
                        row.append(bm.verts.new(Vector((dirv.x * (rad + 0.004 * k), dirv.y * (rad + 0.004 * k), zz))))
                    rows.append(row)
                for j in range(64):
                    a0, a1 = rows[0][j], rows[0][(j + 1) % 64]
                    b0, b1 = rows[1][j], rows[1][(j + 1) % 64]
                    bm.faces.new((a0, a1, b1, b0))
                bmesh.ops.solidify(bm, geom=bm.faces[:], thickness=0.003 * k)
                band = _mesh_object(f"VestBand{i}", bm, "silver", smooth=True)
                if CLEAN46 == "B":
                    no_isect(band)
                upd()
                skin_like(band, vest, rig, TORSO)
        else:
            pts = []
            for i in range(9):
                z = z0 + (z1 - z0) * i / 8
                pts.append(Vector((0, front_y(vest_pts, z, 0.0, 0.03 * k) - 0.001 * k, z)))
            strip = tube_mesh("VestOpening", pts, 0.022 * k, spec["shirt"])
            skin_like(strip, vest, rig, TORSO)
            for i in range(3):
                z = z0 + (z1 - z0) * (0.18 + 0.22 * i)
                skin_like(ellipsoid(f"VestButton{i}", (0.030 * k, front_y(vest_pts, z, 0.030 * k, 0.03 * k) - 0.004 * k, z), (0.008 * k, 0.004 * k, 0.008 * k), "outline", rig, "spine"), vest, rig, TORSO)
    torso_pts = surface_points(shirt)
    if shell_cardi:
        # v0.47 (TPDB_CARDI47): the cardigan is a shell of the top under it (core.shell_over, as the vest is), which is now of the inner
        # colour: open in a V below the collar, where that top shows, closed in a line from the V's point to the hem, the buttons on the
        # line. (v0.46 drew a strip of the inner colour down the cardigan's front with the buttons beside it: "a plank", and in a turned
        # view off the middle.)
        zt47 = (nk - 0.020 * s + cdz) * S
        zv47 = (ch + -0.050 * s) * S
        sl47 = (zt47 - zv47) / (0.060 * k)
        nx47, ny47 = 0.088 * k, 0.070 * k * dp
        hole47 = lambda co, w: min(1.0 - (co.x / nx47) ** 2 - (co.y / ny47) ** 2, (co.z - ch * S) * 20.0)
        off47 = 0.008 * k
        line47 = lambda a, b: abs(a.x) < 1e-5 and abs(b.x) < 1e-5 and a.y < 0 and b.y < 0 and max(a.z, b.z) <= zv47 + off47
        cardi = shell_over(shirt, "Cardigan", top_col, rig, off47,
                           [hole47, lambda co, w: (co.z - zv47) - sl47 * abs(co.x) - 3.0 * max(0.0, co.y + 0.03 * k)], rim=0.6 * off47, mark=line47)
        cardi_pts = surface_points(cardi)
        z0 = (pel + 0.01 * s) * S
        for i in range(3):
            z = z0 + (zv47 - z0) * (0.22 + 0.27 * i)
            skin_like(ellipsoid(f"Button{i}", (0, front_y(cardi_pts, z, 0.0, 0.03 * k) - 0.002 * k, z), (0.008 * k, 0.004 * k, 0.008 * k), "outline", rig, "spine"), cardi, rig, TORSO)
    elif top == "cardigan":
        z0, z1 = (pel + 0.06 * s) * S, (nk - 0.04 * s) * S
        pts = []
        for i in range(9):
            z = z0 + (z1 - z0) * i / 8
            pts.append(Vector((0, front_y(torso_pts, z, 0.0, 0.03 * k) - 0.002 * k, z)))
        strip = tube_mesh("Placket", pts, 0.017 * k, spec.get("inner", "cream"))
        skin_like(strip, shirt, rig, TORSO)
        for i in range(3):
            z = z0 + (z1 - z0) * (0.25 + 0.25 * i)
            skin_like(ellipsoid(f"Button{i}", (0.026 * k, front_y(torso_pts, z, 0.026 * k, 0.03 * k) - 0.004 * k, z), (0.008 * k, 0.004 * k, 0.008 * k), "outline", rig, "spine"), shirt, rig, TORSO)
    if top == "hoodie":
        skin_like(ellipsoid("Hood", P(0, 0.075 * s, nk - 0.005 * s), (0.125 * k, 0.065 * k, 0.075 * k), top_col, rig, "chest"), shirt, rig, TORSO)
        for sg in (1, -1):
            zt = (nk - 0.03 * s) * S
            x = sg * 0.030 * k
            pts = [Vector((x, front_y(torso_pts, zt - d * 0.12 * k, x, 0.03 * k) - 0.004 * k, zt - d * 0.12 * k)) for d in (0, 0.5, 1)]
            tube_and = tube_mesh(f"String{'L' if sg > 0 else 'R'}", pts, 0.006 * k, "cream")
            skin_like(tube_and, shirt, rig, TORSO)
        zp = (pel + 0.11 * s) * S
        pk = skin_like(ellipsoid("Pocket", (0, front_y(torso_pts, zp, 0, 0.03 * k) + 0.012 * k, zp), (0.085 * k, 0.020 * k, 0.045 * k), top_col, rig, "spine"), shirt, rig, TORSO)

    # --- bottoms ----------------------------------------------------------
    bare_legs = bottom in ("shorts", "skirt", "dress")
    bcol = top_col if bottom == "dress" else spec["pants"]
    if bottom in ("pants", "shorts"):
        # the waistband runs well up inside the shirt (narrower than it) so leaning never opens a gap
        verts = [P(0, 0, pel + 0.115 * s), P(0, 0, pel + 0.045 * s), P(0, 0, pel - 0.010 * s), P(0, 0.006 * s, pel - 0.070 * s)]
        radii = [(0.118 * k * B["waist"] * TI, 0.090 * k * dp * TI), (0.136 * k * B["waist"] * TI, 0.104 * k * dp * TI),
                 (0.150 * k * B["hips"] * TI, 0.114 * k * dp * TI), (0.136 * k * B["hips"] * TI, 0.104 * k * dp * TI)]
        wts = [{"hips": 0.6, "spine": 0.4}, {"hips": 0.92, "spine": 0.08}, {"hips": 1.0}, {"hips": 1.0}]
        if tucked:
            # the waistband rides up over the shirt's tail, wider than the shirt there, so the shirt goes into it and no strip of trouser shows
            verts[0], verts[1] = P(0, 0, pel + 0.072 * s), P(0, 0, pel + 0.030 * s)
            radii[0] = (0.170 * k * max(B["waist"], 0.96) * TI, 0.128 * k * dp * TI)
            radii[1] = (0.162 * k * max(B["waist"], B["hips"] * 0.96) * TI, 0.122 * k * dp * TI)
            if B["belly"] > 0:
                radii[0] = (radii[0][0] * 1.04, radii[0][1] * 1.10)
        if MID39 in ("B", "C") and MID42 in ("B", "C"):
            # v0.42 (TPDB_MID42): the seat further back and higher, a little narrower, so its bulge sits behind the hip line
            verts[3] = P(0, 0.030 * s, pel - 0.058 * s)
            radii[3] = (0.128 * k * B["hips"] * TI, 0.104 * k * dp * TI)
        elif MID39 in ("B", "C"):
            # a seat: the back of the hips set back and deeper, so a profile has a rump, not a straight column
            verts[3] = P(0, 0.016 * s, pel - 0.070 * s)
            radii[3] = (0.136 * k * B["hips"] * TI, 0.110 * k * dp * TI)
        edges = [(0, 1), (1, 2), (2, 3)]
        for sd, sg in (("L", 1), ("R", -1)):
            i0 = len(verts)
            j0 = 3
            if MID39 in ("B", "C") and MID42 == "C":
                pass            # (v0.42 "C": no hip node, the leg joined to the seat)
            elif MID39 in ("B", "C") and MID42 == "B":
                # v0.42 (TPDB_MID42 "B"): the hip node set back and smaller, so the hull does not fold over between it and the leg's top
                verts.append(P(sg * hx * 0.88, 0.020 * s, J["hip"] - 0.010 * s))
                radii.append(0.076 * k * B["hips"])
                wts.append({"hips": 0.6, f"thigh_{sd}": 0.4})
                edges.append((3, i0))
                j0, i0 = i0, i0 + 1
            elif MID39 in ("B", "C"):
                # the hip filled where the thigh turns forward: a node between the seat and the top of the leg, its weight blended over two steps
                # (one node at 0.35 hips and 0.65 thigh folded flat when sitting: "the thighs barely show going forward")
                verts.append(P(sg * hx * 0.85, 0.004 * s, J["hip"] - 0.012 * s))
                radii.append(0.083 * k * B["hips"])
                wts.append({"hips": 0.6, f"thigh_{sd}": 0.4})
                edges.append((3, i0))
                j0, i0 = i0, i0 + 1
            hip_w = {"hips": 0.2, f"thigh_{sd}": 0.8} if MID39 in ("B", "C") else {"hips": 0.35, f"thigh_{sd}": 0.65}
            if bottom == "pants":
                cuff = (P(sg * hx, 0, J["ankle"] - 0.004 * s), 0.058 * k * LB) if SHOE39 == "D" else (P(sg * hx, 0, J["ankle"] + 0.005 * s), 0.055 * k * LB)
                verts += [P(sg * hx, 0, J["hip"] - 0.03 * s), P(sg * hx, -0.01 * s, J["knee"]), cuff[0]]
                radii += [0.080 * k * B["hips"], 0.064 * k * LB, cuff[1]] if LIMB47 != "B" else [0.081 * k * B["hips"], 0.059 * k * LB, 0.051 * k * LB]
                wts += [hip_w, {f"thigh_{sd}": 0.5, f"shin_{sd}": 0.5}, {f"shin_{sd}": 1.0}]
                edges += [(j0, i0), (i0, i0 + 1), (i0 + 1, i0 + 2)]
            else:
                verts += [P(sg * hx, 0, J["hip"] - 0.03 * s), P(sg * hx, -0.006 * s, J["knee"] + 0.10 * s)]
                radii += [0.082 * k * B["hips"], 0.074 * k * LB]
                wts += [hip_w, {f"thigh_{sd}": 1.0}]
                edges += [(j0, i0), (i0, i0 + 1)]
        pants_ob = skin_object("Pants", verts, edges, radii, bcol, rig, wts)
        if tucked:
            flatten_above(pants_ob, (pel + 0.062 * s) * S)
        if LIMB47 == "B" and bottom == "pants":
            # v0.47: the trouser leg ends in a straight edge over the shoe (the chain's rounded end was a ball round the ankle)
            flatten_below(pants_ob, (J["ankle"] - 0.034 * s) * S)
    else:
        hem_z = J["knee"] + (0.05 if bottom == "skirt" else 0.03) * s - spec.get("hem_drop", 0.0) * s    # (v0.41 bench: a longer dress, TPDB_MEI41 C)
        verts = [P(0, 0, pel + 0.055 * s), P(0, 0, pel - 0.020 * s), P(0, 0.004 * s, hem_z)]
        radii = [(0.136 * k * B["waist"] * TI, 0.104 * k * dp * TI), (0.158 * k * B["hips"] * TI, 0.122 * k * dp * TI),
                 (0.205 * k * B["hips"], 0.165 * k * dp)]
        wts = [{"hips": 0.8, "spine": 0.2}, {"hips": 1.0}, {"hips": 0.4, "thigh_L": 0.3, "thigh_R": 0.3}]
        sk_edges = [(0, 1), (1, 2)]
        if MID39 in ("B", "C"):
            # one piece from the waist, flaring to the hem (A-line), and a hem edge: a ring just above the hem at nearly its width, the dome
            # below it flattened after baking (the bell's bottom was an egg, so the skirt read as "a bubble", and from behind as shorts)
            top_z = pel + (0.090 if bottom == "dress" else 0.060) * s
            verts = [P(0, 0, top_z), P(0, 0, pel - 0.020 * s), P(0, 0.004 * s, hem_z + 0.040 * s), P(0, 0.004 * s, hem_z)]
            radii = [(0.136 * k * B["waist"] * TI, 0.104 * k * dp * TI), (0.160 * k * B["hips"] * TI, 0.124 * k * dp * TI),
                     (0.200 * k * B["hips"], 0.160 * k * dp), (0.206 * k * B["hips"], 0.166 * k * dp)]
            wts = [{"hips": 0.6, "spine": 0.4}, {"hips": 1.0}, {"hips": 0.5, "thigh_L": 0.25, "thigh_R": 0.25}, {"hips": 0.4, "thigh_L": 0.3, "thigh_R": 0.3}]
            sk_edges = [(0, 1), (1, 2), (2, 3)]
        pants_ob = skin_object("Skirt", verts, sk_edges, radii, bcol, rig, wts)
        if MID39 in ("B", "C"):
            flatten_below(pants_ob, hem_z * S - 0.004 * S)
            if HEM47 in ("B", "C", "D"):
                reweight_skirt(pants_ob, hx * S, (pel - 0.020 * s) * S, hem_z * S, 0.166 * k * dp, HEM47)
            if bottom == "dress":
                no_isect(pants_ob)          # (the same cloth as the top above it: no line where they meet)
            if SEAT47 == "B":
                # v0.47 (TPDB_SEAT47): seated, the skirt is another object, a wrap of the two thighs. The bell keeps its depth, front to
                # back, as its height when the thighs swing forward: measured on a seated figure it stood 9 cm above the thighs and hung
                # 12 cm below them, and its flat hem was a wall the knees came out of ("knees pasted on top of the skirt", "a sack").
                # The wrap is as deep as a thigh and its cloth, goes with the thighs wholly from just below the hip, and ends at the
                # knee at the lowest (a longer skirt rides up to there when its wearer sits). build_cast shows it in the seated
                # postures and the bell in the rest.
                rt47 = 0.064 * k * LB + 0.014 * k
                hem_s = max(hem_z, J["knee"] + 0.020 * s)
                sv = [verts[0], verts[1], P(0, -0.006 * s, J["hip"] - 0.060 * s), P(0, -0.008 * s, hem_s + 0.040 * s), P(0, -0.008 * s, hem_s)]
                sr = [radii[0], radii[1], (hx * S + rt47 * 1.04, rt47 * 1.10), (hx * S + rt47, rt47), (hx * S + rt47, rt47)]
                sw = [wts[0], wts[1], {"hips": 0.2, "thigh_L": 0.4, "thigh_R": 0.4}, {"thigh_L": 0.5, "thigh_R": 0.5}, {"thigh_L": 0.5, "thigh_R": 0.5}]
                seat = skin_object("SkirtSeat", sv, [(0, 1), (1, 2), (2, 3), (3, 4)], sr, bcol, rig, sw)
                flatten_below(seat, hem_s * S - 0.004 * S)
                reweight_skirt(seat, hx * S, (J["hip"] + 0.030 * s) * S, hem_s * S, rt47, "S", z_full=(J["hip"] - 0.070 * s) * S)
                # (the hem's lid an object of its own, which draws a line where a knee comes out of it)
                open_end(seat, hem_s * S - 0.004 * S, rig, bcol, lid="SkirtSeatLid")
                if bottom == "dress":
                    no_isect(seat)
        # v0.15: the fabric over each thigh. The bell above hangs from the hips and cannot follow two legs, so
        # when a thigh swung forward (sitting, kicking, sliding) the leg below it came out of nowhere, a gap
        # between the hem and a floating leg. Each lobe runs from the hip joint past the top of the bare leg
        # and turns with its thigh; standing, both lie inside the bell, so the skirt looks as it did.
        lv, lr, lw, le = [], [], [], []
        f = 0.80
        for sd, sg in (("L", 1), ("R", -1)):
            i0 = len(lv)
            lx = sg * hx * 0.8      # a little inside the leg, so standing it stays clear of the hem's rounded edge
            # three nodes (two made a box that the smoothing shrank to a short blob), flatter front to back and tapering to
            # a thin end that overlaps the top of the bare leg; the lower nodes a little to the front, so a leg swung back
            # in a stride barely lifts the back of the skirt
            lv += [P(lx, 0, J["hip"]), P(lx, -0.012 * s, J["hip"] + (J["knee"] - J["hip"]) * f * 0.5),
                   P(lx, -0.020 * s, J["hip"] + (J["knee"] - J["hip"]) * f)]
            lr += [(0.080 * k * B["hips"], 0.064 * k * B["hips"]), (0.072 * k * B["hips"], 0.058 * k * B["hips"]),
                   (0.048 * k * B["hips"], 0.044 * k * B["hips"])]
            lw += [{f"thigh_{sd}": 0.7, "hips": 0.3}, {f"thigh_{sd}": 1.0}, {f"thigh_{sd}": 1.0}]
            le += [(i0, i0 + 1), (i0 + 1, i0 + 2)]
        lap = skin_object("SkirtLap", lv, le, lr, bcol, rig, lw)
        # no line where a lobe passes into the bell: in a stride the lobe's crossing drew an outlined patch on the skirt
        # ("a pocket, a fold, or a stain"); where it shows, it is the same cloth, bulging with the leg
        try:
            lap.lineart.usage = "NO_INTERSECTION"
        except AttributeError:
            pass
        if __import__("os").environ.get("TPDB_SEAT34", "O") == "P":
            # v0.34 bench: seated, the two lobes wrapped each thigh and left the gap between them, so the dress read as "a yellow top,
            # yellow shorts" on a woman taken for "a child". One flat ellipsoid over both thighs, from the hip to the knee, makes one cloth
            # across the lap; on the thigh's bone, it turns with the thighs as they swing forward together (rungs from thigh to thigh drew
            # seams, a stack of rolls on her knees). Shown only in the seated poses (build_cast hides it in the rest)
            zc = J["hip"] + (J["knee"] - J["hip"]) * 0.56
            panel = ellipsoid("SkirtPanel", P(0, -0.020 * s, zc),
                              (hx * 0.8 * S + 0.064 * k * B["hips"], 0.046 * k * B["hips"], (J["hip"] - J["knee"]) * S * 0.52), bcol, rig, "thigh_L")
            try:
                panel.lineart.usage = "NO_INTERSECTION"
            except AttributeError:
                pass
    if bare_legs:
        verts, radii, wts, edges = [], [], [], []
        for sd, sg in (("L", 1), ("R", -1)):
            i0 = len(verts)
            # v0.15: every bare leg runs down to the ankle joint, inside the shoe, so the foot never stands
            # apart from it
            top_z = J["knee"] + (0.14 if bottom == "shorts" else 0.10) * s
            if SHOE39 == "D" and FOOT42 == "B":
                # v0.42 (TPDB_FOOT42): the calf fuller and set back, the knee and the ankle narrower (an even tube, "pegs")
                zc = J["knee"] - 0.33 * (J["knee"] - J["ankle"])
                if LIMB47 == "B":
                    # v0.47: a fuller thigh end and calf, the calf further back, a slimmer ankle
                    verts += [P(sg * hx, -0.006 * s, top_z), P(sg * hx, -0.012 * s, J["knee"]), P(sg * hx, 0.018 * s, zc), P(sg * hx, 0, J["ankle"])]
                    radii += [0.064 * k * LB, 0.046 * k * LB, 0.060 * k * LB, 0.027 * k * LB]
                else:
                    verts += [P(sg * hx, -0.006 * s, top_z), P(sg * hx, -0.01 * s, J["knee"]), P(sg * hx, 0.012 * s, zc), P(sg * hx, 0, J["ankle"])]
                    radii += [0.058 * k * LB, 0.045 * k * LB, 0.058 * k * LB, 0.029 * k * LB]
                wts += [{f"thigh_{sd}": 1.0}, {f"thigh_{sd}": 0.5, f"shin_{sd}": 0.5}, {f"shin_{sd}": 1.0}, {f"shin_{sd}": 1.0}]
                edges += [(i0, i0 + 1), (i0 + 1, i0 + 2), (i0 + 2, i0 + 3)]
                continue
            if SHOE39 == "D":
                # a calf a third of the way down the shin and a narrow ankle, ending inside the shoe
                zc = J["knee"] - 0.35 * (J["knee"] - J["ankle"])
                verts += [P(sg * hx, -0.006 * s, top_z), P(sg * hx, -0.01 * s, J["knee"]), P(sg * hx, 0.004 * s, zc), P(sg * hx, 0, J["ankle"])]
                radii += [0.060 * k * LB, 0.050 * k * LB, 0.054 * k * LB, 0.032 * k * LB]
                wts += [{f"thigh_{sd}": 1.0}, {f"thigh_{sd}": 0.5, f"shin_{sd}": 0.5}, {f"shin_{sd}": 1.0}, {f"shin_{sd}": 1.0}]
                edges += [(i0, i0 + 1), (i0 + 1, i0 + 2), (i0 + 2, i0 + 3)]
                continue
            verts += [P(sg * hx, -0.006 * s, top_z), P(sg * hx, -0.01 * s, J["knee"]), P(sg * hx, 0, J["ankle"])]
            radii += [0.060 * k * LB, 0.050 * k * LB, 0.041 * k * LB]
            wts += [{f"thigh_{sd}": 1.0}, {f"thigh_{sd}": 0.5, f"shin_{sd}": 0.5}, {f"shin_{sd}": 1.0}]
            edges += [(i0, i0 + 1), (i0 + 1, i0 + 2)]
        skin_object("Legs", verts, edges, radii, spec["skin"], rig, wts)

    if __import__("os").environ.get("TPDB_DRESS", "B") == "B" and bottom == "dress" and MID39 not in ("B", "C"):
        # v0.27, chosen on the bench: a belt at the join (the top and the bell drawn as two lobes: "two pieces with a visible join or drawing seam at the waist")
        spec = dict(spec, belt="wood", buckle="sun")
        pants_ob = shirt
    if spec.get("belt") and bottom in ("pants", "shorts", "dress") and (bottom != "dress" or __import__("os").environ.get("TPDB_DRESS", "B") == "B") \
            and BELT39 == "B" and not (bottom == "dress" and MID39 in ("B", "C")):
        # v0.39 bench (TPDB_BELT39 "B"): a flat band on the waistband, bent with the trousers, at the natural waist where the shirt is tucked
        zb = (pel + ((0.052 if tucked else 0.024) if bottom != "dress" else 0.050) * s) * S
        ring_pts = surface_points(pants_ob)
        hh = 0.011 * k
        near = [q for q in ring_pts if abs(q.z - zb) < 0.014 * S] or ring_pts
        bw = max(abs(q.x) for q in near) + 0.002 * k
        bd = max(abs(q.y) for q in near) + 0.002 * k
        bm = bmesh.new()
        rows = []
        for zz in (zb - hh, zb + hh):
            rows.append([bm.verts.new(Vector((bw * math.cos(a), bd * math.sin(a), zz))) for a in [j / 64 * 2 * math.pi for j in range(64)]])
        for j in range(64):
            bm.faces.new((rows[0][j], rows[0][(j + 1) % 64], rows[1][(j + 1) % 64], rows[1][j]))
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
        bmesh.ops.solidify(bm, geom=bm.faces[:], thickness=0.004 * k)
        band = _mesh_object("Belt", bm, spec["belt"], smooth=True)
        upd()
        skin_like(band, pants_ob, rig, TORSO)
        front = -bd
        skin_like(ellipsoid("Buckle", Vector((0, front - 0.006 * k, zb)), (0.018 * k, 0.006 * k, 0.014 * k), spec.get("buckle", "sun"), rig, "hips"), pants_ob, rig, TORSO)
    elif spec.get("belt") and bottom in ("pants", "shorts", "dress") and (bottom != "dress" or __import__("os").environ.get("TPDB_DRESS", "B") == "B") \
            and not (bottom == "dress" and MID39 in ("B", "C")) and not (BELT42 == "B" and top == "tee" and not tucked):
        zb = (pel + (0.024 if bottom != "dress" else 0.050) * s) * S
        ring_pts = surface_points(pants_ob)
        band = [q for q in ring_pts if abs(q.z - zb) < 0.012 * S] or ring_pts
        bw = max(abs(q.x) for q in band) + 0.004 * k
        bd = max(abs(q.y) for q in band) + 0.004 * k
        ring = [Vector((bw * math.cos(a), bd * math.sin(a), zb)) for a in [i / 64 * 2 * math.pi for i in range(64)]]
        cu = tube("Belt", [tuple(r) for r in ring], 0.012 * k, spec["belt"], None, None)
        cu.data.splines[0].use_cyclic_u = True
        cu.data.bevel_depth = 0.011 * k
        upd()
        rig.attach(cu, "hips")
        ellipsoid("Buckle", Vector((0, -bd - 0.010 * k, zb)), (0.020 * k, 0.008 * k, 0.016 * k), spec.get("buckle", "sun"), rig, "hips")

    # --- skin: neck + forearms (+ upper arms for sleeveless) ---------------
    verts = [P(0, 0, nk - 0.05 * s), P(0, 0, J["head_base"] + 0.03 * s)]
    neck_r = (0.060 if kind == "child" else COLLAR46_NR) * (1.0 + 0.5 * (HS - 1) if NECK46 == "O" or HS > 1.0 else 1.0)
    if HEAD48 == "B" and kind == "child":
        neck_r *= 1.12
    radii = [neck_r * k * 1.1, neck_r * k]
    wts = [{"chest": 1.0}, {"neck": 0.5, "head": 0.5}]
    edges = [(0, 1)]
    if HEAD49 == "B" and (HSH.get("neck", 1.0) != 1.0 or HSH.get("neck_y")):
        # v0.49 (core.HEAD49): the neck keeps v0.48's width up to the collar and narrows from there to the jaw (HSH["neck"] of v0.48's
        # width), so the chin stands out past it on both sides; its top may be set back under the skull (HSH["neck_y"], in head radii)
        # (its foot, inside the top, is narrower: the rounded end of the wider one came to the cloth of a slim chest from behind, and Line
        # Art drew a dash of its rim on the front of the dress)
        verts = [verts[0], P(0, 0, nk + 0.030 * s), verts[1] + Vector((0, HSH.get("neck_y", 0.0) * hr, 0))]
        radii = [neck_r * k * 0.85, neck_r * k * 1.10, neck_r * k * HSH.get("neck", 1.0)]
        wts = [{"chest": 1.0}, {"chest": 0.5, "neck": 0.5}, {"neck": 0.5, "head": 0.5}]
        edges = [(0, 1), (1, 2)]
        if NECK49 == "B":
            # v0.49 (TPDB_NECK49): the neck is a part of its own, and Line Art keeps its intersections: the line where the neck passes into
            # the head is drawn whole in every view, and the head's own outline is cut exactly where it meets the neck. As a piece of
            # "Skin", which draws no intersections (ISECT39), the chin's line across the neck came out in dashes in some views
            skin_object("Neck", verts, edges, radii, spec["skin"], rig, wts)
            verts, radii, wts, edges = [], [], [], []
    if not long_sleeve:
        for sd in ("L", "R"):
            i0 = len(verts)
            start = sh[sd].lerp(el[sd], SLEEVE52_P["arm_f"] if SLEEVE52 != "O" else 0.38)
            if LIMB47 == "B":
                # v0.47: the upper arm narrows to the elbow, the forearm swells a little under it and narrows to the wrist
                verts += [start, el[sd], el[sd].lerp(wr[sd], 0.28), wr[sd], wr[sd] + Vector((0, 0, -0.040 * k))]
                radii += [0.051 * k * LA, 0.041 * k * LA, 0.044 * k * LA, 0.028 * k * LA, 0.022 * k * LA]
                wts += [{f"upper_arm_{sd}": 1.0}, {f"upper_arm_{sd}": 0.5, f"forearm_{sd}": 0.5}, {f"forearm_{sd}": 1.0}, {f"forearm_{sd}": 1.0}, {f"hand_{sd}": 1.0}]
                edges += [(i0, i0 + 1), (i0 + 1, i0 + 2), (i0 + 2, i0 + 3), (i0 + 3, i0 + 4)]
                continue
            verts += [start, el[sd], wr[sd]]
            radii += [0.049 * k * LA, 0.045 * k * LA, 0.038 * k * LA] if ARM46 == "B" else [0.046 * k * LA, 0.043 * k * LA, 0.037 * k * LA]
            wts += [{f"upper_arm_{sd}": 1.0}, {f"upper_arm_{sd}": 0.5, f"forearm_{sd}": 0.5}, {f"forearm_{sd}": 1.0}]
            edges += [(i0, i0 + 1), (i0 + 1, i0 + 2)]
            if CLEAN46 == "B":
                # v0.46: the forearm runs on, narrowing, to the middle of the hand. It ended at the wrist wider than the hand's top, and the
                # rim of that end was the line across every wrist
                verts.append(wr[sd] + Vector((0, 0, -0.040 * k))); radii.append(0.024 * k * LA); wts.append({f"hand_{sd}": 1.0})
                edges.append((i0 + 2, i0 + 3))
    else:
        for sd in ("L", "R"):
            i0 = len(verts)
            # (v0.52: the forearm begins well up inside the sleeve, so it passes whole through the cuff's lid)
            verts += [wr[sd] + (el[sd] - wr[sd]) * (SLEEVE52_P["stub_f"] if SLEEVE52 != "O" else 0.12), wr[sd]]
            radii += [0.040 * k * LA, 0.037 * k * LA] if LIMB47 != "B" else [0.033 * k * LA, 0.028 * k * LA]
            wts += [{f"forearm_{sd}": 1.0}, {f"forearm_{sd}": 1.0}]
            edges += [(i0, i0 + 1)]
            if CLEAN46 == "B":
                verts.append(wr[sd] + Vector((0, 0, -0.040 * k))); radii.append((0.022 if LIMB47 == "B" else 0.024) * k * LA); wts.append({f"hand_{sd}": 1.0})
                edges.append((i0 + 1, i0 + 2))
    if verts:
        skin_object("Skin", verts, edges, radii, spec["skin"], rig, wts)

    for sd, sg in (("L", 1), ("R", -1)):
        hcen = wr[sd] + Vector((0.002 * sg, 0, -0.042 * k))
        if HAND47 == "B":
            # v0.47: a mitten, longer than wide and wider than the wrist, flatter from the front; the thumb at its front inner edge, its
            # tip forward and down, clear of the palm
            hcen = wr[sd] + Vector((0.002 * sg, -0.004 * k, -0.050 * k))
            h46 = ellipsoid(f"Hand_{sd}", hcen, (0.032 * k, 0.040 * k, 0.056 * k), spec["skin"], rig, f"hand_{sd}")
            t46 = ellipsoid(f"Thumb_{sd}", hcen + Vector((-sg * 0.016 * k, -0.034 * k, 0.010 * k)), (0.013 * k, 0.014 * k, 0.030 * k),
                            spec["skin"], rig, f"hand_{sd}", rot=Quaternion((1, 0, 0), -0.55))
        else:
            h46 = ellipsoid(f"Hand_{sd}", hcen, (0.040 * k, 0.034 * k, 0.050 * k), spec["skin"], rig, f"hand_{sd}")
            t46 = ellipsoid(f"Thumb_{sd}", hcen + Vector((-sg * 0.012 * k, -0.030 * k, 0.012 * k)), (0.015 * k, 0.016 * k, 0.026 * k),
                            spec["skin"], rig, f"hand_{sd}", rot=Quaternion((1, 0, 0), 0.5))
        if CLEAN46 == "B":
            no_isect(h46)       # v0.46: no seam where the hand passes into the forearm (the thumb keeps its own line on the hand)
        if SHOE39 == "D":
            shoe39(f"Shoe_{sd}", P(sg * hx, 0, 0), s, k, S, spec["shoes"], rig, f"foot_{sd}")
        else:
            ellipsoid(f"Heel_{sd}", P(sg * hx, 0.010 * s, 0.040 * s), (0.050 * k, 0.060 * k, 0.040 * k), spec["shoes"], rig, f"foot_{sd}")
            ellipsoid(f"Toe_{sd}", P(sg * hx, -0.062 * s, 0.034 * s), (0.058 * k, 0.080 * k, 0.036 * k), spec["shoes"], rig, f"foot_{sd}")

    # --- head --------------------------------------------------------------
    ellipsoid("Head", hc, HR, spec["skin"], rig, "head", seg=56 if HEAD49 == "B" else 40, rings=40 if HEAD49 == "B" else 22, sq=HN,
              head={} if HEAD48 == "B" else None)
    for sd, sg in (("L", 1), ("R", -1)):
        if HEAD48 == "B" and HAIR48 == "B" and spec.get("hair") == "long":
            continue        # v0.48: long hair lies over the ears (an ear stood out through it like a knob)
        if HEAD48 == "B":
            # v0.48: on the egg head the ear sits on the side of the head at its own height, a little behind the middle
            ez = -0.030 * kh
            ezs = ez / HR[2]
            # (pair bench 3: "large and placed near the middle of the side of the head, so the head reads as seen from behind": smaller, a
            # little further back)
            ellipsoid(f"Ear_{sd}", hc + Vector((sg * HR[0] * head_f(ezs) * 0.985, 0.022 * kh - HR[1] * head_g(ezs), ez)),
                      (0.015 * kh, 0.021 * kh, 0.031 * kh), spec["skin"], rig, "head")
            continue
        ellipsoid(f"Ear_{sd}", hc + Vector((sg * HR[0] * 0.97, 0.005, -0.012 * kh)), (0.016 * kh, 0.026 * kh, 0.034 * kh), spec["skin"], rig, "head")
    face = Face(rig, "head", hc, HR, kh, n=HN)
    if FACE48 == "B" and spec.get("brow"):
        face.brow_k = spec["brow"]          # v0.48: (length, depth, weight) of this face's brows against the standard
    eye_dx, eye_z = 0.060 * kh, 0.010 * kh
    kf = kh
    if AF:
        # v0.43 (TPDB_ADULT43): the eyes and mouth smaller and set lower in the face (the girls' large eyes high in a round face)
        eye_dx, eye_z, kf = 0.056 * kh, -0.002 * kh, kh * 0.88
    # v0.47 (TPDB_HEAD47 "B"): the eyes a little nearer each other, so the far one stands clear of the outline in a three-quarter view
    eye_dx *= 0.92 if HEAD47 == "B" else 1.0
    if FACE48 == "B":
        # v0.48 (face.FACE48): one layout for every face, the eyes just under the middle of the taller head
        eye_dx, eye_z, kf = 0.052 * kh, -0.004 * kh, kh * (0.94 if AF else 1.0)
    if FACE48 == "B":
        nk = kh * (1.22 if HEAD_STYLE == "B" and spec.get("hair") == "bald_ring" else 1.0)
        nose = ellipsoid("Nose", face.at(0, eye_z - 0.046 * kh, 0.003 * kh), (0.020 * nk, 0.024 * nk, 0.018 * nk), spec["skin"], rig, "head")
    elif HEAD_STYLE == "B" and spec.get("hair") == "bald_ring":
        # v0.23 bench B: a fuller nose standing out from the face, so a profile shows which way the face is turned
        nose = ellipsoid("Nose", face.at(0, eye_z - 0.044 * kh, 0.010 * kh), (0.026 * kh, 0.030 * kh, 0.022 * kh), spec["skin"], rig, "head")
    elif NOSE47 in ("B", "C"):
        # v0.47: a little further out and longer front to back, so a turned head has a nose on its far cheek and a profile a nose at all
        nose = ellipsoid("Nose", face.at(0, eye_z - 0.042 * kh, 0.002 * kh), (0.019 * kh, 0.023 * kh, 0.017 * kh), spec["skin"], rig, "head")
    else:
        nose = ellipsoid("Nose", face.at(0, eye_z - 0.040 * kh, -0.004 * kh), (0.020 * kh, 0.018 * kh, 0.016 * kh), spec["skin"], rig, "head")
    if NOSE47 in ("B", "C"):
        no_isect(nose)          # no ring where it passes into the face: its own outline shows only where it stands clear of the face
    build_hair(spec, rig, hc, HR, kh)
    build_facial_hair(spec, rig, face, eye_z, kh)
    if PROF48 == "B" and spec.get("facial_hair"):
        # v0.48 (face.PROF48): the moustache a second time, round the cheek with the side view's mouth (pair bench 3, of the side view's
        # mouth round the cheek under a moustache left at the front: "a small brown smudge below the nose")
        face.xoff = -PROF48_MOUTH * kf
        build_facial_hair(spec, rig, face, eye_z, kh, pre="p_")
        face.xoff = 0.0
    build_hat(spec, rig, hc, HR, kh)
    if spec.get("backpack"):
        # v0.24 bench (TPDB_TEEN=B): a school backpack on the chest bone, with a pocket and two straps over the shoulders
        bz = (J["chest"] - 0.02) * S
        ellipsoid("Backpack", Vector((0, 0.185 * S, bz)), (0.125 * S, 0.075 * S, 0.175 * S), spec["backpack"], rig, "chest")
        ellipsoid("BackpackPocket", Vector((0, 0.255 * S, bz - 0.05 * S)), (0.085 * S, 0.028 * S, 0.075 * S), spec.get("backpack2", "charcoal"), rig, "chest")
        for sd, sg in (("L", 1), ("R", -1)):
            _blob_chain(f"BackpackStrap_{sd}", [Vector((sg * 0.10 * S, 0.13 * S, (J["sh_z"] + 0.02) * S)), Vector((sg * 0.105 * S, 0.0, (J["sh_z"] + 0.088) * S)),
                                                Vector((sg * 0.11 * S, -0.135 * S, J["sh_z"] * S)), Vector((sg * 0.125 * S, -0.150 * S, (J["chest"] - 0.06) * S)),
                                                Vector((sg * 0.165 * S, -0.065 * S, (J["chest"] - 0.14) * S))],
                        [(0.026 * S, 0.010 * S)] * 5, spec.get("backpack2", "charcoal"), rig, bone="chest")
    build_people_face(face, eye_dx, eye_z, kf, glasses=spec.get("glasses", False), skin_key=spec["skin"], mouth_col="red" if AF else None)
    if ISECT39 == "B":
        for ob in list(bpy.context.scene.objects):
            nm = ob.name.split(".")[0]
            if nm in ("Skin", "Legs", "Belt", "Buckle") or nm.startswith(("Heel_", "Toe_", "Shoe_", "Sole_", "Hand_", "Thumb_")):
                no_isect(ob)

    for sd, sg in (("L", 1), ("R", -1)):
        anchor(rig, f"hand_{sd}_grip", wr[sd] + Vector((0.004 * sg, -0.005, -0.045 * k)), f"hand_{sd}")
        anchor(rig, f"foot_{sd}", P(sg * hx, -0.045 * s, 0.0), f"foot_{sd}")
        anchor(rig, f"eye_{sd}", face.at(sg * eye_dx, eye_z), "head")
    mid = (face.at(eye_dx, eye_z) + face.at(-eye_dx, eye_z)) / 2
    anchor(rig, "gaze_target", mid + Vector((0, -1.0, 0)), "head")
    anchor(rig, "head_top", hc + Vector((0, 0, HR[2] + 0.02 * kh)), "head")
    anchor(rig, "seat", P(0, 0.02 * s, J["pelvis"] - 0.10 * s), "hips")
    anchor(rig, "mouth", face.at(0, eye_z + MOUTH_DZ * kf if FACE48 == "B" else eye_z - 0.080 * kh), "head")
    anchor(rig, "chest", P(0, -0.12 * s, J["chest"]), "spine")
    states = people_expression_states(face, eye_dx, eye_z, kf)
    states_p = people_expression_states(face, eye_dx, eye_z, kf, profile=True) if PROF48 == "B" else None

    ctx = PersonCtx()
    ctx.J, ctx.S, ctx.s, ctx.k, ctx.kh, ctx.HS = J, S, s, k, kh, HS
    ctx.hc, ctx.HR, ctx.face, ctx.eye_dx, ctx.eye_z = hc, HR, face, eye_dx, eye_z
    ctx.spec, ctx.kind = spec, kind
    ctx.states_profile = states_p
    rest_shade()        # v0.47 (TPDB_SHADE47): the trunk's cloth keeps its upright shading; the rig is at rest here
    return rig, states, ctx


def shoe39(name, ankle, s, k, S, matkey, rig, bone):
    """v0.39 bench (TPDB_SHOE39 "D"): a shoe in one piece, a sphere shaped to a small round heel, a toe reaching ahead of the leg (about 1.4
    times the heel's length), wider than the ankle at the ball and flat on the ground. ankle is the foot's ground point under the ankle."""
    f42 = FOOT42 == "B"
    if f42 and SHOE47 == "B":
        return shoe47(name, ankle, s, k, S, matkey, rig, bone)
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=18, radius=1.0)
    half_len, width, height = (0.108 if f42 else 0.098) * k, 0.058 * k, 0.040 * k
    cy, cz = (-0.062 if f42 else -0.052) * s * S, 0.038 * s * S
    sole = (0.010 if f42 else 0.003) * s * S
    for v in bm.verts:
        x, y, z = v.co
        back = max(0.0, y)                    # +y is behind the ankle
        front = max(0.0, -y)
        w = width * (1.0 - 0.22 * back)       # narrower at the heel
        h = height * (1.0 - (0.42 if f42 else 0.28) * front * front)   # lower at the toe (v0.42: flatter, a toe cap below the cuff from the front)
        v.co = Vector((ankle.x + x * w, ankle.y + cy + y * half_len, max(cz + z * h, sole)))
    ob = _mesh_object(name, bm, matkey)
    upd()
    rig.attach(ob, bone)
    if f42:
        # v0.42 (TPDB_FOOT42): a sole, the shoe's outline a little larger and 1 cm deep, grey under a dark shoe and charcoal under the rest (cream
        # read as a white disc under each shoe)
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=10, radius=1.0)
        for v in bm.verts:
            x, y, z = v.co
            back = max(0.0, y)
            w = width * (1.0 if SOLE45 == "A" else 1.04) * (1.0 - 0.22 * back)
            v.co = Vector((ankle.x + x * w, ankle.y + cy + y * half_len * (0.80 if SOLE45 == "A" else 1.03), 0.0052 * s * S + z * 0.0052 * s * S))
        dark = matkey in ("charcoal", "slate", "navy", "outline")
        so = _mesh_object(name.replace("Shoe", "Sole"), bm, "outline" if (SOLE45 == "A" and dark) else "gray" if dark else "charcoal")
        upd()
        rig.attach(so, bone)
        no_isect(so)
    return ob


def shoe47(name, ankle, s, k, S, matkey, rig, bone):
    """v0.47 (TPDB_SHOE47 "B"): the shoe a wedge. v0.42's was a dome, highest at its middle and round underneath but for a patch under the
    middle, on a sole plate shorter than itself ("flat ovals or paddles with no toe, sole, heel or ankle", "a detached sole line"). This one
    is highest round the ankle and falls along the instep to a rounded toe cap, its sides drop straight to a flat underside over nearly its
    whole length, and the dark sole under it is as long as that flat."""
    half_len, width, height = 0.108 * k, 0.056 * k, 0.040 * k
    cy, cz = -0.062 * s * S, 0.040 * s * S
    sole = 0.014 * s * S
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=18, radius=1.0)
    for v in bm.verts:
        x, y, z = v.co
        back = max(0.0, y)                    # +y is behind the ankle
        front = max(0.0, -y)
        r = min(1.0, max(0.0, (y + 0.50) / 0.95))
        r = r * r * (3 - 2 * r)
        w = width * (1.0 - 0.20 * back) * (1.0 - 0.10 * front * front)
        h = height * (0.66 + 0.90 * r) * (1.0 - 0.30 * front * front)
        zz = cz + z * h if z >= 0 else cz + z * height * 2.4
        v.co = Vector((ankle.x + x * w, ankle.y + cy + y * half_len, max(zz, sole)))
    ob = _mesh_object(name, bm, matkey)
    upd()
    rig.attach(ob, bone)
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=10, radius=1.0)
    for v in bm.verts:
        x, y, z = v.co
        back = max(0.0, y)
        front = max(0.0, -y)
        w = width * 0.99 * (1.0 - 0.20 * back) * (1.0 - 0.10 * front * front)
        zz = max(-1.0, min(1.0, z * 2.6))     # a slab: flat above and below, a rounded rim
        v.co = Vector((ankle.x + x * w, ankle.y + cy + y * half_len * 0.97, sole * 0.5 * (1.0 + zz)))
    dark = matkey in ("charcoal", "slate", "navy", "outline")
    so = _mesh_object(name.replace("Shoe", "Sole"), bm, "outline" if dark else "charcoal")
    upd()
    rig.attach(so, bone)
    no_isect(so)
    return ob


def reweight_skirt(ob, hxw, z_top, z_hem, ry, mode="B", z_full=None):
    """v0.47 (TPDB_HEM47): give the baked skirt's lower part to the thighs. From the hip line (z_top) down to the hem (z_hem) the thighs'
    share of a vertex grows to nearly all of it, split between the two thighs by the vertex's side (hxw is the hip joint's offset), the
    middle shared by both. A stride then carries the cloth with each leg and the hem stays one line; seated, the cloth lies along the
    thighs. "C": the back of the skirt keeps more of the hips (it hangs behind a seated figure and is not lifted by a leg swung back);
    "D": the same with a smaller share. "S" (the seated wrap): the whole share, reached at z_full, not at the hem."""
    share = {"B": 0.87, "C": 0.87, "D": 0.70, "S": 1.0}[mode]
    backk = {"B": 1.0, "C": 0.45, "D": 0.45, "S": 1.0}[mode]
    z_full = z_hem if z_full is None else z_full
    groups = {g.name: g for g in ob.vertex_groups}
    for nm in ("hips", "thigh_L", "thigh_R"):
        if nm not in groups:
            groups[nm] = ob.vertex_groups.new(name=nm)
    for v in ob.data.vertices:
        if v.co.z >= z_top:
            continue
        t = min(1.0, (z_top - v.co.z) / max(1e-6, z_top - z_full))
        t = t * t * (3 - 2 * t)
        u = max(-1.0, min(1.0, v.co.x / hxw))
        side = 0.5 + 0.5 * u * (1.5 - 0.5 * u * u)
        fb = max(0.0, min(1.0, 0.5 - v.co.y / (2 * ry)))       # 1 at the front, 0 at the back
        th = share * t * (backk + (1 - backk) * fb)
        for g in ob.vertex_groups:
            try:
                g.remove([v.index])
            except RuntimeError:
                pass
        if th * side > 1e-4:
            groups["thigh_L"].add([v.index], th * side, "REPLACE")
        if th * (1 - side) > 1e-4:
            groups["thigh_R"].add([v.index], th * (1 - side), "REPLACE")
        groups["hips"].add([v.index], 1 - th, "REPLACE")
    ob.data.update()
    return ob


# ------------------------------------------------------------------ hair
def _shell(name, hc, HR, extra, keep, matkey, rig, k, thick=0.012, subsurf=1):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=44, v_segments=24, radius=1.0)
    doomed = [vv for vv in bm.verts if not keep(vv.co)]
    bmesh.ops.delete(bm, geom=doomed, context="VERTS")
    for vv in bm.verts:
        q = squircle(vv.co, HN)
        if HEAD48 == "B":
            q = head_pt(q)
        vv.co = Vector((q.x * (HR[0] + extra), q.y * (HR[1] + extra), q.z * (HR[2] + extra)))
    bmesh.ops.solidify(bm, geom=bm.faces[:], thickness=thick * k)
    ob = _mesh_object(name, bm, matkey)
    ob.location = hc
    if subsurf:
        sub = ob.modifiers.new("Subsurf", "SUBSURF")
        sub.levels = sub.render_levels = subsurf
    upd()
    rig.attach(ob, "head")
    return ob


def _face_window(c, top=0.46, chin=-0.45):
    """True where hair may grow: not the face window (front, below the hairline) and not under the chin."""
    if c.y < -0.35 and c.z < top:
        return False
    if c.z < chin and c.y < 0.3:
        return False
    return True


def _blob_chain(name, pts, radii, matkey, rig, bone="head"):
    me = bpy.data.meshes.new(name)
    me.from_pydata([tuple(p) for p in pts], [(i, i + 1) for i in range(len(pts) - 1)], [])
    ob = link(bpy.data.objects.new(name, me))
    ob.modifiers.new("Skin", "SKIN").use_smooth_shade = True
    for i, r in enumerate(radii):
        me.skin_vertices[0].data[i].radius = r
    me.skin_vertices[0].data[0].use_root = True
    sub = ob.modifiers.new("Subsurf", "SUBSURF")
    sub.levels = sub.render_levels = 2
    ob.data.materials.append(mat(matkey))
    for p in ob.data.polygons:
        p.use_smooth = True
    upd()
    rig.attach(ob, bone)
    return ob


BOB_SIDE_FRONT = 0.30
BOB_HAIRLINE = 0.60
# v0.19: no curls over the front half of the head below the hairline (curls on the cheeks hid a profile's face: a boy's
# head looked "almost seen from behind while the body is side-on"; a kicker's face "faces left ... as if kicking backward")
CURLY_FRONT = 0.0
CURLY_HAIRLINE = 0.55
CURLY_SIDE_BACK = 0.10
CURLY_TEMPLE = 0.30


# v0.48 (TPDB_HAIR48; vision/isolation_v048.md): hair with a drawn hairline. Until v0.47 every head of hair was a shell of the ball cut where a
# grid's points passed a test: a level fringe straight across the brow and a square corner at each temple, a bowl on every head. "B": the
# shell is cut along the zero line of a smooth field (core.cut_field), so a hairline is a curve: higher over the middle of the brow or at a
# parting, rounding down into the temple, a short sideburn in front of the ear and the ear left clear on a short cut, the hair a little
# fuller toward the crown. "O": v0.47's hair
HAIR48 = __import__("os").environ.get("TPDB_HAIR48", "B")


def _smin(a, b, r=0.10):
    return 0.5 * (a + b - math.sqrt((a - b) ** 2 + r * r))


def _sstep(a, b, x):
    t = max(0.0, min(1.0, (x - a) / (b - a)))
    return t * t * (3 - 2 * t)


def _bump(x, c, w):
    t = max(0.0, 1.0 - abs(x - c) / w)
    return t * t * (3 - 2 * t)


def _hair_field(top, y_front, low, r=0.10):
    """Where there is no hair (positive): in front of the line y = -y_front below the hairline top(x), and below the lower edge low(y)."""
    def f(c):
        return -_smin(-_smin(-c.y - y_front, top(c.x) - c.z, r), c.z - low(c.y), 0.06)
    return f


def _shell48(name, hc, HR, extra, field, matkey, rig, k, thick=0.012, subsurf=1, crown=0.0, seg=64, rings=40):
    """A shell of the head cut along the zero line of field (a number for each point of the unit ball; the positive side goes)."""
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=rings, radius=1.0)
    cut_field(bm, {vv: field(vv.co) for vv in bm.verts})
    for vv in bm.verts:
        c = vv.co.copy()
        q = head_pt(squircle(c, HN))
        up = extra + crown * max(0.0, c.z) ** 1.5
        vv.co = Vector((q.x * (HR[0] + up), q.y * (HR[1] + up), q.z * (HR[2] + up)))
    bmesh.ops.solidify(bm, geom=bm.faces[:], thickness=thick * k)
    ob = _mesh_object(name, bm, matkey)
    ob.location = hc
    if subsurf:
        sub = ob.modifiers.new("Subsurf", "SUBSURF")
        sub.levels = sub.render_levels = subsurf
    upd()
    rig.attach(ob, "head")
    return ob


def build_hair48(spec, rig, hc, HR, k):
    """v0.48: the styles drawn with a hairline. Returns False for a style it does not draw (build_hair then draws v0.47's)."""
    style, col = spec["hair"], spec["hair_col"]
    hcx = hc + Vector((0, 0.006 * k, 0.010 * k))
    part = spec.get("part", "side")
    if style == "short":
        # a short cut with a parting: the hairline a little higher on the parting's side, rounding down into the temples; a short sideburn in
        # front of the ear; the ear clear; behind the ear down to the nape
        sgn = -1.0 if spec.get("part_side", "L") == "L" else 1.0

        def top(x):
            return 0.58 + sgn * 0.08 * x - 0.14 * x * x

        def low(y):
            return 0.10 - 0.26 * _bump(y, -0.20, 0.16) - 0.62 * _sstep(0.18, 0.50, y)
        _shell48("Hair", hcx, HR, 0.012 * k, _hair_field(top, 0.38, low), col, rig, k, thick=0.014, crown=0.012 * k)
        return True
    if style in ("long", "ponytail", "bun", "low_bun", "shoulder"):
        if part == "center":
            def top(x):
                return 0.80 - 0.64 * math.sqrt(x * x + 0.006)
        else:
            sgn = -1.0 if spec.get("part_side", "L") == "L" else 1.0

            def top(x):
                # swept from a parting on one side: high at the parting, lower across the brow to the other temple
                return 0.60 + sgn * 0.22 * x - 0.22 * x * x
        if style in ("long", "shoulder"):
            def low(y):
                return -0.70 if y < 0.35 else -2.0
            # (0.50 at first: seen from the side the hair lay over the cheek to the eye's corner, "no visible face" as v0.18's readers had
            # it of the bob; the side panels stop short of the cheek)
            yf = 0.40
        else:
            # drawn back: the ear clear, the hair behind it down to the nape
            def low(y):
                return 0.06 - 0.60 * _sstep(0.16, 0.48, y)
            yf = 0.40
        _shell48("Hair", hcx, HR, 0.014 * k, _hair_field(top, yf, low), col, rig, k, thick=0.016, crown=0.012 * k)
        return True
    if style == "puffs":
        # parted in the middle and drawn up into the two puffs: the ear clear
        def top(x):
            return 0.74 - 0.46 * math.sqrt(x * x + 0.006)

        def low(y):
            return 0.08 - 0.58 * _sstep(0.16, 0.48, y)
        _shell48("Hair", hcx, HR, 0.012 * k, _hair_field(top, 0.40, low), col, rig, k, thick=0.014, crown=0.010 * k)
        return True
    if style == "buzz":
        # cropped close: a rounded hairline, squared a little at the temples, the ear clear
        def top(x):
            return 0.56 - 0.20 * x * x

        def low(y):
            return 0.12 - 0.16 * _bump(y, -0.18, 0.14) - 0.52 * _sstep(0.18, 0.48, y)
        _shell48("Hair", hc + Vector((0, 0.004 * k, 0.006 * k)), HR, 0.004 * k, _hair_field(top, 0.36, low, r=0.07), col, rig, k, thick=0.008)
        return True
    if style == "curly":
        # the cap under the curls: a rounded hairline, the cheek clear in a side view (v0.19)
        def top(x):
            return 0.54 - 0.12 * x * x

        def low(y):
            return 0.16 - 0.60 * _sstep(0.14, 0.46, y)
        _shell48("Hair", hcx, HR, 0.012 * k, _hair_field(top, 0.30, low), col, rig, k, thick=0.014)
        return True
    return False


SHOULDER53 = dict(y=(0.060, 0.080, 0.072), z=-0.215, w=(0.150, 0.172, 0.165), d=(0.095, 0.090, 0.066))
SHOULDER53.update(__import__("json").loads(__import__("os").environ.get("TPDB_SHOULDER53_P", "{}")))


def build_hair(spec, rig, hc, HR, k):
    style, col = spec["hair"], spec["hair_col"]
    off = Vector((0, 0.006 * k, 0.012 * k))
    hcx = hc + off
    if HAIR48 == "B" and HEAD48 == "B" and build_hair48(spec, rig, hc, HR, k):
        pass
    elif style in ("short", "long", "bun", "ponytail", "puffs", "low_bun", "shoulder") and spec.get("sideburns"):
        # v0.39 bench (TPDB_BEN39): short hair with sideburns, a strip forward of each ear down to the cheekbone, and a side part
        def keep39(c):
            if abs(c.x) > 0.74 and -0.58 < c.y < -0.20 and -0.20 < c.z < 0.50:
                return True
            return _face_window(c, 0.46)
        _shell("Hair", hcx, HR, 0.012 * k, keep39, col, rig, k)
    elif style in ("short", "long", "bun", "ponytail", "puffs", "low_bun", "shoulder"):
        _shell("Hair", hcx, HR, 0.012 * k, lambda c: _face_window(c, 0.46), col, rig, k)
    elif style == "curly":
        # (v0.19: below the temples the hair stays behind the ear, so a profile shows the cheek; covering the side of the
        # head, the curly boy in profile "could be looking away ... or be seen from behind at an angle")
        _shell("Hair", hcx, HR, 0.012 * k, lambda c: _face_window(c, 0.50) and (c.y > CURLY_SIDE_BACK or c.z > CURLY_TEMPLE), col, rig, k)
    elif style == "bob":
        # (v0.18: the side panels stop short of the cheek, so a profile shows the face; covering it, the woman in profile
        # read as having "no visible face; head is a round dark shape")
        _shell("Hair", hcx, HR, 0.016 * k, lambda c: (abs(c.x) > 0.62 and c.z > -0.62 and c.y > BOB_SIDE_FRONT) or _face_window(c, BOB_HAIRLINE, -0.30), col, rig, k, thick=0.018)
    elif style == "buzz":
        _shell("Hair", hc + Vector((0, 0.004 * k, 0.006 * k)), HR, 0.004 * k, lambda c: _face_window(c, 0.52, -0.2) and c.z > -0.25, col, rig, k, thick=0.008)
    elif style == "bald_ring":
        # a fringe of hair round the back of the head, from the nape up to the hat line, with a short
        # tuft above each ear and a scalloped lower edge: a crescent of hair, not a band (a narrow
        # band at ear height read as headphones or a bandage)
        def fringe(c):
            # behind the ears only (hair over the ear read as an earmuff or a pad), from the hat line
            # down to the nape, with a scalloped lower edge
            a = math.atan2(c.x, c.y)
            if HEAD_STYLE in ("A", "B"):
                # v0.23 bench: a narrower crescent kept to the back of the head, behind the ear and above the nape (in
                # profile the wide grey patch behind the ear read as "a beard" or "a face mask" on a face turned the
                # other way)
                low = -0.55 + 0.05 * math.sin(a * 9.0)
                back = 0.42 - 0.10 * max(0.0, c.z)
                return c.y > back and low < c.z < 0.22
            low = -0.82 + 0.06 * math.sin(a * 9.0)
            back = 0.16 - 0.10 * max(0.0, c.z)          # the front edge leans back toward the crown
            return c.y > back and low < c.z < 0.24
        _shell("Hair", hc + Vector((0, 0.008 * k, -0.002 * k)), HR, 0.007 * k, fringe, col, rig, k, thick=0.012)
    if style == "long":
        _blob_chain("HairBack", [hc + Vector((0, 0.07 * k, 0.05 * k)), hc + Vector((0, 0.10 * k, -0.12 * k)), hc + Vector((0, 0.08 * k, -0.30 * k))],
                    [(0.15 * k, 0.09 * k), (0.15 * k, 0.07 * k), (0.12 * k, 0.04 * k)], col, rig)
    if style == "shoulder":
        # v0.53 (specs.ANA53): cut to the shoulders and full: a fall as wide as the head behind the neck, wider at its foot, which shows on
        # both sides of the neck from the front and as a mass behind it from the side (the long hair is one narrow fall down the back)
        q53 = SHOULDER53
        _blob_chain("HairBack", [hc + Vector((0, q53["y"][0] * k, 0.04 * k)), hc + Vector((0, q53["y"][1] * k, -0.10 * k)), hc + Vector((0, q53["y"][2] * k, q53["z"] * k))],
                    [(q53["w"][0] * k, q53["d"][0] * k), (q53["w"][1] * k, q53["d"][1] * k), (q53["w"][2] * k, q53["d"][2] * k)], col, rig)
    if style == "bun":
        if HAIR48 == "B" and HEAD48 == "B":
            # (pair bench 3: "the bun on top is very small and hard to see, so the hair could read as a cap or helmet")
            ellipsoid("Bun", hc + Vector((0, 0.085 * k, HR[2] * 0.96)), (0.076 * k, 0.070 * k, 0.064 * k), col, rig, "head")
        else:
            ellipsoid("Bun", hc + Vector((0, 0.07 * k, HR[2] * 0.92)), (0.062 * k, 0.058 * k, 0.055 * k), col, rig, "head")
    if style == "low_bun":
        # v0.42 (TPDB_MEI42): the hair drawn back from the face and tied in a bun at the nape (a bun on top stood "like a topknot", v0.41)
        ellipsoid("Bun", hc + Vector((0, HR[1] * 1.02, -0.035 * k)), (0.060 * k, 0.050 * k, 0.052 * k), col, rig, "head")
    if style == "ponytail":
        _blob_chain("Ponytail", [hc + Vector((0, HR[1] * 0.92, 0.07 * k)), hc + Vector((0, HR[1] * 1.25, -0.02 * k)),
                                 hc + Vector((0, HR[1] * 1.20, -0.17 * k))],
                    [(0.045 * k, 0.040 * k), (0.050 * k, 0.045 * k), (0.030 * k, 0.026 * k)], col, rig)
        ellipsoid("Tie", hc + Vector((0, HR[1] * 0.98, 0.07 * k)), (0.030 * k, 0.020 * k, 0.030 * k), spec.get("tie", "red"), rig, "head")
    if style == "puffs":
        for sg in (1, -1):
            ellipsoid(f"Puff{'L' if sg > 0 else 'R'}", hc + Vector((sg * HR[0] * 0.80, 0.03 * k, HR[2] * 0.62)),
                      (0.070 * k, 0.064 * k, 0.066 * k), col, rig, "head")
    if style == "curly":
        rnd = random.Random(7)
        for i in range(26):
            th = rnd.uniform(0, 2 * math.pi)
            ph = rnd.uniform(0.15, 1.25)
            d = Vector((math.cos(th) * math.sin(ph), math.sin(th) * math.sin(ph), math.cos(ph)))
            if d.y < CURLY_FRONT and d.z < CURLY_HAIRLINE:
                continue
            if d.y < CURLY_SIDE_BACK and d.z < CURLY_TEMPLE:
                continue
            d = squircle(d, HN)
            if HEAD48 == "B":
                d = head_pt(d)
            ellipsoid(f"Curl{i}", hc + Vector((d.x * HR[0], d.y * HR[1], d.z * HR[2])) * 1.0 + d * 0.012 * k,
                      (0.042 * k,) * 3, col, rig, "head", seg=12, rings=8)


# v0.49 (TPDB_MOUSTACHE49 "B"; flaws_v048.md O1): v0.48's short, thin moustache was named by the screen's readers in none of its wearers'
# seventeen pictures, for ten of fifteen with v0.47's ("very large and curled", "slightly comic" to a reviewer of enlarged figures). "B": between
# the two, a fifth wider and a quarter thicker than v0.48's, its ends a little lower, still clear of the mouth. "O": v0.48's
MOUSTACHE49 = __import__("os").environ.get("TPDB_MOUSTACHE49", "B")


def build_facial_hair(spec, rig, face, eye_z, k, pre=""):
    """pre "p_" (v0.48, face.PROF48): only the moustache's curve, a second time, for the side view's face (face.xoff set by the caller)."""
    col = spec.get("facial_hair_col", spec["hair_col"])
    fh = spec.get("facial_hair")
    if not fh:
        return
    mz = eye_z + (MOUTH_DZ if FACE48 == "B" else -0.080) * k
    if fh == "mustache" and MOUSTACHE47 == "B":
        # v0.47 (TPDB_MOUSTACHE47): see the switch
        w, z0, zt = 0.064 * k, mz + 0.021 * k, mz + 0.007 * k
        if FACE48 == "B":
            # v0.48 (pair bench 1: "very large and curled, sitting over an open red mouth; slightly comic", "long drooping moustache crosses
            # the lower face and partly covers the mouth"): shorter, its ends level with the mouth's corners and not below them
            # (pair bench 2: "no mouth under the moustache, so the face is a little blank": higher, under the nose, and lighter)
            w, z0, zt = 0.046 * k, mz + 0.031 * k, mz + 0.022 * k
            if MOUSTACHE49 == "B":
                w, zt = 0.056 * k, mz + 0.016 * k
        m51 = spec.get("moust51", 1.0)          # v0.51 (specs.MOUST51)
        w *= m51
        half = [(0.0, z0), (0.25 * w, z0 + 0.0015 * k), (0.50 * w, z0), (0.78 * w, z0 - 0.45 * (z0 - zt)), (w, zt)]
        pts = [(-x, z) for x, z in reversed(half[1:])] + half
        dense = [(q.x, q.z) for q in smooth_curve([(x, 0.0, z) for x, z in pts], n=6)]
        dark = {"hair_brown": "hair_brown_dark"}.get(col, col)
        ob = face.curve_on(pre + "mustache36", dense, ((0.0116 if MOUSTACHE49 == "B" else 0.0092) if FACE48 == "B" else 0.0125) * k * m51, dark, 0.006 * k)
        n, nip, full = len(dense) - 1, 0.5, 0.28
        for i, q in enumerate(ob.data.splines[0].points):
            t = abs(i / n - 0.5) * 2
            q.radius = nip + (1.0 - nip) * t / full if t < full else 1.0 - 0.78 * ((t - full) / (1.0 - full)) ** 1.5
        ob.name = "FH_" + pre + "mustache36"
    elif fh == "mustache" and __import__("os").environ.get("TPDB_MOUSTACHE36", "M") == "M":
        # v0.36: chosen on the bench (vision/isolation_v036.md; TPDB_MOUSTACHE36=O builds v0.35's). A bold white moustache, wider and thicker and standing off the skin, an age cue that a hat cannot cover (the
        # thin one did not show at scene size, and under the bucket the grandfather was "a boy")
        pts = [(-0.050 * k, mz - 0.002 * k), (-0.030 * k, mz + 0.016 * k), (-0.010 * k, mz + 0.022 * k), (0, mz + 0.020 * k),
               (0.010 * k, mz + 0.022 * k), (0.030 * k, mz + 0.016 * k), (0.050 * k, mz - 0.002 * k)]
        rad, out = 0.019 * k, 0.020 * k
        if __import__("os").environ.get("TPDB_MOUSTACHE36_FLAT", "F") == "F":
            # v0.36, chosen in the bench's second round (TPDB_MOUSTACHE36_FLAT=O builds round 1's): slimmer and lying on the skin, a little higher, so that in profile it does not stand out from the
            # face like something held in the mouth (two bench readers: "a pipe, cigar or whistle")
            pts = [(x, z + 0.006 * k) for x, z in pts]
            rad, out = 0.015 * k, 0.006 * k
        if MOUSTACHE46 in ("B", "C"):
            # v0.46: the same moustache through five times the points, so that it follows the face (between seven points it cut under the
            # skin and came out again, a notched edge), and thinning to its two ends (it ended as thick as its middle: in profile "a dark
            # brown blob", "a moustache, or dirt"). "B" thins from the middle on, to 0.38 of its thickness; "C" keeps its thickness over
            # most of its length and rounds off only the ends, to 0.70
            dense = [(q.x, q.z) for q in smooth_curve([(x, 0.0, z) for x, z in pts], n=6)]
            ob = face.curve_on(pre + "mustache36", dense, rad, col, out)
            n = len(dense) - 1
            taper, power = (0.62, 1.6) if MOUSTACHE46 == "B" else (0.30, 2.6)
            for i, q in enumerate(ob.data.splines[0].points):
                t = abs(i / n - 0.5) * 2
                q.radius = 1.0 - taper * t ** power
        else:
            ob = face.curve_on(pre + "mustache36", pts, rad, col, out)
        ob.name = "FH_" + pre + "mustache36"
    elif fh == "beard" and HAIR48 == "B" and HEAD48 == "B":
        pass        # v0.48: the beard below is drawn round the mouth and is its own moustache
    elif fh in ("mustache", "beard") and not pre:
        pts = [(-0.034 * k, mz + 0.006 * k), (-0.016 * k, mz + 0.020 * k), (0, mz + 0.018 * k), (0.016 * k, mz + 0.020 * k), (0.034 * k, mz + 0.006 * k)]
        ob = face.curve_on("mustache", pts, 0.0105 * k, col, 0.010 * k)
        ob.name = "FH_mustache"
    if fh == "beard" and pre and not (HAIR48 == "B" and HEAD48 == "B"):
        return
    if fh == "beard":
        ax, ay, az = face.ax, face.ay, face.az
        mzr = (mz - 0.016 * k) / az

        def keep(c):
            if c.y > 0.35:
                return False
            if __import__("os").environ.get("TPDB_BEARD", "D") == "D":
                # v0.28 bench: a goatee, on the chin alone, joined to the moustache
                return c.z < mzr and c.z > -0.98 and abs(c.x) < 0.46 and c.y < 0.2
            if c.z < mzr and c.z > -0.98:
                return True
            if __import__("os").environ.get("TPDB_BEARD", "D") == "C":
                # v0.28: fuller on the cheek, still short of the ear ("a thin dark strap along the jaw", "it could look like a chin strap")
                return abs(c.x) > 0.44 and -0.9 < c.z < -0.30 and c.y < 0.05
            if __import__("os").environ.get("TPDB_BEARD", "D") == "B":
                # v0.27: stopping short of the ear, so hair and beard do not join in one shape ("a chin strap, helmet strap or face mask", "a dark face covering or mask",
                # now that the turned head shows it; "hair and beard merge into one dark shape")
                return abs(c.x) > 0.60 and -0.9 < c.z < -0.34 and c.y < 0.05
            return abs(c.x) > 0.60 and -0.9 < c.z < 0.02 and c.y < 0.25
        if HAIR48 == "B" and HEAD48 == "B":
            # v0.48: a short full beard: from the sideburn along the jaw and under the mouth, its upper edge a curve that leaves the cheeks and
            # the lower lip clear (v0.28's goatee was a cap on the chin's underside: on the egg head "a strap")
            # (first trial: a full beard from the sideburns round the jaw. With cropped hair of its own colour it closed the face in a dark
            # ring, a hood or a mask, as v0.27's readers had it: "a chin strap, helmet strap or face mask".) A moustache and a chin beard in
            # one piece round the mouth, the mouth in an opening of it, the cheeks and the jaw's sides clear
            # (second trial: a moustache and chin beard in one piece with an opening for the mouth: a square patch.) A chin beard whose
            # upper edge is a curve under the lower lip, rising to the mouth's corners, where the moustache's ends come down to it
            # (third trial, pair bench 1: a chin beard and a moustache in the hair's own dark colour were, turned, "a larger dark mass that runs
            # from the mouth into the cheek, reading more like a smudge or shadow than facial hair".) A short full beard as a tone: a shade
            # darker than the skin, with no line round it, from the sideburn along the jaw and under the lower lip, and a moustache of the
            # same tone; the mouth's line stays clear between them
            # (fourth trial, pair bench 2: as a tone with no line it was "a soft darker-brown patch on the cheek and jaw with no edge, so it
            # reads more like a shadow or dirt than a beard", and v0.47's small dark one "reads as a beard".) A chin beard in the hair's own
            # colour with its line, rounded, under the lower lip and round the chin, the cheeks clear; and a short moustache over the mouth
            # that does not come down to it, so the mouth shows between the two
            mzs = mz / az

            def nobeard(c):
                up = mzs - 0.125 + 0.16 * min(1.0, abs(c.x) / 0.34) ** 2
                return -_smin(_smin(up - c.z, 0.36 - abs(c.x), 0.12), 0.20 - c.y, 0.10)

            def nobeard50(c):
                # v0.50 (specs.AGE50 "M"): fuller, wider along the jaw and standing off the chin, so that it changes the chin's outline
                # (in the hair's colour on dark skin the v0.48 beard was named in none of its wearer's 25 v0.49 pictures)
                up = mzs - 0.110 + 0.22 * min(1.0, abs(c.x) / 0.50) ** 2
                return -_smin(_smin(up - c.z, 0.52 - abs(c.x), 0.12), 0.26 - c.y, 0.10)
            if not pre and spec.get("beard50"):
                _shell48("Beard", face.c, (ax, ay, az), 0.012 * k, nobeard50, col, rig, k, thick=0.016)
            elif not pre:
                _shell48("Beard", face.c, (ax, ay, az), 0.003 * k, nobeard, col, rig, k, thick=0.010)
            w, z0 = 0.040 * k, mz + 0.030 * k
            half = [(0.0, z0), (0.30 * w, z0 + 0.002 * k), (0.62 * w, z0 - 0.001 * k), (0.86 * w, z0 - 0.005 * k), (w, z0 - 0.010 * k)]
            pts = [(-x, z) for x, z in reversed(half[1:])] + half
            dense = [(q.x, q.z) for q in smooth_curve([(x, 0.0, z) for x, z in pts], n=6)]
            ob = face.curve_on(pre + "mustache36", dense, 0.0088 * k, col, 0.004 * k)
            ob.lineart.usage = "EXCLUDE"
            n = len(dense) - 1
            for i, q in enumerate(ob.data.splines[0].points):
                t = abs(i / n - 0.5) * 2
                q.radius = 0.62 + 0.38 * min(1.0, t / 0.3) if t < 0.3 else 1.0 - 0.45 * ((t - 0.3) / 0.7) ** 1.5
            ob.name = "FH_" + pre + "mustache36"
        else:
            _shell("Beard", face.c, (ax, ay, az), 0.004 * k, keep, col, rig, k, thick=0.020)


def build_hat(spec, rig, hc, HR, k):
    hat = spec.get("hat")
    if not hat:
        return
    col = spec.get("hat_col", "blue")
    R = (HR[0] + 0.020 * k, HR[1] + 0.020 * k, HR[2] + 0.020 * k)
    dome_c = hc + Vector((0, 0.004 * k, 0.020 * k))
    # the dome sits above the brows at the front and lower at the back
    _shell("HatDome", dome_c, R, 0.0, lambda c: c.z > 0.56 - 0.34 * (c.y + 1) / 2, col, rig, k, thick=0.010, subsurf=1)
    if hat == "cap" and spec.get("brim_short"):
        # v0.26 bench (TPDB_OLD=C): a short peak tipped up, so it does not sit over the eye in profile
        ellipsoid("HatBrim", hc + Vector((0, -R[1] * 0.92, R[2] * 0.66)), (0.105 * k, 0.060 * k, 0.011 * k), col, rig, "head",
                  rot=Quaternion((1, 0, 0), 0.10))
        ellipsoid("HatButton", dome_c + Vector((0, 0, R[2] * 1.0)), (0.012 * k,) * 3, col, rig, "head")
    elif hat == "cap":
        ellipsoid("HatBrim", hc + Vector((0, -R[1] * 0.88, R[2] * 0.56)), (0.110 * k, 0.095 * k, 0.012 * k), col, rig, "head",
                  rot=Quaternion((1, 0, 0), -0.12))
        ellipsoid("HatButton", dome_c + Vector((0, 0, R[2] * 1.0)), (0.012 * k,) * 3, col, rig, "head")
    elif hat == "cap_back":
        # v0.24 bench (TPDB_TEEN=A): a cap worn backwards, the brim over the nape
        ellipsoid("HatBrim", hc + Vector((0, R[1] * 0.90, R[2] * 0.44)), (0.105 * k, 0.095 * k, 0.012 * k), col, rig, "head",
                  rot=Quaternion((1, 0, 0), -0.30))
        ellipsoid("HatButton", dome_c + Vector((0, 0, R[2] * 1.0)), (0.012 * k,) * 3, col, rig, "head")
    elif hat == "sun":
        ellipsoid("HatBrim", hc + Vector((0, 0.004 * k, R[2] * 0.52)), (R[0] * 1.85, R[1] * 1.85, 0.012 * k), col, rig, "head")
        ellipsoid("HatBand", hc + Vector((0, 0.004 * k, R[2] * 0.62)), (R[0] * 0.90, R[1] * 0.90, 0.022 * k), spec.get("band_col", "red"), rig, "head")
    elif hat == "beanie":
        ellipsoid("HatBand", hc + Vector((0, 0.004 * k, R[2] * 0.56)), (R[0] * 0.98, R[1] * 0.98, 0.036 * k), col, rig, "head")
        ellipsoid("HatPom", dome_c + Vector((0, 0, R[2] * 1.0)), (0.030 * k,) * 3, spec.get("band_col", "cream"), rig, "head")
