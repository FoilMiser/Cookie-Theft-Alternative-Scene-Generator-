# TPDB v0.25: a shopping bag that looks like one, a roller that touches the fence, a dog with its own paws, read a twenty-second time

v0.24 ended with its screen's one gate failure, the older man's shopping bag at 0.75 ("carrying something yellow", "very long and thin ... could be a tag, folded paper"), and a list of oddities led by a wheelbarrow's oversized shadow, a bird as big as the sandwich it stole ("a blue kettle or jug"), a newspaper dog's "white gloved hands" and a paint roller that "hardly seems to touch the fence".

v0.25 works through those. Each went to the isolation bench first, drawn two or more ways and read blind on its own, and most turned out to have a plain cause: the bag and the roller both showed their narrow edge to a viewer looking at a figure in profile. All of them were then read blind in whole test scenes among other events, the set was regenerated, and it was screened a twenty-second time. Oddities now come in two rows, as v0.24 showed that scorers differ in how much they log.

The twenty-second screen read all 68 pictures, the set's 21 and 47 probes: 779 of 785 scored items had full marks, and none was misread. The bag, the gate's one failure in v0.24, rose from 0.75 to 1.00, "a yellow shopping bag". No reader said kettle, gloves or a shadow too large. But 61 of the 64 templates pass the gate, down from 63: three that this release did not change fall short, each on one or two half marks and each in full in v0.24. The v0.9 retest put the gate's reader variance at about five templates between screens, so this does not by itself show that anything got worse, and `vision/flaws_v025.md` lists what to look at for v0.26 all the same. Above all, the older man's face, the most repeated specific remark.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.24 readers saw | v0.25 |
|---|---|
| The older man's shopping bag: "carrying something yellow", "very long and thin ... could be a tag, folded paper" (0.75, the gate's one failure) | Redrawn on the bench (builder 0.25.0): its broad face along the walker's line, so a profile shows it, as tall as it is wide, with dark handles rising to the hand. Bench readers: "a plain yellow shopping bag with dark handles" |
| A paint roller that "hardly seems to touch the fence", "a small pale oval" | Redrawn on the bench: upright, its side to the viewer, a T on the end of the pole. Its axis had run along the line of sight, so only its round end showed. "A long-handled paint roller up against the fence" |
| The wheelbarrow's shadow: "a large dark oval extending well beyond it" (four probes) | 130 px wide, was 210: "a soft dark shadow beneath it" |
| The bird at the sandwich "about as big as the sandwich", "a blue kettle or jug" | 0.8 of its size, and the sandwich 0.72 of its drawn size (was 0.8). At 0.68 the bird was "a glove or a bag" |
| The newspaper dog's "white gloved hands" | The paper drawn behind the dog with no paws painted over it, so its own paws rest on it, at different heights so both show. Ovals in its own colour read as "stuck onto" the paper |

Left as they were, as notes for the pilot: figures overlapping the pond, goats in a garden or park, the older ones (wind under a clear sky, a stall with nobody at it, sweeping a path with nothing on it). Feet at the edge of a path were looked at and left: only about three of the remarks that seemed to be about them really were.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v025.md`, two rounds, 20 cut-outs, seven readers). The bench casts were built from the same cast library with the variants switched on (`TPDB_BAG`, `TPDB_ROLLER`); the release cast builds with the chosen ones. The bag as tall as it is wide was "a plain yellow shopping bag with dark handles" twice, where a wider one also drew "a briefcase" and "more like a box". The upright roller was "a long-handled paint roller" twice, where a fatter one was once "or wide brush". The barrow's shadow at 130 px lay "beneath it", and at 160 the barrow "looks slightly lifted". The bird at 0.8 still pecked, and at 0.68 it was "a glove or a bag". The dog's paws took a second round: ovals in its own colour, with or without toes, stayed "stuck onto" the paper, so the ovals went, and with its own paws on the paper it "holds an open newspaper ... as if reading it". The sandwich's smaller size and the paws at different heights were first read in whole scenes.

## Design tests

After the bench, the new drawings were read blind in whole test scenes among other events (`vision/design_tests_v025.md`, six pictures, three readers). The bag was "a yellow shopping bag" in all three of its pictures with no hedge, on the older man too. The bird was at the food in all three, "about to eat or take her lunch", with no remark on its size. The roller was "a long-handled paint roller" or "a roller or brush" against the fence, and no reader remarked on the barrow's shadow. The tan newspaper dog read in full with its own paws on the paper. The white dog, small on pale paving in the busiest picture, was "an odd white figure, like a white dog or a person": one reader, so no rule, left for the screen to count. No new rule came out of them, so there was no second round.

## Placement revision 23

Every record stores the placement revision it was made with. v0.25 pictures use revision 23, which adds to those of revisions 1 to 22 the bird's and the sandwich's sizes and the newspaper drawn behind the dog. The bag, the roller and the dog's paws are in the cast (builder 0.25.0), and the barrow's shadow in `scenegen/draw.py`.

Building and inspecting the set and the probes found nothing more to fix. The tier-4 garden and park placed again on their v0.24 seeds with the same events. The tier-4 street took three searches side by side and 13 failed seeds, the tier-4 playground two searches and 3 failed seeds, and the tier-3 playground again the unsteered search after 13 failed seeds under template-variety steering. The tier-4 isomorph came within 13 tries (about 230 in v0.24). The set's isomorphs are two at tier 2, two at tier 3 and one at tier 4. All 68 records rebuild identical to the pixel.

The planner's difficulty priors are the calibration measured on the v0.25 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.24. The bird at the sandwich's cue salience moved by -0.32 with its smaller size, and the newspaper dog's by +0.08 with the paper behind it; every other template's by at most 0.001.

## The twenty-second blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 47 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.24.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) | v0.25 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 | 0.98 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 |
| Oddities per picture, as logged by the scorers | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 | 2.6 |
| Readers' remarks per picture | 8.8 | 5.5 | 6.4 | 5.0 | 4.8 | 5.0 | 5.1 | 4.6 | 4.7 | 4.8 | 4.6 | 4.7 | 4.3 | 4.2 | 4.8 | 4.3 | 4.3 | 4.3 | 4.5 | 4.3 | 5.7 | 6.3 |

Across all 68 pictures 779 of 785 scored items had full marks, and none was misread. Below full marks: a dog by the door "with its eyes shut", its wish for a walk never stated; the clouds, not mentioned in one description; a duck "swimming towards the food", twice, its purpose only implied; an older man "as if sweeping" who "could be ... pausing to watch"; and a floating box called cardboard.

**Oddities now come in two rows.** Scorers differ in how much they log (83% of the readers' remarks in v0.24, 22% in v0.23), so `summarize_screen.py` now counts the remarks in the readers' "unsure" sections directly, for every screen, and the scorer prompt caps its list at three per picture. Remarks rose again, to 6.29 per picture (5.67), so this release did not bring the total down: what it removed were named complaints. Current readers write about 15% more than the v0.23 readers on the same pictures (the v0.24 control), and how much of the rest is readers, pictures or their mix is not separated. What they noticed: the older man's face, in ten of his 21 pictures ("hard to read", "an odd grey patch"); the newspaper dog's head ("a monkey, an otter", "a spacesuit or a small robot"); a backwards cap as a head "the wrong way round"; and figures overlapping the pond.

The templates v0.25 changed, and the three that fail the gate (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.24 | v0.25 | v0.25 meaning items |
|---|---|---|---|
| `carry_bag` | 0.75 (4 items) | 1.00 (3 items) | — |
| `paint_fence` | 1.00 (6 items) | 1.00 (6 items) | — |
| `paint_tracks` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `bird_steals` | 1.00 (15 items) | 1.00 (12 items) | 1.00 (4) |
| `dog_reading` | 1.00 (15 items) | 1.00 (21 items) | 1.00 (14) |
| `dog_wants_walk` | 1.00 (6 items) | 0.83 (6 items) | 0.67 (3) |
| `sweep` | 1.00 (5 items) | 0.88 (4 items) | — |
| `ducks_bread` | 1.00 (9 items) | 0.89 (9 items) | 0.67 (3) |

The bag read in full in all three of its pictures, and the bird, the roller and the newspaper dog in all of theirs. The three that fail the gate are in the table too, as none of them was changed: each read in full in v0.24.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 | 61 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 | 3 |

Every template was screened in at least three pictures (51 in three, 7 in four, 1 in five, 3 in six, 2 in seven), and 61 of 64 pass, down from 63. All three failures are on templates this release did not change, and read in full in v0.24. The v0.9 retest put the gate's reader variance at about five templates between screens, so the gate is a filter and the pilot with people is the test of difficulty.

Templates that did not pass (`vision/flaws_v025.md` gives what the readers saw and the next fix):

| Template | v0.25 mean | Pictures | Misreads |
|---|---|---|---|
| `dog_wants_walk` | 0.83 (6 items) | 3 | 0 |
| `sweep` | 0.88 (4 items) | 4 | 0 |
| `ducks_bread` | 0.89 (9 items) | 3 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.777 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.773 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s031 | 4 | 0 (0) | 2 | 0.778 | — | 15 | 0.044 | birds flying, balloon |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.770 | — | 14 | 0.032 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.711 | 0.393 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_park_s4022 | 8 | 1 (0) | 3 | 0.710 | 0.420 | 20 | 0.024 | kite in tree, photo, walk dog |
| T2_park_s12118_iso (isomorph of T2_playground_s3042) | 8 | 1 (0) | 3 | 0.719 | 0.397 | 21 | 0.028 | dog begs, feed birds, balloon |
| T2_street_s032 | 8 | 1 (0) | 3 | 0.710 | 0.399 | 16 | 0.049 | ice cream drop, carry box, wave |
| T2_street_s9109_iso (isomorph of T2_park_s4022) | 8 | 1 (0) | 3 | 0.707 | 0.418 | 16 | 0.046 | lost balloon, feed birds, run |
| T2_playground_s3042 | 8 | 1 (0) | 3 | 0.708 | 0.409 | 17 | 0.032 | cat stalks bird, push stroller, slide |
| T3_garden_s7013 | 12 | 2 (1) | 6 | 0.646 | 0.283 | 23 | 0.038 | paint tracks, sitting on air, water flowers, bird perched, dog sleeping, play catch |
| T3_garden_s10102_iso (isomorph of T3_street_s1133) | 12 | 3 (0) | 5 | 0.665 | 0.346 | 20 | 0.040 | ball in tree, cat stalks bird, about to trip, carry box, birds flying |
| T3_park_s1023 | 12 | 2 (1) | 5 | 0.662 | 0.378 | 22 | 0.030 | lost balloon, dog reading, read bench, carry bag, ducks swimming |
| T3_street_s1133 | 12 | 3 (0) | 5 | 0.665 | 0.344 | 20 | 0.053 | about to trip, dog begs, ball in tree, ice cream, jump |
| T3_street_s9104_iso (isomorph of T3_park_s1023) | 12 | 2 (1) | 5 | 0.665 | 0.364 | 21 | 0.051 | ball in tree, dog reading, balloon, bird perched, wave |
| T3_playground_s043 | 12 | 3 (0) | 6 | 0.621 | 0.334 | 20 | 0.035 | about to trip, ice cream drop, lost balloon, bird perched, drink bench, birds flying |
| T4_garden_s327962 | 18 | 5 (2) | 8 | 0.570 | 0.238 | 29 | 0.044 | paint tracks, lost balloon, cat stalks bird, dog reading, fish in tree, read bench, birds flying, cat sleeping |
| T4_park_s242971 | 18 | 5 (1) | 8 | 0.582 | 0.240 | 26 | 0.034 | ball in tree, lost balloon, bird steals, ducks bread, dog reading, ice cream, carry bag, cat sleeping |
| T4_street_s820995 | 18 | 5 (2) | 9 | 0.572 | 0.204 | 27 | 0.056 | ice cream drop, windy hat, bird steals, bucket hat, dog reading, jump, sweep, water flowers, birds flying |
| T4_street_s16111_iso (isomorph of T4_playground_s1224004) | 18 | 5 (2) | 9 | 0.572 | 0.231 | 27 | 0.057 | lost balloon, ball in tree, bird steals, square wheel, dog reading, birds flying, ice cream, carry box, water flowers |
| T4_playground_s1224004 | 18 | 5 (2) | 9 | 0.561 | 0.235 | 27 | 0.045 | ball in tree, about to trip, bird steals, square wheel, dog reading, balloon, birds flying, run, dog playing |

Isomorph pairs differ by at most 0.011 in content and 0.014 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 26,666 | 27 | 11,977 | 10^12.7 |
| garden | 3 | 2,497,856 | 296 | 338,691 | 10^18.4 |
| garden | 4 | 78,307,591 | 565 | 6,485,763 | 10^23.3 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 46,656 | 24 | 20,579 | 10^11.6 |
| park | 3 | 5,825,387 | 236 | 1,027,898 | 10^17.4 |
| park | 4 | 335,129,874 | 376 | 44,950,328 | 10^23.1 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,433 | 24 | 2,952 | 10^11.8 |
| street | 3 | 440,799 | 220 | 70,459 | 10^17.2 |
| street | 4 | 7,157,106 | 330 | 947,071 | 10^22.6 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.5 |
| playground | 3 | 749,671 | 183 | 113,624 | 10^17.8 |
| playground | 4 | 10,690,061 | 232 | 1,352,842 | 10^22.0 |

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.25 redraws the bag and the roller, and keeps the bench variants behind `TPDB_BAG` and `TPDB_ROLLER`, with `TPDB_TEEN` and `TPDB_SLIDE` from v0.24 |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out025/` | The 18 `.blend` families (builder 0.25.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib025/` | Every variant the generated scenes and probes use, carried over from `lib024` where the cast did not change or rendered from `out025` |
| `assets/cast/gallery025/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (170, all pass the validator) |
| `scenegen/` | The generator (0.25.0, placement revision 23); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`) and the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`; `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.25 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v025.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v025.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v025.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all twenty-two screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out025                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out025 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s1023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_BAG=A> python vision/isolation_bench.py tpdb_work/bench bagA_1 bagA_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v025   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v025 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery025 --old-gallery <v0.24 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.25 --single   # the release as one zip, tpdb_v0.25.zip
```

The release is one zip, `tpdb_v0.25.zip`, about 163 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.24 record rebuilds with the v0.24 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- Three templates fall under the legibility gate after the v0.25 screen, none of them changed by this release: `dog_wants_walk`
  (0.83), `sweep` (0.88) and `ducks_bread` (0.89). 61 of 64 pass. `vision/flaws_v025.md` lists them and the oddities for v0.26.
- The oddities come in two rows. Readers' remarks per picture are counted directly from their descriptions and compare across
  screens, with the caveat that current readers write about 15% more than the v0.23 readers on the same pictures (`vision/v024/control/`,
  one reader and eight pictures). The scorers' logged oddities do not compare: v0.23's logged 22% of the remarks, v0.24's 83%, and
  v0.25's prompt caps them at three per picture. Earlier screens did not record which model read them; v0.24's and v0.25's ran on Claude Opus 5.5.
- No reader says "teenager": the v0.24 redraw is read as a boy or a man, which the key mostly accepts. It moved him from a woman to a
  boy, not to the key's own word.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 68 pictures 779 of 785 scored items had full marks (799 of 805 in v0.24). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, a v0.24 scorer eleven, and all three v0.25 scorers listed such calls, enough to move a template across the gate.
- Tier-4 pictures are the hardest to place, and revisions 14 to 22 make them harder (walkers' and runners' lanes, pointing
  lines, feet off benches and off other events' things, the photographer's line of sight, the waver's clear hand, body gaps, the gap
  from thin parts, heads clear of figures up to 80 px apart in depth, the ground clear past a reading walker's obstacle, jumpers in the
  front half, an obstacle a full step ahead, runners clear of other movers, ducks off a float, sleepers clear of walkers' feet, nobody in
  the strip before the horizon). The tier-4 garden and park came again on their v0.24 seeds; the street took 13 failed seeds across three
  searches side by side, the playground 3 across two. Their records rebuild them exactly.
- The square-wheeled bicycle still stands on its own: four stands have been tried on the bench, and each
  read as something else (pedals, legs) or not at all.
- The low kick's direction is ambiguous when the kicker's hair hides the face; the teenager kicks first,
  and the kick read in full in all its screened pictures. His cap worn backwards was read as such, and one design-test reader
  noted it "could be misread as him facing left".
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
- The planner's priors come from the v0.25 calibration, with f = 0 and a at its centre for every inference and contradiction, as in
  v0.20 to v0.24: the bird at the sandwich's cue salience moved by -0.32 with its smaller size, the newspaper dog's by +0.08, every other
  template's by at most 0.001.
- Exact rebuilds hold within a release, on the pinned Pillow: the v0.25 cast (builder 0.25.0) and placement rules (revision 23) change how
  the bag, the roller, the bird and the newspaper dog look, so a v0.24 record rebuilds with the v0.24 package.
- Every variant comes from the v0.25 cast (builder 0.25.0, `out025`): the variants of the families and poses v0.25 did not change were
  carried over from `lib024`, the rest rendered anew. Some carried variants date from Linux renders, which differ from an installed Blender's
  only in sub-pixel anti-aliasing on the outlines. The library keeps only the 372 variants the v0.25 set and probes use. The bench
  variants (`TPDB_BAG`, `TPDB_ROLLER`, `TPDB_TEEN`, `TPDB_SLIDE`, `draw.RIDE24`, `draw.PAW25`) stay in the code.
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
  v0.24 and v0.25. The v0.25 isomorphs are two at tier 2, two at tier 3 and one at tier 4.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
