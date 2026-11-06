# TPDB v0.36: the grandfather's moustache, the washing off the line, read a thirty-third time

v0.35 ended with 63 of 64 templates through the gate, the one failure a grandfather with a bucket on his head, taken for "a boy in a white shirt, brown waistcoat and dark trousers". Its list went on to washing on a line offered, twice on one seed, as what a storm pointer points at, and a gate's knob behind a head read as "a hair bun".

v0.36 works through those. The grandfather under the bucket went to the isolation bench first, drawn four ways and then two, and read blind on his own, then into whole test scenes among other events. The set was regenerated and screened a thirty-third time.

The thirty-third screen read all 82 pictures, the set's 21 and 61 probes: 873 of 876 scored items had full marks, and none was misread. The grandfather under the bucket, v0.35's one failure, is an "Old man, front centre: white hair, grey moustache" on the seed of v0.35's misread, and all 64 templates pass. No reader offers washing as what the storm pointer points at; one offers the empty line. The gate's knob is not fixed: revision 34 keeps it off the box round each face, the sweeper it was for stands in profile with his face turned from the gate, and his picture came back unchanged, the knob read as a bun a third time. It is the first item for v0.37.

This screen is a retest too: 60 pictures were identical to v0.35's, and 563 of their 576 items scored the same, the 12 that moved up all clouds that v0.35's two readers had missed.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.35 readers saw | v0.36 |
|---|---|
| The grandfather under the bucket: "a boy in a white shirt, brown waistcoat and dark trousers" | A white moustache, which his spec always gave him but no render ever drew, and the bucket sat higher, so his white hair shows below its rim. On the bench every reader of the two together had him an older man, where none of the three readers of v0.35's drawing did |
| The storm pointer: "could be pointing at the dark clouds (rain coming) or at the laundry on the line" | No washing on the line in a storm pointer's picture, the line left empty |
| "It could be a hair bun, or it could be the gate's knob showing behind his head" | The box round every face kept 16 px clear of the garden gate's knob. The box misses the back of a head in profile, and the picture that asked for the rule came back unchanged: its sweeper was read as a woman "with dark hair in a bun", the knob taken for a bun a third time. It is the v0.37 list's first item |

Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, autumn leaves under summer trees, and hair and clothes that the wind does not move.

## The isolation bench

The grandfather under the bucket was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v036.md`, two rounds, 21 cut-outs, 21 readers, one each). The variants are behind `TPDB_MOUSTACHE36`, `TPDB_MOUSTACHE36_FLAT` and `TPDB_BUCKET36` in the cast; the release builds with the chosen ones. His moustache had never shown: every expression hides each face part it does not name, and none named it. Drawn and shown, it said his age in every reading that had it ("An older man with grey hair and a grey moustache"), and the raised bucket alone said it in two of three. Drawn bold and standing off the face, it was taken twice for "a pipe, cigar or whistle" under the bucket and once in profile for "something held in his mouth"; lying flatter on the skin, in the second round, it was taken for nothing else in six readings.

## Design tests

After the bench, the grandfather's moustache and revision 34 were read blind in whole test scenes among other events (`vision/design_tests_v036.md`, six pictures, six readers). In all four pictures of the grandfather he is old, by his grey hair and moustache, under the bucket and kneeling to plant in profile ("Older man, front, centre-left, standing at the right edge of the dirt path: grey hair and grey moustache"), and no reader takes the moustache for anything in his mouth. The storm pointer reads at the clouds over the empty line ("It is empty, with no clothes or pegs on it"), and the garden's sweepers by the gate draw no remark of its knob. None of the six was the picture that asked for the knob rule, and the screen found that one unchanged.

## Placement revision 34

Every record stores the placement revision it was made with. v0.36 pictures use revision 34, which adds to those of revisions 1 to 33 no washing on the line in a storm pointer's picture, the line left empty; and the box round every face kept 16 px clear of the garden gate's knob (the box misses the back of a head in profile). Both are behind the revision, so v0.35's records rebuild. The cast is v0.35's with the grandfather's moustache and the bucket sat higher (builder 0.36.0).

All four tier-4 cells placed on v0.35's seeds under revision 34, the street's on v0.29 to v0.35's forced set: the garden on its tenth layout, its sixth having had a face beside the gate's knob, the park and the street changed only by the grandfather's moustache, and the playground identical. 13 of the set's 21 pictures came back identical to v0.35's, and seven of the other eight differ by the moustache alone, in a box some 22 by 16 px. The tier-4 isomorph took 12 failed attempts, as in v0.33 to v0.35. The first probe pass left `walk_dog`, `dog_begs` and `windy_hat` short, as in v0.35, and two more probes filled them. All 82 records rebuild identical to the pixel, and the library passes the validator in full, 345 of 345.

The planner's difficulty priors are the calibration measured on the v0.36 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.35. Four fields of `bucket_hat` moved by 0.002 or more with the grandfather's moustache, its salience the most (0.262 to 0.277), and its salience prior went from 0.26 to 0.28.

## The thirty-third blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 61 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.35.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) | v0.25 (21 pictures) | v0.26 (21 pictures) | v0.27 (21 pictures) | v0.28 (21 pictures) | v0.29 (21 pictures) | v0.30 (21 pictures) | v0.31 (21 pictures) | v0.32 (21 pictures) | v0.33 (21 pictures) | v0.34 (21 pictures) | v0.35 (21 pictures) | v0.36 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 0.97 | 1.00 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 | 0.98 | 0.95 | 0.95 | 0.88 | 0.98 | 0.99 | 1.00 | 0.96 | 0.96 | 0.99 | 0.96 | 0.97 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.99 | 0.98 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 0.98 | 1.00 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 | 0 of 286 | 0 of 289 | 0 of 283 | 0 of 284 | 0 of 285 | 0 of 284 | 1 of 286 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 285 |
| Oddities per picture, as logged by the scorers | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 | 2.6 | 2.6 | 2.2 | 2.0 | 2.3 | 2.3 | 0.6 | 0.8 | 0.9 | 0.5 | 0.2 | 0.6 |
| Readers' remarks per picture (recounted in v0.26) | 8.8 | 5.4 | 6.4 | 4.8 | 4.7 | 4.8 | 4.9 | 4.4 | 4.3 | 4.4 | 4.4 | 4.4 | 3.9 | 3.9 | 4.4 | 4.0 | 4.0 | 3.9 | 4.2 | 3.9 | 5.6 | 5.9 | 5.3 | 5.8 | 5.1 | 5.2 | 5.2 | 3.5 | 3.3 | 3.2 | 3.1 | 2.9 | 3.1 |

Across all 82 pictures 873 of 876 scored items had full marks, and none was misread. The three scorers gave none, two and one items under full marks, in 304, 283 and 289: a duck coming for the bread and a balloon let go of, each said by half, and a probe's tree. The set's headline is all items 0.996 (0.982 in v0.35), with things and actions at 1.00, inferences at 0.971 and contradictions at 1.00, and every reader named the clouds.

**A seventh retest.** 60 pictures, 13 of the set's and 47 probes, were identical to the pixel in v0.35 and v0.36. 563 of their 576 items scored the same; 12 moved up, every one the clouds, and one down, the probe's tree.

**Remarks were 3.10 a picture, 254 on 82 pictures**, from 2.33 to 3.89 a reader. On the 60 identical pictures they rose from 163 to 175. The scorers' lists hold two new things: the storm pointer standing on the fork sweeper's dustpan, in the picture that placed again when its washing came off, and a market stall's leg that "seems to stand on the small wooden crate under it", twice, from one reader. The sweeper by the gate was "a woman with dark hair in a bun", the knob behind his head, as in v0.34 and v0.35.

What this release redrew or ruled, among them v0.35's one failure (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.35 | v0.36 | v0.36 meaning items |
|---|---|---|---|
| `bucket_hat` | 0.89 (9 items) | 1.00 (9 items) | 1.00 (6) |
| `rain_coming` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (3) |

`bucket_hat` goes from 0.89 to 1.00, its wearers an old man with a grey moustache, a bearded man and the grandmother, read as an older man under the bucket, her age right. `rain_coming` holds at 1.00, the line empty.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 | v0.27 | v0.28 | v0.29 | v0.30 | v0.31 | v0.32 | v0.33 | v0.34 | v0.35 | v0.36 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 | 61 | 59 | 63 | 61 | 64 | 63 | 63 | 63 | 63 | 64 | 63 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 | 3 | 5 | 1 | 3 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |

Every template was screened in at least three pictures (52 in three, 4 in four, 4 in five, 2 in six and 2 in eleven), and all 64 pass, as in v0.34. The lowest are `ducks_bread` (0.944) and `lost_balloon` (0.967), each on one half-marked inference. The gate is a filter, and the pilot with people is the test of difficulty.

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.777 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.772 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s1031 | 4 | 0 (0) | 3 | 0.776 | — | 12 | 0.043 | birds flying, jump, run |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.772 | — | 14 | 0.033 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.711 | 0.417 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_garden_s8118_iso (isomorph of T2_playground_s042) | 8 | 1 (0) | 3 | 0.710 | 0.394 | 17 | 0.040 | kite in tree, swing, rake |
| T2_park_s022 | 8 | 1 (0) | 4 | 0.709 | 0.410 | 19 | 0.028 | kite in tree, push stroller, carry box, dog sleeping |
| T2_street_s1032 | 8 | 1 (0) | 4 | 0.711 | 0.366 | 20 | 0.050 | cat stalks bird, wave, carry bag, read bench |
| T2_street_s14109_iso (isomorph of T2_park_s022) | 8 | 1 (0) | 4 | 0.708 | 0.430 | 16 | 0.051 | about to trip, drink bench, carry bag, photo |
| T2_playground_s042 | 8 | 1 (0) | 3 | 0.709 | 0.394 | 16 | 0.035 | lost balloon, slide, carry box |
| T3_garden_s11954 | 12 | 3 (0) | 6 | 0.666 | 0.333 | 25 | 0.040 | paint tracks, dog wants walk, rain coming, dig, cat on fence, play catch |
| T3_park_s2023 | 12 | 3 (0) | 6 | 0.640 | 0.307 | 23 | 0.031 | lost balloon, ball in tree, cat stalks bird, ice cream, dig, balloon |
| T3_street_s18133 | 12 | 2 (0) | 5 | 0.667 | 0.357 | 21 | 0.054 | about to trip, dog begs, water flowers, photo, bird perched |
| T3_street_s6104_iso (isomorph of T3_park_s2023) | 12 | 3 (0) | 6 | 0.642 | 0.313 | 21 | 0.051 | about to trip, lost balloon, dog begs, birds flying, bird perched, sweep |
| T3_playground_s1043 | 12 | 2 (1) | 5 | 0.659 | 0.341 | 22 | 0.040 | ice cream drop, dog reading, birds flying, drink bench, fly kite |
| T3_playground_s19102_iso (isomorph of T3_street_s18133) | 12 | 2 (0) | 5 | 0.667 | 0.342 | 21 | 0.037 | lost balloon, cat stalks bird, bird perched, drink bench, fly kite |
| T4_garden_s414896 | 18 | 5 (2) | 8 | 0.567 | 0.222 | 28 | 0.051 | kite in tree, bird steals, blocked hose, bucket hat, square wheel, dog sleeping, rake, cat on fence |
| T4_park_s728923 | 18 | 5 (2) | 8 | 0.566 | 0.254 | 30 | 0.037 | ice cream drop, ducks bread, kite in tree, dog reading, pan watering, birds flying, goat grazing, sweep |
| T4_street_s430752 | 18 | 5 (2) | 9 | 0.583 | 0.212 | 26 | 0.058 | bird steals, about to trip, ball in tree, dog reading, water upward, birds flying, sweep, jump, carry bag |
| T4_street_s26111_iso (isomorph of T4_playground_s460662) | 18 | 5 (2) | 9 | 0.572 | 0.237 | 27 | 0.057 | bird steals, ball in tree, about to trip, square wheel, dog reading, bird perched, wave, sweep, ice cream |
| T4_playground_s460662 | 18 | 5 (2) | 9 | 0.558 | 0.232 | 27 | 0.043 | bird steals, kite in tree, lost balloon, square wheel, dog reading, run, photo, dog playing, birds flying |

Isomorph pairs differ by at most 0.014 in content and 0.020 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 25,810 | 27 | 11,275 | 10^12.7 |
| garden | 3 | 2,343,163 | 296 | 310,307 | 10^18.3 |
| garden | 4 | 70,686,492 | 565 | 5,759,476 | 10^23.3 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 45,955 | 24 | 19,978 | 10^11.2 |
| park | 3 | 5,569,417 | 236 | 972,951 | 10^17.3 |
| park | 4 | 307,551,136 | 376 | 41,212,001 | 10^22.9 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,298 | 24 | 2,847 | 10^11.7 |
| street | 3 | 420,725 | 220 | 65,745 | 10^17.2 |
| street | 4 | 6,676,618 | 330 | 876,099 | 10^21.5 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.3 |
| playground | 3 | 738,151 | 183 | 110,468 | 10^17.7 |
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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, and v0.36 draws the grandfather's moustache and sits the bucket higher |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out036/` | The 18 `.blend` families (builder 0.36.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib036/` | Every variant the generated scenes and probes use, carried over from `lib035` or rendered from `out036` |
| `assets/cast/gallery036/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (175, all pass the validator) |
| `scenegen/` | The generator (0.36.0, placement revision 34); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.36 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v036.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v036.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v036.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all thirty-three screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out036                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out036 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s2023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v036   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v036 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery036 --old-gallery <v0.35 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.36 --single   # the release as one zip, tpdb_v0.36.zip
```

The release is one zip, `tpdb_v0.36.zip`, about 194 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.35 record rebuilds with the v0.35 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- No template falls under the legibility gate after the v0.36 screen: all 64 pass, and `bucket_hat`, v0.35's failure, reads in full with the grandfather's moustache.
  The lowest is `ducks_bread` (0.94), on one half mark. `vision/flaws_v036.md` lists the oddities for v0.37, first among them the gate's knob, which revision 34 did not
  keep off the one head it was for (below).
- A single half mark is noise. 19 pictures were identical to the pixel in v0.29 and v0.30, and 223 of their 230 items scored the same across fresh readers and scorers, with four templates moving by a half mark and no picture changed (`vision/flaws_v030.md`, A retest nobody planned). In v0.31, 12 pictures came back identical once more, and 137 of their 141 items scored the same; the one that went down is the gate's one failure. In v0.32, 19 came back identical, and 242 of their 246 items scored the same; the four that went down are again the gate's one failure, and a begging dog's half mark. In v0.33, 21 came back identical, and 274 of their 281 items scored the same, three moving up and four down. In v0.34, 26 came back identical, and 296 of their 299 items scored the same, two moving up and one down. In v0.35, 78 came back identical, and 806 of their 830 items scored the same, 7 moving up and 17 down, 12 of the 17 the clouds of two readers who named nothing in the sky. In v0.36, 60 came back identical, and 563 of their 576 items scored the same, 12 moving up, every one those clouds, and one down. A template with few items can cross the gate on that alone: `read_bench` has one item to a picture.
- What the trip's long box costs a fresh tier-4 search is as v0.29 found it, 166 failed seeds against 80. In v0.32 the garden, park and playground cells came back on their seeds; the street's did not under revision 30, in 39 seeds, and placed at once with v0.31's template set forced. In v0.33 all four came back unchanged, the street's on the same forced set, and in v0.34 to v0.36 all four came back on their seeds again.
- The oddities come in two rows. Readers' remarks per picture are counted directly from their descriptions and compare across
  screens, with the caveat that current readers write about 18% more than the v0.23 readers on the same pictures (`vision/v024/control/`,
  one reader and eight pictures). The row was recounted in v0.26, as the counter had taken bullets saying nothing is wrong for remarks, so its
  figures differ from those published up to v0.25. The scorers' logged oddities do not compare: v0.23's logged 25% of the remarks, v0.24's 83%, and
  from v0.25 the prompt caps them at three per picture. Earlier screens did not record which model read them; v0.24's to v0.36's ran on Claude Opus 5.5. Readers differ widely: on v0.28's nine, from 4.25 to 6.38 remarks a picture, on v0.29's from 4.50 to 5.75, and on v0.30's from 4.50 to 6.12. v0.31's nine wrote from 2.62 to 4.43, every one fewer than the fewest of v0.30's, and on 12 pictures identical in both screens remarks fell from 65 to 45. So a screen's readers can move the row by a third, and its fall to 3.51 in v0.31 says nothing about the drawings. v0.32's nine wrote from 2.71 to 4.43, 3.28 a picture, and on 19 pictures identical in both screens remarks fell from 79 to 67. v0.33's nine wrote from 2.44 to 4.11, 3.19 a picture, and on 21 identical pictures remarks rose from 77 to 88. v0.34's nine wrote from 2.40 to 4.50, 3.13 a picture, and on 26 identical pictures remarks were 96 in both. v0.35's nine wrote from 2.44 to 3.50, 2.88 a picture, and on 78 identical pictures remarks fell from 243 to 222. v0.36's nine wrote from 2.33 to 3.89, 3.10 a picture, and on 60 identical pictures remarks rose from 163 to 175.
- No reader says "teenager": he is read as a boy, a boy or young man, or a person, which the key mostly accepts. The v0.24 redraw moved him
  from a woman to a boy, and v0.26's cap worn forwards moved him no further toward the key's own word. It read once as "worn backward or sideways" in v0.27.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 82 pictures 873 of 876 scored items had full marks (855 of 877 in v0.35, 17 of whose 22 others
  were the clouds of two readers who named nothing in the sky). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, a v0.24 scorer eleven, and all three scorers of v0.25 to v0.36 listed such calls, enough to move a template across the gate. A v0.29 scorer listed 18 items that hold full marks because the free description committed and only the unsure section hedged, and a v0.30 scorer gave nothing under full marks in 302 and listed 22 it thought a stricter scorer might halve. Two v0.31 scorers gave nothing under full marks, in 236 and 253 items, among them a bird "about to take it" credited as pecking. v0.32's three gave one, three and three items under full marks, in 244, 288 and 244, v0.33's four, one and three, in 301, 255 and 306, v0.34's one, none and ten, in 314, 282 and 289, where the second listed four inferences a stricter scorer might halve, v0.35's twelve, one and nine, in 304, 283 and 290, and v0.36's none, two and one, in 304, 283 and 289, where the first listed eight hedged inferences it credited in full. A misread is a call too: the
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
- The planner's priors come from the v0.36 calibration, with f = 0 and a at its centre for every inference and contradiction, as in
  v0.20 to v0.35: four fields of `bucket_hat` moved by 0.002 or more with the grandfather's moustache, and its salience prior went from 0.26 to 0.28. The ladder's still rests on one sampled placement, since v0.29's lamp rule.
- Exact rebuilds hold within a release, on the pinned Pillow: the v0.36 cast draws the grandfather's moustache, and its placement rules (revision 34) take the washing off a
  storm pointer's line and keep faces off the gate's knob, so a v0.35 record rebuilds with the v0.35 package. Revisions 31 to 34 keep their rules in the templates' placement or
  in `fits`, each behind its revision; revision 30's sky rule is still read at import (`RUNBOOK.md`).
- Every variant comes from the v0.36 cast (builder 0.36.0, `out036`), which draws as v0.35's but for the grandfather's moustache and the bucket sat higher on his head: what the set and probes use was carried over from `lib035`, or rendered on demand on an installed Blender, the seesaw's riders in two pieces each, and every variant of the grandfather rendered again. Some carried variants date from Linux renders, which differ from an installed Blender's
  only in sub-pixel anti-aliasing on the outlines. The library keeps only the 345 variants the v0.36 set and probes use. The bench
  variants (`TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ`, `TPDB_BEARD`, `TPDB_BROW`, `TPDB_BLUSH`, `draw.WHEEL27`, `draw.SPLAT28`, `draw.SEESAW_IN28`, `draw.SWING35`, `library.SHADOW28`, `library.SHADOW29`, and `SLEEP29`, `TRIP29`, `TRIP_OBJ29`, `DUCK29`, `DOOR29`, `HOSE29`, `BULGE29`, `FISH29`, `LADDER_LAMP29`, `HOSE30`, `FISH30`, `TRIP_W30`, `TRIP_LANE30`, `CRUMB30`, `SEESAW31`, `RIDE31`, `CASTLE31`, `LIMB31`, `LOW32`, `LOW_IN32`, `LOW_RISE32`, `LOW_RISE_B32`, `STUCK32`, `HANDLE32`, `HOSE33` and `KICK33` in `templates.py`, `REEL30` and `REEL31` in `settings.py`, and `TPDB_VEST`, `TPDB_CONE`, `TPDB_BOX`, `TPDB_LOW`, `TPDB_SEAT34`, `TPDB_HAIR34`, `TPDB_MOUSTACHE36`, `TPDB_MOUSTACHE36_FLAT` and `TPDB_BUCKET36` in the cast) stay in the code.
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
  v0.24 and v0.25, and with it from v0.26. The v0.36 isomorphs are two at tier 2, two at tier 3 and one at tier 4, three identical to v0.35's and two differing by the grandfather's moustache; the tier-4 one
  took 12 failed attempts.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- A shadow from the figure's own footprint is smaller, and a body lying down has little of it showing. The sleeping dog now reads in full on its new pose and that shadow; a wider one did little on the bench, so whether the shadow cost it marks in v0.28 is still not shown.
- The trip reads in full on the long box, in eleven pictures in v0.30 and five each in v0.31 to v0.36. In v0.30, five of its readers also said the walker may step round it, which on the same five pictures went from four of five to one of five with nothing changed.
- The man on the seesaw's low end is drawn astride, his far leg behind the plank. The v0.32 bench turned him away, or put both legs behind the plank, and readers of each still doubted his seat (legs out was set aside on looking);
  in the v0.32 screen he drew one remark in three pictures, that "the seesaw plank seems to pass behind or among the old man's legs". He is off the list; in v0.33 his legs over the plank drew a remark once more. The stuck girl holds a handle raised with her,
  and once a reader saw her hover, from the kick arcs under her feet, which v0.33 does not draw.
- A rider on the seesaw is two pictures, the far leg drawn behind the plank as background and the rest of the figure in front. The far leg is in no count, mask or check of the scene's own.
  Until v0.32 the validator failed the 12 pieces on their names; it now checks each by its base pose and leaves the ground rule to the piece with the body.
- The child on the swing is swung out 12 degrees (revision 33), turned in the picture with its seat and ropes, not posed so in the cast. The frame is widened on the
  side away from the path when a child swings, so its legs stay off the path, and an empty seat keeps the frame it had. One v0.35 reader found the ropes not quite
  "directly above the seat", and read the child as swinging.
- The gate's knob is kept off the box round each face (revision 34), and that box is drawn round the eyes and mouth: the back of a head in profile is not in it.
  The sweeper whose head the knob sat behind stands in profile, his face turned from the gate, so his picture came back unchanged, and a third screen read the
  knob as "dark hair in a bun" and him as a woman. In a storm pointer's picture the washing line is left empty (revision 34); the reader of the picture that
  asked for it offered the empty line as what she might point at, and as the washing already taken in for the rain. With the washing gone that picture placed
  again, and she stands on the fork sweeper's dustpan, which is not one of the things that others' feet are kept off.
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
