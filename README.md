# TPDB v0.30: a hose that hangs, crumbs on the water, the trip off the street, read a twenty-seventh time

v0.29 ended with all 64 templates through the gate, and three things that needed saying about that. Its trip had only been read in street pictures. Its new hose had a fault of its own, a short piece at the fist that "seems to stop at about waist height". And the fish's new limb was "a little pasted in", with a tuft that "looks detached". Crumbs lay "on the grass past the pond edge", and a reel with nobody at it had "only a short stub of hose joined to nothing".

v0.30 works through those. Each drawing went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a twenty-seventh time.

The twenty-seventh screen read all 78 pictures, the set's 21 and 57 probes: 872 of 877 scored items had full marks, and none was misread. The sleeve is gone, the crumbs are on the water, and no reel has a stub. The trip read in full in eleven pictures, six of them outside the street. 63 of 64 templates pass, against 64, and the one failure, `hang_laundry` (0.83), is one half mark on washing under storm clouds: "taking it down because of the coming storm".

The most useful thing in this release was not planned. It changed so little in the set that 18 of the 21 pictures came back identical to the pixel, so 19 pictures in all were read twice with nothing changed. 223 of their 230 items scored the same, remarks per picture were 5.58 and 5.68, and four templates moved by a half mark with no picture changed. That corrects two things said before: that four of five readers allow the trip's walker may pass the box, which is one of five on the same pictures, and remarks on thin figures, read as a rise in the last two releases, halved with nothing done.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.29 readers saw | v0.30 |
|---|---|
| The hose at the fist: "seems to stop at about waist height, then the part at her hands starts again" | The hose runs on in front of the figure and up to the fist, and hangs from it as a rope hangs. Nobody has it stop or break. "Stiff" stays, as it has of every way of drawing it since v0.25: "rises to her hand in a stiff curve" |
| The fish's limb: "drawn on top of the leafy crown", a tuft that "looks detached" | The fork's other arm and its tuft gone. What it cost: "it sits on what looks like the tree's bent trunk". All three of its pictures read the fish as impossible |
| Crumbs: "several crumbs lie on the grass past the pond edge" | Only those on the water, clear of its edge. No remark in three pictures, and the duck reads as eating in all three |
| The reel: "only a short stub of hose joined to nothing", "a short second stub of hose curls by the reel" | The end of the hose lying on the grass with its nozzle on, and gone when somebody has the hose. "A yellow nozzle lying on the grass", in all four of its pictures |
| The trip, read only in street pictures | Not redrawn. Probes put it in two gardens, two parks and two playgrounds: all eleven of its pictures read in full |

Left as they were: the box's width, as 60 units read a little less firmly than 72; the reading dog, as no reader called it a kangaroo this time, with nothing changed; the heavy rider's leg, now first on the next list; the narrow figure. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, a wind that reaches only some things.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v030.md`, two rounds, 33 cut-outs, 12 readers). The variants are behind `HOSE30`, `FISH30`, `TRIP_W30` and `CRUMB30` in `scenegen/templates.py` and `REEL30` in `scenegen/settings.py`; the release builds with the chosen ones. The cast did not change. The hose took two rounds. Run on to the fist, the square end and the gap went, and with it hanging as a rope hangs its S-bend over the bed went too. Six of six still found it stiff, and there this release stopped. The fish took two: leaves on the crown read as "bushes floating in the foliage", and a limb running on past the fish gave a fish "floating just above" it and a blunt stub, so it has one limb that ends under the fish. Looking at the first crops stopped three things before any reader saw them, among them a bench whose flags had left the old obstacle and the old duck on the new cases.

## Design tests

After the bench, the new drawings were read blind in whole test scenes among other events (`vision/design_tests_v030.md`, six pictures, six readers). The trip was said in the free description in a garden, a park and a playground, the settings v0.29 had not screened it in: "he looks about to walk into it and trip". All three also gave a second reading below. The duck was "pecking at small pale pieces of food", with nothing off the water. The hose drew no sleeve or gap, and "reads as a hose, but the upright section looks a little like a loop standing on its own". The fish's limb was "like a hook or a pipe", once, and went on the list. No reading called for a new rule.

## Placement revision 28

Every record stores the placement revision it was made with. v0.30 pictures use revision 28, which adds to those of revisions 1 to 27 the hose hanging from the fist and running on up to it in front of the figure; the fish's limb with no other arm; the thrown crumbs only on the water; and the end of the hose on the grass with its nozzle on when nobody has the hose, and none when somebody has. The cast is v0.29's (builder 0.30.0, nothing redrawn).

All four tier-4 cells placed on last release's seeds, with no failed seed, against 166 in v0.29. That is not the wide box getting cheaper: nothing about it changed, so the seeds that had been found came back. The box was tried narrower (60 units for 72) and the lane beyond it shorter (300 for 380). Forced into a picture with the difficulty band off, every combination placed every time, 40 of 40 at tier 3 and 24 of 24 at tier 4, which only says the test could not tell them apart. With the band on, the two extremes placed the same in their first two settings, and the test was stopped as the question had gone away. The box stays at 72, as 60 read a little less firmly, and what it costs a fresh search is still as v0.29 found it (`vision/flaws_v030.md`, Placement).

The tier-4 isomorph took 13 failed attempts. Probes put the trip in two gardens, two parks and two playgrounds, and two more filled the templates the first pass left short. All 78 records rebuild identical to the pixel.

The planner's difficulty priors are the calibration measured on the v0.30 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.29. Almost nothing moved: 2 fields in 1 template by 0.002 or more, the duck's, by -0.006 and -0.005, the cast being unchanged.

## The twenty-seventh blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 57 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.29.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) | v0.25 (21 pictures) | v0.26 (21 pictures) | v0.27 (21 pictures) | v0.28 (21 pictures) | v0.29 (21 pictures) | v0.30 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 0.98 | 0.99 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 0.99 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 | 0.98 | 0.95 | 0.95 | 0.88 | 0.98 | 0.99 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 0.98 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.99 | 0.98 | 0.99 | 0.99 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 | 0 of 286 | 0 of 289 | 0 of 283 | 0 of 284 | 0 of 285 |
| Oddities per picture, as logged by the scorers | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 | 2.6 | 2.6 | 2.2 | 2.0 | 2.3 | 2.3 |
| Readers' remarks per picture (recounted in v0.26) | 8.8 | 5.4 | 6.4 | 4.8 | 4.7 | 4.8 | 4.9 | 4.4 | 4.3 | 4.4 | 4.4 | 4.4 | 3.9 | 3.9 | 4.4 | 4.0 | 4.0 | 3.9 | 4.2 | 3.9 | 5.6 | 5.9 | 5.3 | 5.8 | 5.1 | 5.2 | 5.2 |

Across all 78 pictures 872 of 877 scored items had full marks. Four had half marks, one was missed, and none was misread, all five in the set: a missed "a few white clouds", the dog reading ("genuinely reading, or as just holding or playing with the newspaper"), the man at the washing line ("taking it down because of the coming storm"), and in one picture the girl with the ice cream ("an ice cream or a pink lolly") and the lost balloon. One scorer gave no item under full marks in 302, and listed 22 a stricter scorer might halve. The set's headline is all items 0.989 (0.991 in v0.29), with things at 0.990, actions at 0.992, inferences at 0.986 and contradictions at 0.977.

**A retest nobody planned.** 19 pictures, 18 of the set's and one probe, were identical to the pixel in v0.29 and v0.30, so they were read twice by fresh readers and scorers with nothing changed. 223 of their 230 items scored the same. Three of the seven that moved are clouds. The others took `dog_begs` from 1.00 to 0.944, `dog_reading` and `lost_balloon` from 1.00 to 0.967, and `bird_steals` from 0.958 to 1.00, each on one half mark. Remarks were 106 and 108. Readers offering that the trip's walker may pass the box went from four of five to one of five on the same five pictures, so v0.29's concern about that, and its 0.87, were not properties of the picture.

**Remarks did not move, 405 on 78 pictures against 386 on 75**, on a few more templates in each picture, 2.99 against 2.92. The readers range from 4.50 to 6.12 a picture on the same split, against 4.50 to 5.75. `vision/remark_topics.py` sorts them roughly by keyword, and it is rougher than it looked: thin or long bodies fell from 13 pictures to 6, a figure over the pond from 10 to 6, and scale from 6 to 3, all with nothing changed. A branch to hold something fell from 6 to 2, some of which is this release's. A keyword row should not be given as a result unless it moves by more than these did.

The one that failed, the trip, what this release redrew, and three that moved with little or nothing done (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.29 | v0.30 | v0.30 meaning items |
|---|---|---|---|
| `hang_laundry` | 1.00 (3 items) | 0.83 (3 items) | — |
| `about_to_trip` | 1.00 (15 items) | 1.00 (33 items) | 1.00 (11) |
| `hose_water` | 1.00 (3 items) | 1.00 (3 items) | — |
| `ducks_bread` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `dog_begs` | 1.00 (9 items) | 0.94 (9 items) | 1.00 (3) |
| `dog_wants_walk` | 0.92 (6 items) | 1.00 (6 items) | 1.00 (3) |
| `bird_steals` | 0.96 (12 items) | 1.00 (12 items) | 1.00 (4) |

`hang_laundry` is the one failure, on a picture new this release. `about_to_trip` holds at 1.00 on eleven pictures and in every setting, its box not redrawn. `hose_water` reads in full, its sleeve gone. `dog_begs` moved with no picture changed, and `dog_wants_walk` and `bird_steals` rose with nothing done.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 | v0.27 | v0.28 | v0.29 | v0.30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 | 61 | 59 | 63 | 61 | 64 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 | 3 | 5 | 1 | 3 | 0 | 1 |

Every template was screened in at least three pictures (44 in three, 11 in four, 4 in five, 2 in six, and one each in seven, ten and eleven), and 63 of 64 pass, against 64. The failure is one half mark among three items. This release's own retest shows that a half mark comes and goes on a picture that has not changed, as the v0.9 retest did by other means. The gate is a filter, and the pilot with people is the test of difficulty.

Templates that did not pass (`vision/flaws_v030.md` gives what the readers saw and the next fix):

| Template | v0.30 mean | Pictures | Misreads |
|---|---|---|---|
| `hang_laundry` | 0.83 (3 items) | 3 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.777 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.772 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s1031 | 4 | 0 (0) | 3 | 0.776 | — | 12 | 0.043 | birds flying, jump, run |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.771 | — | 14 | 0.033 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.711 | 0.417 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_garden_s8118_iso (isomorph of T2_playground_s042) | 8 | 1 (0) | 3 | 0.708 | 0.393 | 19 | 0.043 | kite in tree, swing, rake |
| T2_park_s022 | 8 | 1 (0) | 4 | 0.709 | 0.410 | 19 | 0.028 | kite in tree, push stroller, carry box, dog sleeping |
| T2_street_s1032 | 8 | 1 (0) | 4 | 0.711 | 0.366 | 20 | 0.050 | cat stalks bird, wave, carry bag, read bench |
| T2_street_s14109_iso (isomorph of T2_park_s022) | 8 | 1 (0) | 4 | 0.710 | 0.430 | 16 | 0.051 | about to trip, drink bench, carry bag, photo |
| T2_playground_s042 | 8 | 1 (0) | 3 | 0.709 | 0.394 | 16 | 0.035 | lost balloon, slide, carry box |
| T3_garden_s19213 | 12 | 3 (1) | 5 | 0.661 | 0.351 | 22 | 0.044 | blocked hose, rain coming, sitting on air, hang laundry, walk dog |
| T3_park_s2023 | 12 | 3 (0) | 6 | 0.640 | 0.307 | 23 | 0.032 | lost balloon, ball in tree, cat stalks bird, ice cream, dig, balloon |
| T3_street_s18133 | 12 | 2 (0) | 5 | 0.667 | 0.357 | 21 | 0.054 | about to trip, dog begs, water flowers, photo, bird perched |
| T3_street_s6104_iso (isomorph of T3_park_s2023) | 12 | 3 (0) | 6 | 0.642 | 0.313 | 21 | 0.051 | about to trip, lost balloon, dog begs, birds flying, bird perched, sweep |
| T3_playground_s1043 | 12 | 2 (1) | 5 | 0.659 | 0.341 | 22 | 0.040 | ice cream drop, dog reading, birds flying, drink bench, fly kite |
| T3_playground_s19102_iso (isomorph of T3_street_s18133) | 12 | 2 (0) | 5 | 0.667 | 0.342 | 21 | 0.038 | lost balloon, cat stalks bird, bird perched, drink bench, fly kite |
| T4_garden_s429914 | 18 | 5 (1) | 9 | 0.550 | 0.201 | 34 | 0.048 | kite in tree, paint tracks, bird steals, cat stalks bird, square wheel, plant flowers, goat grazing, dog playing, rake |
| T4_park_s728923 | 18 | 5 (2) | 8 | 0.566 | 0.254 | 30 | 0.037 | ice cream drop, ducks bread, kite in tree, dog reading, pan watering, birds flying, goat grazing, sweep |
| T4_street_s447752 | 18 | 5 (2) | 9 | 0.571 | 0.213 | 27 | 0.058 | bird steals, about to trip, ball in tree, dog reading, water upward, birds flying, sweep, jump, carry bag |
| T4_street_s26111_iso (isomorph of T4_playground_s460662) | 18 | 5 (2) | 9 | 0.572 | 0.237 | 27 | 0.057 | bird steals, ball in tree, about to trip, square wheel, dog reading, bird perched, wave, sweep, ice cream |
| T4_playground_s460662 | 18 | 5 (2) | 9 | 0.558 | 0.232 | 27 | 0.043 | bird steals, kite in tree, lost balloon, square wheel, dog reading, run, photo, dog playing, birds flying |

Isomorph pairs differ by at most 0.014 in content and 0.020 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 26,415 | 27 | 11,768 | 10^12.7 |
| garden | 3 | 2,417,515 | 296 | 325,793 | 10^18.5 |
| garden | 4 | 72,545,098 | 565 | 5,951,818 | 10^23.2 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 46,279 | 24 | 20,254 | 10^11.2 |
| park | 3 | 5,665,235 | 236 | 1,000,109 | 10^17.2 |
| park | 4 | 313,983,956 | 376 | 42,220,582 | 10^23.1 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,433 | 24 | 2,952 | 10^11.8 |
| street | 3 | 434,458 | 220 | 68,611 | 10^17.3 |
| street | 4 | 6,920,598 | 330 | 910,127 | 10^21.6 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.3 |
| playground | 3 | 738,151 | 183 | 110,468 | 10^17.7 |
| playground | 4 | 10,363,379 | 232 | 1,312,634 | 10^20.8 |

In all 413,171,988 structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, and v0.30 draws nothing new |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out030/` | The 18 `.blend` families (builder 0.30.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib030/` | Every variant the generated scenes and probes use, carried over from `lib029` or rendered from `out030` |
| `assets/cast/gallery030/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (175, all pass the validator) |
| `scenegen/` | The generator (0.30.0, placement revision 28); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`); `library.py` the shadow's two (`SHADOW28`) and the sleeper's wider one (`SHADOW29`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.30 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v030.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v030.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v030.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all twenty-seven screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out030                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out030 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s2023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v030   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v030 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery030 --old-gallery <v0.29 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.30 --single   # the release as one zip, tpdb_v0.30.zip
```

The release is one zip, `tpdb_v0.30.zip`, about 186 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.29 record rebuilds with the v0.29 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- One template falls under the legibility gate after the v0.30 screen, `hang_laundry` (0.83), on one half mark among three items, on washing under storm clouds. 63 of 64 pass.
  `vision/flaws_v030.md` lists this and the oddities for v0.31.
- A single half mark is noise. 19 pictures were identical to the pixel in v0.29 and v0.30, and 223 of their 230 items scored the same across fresh readers and scorers, with four templates moving by a half mark and no picture changed (`vision/flaws_v030.md`, A retest nobody planned). A template with few items can cross the gate on that alone.
- What the trip's long box costs a fresh tier-4 search is as v0.29 found it, 166 failed seeds against 80. This release's cells came back on their seeds, so it paid nothing and shows nothing new.
- The oddities come in two rows. Readers' remarks per picture are counted directly from their descriptions and compare across
  screens, with the caveat that current readers write about 18% more than the v0.23 readers on the same pictures (`vision/v024/control/`,
  one reader and eight pictures). The row was recounted in v0.26, as the counter had taken bullets saying nothing is wrong for remarks, so its
  figures differ from those published up to v0.25. The scorers' logged oddities do not compare: v0.23's logged 25% of the remarks, v0.24's 83%, and
  from v0.25 the prompt caps them at three per picture. Earlier screens did not record which model read them; v0.24's to v0.30's ran on Claude Opus 5.5. Readers differ widely: on v0.28's nine, from 4.25 to 6.38 remarks a picture, on v0.29's from 4.50 to 5.75, and on v0.30's from 4.50 to 6.12.
- No reader says "teenager": he is read as a boy, a boy or young man, or a person, which the key mostly accepts. The v0.24 redraw moved him
  from a woman to a boy, and v0.26's cap worn forwards moved him no further toward the key's own word. It read once as "worn backward or sideways" in v0.27.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 78 pictures 872 of 877 scored items had full marks (829 of 834 in v0.29). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, a v0.24 scorer eleven, and all three scorers of v0.25 to v0.30 listed such calls, enough to move a template across the gate. A v0.29 scorer listed 18 items that hold full marks because the free description committed and only the unsure section hedged, and a v0.30 scorer gave nothing under full marks in 302 and listed 22 it thought a stricter scorer might halve. A misread is a call too: the
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
- The planner's priors come from the v0.30 calibration, with f = 0 and a at its centre for every inference and contradiction, as in
  v0.20 to v0.29: 2 fields in 1 template moved by 0.002 or more, the duck's. The ladder's still rests on one sampled placement, since v0.29's lamp rule.
- Exact rebuilds hold within a release, on the pinned Pillow: the v0.30 cast (builder 0.30.0) and placement rules (revision 28) change what is drawn at the hose, the tree and the pond,
  so a v0.29 record rebuilds with the v0.29 package.
- Every variant comes from the v0.30 cast (builder 0.30.0, `out030`), which draws nothing new: what the set and probes use was carried over from `lib029`, or rendered on demand on an installed Blender. Some carried variants date from Linux renders, which differ from an installed Blender's
  only in sub-pixel anti-aliasing on the outlines. The library keeps only the 386 variants the v0.30 set and probes use. The bench
  variants (`TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ`, `TPDB_BEARD`, `TPDB_BROW`, `TPDB_BLUSH`, `draw.WHEEL27`, `draw.SPLAT28`, `draw.SEESAW_IN28`, `library.SHADOW28`, `library.SHADOW29`, and `SLEEP29`, `TRIP29`, `TRIP_OBJ29`, `DUCK29`, `DOOR29`, `HOSE29`, `BULGE29`, `FISH29`, `LADDER_LAMP29`, `HOSE30`, `FISH30`, `TRIP_W30`, `TRIP_LANE30` and `CRUMB30` in `templates.py`, and `REEL30` in `settings.py`) stay in the code.
- The figures are still narrow. Legs an eighth shorter and limbs 14% thicker took the bench from eight remarks to three, on four cut-outs a side, but the screen's remarks on
  thin or long bodies did not fall (six pictures to eight in v0.27, to thirteen in v0.28 and v0.29, and back to six in v0.30, with nothing changed, by keyword, so that row says little). A real change of build is a larger job than these.
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
  v0.24 and v0.25, and with it from v0.26. The v0.30 isomorphs are two at tier 2, two at tier 3 and one at tier 4; the tier-4 one
  took 13 failed attempts.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- A shadow from the figure's own footprint is smaller, and a body lying down has little of it showing. The sleeping dog now reads in full on its new pose and that shadow; a wider one did little on the bench, so whether the shadow cost it marks in v0.28 is still not shown.
- The trip's meaning item is 1.00 on the long box in eleven pictures and every setting. Five of its readers also say the walker may step round it, which on the same five pictures went from four of five to one of five with nothing changed.
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
