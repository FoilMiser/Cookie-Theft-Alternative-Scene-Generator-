# v0.43 blind screen: what it found (the work list for v0.44)

The v0.43 screen read the set's 21 pictures and 73 probes with the prompts of v0.39 (`screen_prompts.md`). There were twelve readers of seven or eight pictures and four scorers of 23 or 24. The oddity tally is by angle, as in v0.39. Keys, descriptions and scores are in `v043/`.

v0.43 worked two lists, `flaws_v042.md` and Sam's notes on the figures (`tpdb_work/figure-fixes-v042.md`). The bench (`isolation_v043.md`) took these into the cast (builder 0.43.0):
- **the reading dog lying down** like a sphinx, its head bowed over a paper laid open on the ground under its forepaws;
- **the two women:** the head smaller and the neck longer, a narrower face with smaller eyes set lower and red lips; the woman in yellow's bob back, and her shoes a darker red;
- **the dogs:** the legs a tenth shorter and tapered, the hind leg's thigh part of the body, a brown patch over the spotted dog's hip, the far legs darker;
- **the goat:** one smooth tapered curve for each horn, a larger grey beard, and the neck forward when it stands.

Placement revision 41 adds six rules:
- the reading dog is kept away from the trip and from anyone reading as they walk;
- its paper lies flat on the ground;
- a dog, never a goat, stands on the stopped hose;
- the stalking cat is drawn in profile only, with a gap before its bird;
- the begging dog's mouth is closed;
- the goat's rope is slack and always drawn.

Every dog, goat and woman is drawn anew, so no picture is identical to v0.42's, and there is no retest this time.

## Headline (the 21 pictures of the set)

| | v0.39 (21) | v0.40 (21) | v0.41 (21) | v0.42 (21) | v0.43 (21) |
|---|---|---|---|---|---|
| Things | 1.00 | 0.991 | 1.00 | 0.991 | 0.952 |
| Actions | 1.00 | 0.996 | 1.00 | 1.00 | 0.996 |
| Inferences | 1.00 | 0.986 | 0.958 | 0.939 | 1.00 |
| Contradictions | 1.00 | 1.00 | 1.00 | 0.942 | 0.712 |
| All items | 1.00 | 0.993 | 0.995 | 0.984 | 0.955 |
| Misread items | 0 of 287 | 0 of 287 | 0 of 287 | 0 of 290 | 1 of 290 |
| Readers' remarks per picture (all screened pictures) | 3.10 | 3.04 | 3.17 | 3.05 | 3.12 |
| Oddities per picture, as logged by the scorers | 0.8 (at most 3) | 0.5 (at most 3) | 0.4 (at most 3) | 0.7 (at most 3) | 1.1 (at most 3) |

The reading dog is in five of the set's pictures, and its contradictions are most of what the set lost: contradictions 0.712, and all items 0.955.

Across all 94 pictures, 977 of the 1003 scored items had full marks, and one was misread. The 26 under full marks:
- **Ten on the reading dog, in all five of its pictures**, every one in the set. In four the dog was "lying on an open newspaper". "Reading" came only beside lying on it, pawing at it or tearing it:
  - "The puppy on the newspaper could be lying/resting on it or tearing/reading it; it just looks like it is lying on it" (25);
  - "The brown dog on the newspaper could be lying on it, tearing it, or "reading" it" (31);
  - "as if reading it", with "simply lying on it" as the equal reading (59);
  - "reading it or about to tear it" (9).
  - The misread (85): "lying on an open newspaper and pawing at it, apparently tearing it up".
  - Its contradiction notice was 0 in three pictures and 0.5 in two.
- **Twelve setting items, not mentioned.** Ten are clouds, from two readers who wrote "sunny" in each of their back gardens and parks (57 to 64, 81 to 86). Two are a tree (71, 72).
- **Two on the dog by the door (55).** The lead in its mouth read as "attached" to its red collar and "lying loose in a loop on the ground", and "it may simply have been left with its lead on".
- **The camera (31):** "binoculars (or a camera)".
- **The square wheel (57):** "a square, grid-like thing where its round wheel should be", called wrong, with a drain grate as the equal reading.

The scorers gave two, five, twelve and seven items under full marks, of 231, 284, 262 and 226.

**What the full marks rest on.** The scorers' notes mark 7 items they credited in full where the free description commits and the unsure section adds another reading (10 in v0.42). Halved, they take no template under the gate (`tpdb_work/strict43.py`): the same two fall as on the plain count. `photo` and `plant_flowers`, v0.42's two under the strict count, read 0.90 and 1.00 on five pictures each.

## The v0.42 list and Sam's notes

| v0.42 reading, or the notes' item | v0.43 result |
|---|---|
| R1, item 1: `about_to_trip` 0.889, the reading dog beside the walker | **1.00 in five pictures** (15 items). Revision 41 kept the reading dog away from the walker and the box in both pictures that have both |
| R2, item 2: the reading dog's paper "stands upright on its own" | **Redrawn lying down (`TPDB_READ43` A), and under the gate: 0.533** (15 items, 5 pictures), and the screen's one misread. The paper never stood by itself and the dog was never a person. On the bench and in the design tests, larger, it read as reading ("as if it is reading the paper. That is odd, because dogs can't read"). Small in a whole picture, it was a dog lying on a newspaper |
| R3, item 7: `plant_flowers`, `photo` under the strict count | **Probed five times each.** `plant_flowers` 1.00 and `photo` 0.90 (once "binoculars (or a camera)"), both passing read strictly |
| O1, item 3: the woman in yellow "girl" in 6 of her 14 pictures | **Redrawn (`TPDB_ADULT43` B): "a woman" in 15 of her 16 pictures**, once "a woman or girl with dark hair, a yellow dress and red shoes is sweeping" (19) |
| O2, item 3: the woman in purple "girl" in about ten of her 23 | **"A woman" in 16 of her 18**, twice hedged: "woman (or older girl)" (14), "A woman or older girl with long dark hair" (22) |
| O3: the stopped hose's swelling as a puddle or a glitch | Not changed. It was named in all six hose pictures, five times as water backed up behind the dog and once "a squashed section or a puddle" (18) |
| O4, item 8: the stalking cat's legs at 45 | **In profile only (`CAT43` B)**: at 135 the bench found them "jumbled together under the body", as at 45. Stalking in all three pictures, hedged "alternatively the cat is just walking along the fence" (29). In profile its face was "right up against" the bird in a design test, and revision 41 keeps a gap |
| O5, item 4: the goat unusual twice, its tether hard to follow | **The rope slack and never left out (`TETHER43` R)**: tethered in all six pictures. The horns are one curve each, the beard larger and grey, and no goat stands on the hose. Unusual in four (two in gardens), and twice, from behind, possibly a sheep: "a quick glance might take it for a sheep" (40), "could be read as a goat or a sheep" (78). Its graze was benched and kept: the bench's lower hips and bent knees read "cramped" |
| Items 5 and 6: the dogs' legs "stiff and tube-like", the begging head "almost straight up" | **The legs redrawn (`TPDB_DOG43` B)**, and no stiff, stilt or tube in 29 pictures with a dog. The begging head lowered placed on none of 12 seeds at 45 (the gaze check) and was left; the mouth is closed. Begging in all four pictures, no howling |
| O6: the seesaw plank through the thighs | Not changed; once more "the seesaw plank looks as if it passes behind or through the man's legs" (94, scorer d) |
| Item 9: the shoes as flat ovals | The woman in yellow's shoes a darker red, after the bench's "flat and splayed, almost flipper-like". No reader mentioned a shoe |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.39 | v0.40 | v0.41 | v0.42 | v0.43 |
|---|---|---|---|---|---|
| Pass | 64 | 64 | 64 | 63 | 62 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 0 | 0 | 0 | 1 | 2 |

Every template was screened in at least three pictures. By count: 42 in three, 8 in four, 6 in five, 5 in six, 1 in seven, 1 in nine and 1 in nineteen, with 458 scored items behind the verdicts.

**The two failures.**
- **`dog_reading`** is at 0.533 (15 items, 5 pictures), with a misread. It is the drawing v0.43 chose, read above.
- **`dog_wants_walk`** is at 0.833 (6 items, 3 pictures), on the two half marks in picture 55. It was not redrawn, and read 0.917 in v0.42 on a half mark of the same kind. Its red lead runs from the mouth straight past the dog's red collar.

The lowest that pass:
- `photo` (0.90, 5 items, 5 pictures);
- `square_wheel` (0.944, 9 items, 3 pictures).
Every other template reads 1.00.

**Per angle** (`v043/gate_yaw.json`), all 23 (template, angle) pairs pass at 1.00: v0.42's 25 less the stalking cat's two, now drawn only in profile.

## What reads least well (the v0.44 list)

| # | Template | v0.43 | What the readers saw | Fix for v0.44 |
|---|---|---|---|---|
| R1 | `dog_reading` | 0.533 (15 items, 5 pictures), one misread | Lying over a paper on the ground, the dog was "lying on an open newspaper" in four pictures and tearing it once. Reading was offered beside lying, pawing or tearing, never alone | Go back to the dog sitting up with the paper held in its forepaws (v0.42's 0.917), and give the paper's foot to the paws as well: the top gripped, the foot not on the ground. The flat paper reads as something lain on. Bench the two beside each other in whole pictures, not cut-outs, since the bench's cut-outs read the lying dog as reading |
| R2 | `dog_wants_walk` | 0.833 (6 items, 3 pictures) | The red lead in the mouth read as "attached" to the red collar (55) | A lead in a colour of its own, not the collar's, and the loop held up off the ground at the mouth; read in whole pictures |
| R3 | `photo` | 0.90 (5 pictures) | "binoculars (or a camera)" (31) | Watch: a flash or strap on the camera, as the notes suggest, if it falls again |

## Unintended oddities

Named kinds, from the scorers' lists (`v043/scores_summary_a.md` to `_d.md`) and the readers' unsure sections, most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.44 |
|---|---|---|---|---|
| O1 | C | The goat unusual in four of six pictures ("a little unusual", "a bit unusual"), two in gardens. Twice, from behind at three-quarters, possibly a sheep | 25, 40, 78, 85 | The garden goat: a shed or a hutch at the garden's edge, or the park only. The sheep reading from behind: the beard and horns hidden there |
| O2 | C | Figures overlapping the pond's outline, read as standing in front of it (six pictures), and the seesaw plank through the man's legs | Park pictures; 94 | Notes for the pilot, as before |
| O3 | C | The stopped hose's swelling once "a squashed section or a puddle" | 18 | Watch |
| O4 | C | The ten clouds not named by two readers | 57 to 64, 81 to 86 | Notes: one reader can empty a row (RUNBOOK) |

## Placement

**The set.**
- **Tiers 1 to 3.** Every cell placed under revision 41 on its base seed but one: the tier-3 playground. The showcase pass and its search failed it on 13 base seeds, most of the failures naming the stalking cat. A wider search found it with two fresh seed lists side by side, and each list placed on its first seed (`tpdb_work/t3pg43.sh`); the second's is kept. In profile, with the gap, the stalking cat placed as often as before in the playground sets tried (`tpdb_work/place43.py`).
- **Tier 4.** The park and the playground placed on v0.42's seeds and layouts, and the street on v0.29 to v0.42's forced set, also on v0.42's seed and layout. The garden placed on the fourth seed of its search.
- **The isomorphs** are new. The tier-4 one is a garden drawn from the tier-4 playground.

**The probes.**
- **The first pass** (`probes.py 3`, with five for `about_to_trip`, `plant_flowers` and `photo`) ended `SHORT {'fishing': 0, 'dog_begs': 1, 'windy_hat': 2}`. These are the counts of pictures each had, not shortfalls.
- **The pass stratified by angle** added 13 probes, the begging dog at 45 among them (none before).
- **Three park probes were forced** for fishing, which places alone but never in the first pass's crowded groups; the first of them also carries the windy hat.

All 94 records rebuild identical to the pixel, and the library passes the validator in full.
