"""Animals: a parameterized quadruped (dogs, cats, goat) and birds (songbirds, duck)."""
import json
import math
import os

import bpy  # noqa: F401
import bmesh
from mathutils import Matrix, Quaternion, Vector

from .core import ISECT39, Frame, Rig, _mesh_object, anchor, box, cyl, ellipsoid, link, list_m, mat, no_isect, nrm, shell_over, skin_like, skin_object, upd

QUAD39 = os.environ.get("TPDB_QUAD39", "B")  # v0.39 bench (vision/isolation_v039.md): B
ART39 = os.environ.get("TPDB_ART39", "B")  # v0.39 bench (vision/isolation_v039.md): B
# v0.42 bench (TPDB_GOAT42; figure-fixes-v041.md item 1, vision/flaws_v041.md O4): the goat out of place in seven v0.41 pictures and once "a sheep".
# "B": a long wedge head (a smaller cranium and a face chain running down to the muzzle; the sphere's side ear read as an eye socket in profile),
# leaf ears out and back from the poll, a neck chain from the withers into the back of the head (at 135 the head floated), the back a fifth longer
# and level on shorter legs (hunched, short in the back), split hooves in dark grey, a pointed beard. "C": B with a collar, for a tether. "O": v0.41
GOAT42 = os.environ.get("TPDB_GOAT42", "C")  # v0.42 bench (vision/isolation_v042.md): C
# v0.42 bench (TPDB_DOG42; figure-fixes-v041.md item 4): at three-quarters the tan dog's chest patch read "like a bib or a nappy", the spotted dog's
# white legs stood like stilts and its far legs lost their outline, and the heads were balls. "B": the patch a narrow blaze down the chest that
# ends above the belly (none on the spotted coat, white on white), the far legs a step darker, a brown patch on the spotted dog's near foreleg,
# and the muzzle longer with a level top, the skull a little flatter, so the stop shows at 45. "O": v0.41
DOG42 = os.environ.get("TPDB_DOG42", "B")  # v0.42 bench (vision/isolation_v042.md): B
# v0.42 bench (TPDB_BEG42; figure-fixes-v041.md item 5, flaws_v041.md O2): the begging dog at 90 "upright", "kneeling", "human-like", and the
# reading dog's hind legs stretched out in front "like a person sitting". "B": begging on the haunches, the rump on the ground, the hocks flat
# and the hind paws forward under the body, the stifles up, the trunk upright and shorter and rounder (tipped back, it stretched into a tall
# tube; built on the dog's sit, it stood on its hind legs); the reading dog's hind legs folded, the paws flat beside the rump. "O": v0.41
BEG42 = os.environ.get("TPDB_BEG42", "B")  # v0.42 bench (vision/isolation_v042.md): B
# v0.42 bench (TPDB_CAT42; figure-fixes-v041.md item 7, flaws_v041.md O5): the stalking cat's legs "bunched" or "tangled" at 45 on every v0.41
# bench cut-out, knobs at the joints in the walk, and the head large for the body. "B": the head a tenth smaller, the legs' radii blended, and
# the stalk's stride spread with the near legs outside the far ones; "C": the far legs outside. "O": v0.41
CAT42 = os.environ.get("TPDB_CAT42", "O")  # v0.42 bench (vision/isolation_v042.md): O, the legs tangled either way
# v0.43 bench (TPDB_DOG43; figure-fixes-v042.md items 5 and 6): the dogs' legs "long, stiff and tube-like" and the spotted dog's hind legs "pasted onto
# the body" on the v0.42 bench, its far legs pale and floating; the begging dog's nose "almost straight up", once "howling". "B": the legs a tenth
# shorter and tapered, thick at the shoulder and narrow at the paw; the hind leg's thigh drawn as part of the body, the leg leaving it above the
# stifle; a brown patch over the spotted dog's near hip; the far legs a step darker again. "O": v0.42. (The begging head lowered, the nose up at
# about 35 degrees, was tried and left: at 45 the gaze check refused it on every spot of 12 street seeds, the face turned to the viewer, as
# v0.41's leaning beg had been; tpdb_work/begp43.sh)
DOG43 = os.environ.get("TPDB_DOG43", "B")  # v0.43 bench (vision/isolation_v043.md): B
# v0.43 bench (TPDB_GOAT43; figure-fixes-v042.md item 4): grazing at 45 and 135 "the back is high and hunched"; the beard twice unseen ("a ram or
# horned sheep"); the horns stacked segments, "springs or screws"; standing, the neck straight up, "a little llama-like". "B": grazing with the
# withers raised, the hips a little lower and the hind feet further back, the neck bent down from the withers and the front knees a little bent;
# the beard larger and grey (specs.py); each horn one smooth tapered curve; standing, the neck forward at about 35 degrees. "C": B with v0.42's
# graze (bench round 1: B's grazing legs "cramped", "folded under the chest"). "O": v0.42
GOAT43 = os.environ.get("TPDB_GOAT43", "C")  # v0.43 bench (vision/isolation_v043.md): C
# v0.43 bench (TPDB_READ43; figure-fixes-v042.md item 2, vision/flaws_v042.md R2): the reading dog's paper "stands upright on its own" in three v0.42
# descriptions, the shorter trunk's paws reaching only its edge. "A": lying down like a sphinx, the head bowed over the forepaws, which rest on a
# paper laid open on the ground ("down_read"); "B": sitting as v0.42, the head bowed toward the page and the forepaws lower, on the top of a paper
# whose foot rests on the ground (the paper is the scene's, templates.READ43). "O": v0.42
READ43 = os.environ.get("TPDB_READ43", "A")  # v0.43 bench (vision/isolation_v043.md): A
# v0.44 bench (TPDB_READ44; figure-fixes-v043.md item 1, figure-review-v043.md item 7, vision/flaws_v043.md R1): lying over a paper on the ground the
# reading dog was "lying on an open newspaper" in four of five v0.43 pictures and "apparently tearing it up" in the fifth; sitting up (v0.42) it read
# 0.917, but looked straight ahead past the paper. "A": sitting up as v0.42, both forepaws raised to the paper's top edge (the scene hangs the paper
# from them, templates.READ44), the head bowed about 20 degrees toward the page and turned a little to the viewer, so the face still shows (bowed
# right over it in v0.26 it was "a monkey, an otter, or a person in a costume"); a "read" expression, the eyes in round reading glasses. "O": v0.43
READ44 = os.environ.get("TPDB_READ44", "A")  # v0.44 bench (vision/isolation_v044.md): A
# v0.44 bench (TPDB_CAT44; figure-review-v043.md item 3): in profile the cat's ears are wedges seen edge on and its whiskers point at the viewer, so the
# head is a plain ball (v0.39 "cat or small black dog"); revision 41 draws the stalking cat only in profile. "A": each ear turned about 40 degrees
# about the vertical and a little taller, so its triangle shows at 90 and 45; the muzzle lobes larger and further forward; the whiskers angled
# forward as well as out, so they reach past the head's outline in profile. "O": v0.43
CAT44 = os.environ.get("TPDB_CAT44", "A")  # v0.44 bench (vision/isolation_v044.md): A
# v0.44 bench (TPDB_GOAT44; figure-review-v043.md item 25): grazing, the beard "sticks out as a hard grey wedge", a tusk or a spike. "A": a shorter,
# blunt tuft angled back toward the throat, so it hangs nearly straight down when the head is lowered to graze. "O": v0.43
GOAT44 = os.environ.get("TPDB_GOAT44", "A")  # v0.44 bench (vision/isolation_v044.md): A
# v0.44 bench (TPDB_NOSE44; figure-review-v043.md item 16): at 90 the tan dog's black nose and the happy tongue stand off the muzzle, "a black dot and a
# red dot in front of the muzzle" that could be a ball, a fly or the lead's end. "A": the nose set back into the muzzle's end, the tongue rooted in
# the mouth. "O": v0.43
NOSE44 = os.environ.get("TPDB_NOSE44", "A")  # v0.44 (vision/isolation_v044.md; read in the design tests): A
# v0.47 bench (TPDB_ANIM47; the cast study, two reviews of the animals as v0.46 drew them): "A black crescent sits on the front edge of the head", "a
# dark smudge cut off at the front edge of the head" (the eye, 27 degrees round the head, seen edge on in a side view), a songbird ("Two eyes are drawn
# side by side on a head in side view"), brown patches ("each patch is a separately outlined blob that bulges beyond the body outline"), the cat's whiskers "a black bristle
# block", the white dog's far legs grey, the tail a straight stick. "B": the eyes of the dogs and cats 44 degrees round the head, a full eye inside
# the outline in a side view and one eye at three-quarters; a songbird one pair, 50 degrees round, and no second pair on the side; the duck's 48;
# a coat's markings patches of the body's own surface (core.shell_over), flat on it and drawn with no line of their own, and none on a leg; a
# white coat's far legs a light shade; the dog's tail shorter, tapered to its tip and curved; the cat's whiskers two thin lines a side with no
# outline; the paws shorter and higher. "O": v0.46
ANIM47 = os.environ.get("TPDB_ANIM47", "B")
# v0.47 bench (TPDB_READ47; vision/flaws_v046.md R1): the reading dog held its paws up beside its muzzle and the scene hung a flat paper from them, so
# the paper lay against the mouth: "A brown dog sits up holding a newspaper in its mouth." (picture 53). "B": a pose of its own, sit_read: sitting
# up on the haunches as the begging dog does, the forelegs bent and held out at chest height, an open newspaper (an object of the pose, two pages
# in a shallow V with ruled bands, turned to the viewer) held by its lower corners below the muzzle and clear of the head, the head tipped down
# to it and turned a little to the viewer. "O": v0.46 (the pose is not built)
# Bench round 1 (vision/isolation_v047/round1): it reads, a dog reading a newspaper, in three crops of three, and three readers name the collar:
# "could be a collar, a bandana/scarf, or a cape; it sticks out behind the neck like a flap" (the collar is a ring fitted to the standing neck, and
# sitting upright the neck is thinner and straight, so the ring stands out behind it); one, the lower body "a rounded lump with bent hind legs and
# no clear tail" (the tail curled round the near haunch). "C": as B, the tail out behind on the ground with its tip up, as the v0.44 sitting-up
# pose has it, and no collar in this pose (the standing collar is hidden; a narrow band of its own round the upright neck was tried on the cast
# bench, and the bowed head hides all of it but the back, a small flap again). "B": round 1
# Bench round 2 (vision/isolation_v047/round2): it reads in three crops of three again, and all three readers name the hindquarters: "the lower
# body looks like a blob without clearly separate hind legs/feet" (iso_01), "the hind legs are not clearly drawn, so it is unclear whether it is
# standing or sitting" (iso_05) (the hind paws lay under the rump, behind the outline of the haunch). "D": as C, the hind paws wider apart and
# forward of the rump, so the near thigh, the shank lying along the ground and a hind foot flat on the ground ahead of the rump all show, the far
# foot behind it (further forward still, the legs stuck out in front as a sitting person's do; v0.42). "C": round 2
# Bench round 3 (vision/isolation_v047/round3, figs3): a dog reading a newspaper in three crops of three, the hindquarters named by no one, and
# the pair goes to it; but all three readers now offer another animal beside the dog: "almost like a weasel or otter when it sits up" (iso_02),
# "more like a meerkat" (iso_06), "the tail is long and curled like a weasel's" (iso_09) (none did in round 1, with the collar and the tail
# curled in; one in round 2). "E": as D, with a collar of its own in this pose, a flat band in the collar's colour low on the neck, fitted to
# the measured section of the upright body there (wide from side to side and thin from front to back, so a round ring on the neck's bone, which
# runs up the back of it, showed only behind: the flaps of rounds 1 and "C"), and the tail raised behind the rump with its tip curled up, as a
# sitting dog carries it, not laid out long on the ground (a trunk deeper from front to back changed little: the near foreleg and the paper
# cover its front; cast bench, vision/isolation_v047.md). "D": round 3
# Bench round 4 (vision/isolation_v047/round4, figs4): a dog reading a newspaper in three crops of three, "a red collar" named in each and no
# other animal offered by any reader. The pair against round 3's drawing: "No difference.", the band seen from the side "like a strap, not a
# ring" (it stops at the far paw). E is kept.
READ47 = os.environ.get("TPDB_READ47", "E")
# v0.47 bench (TPDB_HOSE47; vision/flaws_v046.md R4): the dog on the hose stood square, the hose along the line of its feet and pinched under a back
# paw amid its legs: "The dog may be standing on the hose or just in front of it." (picture 96). "B": a pose of its own, stand_hose: standing, the
# near forepaw set a step out ahead of the chest and planted (the scene lays the hose under it), with a point of its own on the ground under that
# paw, hose_paw. "O": v0.46 (the pose is not built)
# Bench round 1 (vision/isolation_v047/round1): the paw on the hose is seen, but the stride makes it a dog passing by: "walks over the hose" (two
# crops), "stepping over or onto the hose". "D": standing still and square, the legs upright under the body in pairs, the near forepaw only a
# little ahead of the far one and flat on the hose, the head turned a little to the viewer. "B": round 1
HOSE47 = os.environ.get("TPDB_HOSE47", "D")
# v0.47 bench (TPDB_PECK47; vision/flaws_v046.md R5, R6): the pecking songbird's beak came half-way down its legs, the face 40 degrees below level:
# "perched right beside it, looking ready to steal it" (picture 53), and the stalked bird read as standing, not feeding (48). "B": the body tipped
# further about the feet, the neck down, the face about 66 degrees below level so the beak's tip is at the ground ahead of the feet, the tail level,
# the legs apart fore and aft. "O": v0.46
# Bench round 1 (vision/isolation_v047/figs1, the red bird pecking): the action is clearer but "a's eye sits on the outline at the bottom of the
# head" (the eye is on the side of the face, so a face tipped 66 degrees carries it down to the head's lower edge). "C": the body tipped 40
# degrees and the neck 74 below level, the face 46, so the eye stays inside the head, and the whole bird lowered on legs spread wider fore and
# aft, so the beak's tip comes as near the ground as it did (with the angles alone it stood half as far again above it; tipped enough to reach,
# 48 to 54 degrees, the eye was back on the outline). "B": round 1
# Bench round 2 (vision/isolation_v047/round2, figs2): in the scene it reads, three crops of three, with "it could be read as pecking at the
# sandwich or as lying flat or crouched on the bench" (iso_04); as a drawing both birds lose to v0.46's: "a looks like it is falling forward on
# stubs" (fig_01), "b's odd splayed back leg and crushed front leg make the pose confusing" (fig_03). A body tipped about the feet drops its
# hips, so its legs must splay or sink into it. "D": the body tipped 58 degrees about the hips, which stay at their standing height, so the legs
# stand upright under it and clear of the belly; the neck 84 degrees below level and the face 46, the eye inside the head, the beak's tip near
# the ground ahead of the feet (tipped 62 and more the belly comes down round the legs; the legs staggered fore and aft made a narrow V with
# crossing feet; a face past 48 degrees put the eye back on the outline: cast bench, vision/isolation_v047.md). "C": round 2
PECK47 = os.environ.get("TPDB_PECK47", "D")
# v0.47 bench round 1 (TPDB_STALK47; vision/isolation_v047/round1 and whole1): every reader of the stalking cat, in the v0.46 drawing as in the new
# one, names its forelegs: "they seem folded up against its chest, with a paw bent near its chin, instead of reaching down to the floor", "its
# front legs are tucked oddly under the body" (the near forepaw was lifted to the height of the chest with its elbow pointed down and back). "B":
# the far foreleg down to the ground under the chest, the near one reaching forward with its paw a little off the ground mid-step, the elbows up
# beside the chest (pointed back and low, the forelegs lay along the ground with a knot at the elbow), the chest a little higher. "O": v0.46
# Bench round 2 (vision/isolation_v047/round2): stalking in three crops of three, and all three name the legs: "The cat's legs are tangled and
# hard to read" (iso_09), "its legs overlap in a tangled way" (iso_15) (the far forepaw lay back across the near foreleg, and the two hind paws
# one on the other). "C": the four paws apart along the ground, the far foreleg down under the chest and the near one reaching forward, mid-step;
# the far hind paw under the belly and the near one a step behind it, so each leg shows whole and the far ones show between the near ones, the
# crouch (the chest low, the head low and level, the tail low) as it was. "B": round 2
STALK47 = os.environ.get("TPDB_STALK47", "C")


def _frame_quat(d, side):
    """v0.42: the rotation that lays an ellipsoid's long (x) axis along d with its flat (z) face turned toward the side (+x or -x)."""
    xl = Vector(d).normalized()
    s = Vector((side, 0, 0))
    zl = (s - xl * s.dot(xl)).normalized()
    yl = zl.cross(xl)
    return Matrix((xl, yl, zl)).transposed().to_quaternion()


def far_mat(key, f=0.80):
    """v0.39 (TPDB_QUAD39): a copy of a palette material that the renderer's cel shading darkens by f (render_assets.to_cel), for the far legs."""
    m = mat(key).copy()
    m.name = key + "_far"
    m["tpdb_far"] = f
    return m
from .face import Face
from .people import surface_points


# ================================================================== quadrupeds
def build_quadruped(spec):
    kind = spec["kind"]
    S = spec.get("scale", 1.0)
    LH = spec.get("legs", 1.0)

    Q, ART = QUAD39 == "B", ART39 == "B"
    G42 = kind == "goat" and GOAT42 in ("B", "C") and Q and ART
    G43 = G42 and GOAT43 in ("B", "C")
    D43 = kind == "dog" and DOG43 == "B" and Q and ART
    if D43:
        LH *= 0.90       # v0.43 (TPDB_DOG43): the legs a tenth shorter
    FARF = (0.58 if D43 else 0.68) if (DOG42 == "B" and kind == "dog") else 0.80
    A47 = ANIM47 == "B" and Q and ART
    if A47 and spec.get("leg_col", spec["body"]) in ("white", "cream"):
        FARF = max(FARF, 0.80)      # v0.47 (TPDB_ANIM47): a white coat's far legs a light shade (at 0.58 they were grey, "metal legs")
    yb = 0.07 if G42 else 0.0       # v0.42: the goat's back a fifth longer, everything behind the chest moved back by up to yb

    def P(x, y, z):
        if yb and y > -0.16:
            y = y + yb * min(1.0, (y + 0.16) / 0.36)
        return Vector((x * S, y * S, z * S))

    root = link(bpy.data.objects.new("ROOT", None))
    hip_z, chest_z, knee_z = 0.44 * LH, 0.46 * LH, 0.24 * LH
    if G42:
        hip_z = chest_z      # (a level back: the withers stood above the rump, "hunched")
    if ART and kind == "cat":
        # (a cat's back rises toward the hips: the hind legs are longer than the front)
        hip_z, chest_z = 0.47 * LH, 0.43 * LH
    hx = (0.088 if kind in ("dog", "goat") else 0.080) if Q else 0.075     # a wider stance, so the legs separate at three-quarters
    neck_tail = P(0, -0.30, chest_z + 0.24) if (ART and kind == "goat") else P(0, -0.25, chest_z + 0.15)
    bones = {
        "hips": (P(0, 0.20, hip_z), P(0, 0.20, hip_z + 0.06), None),
        "spine": (P(0, 0.20, hip_z), P(0, -0.16, chest_z), "hips"),
        "neck": (P(0, -0.16, chest_z), neck_tail, "spine"),
        "head": (neck_tail, neck_tail + P(0, 0, 0.25), "neck"),
        "tail1": (P(0, 0.27, hip_z + 0.04), P(0, 0.38, hip_z + 0.14), "hips"),
        "tail2": (P(0, 0.38, hip_z + 0.14), P(0, 0.46, hip_z + 0.31) if (ART and kind == "cat") else P(0, 0.44, hip_z + 0.27), "tail1"),
    }
    for sd, sg in (("L", 1), ("R", -1)):
        bones.update({
            f"fleg_{sd}": (P(sg * hx, -0.15, chest_z - 0.06), P(sg * hx, -0.15, knee_z), "spine"),
            f"fshin_{sd}": (P(sg * hx, -0.15, knee_z), P(sg * hx, -0.16, 0.04), f"fleg_{sd}"),
        })
        if Q:
            # three bones: thigh forward to the stifle, gaskin back to the hock, cannon down to the paw (two made "table legs")
            bones.update({
                f"bleg_{sd}": (P(sg * hx, 0.20, hip_z - 0.04), P(sg * hx, 0.15, 0.27 * LH), "hips"),
                f"bshin_{sd}": (P(sg * hx, 0.15, 0.27 * LH), P(sg * hx, 0.27, 0.13 * LH), f"bleg_{sd}"),
                f"bmeta_{sd}": (P(sg * hx, 0.27, 0.13 * LH), P(sg * hx, 0.24, 0.04), f"bshin_{sd}"),
            })
        else:
            bones.update({
                f"bleg_{sd}": (P(sg * hx, 0.20, hip_z - 0.04), P(sg * hx, 0.25, knee_z), "hips"),
                f"bshin_{sd}": (P(sg * hx, 0.25, knee_z), P(sg * hx, 0.21, 0.04), f"bleg_{sd}"),
            })
    rig = Rig(root, bones)
    paw_bone = "bmeta" if Q else "bshin"
    body, belly, acc = spec["body"], spec.get("belly", spec["body"]), spec.get("accent", spec["body"])
    k = S
    G = spec.get("girth", 1.0)

    verts = [P(0, 0.22, hip_z), P(0, -0.15, chest_z), P(0, -0.24, chest_z + 0.12),
             P(0, 0.097, hip_z + 0.007), P(0, -0.027, hip_z + 0.013)]
    radii = [(0.115 * k * G, 0.12 * k * G), (0.125 * k * G, 0.12 * k * G), (0.07 * k, 0.07 * k),
             (0.118 * k * G, 0.12 * k * G), (0.122 * k * G, 0.12 * k * G)]
    wts = [{"hips": 1.0}, {"spine": 1.0}, {"neck": 1.0}, {"hips": 0.67, "spine": 0.33}, {"hips": 0.33, "spine": 0.67}]
    edges = [(0, 3), (3, 4), (4, 1), (1, 2)]
    LR = spec.get("leg_r", 1.0)
    if ART and kind == "dog":
        # a deep chest and a tuck-up belly line, a visible shoulder and haunch
        radii[1] = (0.128 * k * G, 0.140 * k * G)
        radii[4] = (0.110 * k * G, 0.106 * k * G)
        radii[3] = (0.106 * k * G, 0.110 * k * G)
    if ART and kind == "goat":
        # boxy, a straight back and a deep barrel
        radii[1] = (0.130 * k * G, 0.142 * k * G)
        radii[4] = (0.130 * k * G, 0.140 * k * G)
        radii[3] = (0.128 * k * G, 0.138 * k * G)
        radii[0] = (0.122 * k * G, 0.130 * k * G)
    if ART and kind == "cat":
        # slender
        radii = [(r[0] * 0.88, r[1] * 0.90) if isinstance(r, tuple) else r for r in radii]
    if G42:
        # v0.42: an even barrel, so the top line runs level from the withers to the rump, and the neck's root low in front of the withers (it rose
        # from the top of the chest and made a hump)
        radii[1] = (0.128 * k * G, 0.134 * k * G)
        radii[4] = (0.126 * k * G, 0.132 * k * G)
        radii[3] = (0.125 * k * G, 0.131 * k * G)
        radii[0] = (0.122 * k * G, 0.128 * k * G)
        verts[2] = P(0, -0.25, chest_z + 0.06)
        radii[2] = (0.082 * k, 0.082 * k)
    if Q:
        legv = {"L": [], "R": []}
        for sd, sg in (("L", 1), ("R", -1)):
            fr = (0.058, 0.044, 0.034, 0.033) if not (ART and kind == "goat") else (0.054, 0.036, 0.026, 0.026)
            hr_ = (0.095, 0.062, 0.040, 0.036) if not (ART and kind == "goat") else (0.090, 0.056, 0.030, 0.027)
            if ART and kind == "cat" and CAT42 in ("B", "C"):
                # v0.42: an even taper, so a bent joint does not bulge into a knob
                fr, hr_ = (0.043, 0.036, 0.031, 0.030), (0.068, 0.049, 0.036, 0.031)
            elif ART and kind == "cat":
                fr, hr_ = (0.048, 0.038, 0.030, 0.030), (0.082, 0.054, 0.034, 0.031)
            if D43:
                # v0.43 (TPDB_DOG43): tapered, thick at the shoulder and narrow at the paw; the hind leg's top inside the thigh the body now draws
                fr, hr_ = (0.064, 0.043, 0.031, 0.028), (0.052, 0.058, 0.036, 0.029)
            lv = [P(sg * hx, -0.15, chest_z - 0.07), P(sg * hx, -0.15, knee_z), P(sg * hx, -0.155, 0.10 * LH), P(sg * hx, -0.16, 0.035),
                  P(sg * hx, 0.20, hip_z - 0.05), P(sg * hx, 0.15, 0.27 * LH), P(sg * hx, 0.27, 0.13 * LH), P(sg * hx, 0.24, 0.035)]
            if ART and kind == "goat" and spec.get("leg_col", body) != body:
                # the white legs start under the brown body
                lv[0], lv[4] = P(sg * hx, -0.15, chest_z - 0.11), P(sg * hx, 0.19, hip_z - 0.10)
                fr, hr_ = (0.044,) + fr[1:], (0.054,) + hr_[1:]
            if D43:
                lv[4] = P(sg * hx, 0.172, 0.34 * LH)
            lr = [r * k * LR for r in fr + hr_]
            lw = [{"spine": 0.4, f"fleg_{sd}": 0.6}, {f"fleg_{sd}": 0.5, f"fshin_{sd}": 0.5}, {f"fshin_{sd}": 1.0}, {f"fshin_{sd}": 1.0},
                  {"hips": 0.4, f"bleg_{sd}": 0.6}, {f"bleg_{sd}": 0.5, f"bshin_{sd}": 0.5}, {f"bshin_{sd}": 0.5, f"bmeta_{sd}": 0.5}, {f"bmeta_{sd}": 1.0}]
            legv[sd] = (lv, lr, lw)
    if Q:
        # stubs of the four legs' tops in the body chain, so the body keeps the hull it had (without them the hips closed in a flat face)
        for sd, sg in (("L", 1), ("R", -1)):
            i0 = len(verts)
            verts += [P(sg * hx, -0.15, chest_z - 0.07), P(sg * hx, 0.20, hip_z - 0.05)]
            # (inside the legs' tops; the goat's larger ones bulged out of its barrel and split the body in two lumps)
            radii += [0.048 * k * LR, 0.072 * k * LR]
            wts += [{"spine": 0.4, f"fleg_{sd}": 0.6}, {"hips": 0.4, f"bleg_{sd}": 0.6}]
            edges += [(1, i0), (0, i0 + 1)]
            if D43:
                # v0.43 (TPDB_DOG43): the thigh part of the body, down to just above the stifle, so the haunch runs into the leg with no seam
                verts += [P(sg * hx, 0.168, 0.31 * LH)]
                radii += [0.064 * k * LR]
                wts += [{"hips": 0.15, f"bleg_{sd}": 0.85}]
                edges += [(i0 + 1, i0 + 2)]
    for sd, sg in ((("L", 1), ("R", -1)) if not Q else ()):
        i0 = len(verts)
        verts += [P(sg * 0.075, -0.15, chest_z - 0.07), P(sg * 0.075, -0.15, knee_z), P(sg * 0.075, -0.16, 0.035)]
        radii += [0.058 * k * LR, 0.046 * k * LR, 0.040 * k * LR]
        wts += [{"spine": 0.4, f"fleg_{sd}": 0.6}, {f"fleg_{sd}": 0.5, f"fshin_{sd}": 0.5}, {f"fshin_{sd}": 1.0}]
        edges += [(1, i0), (i0, i0 + 1), (i0 + 1, i0 + 2)]
        i0 = len(verts)
        verts += [P(sg * 0.075, 0.20, hip_z - 0.05), P(sg * 0.075, 0.25, knee_z), P(sg * 0.075, 0.21, 0.035)]
        radii += [0.070 * k * LR, 0.046 * k * LR, 0.040 * k * LR]
        wts += [{"hips": 0.4, f"bleg_{sd}": 0.6}, {f"bleg_{sd}": 0.5, f"bshin_{sd}": 0.5}, {f"bshin_{sd}": 1.0}]
        edges += [(0, i0), (i0, i0 + 1), (i0 + 1, i0 + 2)]
    if G42:
        # v0.42: a neck of two more nodes from the withers into the back of the head, tapering, so the head never stands apart from the body
        i0 = len(verts)
        verts += [P(0, -0.285, chest_z + 0.150), P(0, -0.315, chest_z + 0.240)]
        radii += [(0.066 * k, 0.068 * k), (0.054 * k, 0.056 * k)]
        wts += [{"neck": 1.0}, {"neck": 0.35, "head": 0.65}]
        edges += [(2, i0), (i0, i0 + 1)]
    elif kind == "goat":
        # a proper neck up to the head (the goat's head sits high on long legs)
        i0 = len(verts)
        verts += [P(0, -0.27, chest_z + 0.20)]
        radii += [(0.060 * k, 0.062 * k)]
        wts += [{"neck": 0.5, "head": 0.5}]
        edges += [(2, i0)]
    tail = spec.get("tail", kind)
    i0 = len(verts)
    if tail == "goat":
        verts += [P(0, 0.30, hip_z + 0.06), P(0, 0.33, hip_z + 0.13)]
        radii += [0.030 * k, 0.020 * k]
        wts += [{"tail1": 1.0}, {"tail1": 1.0}]
        edges += [(0, i0), (i0, i0 + 1)]
    else:
        tr = {"dog": (0.030, 0.026, 0.018), "cat": (0.026, 0.022, 0.020), "curl": (0.034, 0.030, 0.026)}[tail]
        if A47 and tail == "dog":
            # v0.47 (TPDB_ANIM47): a fifth shorter, tapered to its tip and curved up (a straight stick as long as a leg, "an antenna")
            verts += [P(0, 0.30, hip_z + 0.06), P(0, 0.375, hip_z + 0.125), P(0, 0.420, hip_z + 0.195), P(0, 0.432, hip_z + 0.250)]
            radii += [0.031 * k, 0.025 * k, 0.018 * k, 0.011 * k]
            wts += [{"tail1": 1.0}, {"tail1": 0.5, "tail2": 0.5}, {"tail2": 1.0}, {"tail2": 1.0}]
            edges += [(0, i0), (i0, i0 + 1), (i0 + 1, i0 + 2), (i0 + 2, i0 + 3)]
        else:
            verts += [P(0, 0.30, hip_z + 0.06), P(0, 0.38, hip_z + 0.14), P(0, 0.44, hip_z + 0.27)]
            radii += [tr[0] * k, tr[1] * k, tr[2] * k]
            wts += [{"tail1": 1.0}, {"tail1": 0.5, "tail2": 0.5}, {"tail2": 1.0}]
            edges += [(0, i0), (i0, i0 + 1), (i0 + 1, i0 + 2)]
    body_ob = skin_object("Body", verts, edges, radii, body, rig, wts)

    def patch(name, c, r, colkey):
        """v0.47 (TPDB_ANIM47): a marking as the part of the body's own surface inside an ellipsoid (centre c, radii r), lying flat on the
        body, bent with it and drawn with no line of its own (an ellipsoid set into the flank stood out of the outline as a lump with its own
        outline)."""
        c, r = Vector(c), Vector(r)
        ob = shell_over(body_ob, name, colkey, rig, 0.0025 * k,
                        [lambda co, w: ((co.x - c.x) / r.x) ** 2 + ((co.y - c.y) / r.y) ** 2 + ((co.z - c.z) / r.z) ** 2 - 1.0])
        try:
            ob.lineart.usage = "EXCLUDE"
        except (AttributeError, TypeError):
            pass
        return ob

    if G42:
        no_isect(body_ob)       # (seam ticks at the withers where the legs' tops pass into the body)
    leg_col = spec.get("leg_col", body)
    if Q:
        for sd in ("L", "R"):
            lv, lr, lw = legv[sd]
            ob = skin_object(f"Legs_{sd}", lv, [(0, 1), (1, 2), (2, 3), (4, 5), (5, 6), (6, 7)], lr, leg_col, rig, lw)
            if sd == "L":
                # the far side at three-quarters and in profile (yaw 45, 90, 135 turn the character's left away from the camera)
                ob.data.materials[0] = far_mat(leg_col, FARF)
            no_isect(ob)
            if DOG42 == "B" and kind == "dog" and sd == "R" and spec.get("spots") and not A47:
                # v0.42: a brown patch on the near foreleg, so the white legs part from a pale ground
                pv = P(-hx - 0.034, -0.150, 0.5 * (chest_z - 0.07 + knee_z) + 0.012)
                skin_like(no_isect(ellipsoid("LegSpot", pv, (0.016 * k, 0.034 * k, 0.050 * k), spec["spot_col"], rig, "fleg_R")), ob, rig)

    for sd, sg in (("L", 1), ("R", -1)):
        if G42:
            # v0.42: split hooves, two halves with a notch between them, longer than high and dark grey (black balls)
            for part, px in (("a", 0.0115), ("b", -0.0115)):
                for nm, y_, bone in ((f"FPaw_{sd}{part}", -0.168, f"fshin_{sd}"), (f"BPaw_{sd}{part}", 0.236, f"bmeta_{sd}")):
                    no_isect(ellipsoid(nm, P(sg * hx + px, y_, 0.019), (0.0125 * k, 0.030 * k, 0.019 * k), "slate", rig, bone))
            continue
        if Q and ART and kind == "goat":
            # small split hooves, a notch between the two halves
            for part, px in (("a", 0.010), ("b", -0.010)):
                ellipsoid(f"FPaw_{sd}{part}", P(sg * hx + px, -0.170, 0.022), (0.012 * k, 0.026 * k, 0.020 * k), spec.get("paws", "charcoal"), rig, f"fshin_{sd}")
                ellipsoid(f"BPaw_{sd}{part}", P(sg * hx + px, 0.230, 0.022), (0.012 * k, 0.026 * k, 0.020 * k), spec.get("paws", "charcoal"), rig, f"bmeta_{sd}")
            continue
        if Q:
            # the paw the end of the leg, in its colour, a little wider than the wrist and toes forward
            pc = leg_col if kind != "goat" else spec.get("paws", belly)
            for nm, y_, bone in ((f"FPaw_{sd}", -0.182, f"fshin_{sd}"), (f"BPaw_{sd}", 0.222, f"bmeta_{sd}")):
                if A47 and kind != "goat":
                    # v0.47 (TPDB_ANIM47): shorter and higher, a rounded block at the leg's end (a flat oval twice the leg's width, "round blobs")
                    ob = ellipsoid(nm, P(sg * hx, y_ + 0.008, 0.029), (0.040 * k * LR, 0.048 * k * LR, 0.029 * k), pc, rig, bone, sq=2.6)
                else:
                    ob = ellipsoid(nm, P(sg * hx, y_, 0.026), (0.043 * k * LR, 0.056 * k * LR, 0.026 * k), pc, rig, bone)
                if sd == "L" and pc == leg_col:
                    ob.data.materials[0] = far_mat(leg_col, FARF)
                no_isect(ob)
            continue
        fp = ellipsoid(f"FPaw_{sd}", P(sg * 0.075, -0.180, 0.030), (0.046 * k * LR, 0.058 * k * LR, 0.032 * k), spec.get("paws", belly), rig, f"fshin_{sd}")
        bp = ellipsoid(f"BPaw_{sd}", P(sg * 0.075, 0.195, 0.030), (0.046 * k * LR, 0.058 * k * LR, 0.032 * k), spec.get("paws", belly), rig, f"bshin_{sd}")
        if ISECT39 == "B":
            no_isect(fp)
            no_isect(bp)
    if DOG42 == "B" and kind == "dog":
        if not spec.get("spots") and A47:
            patch("Chest", P(0, -0.290, chest_z + 0.005), (0.050 * k, 0.075 * k, 0.092 * k), belly)
        elif not spec.get("spots"):
            # v0.42: a narrow blaze down the front of the chest, ending above the belly (the wide oval read "like a bib or a nappy")
            no_isect(ellipsoid("Chest", P(0, -0.236, chest_z + 0.025), (0.042 * k, 0.040 * k, 0.080 * k), belly, rig, "spine",
                               rot=Quaternion((1, 0, 0), -0.30)))
    elif A47 and kind == "cat":
        patch("Chest", P(0, -0.250, chest_z - 0.035), (0.075 * k, 0.085 * k, 0.100 * k), belly)
    elif not (ART and kind == "goat"):
        # (no chest patch on the brown goat: at three-quarters its white oval stood on the shoulder like an egg)
        chest_ob = ellipsoid("Chest", P(0, -0.22, chest_z - 0.02), (0.085 * k, 0.05 * k, 0.095 * k), belly, rig, "spine")
        if Q or ISECT39 == "B":
            no_isect(chest_ob)

    # spots on the flanks, sitting on the actual body surface
    if spec.get("spots"):
        pts = surface_points(body_ob)
        for i, (y, z, rx, rz, side) in enumerate(spec["spots"]):
            yy, zz = y * S, z * S
            if ART and kind == "dog":
                # v0.39 (bench round 1): halfway to the body's middle, onto the flank (on the slimmer back of revision "B" they stood over the outline
                # "like small round bumps")
                zc = 0.5 * (hip_z + chest_z)
                zz = (zc + (z - zc) * 0.5) * S
            near = [q for q in pts if abs(q.y - yy) < 0.03 * S and abs(q.z - zz) < 0.03 * S and q.x * side > 0]
            xs = max((abs(q.x) for q in near), default=0.11 * S)
            bone = "hips" if y > 0.05 else "spine"
            if A47:
                patch(f"Spot{i}", (side * xs, yy, zz), (0.070 * k, rx * k, rz * k), spec["spot_col"])
                continue
            skin_like(ellipsoid(f"Spot{i}", Vector((side * (xs - 0.004 * S), yy, zz)), (0.012 * k, rx * k, rz * k), spec["spot_col"], rig, bone), body_ob, rig)   # v0.15: bends with the flank
        if D43:
            # v0.43 (TPDB_DOG43): a brown patch over the near hip, which the thigh runs into (white on white, the hind leg was "pasted onto the body")
            yy, zz = 0.19 * S, (hip_z - 0.03) * S
            near = [q for q in pts if abs(q.y - yy) < 0.03 * S and abs(q.z - zz) < 0.03 * S and q.x < 0]
            xs = max((abs(q.x) for q in near), default=0.11 * S)
            if A47:
                patch("HipSpot", (-xs, yy, zz), (0.075 * k, 0.068 * k, 0.062 * k), spec["spot_col"])
            else:
                skin_like(ellipsoid("HipSpot", Vector((-(xs - 0.004 * S), yy, zz)), (0.014 * k, 0.068 * k, 0.060 * k), spec["spot_col"], rig, "hips"), body_ob, rig)

    hc = P(0, -0.30, chest_z + 0.22) if not (ART and kind == "goat") else neck_tail + P(0, -0.04, 0.06)
    hr = spec.get("head_r", 0.115 if kind == "dog" else 0.135) * k
    if ART and kind == "cat":
        hr *= 0.88           # a smaller head for the body (the sphere was about as large as the chest)
        if CAT42 in ("B", "C"):
            hr *= 0.90       # (v0.42: still large for the body)
    head_col = spec.get("head_col", body)
    if G42:
        # v0.42: a smaller cranium; the face runs on from it as a chain down to the muzzle (below)
        hr = 0.082 * k
        no_isect(ellipsoid("Head", hc, (hr * 0.94, hr * 1.06, hr), head_col, rig, "head", seg=36, rings=20))
    elif DOG42 == "B" and kind == "dog":
        ellipsoid("Head", hc, (hr * 1.02, hr * 1.04, hr * 0.90), head_col, rig, "head", seg=36, rings=20)
    else:
        ellipsoid("Head", hc, (hr * 1.02, hr, hr * 0.96), head_col, rig, "head", seg=36, rings=20)
    ears = spec.get("ears", "flop" if kind == "dog" else "prick")
    if kind in ("dog", "goat"):
        sl = spec.get("snout", 1.0)
        snout_c = hc + Vector((0, -hr * 0.95, -0.045 * k))
        if ART and kind == "goat":
            snout_c = hc + Vector((0, -hr * 1.20, -0.040 * k))
        if G42:
            # v0.42: the face a wedge from the poll down to the muzzle, narrowing, in the head's colour, the muzzle's end in line with it and paler
            mv = [hc + Vector((0, -0.030, -0.036)) * k, hc + Vector((0, -0.090, -0.060)) * k, hc + Vector((0, -0.142, -0.084)) * k,
                  hc + Vector((0, -0.170, -0.096)) * k]
            mr = [0.060 * k, 0.052 * k, 0.045 * k, 0.040 * k]
            no_isect(skin_object("Snout", mv, [(0, 1), (1, 2), (2, 3)], mr, head_col, rig, [{"head": 1.0}] * 4))
            nose_p = mv[-1] + Vector((0, -mr[-1] * 0.22, mr[-1] * 0.24))
            mouth_p = mv[-1] + Vector((0, -mr[-1] * 0.30, -mr[-1] * 0.55))
        elif ART and kind in ("dog", "goat"):
            # the muzzle grows out of the head through a stop, a tapered chain from inside the skull, with no line where it leaves it (the goat's
            # longer and narrower: a long head, wedge-shaped from the side)
            if kind == "goat":
                mv = [hc + Vector((0, -hr * 0.40, -0.010 * k)), hc + Vector((0, -hr * 0.98, -0.030 * k)), snout_c + Vector((0, -0.040 * k * sl, -0.004 * k))]
                mr = [0.066 * k, 0.052 * k, 0.038 * k]
            elif DOG42 == "B":
                # v0.42: longer, its top level from the stop to the nose
                mv = [hc + Vector((0, -hr * 0.45, -0.042 * k)), hc + Vector((0, -hr * 0.95, -0.034 * k)), hc + Vector((0, -hr * 1.28 - 0.012 * k * sl, -0.027 * k))]
                mr = [0.060 * k, 0.052 * k, 0.045 * k]
            else:
                mv = [hc + Vector((0, -hr * 0.45, -0.020 * k)), hc + Vector((0, -hr * 0.92, -0.036 * k)), snout_c + Vector((0, -0.030 * k * sl, -0.002 * k))]
                mr = [0.062 * k, 0.054 * k, 0.044 * k]
            mz = skin_object("Snout", mv, [(0, 1), (1, 2)], mr, belly, rig, [{"head": 1.0}] * 3)
            no_isect(mz)
            nose_p = mv[-1] + Vector((0, -mr[-1] * 0.38, mr[-1] * 0.22))
            if kind == "dog" and NOSE44 == "A":
                nose_p = mv[-1] + Vector((0, -mr[-1] * 0.10, mr[-1] * 0.30))     # v0.44 (TPDB_NOSE44): set into the muzzle's end
            mouth_p = mv[-1] + Vector((0, -mr[-1] * 0.10, -mr[-1] * 0.40))
        else:
            ellipsoid("Snout", snout_c, (0.058 * k * (0.85 if kind == "goat" else 1.0), 0.062 * k * sl, 0.045 * k), belly, rig, "head")
            nose_p = snout_c + Vector((0, -0.058 * k * sl, 0.012 * k))
            mouth_p = snout_c + Vector((0, -0.045 * k * sl, -0.032 * k))
        if G42:
            # (two nostrils, not a pink button)
            for sd, sg in (("L", 1), ("R", -1)):
                ellipsoid(f"NoseTip_{sd}", nose_p + Vector((sg * 0.011, 0, 0)) * k, (0.007 * k, 0.006 * k, 0.008 * k), "outline", rig, "head")
        else:
            ellipsoid("NoseTip", nose_p, (0.020 * k, 0.014 * k, 0.015 * k), "outline" if kind == "dog" else "pink", rig, "head")
    else:
        snout_c = hc + Vector((0, -hr * 0.90, -0.035 * k))
        if ART:
            # a whisker pad, two lobes, and whiskers: the strongest cat cue at small size
            for sd, sg in (("L", 1), ("R", -1)):
                if CAT44 == "A":
                    # v0.44 (TPDB_CAT44): the lobes larger and further forward, so the muzzle stands out of the head's round in profile
                    ellipsoid(f"Snout_{sd}", snout_c + Vector((sg * 0.017 * k, -0.014 * k, -0.006 * k)), (0.030 * k, 0.030 * k, 0.025 * k), belly, rig, "head")
                else:
                    ellipsoid(f"Snout_{sd}", snout_c + Vector((sg * 0.016 * k, -0.004 * k, -0.004 * k)), (0.026 * k, 0.024 * k, 0.022 * k), belly, rig, "head")
                for i, dz in enumerate((0.006, -0.004, -0.014) if not A47 else ()):
                    a0 = snout_c + Vector((sg * 0.026 * k, -0.012 * k, dz * k))
                    # (0.095 long with a droop of 1.6 hung below the sleeping cat's ground point: shorter, and nearly level)
                    a1 = a0 + Vector((sg * 0.068 * k, 0.004 * k, (dz * 0.4 + 0.003 * (1 - i)) * k))
                    if CAT44 == "A":
                        # v0.44 (TPDB_CAT44): forward as well as out, so they reach past the head's outline in profile; a little up, so the sleeping
                        # cat's, its head lowered, stay above its ground point (the validator: +49.9 px below it, 43.8 allowed)
                        a0 = a0 + Vector((0, -0.010 * k, 0))
                        a1 = a0 + Vector((sg * 0.060 * k, -0.024 * k, (dz * 0.4 + 0.003 * (1 - i) + 0.016) * k))
                    ob = cyl(f"Whisker_{sd}{i}", a0, a1, 0.0026 * k, "outline", seg=6)
                    rig.attach(ob, "head")
                for i, (dz, rise) in enumerate(((0.004, 0.022), (-0.008, 0.004)) if A47 else ()):
                    # v0.47 (TPDB_ANIM47): two a side, spread apart, each a thin dark line with no outline of its own (three thin tubes, each
                    # outlined on both sides, made one black block at the muzzle)
                    a0 = snout_c + Vector((sg * 0.030 * k, -0.022 * k, dz * k))
                    a1 = a0 + Vector((sg * 0.064 * k, -0.026 * k, rise * k))
                    ob = cyl(f"Whisker_{sd}{i}", a0, a1, 0.0036 * k, "outline", seg=6, r1=0.0018 * k)
                    rig.attach(ob, "head")
                    try:
                        ob.lineart.usage = "EXCLUDE"
                    except (AttributeError, TypeError):
                        pass
        else:
            ellipsoid("Snout", snout_c, (0.040 * k, 0.030 * k, 0.028 * k), belly, rig, "head")
        nose_p = snout_c + Vector((0, -0.030 * k, 0.012 * k))
        ellipsoid("NoseTip", nose_p, (0.011 * k, 0.007 * k, 0.008 * k), "pink", rig, "head")
        mouth_p = snout_c + Vector((0, -0.024 * k, -0.025 * k))
    for sd, sg in (("L", 1), ("R", -1)):
        if ears == "flop" and ART:
            el = spec.get("ear_len", 1.0)
            ellipsoid(f"Ear_{sd}", hc + Vector((sg * hr * 0.84, 0.030 * k, -0.020 * k - 0.025 * k * (el - 1))), (0.036 * k, 0.055 * k, 0.088 * k * el), acc, rig, "head",
                      rot=Quaternion((0, 1, 0), sg * 0.18))
        elif ears == "flop":
            ellipsoid(f"Ear_{sd}", hc + Vector((sg * hr * 0.92, 0.02 * k, -0.035 * k)), (0.028 * k, 0.050 * k, 0.085 * k), acc, rig, "head",
                      rot=Quaternion((0, 1, 0), sg * 0.25))
        elif ears == "goat" and G42:
            # v0.42: flat leaves from the poll, out and back and a little down, the flat face to the side so a profile shows the leaf (end on, the
            # side oval read as an eye socket)
            d = Vector((sg * 0.72, 0.55, -0.42)).normalized()
            no_isect(ellipsoid(f"Ear_{sd}", hc + Vector((sg * 0.050, 0.030, 0.026)) * k + d * 0.052 * k, (0.060 * k, 0.027 * k, 0.010 * k), acc, rig, "head",
                               rot=_frame_quat(d, sg)))
        elif ears == "goat":
            ellipsoid(f"Ear_{sd}", hc + Vector((sg * hr * 1.05, 0.02 * k, 0.01 * k)), (0.075 * k, 0.030 * k, 0.022 * k), acc, rig, "head",
                      rot=Quaternion((0, 1, 0), -sg * 0.35))
        else:
            big = spec.get("ear_size", 1.0)
            bm = bmesh.new()
            bmesh.ops.create_cone(bm, cap_ends=True, segments=16, radius1=0.060 * k * big, radius2=0.004 * k, depth=0.11 * k * big)
            ob = _mesh_object(f"Ear_{sd}", bm, acc if kind == "dog" else body)
            ob.location = hc + Vector((sg * hr * 0.55, 0.0, hr * 0.85))
            ob.rotation_euler = (0.1, sg * 0.35, 0)
            ob.scale = (1, 0.55, 1)
            if ART and kind == "cat":
                # flat triangular wedges turned forward (the cones read as horns in profile)
                ob.location = hc + Vector((sg * hr * 0.56, 0.004 * k, hr * 0.80))
                ob.rotation_euler = (-0.22, sg * 0.30, 0)
                ob.scale = (1.05, 0.26, 0.92)
                if CAT44 == "A":
                    # v0.44 (TPDB_CAT44): turned about 40 degrees about the vertical and taller, so the triangle shows in profile
                    ob.rotation_euler = (-0.22, sg * 0.30, sg * 0.70)
                    ob.scale = (1.05, 0.26, 1.15)
            upd()
            rig.attach(ob, "head")
            if spec.get("inner_ear"):
                bm = bmesh.new()
                bmesh.ops.create_cone(bm, cap_ends=True, segments=16, radius1=0.036 * k * big, radius2=0.003 * k, depth=0.07 * k * big)
                ob2 = _mesh_object(f"EarIn_{sd}", bm, spec["inner_ear"])
                ob2.location = hc + Vector((sg * hr * 0.55, -0.012 * k, hr * 0.82))
                ob2.rotation_euler = (0.1, sg * 0.35, 0)
                ob2.scale = (1, 0.40, 1)
                if ART and kind == "cat":
                    ob2.location = hc + Vector((sg * hr * 0.56, -0.010 * k, hr * 0.79))
                    ob2.rotation_euler = (-0.22, sg * 0.30, 0)
                    ob2.scale = (0.95, 0.16, 0.85)
                    if CAT44 == "A":
                        ob2.location = hc + Vector((sg * hr * 0.56, -0.010 * k, hr * 0.80))
                        ob2.rotation_euler = (-0.22, sg * 0.30, sg * 0.70)
                        ob2.scale = (0.95, 0.16, 1.06)
                upd()
                rig.attach(ob2, "head")
    if spec.get("horns"):
        # horns sweep up and back in a tapering arc (v0.17: horn_size, larger and darker, so a white goat is not "a lamb or
        # a white dog")
        hs = spec.get("horn_size", 1.0)
        for sd, sg in (("L", 1), ("R", -1)):
            base = hc + Vector((sg * hr * 0.34, 0.015 * k, hr * 0.84))
            if G42:
                base = hc + Vector((sg * 0.026, 0.006, 0.070)) * k
            arc = [base + Vector((sg * 0.012 * t * hs, (0.075 * t * t + 0.020 * t) * hs, (0.085 * t - 0.050 * t * t * t) * hs)) * k
                   for t in (0.0, 0.3, 0.55, 0.8, 1.0)]
            if G43:
                # v0.43 (TPDB_GOAT43): one smooth tapered horn on the same arc (five stacked pieces read as "springs or screws")
                ts = [i / 8 for i in range(9)]
                arc = [base + Vector((sg * 0.012 * t * hs, (0.075 * t * t + 0.020 * t) * hs, (0.085 * t - 0.050 * t * t * t) * hs)) * k for t in ts]
                rr = [0.019 * k * min(hs, 1.25) * (1 - 0.8 * t) for t in ts]
                no_isect(skin_object(f"Horn_{sd}", arc, [(i, i + 1) for i in range(len(arc) - 1)], rr, spec.get("horn_col", "khaki"), rig,
                                     [{"head": 1.0}] * len(arc)))
                continue
            for i in range(len(arc) - 1):
                r0 = 0.019 * k * min(hs, 1.25) * (1 - 0.8 * i / 4)
                r1 = 0.019 * k * min(hs, 1.25) * (1 - 0.8 * (i + 1) / 4)
                ob = cyl(f"Horn_{sd}{i}", arc[i], arc[i + 1] + (arc[i + 1] - arc[i]) * 0.08, r0, spec.get("horn_col", "khaki"), r1=r1)
                rig.attach(ob, "head")
    if spec.get("beard"):
        bs = spec.get("beard_size", 1.0)
        if G42:
            # v0.42: a pointed tuft hanging from under the jaw, behind the muzzle (at the muzzle's end it made the face a beak)
            root_ = mv[1] + Vector((0, -0.010, -mr[1] * 0.80))
            if GOAT44 == "A":
                # v0.44 (TPDB_GOAT44): shorter and blunt, angled back toward the throat, so it hangs nearly straight down when the head is lowered
                ob = cyl("Beard", root_, root_ + Vector((0, 0.028, -0.030 * bs)) * k, 0.019 * k, spec.get("beard_col", belly), r1=0.007 * k)
            else:
                ob = cyl("Beard", root_, root_ + Vector((0, 0.012, -0.050 * bs)) * k, 0.020 * k, spec.get("beard_col", belly), r1=0.004 * k)
            rig.attach(ob, "head")
        elif bs > 1.0:
            # v0.17: a pointed tuft growing from the chin (an oval hung below the snout read as a tongue or a tag)
            ob = cyl("Beard", mouth_p + Vector((0, 0.010, 0.006)) * k, mouth_p + Vector((0, 0.026, -0.055 * bs)) * k, 0.024 * k,
                     spec.get("beard_col", belly), r1=0.004 * k)
            rig.attach(ob, "head")
        else:
            ellipsoid("Beard", mouth_p + Vector((0, 0.012, -0.040)) * k, (0.022 * k, 0.020 * k, 0.040 * k), spec.get("beard_col", belly), rig, "head")
    if spec.get("collar") and G42:
        # v0.42 (TPDB_GOAT42 "C"): a collar round the middle of the neck, for the tether
        ob = cyl("Collar", P(0, -0.266, chest_z + 0.104), P(0, -0.275, chest_z + 0.128), 0.077 * k, spec["collar"], seg=24)
        rig.attach(ob, "neck")
    elif spec.get("collar"):
        ob = cyl("Collar", P(0, -0.20, chest_z + 0.06) + Vector((0, 0.03, 0)) * k, P(0, -0.235, chest_z + 0.115), 0.075 * k, spec["collar"], seg=24)
        rig.attach(ob, "neck")

    face = Face(rig, "head", hc, (hr * 1.02, hr, hr * 0.96), k, prefix="F")
    eye_dx, eye_z = 0.052 * k, 0.022 * k
    r_e = 0.024 * k
    eye_t = 0.010 * k
    if A47 and kind in ("dog", "cat"):
        # v0.47 (TPDB_ANIM47): 44 degrees round the head (27: in a side view the eye lay on the head's front edge, seen edge on, "a black
        # crescent"), and flatter, so the far one, on the outline at three-quarters, does not stand out of it
        eye_dx = 0.70 * hr * 1.02
        eye_t = 0.007 * k
    for sd, sg in (("L", 1), ("R", -1)):
        x = sg * eye_dx
        face.place(f"eye_{sd}", ellipsoid("eye", (0, 0, 0), (1, 1, 1), "outline"), face.frame(x, eye_z, 0.0, scale=(r_e * 0.85, eye_t, r_e * 1.15)))
        face.place(f"catch_{sd}", ellipsoid("catch", (0, 0, 0), (1, 1, 1), "cream"), face.frame(x + 0.006 * k * sg, eye_z + 0.012 * k, 0.009 * k, scale=(r_e * 0.30, 0.004 * k, r_e * 0.36)))
        w = r_e * 1.1
        face.curve_on(f"arcup_{sd}", [(x - w, eye_z - 0.010 * k), (x, eye_z + 0.013 * k), (x + w, eye_z - 0.010 * k)], 0.006 * k, "outline", 0.004 * k)
        face.curve_on(f"arcdn_{sd}", [(x - w, eye_z + 0.002 * k), (x, eye_z - 0.012 * k), (x + w, eye_z + 0.002 * k)], 0.006 * k, "outline", 0.004 * k)
        face.place(f"brow_{sd}", ellipsoid("brow", (0, 0, 0), (1, 1, 1), "outline"),
                   face.frame(x, eye_z + 0.040 * k, 0.004 * k, spin=-math.radians(20) * sg, scale=(0.020 * k, 0.006 * k, 0.006 * k)))
    if NOSE44 == "A" and kind == "dog":
        # v0.44 (TPDB_NOSE44): rooted in the mouth
        face.obj("tongue", ellipsoid("Tongue", mouth_p + Vector((0, 0.006 * k, -0.013 * k)), (0.018 * k, 0.012 * k, 0.022 * k), "throat", rig, "head"))
    else:
        face.obj("tongue", ellipsoid("Tongue", mouth_p + Vector((0, -0.006 * k, -0.018 * k)), (0.020 * k, 0.010 * k, 0.026 * k), "throat", rig, "head"))
    if READ44 == "A" and kind == "dog":
        # v0.44 (TPDB_READ44): round reading glasses for the "read" expression, a ring round each eye and a bridge over the muzzle
        for sd, sg in (("L", 1), ("R", -1)):
            x = sg * eye_dx
            ring = [(x + r_e * 1.55 * math.cos(a), eye_z + r_e * 1.60 * math.sin(a)) for a in [i / 28 * 2 * math.pi for i in range(28)]]
            ob = face.curve_on(f"glass_{sd}", ring, 0.0055 * k, "outline", 0.010 * k)
            ob.data.splines[0].use_cyclic_u = True
        gb = eye_dx - r_e * 1.55
        face.curve_on("glass_bridge", [(gb * t, eye_z + 0.004 * k) for t in ((-1.0, -0.5, 0.0, 0.5, 1.0) if A47 else (-1.0, 1.0))], 0.005 * k, "outline", 0.012 * k)

    expr = {
        "neutral": {"eye_L", "eye_R", "catch_L", "catch_R"},
        "happy": {"arcup_L", "arcup_R"} | ({"tongue"} if kind == "dog" else set()),
        "sleepy": {"arcdn_L", "arcdn_R"},
        "alert": {"eye_L", "eye_R", "catch_L", "catch_R"},
        "sad": {"eye_L", "eye_R", "catch_L", "catch_R", "brow_L", "brow_R"},
    }
    if READ44 == "A" and kind == "dog":
        expr["read"] = {"eye_L", "eye_R", "catch_L", "catch_R", "glass_L", "glass_R", "glass_bridge"}     # v0.44 (TPDB_READ44)
    states = {}
    for name, show in expr.items():
        st = {key_ob.name: {"hide": key not in show} for key, key_ob in face.objs.items()}
        sc = {"alert": 1.25, "sad": 1.08}.get(name, 1.0)
        for sd, sg in (("L", 1), ("R", -1)):
            st[face.objs[f"eye_{sd}"].name]["basis"] = list_m(face.frame(sg * eye_dx, eye_z, 0.0, scale=(r_e * 0.85 * sc, eye_t, r_e * 1.15 * sc)))
        states[name] = st

    for sd, sg in (("L", 1), ("R", -1)):
        anchor(rig, f"eye_{sd}", face.at(sg * eye_dx, eye_z), "head")
        anchor(rig, f"paw_F{sd}", P(sg * hx, -0.18, 0.0), f"fshin_{sd}")
        anchor(rig, f"paw_B{sd}", P(sg * hx, 0.21 if Q else 0.19, 0.0), f"{paw_bone}_{sd}")
    mid = (face.at(eye_dx, eye_z) + face.at(-eye_dx, eye_z)) / 2
    anchor(rig, "gaze_target", mid + Vector((0, -1.0, 0)), "head")
    anchor(rig, "head_top", hc + Vector((0, 0, hr + 0.01)), "head")
    anchor(rig, "mouth", mouth_p, "head")
    anchor(rig, "back", P(0, 0.02, chest_z + 0.12), "spine")
    anchor(rig, "collar", P(0, -0.335, chest_z + 0.108) if G42 else P(0, -0.235, chest_z + 0.08), "neck")
    names = make_quadruped_poses(rig, S, kind, hip_z, chest_z, hx=hx, three=Q, yb=yb, collar=spec.get("collar"))
    return rig, states, names


SB = {"cx": 0.0, "tail": (-0.9, -0.45, -0.05), "tail2": (-0.2, -1.0, -0.05), "neck": (-0.35, -0.85, -0.25), "hp": -30, "ht": 0,
      "bl": (0.09, 0.10, 0), "br": (-0.09, 0.14, 0), "bh": (0, -1, -0.3)}


def make_quadruped_poses(rig, S, kind, hip_z, chest_z, hx=0.075, three=False, yb=0.0, collar=None):
    names = []
    rig.pose_props = {}
    rig.pose_hides = {}
    g43 = bool(yb) and GOAT43 in ("B", "C")
    LH = hip_z / 0.44
    if yb:
        LH = chest_z / 0.46      # (v0.42's goat: its hips raised level with its chest, not longer legs)
    cat39 = ART39 == "B" and kind == "cat"
    if cat39:
        # (the redrawn cat's hips stand at 0.47 of its legs, not 0.44: its legs are no longer for that, so its drops are scaled as v0.38's)
        LH = hip_z / 0.47
    state = {"hip_drop": 0.0, "chest_drop": 0.0}
    wide = hx / 0.075          # (a pose's paw targets at x 0.075 widened with the stance)

    def legs(front, back, fhint=(0, 0.6, 0.2), bhint=(0, -1, 0.1)):
        for sd in ("L", "R"):
            f = Vector(front[sd])
            b = Vector(back[sd])
            b.y += yb              # (v0.42's goat: the hind feet under its hips, moved back with them)
            if three:
                f.x *= wide
                b.x *= wide
            rig.ik2(f"fleg_{sd}", f"fshin_{sd}", f * S, fhint)
            if not three:
                rig.ik2(f"bleg_{sd}", f"bshin_{sd}", b * S, bhint)
                continue
            # v0.39 (TPDB_QUAD39): through the hock. Standing, the hock behind and above the paw; crouched, lower; sitting or lying, the cannon
            # laid flat on the ground behind the paw, under the haunch
            if state.get("hock"):
                # v0.42 (TPDB_BEG42): the hock on the ground behind the paw, the cannon flat and the paw forward, the stifle up
                hock = b + Vector(state["hock"]) * LH
                stifle_hint = bhint
            elif state["hip_drop"] >= 0.20:
                # sitting, begging, lying: the hock close above the paw and a little behind, so the leg folds under the haunch as the two-bone
                # leg did (the cannon laid flat behind the paw read as kneeling shins)
                hock = b + Vector((0, 0.030, 0.062)) * LH
                stifle_hint = bhint
            elif state["hip_drop"] >= 0.08 or state["chest_drop"] >= 0.15:
                hock = b + Vector((0, 0.080, 0.060)) * LH
                stifle_hint = (0, -1, 0.35)
            else:
                hock = b + Vector((0, 0.045, 0.090)) * LH
                stifle_hint = (0, -1, 0.25)
            rig.ik2(f"bleg_{sd}", f"bshin_{sd}", hock * S, stifle_hint)
            rig.aim(f"bmeta_{sd}", b * S)

    def body(hip_drop=0.0, chest_drop=0.0, head_pitch=0.0, head_turn=0.0, tail=(0, 0.6, 1.0), neck=(0, -0.5, 1.0), hip_back=0.0, chest_y=-0.16, chest_x=0.0,
             spine_scale=None):
        state["hip_drop"], state["chest_drop"] = hip_drop, chest_drop
        state["hock"] = None
        if cat39:
            # lying (a drop of a quarter or more), the redrawn cat's hips and chest end where v0.38's did, 0.44 and 0.46 less the drop: from its
            # hips at 0.47 and chest at 0.43 the chest came down to 0.07, the head onto the ground
            if hip_drop >= 0.25:
                hip_drop += 0.03
            if chest_drop >= 0.25:
                chest_drop -= 0.03
        hb = rig.arm.pose.bones["hips"]
        hb.location = (0, -hip_drop * S * LH, -hip_back * S)
        if spine_scale:
            # v0.13: the trunk drawn shorter and rounder (a cat curled up asleep); the neck and front legs keep their size
            for b in ("neck", "fleg_L", "fleg_R"):
                rig.arm.data.bones[b].inherit_scale = "NONE"
            rig.arm.pose.bones["spine"].scale = tuple(spine_scale)
        upd()
        chest = Vector((chest_x * S, chest_y * S, (chest_z - chest_drop * LH) * S))
        rig.aim("spine", chest)
        rig.aim_dir("neck", neck)
        p = math.radians(head_pitch)
        rig.aim_dir("head", (0, math.sin(p), math.cos(p)), twist=math.radians(head_turn))
        rig.aim_dir("tail1", tail)
        rig.aim_dir("tail2", (tail[0], tail[1] * 0.6, tail[2] * 1.2))

    def paws(fy=-0.16, by=0.21, z=0.04):
        return ({"L": (0.075, fy, z), "R": (-0.075, fy, z)}, {"L": (0.075, by, z), "R": (-0.075, by, z)})

    def pose(name, fn):
        rig.reset()
        fn()
        rig.key_pose(name)
        names.append(name)

    def stand():
        if g43:
            # v0.43 (TPDB_GOAT43): the neck forward at about 35 degrees, the face level (straight up, "a little llama-like")
            body(neck=(0, -0.78, 1.0), head_pitch=4)
            legs(*paws())
            return
        body()
        legs(*paws())

    def walk():
        body(tail=(0, 0.5, 1.0))
        legs({"L": (0.075, -0.25, 0.06), "R": (-0.075, -0.08, 0.04)}, {"L": (0.075, 0.13, 0.04), "R": (-0.075, 0.29, 0.06)})

    def stand_hose():
        # v0.47 (TPDB_HOSE47): see the switch
        if HOSE47 == "D":
            body(head_pitch=0, head_turn=-18)
            f, b = paws()
            fx, fy = -0.075, -0.20
            f["R"] = (fx, fy, 0.04)
            f["L"] = (0.075, -0.15, 0.04)
            legs(f, b)
        else:
            body(head_pitch=0, chest_drop=0.055, neck=(0, -0.5, 1.0))
            f, b = paws()
            fx, fy = -0.10, -0.30
            f["R"] = (fx, fy, 0.04)
            f["L"] = (0.075, -0.13, 0.04)
            legs(f, b, fhint=(0, 0.6, 0.2))
        x = fx * (wide if three else 1.0)
        miss = (rig.tail("fshin_R") - Vector((x, fy, 0.04)) * S).length
        if miss > 1e-4 * S:
            print("stand_hose: the near forepaw misses its place by", round(miss / S, 4))
        anchor(rig, "hose_paw@stand_hose", Vector((x, fy - 0.02, 0.0)) * S, "fshin_R")

    def sit():
        # haunches down and forward under the body, chest up over straight front legs
        body(hip_drop=0.25, hip_back=-0.12, chest_drop=-0.03, tail=(0.15, 0.9, -0.35), neck=(0, -0.20, 1), head_pitch=6)
        legs({"L": (0.075, -0.165, 0.04), "R": (-0.075, -0.165, 0.04)}, {"L": (0.10, 0.00, 0.035), "R": (-0.10, 0.02, 0.035)},
             fhint=(0, 0.3, 0.1), bhint=(0, -1, 0.35))

    def sit_wait():
        # v0.29: as sit, the tail curled round the near haunch (at three-quarters, with the tail out behind, "the rear of the dog is jumbled": "a tangle of thin shapes")
        sit()
        rig.aim_dir("tail1", (-0.55, 0.45, -0.70))
        rig.aim_dir("tail2", (-0.35, -0.90, -0.05))
        # (the hind paws drawn in under the body: "the back legs and rear splay out to the right in overlapping shapes")
        legs({"L": (0.075, -0.165, 0.04), "R": (-0.075, -0.165, 0.04)}, {"L": (0.09, -0.07, 0.035), "R": (-0.09, -0.05, 0.035)}, fhint=(0, 0.3, 0.1), bhint=(0, -1, 0.35))

    def sit_look_down():
        # sitting, head bent down as if looking at something held in front of the chest
        sit()
        rig.aim_dir("neck", (0, -0.45, 1))
        p = math.radians(-30)
        rig.aim_dir("head", (0, math.sin(p), math.cos(p)))

    def sit_up_hold():
        if BEG42 == "B" and READ44 == "A":
            # v0.44 (TPDB_READ44): sitting up as v0.42, both forepaws raised level to the paper's top edge, the far one a little ahead so both show
            # on it in profile; the head bowed about 20 degrees and turned a little to the viewer
            body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.30, chest_y=0.0, tail=(0.10, 0.90, 0.25), neck=(0, -0.30, 1), head_pitch=-26,
                 head_turn=-20, spine_scale=(1.12, 0.80, 1.12))
            rig.aim_dir("tail2", (0.0, 0.25, 1.0))
            fz = chest_z * 0.72
            legs({"L": (0.065, -0.21, fz + 0.13), "R": (-0.065, -0.25, fz + 0.135)}, {"L": (0.12, 0.09, 0.035), "R": (-0.12, 0.11, 0.035)},
                 fhint=(0, 0.4, -1), bhint=(0, -1, 0.35))
            return
        if BEG42 == "B" and READ43 == "B":
            # v0.43 (TPDB_READ43): sitting a little more upright, the head bowed toward the page and the forepaws lower, on the top of a paper whose
            # foot is on the ground (its paper stood "upright on its own")
            body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.30, chest_y=-0.05, tail=(0.10, 0.90, 0.25), neck=(0, -0.50, 1), head_pitch=-34,
                 head_turn=-15, spine_scale=(1.12, 0.80, 1.12))
            rig.aim_dir("tail2", (0.0, 0.25, 1.0))
            fz = chest_z * 0.72
            legs({"L": (0.065, -0.27, fz - 0.02), "R": (-0.065, -0.27, fz - 0.10)}, {"L": (0.12, 0.09, 0.035), "R": (-0.12, 0.11, 0.035)},
                 fhint=(0, 0.4, -1), bhint=(0, -1, 0.35))
            return
        # sitting up on the haunches, front legs raised to hold something in front of the chest,
        # head bent down over it (a dog "reading" with its paws on the paper)
        # v0.26 bench (TPDB_READDOG): the head bent over the paper showed only its round back and an ear in profile ("could be taken
        # for a monkey, an otter, or a person in a costume", "a person in a spacesuit or a small robot"). A: the head up, its muzzle and
        # eye in profile above the paper. B: and turned a little to the viewer. v0.26: B, on the bench (isolation_v026.md: "a brown-and-tan
        # cartoon dog", and no animal but a dog; A's was once "a weasel or an otter").
        _rd = __import__("os").environ.get("TPDB_READDOG", "B")
        _rn, _rp, _rt = {"A": ((0, -0.30, 1), -8, 0), "B": ((0, -0.30, 1), -8, -28)}.get(_rd, ((0, -0.45, 1), -34, 0))
        body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.30, chest_y=0.0, tail=(0.35, 0.75, -0.55), neck=_rn, head_pitch=_rp, head_turn=_rt,
             spine_scale=(1.12, 0.80, 1.12) if BEG42 == "B" else None)
        # v0.11: the tail curled forward along the ground beside the haunch (straight out behind, long and
        # thin, it read as a fox's or a kangaroo's)
        rig.aim_dir("tail2", (0.55, -0.80, -0.05))
        if __import__("os").environ.get("TPDB_RDTAIL", "A") == "A":
            # v0.26, chosen on the bench: the tail up behind (along the ground, "the rear end spreads out into a flat, pointed shape that could
            # be the tail or a haunch"; isolation_v026.md)
            rig.aim_dir("tail1", (0.10, 0.90, 0.25))
            rig.aim_dir("tail2", (0.0, 0.25, 1.0))
        fz = chest_z * 0.72
        if BEG42 == "B":
            # v0.42: the hind legs folded, stifle and hock bent, the hind paws flat beside the rump (stretched out in front, "like a person sitting")
            legs({"L": (0.065, -0.25, fz + 0.055), "R": (-0.065, -0.25, fz - 0.055)}, {"L": (0.12, 0.09, 0.035), "R": (-0.12, 0.11, 0.035)},
                 fhint=(0, 0.4, -1), bhint=(0, -1, 0.35))
            return
        # v0.25: the paws at different heights, so both show on the paper in profile (level, one hid the other: "only one paw
        # clearly touches it", on the bench)
        legs({"L": (0.065, -0.25, fz + 0.055), "R": (-0.065, -0.25, fz - 0.055)}, {"L": (0.11, -0.17, 0.035), "R": (-0.11, -0.15, 0.035)},
             fhint=(0, 0.4, -1), bhint=(0, -0.3, 1))

    def sit_read():
        # v0.47 (TPDB_READ47): see the switch
        c47 = READ47 in ("C", "D", "E")
        e47 = READ47 == "E"
        # (the tail's root and its tip: where each points)
        tl = (0.0, 0.62, 0.78, 0.0, -0.25, 1.0) if e47 else (0.10, 0.90, 0.25, 0.0, 0.25, 1.0)
        body(hip_drop=0.37 if (kind == "dog" and DOG43 == "B") else 0.38, hip_back=-0.04, chest_drop=-0.30, chest_y=0.12,
             tail=tuple(tl[:3]) if c47 else (-0.55, 0.45, -0.70), neck=(0, -0.34, 1), head_pitch=-30, head_turn=-22,
             spine_scale=(1.12, 0.80, 1.12))
        state["hock"] = (0, 0.085, 0.012)
        rig.aim_dir("tail2", tuple(tl[3:6]) if c47 else (-0.35, -0.90, -0.05))
        hx_, hy_ = (0.125, -0.02) if READ47 in ("D", "E") else (0.10, 0.08)
        legs({"L": (0.065, -0.04, 0.30), "R": (-0.065, -0.04, 0.30)}, {"L": (hx_, hy_, 0.030), "R": (-hx_, hy_ + 0.02, 0.030)}, fhint=(0, -1, -0.2),
             bhint=(0, -1, 1.2))
        ch = rig.tail("spine")
        pw, ph, th = 0.19 * S, 0.27 * S, 0.006 * S
        F = Frame.euler(ch + Vector((-0.02, -0.24, -0.08)) * S, rx=38, rz=42)
        fold = 10
        for sd, sg in (("L", 1), ("R", -1)):
            # (the near paw under the near page's lower corner; the far paw high on the far page's outer edge, where it shows above the near foreleg)
            g = F.p(sg * pw * (0.78 if sg < 0 else 0.95), 0.012 * S, -ph * (0.44 if sg < 0 else -0.18))
            miss = rig.ik2(f"fleg_{sd}", f"fshin_{sd}", g, (0, 0.3, -1))
            if miss > 1e-4:
                print("sit_read: paw", sd, "misses the paper by", round(miss / S, 4))

        def part(nm, ob, lines=True):
            ob.name = f"PROP_sit_read_{nm}"
            rig.attach(ob, "spine")
            ob.hide_render = True
            ob.hide_viewport = True
            if not lines:
                try:
                    ob.lineart.usage = "EXCLUDE"
                except (AttributeError, TypeError):
                    pass
            rig.pose_props.setdefault("sit_read", []).append(ob.name)
            return ob

        for sd, sg in (("L", 1), ("R", -1)):
            q = F.q @ Quaternion((0, 0, 1), math.radians(sg * fold))
            Fp = Frame(F.o + q @ Vector((sg * pw / 2, 0, 0)), q)
            part(f"page{sd}", box(f"page{sd}", Fp.o, (pw, th, ph), "white", rot=q))
            y = th / 2 + 0.0015 * S
            part(f"head{sd}", box(f"head{sd}", Fp.p(0, y, ph * 0.36), (pw * 0.80, 0.002 * S, ph * 0.085), "charcoal", rot=q), lines=False)
            rows = 5
            if sg > 0:
                # (a pale photo on the far page, three ruled bands under it)
                part("photo", box("photo", Fp.p(-pw * 0.13, y, ph * 0.13), (pw * 0.52, 0.002 * S, ph * 0.24), "cloud_dark", rot=q), lines=False)
                rows = 3
            for i in range(rows):
                z = (ph * (0.22 - i * 0.135)) if sg < 0 else (ph * (-0.10 - i * 0.135))
                part(f"text{sd}{i}", box(f"text{sd}{i}", Fp.p(0, y, z), (pw * 0.80, 0.002 * S, ph * 0.040), "gray", rot=q), lines=False)
        for nm, (x, z) in (("paper_a", (-1, 1)), ("paper_b", (1, 1)), ("paper_c", (1, -1)), ("paper_d", (-1, -1)), ("paper_mid", (0, 0))):
            anchor(rig, f"{nm}@sit_read", F.p(x * pw * 0.98, 0.0, z * ph / 2), "spine")
        if c47 and collar and bpy.data.objects.get("Collar") is not None:
            # (no collar in this pose: the ring is fitted to the standing neck and stands out behind the upright one)
            rig.pose_hides.setdefault("sit_read", []).append("Collar")
        if e47 and collar:
            # a band round the body's own section a little above the neck's base (up the neck from its base, the band's height, and how far it
            # stands off the skin)
            tv = (0.05, 0.034, 0.005)
            nh, nt = rig.head("neck"), rig.tail("neck")
            ax = (nt - nh).normalized()
            fw = ax.cross(Vector((1, 0, 0))).normalized()
            if fw.y > 0:
                fw = -fw
            upd()
            ev = bpy.data.objects["Body"].evaluated_get(bpy.context.evaluated_depsgraph_get())
            me = ev.to_mesh()
            mi = rig.arm.matrix_world.inverted() @ ev.matrix_world
            pts = [mi @ v.co for v in me.vertices]
            ev.to_mesh_clear()

            def section(t, h):
                q = [(v.x, (v - nh).dot(fw)) for v in pts if abs((v - nh).dot(ax) - t * S) <= h * S / 2]
                xs, fs = [a for a, _ in q], [b for _, b in q]
                return len(q), min(xs), max(xs), min(fs), max(fs)
            n_, x0, x1, f0, f1 = section(tv[0], tv[1])
            print("sit_read: the collar's section", n_, "points, across", round((x1 - x0) / S, 3), "fore and aft", round((f1 - f0) / S, 3))
            c = nh + ax * tv[0] * S + fw * (f0 + f1) / 2
            rx, rf, hh = (x1 - x0) / 2 + tv[2] * S, (f1 - f0) / 2 + tv[2] * S, tv[1] * S
            bm = bmesh.new()
            lo, hi = [], []
            for i in range(32):
                a = 2 * math.pi * i / 32
                d = Vector((1, 0, 0)) * (rx * math.cos(a)) + fw * (rf * math.sin(a))
                lo.append(bm.verts.new(c + d - ax * hh / 2))
                hi.append(bm.verts.new(c + d + ax * hh / 2))
            for i in range(32):
                j = (i + 1) % 32
                bm.faces.new((lo[i], lo[j], hi[j], hi[i]))
            bm.faces.new(lo[::-1])
            bm.faces.new(hi)
            bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
            part("collar", _mesh_object("collar", bm, collar))

    def down_read():
        # v0.43 (TPDB_READ43 "A"): lying down like a sphinx, the trunk short, the forepaws out in front on a paper laid open on the ground (the
        # scene draws it), the head bowed over them and turned a little to the viewer
        # (bench round 1: with the nose down on the page each reader offered "sniffing" beside "reading"; round 2, the head raised, it looked "past the
        # paper". Between the two, bowed toward the page)
        body(hip_drop=0.33, chest_drop=0.33, hip_back=-0.05, chest_y=-0.10, tail=(0.9, -0.55, -0.05), neck=(0, -0.60, 0.80), head_pitch=-40,
             head_turn=-15, spine_scale=(1.12, 0.85, 1.10))
        legs({"L": (0.05, -0.42, 0.025), "R": (-0.05, -0.40, 0.025)}, {"L": (0.12, 0.10, 0.03), "R": (-0.12, 0.13, 0.03)}, fhint=(0, 0.7, 0.7),
             bhint=(0, -1, -0.2))
        rig.aim_dir("tail2", (-0.1, -1, -0.05))

    def sleep():
        # lying down, head resting on the front paws, tail curled along the side, eyes closed by expression
        body(hip_drop=0.32, chest_drop=0.33, tail=(0.9, -0.5, -0.1), neck=(0, -0.95, 0.05), head_pitch=-38, head_turn=8)
        legs({"L": (0.06, -0.40, 0.035), "R": (-0.06, -0.38, 0.035)}, {"L": (0.13, 0.12, 0.035), "R": (-0.12, 0.20, 0.035)},
             fhint=(0, 1, -0.4), bhint=(0, -1, -0.2))

    def sleep_curl():
        # v0.10: curled up asleep, the head turned back along the side and laid down by the front
        # paws, legs tucked under, the tail wrapped forward round the body (the sleeping cat lying
        # stretched out read as "crouched low")
        body(hip_drop=0.34, hip_back=-0.05, chest_drop=0.34, chest_y=-0.13, tail=(-0.95, -0.55, -0.05),
             neck=(-0.45, -0.60, -0.10), head_pitch=-30, head_turn=-35)
        legs({"L": (0.07, -0.24, 0.03), "R": (-0.07, -0.21, 0.03)}, {"L": (0.11, 0.03, 0.03), "R": (-0.11, 0.06, 0.03)},
             fhint=(0, 1, -0.5), bhint=(0, -1, -0.1))

    def sleep_ball():
        # v0.13: curled up in a ball to sleep, the front half swung round to one side so the body makes a
        # ring, the head laid on the back haunch, the paws tucked in, the tail wrapped round the front (lying
        # stretched out flat, a sleeping cat or dog "could also be read as collapsed", "unwell")
        body(hip_drop=0.33, hip_back=-0.08, chest_drop=0.35, chest_y=-0.08, chest_x=SB["cx"], tail=SB["tail"],
             neck=SB["neck"], head_pitch=SB["hp"], head_turn=SB["ht"])
        legs({"L": (0.05 + SB["cx"] * 0.5, -0.30, 0.025), "R": (-0.05 + SB["cx"] * 0.5, -0.28, 0.025)},
             {"L": (SB["bl"][0], SB["bl"][1], 0.025), "R": (SB["br"][0], SB["br"][1], 0.025)}, fhint=(0, 1, 0.2), bhint=SB["bh"])
        rig.aim_dir("tail2", SB["tail2"])

    def sleep_paws():
        # v0.29: lying down, the chin laid on both front paws in front of it and the elbows drawn in, facing out (curled up with the nose bowed to the ground, it was
        # "sniffing the grass, lying down, or curled up asleep")
        body(hip_drop=0.33, chest_drop=0.35, hip_back=-0.05, chest_y=-0.12, tail=(0.9, -0.55, -0.05), neck=(0, -0.90, 0.20), head_pitch=-22)
        legs({"L": (0.05, -0.36, 0.025), "R": (-0.05, -0.36, 0.025)}, {"L": (0.12, 0.10, 0.03), "R": (-0.12, 0.13, 0.03)}, fhint=(0, 0.7, 0.7), bhint=(0, -1, -0.2))
        rig.aim_dir("tail2", (-0.1, -1, -0.05))

    def sleep_paws_turn():
        # v0.29 bench: the same with a shorter trunk, the head turned to the viewer, for three-quarters view
        body(hip_drop=0.33, chest_drop=0.36, hip_back=-0.08, chest_y=-0.08, tail=(0.9, -0.55, -0.05), neck=(0, -0.92, 0.12), head_pitch=-26, head_turn=-25, spine_scale=(1.15, 0.72, 1.0))
        legs({"L": (0.05, -0.33, 0.025), "R": (-0.05, -0.33, 0.025)}, {"L": (0.11, 0.05, 0.03), "R": (-0.11, 0.08, 0.03)}, fhint=(0, 0.9, 0.3), bhint=(0, -1, -0.2))
        rig.aim_dir("tail2", (-0.1, -1, -0.05))

    def sleep_tuck():
        # v0.13 (cats): curled up asleep, the trunk drawn short and round, the legs tucked under, the head bowed
        # down onto the front paws and turned to the viewer, the tail laid along the side (the cat curled face-on
        # was too small to see; turned three-quarters with the trunk at full length it read as "stretched out on
        # its belly with its back legs extended behind it ... collapsed, injured or dead")
        body(hip_drop=0.33, hip_back=-0.08, chest_drop=0.36, chest_y=-0.08, neck=(-0.5, -0.7, -0.45), head_pitch=-30, head_turn=-45,
             tail=(-0.9, -0.45, -0.05), spine_scale=(1.25, 0.55, 1.0))
        legs({"L": (0.04, -0.18, 0.025), "R": (-0.06, -0.16, 0.025)}, {"L": (0.09, 0.04, 0.02), "R": (-0.09, 0.06, 0.02)},
             fhint=(0, 1, 0.2), bhint=(0, -1, -0.3))
        rig.aim_dir("tail2", (-0.1, -1, -0.05))

    def lie():
        body(hip_drop=0.31, chest_drop=0.30, tail=(0.5, 0.8, -0.15), neck=(0, -0.7, 0.6), head_pitch=-14)
        legs({"L": (0.08, -0.40, 0.035), "R": (-0.08, -0.37, 0.035)}, {"L": (0.11, 0.24, 0.035), "R": (-0.11, 0.25, 0.035)},
             fhint=(0, 1, -0.4), bhint=(0, -1, -0.3))

    def crouch():
        body(hip_drop=0.06, chest_drop=0.16, tail=(0, 1.0, 0.05), neck=(0, -1.0, 0.45), head_pitch=-4)
        legs({"L": (0.085, -0.22, 0.04), "R": (-0.085, -0.20, 0.04)}, {"L": (0.085, 0.24, 0.04), "R": (-0.085, 0.22, 0.04)},
             fhint=(0, 0.5, 0.5), bhint=(0, -1, 0.3))

    def stalk():
        # v0.8: stalking, belly almost on the ground, head low and level, eyes forward, tail straight
        # back and low; front paws reaching forward, back legs folded under (the old crouch read as
        # running)
        body(hip_drop=0.15, chest_drop=0.24, tail=(0, 1.0, -0.10), neck=(0, -1.0, 0.18), head_pitch=0)
        legs({"L": (0.085, -0.30, 0.035), "R": (-0.085, -0.25, 0.035)}, {"L": (0.09, 0.25, 0.035), "R": (-0.09, 0.27, 0.035)},
             fhint=(0, 0.7, 0.3), bhint=(0, -1, 0.6))

    def stalk_paw():
        # v0.13: stalking, frozen mid-step, one front paw lifted and bent, the hind legs bunched under ready to
        # spring, belly low, head low and level on the prey, the tail low (crawling on all four legs stretched
        # out, the stalking cat read as "creeping or running toward" the bird, "or just running past")
        # (v0.14: a lower crouch with the rump level with the shoulders, the hind legs folded under and the tail low was
        # read on the bench side by side with this one, three scenes each: it read as "running or creeping toward the
        # bird" twice, this one as "crouched low ... stalking" three times, so this one stays)
        body(hip_drop=0.10, chest_drop=0.19 if STALK47 in ("B", "C") else 0.22, tail=(0, 1.0, -0.12), neck=(0, -1.0, 0.10), head_pitch=0)
        rig.aim_dir("tail2", (0, 1.0, 0.2))
        s41 = os.environ.get("TPDB_STALK41", "O")    # v0.41 bench (vision/isolation_v041.md): O
        if STALK47 in ("B", "C"):
            # v0.47 (TPDB_STALK47): see the switch (the far and the near forepaw's place fore and aft, the near forepaw's height, the far and
            # the near hind paw's place)
            fl, fr, fz, bl, br = (-0.12, -0.36, 0.07, 0.10, 0.26) if STALK47 == "C" else (-0.24, -0.34, 0.08, 0.15, 0.18)
            legs({"L": (0.085, fl, 0.035), "R": (-0.085, fr, fz)}, {"L": (0.08, bl, 0.035), "R": (-0.08, br, 0.035)},
                 fhint=(0, 1, 0.8), bhint=(0, -1, 0.7))
            return
        if CAT42 == "B":
            # v0.42: a long stride, the near (right) legs outside the far ones, the near forepaw lifted well ahead and the near hind paw well back
            legs({"L": (0.10, -0.22, 0.035), "R": (-0.10, -0.40, 0.11)}, {"L": (0.10, 0.10, 0.035), "R": (-0.10, 0.27, 0.035)},
                 fhint=(0, 1, -0.6), bhint=(0, -1, 0.7))
            return
        if CAT42 == "C":
            # (v0.42: the far legs outside, the near forepaw lifted just ahead of the far one)
            legs({"L": (0.10, -0.36, 0.035), "R": (-0.10, -0.26, 0.12)}, {"L": (0.10, 0.27, 0.035), "R": (-0.10, 0.12, 0.035)},
                 fhint=(0, 1, -0.6), bhint=(0, -1, 0.7))
            return
        if s41 == "B":
            # v0.41 (vision/flaws_v040.md O3): at 45 the lifted far forepaw crossed the near leg and the hind paws stood under the belly, "legs
            # bunched up and a bit tangled under its body" (two pictures). The paws apart, the hind ones further back, and the near forepaw
            # lifted, reaching ahead mid-step
            legs({"L": (0.10, -0.40, 0.09), "R": (-0.10, -0.28, 0.035)}, {"L": (0.10, 0.20, 0.035), "R": (-0.10, 0.25, 0.035)},
                 fhint=(0, 1, -0.6), bhint=(0, -1, 0.7))
            return
        if s41 == "C":
            # (v0.41: the paws apart, the far forepaw just off the ground)
            legs({"L": (0.10, -0.30, 0.035), "R": (-0.10, -0.38, 0.06)}, {"L": (0.10, 0.22, 0.035), "R": (-0.10, 0.27, 0.035)},
                 fhint=(0, 1, -0.6), bhint=(0, -1, 0.7))
            return
        legs({"L": (0.085, -0.27, 0.035), "R": (-0.085, -0.33, 0.17)}, {"L": (0.08, 0.15, 0.035), "R": (-0.08, 0.18, 0.035)},
             fhint=(0, 1, -0.6), bhint=(0, -1, 0.7))

    def graze():
        # v0.8: grazing, muzzle down in the grass (sniffing read as "about to butt" or "sniffing")
        g40 = os.environ.get("TPDB_GRAZE40", "C")
        if g43 and GOAT43 == "B":
            # v0.43 (TPDB_GOAT43): the withers raised and the hips a little lower, the hind feet further back so the hind legs stay straight, the neck
            # bent down from the withers, the front knees a little bent (at 45 and 135 the rump stood highest, "the back is high and hunched")
            body(hip_drop=0.045, chest_drop=-0.04, neck=(0, -0.62, -0.78), head_pitch=-50, tail=(0, 0.45, 0.85))
            legs({"L": (0.075, -0.13, 0.04), "R": (-0.075, -0.13, 0.04)}, {"L": (0.075, 0.25, 0.04), "R": (-0.075, 0.25, 0.04)}, fhint=(0, -1, 0.1),
                 bhint=(0, -1, 0.25))
            return
        if kind == "goat" and yb:
            # v0.42's goat: on its shorter legs and longer neck, the neck reaching further forward, so the head is ahead of the front legs, the back level
            # (bench round 2 sloped it down to the rump, the hind legs bent: still "hunched" at 135, and at 90 "kneeling or bowing on its front legs")
            body(hip_drop=0.0, chest_drop=0.0, neck=(0, -0.78, -0.62), head_pitch=-48, tail=(0, 0.45, 0.85))
            legs(*paws(fy=-0.16))
            return
        if ART39 == "B" and kind == "goat" and g40 in ("B", "C"):
            # v0.40 (vision/flaws_v039.md O2): the back level on straight legs and the neck reaching forward and down, the head ahead of the front
            # legs with its face showing. v0.39's neck straight down from a high back read "the back is a tall, hunched arch, the rear sticks up"
            # on the bench, and in the screen the head "blends into the grass tuft". Hips and chest lowered together, the goat crouched on bent
            # knees. "B" the mouth at the grass; "C" the chest a little higher, the head further ahead
            if g40 == "B":
                body(hip_drop=0.03, chest_drop=0.03, neck=(0, -0.60, -0.80), head_pitch=-62, tail=(0, 0.45, 0.85))
                legs(*paws(fy=-0.18))
            else:
                body(hip_drop=0.0, chest_drop=-0.04, neck=(0, -0.55, -0.84), head_pitch=-60, tail=(0, 0.45, 0.85))
                legs(*paws(fy=-0.16))
            return
        if ART39 == "B" and kind == "goat":
            # v0.39 (TPDB_ART39): the long neck lowered to the grass on straight front legs, the hind legs a little bent at the hock (the front
            # legs bent under a tall straight back read as "contorted")
            body(chest_drop=0.03, neck=(0, -0.42, -0.91), head_pitch=-88, tail=(0, 0.35, 0.95))
            legs(*paws(fy=-0.18))
            return
        body(chest_drop=0.08, neck=(0, -0.75, -0.65), head_pitch=-82, tail=(0, 0.5, 0.8))
        legs(*paws(fy=-0.15))

    def look_up():
        body(head_pitch=38, neck=(0, -0.35, 1), tail=(0, 0.5, 1.0))
        legs(*paws())

    def beg():
        # v0.9: begging, sitting square with the haunches and tail on the ground, the body leaning
        # less steeply, the head tipped right up toward the food (the upright sit read as rearing up,
        # standing and looking up as just watching)
        style = os.environ.get("TPDB_BEG", "A3")   # v0.23: A3 (bench A and A2: "sits up ... as if begging" in all four)
        b41 = os.environ.get("TPDB_BEG41", "F")
        if style == "A3" and BEG42 == "B":
            # v0.42 (TPDB_BEG42): on the haunches, the rump on the ground, the stifles up, the hocks flat and the hind paws forward under the body; the
            # trunk upright, shorter and rounder; the forelegs folded as v0.41's, the head tipped up as much (the gaze check)
            # (v0.43, TPDB_DOG43's shorter legs: the hips 0.01 higher, as the validator's ground rule needs; at 0.38 the rump was 32.9 px past the
            # ground point, 31 allowed)
            body(hip_drop=0.37 if (kind == "dog" and DOG43 == "B") else 0.38, hip_back=-0.04, chest_drop=-0.30, chest_y=0.16, tail=(-0.55, 0.45, -0.70),
                 neck=(0, -0.28, 1), head_pitch=38, spine_scale=(1.12, 0.80, 1.12))
            state["hock"] = (0, 0.085, 0.012)
            rig.aim_dir("tail2", (-0.35, -0.90, -0.05))
            fz = chest_z * 0.72
            legs({"L": (0.065, -0.04, fz), "R": (-0.065, -0.04, fz)}, {"L": (0.10, 0.08, 0.030), "R": (-0.10, 0.10, 0.030)},
                 fhint=(0, -1, -0.2), bhint=(0, -1, 1.2))
            return
        if style == "A3" and b41 == "F":
            # v0.41 bench round 2 (vision/isolation_v041.md): A3's body and head with the forelegs folded, the elbows forward and the paws tipped
            # down at the chest. In round 1 every beg, A3 too, had forelegs held out "like stiff rods", "like a human arm reaching out"
            body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.30, chest_y=0.0, tail=(-0.55, 0.45, -0.70), neck=(0, -0.20, 1), head_pitch=38)
            rig.aim_dir("tail2", (-0.35, -0.90, -0.05))
            fz = chest_z * 0.72
            legs({"L": (0.065, -0.14, fz), "R": (-0.065, -0.14, fz)}, {"L": (0.10, -0.06, 0.035), "R": (-0.10, -0.04, 0.035)},
                 fhint=(0, -1, -0.2), bhint=(0, -1, 0.35))
            return
        if style == "A3" and b41 in ("B", "C"):
            # v0.41 (vision/flaws_v040.md O2): A3 in profile was "stretched-upright", "far-back head tilt", "stiff and human-like" (two pictures at 90;
            # none at 45). The body leans forward from the haunches, the head is tipped up less, toward the person rather than the sky, and the
            # forepaws are held out ahead and lower. "B" leaning further; "C" between B and A3. (The head at 30: tipped up 18 or 20, at 45 the gaze
            # passed under the eater's food, and the template placed on none of 40 street seeds)
            if b41 == "B":
                body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.14, chest_y=-0.15, tail=(-0.55, 0.45, -0.70), neck=(0, -0.45, 1), head_pitch=30)
                fy, fz = -0.30, chest_z * 0.48
            else:
                body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.20, chest_y=-0.10, tail=(-0.55, 0.45, -0.70), neck=(0, -0.40, 1), head_pitch=30)
                fy, fz = -0.26, chest_z * 0.57
            rig.aim_dir("tail2", (-0.35, -0.90, -0.05))
            legs({"L": (0.065, fy, fz), "R": (-0.065, fy, fz)}, {"L": (0.10, -0.06, 0.035), "R": (-0.10, -0.04, 0.035)},
                 fhint=(0, -0.2, -1), bhint=(0, -1, 0.35))
            return
        if style == "A3":
            # as A2, the tail curled tight round the near haunch instead of laid out on the ground behind (laid out, the
            # sitting dog's "lower body stretches long and flat ... like a kangaroo")
            body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.30, chest_y=0.0, tail=(-0.55, 0.45, -0.70), neck=(0, -0.20, 1), head_pitch=38)
            rig.aim_dir("tail2", (-0.35, -0.90, -0.05))
            fz = chest_z * 0.62
            legs({"L": (0.065, -0.17, fz), "R": (-0.065, -0.17, fz)}, {"L": (0.10, -0.06, 0.035), "R": (-0.10, -0.04, 0.035)},
                 fhint=(0, -0.2, -1), bhint=(0, -1, 0.35))
            return
        if style == "A2":
            # v0.23 bench round 2: as A, with the hind legs folded under the haunches instead of stretched forward (A's hind
            # paws out in front read "as if kneeling", "legs stretched forward like a person")
            body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.30, chest_y=0.0, tail=(0.35, 0.75, -0.55), neck=(0, -0.20, 1), head_pitch=38)
            rig.aim_dir("tail2", (0.55, -0.80, -0.05))
            fz = chest_z * 0.62
            legs({"L": (0.065, -0.17, fz), "R": (-0.065, -0.17, fz)}, {"L": (0.10, -0.06, 0.035), "R": (-0.10, -0.04, 0.035)},
                 fhint=(0, -0.2, -1), bhint=(0, -1, 0.35))
            return
        if style == "A":
            # v0.23 bench A: sitting up on the haunches, both front paws lifted and folded at the chest, the tail curled
            # forward along the ground (the v0.9 slope, its tail stretched out behind, read "as if half-lying")
            body(hip_drop=0.40, hip_back=-0.04, chest_drop=-0.30, chest_y=0.0, tail=(0.35, 0.75, -0.55), neck=(0, -0.20, 1), head_pitch=38)
            rig.aim_dir("tail2", (0.55, -0.80, -0.05))
            fz = chest_z * 0.62
            legs({"L": (0.065, -0.17, fz), "R": (-0.065, -0.17, fz)}, {"L": (0.11, -0.17, 0.035), "R": (-0.11, -0.15, 0.035)},
                 fhint=(0, -0.2, -1), bhint=(0, -0.3, 1))
            return
        if style == "B":
            # v0.23 bench B: sitting square and upright as in sit(), the near front paw lifted toward the food, the head
            # tipped up, the tail curled forward beside the haunch
            body(hip_drop=0.25, hip_back=-0.12, chest_drop=-0.05, tail=(0.35, 0.75, -0.55), neck=(0, -0.22, 1), head_pitch=38)
            rig.aim_dir("tail2", (0.55, -0.80, -0.05))
            legs({"L": (0.075, -0.165, 0.04), "R": (-0.075, -0.24, chest_z * 0.45)}, {"L": (0.10, 0.00, 0.035), "R": (-0.10, 0.02, 0.035)},
                 fhint=(0, 0.3, 0.1), bhint=(0, -1, 0.35))
            return
        body(hip_drop=0.30, hip_back=-0.10, chest_drop=0.07, tail=(0.25, 0.95, -0.45), neck=(0, -0.30, 1), head_pitch=40)
        legs({"L": (0.075, -0.215, 0.04), "R": (-0.075, -0.215, 0.04)}, {"L": (0.10, 0.01, 0.035), "R": (-0.10, 0.03, 0.035)},
             fhint=(0, 0.3, 0.1), bhint=(0, -1, 0.35))

    def sniff():
        body(chest_drop=0.05, neck=(0, -1.0, -0.15), head_pitch=-70, tail=(0, 0.6, 0.8))
        legs(*paws(fy=-0.17))

    def play_bow():
        # v0.12: the hind legs apart, hocks bent, and the tail raised at a slant (both hind legs on one line
        # and a straight upright tail read as one stiff stick: "stretching or play-bowing")
        body(hip_drop=-0.02, chest_drop=0.24, neck=(0, -0.9, 0.55), head_pitch=12, tail=(0, 0.55, 0.85))
        legs({"L": (0.085, -0.38, 0.035), "R": (-0.085, -0.36, 0.035)}, {"L": (0.075, 0.13, 0.04), "R": (-0.075, 0.28, 0.04)},
             fhint=(0, 1, -0.5), bhint=(0, -1, 0.45))

    # v0.15: the poses that earlier releases replaced (lie, sleep, crouch, look_up, sit_look_down, stalk,
    # sleep_curl) are retired; no template asks for them, so they leave the cast and the gallery
    plan = [("stand", stand), ("walk", walk), ("sit", sit), ("sniff", sniff), ("play_bow", play_bow)]
    if kind == "dog":
        plan.append(("sit_wait", sit_wait))
        plan.append(("beg", beg))
        plan.append(("sit_up_hold", sit_up_hold))
        if READ43 == "A":
            plan.append(("down_read", down_read))
        if READ47 in ("B", "C", "D", "E"):
            plan.append(("sit_read", sit_read))
        if HOSE47 in ("B", "D"):
            plan.append(("stand_hose", stand_hose))
    if kind == "cat":
        plan.append(("stalk_paw", stalk_paw))
    if kind == "dog":
        plan.append(("sleep_ball", sleep_ball))
        plan.append(("sleep_paws", sleep_paws))
        plan.append(("sleep_paws_turn", sleep_paws_turn))
    if kind == "cat":
        plan.append(("sleep_tuck", sleep_tuck))
    if os.environ.get("TPDB_EXP") and kind in ("cat", "dog", "goat"):
        # pose experiments for the isolation bench (never set in a release build; v0.41: the goat too)
        for i, d in enumerate(json.loads(os.environ["TPDB_EXP"])):
            def _exp(d=d):
                body(**d["body"])
                if d.get("hock"):
                    state["hock"] = tuple(d["hock"])
                legs({"L": tuple(d["fL"]), "R": tuple(d["fR"])}, {"L": tuple(d["bL"]), "R": tuple(d["bR"])},
                     fhint=tuple(d.get("fh", (0, 1, 0.2))), bhint=tuple(d.get("bh", (0, -1, -0.3))))
                if d.get("tail2"):
                    rig.aim_dir("tail2", tuple(d["tail2"]))
            plan.append((f"exp{i}", _exp))
    if kind == "goat":
        plan = [p for p in plan if p[0] != "sit"]       # goats lie down rather than sit
        if ART39 == "B":
            # (a goat stands, walks and grazes: the dog's play bow and sniff are not its poses)
            plan = [p for p in plan if p[0] not in ("play_bow", "sniff")]
        plan.append(("graze", graze))
    for nm, fn in plan:
        pose(nm, fn)
    rig.reset()
    return names


# ================================================================== birds
def build_bird(spec):
    kind = spec.get("kind", "songbird")
    S = spec.get("scale", 1.0)
    duck = kind == "duck"

    def P(x, y, z):
        return Vector((x * S, y * S, z * S))

    root = link(bpy.data.objects.new("ROOT", None))
    if duck:
        bz, hz, hy = 0.12, 0.27, -0.10
    else:
        bz, hz, hy = 0.10, 0.17, -0.045
    bones = {
        "body": (P(0, 0, bz - 0.04), P(0, 0, bz + 0.04), None),
        "neck": (P(0, hy * 0.5, bz + 0.03), P(0, hy, hz - 0.03), "body"),
        "head": (P(0, hy, hz - 0.03), P(0, hy, hz + 0.05), "neck"),
        "tail": (P(0, 0.05, bz + 0.01), P(0, 0.14, bz + 0.05), "body"),
    }
    for sd, sg in (("L", 1), ("R", -1)):
        bones[f"wing_{sd}"] = (P(sg * 0.045, -0.01, bz + 0.03), P(sg * 0.050, 0.07, bz + 0.02), "body")
        bones[f"leg_{sd}"] = (P(sg * 0.025, 0.0, bz - 0.04), P(sg * 0.025, 0.0, 0.005), "body")
    rig = Rig(root, bones)
    k = S
    col, bel, acc = spec["body"], spec.get("belly", spec["body"]), spec.get("accent", "yellow")
    if duck:
        ellipsoid("Body", P(0, 0.02, bz), (0.090 * k, 0.140 * k, 0.075 * k), col, rig, "body", rot=Quaternion((1, 0, 0), -0.15))
        ellipsoid("Neck", P(0, -0.07, bz + 0.08), (0.040 * k, 0.040 * k, 0.070 * k), col, rig, "neck")
        hr = 0.052 * k
    else:
        ellipsoid("Body", P(0, 0.012, bz), (0.055 * k, 0.078 * k, 0.052 * k), col, rig, "body", rot=Quaternion((1, 0, 0), -0.35))
        ellipsoid("Belly", P(0, -0.020, bz - 0.010), (0.044 * k, 0.045 * k, 0.040 * k), bel, rig, "body")
        hr = 0.043 * k
    hc = P(0, hy, hz)
    ellipsoid("Head", hc, (hr, hr, hr), col, rig, "head", seg=28, rings=16)
    tail_tip = P(0, 0.15, bz + (0.06 if not duck else 0.08))
    ob = cyl("Tail", P(0, 0.05, bz + 0.01), tail_tip, 0.028 * k, spec.get("tail_col", col), seg=4, r1=0.012 * k)
    rig.attach(ob, "tail")
    for sd, sg in (("L", 1), ("R", -1)):
        if duck:
            # a smaller wing set back and tilted up toward the tail, so the body still reads as a body
            ellipsoid(f"Wing_{sd}", P(sg * 0.074, 0.050, bz + 0.035), (0.018 * k, 0.070 * k, 0.030 * k), spec.get("wing_col", col), rig, f"wing_{sd}",
                      rot=Quaternion((1, 0, 0), -0.50))
        else:
            ellipsoid(f"Wing_{sd}", P(sg * 0.050, 0.025, bz + 0.02), (0.014 * k, 0.065 * k, 0.034 * k), spec.get("wing_col", col), rig, f"wing_{sd}",
                      rot=Quaternion((1, 0, 0), -0.3))
        lc = spec.get("leg_col", "orange")
        if duck:
            ob = cyl(f"Leg_{sd}", P(sg * 0.035, 0.0, bz - 0.05), P(sg * 0.035, -0.005, 0.012), 0.010 * k, lc)
            rig.attach(ob, f"leg_{sd}")
            ellipsoid(f"Foot_{sd}", P(sg * 0.035, -0.02, 0.008), (0.030 * k, 0.040 * k, 0.008 * k), lc, rig, f"leg_{sd}")
        else:
            ob = cyl(f"Leg_{sd}", P(sg * 0.022, 0.0, bz - 0.04), P(sg * 0.022, 0.0, 0.006), 0.0055 * k, lc)
            rig.attach(ob, f"leg_{sd}")
            for i, a in enumerate((-0.5, 0.0, 0.5)):
                d = Vector((math.sin(a) * 0.4, -math.cos(a), 0)) * 0.022 * k
                ob = cyl(f"Toe_{sd}{i}", P(sg * 0.022, 0.0, 0.004), P(sg * 0.022, 0.0, 0.004) + d, 0.004 * k, lc)
                rig.attach(ob, f"leg_{sd}")

    face = Face(rig, "head", hc, (hr, hr, hr), k * (0.30 if not duck else 0.36), prefix="F")
    fk = face.k
    eye_dx, eye_z = hr * 0.52, hr * 0.18
    A47 = ANIM47 == "B"
    if A47:
        # v0.47 (TPDB_ANIM47): one pair of eyes, on the sides of the head (a songbird 50 degrees round it, a duck 48): one full eye in a side
        # view and at three-quarters (the songbird had a pair in front and a pair on the sides, "two eyes side by side"; the duck's, 31
        # degrees round, lay on the head's edge in a side view, "no eye")
        eye_dx = hr * (0.74 if duck else 0.77)
    # beak: upper and lower halves so "sing" can open it
    bl = 0.040 * k if not duck else 0.060 * k
    bw = 0.013 * k if not duck else 0.026 * k
    base = face.at(0, -hr * 0.05, -0.004 * k)
    up = ellipsoid("BeakUp", (0, 0, 0), (1, 1, 1), acc)
    lo = ellipsoid("BeakLo", (0, 0, 0), (1, 1, 1), acc)
    if duck:
        Mu = Matrix.LocRotScale(base + Vector((0, -bl * 0.55, 0.004 * k)), Quaternion(), Vector((bw, bl * 0.6, 0.010 * k)))
        Ml = Matrix.LocRotScale(base + Vector((0, -bl * 0.45, -0.008 * k)), Quaternion(), Vector((bw * 0.9, bl * 0.5, 0.008 * k)))
    else:
        Mu = Matrix.LocRotScale(base + Vector((0, -bl * 0.45, 0.003 * k)), Quaternion(), Vector((bw, bl * 0.55, 0.008 * k)))
        Ml = Matrix.LocRotScale(base + Vector((0, -bl * 0.35, -0.006 * k)), Quaternion(), Vector((bw * 0.85, bl * 0.42, 0.006 * k)))
    face.place("beak_up", up, Mu)
    face.place("beak_lo", lo, Ml)
    if not duck and __import__("os").environ.get("TPDB_PECK", "B") == "B" and not A47:
        # v0.27: an eye on the side of the head, where a bird has one (from the side the head was "a red ball")
        for sd, sg in (("L", 1), ("R", -1)):
            ellipsoid(f"EyeSide_{sd}", hc + Vector((sg * hr * 0.86, -hr * 0.34, hr * 0.26)), (0.006 * k, 0.0105 * k, 0.0105 * k), "charcoal", rig, "head")
    Ml_open = Matrix.Translation(base) @ Matrix.Rotation(math.radians(28), 4, "X") @ Matrix.Translation(-base) @ Ml
    r_e = hr * (0.24 if A47 else 0.20)
    for sd, sg in (("L", 1), ("R", -1)):
        x = sg * eye_dx
        face.place(f"eye_{sd}", ellipsoid("eye", (0, 0, 0), (1, 1, 1), "outline"), face.frame(x, eye_z, 0.0, scale=(r_e * 0.85, r_e * 0.5, r_e * 1.1)))
        face.place(f"catch_{sd}", ellipsoid("catch", (0, 0, 0), (1, 1, 1), "cream"), face.frame(x + r_e * 0.3 * sg, eye_z + r_e * 0.45, r_e * 0.35, scale=(r_e * 0.28, r_e * 0.2, r_e * 0.34)))
        w = r_e * 1.1
        face.curve_on(f"arcdn_{sd}", [(x - w, eye_z + r_e * 0.1), (x, eye_z - r_e * 0.5), (x + w, eye_z + r_e * 0.1)], r_e * 0.22, "outline", r_e * 0.15)

    expr = {"neutral": ({"eye_L", "eye_R", "catch_L", "catch_R", "beak_up", "beak_lo"}, False),
            "sing": ({"eye_L", "eye_R", "catch_L", "catch_R", "beak_up", "beak_lo"}, True),
            "sleepy": ({"arcdn_L", "arcdn_R", "beak_up", "beak_lo"}, False)}
    states = {}
    for name, (show, opened) in expr.items():
        st = {ob.name: {"hide": key not in show} for key, ob in face.objs.items()}
        st[face.objs["beak_lo"].name]["basis"] = list_m(Ml_open if opened else Ml)
        states[name] = st

    for sd, sg in (("L", 1), ("R", -1)):
        anchor(rig, f"eye_{sd}", face.at(sg * eye_dx, eye_z), "head")
        anchor(rig, f"foot_{sd}", P(sg * 0.025, 0.0, 0.0), f"leg_{sd}")
    mid = (face.at(eye_dx, eye_z) + face.at(-eye_dx, eye_z)) / 2
    anchor(rig, "gaze_target", mid + Vector((0, -1.0, 0)), "head")
    anchor(rig, "head_top", hc + Vector((0, 0, hr + 0.005 * k)), "head")
    anchor(rig, "mouth", base + Vector((0, -bl, 0)), "head")
    names = make_bird_poses(rig, S, duck, bz)
    return rig, states, names


def make_bird_poses(rig, S, duck, bz):
    names = []

    def pose(name, fn):
        rig.reset()
        fn()
        rig.key_pose(name)
        names.append(name)

    def perch():
        pass

    def peck():
        pb = rig.arm.pose.bones["body"]
        upd()
        M = pb.matrix.copy()
        h = Vector((0, 0, 0.004 * S))
        if PECK47 in ("B", "C", "D") and not duck:
            # v0.47 (TPDB_PECK47): see the switch (the body's tip, the neck and the face below level, in degrees; the body lowered; the widest
            # the legs may splay; the pivot of the tip, 0 the feet, 1 the hips)
            tip, nk, fc, dz, cap, pv = {"B": (34, 60, 66, 0.0, 40, 0.0), "C": (40, 74, 46, 0.011, 60, 0.0), "D": (58, 84, 46, 0.0, 60, 1.0)}[PECK47]
            hp = Vector((0, rig.head("leg_L").y * pv, h.z + (rig.head("leg_L").z - h.z) * pv))
            pb.matrix = Matrix.Translation(hp - Vector((0, 0, dz * S))) @ Matrix.Rotation(math.radians(tip), 4, "X") @ Matrix.Translation(-hp) @ M
            upd()
            a = math.radians(nk)
            rig.aim_dir("neck", (0, -math.cos(a), -math.sin(a)))
            a = math.radians(fc)
            rig.aim_dir("head", (0, -math.sin(a), math.cos(a)))
            rig.aim_dir("tail", (0, 1, 0.12))
            # (the legs apart fore and aft, the near one forward, as far as keeps both feet on the ground under the lowered body)
            for sd, sg in (("L", 1), ("R", -1)):
                c = (rig.head(f"leg_{sd}").z - 0.004 * S) / rig.arm.pose.bones[f"leg_{sd}"].bone.length
                ph = min(math.acos(max(-1.0, min(1.0, c))), math.radians(cap))
                rig.aim_dir(f"leg_{sd}", (0, sg * math.sin(ph), -math.cos(ph)))
            return
        b27 = __import__("os").environ.get("TPDB_PECK", "B") == "B"
        # v0.27, chosen on the bench: the body less tipped, the head out in front of it (its head a ball at the ground under a tail standing up: "could be tumbling or injured")
        pb.matrix = Matrix.Translation(h) @ Matrix.Rotation(math.radians(20 if b27 else 28), 4, "X") @ Matrix.Translation(-h) @ M
        upd()
        rig.aim_dir("neck", (0, -0.62, -0.95) if b27 else (0, -0.9, -0.5))
        # (the head bone runs up through the crown, so aiming it this way tips the face about 40 degrees below level, eye and beak showing)
        rig.aim_dir("head", (0, -0.64, 0.77) if b27 else (0, -0.7, -0.6))
        if b27:
            rig.aim_dir("tail", (0, 1, 0.12))
        for sd in ("L", "R"):
            rig.aim_dir(f"leg_{sd}", (0, 0.05, -1))

    def fly():
        # wings raised and lengthened, legs tucked back, tail streaming
        rig.arm.pose.bones["body"].location = (0, 0.05 * S, 0)
        upd()
        for sd, sg in (("L", 1), ("R", -1)):
            rig.aim_dir(f"wing_{sd}", (sg * 0.45, 0.30, 1.0))
            rig.arm.pose.bones[f"wing_{sd}"].scale = (1.0, 1.9, 1.35)
            rig.aim_dir(f"leg_{sd}", (0, 1, -0.15))
        rig.aim_dir("tail", (0, 1, 0.1))
        upd()

    def sing():
        rig.aim_dir("neck", (0, -0.25, 1))
        rig.aim_dir("head", (0, -0.3, 1))

    def swim():
        # lower the body so the waterline sits at the root origin; tuck the legs
        rig.arm.pose.bones["body"].location = (0, -(bz - 0.075) * S, 0)
        upd()
        for sd in ("L", "R"):
            rig.aim_dir(f"leg_{sd}", (0, 1, 0.2))
            if __import__("os").environ.get("TPDB_DUCK45", "A") == "A":     # v0.45 bench (vision/isolation_v045.md): A
                # v0.45 bench (look review, TPDB_DUCK45): an orange foot showed under the floating body ("the duck stands on the water"); out of sight
                rig.arm.pose.bones[f"leg_{sd}"].scale = (0.02, 0.02, 0.02)

    def swim_eat():
        # v0.29: as swim, the neck stretched out and down and the bill at the water, for a crumb there (upright with the crumbs ahead of it, the duck was "swimming towards those crumbs")
        swim()
        # (with the neck down along the breast and the tail up, three of three: "lying on its side or collapsed", "tipped over"; so the neck straight out and the body as it is)
        rig.aim_dir("neck", (0, -0.98, 0.04))
        rig.aim_dir("head", (0, -0.72, 0.70))

    def swim_look():
        # v0.29 bench: as swim, the neck arched forward and the head bent down over a crumb just ahead of it
        swim()
        rig.aim_dir("neck", (0, -0.62, 0.72))
        rig.aim_dir("head", (0, -0.78, 0.62))

    plan = [("perch", perch), ("peck", peck), ("fly", fly), ("sing", sing)]
    if duck:
        plan.append(("swim", swim))
        plan.append(("swim_eat", swim_eat))
        plan.append(("swim_look", swim_look))
    for nm, fn in plan:
        pose(nm, fn)
    rig.reset()
    return names
