# v0.42 isolation bench

Each visual was forced into a picture with little else and cut out, then read blind by fresh readers (the method of `isolation_v023.md`). There were two rounds:
- round 1: twenty-five readers of 50 cut-outs, two to a reader and never two takes of one thing (`isolation_v042/round1`);
- round 2: nine readers of 9 cut-outs, one each (`isolation_v042/round2`).

`map.json` in each says which cut-out is which case.

What was drawn is two lists: `flaws_v041.md`'s and Sam's notes on the figures (`figure-fixes-v041.md`, kept in `tpdb_work/`), which ranked nine things by what they cost a reader. Eight changes are in the cast, behind switches read when it is built:
- `TPDB_GOAT42` (the notes' item 1, O4): the goat. **B** has a long wedge head, a smaller cranium with a face chain running down to the muzzle; the sphere's side ear had read as an eye socket in profile. It has leaf ears out and back from the poll, and a neck chain from the withers into the back of the head (at 135 the head had floated). The back is a fifth longer and level, on shorter legs. The hooves are split, in dark grey, and the beard is pointed. **C** is B with a collar.
- `TPDB_DOG42` (item 4): the dogs. **B** makes the tan dog's chest patch a narrow blaze that ends above the belly (in v0.41's picture 1, "like a bib or nappy") and drops it on the spotted coat, where it was white on white. The far legs are a step darker, and the spotted dog has a brown patch on its near foreleg. The muzzle is longer with a level top, and the skull a little flatter.
- `TPDB_BEG42` (item 5, O2): **B** puts the begging dog on its haunches, the rump on the ground, the hocks flat and the hind paws forward under the body, the trunk upright, shorter and rounder. The reading dog's hind legs fold beside the rump; they had been stretched out in front.
- `TPDB_MID42` (item 3): the trousers' seat and hip, which left a V across the front, "briefs". **B** sets the seat and hip nodes back; **C** sets the seat back and drops the hip node.
- `TPDB_BELT42` (item 2): **B**, no belt under an untucked tee.
- `TPDB_FOOT42` (item 6): **B**, a longer and flatter toe, which shows below the cuff from the front, and a sole; a bare leg's calf fuller and set back.
- `TPDB_CAT42` (item 7, O5): the cat's head a tenth smaller and its legs' radii blended; the stalk's stride spread with the near legs outside the far ones (**B**) or the far ones outside (**C**).
- `TPDB_MEI42` (item 8, O3): **B**, the woman in yellow with her hair drawn back into a low bun at the nape, as tall as the men with a smaller head. The runbook's lesson is to try the head before the clothes.

Four changes are in placement revision 40:
- `templates.GOAT42` **T**: the grazing goat tethered, a rope from its collar to a peg in front of it (out of place in seven v0.41 pictures);
- `templates.BIRD42` **B**: the songbirds and the duck at 45 as well as 90, where they need no direction (item 9);
- `templates.KINK42` **K**: the stopped hose crimped where the paw stands on it (R1);
- `templates.BEG40` **B**: no one else with an ice cream near the begging dog (O1), a placement rule left to the design tests.

Each thing was read in v0.41's cast and scene, **O** (`BENCH_CAST=assets/cast/out041`, its library copied), against **N**, the cast with every switch on (GOAT42 C, DOG42 B, BEG42 B, CAT42 C, MID42 C, BELT42 B, FOOT42 B, MEI42 B) and the goat tethered. The crimp (K) and the birds at 45 (B) were read on v0.41's cast. The first three letters of a case name the thing.

Not drawn:
- **The knees** (item 6's third part). A standing leg is already set to 0.985 of its length, which bends the knee about 20 degrees. The bend points at the camera in a front view, where no bend shows. A few degrees more would not show either.
- **The belt as the trousers' own top band** (item 2's option B). Option A, no belt, went to the bench.

Before the readers, the bench's own look caught these:
- **The goat's first collar was a red scarf.** It was a band as tall as the neck. It was made a strap, and the beard, which hung at the end of the muzzle and made the face a beak, was moved under the jaw (`tpdb_work/bench42/look_g1.png`, `look_g2.png`).
- **The nostrils stood in front of the muzzle.** The skin chain ends short of its last radius, and they were moved in twice (`look_gh1.png`, `look_gh2.png`).
- **The leaning beg was not a dog.** Tipped back, the trunk stretched into a tall tube. Built on the dog's sit, it stood on its hind legs. The upright trunk, shortened and rounded, sat on its haunches (`look_d1.png`, `look_d2.png`, `look_e1.png`).
- **MID42 B left the V.** Only C, with no hip node, took it away, at 0 and 45, and the seat still sat (`look_mO.png`, `look_mB.png`, `look_mC.png`).
- **A cream sole read as a white disc** under each shoe. It became grey under a dark shoe and charcoal under the rest.
- **The crimp's fold was a speck.** At five pixels it read as nothing, so it was enlarged before the readers saw it (`s_kink1.png`).
- **Two people cases did not place.** The photographer, forced, never came out as Dev, Ben or Ana in 40 seeds, so those two cases became a washing hanger and a sweeper.

## Round 1

| Case | Drawn | What the readers said |
|---|---|---|
| `gt2O_1` to `_3` | the grazing goat, v0.41, at 90, 45 and 135 | A goat grazing in all three. The head at 90: "a flat, round white disc with an oval and a dark dot inside it ... There is almost no visible neck" (`_1`); the body: "an odd lumpy outline" (`_2`), "strongly arched, with the rump highest" (`_3`) |
| `gt2N_1` to `_3` | redrawn and tethered (C, T) | A goat grazing in all three, tethered in all three ("so the goat is tethered", `_1`, `_2`). No remark on the head as a disc. Once "it could be read as a ram or sheep. It has no wool and no visible beard" (`_1`). The body still: "the rump/back is high and blocky" (`_2`), "The back is high and hunched" (`_3`) |
| `bg2O_1` to `_3` | the begging dog, v0.41, at 90 (twice) and 45 | Begging in all three, and kneeling or human in all three: "more like a person kneeling than a dog sitting" (`_1`), "a figure kneeling upright almost like a person" (`_2`), "very upright and stretched, almost human-like" (`_3`) |
| `bg2N_1` to `_3` | on its haunches, the trunk shorter (B) | Begging in all three, and no reader saw kneeling or a person. "The dog's body looks short and compressed" (`_2`), and its head "tipped back so its nose points almost straight up", read once as howling (`_2`); "sitting up to beg or half-standing on its hind legs" (`_3`) |
| `rd2O_1`, `_2` | the reading dog, v0.41 | Reading or holding the paper in both. "The dog's pose is very human-like" (`_1`); "a human-like, leaning-back pose" with "a stretched-out hind leg reaching forward under the paper" (`_2`) |
| `rd2N_1`, `_2` | the hind legs folded beside the rump (B) | Reading or holding the paper in both. Still human: "upright like a person or kangaroo" (`_1`), "almost like a person kneeling" (`_2`) |
| `dg2O_1`, `_2` and `dg2N_1`, `_2` | the dogs at 45 on the stopped hose | The whole template was cut out, and the dog was small in it. Nothing was said of its chest, legs or head on either side |
| `hk2O_1` to `_3` | the stopped hose, v0.41 | Blocked by the dog at 90: "It reads as the dog standing on the hose and blocking the water" (`_1`) |
| `hk2K_1` to `_3` | crimped at the paw (K) | A kink, once with a doubt: "a short curved piece of hose sticks up like a hook. It could be a kink in the hose or a separate stray bit. It looks a little detached" (`_1`); "the hose has a small curl or kink" (`_2`). At 135 the dog hides it |
| `wv2O_1` to `_3` | Dev hanging washing, Ben raking, Ana sweeping, v0.41 | Each named and doing it. Once the belt: "There is a dark band at her waist. It could be a belt, or it could be the gap between her shirt and trousers" (`_3`) |
| `wv2N_1` to `_3` | no hip node, no belt under a tee, the new shoes (MID42 C, BELT42 B, FOOT42 B) | Each named and doing it. Nothing said of the waist, the trousers or the shoes |
| `me2O_1` to `_3` | the woman in yellow in whole pictures with other adults, v0.41 | "A woman" in all three, once "a young woman" (`_2`) |
| `me2N_1` to `_3` | the low bun, taller (B) | "A woman" in all three; her hair "a dark ponytail" (`_1`). Once her shoes, "two flat red ovals ... a little like slippers or discs" (`_1`), which v0.41's shoes look the same as at that size |
| `sc2O_1` to `_3` | the stalking cat, v0.41, at 45 (twice) and 90 | Stalking in all three, and the legs bunched or tangled in all three; once "a skinny dog or a fox-like animal" (`_1`) |
| `sc2N_1` to `_3` | the far legs outside, the head smaller (C) | Stalking in all three, and the legs tangled in all three; "it could be read as a rat or weasel" (`_1`), and "it could also be a fox or a small dog. It has no clear ears" (`_3`) |
| `bd2O_1` to `_3` | the perched bird, the fed birds, the duck at 90 | Each read |
| `bd2B_1` to `_3` | the same at 45 (B) | Each read: the perched bird, a bird pecking at the seed, and "It reads clearly as a swimming duck" (`_3`) |

**Round 1.**
- **The goat: N, with its graze to round 2.** It was tethered in all three cut-outs, and the disc head was gone. The hunch at 45 and 135 stayed: grazing, the head goes down and the rump is what is left high.
- **The begging dog: B.** Kneeling or a person went from three of v0.41's three to none.
- **The reading dog: to round 2.** The folded hind legs alone did not take the person away.
- **The dogs: to round 2,** cut out close.
- **The crimp: O.** v0.41's hose already read as blocked under the paw, and the fold drew a doubt of its own.
- **The waist and the shoes: MID42 C, BELT42 B, FOOT42 B.** Nothing was said of them in N; v0.41's belt was once "a belt, or ... the gap".
- **The woman in yellow: B.** She was a woman in all six whole pictures on both sides, as on v0.41's bench. The screen's "girl" will tell.
- **The cat: O.** Its legs were tangled on both sides, and the smaller head drew two other animals.
- **The birds at 45: B.**

## Round 2

The N cast built whole again (`BENCH_CAST=tpdb_work/bench42/out_N2`), with two changes. The goat's graze has the hind legs bent and the chest up, so the back slopes down to the rump, and its nostrils are on the muzzle. The reading dog's trunk is the begging dog's, shorter and rounder. The goat and the reading dog were read on round 1's seeds. The dogs at 45 were cut out close, on v0.41's cast and N's. Each cut-out went to its own reader.

| Case | Drawn | What the readers said |
|---|---|---|
| `gt3N_1` to `_3` | the goat's graze sloped to the rump | Tethered in all three. The body still, and at 90 worse: "It can read as a goat leaning down to graze, or as one kneeling or bowing on its front legs" (`_1`); "The goat's pose looks hunched and awkward" (`_3`). Once again "no beard is visible, so it could also be read as a ram or horned sheep" (`_2`) |
| `rd3N_1`, `_2` | the reading dog's trunk shorter | Reading in both. "The pose is human-like and a little awkward" (`_1`); "It could be sitting up and begging, or half crouching or jumping" (`_2`) |
| `dg3O_1`, `_2` | the dogs at 45, v0.41, cut out close | Dogs, once "looks like a beagle" (`_1`). "The dog's legs are long and stiff, almost post-like" (`_1`); the spotted dog's body "properly joined and in proportion" (`_2`) |
| `dg3N_1`, `_2` | the same, B | Dogs. "The legs look long and somewhat stiff and tube-like" (`_1`); the spotted dog's "rear legs look slightly pasted onto the body rather than clearly joined at the hips" (`_2`). Neither side drew a bib or stilts |

**Round 2.**
- **The goat's graze: back to round 1's level back.** The slope bought nothing at 135 and drew kneeling at 90. Sam's note asks for the level top line, and round 1's back is level.
- **The reading dog: B with the shorter trunk.** The person went from two of v0.41's two to one of two.
- **The dogs: B.** The bench found nothing to choose between them. The bib was said of a dog at three-quarters in a whole picture, which a close cut-out at 45 does not reproduce. B is the notes' drawing and drew no misreading, and the screen will read it.

## Chosen

- **The cast, builder 0.42.0:** `TPDB_GOAT42` C, `TPDB_DOG42` B, `TPDB_BEG42` B (the reading dog's trunk with it), `TPDB_MID42` C, `TPDB_BELT42` B, `TPDB_FOOT42` B, `TPDB_MEI42` B; `TPDB_CAT42` O.
  - Every person is redrawn, through the shoes, and so are both dogs and the goat. Only the cats', the songbirds' and the duck's renders carry over to `lib042` and `gallery042`.
- **Placement revision 40:** `GOAT42` T, `BIRD42` B, `BEG40` B; `KINK42` O.
- **After the bench, the validator.** It failed the two begging dogs at 90: the underside of the rump was 37 px below the ground point, where 33 is allowed (the hip dropped 0.42, v0.41's 0.40). Raising the flat hock changed nothing, and a drop of 0.38 passes (`tpdb_work/patch42x.py`, `patch42y.py`). The rump stands 4 cm higher than the bench's.
- **On the list:** the cat's legs at 45; the goat's body when it grazes, and its beard, which twice did not show.
