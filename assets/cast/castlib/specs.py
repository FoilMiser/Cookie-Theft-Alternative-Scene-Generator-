"""The v0.4 stand-in cast: who they are, what they wear, how speakers would name them."""
import os

PERSON_AFFORDANCES = ["hold", "reach", "look_at", "point", "wave", "sit_on", "carry", "walk"]


def L(everyday, accepted, category, age, skin, hair):
    return dict(everyday_name=everyday, accepted_names=accepted, category=category,
                person=dict(age_group=age, skin_tone=skin, hair=hair))


PEOPLE = {
    "person.ana": dict(age="adult", scale=0.985, skin="skin2", hair="long", hair_col="charcoal", top="tee", shirt="purple",
                       bottom="pants", pants="teal", shoes="charcoal", build=dict(chest=0.96, waist=0.90, hips=1.06),
                       belt="charcoal", buckle="gray",
                       labels=L("woman", ["woman", "lady", "mother", "mom", "person"], "adult_person", "adult", "skin2", "long_dark")),
    "person.ben": dict(age="adult", scale=1.03, skin="skin1", hair="short", hair_col="hair_brown", top="tee", shirt="red",
                       bottom="pants", pants="blue", shoes="charcoal", build=dict(chest=1.08, waist=1.02, depth=1.05),
                       belt="brown", buckle="sun",
                       labels=L("man", ["man", "guy", "father", "dad", "person"], "adult_person", "adult", "skin1", "short_brown")),
    "person.kai": dict(age="child", scale=1.0, skin="skin3", hair="curly", hair_col="charcoal", top="tee", shirt="yellow",
                       bottom="shorts", pants="orange", shoes="slate", build=dict(waist=1.06, depth=1.08),
                       labels=L("child", ["child", "kid", "boy", "girl", "son", "daughter"], "child_person", "child", "skin3", "curly_dark")),
    "person.rosa": dict(age="older_adult", scale=0.955, skin="skin1", hair="bun", hair_col="hair_gray", top="cardigan", shirt="teal",
                        inner="cream", bottom="skirt", pants="slate", shoes="brown", glasses=True, build=dict(hips=1.05, depth=1.04),
                        labels=L("grandmother", ["grandmother", "grandma", "old woman", "older woman", "lady", "woman"],
                                 "adult_person", "older_adult", "skin1", "gray_bun")),
    "person.tomas": dict(age="older_adult", scale=1.0, skin="skin2", hair="bald_ring", hair_col="hair_white", facial_hair="mustache",
                         top="vest", shirt="cream", sleeves="long", vest="brown", bottom="pants", pants="charcoal", shoes="brown",
                         belt="charcoal", buckle="gray", hat="cap", hat_col="slate",
                         build=dict(chest=1.05, waist=1.12, hips=1.04, depth=1.06, belly=1.0),
                         labels=L("grandfather", ["grandfather", "grandpa", "old man", "older man", "man"],
                                  "adult_person", "older_adult", "skin2", "gray_ring")),
    "person.dev": dict(age="adult", scale=1.04, skin="skin3", hair="buzz", hair_col="charcoal", facial_hair="beard",
                       top="tee", shirt="green", bottom="pants", pants="khaki", shoes="brown", belt="charcoal", buckle="gray",
                       build=dict(chest=1.10, waist=1.04, depth=1.06, limbs=1.06),
                       labels=L("man", ["man", "guy", "father", "dad", "person"], "adult_person", "adult", "skin3", "buzz_beard")),
    "person.mei": dict(age="adult", scale=0.98, skin="skin4", hair="bob", hair_col="charcoal", top="tee", shirt="yellow",
                       bottom="dress", shoes="red", build=dict(chest=0.92, waist=0.86, hips=1.02),
                       labels=L("woman", ["woman", "lady", "mother", "mom", "person"], "adult_person", "adult", "skin4", "black_bob")),
    "person.leo": dict(age="teen", scale=0.92, head_scale=1.05, skin="skin1", hair="ponytail", hair_col="hair_brown", tie="red",
                       top="hoodie", shirt="blue", bottom="pants", pants="charcoal", shoes="white",
                       build=dict(chest=0.94, waist=0.92, depth=0.96, limbs=0.94),
                       labels=L("teenager", ["teenager", "teen", "boy", "girl", "kid", "young person"], "teen_person", "teen", "skin1", "brown_ponytail")),
    "person.nia": dict(age="child", scale=0.86, head_scale=1.04, skin="skin2", hair="puffs", hair_col="charcoal", top="tee", shirt="pink",
                       bottom="dress", shoes="yellow",
                       labels=L("girl", ["girl", "little girl", "child", "kid", "daughter"], "child_person", "child", "skin2", "puffs")),
    "person.jo": dict(age="adult", scale=1.0, skin="skin4", hair="short", hair_col="brown", top="vest", shirt="slate", vest="orange", vest_style="hivis",
                      bottom="pants", pants="navy", shoes="charcoal", hat="cap", hat_col="orange", build=dict(chest=1.02),
                      labels=L("worker", ["worker", "man", "woman", "person", "gardener", "delivery person"], "adult_person", "adult", "skin4", "short_cap")),
}

# v0.24 bench (TPDB_TEEN): no v0.23 reader called the teenager a teenager ("a woman with a brown ponytail", 13 items).
# Each candidate is shorter, with a larger head: A a cap worn backwards, B the ponytail and a school backpack. v0.24: A,
# chosen on the bench (isolation_v024.md: "a boy or young man", "a teenager or a slim adult"; B's pack read as "a second
# ball" or "shield-like", and B stayed "a girl or young woman"). TPDB_TEEN=O builds the v0.23 teenager.
TEEN_STYLE = os.environ.get("TPDB_TEEN", "D")
TEEN_BUILD = dict(scale=0.88, head_scale=1.09, build=dict(chest=0.90, waist=0.90, depth=0.94, limbs=0.92))
if TEEN_STYLE == "A":
    PEOPLE["person.leo"].update(TEEN_BUILD, hair="short", hat="cap_back", hat_col="red")
elif TEEN_STYLE == "B":
    PEOPLE["person.leo"].update(TEEN_BUILD, backpack="orange")
elif TEEN_STYLE == "C":
    # v0.26 bench: a beanie has no peak to point the wrong way (seven v0.25 pictures remarked that the backwards peak points away
    # from his face, twice "the head is on the wrong way round")
    PEOPLE["person.leo"].update(TEEN_BUILD, hair="short", hat="beanie", hat_col="red", band_col="red")
elif TEEN_STYLE == "D":
    # v0.26 bench: the cap worn forwards, its peak the way he faces. v0.26: D (isolation_v026.md: "a boy or young man" in "a red baseball
    # cap", and no reader had his head the wrong way round). TPDB_TEEN=A builds the v0.24 and v0.25 teenager.
    PEOPLE["person.leo"].update(TEEN_BUILD, hair="short", hat="cap", hat_col="red")

# v0.26 bench (TPDB_OLD): the older man's head, the v0.25 screen's most repeated remark, in ten of his 21 pictures ("the older
# man's face is hard to read": a cap peak on one side, grey hair on the other, "something like an ear in the middle", "no clear
# eyes"; the crescent of hair "could be sideburns, a beard or an ear"). A: no cap, bald with the white fringe. B: no cap, short
# white hair. C: the cap kept, a shorter peak, short white hair under it, so there is no patch. v0.26: C, on the bench
# (isolation_v026.md: "an older man with grey hair and a blue-grey flat cap"; A's fringe was "a strap or bandage", and B's hair "a smooth
# grey cap"). TPDB_OLD=O builds the v0.25 man.
OLD_STYLE = os.environ.get("TPDB_OLD", "C")
if OLD_STYLE == "A":
    PEOPLE["person.tomas"].update(hat=None)
elif OLD_STYLE == "B":
    PEOPLE["person.tomas"].update(hat=None, hair="buzz")
elif OLD_STYLE == "C":
    PEOPLE["person.tomas"].update(hair="buzz", brim_short=True)

# v0.39 bench (TPDB_BEN39): the man in red read as a boy (9 of 24 mentions in v0.37, 5 of 32 in v0.38, the most of any grown man), and he
# hangs the washing. "B": taller and broader, a slightly smaller head and sideburns (a parting drew a bald stripe). "C": B and a short moustache. "O": v0.38.
BEN39 = os.environ.get("TPDB_BEN39", "C")  # v0.39 bench (vision/isolation_v039.md): C
if BEN39 in ("B", "C"):
    PEOPLE["person.ben"].update(scale=1.065, head_scale=0.95, sideburns=True, build=dict(chest=1.15, waist=1.04, depth=1.08, limbs=1.04))
if BEN39 == "C":
    PEOPLE["person.ben"].update(facial_hair="mustache", facial_hair_col="hair_brown")

# v0.41 bench (TPDB_MEI41): the woman in yellow was "a girl" in 6 of her 27 v0.40 pictures (5 of 24 in v0.39), watering, eating an ice cream, carrying
# a box, reading. "B": as Ben's in v0.39, as tall as the men with a smaller head, and a woman's figure, a fuller bust and hips; "C": B with the dress
# below the knee. "O": v0.40. (On a first look, B at 1.02 and a head of 0.94 was barely v0.40, and her hair in a bun stood on top like a topknot.)
MEI41 = os.environ.get("TPDB_MEI41", "O")  # v0.41 bench (vision/isolation_v041.md): O
if MEI41 in ("B", "C"):
    PEOPLE["person.mei"].update(scale=1.05, head_scale=0.90, build=dict(chest=1.06, waist=0.86, hips=1.14))
if MEI41 == "C":
    PEOPLE["person.mei"].update(hem_drop=0.12)

# v0.42 bench (TPDB_MEI42; figure-fixes-v041.md item 8, flaws_v041.md O3): still "a girl" in 8 of her 24 v0.41 pictures. The head before the
# clothes (RUNBOOK): "B" her hair drawn back into a low bun at the nape, an adult's, and as tall as the men with a smaller head. "O": v0.41
MEI42 = os.environ.get("TPDB_MEI42", "B")  # v0.42 bench (vision/isolation_v042.md): B
if MEI42 == "B":
    PEOPLE["person.mei"].update(hair="low_bun", scale=1.04, head_scale=0.92)

# v0.43 bench (TPDB_ADULT43; figure-fixes-v042.md item 3, vision/flaws_v042.md O1 and O2): the woman in yellow still "girl" in 6 of her 14 v0.42 pictures,
# her bun "a dark ponytail", and the woman in purple "girl" or "girl or young woman" in about ten of her 23; both drawn with the girls' large head and
# round face. The head first (RUNBOOK): "B" the head smaller again and the neck longer, a narrower, taller face with smaller eyes set lower and
# red lips, and the woman in yellow's bob back (v0.41). "C": B with the clothes and hair as well, the yellow dress to mid-calf and the woman in
# purple's long loose hair tied back in a ponytail (on a first look, tied back, it vanished from the front and she looked short-haired). "O": v0.42
ADULT43 = os.environ.get("TPDB_ADULT43", "B")  # v0.43 bench (vision/isolation_v043.md): B
if ADULT43 in ("B", "C"):
    # (and the woman in yellow's red shoes a darker red: "flat and splayed, almost flipper-like", bench round 1; figure-fixes-v042.md item 9)
    PEOPLE["person.mei"].update(hair="bob", head_scale=0.85, neck_add=0.025, adult_face=True, shoes="throat")
    PEOPLE["person.ana"].update(head_scale=0.90, neck_add=0.025, adult_face=True)
# v0.46 bench (vision/isolation_v046.md, TPDB_MEI46), "O" for v0.45's drawing. "B": her waist less pinched, 0.94 for 0.86 of the standard figure's
# (between a chest of 0.92 and hips of 1.02 it drew her in two lumps, the dress an hourglass)
MEI46 = os.environ.get("TPDB_MEI46", "B")
if MEI46 == "B":
    PEOPLE["person.mei"]["build"] = dict(PEOPLE["person.mei"].get("build", {}), waist=0.94)
if ADULT43 == "C":
    PEOPLE["person.mei"].update(hem_drop=0.12)
    PEOPLE["person.ana"].update(hair="ponytail", tie="charcoal")

# v0.49 (core.HEAD49): whose head has which jaw. Unnamed, a grown figure has the man's and a child the child's
for _fam, _h in (("person.ana", "woman"), ("person.mei", "woman"), ("person.rosa", "woman"), ("person.leo", "teen")):
    PEOPLE[_fam]["head49"] = _h
# v0.49 bench (TPDB_HS49; vision/isolation_v049.md, the age bench): a grown figure's head scaled by this against its body. 1.0 is v0.48's
_HS49 = float(os.environ.get("TPDB_HS49", "1.0"))
if _HS49 != 1.0:
    for _fam, _sp in PEOPLE.items():
        if _sp["age"] in ("adult", "older_adult"):
            _sp["head_scale"] = _sp.get("head_scale", 1.0) * _HS49
# v0.48 (people.HAIR48, face.FACE48): the two women's brows finer, and their hair parted differently so that they differ by more than colour
if os.environ.get("TPDB_HAIR48", "B") == "B":
    PEOPLE["person.mei"].update(part="center", brow=(0.92, 1.0, 0.80))
    PEOPLE["person.ana"].update(part="side", part_side="R", brow=(0.92, 1.0, 0.80))
    PEOPLE["person.rosa"].update(brow=(0.92, 1.0, 0.80))
    PEOPLE["person.nia"].update(brow=(0.90, 1.0, 0.84))
    PEOPLE["person.kai"].update(brow=(0.90, 1.0, 0.84))
    for _f, _a in (("person.mei", 0.88), ("person.ana", 0.90), ("person.rosa", 0.92), ("person.nia", 0.92)):
        PEOPLE[_f]["build"] = dict(PEOPLE[_f].get("build", {}), arms=_a)      # slimmer arms (people.py, "arms")

# v0.50 bench (TPDB_AGE50; vision/flaws_v049.md O1, vision/isolation_v050.md): the grown figures were called a girl or a boy first in 20 of their 89
# v0.49 pictures. Letters, any of them together: "M" marks of age (the woman in purple as tall as the woman in yellow, and a woman's bust; the woman in yellow a
# bust and her dress to below the knee; the man in green a fuller beard); "P" every grown figure's head smaller against its body. "O": v0.49's.
# v0.50: MP, on the bench in whole scenes (tools/cycle/age_scenes.py: 32 of v0.49's pictures built with each of four casts, 128 readings by
# sixteen readers, two pictures of each cast to a reader). Called young first, of the four figures' 45 appearances: O 13, M 3, P 5, MP 1
AGE50 = os.environ.get("TPDB_AGE50", "MP")
AGE50_HEAD = float(os.environ.get("TPDB_AGE50_HEAD", "0.86"))
if "M" in AGE50:
    # (first look: with her hair up in a bun and her whole face bare the woman in purple looked younger, a child with a topknot; her hair stays)
    PEOPLE["person.ana"].update(scale=1.03)
    PEOPLE["person.ana"]["build"] = dict(PEOPLE["person.ana"].get("build", {}), bust=float(os.environ.get("TPDB_BUST50", "1.0")))
    PEOPLE["person.mei"]["build"] = dict(PEOPLE["person.mei"].get("build", {}), bust=float(os.environ.get("TPDB_BUST50", "1.0")))
    PEOPLE["person.mei"].update(hem_drop=0.10)
    PEOPLE["person.dev"].update(beard50=True)
# v0.51 bench (TPDB_MOUST51; vision/flaws_v050.md O2): on the smaller head the moustache is a smaller mark. v0.50's readers named it in 7 of
# the 23 pictures of the man in the red shirt, for 13 of 22 in v0.49, and he is the one grown figure still called a boy (2 of 23). "B": as wide
# and as thick as it was on v0.49's head. "O": v0.50's, scaled with the head
# v0.51: O. Sixteen of v0.50's pictures of him, built again with B and read in whole scenes beside v0.50's own (vision/isolation_v051.md): the
# moustache is in his inventory line in 9 of 16 with B and 7 of 16 with O, and he is a boy first in 2 of 16 with each. The width is not it.
# Three of the four boys are the sweeper, bent over his broom with his face down: the pose, for the next list
MOUST51 = os.environ.get("TPDB_MOUST51", "O")
# v0.53 bench (TPDB_ANA53; vision/flaws_v052.md O1): the woman in purple was a girl first in 4 of her 25 v0.52 pictures and in 4 of v0.51's, in
# three poses. Her hair hangs loose down her back in one narrow fall, which from the side is a ponytail. "N": drawn back into a low bun at the
# nape (the woman in yellow's of v0.42). "S": cut to the shoulders and full at the sides. "O": v0.52's
ANA53 = os.environ.get("TPDB_ANA53", "O")
if "N" in ANA53:
    PEOPLE["person.ana"].update(hair="low_bun")
if "S" in ANA53:
    PEOPLE["person.ana"].update(hair="shoulder")
if "F" in ANA53:
    # a woman's figure: a narrower waist, wider hips and a fuller bust than v0.50 gave her
    PEOPLE["person.ana"]["build"] = dict(PEOPLE["person.ana"].get("build", {}), **__import__("json").loads(os.environ.get("TPDB_ANA53_F", '{"waist": 0.84, "hips": 1.16, "bust": 1.5}')))
if "K" in ANA53:
    # a skirt to the knee in the trousers' colour
    PEOPLE["person.ana"].update(bottom="skirt")
if "L" in ANA53:
    # a skirt to below the knee, as the woman in yellow's dress is
    PEOPLE["person.ana"].update(bottom="skirt", hem_drop=float(os.environ.get("TPDB_ANA53_HEM", "0.15")))
if "C" in ANA53:
    # a cardigan in her purple over a cream top, for the tee
    PEOPLE["person.ana"].update(top="cardigan", inner="cream")
if "P" in AGE50:
    for _fam, _sp in PEOPLE.items():
        if _sp["age"] in ("adult", "older_adult"):
            _sp["head_scale"] = _sp.get("head_scale", 1.0) * AGE50_HEAD
            if MOUST51 == "B":
                _sp["moust51"] = 1.0 / AGE50_HEAD

QUADRUPEDS = {
    "animal.dog_01": dict(kind="dog", scale=1.0, body="tan", belly="cream", accent="brown", collar="red", tail="dog",
                          labels=dict(everyday_name="dog", accepted_names=["dog", "puppy", "pup"], category="medium_animal")),
    "animal.dog_02": dict(kind="dog", scale=0.80, body="white", belly="white", accent="brown", ears="flop",
                          tail="curl", collar="blue", head_r=0.122, spot_col="brown",
                          spots=[(0.10, 0.50, 0.050, 0.040, 1), (-0.05, 0.47, 0.040, 0.035, 1), (0.16, 0.46, 0.035, 0.030, -1), (-0.02, 0.52, 0.050, 0.038, -1)],
                          labels=dict(everyday_name="dog", accepted_names=["dog", "puppy", "pup"], category="small_animal")),
    "animal.cat_01": dict(kind="cat", scale=0.86, body="charcoal", belly="white", accent="charcoal", inner_ear="pink", tail="cat",
                          labels=dict(everyday_name="cat", accepted_names=["cat", "kitten", "kitty"], category="small_animal")),
    "animal.cat_02": dict(kind="cat", scale=0.84, body="orange", belly="cream", accent="orange", paws="cream", inner_ear="pink", tail="cat",
                          labels=dict(everyday_name="cat", accepted_names=["cat", "kitten", "kitty"], category="small_animal")),
    "animal.goat_01": dict(kind="goat", scale=1.0, legs=1.12, girth=1.04, body="white", belly="cream", accent="white", paws="charcoal",
                           ears="goat", horns=True, horn_col="slate", horn_size=1.45, beard=True, beard_col="cream", tail="goat", head_r=0.108, snout=1.15,
                           labels=dict(everyday_name="goat", accepted_names=["goat", "kid"], category="medium_animal")),
}

# v0.39 bench (TPDB_ART39 "B"): the second dog shorter in the leg with longer ears (a beagle's shape, so the two dogs differ by shape and not only
# colour); the black cat a dark grey, so its line art shows (a solid silhouette: "cat/kitten or small black dog"); the goat brown with a white face
# and white legs (all white, it was "a lamb or a dog" and vanished on its fill)
if os.environ.get("TPDB_ART39", "B") == "B":
    QUADRUPEDS["animal.dog_02"].update(legs=0.90, ear_len=1.28)
    QUADRUPEDS["animal.cat_01"].update(body="slate", accent="slate")
    # v0.39 bench (vision/isolation_v039.md, round 3): D, v0.38's white on the redrawn goat. B (brown, white face and legs) was "a sack or saddle
    # blanket draped over a white animal" to three readers of three and "The strangest thing" in a whole scene; C (brown legs) and E (brown
    # all over) moved the name toward "antelope or deer"; D was "a goat" to three of three
    G39 = os.environ.get("TPDB_GOAT39", "D")
    if G39 != "D":
        QUADRUPEDS["animal.goat_01"].update(body="brown", accent="white", head_col="white", belly="white", leg_col="white", beard_col="white")
    if G39 == "E":
        # (bench round 3: brown all over, the muzzle and beard white, so no colour edge cuts the animal at the legs or the neck)
        QUADRUPEDS["animal.goat_01"].update(head_col="brown", leg_col="brown", accent="brown")
    if G39 == "C":
        # (bench round 2: the legs brown as the body, the face white; white legs under a brown body read as "a sack or saddle blanket draped
        # over a white animal", three readers of three)
        QUADRUPEDS["animal.goat_01"].update(leg_col="brown")

# v0.42 bench (TPDB_GOAT42, castlib/animals.py): the redrawn goat on shorter legs (with the back a fifth longer, its legs were "long"), a pointed beard
# from the chin; "C" a red collar for the tether the scene draws
GOAT42 = os.environ.get("TPDB_GOAT42", "C")  # v0.42 bench (vision/isolation_v042.md): C
if GOAT42 in ("B", "C"):
    QUADRUPEDS["animal.goat_01"].update(legs=1.0, beard_size=1.3)
if GOAT42 == "C":
    QUADRUPEDS["animal.goat_01"].update(collar="red")
# v0.43 bench (TPDB_GOAT43, castlib/animals.py): the beard larger and grey, so it shows on the white face (twice unseen in v0.42: "a ram or horned sheep")
if os.environ.get("TPDB_GOAT43", "C") in ("B", "C") and GOAT42 in ("B", "C"):
    QUADRUPEDS["animal.goat_01"].update(beard_size=1.9, beard_col="gray")

BIRDS = {
    "animal.bird_01": dict(kind="songbird", scale=1.6, body="red", belly="cream", wing_col="roof", accent="yellow", leg_col="orange",
                           labels=dict(everyday_name="bird", accepted_names=["bird", "robin", "little bird"], category="bird")),
    "animal.bird_02": dict(kind="songbird", scale=1.6, body="blue", belly="cream", wing_col="navy", accent="yellow", leg_col="orange",
                           labels=dict(everyday_name="bird", accepted_names=["bird", "bluebird", "little bird"], category="bird")),
    "animal.duck_01": dict(kind="duck", scale=1.25, body="white", wing_col="cream", accent="orange", leg_col="orange", tail_col="white",
                           labels=dict(everyday_name="duck", accepted_names=["duck", "duckling", "bird"], category="water_bird")),
}

QUAD_AFFORDANCES = {
    "dog": ["stand_on", "be_pinched_under", "look_at", "sleep", "bark", "beg", "play", "walk_on_leash"],
    "cat": ["stand_on", "look_at", "sleep", "stalk", "knock_over"],
    "goat": ["stand_on", "look_at", "eat_grass", "chew"],
}
