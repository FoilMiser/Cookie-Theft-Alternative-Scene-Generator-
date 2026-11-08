# TPDB v0.42: the goat, the dogs, the trousers, the shoes and the woman in yellow redrawn, the goat tethered, the birds turned, read a thirty-ninth time

v0.41 ended with all 64 templates through the gate, and read strictly with two under it: `blocked_hose`, its cause given with "it could also simply be turned off", and `rain_coming`. The list went on to a second ice cream near the begging dog, the dog's body in profile, "upright", "kneeling", "human-like", the woman in yellow called "girl", and the goat out of place. Sam's notes on the figures (`tpdb_work/figure-fixes-v041.md`) ranked nine more things by what they cost a reader. First the goat, a sphere head on a hunched body. Then the belt, a ring at the waist, and the trousers' V across the front, a "briefs" look. Then the dog's chest patch, "like a bib or nappy", the begging and reading dogs' human poses, front-view shoes and bare legs, the cat, the woman in yellow, and the birds always in profile.

v0.42 benched those in two rounds and took most of them (builder 0.42.0):
- **The goat:** a wedge head on a neck, the back a fifth longer and level on shorter legs, split hooves, a pointed beard and a red collar; tethered to a peg when it grazes.
- **The dogs:** the tan dog's patch a narrow blaze down the chest, the far legs a step darker, a brown patch on the spotted dog's near foreleg, and a longer muzzle with a level top. The begging dog sits on its haunches with a shorter trunk, and the reading dog's hind legs fold beside it.
- **The people:** no hip node in the trousers, so no V; no belt under an untucked tee; shoes with a longer toe and a sole; bare legs with a calf. The woman in yellow has a low bun.
- **The birds:** the songbirds and the duck at 45 as well as 90.
- **Placement revision 40:** the goat's tether and the birds' angle; no one else with an ice cream near the begging dog; after the screen, the square-wheeled bicycle off the stall and the bench.
- **Read and left as they were:** the cat (its legs tangled either way) and a crimp in the stopped hose. The knees were priced and not changed.

The set was regenerated and screened a thirty-ninth time. Every person, dog and goat is drawn anew, so no picture is identical to v0.41's.

The thirty-ninth screen read 93 pictures, the set's 21 and 72 probes, with twelve readers and four scorers, and two pictures read and scored on their own after it: 1010 of 1020 scored items had full marks, and none was misread. 63 of 64 templates pass the gate; `about_to_trip` falls, on one reader who saw the box and the walking reader and did not link them. Every (template, angle) the animals are drawn at passes on its own, the birds at 45 among them. The goat, tethered, was out of place twice where it was seven times; the begging dog kneeled in none of its pictures; no reader mentioned a belt, a V, a bib or the shoes. The woman in yellow, with her new bun, was still "girl" in six of her fourteen pictures.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.41 readers, or Sam's notes, saw | v0.42 |
|---|---|
| The goat out of place in seven pictures, once "a sheep"; its sphere head, an ear like an eye socket, a hunched body | Redrawn and tethered. Tied to a stake in six descriptions, out of place twice, both softened ("a little unusual, but it is tethered and calm"); no sheep |
| The begging dog at 90 "upright", "kneeling", "human-like" | On its haunches with a shorter trunk: kneeling or a person in none of its five pictures (three of three of v0.41's on the bench) |
| A second ice cream near the begging dog: "I can't tell who the dog is begging from" | Nobody else with an ice cream near it (revision 40); in both pictures with another eater in view, the reader gave the one on the bench |
| The belt a ring at the waist, and a V across the trousers, a "briefs" look (Sam's notes) | No belt under a tee, no hip node: no description mentions a belt, briefs or a waistband (v0.41's mentioned a belt in six) |
| The dog's chest "like a bib or nappy"; white legs like stilts | A narrow blaze, darker far legs: no bib or stilts in 30 pictures with a dog |
| The reading dog's hind legs stretched out "like a person sitting" | Folded, the trunk shorter: no reader called it a person. But its paper "stands upright on its own" three times (once in v0.41) |
| Birds and the duck only in profile | At 45 too: every (template, angle) pair of the four bird templates reads 1.00 |
| The woman in yellow called "girl" | A low bun, read as "a ponytail": "girl" in 6 of her 14 pictures, five hedged (8 of 24 in v0.41). Not fixed |

Left as notes for the pilot: the cat's legs at 45, the stopped hose's swelling, and figures drawn over the prop beside them.

## The isolation bench

The two lists were benched in two rounds of single cut-outs (`vision/isolation_v042.md`). Round 1, twenty-five readers of 50 cut-outs, two to a reader and never two takes of one thing, read each thing in v0.41's cast and scene against the cast with every switch on:
- **The goat:** tethered in all three cut-outs, and the disc head gone; the hunch at 45 and 135 stayed.
- **The begging dog:** kneeling or a person in three of v0.41's three cut-outs, in none of the new three.
- **The trousers, belt and shoes:** nothing said of them; v0.41's belt once "a belt, or ... the gap".
- **The woman in yellow:** a woman in all six whole pictures on both sides.
- **The cat:** tangled on both sides, and the smaller head drew "a rat or weasel".
- **The crimp at the paw:** once "a separate stray bit".
- **The birds at 45:** each read.

Round 2, nine readers of one cut-out each, read the goat's graze sloped to the rump (no better, and once "kneeling or bowing", so the level back stayed), the reading dog with the shorter trunk (the person in one of two), and the dogs cut out close at 45, where nothing chose between them.

Before any reader, the bench's own look caught five things: the goat's first collar a scarf and its beard a beak; nostrils in front of the muzzle; a leaning beg that stretched into a tube; a set-back hip node that left the V; and cream soles that read as white discs.

## Design tests

The cast of builder 0.42.0 and revision 40 were read blind in whole test scenes among other events (`vision/design_tests_v042.md`, six pictures, six readers), each with the redrawn animal at a forced angle. All six placed on their first seed:
- **The goat** is tethered in both pictures: it "is tied by a rope to a small stake near the gate and is eating a tuft of grass".
- **The begging dog** begs from the bench in both pictures with a second ice cream, "as if begging, looking up toward the man and his ice cream", and nobody saw it kneel.
- **The reading dog** "sits upright on its haunches", and of its paper "reads most like reading".
- **The birds and the duck at 45** read as at 90.
- **The woman in purple** was "a girl in a purple top" once, as she has been before; the woman in yellow was "a woman in a yellow dress".

## Placement revision 40

Every record stores the placement revision it was made with. v0.42 pictures use revision 40:
- **The goat's tether:** a rope from its collar to a peg in the ground when it grazes (`templates.GOAT42` "T").
- **The birds' angle:** the songbirds and the duck at 45 as well as 90 where they need no direction (`templates.BIRD42` "B", `ANIMAL_YAWS40`).
- **The begging dog's zone:** no one else with an ice cream near it, in front of the bench as well (`templates.BEG40` "B").
- **The square wheel:** the bicycle or barrow clear of the stall and the bench, added after the screen (in front of a stall's legs, the bicycle was "parked against the stall").
- **The stopped hose's crimp:** read on the bench and not taken (`templates.KINK42` "O").

A v0.41 record rebuilds with the v0.41 package. The cast redraws every person, both dogs and the goat (builder 0.42.0).

Every cell of the set placed under revision 40, tiers 1 to 3 on v0.41's base seeds, the tier-4 park on its seed and layout, the street on v0.29 to v0.41's forced set, the garden on the third seed of its search and the playground on the 40th. The five isomorphs are new, the tier-4 one searched again after the screen's rule. The probe pass gave `blocked_hose` and `rain_coming` five pictures each, the pass stratified by angle filled the begging dog at 45 and the birds, and two probes were forced for `windy_hat`, the second with `balloon` and `wave` after the screen. Every picture was looked at before the screen. All 93 records rebuild identical to the pixel, and the library passes the validator in full, 408 of 408.

The planner's difficulty priors are the calibration measured on the v0.42 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.41. With the cast redrawn, 34 fields of the calibration moved by 0.002 or more, most of all `dog_begs`'s inference (s from -0.76 to -0.89) and `dog_reading`'s.

## The thirty-ninth blind screen

Twelve fresh readers, who had never seen the key, described every picture of the new set and 72 probe pictures; four separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.41.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) | v0.25 (21 pictures) | v0.26 (21 pictures) | v0.27 (21 pictures) | v0.28 (21 pictures) | v0.29 (21 pictures) | v0.30 (21 pictures) | v0.31 (21 pictures) | v0.32 (21 pictures) | v0.33 (21 pictures) | v0.34 (21 pictures) | v0.35 (21 pictures) | v0.36 (21 pictures) | v0.37 (21 pictures) | v0.38 (21 pictures) | v0.39 (21 pictures) | v0.40 (21 pictures) | v0.41 (21 pictures) | v0.42 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 0.97 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 | 0.98 | 0.95 | 0.95 | 0.88 | 0.98 | 0.99 | 1.00 | 0.96 | 0.96 | 0.99 | 0.96 | 0.97 | 0.97 | 0.98 | 1.00 | 0.99 | 0.96 | 0.94 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 1.00 | 0.94 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.99 | 0.98 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 0.98 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.98 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 | 0 of 286 | 0 of 289 | 0 of 283 | 0 of 284 | 0 of 285 | 0 of 284 | 1 of 286 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 286 | 0 of 287 | 0 of 287 | 0 of 287 | 0 of 290 |
| Oddities per picture, as logged by the scorers | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 | 2.6 | 2.6 | 2.2 | 2.0 | 2.3 | 2.3 | 0.6 | 0.8 | 0.9 | 0.5 | 0.2 | 0.6 | 0.4 | 0.8 | 0.8 | 0.5 | 0.4 | 0.7 |
| Readers' remarks per picture (recounted in v0.26) | 8.8 | 5.4 | 6.4 | 4.8 | 4.7 | 4.8 | 4.9 | 4.4 | 4.3 | 4.4 | 4.4 | 4.4 | 3.9 | 3.9 | 4.4 | 4.0 | 4.0 | 3.9 | 4.2 | 3.9 | 5.6 | 5.9 | 5.3 | 5.8 | 5.1 | 5.2 | 5.2 | 3.5 | 3.3 | 3.2 | 3.1 | 2.9 | 3.1 | 2.8 | 3.4 | 3.1 | 3.0 | 3.2 | 3.0 |

Across all 93 pictures 1010 of 1020 scored items had full marks, and none was misread. Of the ten under full marks, two are setting items (clouds and a tree). The other eight:
- three half marks on the reading dog, in two pictures of the set: the paper "grabbed or knocked over" or "fetched";
- the trip, not inferred (the box "has no obvious owner or purpose");
- four half marks on a balloon, a dropped ice cream, a dog by the door and a probe's ice cream, each offered with another reading.

The set's headline is all items 0.984 (0.995 in v0.41).

**After the screen.** The first count failed `square_wheel` (0.867), on the tier-4 street's isomorph, where the square-wheeled bicycle stood in front of a fruit stall's legs and read as "parked against the stall". Revision 40 now keeps it off the stall and the bench. The one picture that changed was searched again and read by a fresh reader and a fresh scorer. `square_wheel` passes at 1.00, and `about_to_trip`, which lost its fourth picture with the old one, falls. One more probe put `windy_hat`, `balloon` and `wave` back at three pictures each, and it read in full.

**What the full marks rest on.** The scorers' notes mark 10 items they credited in full where the free description commits and the unsure section adds another reading (16 in v0.41). Halved, 61 of 64 templates pass, with `about_to_trip`, `photo` (0.833) and `plant_flowers` (0.667) under the gate, the last two on three items each.

**Remarks were 3.05 a picture, 284 on 93 pictures**, from 2.25 to 4.00 a reader.

What this release redrew or ruled, and the one that fell under the gate (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.41 | v0.42 | v0.42 meaning items |
|---|---|---|---|
| `goat_grazing` | 1.00 (6 items) | 1.00 (6 items) | — |
| `dog_begs` | 1.00 (12 items) | 1.00 (15 items) | 1.00 (5) |
| `dog_reading` | 1.00 (12 items) | 0.92 (18 items) | 0.88 (12) |
| `blocked_hose` | 1.00 (24 items) | 1.00 (24 items) | 1.00 (6) |
| `bird_perched` | 1.00 (3 items) | 1.00 (5 items) | — |
| `feed_birds` | 1.00 (3 items) | 1.00 (3 items) | — |
| `bird_steals` | 1.00 (18 items) | 1.00 (12 items) | 1.00 (4) |
| `ducks_swimming` | 1.00 (3 items) | 1.00 (5 items) | — |
| `square_wheel` | 1.00 (12 items) | 1.00 (12 items) | 1.00 (8) |
| `about_to_trip` | 1.00 (15 items) | 0.89 (9 items) | 0.67 (3) |

`goat_grazing`, the goat redrawn and tethered, reads 1.00 in six pictures, at 90, 45 and 135; out of place twice, both softened, and never a sheep. `dog_begs`, on its haunches, holds at 1.00 in five pictures, with no kneeling. `dog_reading`, its hind legs folded and its trunk shorter, is at 0.917: its paper "stands upright on its own" in three descriptions. The four bird templates read 1.00 at 90 and at 45. `blocked_hose` reads 1.00 and 1.00 strictly, the crimp not taken. No description mentions a belt, briefs, a waistband, a bib, stilts or the shoes.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 | v0.27 | v0.28 | v0.29 | v0.30 | v0.31 | v0.32 | v0.33 | v0.34 | v0.35 | v0.36 | v0.37 | v0.38 | v0.39 | v0.40 | v0.41 | v0.42 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 | 61 | 59 | 63 | 61 | 64 | 63 | 63 | 63 | 63 | 64 | 63 | 64 | 63 | 64 | 64 | 64 | 64 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 | 3 | 5 | 1 | 3 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |

Every template was screened in at least three pictures (42 in three, 7 in four, 7 in five, 4 in six, 2 in seven, 1 in twelve and 1 in nineteen), and 63 of 64 pass. `about_to_trip` falls at 0.889, on one zero in three pictures; it was 1.00 in five pictures in v0.41, and its drawing has not changed. The lowest that pass are `dog_reading` and `dog_wants_walk` (0.917) and `lost_balloon` (0.967). Per angle (`vision/v042/gate_yaw.json`), all 25 (template, angle) pairs pass, v0.41's 17 and the four bird templates at 90 and 45; the lowest is the dropped ice cream at 90 (0.938). The gate is a filter, and the pilot with people is the test of difficulty.

Templates that did not pass (`vision/flaws_v042.md` gives what the readers saw and the next fix):

| Template | v0.42 mean | Pictures | Misreads |
|---|---|---|---|
| `about_to_trip` | 0.89 (9 items) | 3 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.777 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s1021 | 5 | 0 (0) | 3 | 0.780 | — | 13 | 0.022 | kick ball, ice cream, fly kite |
| T1_street_s1031 | 5 | 0 (0) | 3 | 0.778 | — | 16 | 0.045 | birds flying, run, wave |
| T1_playground_s11041 | 5 | 0 (0) | 3 | 0.762 | — | 13 | 0.033 | photo, sandbox, read bench |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.713 | 0.417 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_park_s022 | 8 | 1 (0) | 4 | 0.711 | 0.407 | 21 | 0.029 | kite in tree, push stroller, plant flowers, carry box |
| T2_park_s9118_iso (isomorph of T2_playground_s042) | 8 | 1 (0) | 4 | 0.726 | 0.353 | 17 | 0.028 | dog begs, photo, run, water flowers |
| T2_street_s1032 | 8 | 1 (0) | 4 | 0.710 | 0.373 | 16 | 0.047 | cat stalks bird, balloon, carry bag, read bench |
| T2_street_s17109_iso (isomorph of T2_park_s022) | 8 | 1 (0) | 4 | 0.711 | 0.391 | 16 | 0.046 | lost balloon, jump, birds flying, ice cream |
| T2_playground_s042 | 8 | 1 (0) | 4 | 0.711 | 0.361 | 17 | 0.035 | cat stalks bird, dog playing, ice cream, sandbox |
| T3_garden_s6013 | 12 | 3 (1) | 6 | 0.641 | 0.297 | 23 | 0.046 | bird steals, about to trip, dog reading, swing, dog sleeping, jump |
| T3_garden_s7102_iso (isomorph of T3_street_s1133) | 12 | 3 (0) | 5 | 0.669 | 0.325 | 20 | 0.040 | ball in tree, cat stalks bird, lost balloon, read bench, birds flying |
| T3_park_s023 | 12 | 2 (1) | 5 | 0.639 | 0.330 | 21 | 0.028 | lost balloon, square wheel, fishing, bird perched, ducks swimming |
| T3_street_s1133 | 12 | 3 (0) | 5 | 0.669 | 0.342 | 22 | 0.053 | about to trip, dog begs, ball in tree, water flowers, feed birds |
| T3_street_s10104_iso (isomorph of T3_park_s023) | 12 | 2 (1) | 5 | 0.646 | 0.321 | 20 | 0.053 | ball in tree, square wheel, ice cream, birds flying, run |
| T3_playground_s6043 | 12 | 2 (0) | 5 | 0.642 | 0.308 | 20 | 0.036 | seesaw heavy, ice cream drop, fly kite, cat sleeping, bird perched |
| T4_garden_s407995 | 18 | 5 (2) | 9 | 0.566 | 0.236 | 27 | 0.046 | ball in tree, cat stalks bird, blocked hose, dog reading, square wheel, dog sleeping, cat sleeping, read bench, play catch |
| T4_park_s728923 | 18 | 5 (2) | 8 | 0.566 | 0.251 | 32 | 0.037 | ice cream drop, ducks bread, kite in tree, dog reading, pan watering, birds flying, goat grazing, sweep |
| T4_street_s430752 | 18 | 5 (2) | 9 | 0.580 | 0.206 | 27 | 0.056 | bird steals, about to trip, ball in tree, dog reading, water upward, birds flying, sweep, jump, carry bag |
| T4_street_s37111_iso (isomorph of T4_park_s728923) | 18 | 5 (2) | 8 | 0.584 | 0.245 | 26 | 0.055 | ice cream drop, cat stalks bird, lost balloon, dog reading, bucket hat, bird perched, sweep, carry box |
| T4_playground_s460662 | 18 | 5 (2) | 9 | 0.557 | 0.223 | 27 | 0.042 | bird steals, kite in tree, lost balloon, square wheel, dog reading, run, photo, dog playing, birds flying |

Isomorph pairs differ by at most 0.018 in content and 0.017 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 25,810 | 27 | 11,275 | 10^12.7 |
| garden | 3 | 2,343,163 | 296 | 310,307 | 10^18.5 |
| garden | 4 | 70,686,492 | 565 | 5,759,476 | 10^23.3 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 45,955 | 24 | 19,978 | 10^11.2 |
| park | 3 | 5,569,417 | 236 | 972,951 | 10^17.3 |
| park | 4 | 307,551,136 | 376 | 41,212,001 | 10^23.1 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,298 | 24 | 2,847 | 10^11.7 |
| street | 3 | 420,725 | 220 | 65,745 | 10^17.2 |
| street | 4 | 6,676,618 | 330 | 876,099 | 10^21.6 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.3 |
| playground | 3 | 738,151 | 183 | 110,468 | 10^17.5 |
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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, v0.41 folds the begging dog's forelegs, and v0.42 redraws the goat, the dogs, the trousers' waist, the shoes and the woman in yellow's hair |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out042/` | The 18 `.blend` families (builder 0.42.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib042/` | Every variant the generated scenes and probes use, carried over from `lib041` (the cats, songbirds and duck) or rendered from `out042` |
| `assets/cast/gallery042/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (177, all pass the validator) |
| `scenegen/` | The generator (0.42.0, placement revision 40); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.42 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v042.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v042.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v042.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all thirty-nine screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out042                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out042 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v042   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v042 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery042 --old-gallery <v0.41 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.42 --single   # the release as one zip, tpdb_v0.42.zip
```

The release is one zip, `tpdb_v0.42.zip`, about 227 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.41 record rebuilds with the v0.41 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- One template falls under the legibility gate after the v0.42 screen: `about_to_trip` (0.89, 3 pictures), on one reader who saw the walking reader and the box
  and did not link them, a template not redrawn that read 1.00 in five pictures in v0.41. The other 63 pass, and every (template, angle) placed passes on its own in
  two or more pictures. Read strictly, the full marks the scorers themselves called hedged would take two more under the gate (below), `photo` and `plant_flowers`,
  on three items each; neither of v0.41's two is among them. A first count failed `square_wheel` instead, on a bicycle in front of a stall's legs: a rule moved it and
  the one picture it changed was read again, which took `about_to_trip`'s fourth picture out (`vision/flaws_v042.md`, which lists the oddities for v0.43, first
  among them the woman in yellow, still "girl" in six of her fourteen pictures).
- A single half mark is noise. 19 pictures were identical to the pixel in v0.29 and v0.30, and 223 of their 230 items scored the same across fresh readers and scorers, with four templates moving by a half mark and no picture changed (`vision/flaws_v030.md`, A retest nobody planned). In v0.31, 12 pictures came back identical once more, and 137 of their 141 items scored the same; the one that went down is the gate's one failure. In v0.32, 19 came back identical, and 242 of their 246 items scored the same; the four that went down are again the gate's one failure, and a begging dog's half mark. In v0.33, 21 came back identical, and 274 of their 281 items scored the same, three moving up and four down. In v0.34, 26 came back identical, and 296 of their 299 items scored the same, two moving up and one down. In v0.35, 78 came back identical, and 806 of their 830 items scored the same, 7 moving up and 17 down, 12 of the 17 the clouds of two readers who named nothing in the sky. In v0.36, 60 came back identical, and 563 of their 576 items scored the same, 12 moving up, every one those clouds, and one down. In v0.37, 75 came back identical, and 775 of their 783 items scored the same, three moving up and five down, one of the five the gate's one failure. In v0.38, 22 came back identical, and 291 of their 294 items scored the same, three moving up and none down. With v0.39's cast redrawn none could; on the 7 pictures with the same seed and events in both screens, each in its own cast, all 75 items scored the same. In v0.40, 28 came back identical, and 326 of their 328 items scored the same, two moving up and none down, both on templates of v0.39's list. In v0.41, 43 came back identical, and 523 of their 532 items scored the same, three moving up and six down, three of the nine the clouds. In v0.42 none could: every person, dog and goat was drawn anew. A template with few items can cross the gate on that alone: `read_bench` and `hang_laundry` have one item to a picture.
- What the trip's long box costs a fresh tier-4 search is as v0.29 found it, 166 failed seeds against 80. In v0.32 the garden, park and playground cells came back on their seeds; the street's did not under revision 30, in 39 seeds, and placed at once with v0.31's template set forced. In v0.33 all four came back unchanged, the street's on the same forced set, and in v0.34 to v0.38 all four came back on their seeds again, identical to the pixel in v0.37 and v0.38. With v0.39's redrawn cast the garden and park came back on their seeds and the street on its forced set; the playground's seed and the next 39 placed nothing, and the 41st did. In v0.40 all four placed again on v0.39's seeds and layouts, and in v0.41 all four came back identical to the pixel. With v0.42's redrawn cast the park placed on its seed and layout and the street on its forced set; the garden took three seeds and the playground forty.
- The oddities come in two rows. Readers' remarks per picture are counted directly from their descriptions and compare across
  screens, with the caveat that current readers write about 18% more than the v0.23 readers on the same pictures (`vision/v024/control/`,
  one reader and eight pictures). The row was recounted in v0.26, as the counter had taken bullets saying nothing is wrong for remarks, so its
  figures differ from those published up to v0.25. The scorers' logged oddities do not compare: v0.23's logged 25% of the remarks, v0.24's 83%, and
  from v0.25 the prompt caps them at three per picture. Earlier screens did not record which model read them; v0.24's to v0.42's ran on Claude Opus 5.5. Readers differ widely: on v0.28's nine, from 4.25 to 6.38 remarks a picture, on v0.29's from 4.50 to 5.75, and on v0.30's from 4.50 to 6.12. v0.31's nine wrote from 2.62 to 4.43, every one fewer than the fewest of v0.30's, and on 12 pictures identical in both screens remarks fell from 65 to 45. So a screen's readers can move the row by a third, and its fall to 3.51 in v0.31 says nothing about the drawings. v0.32's nine wrote from 2.71 to 4.43, 3.28 a picture, and on 19 pictures identical in both screens remarks fell from 79 to 67. v0.33's nine wrote from 2.44 to 4.11, 3.19 a picture, and on 21 identical pictures remarks rose from 77 to 88. v0.34's nine wrote from 2.40 to 4.50, 3.13 a picture, and on 26 identical pictures remarks were 96 in both. v0.35's nine wrote from 2.44 to 3.50, 2.88 a picture, and on 78 identical pictures remarks fell from 243 to 222. v0.36's nine wrote from 2.33 to 3.89, 3.10 a picture, and on 60 identical pictures remarks rose from 163 to 175. v0.37's nine wrote from 1.89 to 4.44, 2.82 a picture, and on 75 identical pictures remarks fell from 226 to 209. v0.38's nine wrote from 2.22 to 4.25, 3.38 a picture, and on 22 identical pictures remarks rose from 73 to 94. v0.39's twelve, eight pictures each, wrote from 2.62 to 4.00, 3.10 a picture, and on 7 pictures of the same events in both screens remarks fell from 28 to 25. v0.40's twelve wrote from 2.62 to 3.62, 3.04 a picture, and on 28 identical pictures remarks fell from 106 to 93. v0.41's twelve wrote from 2.25 to 3.88, 3.17 a picture, and on 43 identical pictures remarks rose from 151 to 156. v0.42's twelve wrote from 2.25 to 4.00, 3.05 a picture over all 93 screened.
- No reader says "teenager": he is read as a boy, a boy or young man, or a person, which the key mostly accepts. The v0.24 redraw moved him
  from a woman to a boy, and v0.26's cap worn forwards moved him no further toward the key's own word. It read once as "worn backward or sideways" in v0.27.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 93 pictures 1010 of 1020 scored items had full marks (999 of 1008 in v0.41, five of the nine others the clouds of one reader; 1011 of 1014 in v0.40, 1025 of 1030 in v0.39, 841 of 842 in v0.38, 870 of 876 in v0.37, 873 of 876 in v0.36, and 855 of 877 in v0.35, 17 of
  whose 22 others were the clouds of two readers who named nothing in the sky). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, a v0.24 scorer eleven, and all three scorers of v0.25 to v0.38 listed such calls, enough to move a template across the gate. A v0.29 scorer listed 18 items that hold full marks because the free description committed and only the unsure section hedged, and a v0.30 scorer gave nothing under full marks in 302 and listed 22 it thought a stricter scorer might halve. Two v0.31 scorers gave nothing under full marks, in 236 and 253 items, among them a bird "about to take it" credited as pecking. v0.32's three gave one, three and three items under full marks, in 244, 288 and 244, v0.33's four, one and three, in 301, 255 and 306, v0.34's one, none and ten, in 314, 282 and 289, where the second listed four inferences a stricter scorer might halve, v0.35's twelve, one and nine, in 304, 283 and 290, v0.36's none, two and one, in 304, 283 and 289, where the first listed eight hedged inferences it credited in full, v0.37's four, one and one, in 304, 283 and 289, where the second listed seven items it credited in full on a committed free description, and two birds seen standing, not pecking, and v0.38's none, none and one, in 298, 268 and 276, where the first listed eleven items it credited in full though the reader gave a second reading, and the second twelve more. Halved, those 23 would take six templates under the gate; 11 of them are on pictures identical to v0.37's, whose scorers had credited all 11 in full (`vision/flaws_v038.md`). v0.39's four (for 96 pictures) gave two, two, none and one, in 282, 246, 269 and 233, where two listed 11 items they credited in full on a committed free description; halved, those would take one template under the gate (`vision/flaws_v039.md`). v0.40's four, and a fifth for one picture read again, gave one, one, one, none and none, in 228, 270, 260, 241 and 15, and listed 21 items they credited in full on a committed free description; halved, those would take five templates under the gate (`vision/flaws_v040.md`). v0.41's four gave one, two, five and one, in 255, 263, 253 and 237, the five the clouds of one reader, and their notes mark 16 items they credited in full on a committed free description; halved, those would take two templates under the gate (`vision/flaws_v041.md`). v0.42's four gave none, three, five and one, in 225, 270, 237 and 250 (scorer a's old picture 10 left out, read again with one of 25 under), and their notes mark 10 items they credited in full on a committed free description; halved, those would take two more templates under the gate (`vision/flaws_v042.md`). A misread is a call too: the
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
- The planner's priors come from the v0.42 calibration, with f = 0 and a at its centre for every inference and contradiction, as in
  v0.20 to v0.41. With the cast redrawn, 34 fields moved by 0.002 or more, most of all `dog_begs`'s inference (s from -0.76 to -0.89) and `dog_reading`'s (two in v0.41, both `dog_begs`'s; 34 in v0.39, with the cast redrawn). The ladder's still rests on one sampled placement, since v0.29's lamp rule.
- Exact rebuilds hold within a release, on the pinned Pillow: the v0.42 placement rules (revision 40) tether the grazing goat, draw the songbirds and the duck at 45 as well
  as 90, keep anyone else with an ice cream away from the begging dog, and keep the square-wheeled bicycle or barrow off the stall and the bench. The stopped hose's crimp
  was read on the bench and is kept behind a switch at the old drawing (`KINK42` "O"). A v0.41 record rebuilds with the v0.41 package. Revisions 31 to 40 keep their rules in the templates'
  placement and binding, the planner's features and plans, the setting or `fits`, each behind its revision; revision 30's sky rule is still read at import (`RUNBOOK.md`).
- Every variant comes from the v0.42 cast (builder 0.42.0, `out042`), which redraws every person (shoes, and the trousers' waist), both dogs and the goat: only the cats', the songbirds' and the duck's renders carried over from `lib041`, and the seesaw's riders are in two pieces each, as before. The library keeps only the 408 variants the v0.42 set and probes use. The bench
  variants (`TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ`, `TPDB_BEARD`, `TPDB_BROW`, `TPDB_BLUSH`, `draw.WHEEL27`, `draw.SPLAT28`, `draw.SEESAW_IN28`, `draw.SWING35`, `library.SHADOW28`, `library.SHADOW29`, and `SLEEP29`, `TRIP29`, `TRIP_OBJ29`, `DUCK29`, `DOOR29`, `HOSE29`, `BULGE29`, `FISH29`, `LADDER_LAMP29`, `HOSE30`, `FISH30`, `TRIP_W30`, `TRIP_LANE30`, `CRUMB30`, `SEESAW31`, `RIDE31`, `CASTLE31`, `LIMB31`, `LOW32`, `LOW_IN32`, `LOW_RISE32`, `LOW_RISE_B32`, `STUCK32`, `HANDLE32`, `HOSE33`, `KICK33` and `BASKET38` in `templates.py`, `REEL30` and `REEL31` in `settings.py`, and `TPDB_VEST`, `TPDB_CONE`, `TPDB_BOX`, `TPDB_LOW`, `TPDB_SEAT34`, `TPDB_HAIR34`, `TPDB_MOUSTACHE36`, `TPDB_MOUSTACHE36_FLAT`, `TPDB_BUCKET36`, `TPDB_ISECT39`, `TPDB_SHOE39`, `TPDB_KNEE39`, `TPDB_MID39`, `TPDB_BELT39`, `TPDB_BEN39`, `TPDB_QUAD39`, `TPDB_ART39`, `TPDB_GOAT39`, `TPDB_REACH40`, `TPDB_HOSE40`, `TPDB_GRAZE40`, `TPDB_WALK40`, `TPDB_BEG41`, `TPDB_STALK41`, `TPDB_MEI41`, `TPDB_GOAT42`, `TPDB_DOG42`, `TPDB_BEG42`, `TPDB_CAT42`, `TPDB_MID42`, `TPDB_BELT42`, `TPDB_FOOT42` and `TPDB_MEI42` in the cast, and `YAW39`, `TUFT40`, `ICE40`, `BOX41`, `SEASON41`, `GOAT42`, `BIRD42`, `KINK42` and `BEG40` in `templates.py` and `HEAP39` and `HEAP40` in `draw.py`) stay in the code.
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
  v0.24 and v0.25, and with it from v0.26. The v0.42 isomorphs are new, four from the first search and the tier-4 one searched again after the screen's rule for the square wheel; an animal whose template its partner shares is drawn at the
  partner's angle (revision 37), a constraint `calibrate.py` has not yet tested for difficulty.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- A shadow from the figure's own footprint is smaller, and a body lying down has little of it showing. The sleeping dog now reads in full on its new pose and that shadow; a wider one did little on the bench, so whether the shadow cost it marks in v0.28 is still not shown.
- The trip reads in full on the long box, in eleven pictures in v0.30 and five each in v0.31 to v0.41. In v0.42 it read in two of three: the third reader, a reading dog beside the walker, saw the box and no trip. In v0.30, five of its readers also said the walker may step round it, which on the same five pictures went from four of five to one of five with nothing changed.
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
- Animals are drawn at 45 or 135 as well as 90 for eight templates (revision 37), and the songbirds and the duck at 45 for four more (revision 40); people are not. The dog walked on a lead is drawn at 90 only: at 45 its lead
  crossed its back at every spot tried, which revision 12 forbids. Every (template, angle) placed read at 1.00 in two or more pictures in v0.39, and at 0.94 or more in v0.40 to v0.42, the four bird templates at 45 too,
  and the scorers' oddities by angle were about the goat out of place, the begging dog's upright pose in profile and the stalking cat's legs at 45, not about an
  angle as such.
- The begging dog's forelegs are folded from v0.41, the elbows forward and the paws tipped down at the chest: held out level, they were "stiff rods" to the bench's readers
  (`vision/isolation_v041.md`). From v0.42 it sits on its haunches with a shorter trunk, and no screen reader saw it kneel; once it was "jumping up". Nobody else with an
  ice cream comes near it (revision 40), and in both v0.42 pictures with another eater in view the reader gave the one on the bench.
- The goat is tethered when it grazes, a rope from its collar to a peg (revision 40): out of place twice in v0.42, both softened ("a little unusual, but it is tethered
  and calm"), where it was seven times in v0.41. On the stopped hose it has its collar but no tether. The reading dog sits with its hind legs folded and its trunk
  shorter; its paper "stands upright on its own" in three descriptions (one in v0.41).
- A reader can describe the wrong picture. v0.40's reader 7 described picture 56 under picture 55's name, and wrote of picture 56 that it "couldn't find any difference between this
  picture and pic_55"; the files were distinct and right. Picture 55 was read again by a fresh reader and scored by a fresh scorer, and reader 7's description is kept aside
  (`vision/flaws_v040.md`). A scorer who finds a description that does not fit its key, as this one did, is the check.
- The washing's hanger is read hanging it out from the basket at her feet and the drops, not from the pose: on the bench, with neither, three readers of three could
  not tell up from down, and some design-test readers still said the pose alone could go either way (none of v0.38's three did, and of v0.39's five, one raised taking it down and settled it on the drips and the basket). All the washing drips, the jeans and the sleeve over the basket's rim too: with
  the shirt alone wet, a design test read the basket's clothes as dry and "about to get wet". The washing and a watering can placed 0 of 12 together, with the
  basket or without it.
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
