# TPDB v0.43: the reading dog lying down, the two women grown up, the dogs' legs, the goat's horns, beard and rope, read a fortieth time

v0.42 ended with 63 of 64 templates through the gate: `about_to_trip` fell on one reader who saw the box beside a boy reading as he walked, with the reading dog and its paper just behind him. Next on the list came the reading dog itself, whose paper "stands upright on its own", and the two women still called "girl". Sam's notes on the figures (`tpdb_work/figure-fixes-v042.md`) ranked nine things:
- keep the reading dog away from the trip;
- lay the dog down with its paper flat on the ground, or let the paper lean on it;
- give the women an adult head and face;
- the goat's hunched graze, its beard, its segmented horns and the garden goat with no tether;
- the dogs' stiff tube legs;
- the begging dog's nose pointing at the sky;
- the camera and the planting;
- the cat's legs at 45;
- the shoes.

v0.43 benched those in two rounds and took most of them (builder 0.43.0):
- **The reading dog:** lying down like a sphinx, the head bowed over a paper laid open on the ground under its forepaws.
- **The women:** the head smaller and the neck longer, a narrower, taller face with smaller eyes set lower and red lips. The woman in yellow has her bob back and darker shoes.
- **The dogs:** the legs a tenth shorter and tapered, the hind leg's thigh part of the body, a brown patch over the spotted dog's hip, the far legs darker.
- **The goat:** one smooth tapered curve for each horn, a larger grey beard, and the neck forward when it stands.
- **Placement revision 41:**
  - the reading dog kept away from the trip and from anyone reading as they walk;
  - a dog, never a goat, on the stopped hose;
  - the stalking cat in profile only, with a gap before its bird;
  - the begging dog's mouth closed;
  - the goat's rope slack and always drawn.
- **Read and left as they were:**
  - the paper leaning on a sitting dog ("the paper falling");
  - the cat at 135, as tangled as at 45;
  - the goat's graze with lower hips ("cramped").
- **Tried and left before the readers:** the begging dog's head lowered. At 45 the gaze check found it facing the viewer, and it placed on none of 12 seeds.

The set was regenerated and screened a fortieth time. Every dog, goat and woman is drawn anew, so no picture is identical to v0.42's.

The fortieth screen read 94 pictures, the set's 21 and 73 probes, with twelve readers and four scorers: 977 of 1003 scored items had full marks, and one was misread. 62 of 64 templates pass the gate. `dog_reading` falls, and with it the one misread: the dog lying over its paper, which read as reading on the bench and in the design tests, read in whole pictures as a dog "lying on an open newspaper", pawing at it or tearing it. `dog_wants_walk` falls on one reader who took the lead in the dog's mouth for one on its collar. The trip, v0.42's failure, reads 1.00 in five pictures with the reading dog kept away. The woman in yellow was "a woman" in 15 of her 16 pictures and the woman in purple in 16 of her 18, where v0.42 had them "girl" in six of 14 and about ten of 23.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.42 readers, or Sam's notes, saw | v0.43 |
|---|---|
| `about_to_trip` under the gate, the reading dog beside the walker | The reading dog kept away (revision 41): the trip reads 1.00 in five pictures |
| The woman in yellow called "girl" in 6 of her 14 pictures | A grown woman's head and face: "a woman" in 15 of her 16, once "a woman or girl" |
| The woman in purple "girl" or "girl or young woman" in about ten of her 23 | "A woman" in 16 of her 18, twice hedged ("woman (or older girl)") |
| The dogs' legs "stiff and tube-like" (Sam's notes, the bench) | Shorter and tapered: no stiff, stilt or tube in 29 pictures with a dog |
| The goat's horns stacked segments, the beard unseen, a garden goat untethered | Smooth horns, a grey beard, the rope slack and always drawn, no goat on the hose: tethered in all six pictures, though unusual in four and twice, from behind, possibly a sheep |
| The stalking cat's legs tangled at 45 | In profile only: stalking in all three pictures |
| The begging dog "howling", its nose straight up | The mouth closed: begging in all four pictures. The lowered head did not place at 45 |
| `photo` and `plant_flowers` under the strict count | Five probes each: 0.90 and 1.00, both passing read strictly |
| The reading dog's paper "stands upright on its own" | Lying down over a paper on the ground: never a person and no paper standing, but "lying on an open newspaper", once tearing it. **Not fixed: under the gate** |

Left as notes for the pilot: the stopped hose's swelling, figures drawn over the pond or the prop beside them, and the goat in a garden.

## The isolation bench

The two lists were benched in two rounds of single cut-outs (`vision/isolation_v043.md`). Round 1 had sixteen readers of 31 cut-outs, two to a reader and never two takes of one thing. It read each thing in v0.42's cast and scene against the cast with every switch on:
- **The reading dog:** v0.42's "kneeling upright on its hind legs like a person". Lying down, reading in three of three, each with "sniffing" or "pawing" beside it, the paper "an open book". Leaning, the paper "balanced on one corner", "falling".
- **The woman in yellow:** "a woman or older girl" and "A woman or girl" for v0.42's; "a woman" in both of the new.
- **The dogs:** v0.42's legs "long, straight posts" and "stiff like stilts"; none of that in the new.
- **The goat:** the new graze "cramped", so v0.42's was kept. The rope was "a J-shaped hook or walking-stick handle".
- **The cat at 135:** "jumbled together under the body", as at 45.

Round 2, six readers of 12 cut-outs, read four things:
- **The reading dog:** a larger paper slanted flat, "an open newspaper lying flat on the grass", though the raised head looked "past the paper".
- **The goat's rope:** the slack rope, with no stiffness.
- **The begging dog:** the closed mouth, "as if begging, possibly for the ice cream", where v0.42's was "happily stretching or sniffing the air".
- **The woman in yellow:** her darker shoes, unremarked.

Before any reader, the bench's own look caught four things:
- the begging head's pitch barely moved the nose;
- the woman in purple's ponytail vanished from the front;
- the cat at 135 was as tangled as at 45;
- the lowered begging head did not place.

## Design tests

The cast of builder 0.43.0 and revision 41 were read blind in whole test scenes among other events (`vision/design_tests_v043.md`, six pictures and one rebuilt, seven readers). Five placed on their first, second or fourth seed, and one on its fifth:
- **The trip and the reading dog,** in two pictures, were kept apart. The trip read in both, and the dog lying over its paper read as reading in both, the contradiction named: "looking down at it as if it is reading the paper. That is odd, because dogs can't read". Each reader also offered "pawing at" the paper.
- **The begging dog at 45,** its mouth closed, begged "as if begging for her ice cream".
- **The goat** was tethered in both of its pictures. In a back garden it was still "a little unusual, but not impossible".
- **The two women:** no reader called either a girl. The woman in purple, half turned with a camera, was once "a person with long dark hair", her gender "not certain".
- **The stalking cat:** on the ground in profile, its face was "right up against" the bird, "it already has the bird at its mouth". Revision 41 now keeps a gap, and the rebuilt picture read "about to pounce on the bird".

## Placement revision 41

Every record stores the placement revision it was made with. v0.43 pictures use revision 41:
- **The trip's zone:** the reading dog kept out of a zone round the trip's walker and box, and away from anyone reading as they walk (`templates.TRIP43` "B").
- **The reading dog's paper:** laid flat on the ground under the forepaws of a dog lying down (`templates.READ43` "A"; "B", the paper leaning on a sitting dog, read on the bench and not taken).
- **The stopped hose:** a dog on it, never a goat (`templates.HOSE43` "B").
- **The stalking cat:** in profile only, with a gap of 45 units between its front and the bird (`templates.CAT43` "B"; "C", at 135 as well, not taken).
- **The begging dog:** its mouth closed (`templates.BEGX43` "B").
- **The goat's rope:** slack, with room kept for its peg, and the goat never drawn untethered (`templates.TETHER43` "R").

A v0.42 record rebuilds with the v0.42 package. The cast redraws both dogs, the goat and the two women (builder 0.43.0).

Every cell of the set placed under revision 41: tiers 1 to 3 on v0.42's base seeds, but the tier-3 playground, which placed only on a fresh seed list after 13 base seeds failed; the tier-4 park and playground on v0.42's seeds and layouts, the street on v0.29 to v0.42's forced set, and the garden on the fourth seed of its search. The five isomorphs are new. The probe pass gave `about_to_trip`, `plant_flowers` and `photo` five pictures each, the pass stratified by angle filled the begging dog at 45, and three park probes were forced for fishing, the first with the windy hat. Every picture was looked at before the screen. All 94 records rebuild identical to the pixel, and the library passes the validator in full, 404 of 404.

The planner's difficulty priors are the calibration measured on the v0.43 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.42. With the reading dog lying down, 42 fields of the calibration moved by 0.002 or more, most of all `dog_reading`'s contradiction (s from -0.44 to -0.57) and `cat_stalks_bird`'s inference.

## The fortieth blind screen

Twelve fresh readers, who had never seen the key, described every picture of the new set and 73 probe pictures; four separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.42.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) | v0.25 (21 pictures) | v0.26 (21 pictures) | v0.27 (21 pictures) | v0.28 (21 pictures) | v0.29 (21 pictures) | v0.30 (21 pictures) | v0.31 (21 pictures) | v0.32 (21 pictures) | v0.33 (21 pictures) | v0.34 (21 pictures) | v0.35 (21 pictures) | v0.36 (21 pictures) | v0.37 (21 pictures) | v0.38 (21 pictures) | v0.39 (21 pictures) | v0.40 (21 pictures) | v0.41 (21 pictures) | v0.42 (21 pictures) | v0.43 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 0.97 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 0.95 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 | 0.98 | 0.95 | 0.95 | 0.88 | 0.98 | 0.99 | 1.00 | 0.96 | 0.96 | 0.99 | 0.96 | 0.97 | 0.97 | 0.98 | 1.00 | 0.99 | 0.96 | 0.94 | 1.00 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 1.00 | 0.94 | 0.71 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.99 | 0.98 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 0.98 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.98 | 0.95 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 | 0 of 286 | 0 of 289 | 0 of 283 | 0 of 284 | 0 of 285 | 0 of 284 | 1 of 286 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 286 | 0 of 287 | 0 of 287 | 0 of 287 | 0 of 290 | 1 of 290 |
| Oddities per picture, as logged by the scorers | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 | 2.6 | 2.6 | 2.2 | 2.0 | 2.3 | 2.3 | 0.6 | 0.8 | 0.9 | 0.5 | 0.2 | 0.6 | 0.4 | 0.8 | 0.8 | 0.5 | 0.4 | 0.7 | 1.1 |
| Readers' remarks per picture (recounted in v0.26) | 8.8 | 5.4 | 6.4 | 4.8 | 4.7 | 4.8 | 4.9 | 4.4 | 4.3 | 4.4 | 4.4 | 4.4 | 3.9 | 3.9 | 4.4 | 4.0 | 4.0 | 3.9 | 4.2 | 3.9 | 5.6 | 5.9 | 5.3 | 5.8 | 5.1 | 5.2 | 5.2 | 3.5 | 3.3 | 3.2 | 3.1 | 2.9 | 3.1 | 2.8 | 3.4 | 3.1 | 3.0 | 3.2 | 3.0 | 3.1 |

Across all 94 pictures 977 of 1003 scored items had full marks, and one was misread. Of the 26 under full marks:
- ten are the reading dog's, in all five of its pictures, four of them "lying on an open newspaper", the misread "apparently tearing it up";
- ten are clouds, from two readers who wrote "sunny" and named nothing in the sky, and two a tree;
- two are the dog by the door, its lead "attached" to its collar;
- one is the camera, "binoculars (or a camera)", and one the square wheel, with a drain grate as the equal reading.

The set's headline is all items 0.955 (0.984 in v0.42), most of the fall the reading dog's contradictions (0.712), which is in five of the set's pictures.

**What the full marks rest on.** The scorers' notes mark 7 items they credited in full where the free description commits and the unsure section adds another reading (10 in v0.42). Halved, they take no more templates under the gate: `photo` and `plant_flowers`, v0.42's two under the strict count, pass on five pictures each.

**Remarks were 3.12 a picture, 293 on 94 pictures**, from 2.50 to 4.12 a reader.

What this release redrew or ruled, and the two that fell under the gate (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.42 | v0.43 | v0.43 meaning items |
|---|---|---|---|
| `dog_reading` | 0.92 (18 items) | 0.53 (15 items) | 0.30 (10) |
| `about_to_trip` | 0.89 (9 items) | 1.00 (15 items) | 1.00 (5) |
| `dog_begs` | 1.00 (15 items) | 1.00 (12 items) | 1.00 (4) |
| `goat_grazing` | 1.00 (6 items) | 1.00 (6 items) | — |
| `blocked_hose` | 1.00 (24 items) | 1.00 (24 items) | 1.00 (6) |
| `cat_stalks_bird` | 1.00 (18 items) | 1.00 (9 items) | 1.00 (3) |
| `plant_flowers` | 1.00 (3 items) | 1.00 (5 items) | — |
| `photo` | 1.00 (3 items) | 0.90 (5 items) | — |
| `dog_wants_walk` | 0.92 (6 items) | 0.83 (6 items) | 0.83 (3) |

`dog_reading`, lying down, is at 0.533, its paper never standing by itself and the dog never a person, but read as lying on the paper. `about_to_trip` reads 1.00 in five pictures, the reading dog away from it. `dog_begs`, its mouth closed, reads 1.00 in four pictures, at 90 and 45. `goat_grazing` reads 1.00 in six pictures, tethered in all six, unusual in four and twice, from behind, possibly a sheep. `cat_stalks_bird`, in profile only, reads 1.00. `plant_flowers` and `photo`, probed five times each, read 1.00 and 0.90. `dog_wants_walk`, not redrawn, falls at 0.833. No reader called the dogs' legs stiff or the cat's tangled, or mentioned a shoe.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 | v0.27 | v0.28 | v0.29 | v0.30 | v0.31 | v0.32 | v0.33 | v0.34 | v0.35 | v0.36 | v0.37 | v0.38 | v0.39 | v0.40 | v0.41 | v0.42 | v0.43 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 | 61 | 59 | 63 | 61 | 64 | 63 | 63 | 63 | 63 | 64 | 63 | 64 | 63 | 64 | 64 | 64 | 64 | 63 | 62 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 | 3 | 5 | 1 | 3 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 2 |

Every template was screened in at least three pictures (42 in three, 8 in four, 6 in five, 5 in six, 1 in seven, 1 in nine and 1 in nineteen), and 62 of 64 pass. `dog_reading` falls at 0.533 with the misread, in five pictures; `dog_wants_walk` at 0.833, on two half marks in one of its three pictures, as in v0.42 (0.917) on a half mark of the same kind. The lowest that pass are `photo` (0.90) and `square_wheel` (0.944). Per angle (`vision/v043/gate_yaw.json`), all 23 (template, angle) pairs pass at 1.00, v0.42's 25 less the stalking cat's two now that it is drawn only in profile. The gate is a filter, and the pilot with people is the test of difficulty.

Templates that did not pass (`vision/flaws_v043.md` gives what the readers saw and the next fix):

| Template | v0.43 mean | Pictures | Misreads |
|---|---|---|---|
| `dog_reading` | 0.53 (15 items) | 5 | 1 |
| `dog_wants_walk` | 0.83 (6 items) | 3 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.777 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s1021 | 4 | 0 (0) | 3 | 0.782 | — | 13 | 0.022 | kick ball, ice cream, fly kite |
| T1_street_s1031 | 5 | 0 (0) | 3 | 0.778 | — | 16 | 0.045 | birds flying, run, wave |
| T1_playground_s5041 | 5 | 0 (0) | 3 | 0.753 | — | 18 | 0.035 | sandbox, run, dog playing |
| T2_garden_s2012 | 8 | 1 (0) | 4 | 0.711 | 0.388 | 19 | 0.042 | kite in tree, read bench, jump, water flowers |
| T2_garden_s6118_iso (isomorph of T2_playground_s042) | 8 | 1 (0) | 4 | 0.703 | 0.368 | 18 | 0.040 | lost balloon, cat sleeping, play catch, swing |
| T2_park_s2022 | 8 | 1 (0) | 4 | 0.695 | 0.367 | 21 | 0.025 | lost balloon, balloon, ducks swimming, picnic |
| T2_street_s1032 | 8 | 1 (0) | 4 | 0.709 | 0.367 | 16 | 0.049 | lost balloon, push stroller, play catch, carry bag |
| T2_street_s7109_iso (isomorph of T2_park_s2022) | 8 | 1 (0) | 4 | 0.695 | 0.350 | 18 | 0.051 | ball in tree, water flowers, wave, ice cream |
| T2_playground_s042 | 8 | 1 (0) | 4 | 0.704 | 0.383 | 18 | 0.035 | kite in tree, sandbox, play catch, drink bench |
| T3_garden_s3013 | 12 | 3 (1) | 6 | 0.649 | 0.338 | 20 | 0.038 | about to trip, cat stalks bird, dog reading, bird perched, paint fence, dog sleeping |
| T3_garden_s7102_iso (isomorph of T3_street_s12133) | 12 | 3 (1) | 6 | 0.660 | 0.285 | 21 | 0.043 | sprinkler package, cat stalks bird, bucket hat, dig, walk dog, cat sleeping |
| T3_park_s18023 | 12 | 3 (0) | 5 | 0.658 | 0.344 | 21 | 0.027 | rain coming, ice cream drop, ducks bread, feed birds, dog playing |
| T3_park_s7104_iso (isomorph of T3_playground_s32043) | 12 | 2 (0) | 4 | 0.668 | 0.337 | 20 | 0.023 | ice cream drop, lost balloon, carry bag, dog playing |
| T3_street_s12133 | 12 | 3 (1) | 6 | 0.659 | 0.292 | 22 | 0.057 | ball in tree, dog begs, sweep fork, walk dog, sweep, photo |
| T3_playground_s32043 | 12 | 2 (0) | 4 | 0.657 | 0.342 | 20 | 0.037 | ice cream drop, ball in tree, cat sleeping, bird perched |
| T4_garden_s459986 | 18 | 5 (2) | 8 | 0.571 | 0.213 | 27 | 0.047 | blocked hose, ball in tree, bird steals, bucket hat, square wheel, birds flying, dig, carry box |
| T4_garden_s19111_iso (isomorph of T4_playground_s460662) | 18 | 5 (2) | 9 | 0.556 | 0.223 | 31 | 0.047 | bird steals, lost balloon, ball in tree, square wheel, dog reading, birds flying, goat grazing, cat on fence, dog playing |
| T4_park_s728923 | 18 | 5 (2) | 8 | 0.565 | 0.243 | 30 | 0.036 | ice cream drop, ducks bread, kite in tree, dog reading, pan watering, birds flying, goat grazing, sweep |
| T4_street_s430752 | 18 | 5 (2) | 9 | 0.580 | 0.208 | 26 | 0.056 | bird steals, about to trip, ball in tree, dog reading, water upward, birds flying, sweep, jump, carry bag |
| T4_playground_s460662 | 18 | 5 (2) | 9 | 0.557 | 0.217 | 26 | 0.042 | bird steals, kite in tree, lost balloon, square wheel, dog reading, run, photo, dog playing, birds flying |

Isomorph pairs differ by at most 0.011 in content and 0.017 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 25,810 | 27 | 11,275 | 10^12.6 |
| garden | 3 | 2,343,163 | 296 | 310,307 | 10^18.6 |
| garden | 4 | 70,686,492 | 565 | 5,759,476 | 10^23.2 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 45,955 | 24 | 19,978 | 10^11.2 |
| park | 3 | 5,569,417 | 236 | 972,951 | 10^17.4 |
| park | 4 | 307,551,136 | 376 | 41,212,001 | 10^23.0 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,298 | 24 | 2,847 | 10^11.8 |
| street | 3 | 420,725 | 220 | 65,745 | 10^17.3 |
| street | 4 | 6,676,618 | 330 | 876,099 | 10^21.8 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.3 |
| playground | 3 | 738,151 | 183 | 110,468 | 10^17.6 |
| playground | 4 | 10,363,379 | 232 | 1,312,634 | 10^20.8 |

In all 404,451,615 structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.

## Key words, frequency and age of acquisition


Unchanged from v0.20: every item record carries its key word's Zipf frequency (f, for things and actions only) and its
age of acquisition (a, from the bundled excerpt of Kuperman, Stadthagen-Gonzalez and Brysbaert, 2012) at weight 0;
`scenegen/norms/aoa_kuperman2012.tsv` keeps the citation and source in its header and every record stores its sha256.
The licence note and what the pilot should test are in the v0.20 README section of the same name (the CC BY-NC-ND 3.0
question about shipping an excerpt; the model with AoA against the model without, pre-registered; AoA kept varying apart
from frequency when choosing the pilot's pictures). Before the pilot, check the bundled rows against the original file
(`python -m scenegen.difficulty --check-aoa <the original .xlsx or .csv>`).

## Folders

| Folder | What it holds |
|---|---|
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts; from v0.31 a pose name with `~near` or `~far` draws a figure in two pieces at its far leg, and from v0.32 `~body` and `~legs` at both legs, for the bench) |
| `assets/blender_run.py` | Lets the `bpy` scripts run with plain `python`, inside an installed Blender where the `bpy` module is missing |
| `assets/validate_assets.py` | Checks for every rendered variant; from v0.32 a piece of a split figure is checked by its base pose, and the manifest schema takes the `~` suffix |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, v0.41 folds the begging dog's forelegs, v0.42 redraws the goat, the dogs, the trousers' waist, the shoes and the woman in yellow's hair, and v0.43 lays the reading dog down and redraws the dogs' legs, the goat's horns and beard and the two women's heads |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out043/` | The 18 `.blend` families (builder 0.43.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib043/` | Every variant the generated scenes and probes use, carried over from `lib042` or rendered from `out043` (the dogs, the goat and the two women) |
| `assets/cast/gallery043/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (179, all pass the validator) |
| `scenegen/` | The generator (0.43.0, placement revision 41); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.43 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v043.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v043.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v043.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all forty screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out043                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out043 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s18023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v043   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v043 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery043 --old-gallery <v0.42 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.43 --single   # the release as one zip, tpdb_v0.43.zip
```

The release is one zip, `tpdb_v0.43.zip`, about 232 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.42 record rebuilds with the v0.42 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- Two templates fall under the legibility gate after the v0.43 screen. `dog_reading` (0.53, 5 pictures) is the screen's one misread: v0.43 laid the dog down
  over a paper on the ground, and in four of its five pictures it was "lying on an open newspaper", the reading offered only beside lying on it, pawing at it or
  tearing it, once "apparently tearing it up". On the bench and in the design tests, at a larger size, it read as reading. `dog_wants_walk` (0.83, 3 pictures), not
  redrawn, falls on one reader who took the red lead in the dog's mouth for one clipped to its red collar. The other 62 pass, `about_to_trip` among them at 1.00 in five
  pictures, and every (template, angle) placed passes on its own in two or more pictures. Read strictly, the full marks the scorers themselves called hedged take no
  more under the gate (below): `photo` and `plant_flowers`, v0.42's two, pass on five pictures each (`vision/flaws_v043.md`, which lists the oddities for v0.44, first
  among them the reading dog's pose).
- A single half mark is noise. 19 pictures were identical to the pixel in v0.29 and v0.30, and 223 of their 230 items scored the same across fresh readers and scorers, with four templates moving by a half mark and no picture changed (`vision/flaws_v030.md`, A retest nobody planned). In v0.31, 12 pictures came back identical once more, and 137 of their 141 items scored the same; the one that went down is the gate's one failure. In v0.32, 19 came back identical, and 242 of their 246 items scored the same; the four that went down are again the gate's one failure, and a begging dog's half mark. In v0.33, 21 came back identical, and 274 of their 281 items scored the same, three moving up and four down. In v0.34, 26 came back identical, and 296 of their 299 items scored the same, two moving up and one down. In v0.35, 78 came back identical, and 806 of their 830 items scored the same, 7 moving up and 17 down, 12 of the 17 the clouds of two readers who named nothing in the sky. In v0.36, 60 came back identical, and 563 of their 576 items scored the same, 12 moving up, every one those clouds, and one down. In v0.37, 75 came back identical, and 775 of their 783 items scored the same, three moving up and five down, one of the five the gate's one failure. In v0.38, 22 came back identical, and 291 of their 294 items scored the same, three moving up and none down. With v0.39's cast redrawn none could; on the 7 pictures with the same seed and events in both screens, each in its own cast, all 75 items scored the same. In v0.40, 28 came back identical, and 326 of their 328 items scored the same, two moving up and none down, both on templates of v0.39's list. In v0.41, 43 came back identical, and 523 of their 532 items scored the same, three moving up and six down, three of the nine the clouds. In v0.42 none could: every person, dog and goat was drawn anew. Nor in v0.43, with both dogs, the goat and the two women redrawn. A template with few items can cross the gate on that alone: `read_bench` and `hang_laundry` have one item to a picture.
- What the trip's long box costs a fresh tier-4 search is as v0.29 found it, 166 failed seeds against 80. In v0.32 the garden, park and playground cells came back on their seeds; the street's did not under revision 30, in 39 seeds, and placed at once with v0.31's template set forced. In v0.33 all four came back unchanged, the street's on the same forced set, and in v0.34 to v0.38 all four came back on their seeds again, identical to the pixel in v0.37 and v0.38. With v0.39's redrawn cast the garden and park came back on their seeds and the street on its forced set; the playground's seed and the next 39 placed nothing, and the 41st did. In v0.40 all four placed again on v0.39's seeds and layouts, and in v0.41 all four came back identical to the pixel. With v0.42's redrawn cast the park placed on its seed and layout and the street on its forced set; the garden took three seeds and the playground forty. In v0.43 the park, the playground and the street placed on v0.42's seeds and layouts, and the garden on the fourth seed of its search.
- The oddities come in two rows. Readers' remarks per picture are counted directly from their descriptions and compare across
  screens, with the caveat that current readers write about 18% more than the v0.23 readers on the same pictures (`vision/v024/control/`,
  one reader and eight pictures). The row was recounted in v0.26, as the counter had taken bullets saying nothing is wrong for remarks, so its
  figures differ from those published up to v0.25. The scorers' logged oddities do not compare: v0.23's logged 25% of the remarks, v0.24's 83%, and
  from v0.25 the prompt caps them at three per picture. Earlier screens did not record which model read them; v0.24's to v0.43's ran on Claude Opus 5.5. Readers differ widely: on v0.28's nine, from 4.25 to 6.38 remarks a picture, on v0.29's from 4.50 to 5.75, and on v0.30's from 4.50 to 6.12. v0.31's nine wrote from 2.62 to 4.43, every one fewer than the fewest of v0.30's, and on 12 pictures identical in both screens remarks fell from 65 to 45. So a screen's readers can move the row by a third, and its fall to 3.51 in v0.31 says nothing about the drawings. v0.32's nine wrote from 2.71 to 4.43, 3.28 a picture, and on 19 pictures identical in both screens remarks fell from 79 to 67. v0.33's nine wrote from 2.44 to 4.11, 3.19 a picture, and on 21 identical pictures remarks rose from 77 to 88. v0.34's nine wrote from 2.40 to 4.50, 3.13 a picture, and on 26 identical pictures remarks were 96 in both. v0.35's nine wrote from 2.44 to 3.50, 2.88 a picture, and on 78 identical pictures remarks fell from 243 to 222. v0.36's nine wrote from 2.33 to 3.89, 3.10 a picture, and on 60 identical pictures remarks rose from 163 to 175. v0.37's nine wrote from 1.89 to 4.44, 2.82 a picture, and on 75 identical pictures remarks fell from 226 to 209. v0.38's nine wrote from 2.22 to 4.25, 3.38 a picture, and on 22 identical pictures remarks rose from 73 to 94. v0.39's twelve, eight pictures each, wrote from 2.62 to 4.00, 3.10 a picture, and on 7 pictures of the same events in both screens remarks fell from 28 to 25. v0.40's twelve wrote from 2.62 to 3.62, 3.04 a picture, and on 28 identical pictures remarks fell from 106 to 93. v0.41's twelve wrote from 2.25 to 3.88, 3.17 a picture, and on 43 identical pictures remarks rose from 151 to 156. v0.42's twelve wrote from 2.25 to 4.00, 3.05 a picture over all 93 screened, and v0.43's twelve from 2.50 to 4.12, 3.12 a picture over 94.
- No reader says "teenager": he is read as a boy, a boy or young man, or a person, which the key mostly accepts. The v0.24 redraw moved him
  from a woman to a boy, and v0.26's cap worn forwards moved him no further toward the key's own word. It read once as "worn backward or sideways" in v0.27.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 94 pictures 977 of 1003 scored items had full marks, ten of the 26 others the clouds of two readers who wrote "sunny" and two
  more a tree, and ten the reading dog's (1010 of 1020 in v0.42; 999 of 1008 in v0.41, five of the nine others the clouds of one reader; 1011 of 1014 in v0.40, 1025 of 1030 in v0.39, 841 of 842 in v0.38, 870 of 876 in v0.37, 873 of 876 in v0.36, and 855 of 877 in v0.35, 17 of
  whose 22 others were the clouds of two readers who named nothing in the sky). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, a v0.24 scorer eleven, and all three scorers of v0.25 to v0.38 listed such calls, enough to move a template across the gate. A v0.29 scorer listed 18 items that hold full marks because the free description committed and only the unsure section hedged, and a v0.30 scorer gave nothing under full marks in 302 and listed 22 it thought a stricter scorer might halve. Two v0.31 scorers gave nothing under full marks, in 236 and 253 items, among them a bird "about to take it" credited as pecking. v0.32's three gave one, three and three items under full marks, in 244, 288 and 244, v0.33's four, one and three, in 301, 255 and 306, v0.34's one, none and ten, in 314, 282 and 289, where the second listed four inferences a stricter scorer might halve, v0.35's twelve, one and nine, in 304, 283 and 290, v0.36's none, two and one, in 304, 283 and 289, where the first listed eight hedged inferences it credited in full, v0.37's four, one and one, in 304, 283 and 289, where the second listed seven items it credited in full on a committed free description, and two birds seen standing, not pecking, and v0.38's none, none and one, in 298, 268 and 276, where the first listed eleven items it credited in full though the reader gave a second reading, and the second twelve more. Halved, those 23 would take six templates under the gate; 11 of them are on pictures identical to v0.37's, whose scorers had credited all 11 in full (`vision/flaws_v038.md`). v0.39's four (for 96 pictures) gave two, two, none and one, in 282, 246, 269 and 233, where two listed 11 items they credited in full on a committed free description; halved, those would take one template under the gate (`vision/flaws_v039.md`). v0.40's four, and a fifth for one picture read again, gave one, one, one, none and none, in 228, 270, 260, 241 and 15, and listed 21 items they credited in full on a committed free description; halved, those would take five templates under the gate (`vision/flaws_v040.md`). v0.41's four gave one, two, five and one, in 255, 263, 253 and 237, the five the clouds of one reader, and their notes mark 16 items they credited in full on a committed free description; halved, those would take two templates under the gate (`vision/flaws_v041.md`). v0.42's four gave none, three, five and one, in 225, 270, 237 and 250 (scorer a's old picture 10 left out, read again with one of 25 under), and their notes mark 10 items they credited in full on a committed free description; halved, those would take two more templates under the gate (`vision/flaws_v042.md`). v0.43's four gave two, five, twelve and seven, in 231, 284, 262 and 226, and their notes mark seven; halved, those take none under the gate (`vision/flaws_v043.md`). A misread is a call too: the
  rake in v0.26's picture 37 could have been marked as sweeping half right.
- Tier-4 pictures are the hardest to place, and revisions 14 to 26 make them harder (walkers' and runners' lanes, pointing
  lines, feet off benches and off other events' things, the photographer's line of sight, the waver's clear hand, body gaps, the gap
  from thin parts, heads clear of figures up to 80 px apart in depth, the ground clear past a reading walker's obstacle, jumpers in the
  front half, an obstacle a full step ahead, runners clear of other movers, ducks off a float, sleepers clear of walkers' feet, nobody in
  the strip before the horizon, a person's box off the lamp post, the ground kept clear round a begging dog). A tier-4 playground plan now holds the bird stealing a sandwich and the
  square wheel, has no swing set as scenery and counts the railing up to 30% hidden, each of which alone placed nothing from 12 seeds, where all three placed 2 (`vision/flaws_v028.md`). So every tier-4 playground has those two, and none
  has the begging dog. A tier-4 street plan holds the bird too, on the evidence of one picture. A picture that also holds a floating, carried or soaked box falls back to the bucket from the long box, and none of the eleven screened pictures of the trip did.
- The square-wheeled bicycle still stands on its own: four stands have been tried on the bench, and each
  read as something else (pedals, legs) or not at all.
- The low kick's direction is ambiguous when the kicker's hair hides the face; the teenager kicks first,
  and the kick read in full in all its screened pictures. His cap now points the way he faces, but two readers still took it for sideways or backwards.
- The stuck girl on the seesaw always calls out, and from v0.33 no kick arcs are drawn at her feet: the tilt, the man's weight, her open mouth and
  the raised handle carry the reading, and in the v0.33 and v0.34 screens she was stuck in all three of her pictures.
- The body check (`assets/cast/gapcheck.py`) finds parts that come apart, not parts that pass through one
  another: a hand inside a hip or a lobe of skirt inside the bell is allowed, and only the outline drawn
  in the render shows whether the join looks right.
- The wind reaches the hat, the washing, an empty swing, the tree and the sky, but not hair or clothes, nor the
  bushes and flowers (three v0.19 probe readers noticed): the cast is posed and rendered in 3D, and a blowing
  fringe or skirt would be a new rig. From revision 32 no can, pan, hose or sprinkler pours in a windy picture, and from revision 33 no pile is
  swept or raked in one (in v0.34 one lay still: "yet the woman's pile of leaves stays neatly in place").
- The isolation bench reads one template cut out of its picture. A visual that reads alone can still be
  misread among other events, so the bench comes before the test scenes and the screen, never instead of them.
- The planner's priors come from the v0.43 calibration, with f = 0 and a at its centre for every inference and contradiction, as in
  v0.20 to v0.42. 42 fields moved by 0.002 or more, most of all `dog_reading`'s contradiction (s from -0.44 to -0.57, the dog lying down) and `cat_stalks_bird`'s inference (34 in v0.42, with the cast redrawn, most of all `dog_begs`'s inference; two in v0.41). The ladder's still rests on one sampled placement, since v0.29's lamp rule.
- Exact rebuilds hold within a release, on the pinned Pillow: the v0.43 placement rules (revision 41) keep the reading dog away from the trip and from anyone reading as
  they walk, lay its paper flat on the ground, put a dog and never a goat on the stopped hose, draw the stalking cat in profile only with a gap before the bird, close the
  begging dog's mouth, and draw the goat's rope slack, never leaving it untethered. The leaning paper and the stalking cat at 135 were read on the bench and are kept behind
  switches (`READ43` "B", `CAT43` "C"). A v0.42 record rebuilds with the v0.42 package. Revisions 31 to 41 keep their rules in the templates'
  placement and binding, the planner's features and plans, the setting or `fits`, each behind its revision; revision 30's sky rule is still read at import (`RUNBOOK.md`).
- Every variant comes from the v0.43 cast (builder 0.43.0, `out043`), which redraws both dogs (the legs; the reading dog lying down), the goat (its horns, beard and standing neck) and the two women (head and face; the woman in yellow's bob and shoes): every other family's renders carried over from `lib042`, and the seesaw's riders are in two pieces each, as before. The library keeps only the 404 variants the v0.43 set and probes use. The bench
  variants (`TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ`, `TPDB_BEARD`, `TPDB_BROW`, `TPDB_BLUSH`, `draw.WHEEL27`, `draw.SPLAT28`, `draw.SEESAW_IN28`, `draw.SWING35`, `library.SHADOW28`, `library.SHADOW29`, and `SLEEP29`, `TRIP29`, `TRIP_OBJ29`, `DUCK29`, `DOOR29`, `HOSE29`, `BULGE29`, `FISH29`, `LADDER_LAMP29`, `HOSE30`, `FISH30`, `TRIP_W30`, `TRIP_LANE30`, `CRUMB30`, `SEESAW31`, `RIDE31`, `CASTLE31`, `LIMB31`, `LOW32`, `LOW_IN32`, `LOW_RISE32`, `LOW_RISE_B32`, `STUCK32`, `HANDLE32`, `HOSE33`, `KICK33` and `BASKET38` in `templates.py`, `REEL30` and `REEL31` in `settings.py`, and `TPDB_VEST`, `TPDB_CONE`, `TPDB_BOX`, `TPDB_LOW`, `TPDB_SEAT34`, `TPDB_HAIR34`, `TPDB_MOUSTACHE36`, `TPDB_MOUSTACHE36_FLAT`, `TPDB_BUCKET36`, `TPDB_ISECT39`, `TPDB_SHOE39`, `TPDB_KNEE39`, `TPDB_MID39`, `TPDB_BELT39`, `TPDB_BEN39`, `TPDB_QUAD39`, `TPDB_ART39`, `TPDB_GOAT39`, `TPDB_REACH40`, `TPDB_HOSE40`, `TPDB_GRAZE40`, `TPDB_WALK40`, `TPDB_BEG41`, `TPDB_STALK41`, `TPDB_MEI41`, `TPDB_GOAT42`, `TPDB_DOG42`, `TPDB_BEG42`, `TPDB_CAT42`, `TPDB_MID42`, `TPDB_BELT42`, `TPDB_FOOT42`, `TPDB_MEI42`, `TPDB_DOG43`, `TPDB_GOAT43`, `TPDB_READ43` and `TPDB_ADULT43` in the cast, and `YAW39`, `TUFT40`, `ICE40`, `BOX41`, `SEASON41`, `GOAT42`, `BIRD42`, `KINK42`, `BEG40`, `TRIP43`, `READ43`, `HOSE43`, `CAT43`, `BEGX43` and `TETHER43` in `templates.py` and `HEAP39` and `HEAP40` in `draw.py`) stay in the code.
- The figures are still narrow. Legs an eighth shorter and limbs 14% thicker took the bench from eight remarks to three, on four cut-outs a side, but the screen's remarks on
  thin or long bodies did not fall (six pictures to eight in v0.27, to thirteen in v0.28 and v0.29, and back to six in v0.30, with nothing changed, and one each in v0.31 and v0.32, with readers who remark less; by keyword, so that row says little). A real change of build is a larger job than these.
- A person in full profile has the head turned 35 degrees to the viewer, baked as a twin action of the pose (`__p`), except where a hand-held thing at the face would be left behind
  (`PROFILE_SKIP`). Those poses keep the hidden face readers remark on.
- Age of acquisition is recorded at weight 0, so it moves nothing until the pilot's pre-registered test says it
  should. The bundled ratings are a verbatim excerpt of Kuperman et al. (2012) under CC BY-NC-ND 3.0, taken from a
  copy in the lftk package; they have not yet been checked against the original file at crr.ugent.be.
- Key words follow one rule (the word the first accepted answer names: an action's verb, or the thing that names
  it), applied by hand in v0.20 and unchanged since; a key that is itself an accepted answer was left alone.
- The sleeping cat, 1.4 times its v0.17 size, read as "small" in one v0.18 probe and drew no remark in its four
  v0.19 pictures; drawn larger, the standing and stalking cats would come out as big as the small white dog.
- Twenty-seven actions in the cast are used by no template; they are kept for later templates and left
  out of the gallery and the screen, so they have never been read blind.
- Edge density is not part of the isomorph rule. Street pictures stay the busiest, so a street
  isomorph of a park or playground picture carries more visual detail at the same object count.
- The top third of park and playground pictures is still mostly sky.
- A filler closer than 24 px to the picture's side edge is now moved 30 px inside it, and no reader said one
  was cut off; the sun can still sit partly off the top edge, where the backdrop draws it.
- The strip before the horizon leaves the playground less room: the tier-3 playground placed only without template-variety steering in
  v0.24 and v0.25, and with it from v0.26. The v0.43 isomorphs are new, the tier-4 one a garden drawn from the tier-4 playground; the tier-3 playground itself placed in v0.43 only on a fresh seed list without template-variety steering, after the showcase pass and its search failed 13 base seeds; an animal whose template its partner shares is drawn at the
  partner's angle (revision 37), a constraint `calibrate.py` has not yet tested for difficulty.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- A shadow from the figure's own footprint is smaller, and a body lying down has little of it showing. The sleeping dog now reads in full on its new pose and that shadow; a wider one did little on the bench, so whether the shadow cost it marks in v0.28 is still not shown.
- The trip reads in full on the long box, in eleven pictures in v0.30 and five each in v0.31 to v0.41. In v0.42 it read in two of three: the third reader, a reading dog beside the walker, saw the box and no trip. From v0.43 the reading dog is kept away from it (revision 41), and it read in all five of its pictures. In v0.30, five of its readers also said the walker may step round it, which on the same five pictures went from four of five to one of five with nothing changed.
- The man on the seesaw's low end is drawn astride, his far leg behind the plank. The v0.32 bench turned him away, or put both legs behind the plank, and readers of each still doubted his seat (legs out was set aside on looking);
  in the v0.32 screen he drew one remark in three pictures, that "the seesaw plank seems to pass behind or among the old man's legs". He is off the list; in v0.33 his legs over the plank drew a remark once more. The stuck girl holds a handle raised with her,
  and once a reader saw her hover, from the kick arcs under her feet, which v0.33 does not draw.
- A rider on the seesaw is two pictures, the far leg drawn behind the plank as background and the rest of the figure in front. The far leg is in no count, mask or check of the scene's own.
  Until v0.32 the validator failed the 12 pieces on their names; it now checks each by its base pose and leaves the ground rule to the piece with the body.
- The child on the swing is swung out 12 degrees (revision 33), turned in the picture with its seat and ropes, not posed so in the cast. The frame is widened on the
  side away from the path when a child swings, so its legs stay off the path, and an empty seat keeps the frame it had. One v0.35 reader found the ropes not quite
  "directly above the seat", and read the child as swinging.
- The gate's knob is kept 16 px clear of every figure's drawing, hair, hands and props included (revision 35; revision 34's box round the face missed the back of a
  head in profile). The sweeper it was for now stands lower on the path, and was "a boy with short dark hair". A storm pointer's garden has no clothesline
  (revision 35): with the washing off it (revision 34) the empty line was offered as what she pointed at, and the planner had long noted that an empty line reads
  as a bare wire. Her readers still offer the tree or the roof as a second reading. From revision 36 no cat walks the fence in her picture (one storm pointer was offered
  the cat on the fence in three screens running) and the stalking cat stays on the ground, and in the garden no bird perches up high either; the three v0.38 storm pointers
  read at the clouds. The bird is dropped from the plan in the garden only: dropped in every setting, it changed a playground cell whose picture has neither, as an earlier try of its seed drew the pair.
- The broom's and the rake's heaps have been drawn three ways, and each drew a remark on the season: v0.38's autumn leaves "under green trees" (seven pictures),
  v0.39's summer heap, whose green leaves were "a little odd for raked fallen leaves" (five), and v0.40's dry leaves, leaf-shaped (`draw.HEAP40` "D"), "The brown leaves
  are slightly odd when the trees are green" (five pictures, from three readers). Cut grass read as a dome or dustpan on the bench, and grit as dust or a rock.
  In v0.41, the heap unchanged, no reader remarked on the season in 93 pictures; trees turning over the heap read as fruit on the bench (`vision/isolation_v041.md`).
- Animals are drawn at 45 or 135 as well as 90 for eight templates (revision 37), and the songbirds and the duck at 45 for four more (revision 40); the stalking cat is drawn in profile only from revision 41, its legs tangled at 45 and at 135; people are not. The dog walked on a lead is drawn at 90 only: at 45 its lead
  crossed its back at every spot tried, which revision 12 forbids. Every (template, angle) placed read at 1.00 in two or more pictures in v0.39, and at 0.94 or more in v0.40 to v0.42 and 1.00 in v0.43, the four bird templates at 45 too,
  and the scorers' oddities by angle were about the goat out of place, the begging dog's upright pose in profile and the stalking cat's legs at 45, not about an
  angle as such.
- The begging dog's forelegs are folded from v0.41, the elbows forward and the paws tipped down at the chest: held out level, they were "stiff rods" to the bench's readers
  (`vision/isolation_v041.md`). From v0.42 it sits on its haunches with a shorter trunk, and no screen reader saw it kneel; once it was "jumping up". Nobody else with an
  ice cream comes near it (revision 40), and in both v0.42 pictures with another eater in view the reader gave the one on the bench. From v0.43 its mouth is closed;
  a head lowered to look at the eater rather than the sky did not place at 45, where the gaze check found it facing the viewer (`vision/isolation_v043.md`).
- The goat is tethered when it grazes, a rope from its collar to a peg (revision 40): out of place twice in v0.42, both softened ("a little unusual, but it is tethered
  and calm"), where it was seven times in v0.41. From v0.43 its rope is slack and it is never drawn untethered or on the stopped hose; unusual in four of six
  pictures, and twice, from behind, possibly a sheep. The reading dog sat with its hind legs folded in v0.42, and its paper "stands upright on its own" in three descriptions; v0.43 laid it
  down over the paper, which read as lying on it.
- A reader can describe the wrong picture. v0.40's reader 7 described picture 56 under picture 55's name, and wrote of picture 56 that it "couldn't find any difference between this
  picture and pic_55"; the files were distinct and right. Picture 55 was read again by a fresh reader and scored by a fresh scorer, and reader 7's description is kept aside
  (`vision/flaws_v040.md`). A scorer who finds a description that does not fit its key, as this one did, is the check.
- The washing's hanger is read hanging it out from the basket at her feet and the drops, not from the pose: on the bench, with neither, three readers of three could
  not tell up from down, and some design-test readers still said the pose alone could go either way (none of v0.38's three did, and of v0.39's five, one raised taking it down and settled it on the drips and the basket). All the washing drips, the jeans and the sleeve over the basket's rim too: with
  the shirt alone wet, a design test read the basket's clothes as dry and "about to get wet". The washing and a watering can placed 0 of 12 together, with the
  basket or without it.
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
