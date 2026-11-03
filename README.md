# TPDB v0.26: an older man's head that reads, a dog at the door with its eyes open, leaves to sweep, read a twenty-third time

v0.25 ended with three gate failures, `dog_wants_walk` at 0.83 ("with its eyes shut"), `sweep` at 0.88 ("no visible rubbish or leaf pile for the old man to sweep") and `ducks_bread` at 0.89, and a list of oddities led by the older man's face, "hard to read" in ten of his 21 pictures, a newspaper dog that "could be taken for a monkey, an otter, or a person in a costume", and a cap worn backwards that twice read as a head "the wrong way round".

v0.26 works through those, and it sorted all 428 of the v0.25 readers' remarks by what they were about, which added the feeder's bag and the sandcastle. Each went to the isolation bench first, drawn two or more ways and read blind on its own. All of them were then read blind in whole test scenes among other events, the set was regenerated, and it was screened a twenty-third time. One drawing chosen on the bench, the broom, did not survive the screen.

The twenty-third screen read all 67 pictures, the set's 21 and 46 probes: 743 of 752 scored items had full marks, and one, in a probe, was misread. The gate went down: 59 of the 64 templates pass, against 61, with five failures against three. Two of v0.25's three failures now read in full, the dog at the door and the ducks' bread. The third got worse, and that is this release's own doing: `sweep` gained a heap of leaves and a fan of bristles, and one of its three readers saw "a long yellow-headed rake", at 0.67. It is first on the v0.27 list. The other four failures are on drawings this release did not change, each on one or two half marks and each in full in v0.25; the v0.9 retest put the gate's reader variance at about five templates between screens. The named complaints did fall. The older man's face drew one remark in his 12 pictures, against ten of his 21, no reader had the teenager's head on the wrong way round, and the newspaper dog was only ever a dog. Readers' remarks per picture fell for the first time since v0.23, from 5.93 to 5.27. That row is recounted here, because the counter had been taking bullets that say nothing is wrong for remarks: the rise published with v0.25 as 11% was 5%.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.25 readers saw | v0.26 |
|---|---|
| The older man's head: "the older man's face is hard to read", a grey patch (ten of his 21 pictures) | His cap kept, with a shorter peak tipped up and short white hair running round under it (builder 0.26.0). Bench: "an older man with grey hair and a blue-grey flat cap". One remark on his face in his 12 screened pictures |
| The newspaper dog's head: "a monkey, an otter, or a person in a costume", "a person in a spacesuit or a small robot" | Its head up and turned a little to the viewer, its tail up behind it. "A brown-and-tan cartoon dog", and no other animal in its five screened pictures |
| The teenager's cap worn backwards, twice a head "the wrong way round" | Worn forwards. "A cartoon boy or young man", and no head on the wrong way round in his 20 pictures. Two readers still took the cap for sideways or backwards |
| The dog at the door "with its eyes shut", its wish for a walk never stated (0.83) | The neutral face only, as the happy one closes its eyes. "As if it is asking to go for a walk": 1.00 |
| `sweep` with nothing to sweep: "no visible rubbish or leaf pile for the old man to sweep" (0.88) | A heap of leaves at the broom, which worked: "sweeping up a pile of autumn leaves". And a fan of seven bristles for its head, as the old wedge read as "a dustpan or scraper" on the bench, which did not: "a long yellow-headed rake", this screen's one misread (0.67). First on the v0.27 list |
| The feeder's "a paper bag, a cup or a carton" | A brown paper bag: "a brown paper bag" or "a paper bag" for all six feeders in five pictures. The crumbs at the pond are bread-coloured |
| The sandcastle: "very straight, boxy edges ... a cardboard or wooden model" | Heaped sand with bucket-shaped towers: "a sandcastle with three towers and a small red flag". The child and the castle stay back from the sandbox's front rim |
| A lamp post merging with a figure | A placement rule keeps a person's box off the post. No reader had a figure growing out of it or about to walk into it |
| Two probes nearly the same picture, both `seesaw` alone | A template's second solo probe now gets a companion event |

Left as they were, as notes for the pilot: figures overlapping the pond, goats in a garden or park, a wind that reaches only some things, swing ropes behind a rider's head. Tried and left: fuller bodies, as a figure 22% deeper with limbs 12% thicker did not move the readers' words, and the bearded man's bowed head over the birds, which a rule from revision 5 needs.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v026.md`, two rounds, 36 cut-outs, 15 readers). The bench casts were built from the same cast library with the variants switched on (`TPDB_OLD`, `TPDB_TEEN`, `TPDB_READDOG`, `TPDB_RDTAIL`, `TPDB_FEED`, `TPDB_BROOM`, `TPDB_BODY`); the release cast builds with the chosen ones. For the older man the eye and the readers disagreed: no cap and short white hair looked best, but read as "a smooth grey cap or hat", and "the face is hard to read", while the cap kept, its peak shorter, was "an older man with grey hair and a blue-grey flat cap". The newspaper dog with its head up in profile could still be "a weasel or an otter"; turned a little to the viewer it was only a dog, and a flat shape at its rear went when the tail went up. A red beanie named the teenager less firmly than the cap worn forwards. A heap of dust and grit was "a small rock or mound", where leaves were "sweeping up leaves". A slice of bread for the feeder was "a couple of sheets of paper". The broom's yellow wedge was "a dustpan or scraper", so round 2 tried the fan, and one reader there said "broom or rake", which the screen bore out.

## Design tests

After the bench, the new drawings were read blind in whole test scenes among other events (`vision/design_tests_v026.md`, six pictures, three readers). The older man was "old man ... grey hair, blue-grey flat cap" or an "older man with grey hair in a blue-grey cap", with a remark on his face only on the seesaw pose. The dog at the door was "looking at the viewer as if waiting for a walk", with open eyes. Both newspaper dogs read as dogs reading, and the white one, "an odd white figure ... ghostly" in the v0.25 design tests, was now a "white dog with brown patches". The swept leaves read in all three pictures, though twice a reader asked where they came from: "the leaves do not obviously come from anywhere". No reader had a figure growing out of the lamp post or about to walk into it. No new rule came out of them, so there was no second round.

## Placement revision 24

Every record stores the placement revision it was made with. v0.26 pictures use revision 24, which adds to those of revisions 1 to 23 the leaf heap at a sweeper's broom, the neutral face for the dog at the door, the heaped sandcastle with the sandbox's child and castle back from its front rim, the newspaper's pale photo (its photo block had kept a dark outline), the bread-coloured crumbs, and a person's box kept off the lamp post. The older man, the teenager, the newspaper dog's head and tail, the feeder's bag and the broom are in the cast (builder 0.26.0).

Building and inspecting the set and the probes found nothing more to fix, but placement took more searching. The tier-4 garden and street placed again on their v0.25 seeds. The tier-4 park took 16 failed seeds, and the tier-4 playground 89 across two searches side by side, on the last seed of the second list (3 in v0.25). The tier-3 playground placed under template-variety steering, after seven failed seeds, where v0.24's and v0.25's needed the unsteered search. The tier-4 isomorph took 676 failed attempts (13 tries in v0.25). Why the playground got so much harder was not traced, and `vision/flaws_v026.md` says what was ruled out. The set's isomorphs are two at tier 2, two at tier 3 and one at tier 4. All 67 records rebuild identical to the pixel.

The planner's difficulty priors are the calibration measured on the v0.26 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.25. The ducks' bread's cue salience moved by +0.025 and the newspaper dog's by +0.024, with their redraws; the bucket hat's by -0.010 and the trip's by -0.005, with no drawing of theirs changed; every other template's by less than 0.002.

## The twenty-third blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 46 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.25.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) | v0.25 (21 pictures) | v0.26 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 | 0.98 | 0.95 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 | 0 of 286 |
| Oddities per picture, as logged by the scorers | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 | 2.6 | 2.6 |
| Readers' remarks per picture (recounted in v0.26) | 8.8 | 5.4 | 6.4 | 4.8 | 4.7 | 4.8 | 4.9 | 4.4 | 4.3 | 4.4 | 4.4 | 4.4 | 3.9 | 3.9 | 4.4 | 4.0 | 4.0 | 3.9 | 4.2 | 3.9 | 5.6 | 5.9 | 5.3 |

Across all 67 pictures 743 of 752 scored items had full marks. Eight had half marks, one was misread and none was missed. The misread is the broom: an older man raking leaves "with a long yellow-headed rake" (picture 37), where the two other readers of `sweep` said "sweeping up a pile of autumn leaves" and "sweeping a pile of red, orange and brown leaves with a long broom". Below full marks: a bearded man's ice cream, twice, "looking at or eating it" and "could be eating the ice cream or just holding it up"; a walker's obstacle, twice, as it "lies slightly off his line"; "binoculars or a camera"; a sprinkler's box as "a wooden crate standing in a puddle", with its soaking only one of two readings; and a person "sitting in mid-air or on the edge of the path". The set's headline falls a little with those: all items 0.988 (0.995), with inferences at 0.953 and the first contradiction below 1.00 since v0.21, each on a few half marks.

**The remarks row is recounted.** Sorting v0.25's remarks for this release's list showed that `summarize_screen.py` had counted bullets that say nothing is wrong (25 of v0.25's 428, 2 of v0.24's 408). The counter is fixed and the row recounted for every screen that has one, so its figures differ from those published before: v0.21 3.92 (4.35), v0.22 4.17 (4.49), v0.23 3.86 (4.32), v0.24 5.64 (5.67), v0.25 5.93 (6.29). v0.25's rise was 5%, not the 11% its README gave, and the v0.24 control's reader effect 18%, not 15%. On the corrected row remarks fell by 11% here. The remarks were not sorted by kind this time, so how much of the fall is the drawings and how much the readers is not separated. What they noticed most: a seesaw's plank through its sitter ("sitting right into the plank"), a hose "like a stiff loop standing in the air", water "like a beaded curtain", and faces hidden by a tilted head.

The templates v0.26 changed, and the ones that fail the gate (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.25 | v0.26 | v0.26 meaning items |
|---|---|---|---|
| `sweep` | 0.88 (4 items) | 0.67 (3 items) | — |
| `dog_wants_walk` | 0.83 (6 items) | 1.00 (6 items) | 1.00 (3) |
| `dog_reading` | 1.00 (21 items) | 1.00 (15 items) | 1.00 (10) |
| `feed_birds` | 1.00 (3 items) | 1.00 (3 items) | — |
| `ducks_bread` | 0.89 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `sandbox` | 1.00 (3 items) | 1.00 (3 items) | — |
| `ice_cream` | 1.00 (4 items) | 0.83 (6 items) | — |
| `photo` | 1.00 (3 items) | 0.83 (3 items) | — |
| `about_to_trip` | 1.00 (12 items) | 0.89 (9 items) | 0.67 (3) |
| `sprinkler_package` | 1.00 (9 items) | 0.89 (9 items) | 0.83 (3) |

`dog_wants_walk` and `dog_reading` read in full, and so did the feeders' bag: "a brown paper bag" or "a paper bag" for all six feeders in five pictures, with no cup or carton. `sandbox` read in full with no box or model. `ducks_bread` read in full, its v0.25 half marks probably scoring variance. `sweep` is the one this release made worse. The last four rows were not changed and each read in full in v0.25.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 | 61 | 59 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 | 3 | 5 |

Every template was screened in at least three pictures (56 in three, 3 in four, 2 in five, 3 in six), and 59 of 64 pass, down from 61. One failure, `sweep`, is a misread on what this release redrew. The other four are on unchanged drawings and each read in full in v0.25, and the v0.9 retest put the gate's reader variance at about five templates between screens, so those four do not by themselves show that anything got worse. The gate is a filter, and the pilot with people is the test of difficulty.

Templates that did not pass (`vision/flaws_v026.md` gives what the readers saw and the next fix):

| Template | v0.26 mean | Pictures | Misreads |
|---|---|---|---|
| `sweep` | 0.67 (3 items) | 3 | 1 |
| `ice_cream` | 0.83 (6 items) | 6 | 0 |
| `photo` | 0.83 (3 items) | 3 | 0 |
| `about_to_trip` | 0.89 (9 items) | 3 | 0 |
| `sprinkler_package` | 0.89 (9 items) | 3 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.777 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.773 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s1031 | 4 | 0 (0) | 3 | 0.777 | — | 12 | 0.043 | birds flying, jump, run |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.771 | — | 14 | 0.033 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.709 | 0.393 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_park_s022 | 8 | 1 (0) | 4 | 0.711 | 0.411 | 21 | 0.031 | kite in tree, push stroller, carry box, dig |
| T2_park_s12118_iso (isomorph of T2_playground_s3042) | 8 | 1 (0) | 3 | 0.719 | 0.397 | 21 | 0.028 | dog begs, feed birds, balloon |
| T2_street_s032 | 8 | 1 (0) | 3 | 0.711 | 0.399 | 19 | 0.053 | ice cream drop, walk dog, wave |
| T2_street_s14109_iso (isomorph of T2_park_s022) | 8 | 1 (0) | 4 | 0.711 | 0.430 | 16 | 0.051 | about to trip, drink bench, carry bag, photo |
| T2_playground_s3042 | 8 | 1 (0) | 3 | 0.711 | 0.409 | 17 | 0.033 | cat stalks bird, slide, fly kite |
| T3_garden_s7013 | 12 | 2 (1) | 6 | 0.646 | 0.283 | 23 | 0.038 | paint tracks, sitting on air, water flowers, bird perched, dog sleeping, play catch |
| T3_garden_s10102_iso (isomorph of T3_street_s1133) | 12 | 3 (0) | 5 | 0.656 | 0.346 | 20 | 0.040 | ball in tree, cat stalks bird, about to trip, carry box, birds flying |
| T3_park_s1023 | 12 | 2 (1) | 5 | 0.660 | 0.376 | 21 | 0.030 | lost balloon, dog reading, read bench, carry bag, ducks swimming |
| T3_street_s1133 | 12 | 3 (0) | 5 | 0.656 | 0.341 | 20 | 0.052 | about to trip, dog begs, ball in tree, ice cream, balloon |
| T3_street_s9104_iso (isomorph of T3_park_s1023) | 12 | 2 (1) | 5 | 0.658 | 0.367 | 21 | 0.051 | ball in tree, dog reading, balloon, bird perched, wave |
| T3_playground_s11743 | 12 | 2 (1) | 6 | 0.628 | 0.286 | 21 | 0.038 | seesaw heavy, square wheel, slide, wave, dog sleeping, bird perched |
| T4_garden_s327962 | 18 | 5 (2) | 8 | 0.570 | 0.239 | 29 | 0.044 | paint tracks, lost balloon, cat stalks bird, dog reading, fish in tree, read bench, birds flying, cat sleeping |
| T4_park_s437869 | 18 | 5 (1) | 9 | 0.541 | 0.206 | 27 | 0.033 | bird steals, sprinkler package, ducks bread, ball in tree, sitting on air, dog sleeping, goat grazing, carry bag, ice cream |
| T4_park_s66111_iso (isomorph of T4_street_s820995) | 18 | 5 (2) | 9 | 0.549 | 0.200 | 32 | 0.035 | ice cream drop, windy hat, bird steals, pan watering, dog reading, goat grazing, birds flying, cat sleeping, ducks swimming |
| T4_street_s820995 | 18 | 5 (2) | 9 | 0.566 | 0.202 | 30 | 0.057 | ice cream drop, windy hat, bird steals, bucket hat, dog reading, jump, sweep, water flowers, birds flying |
| T4_playground_s1472617 | 18 | 5 (2) | 9 | 0.548 | 0.204 | 26 | 0.042 | ball in tree, bird steals, ice cream drop, bucket hat, square wheel, photo, cat sleeping, sandbox, birds flying |

Isomorph pairs differ by at most 0.017 in content and 0.019 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 26,666 | 27 | 11,977 | 10^12.7 |
| garden | 3 | 2,497,856 | 296 | 338,691 | 10^18.4 |
| garden | 4 | 78,307,591 | 565 | 6,485,763 | 10^23.4 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 46,656 | 24 | 20,579 | 10^11.6 |
| park | 3 | 5,825,387 | 236 | 1,027,898 | 10^17.4 |
| park | 4 | 335,129,874 | 376 | 44,950,328 | 10^23.1 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,433 | 24 | 2,952 | 10^11.8 |
| street | 3 | 440,799 | 220 | 70,459 | 10^17.2 |
| street | 4 | 7,157,106 | 330 | 947,071 | 10^22.5 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.5 |
| playground | 3 | 749,671 | 183 | 113,624 | 10^17.8 |
| playground | 4 | 10,690,061 | 232 | 1,352,842 | 10^21.8 |

In all 440,902,571 structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.

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
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts) |
| `assets/blender_run.py` | Lets the `bpy` scripts run with plain `python`, inside an installed Blender where the `bpy` module is missing |
| `assets/validate_assets.py` | Checks for every rendered variant |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.26 redraws the older man's and the teenager's caps, the newspaper dog's head and tail, the feeder's bag and the broom, and keeps the bench variants behind `TPDB_OLD`, `TPDB_TEEN`, `TPDB_READDOG`, `TPDB_RDTAIL`, `TPDB_FEED`, `TPDB_BROOM` and `TPDB_BODY`, with `TPDB_BAG`, `TPDB_ROLLER` and `TPDB_SLIDE` from earlier releases |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out026/` | The 18 `.blend` families (builder 0.26.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib026/` | Every variant the generated scenes and probes use, carried over from `lib025` where the cast did not change or rendered from `out026` |
| `assets/cast/gallery026/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (170, all pass the validator) |
| `scenegen/` | The generator (0.26.0, placement revision 24); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, and the swept heap's two drawings (`SWEEP26`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.26 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v026.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v026.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v026.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all twenty-three screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out026                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out026 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s1023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_OLD=A> python vision/isolation_bench.py tpdb_work/bench oldA_1 oldA_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v026   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v026 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery026 --old-gallery <v0.25 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.26 --single   # the release as one zip, tpdb_v0.26.zip
```

The release is one zip, `tpdb_v0.26.zip`, about 168 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.25 record rebuilds with the v0.25 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- Five templates fall under the legibility gate after the v0.26 screen: `sweep` (0.67, with one misread, on this release's own redraw), and
  `ice_cream` (0.83), `photo` (0.83), `about_to_trip` (0.89) and `sprinkler_package` (0.89), none of which it changed. 59 of 64 pass.
  `vision/flaws_v026.md` lists them and the oddities for v0.27.
- The oddities come in two rows. Readers' remarks per picture are counted directly from their descriptions and compare across
  screens, with the caveat that current readers write about 18% more than the v0.23 readers on the same pictures (`vision/v024/control/`,
  one reader and eight pictures). The row was recounted in v0.26, as the counter had taken bullets saying nothing is wrong for remarks, so its
  figures differ from those published up to v0.25. The scorers' logged oddities do not compare: v0.23's logged 25% of the remarks, v0.24's 83%, and
  from v0.25 the prompt caps them at three per picture. Earlier screens did not record which model read them; v0.24's to v0.26's ran on Claude Opus 5.5.
- No reader says "teenager": he is read as a boy, a boy or young man, or a person, which the key mostly accepts. The v0.24 redraw moved him
  from a woman to a boy, and v0.26's cap worn forwards moved him no further toward the key's own word.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 67 pictures 743 of 752 scored items had full marks (779 of 785 in v0.25). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, a v0.24 scorer eleven, and all three scorers of v0.25 and of v0.26 listed such calls, enough to move a template across the gate. A misread is a call too: the
  rake in picture 37 could have been marked as sweeping half right.
- Tier-4 pictures are the hardest to place, and revisions 14 to 24 make them harder (walkers' and runners' lanes, pointing
  lines, feet off benches and off other events' things, the photographer's line of sight, the waver's clear hand, body gaps, the gap
  from thin parts, heads clear of figures up to 80 px apart in depth, the ground clear past a reading walker's obstacle, jumpers in the
  front half, an obstacle a full step ahead, runners clear of other movers, ducks off a float, sleepers clear of walkers' feet, nobody in
  the strip before the horizon, a person's box off the lamp post). The tier-4 garden and street came again on their v0.25 seeds; the park took 16
  failed seeds, and the playground 89 across two searches, on the last seed of the second list, where v0.25's took 3. Why the playground got so much
  harder was not traced. Their records rebuild them exactly.
- The square-wheeled bicycle still stands on its own: four stands have been tried on the bench, and each
  read as something else (pedals, legs) or not at all.
- The low kick's direction is ambiguous when the kicker's hair hides the face; the teenager kicks first,
  and the kick read in full in all its screened pictures. His cap now points the way he faces, but two readers still took it for sideways or backwards.
- The stuck girl on the seesaw always calls out, but no reader mentioned it: the tilt, the man's weight and
  the motion lines at her feet carry the reading.
- The body check (`assets/cast/gapcheck.py`) finds parts that come apart, not parts that pass through one
  another: a hand inside a hip or a lobe of skirt inside the bell is allowed, and only the outline drawn
  in the render shows whether the join looks right.
- The wind reaches the hat, the washing, an empty swing, the tree and the sky, but not hair or clothes, nor the
  bushes and flowers (three v0.19 probe readers noticed): the cast is posed and rendered in 3D, and a blowing
  fringe or skirt would be a new rig.
- The isolation bench reads one template cut out of its picture. A visual that reads alone can still be
  misread among other events, so the bench comes before the test scenes and the screen, never instead of them.
- The planner's priors come from the v0.26 calibration, with f = 0 and a at its centre for every inference and contradiction, as in
  v0.20 to v0.25: the ducks' bread's cue salience moved by +0.025, the newspaper dog's by +0.024, the bucket hat's by -0.010, the trip's by -0.005,
  and every other template's by less than 0.002.
- Exact rebuilds hold within a release, on the pinned Pillow: the v0.26 cast (builder 0.26.0) and placement rules (revision 24) change how
  the older man, the teenager, the newspaper dog, the feeder, the broom and the sandcastle look, so a v0.25 record rebuilds with the v0.25 package.
- Every variant comes from the v0.26 cast (builder 0.26.0, `out026`): the variants of the families and poses v0.26 did not change were
  carried over from `lib025`, the rest rendered anew. Some carried variants date from Linux renders, which differ from an installed Blender's
  only in sub-pixel anti-aliasing on the outlines. The library keeps only the 393 variants the v0.26 set and probes use. The bench
  variants (`TPDB_OLD`, `TPDB_TEEN`, `TPDB_READDOG`, `TPDB_RDTAIL`, `TPDB_FEED`, `TPDB_BROOM`, `TPDB_BODY`, `draw.SWEEP26`) stay in the code.
- The figures are narrow from the side, and nearly every v0.26 bench cut-out said so. A body 22% deeper with limbs 12% thicker did not move the
  readers' words, so it was left (`TPDB_BODY`); a real change to their proportions is a larger job than one bench round.
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
  v0.24 and v0.25, and with it in v0.26 after seven failed seeds. The v0.26 isomorphs are two at tier 2, two at tier 3 and one at tier 4; the tier-4 one
  took 676 failed attempts.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
