# TPDB v0.31: riders astride the seesaw, a spade at the castle, read a twenty-eighth time

v0.30 ended with 63 of 64 templates through the gate, the one failure a half mark on washing hung under storm clouds. Its list began with the seesaw, on the list since v0.27 and the largest thing left that was plainly a drawing fault: "the man's legs appear to go through or around the plank". The bearded man's vest had "a jagged edge against the white shirt", a child's hand and the castle "merge a little", and a reel stood "partly overlapping the edge of the flower bed".

v0.31 works through those. Each drawing went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a twenty-eighth time.

The twenty-eighth screen read all 71 pictures, the set's 21 and 50 probes: 783 of 784 scored items had full marks, and none was misread. The riders sit astride the plank now, and in the three pictures of two children no reader remarks on it; the man on the low end still draws a remark in two of his three. The vest, the castle and the reel drew none. 63 of 64 templates pass, as in v0.30, and the one failure, `jump` (0.83), is one half mark on a picture unchanged since v0.30, where it read in full.

The screen says less than it seems to. Each of its nine readers wrote fewer remarks than the fewest of v0.30's, and on the 12 pictures identical in both screens remarks fell from 65 to 45 with nothing changed. Two of the three scorers gave nothing under full marks. So the fall in remarks, from 5.19 a picture to 3.51, is the readers, and a remark that went away on a drawing not changed shows only that. What stands is what a picture's own words say, and the seesaw's are the plainest: five of v0.30's six seesaw pictures drew a remark on the plank, and two of v0.31's six, both the one man.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.30 readers saw | v0.31 |
|---|---|
| The seesaw: "the man's legs appear to go through or around the plank" | Each rider drawn in two pieces, the leg further from the viewer behind the plank and the rest in front, and raised so the hips rest on it. Plank remarks in 2 of 6 seesaw pictures, against 5 of 6, both of them the man on the low end, and none in the three pictures of two children |
| The vest: "a jagged edge against the white shirt" | Wider than the shirt, so the shirt cannot come through. The man is in 13 pictures, and no reader remarks on his vest |
| The castle: "the hand and castle merge a little" | Further from the spade, so the hand and the spade show: "probably a toy spade, next to the castle" |
| The reel: "partly overlapping the edge of the flower bed" | Moved down and to the left, clear of the bed and the step. No remark in its 10 pictures |
| Washing under storm clouds: "taking it down because of the coming storm" | No washing hung under a dark sky. 1.00 in three pictures, though one reader still offers that he may be taking it down, under a clear sky |

Left as they were: the fish's limb, which a redraw on the bench made worse, and which comes off the list; the cone, where the bench found nothing to choose; the walker's book and the feed bag. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, a wind that reaches only some things.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v031.md`, two rounds, 42 cut-outs, 19 readers). The variants are behind `SEESAW31`, `RIDE31`, `CASTLE31` and `LIMB31` in `scenegen/templates.py`, `REEL31` in `scenegen/settings.py`, and `TPDB_VEST` and `TPDB_CONE` in the cast; the release builds with the chosen ones. The seesaw needed the renderer to cut a rider in two (`split_leg` in `assets/render_assets.py`): a pose name with `~near` draws the figure without the leg further from the camera, and `~far` that leg alone, in the same frame. The far leg behind the plank read no better on its own, because the hips still lay over the plank; raised as well, the children sat on it. A seat on the plank added a thing to explain and read no better. The vest needed only its size, and the castle only a step further from the spade, which had been drawn all along behind it.

## Design tests

After the bench, the new drawings were read blind in whole test scenes among other events (`vision/design_tests_v031.md`, six pictures, six readers). Two children on the seesaw drew nothing on how they sit. Both men on its low end still did: "the plank seems to pass behind or through his legs and lower body". The moved reel drew nothing on the bed or the step in two gardens, and the vest nothing. With the washing under a clear sky, one reader still offered that the man "could be hanging the T-shirt up, or taking it down off the line". No reading called for a new rule.

## Placement revision 29

Every record stores the placement revision it was made with. v0.31 pictures use revision 29, which adds to those of revisions 1 to 28 riders astride the seesaw, in two pieces and raised onto the plank; the castle further from the spade; the reel down and to the left; and washing hung only under a clear sky. The cast is v0.30's with the vest widened (builder 0.31.0).

The park, street and playground tier-4 cells placed on v0.30's seeds. The garden's did not, with the reel moved and no washing under a dark sky, and 13 seeds failed before one placed. The tier-3 garden came from a seed search past its showcase seed. The tier-4 isomorph took 12 failed attempts. The first probe pass left `walk_dog` and `dog_begs` short, and two more probes filled them. All 71 records rebuild identical to the pixel.

The planner's difficulty priors are the calibration measured on the v0.31 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.30. Almost nothing moved: 5 fields in 2 templates by 0.002 or more, the stopped hose's and the heavy seesaw's.

## The twenty-eighth blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 50 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.30.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) | v0.25 (21 pictures) | v0.26 (21 pictures) | v0.27 (21 pictures) | v0.28 (21 pictures) | v0.29 (21 pictures) | v0.30 (21 pictures) | v0.31 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 | 0.98 | 0.95 | 0.95 | 0.88 | 0.98 | 0.99 | 1.00 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.99 | 0.98 | 0.99 | 0.99 | 1.00 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 | 0 of 286 | 0 of 289 | 0 of 283 | 0 of 284 | 0 of 285 | 0 of 284 |
| Oddities per picture, as logged by the scorers | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 | 2.6 | 2.6 | 2.2 | 2.0 | 2.3 | 2.3 | 0.6 |
| Readers' remarks per picture (recounted in v0.26) | 8.8 | 5.4 | 6.4 | 4.8 | 4.7 | 4.8 | 4.9 | 4.4 | 4.3 | 4.4 | 4.4 | 4.4 | 3.9 | 3.9 | 4.4 | 4.0 | 4.0 | 3.9 | 4.2 | 3.9 | 5.6 | 5.9 | 5.3 | 5.8 | 5.1 | 5.2 | 5.2 | 3.5 |

Across all 71 pictures 783 of 784 scored items had full marks. One had a half mark and none was misread: a child jumping for joy, who "could be trying to reach the ball or just cheering". Two of the three scorers gave no item under full marks, in 236 and 253 items, and each listed what it had credited in full with a caveat, such as a bird "about to take it" marked as pecking. The set's headline is all items 0.998 (0.989 in v0.30), with things at 1.00, actions at 0.996, inferences at 1.00 and contradictions at 1.00.

**A second retest.** 12 pictures, 11 of the set's and one probe, were identical to the pixel in v0.30 and v0.31. 137 of their 141 items scored the same: three moved up by a half mark and one down, the `jump` item that is the gate's one failure.

**Remarks fell to 3.51 a picture from 5.19, 249 on 71 pictures, and that is the readers.** Each of the nine wrote fewer than the fewest of v0.30's nine (2.62 to 4.43 a picture, against 4.50 to 6.12), and on the 12 identical pictures remarks fell from 65 to 45. On v0.30's 19 identical pictures they had held, 106 and 108, so a screen's readers can leave the row alone or move it by a third. The scorers' oddity row fell with it, to 0.6 a picture. Neither row says anything about this release's drawings, and the plank is read picture by picture instead: five of v0.30's six seesaw pictures drew a remark on the plank and the riders, and two of v0.31's six, both the man on the low end.

What this release redrew, the washing, and the one that failed (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.30 | v0.31 | v0.31 meaning items |
|---|---|---|---|
| `seesaw` | 1.00 (6 items) | 1.00 (6 items) | — |
| `seesaw_heavy` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `sandbox` | 1.00 (4 items) | 1.00 (3 items) | — |
| `hang_laundry` | 0.83 (3 items) | 1.00 (3 items) | — |
| `jump` | 1.00 (3 items) | 0.83 (3 items) | — |

Both seesaw templates hold at 1.00 with their riders astride. `sandbox` holds with the castle moved. `hang_laundry` is back to 1.00 with the washing under a clear sky. `jump`, not redrawn, is the one failure, on a picture that came back unchanged.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 | v0.27 | v0.28 | v0.29 | v0.30 | v0.31 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 | 61 | 59 | 63 | 61 | 64 | 63 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 | 3 | 5 | 1 | 3 | 0 | 1 | 1 |

Every template was screened in at least three pictures (52 in three, 4 in four, 5 in five, 2 in six and one in nine), and 63 of 64 pass, as in v0.30. The failure is one half mark among three items, on a picture identical to v0.30's, where that item had full marks: the retest's one move downward. The gate is a filter, and the pilot with people is the test of difficulty.

Templates that did not pass (`vision/flaws_v031.md` gives what the readers saw and the next fix):

| Template | v0.31 mean | Pictures | Misreads |
|---|---|---|---|
| `jump` | 0.83 (3 items) | 3 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.777 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.772 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s1031 | 4 | 0 (0) | 3 | 0.776 | — | 12 | 0.043 | birds flying, jump, run |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.772 | — | 14 | 0.033 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.711 | 0.417 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_garden_s8118_iso (isomorph of T2_playground_s042) | 8 | 1 (0) | 3 | 0.708 | 0.393 | 19 | 0.043 | kite in tree, swing, rake |
| T2_park_s022 | 8 | 1 (0) | 4 | 0.709 | 0.410 | 19 | 0.028 | kite in tree, push stroller, carry box, dog sleeping |
| T2_street_s1032 | 8 | 1 (0) | 4 | 0.711 | 0.366 | 20 | 0.050 | cat stalks bird, wave, carry bag, read bench |
| T2_street_s14109_iso (isomorph of T2_park_s022) | 8 | 1 (0) | 4 | 0.708 | 0.430 | 16 | 0.051 | about to trip, drink bench, carry bag, photo |
| T2_playground_s042 | 8 | 1 (0) | 3 | 0.709 | 0.394 | 16 | 0.035 | lost balloon, slide, carry box |
| T3_garden_s413 | 12 | 2 (0) | 6 | 0.656 | 0.309 | 23 | 0.043 | blocked hose, rain coming, cat on fence, swing, play catch, paint fence |
| T3_park_s2023 | 12 | 3 (0) | 6 | 0.640 | 0.307 | 23 | 0.031 | lost balloon, ball in tree, cat stalks bird, ice cream, dig, balloon |
| T3_street_s18133 | 12 | 2 (0) | 5 | 0.667 | 0.357 | 21 | 0.054 | about to trip, dog begs, water flowers, photo, bird perched |
| T3_street_s6104_iso (isomorph of T3_park_s2023) | 12 | 3 (0) | 6 | 0.642 | 0.313 | 21 | 0.051 | about to trip, lost balloon, dog begs, birds flying, bird perched, sweep |
| T3_playground_s1043 | 12 | 2 (1) | 5 | 0.659 | 0.341 | 22 | 0.040 | ice cream drop, dog reading, birds flying, drink bench, fly kite |
| T3_playground_s19102_iso (isomorph of T3_street_s18133) | 12 | 2 (0) | 5 | 0.667 | 0.342 | 21 | 0.037 | lost balloon, cat stalks bird, bird perched, drink bench, fly kite |
| T4_garden_s414896 | 18 | 5 (2) | 8 | 0.568 | 0.223 | 28 | 0.050 | kite in tree, bird steals, blocked hose, bucket hat, square wheel, dog sleeping, rake, cat on fence |
| T4_park_s728923 | 18 | 5 (2) | 8 | 0.566 | 0.254 | 30 | 0.037 | ice cream drop, ducks bread, kite in tree, dog reading, pan watering, birds flying, goat grazing, sweep |
| T4_street_s447752 | 18 | 5 (2) | 9 | 0.571 | 0.213 | 27 | 0.058 | bird steals, about to trip, ball in tree, dog reading, water upward, birds flying, sweep, jump, carry bag |
| T4_street_s26111_iso (isomorph of T4_playground_s460662) | 18 | 5 (2) | 9 | 0.572 | 0.237 | 27 | 0.057 | bird steals, ball in tree, about to trip, square wheel, dog reading, bird perched, wave, sweep, ice cream |
| T4_playground_s460662 | 18 | 5 (2) | 9 | 0.558 | 0.232 | 27 | 0.043 | bird steals, kite in tree, lost balloon, square wheel, dog reading, run, photo, dog playing, birds flying |

Isomorph pairs differ by at most 0.014 in content and 0.020 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 26,188 | 27 | 11,581 | 10^12.7 |
| garden | 3 | 2,394,371 | 296 | 321,073 | 10^18.4 |
| garden | 4 | 71,996,856 | 565 | 5,886,606 | 10^23.4 |
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

In all 412,600,375 structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.

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
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts; from v0.31 a pose name with `~near` or `~far` draws a figure in two pieces at its far leg) |
| `assets/blender_run.py` | Lets the `bpy` scripts run with plain `python`, inside an installed Blender where the `bpy` module is missing |
| `assets/validate_assets.py` | Checks for every rendered variant |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, and v0.31 widens the vest |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out031/` | The 18 `.blend` families (builder 0.31.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib031/` | Every variant the generated scenes and probes use, carried over from `lib030` or rendered from `out031` |
| `assets/cast/gallery031/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (175, all pass the validator) |
| `scenegen/` | The generator (0.31.0, placement revision 29); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`); `library.py` the shadow's two (`SHADOW28`) and the sleeper's wider one (`SHADOW29`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.31 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v031.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v031.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v031.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all twenty-eight screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out031                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out031 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s2023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v031   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v031 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery031 --old-gallery <v0.30 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.31 --single   # the release as one zip, tpdb_v0.31.zip
```

The release is one zip, `tpdb_v0.31.zip`, about 180 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.30 record rebuilds with the v0.30 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- One template falls under the legibility gate after the v0.31 screen, `jump` (0.83), on one half mark among three items, on a picture unchanged since v0.30, where that item had full marks. 63 of 64 pass.
  `vision/flaws_v031.md` lists this and the oddities for v0.32.
- A single half mark is noise. 19 pictures were identical to the pixel in v0.29 and v0.30, and 223 of their 230 items scored the same across fresh readers and scorers, with four templates moving by a half mark and no picture changed (`vision/flaws_v030.md`, A retest nobody planned). In v0.31, 12 pictures came back identical once more, and 137 of their 141 items scored the same; the one that went down is the gate's one failure. A template with few items can cross the gate on that alone.
- What the trip's long box costs a fresh tier-4 search is as v0.29 found it, 166 failed seeds against 80. This release's cells came back on their seeds, so it paid nothing and shows nothing new.
- The oddities come in two rows. Readers' remarks per picture are counted directly from their descriptions and compare across
  screens, with the caveat that current readers write about 18% more than the v0.23 readers on the same pictures (`vision/v024/control/`,
  one reader and eight pictures). The row was recounted in v0.26, as the counter had taken bullets saying nothing is wrong for remarks, so its
  figures differ from those published up to v0.25. The scorers' logged oddities do not compare: v0.23's logged 25% of the remarks, v0.24's 83%, and
  from v0.25 the prompt caps them at three per picture. Earlier screens did not record which model read them; v0.24's to v0.31's ran on Claude Opus 5.5. Readers differ widely: on v0.28's nine, from 4.25 to 6.38 remarks a picture, on v0.29's from 4.50 to 5.75, and on v0.30's from 4.50 to 6.12. v0.31's nine wrote from 2.62 to 4.43, every one fewer than the fewest of v0.30's, and on 12 pictures identical in both screens remarks fell from 65 to 45. So a screen's readers can move the row by a third, and its fall to 3.51 in v0.31 says nothing about the drawings.
- No reader says "teenager": he is read as a boy, a boy or young man, or a person, which the key mostly accepts. The v0.24 redraw moved him
  from a woman to a boy, and v0.26's cap worn forwards moved him no further toward the key's own word. It read once as "worn backward or sideways" in v0.27.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 71 pictures 783 of 784 scored items had full marks (872 of 877 in v0.30). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, a v0.24 scorer eleven, and all three scorers of v0.25 to v0.31 listed such calls, enough to move a template across the gate. A v0.29 scorer listed 18 items that hold full marks because the free description committed and only the unsure section hedged, and a v0.30 scorer gave nothing under full marks in 302 and listed 22 it thought a stricter scorer might halve. Two v0.31 scorers gave nothing under full marks, in 236 and 253 items, among them a bird "about to take it" credited as pecking. A misread is a call too: the
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
- The planner's priors come from the v0.31 calibration, with f = 0 and a at its centre for every inference and contradiction, as in
  v0.20 to v0.30: 5 fields in 2 templates moved by 0.002 or more, the stopped hose's and the heavy seesaw's. The ladder's still rests on one sampled placement, since v0.29's lamp rule.
- Exact rebuilds hold within a release, on the pinned Pillow: the v0.31 cast (builder 0.31.0) and placement rules (revision 29) change what is drawn at the seesaw, the castle, the reel and the bearded man's vest,
  so a v0.30 record rebuilds with the v0.30 package.
- Every variant comes from the v0.31 cast (builder 0.31.0, `out031`), which widens the vest: what the set and probes use was carried over from `lib030`, or rendered on demand on an installed Blender, the seesaw's riders in two pieces each. Some carried variants date from Linux renders, which differ from an installed Blender's
  only in sub-pixel anti-aliasing on the outlines. The library keeps only the 350 variants the v0.31 set and probes use. The bench
  variants (`TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ`, `TPDB_BEARD`, `TPDB_BROW`, `TPDB_BLUSH`, `draw.WHEEL27`, `draw.SPLAT28`, `draw.SEESAW_IN28`, `library.SHADOW28`, `library.SHADOW29`, and `SLEEP29`, `TRIP29`, `TRIP_OBJ29`, `DUCK29`, `DOOR29`, `HOSE29`, `BULGE29`, `FISH29`, `LADDER_LAMP29`, `HOSE30`, `FISH30`, `TRIP_W30`, `TRIP_LANE30`, `CRUMB30`, `SEESAW31`, `RIDE31`, `CASTLE31` and `LIMB31` in `templates.py`, `REEL30` and `REEL31` in `settings.py`, and `TPDB_VEST` and `TPDB_CONE` in the cast) stay in the code.
- The figures are still narrow. Legs an eighth shorter and limbs 14% thicker took the bench from eight remarks to three, on four cut-outs a side, but the screen's remarks on
  thin or long bodies did not fall (six pictures to eight in v0.27, to thirteen in v0.28 and v0.29, and back to six in v0.30, with nothing changed, and one in v0.31, with readers who remark less; by keyword, so that row says little). A real change of build is a larger job than these.
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
  v0.24 and v0.25, and with it from v0.26. The v0.31 isomorphs are two at tier 2, two at tier 3 and one at tier 4; the tier-4 one
  took 12 failed attempts.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- A shadow from the figure's own footprint is smaller, and a body lying down has little of it showing. The sleeping dog now reads in full on its new pose and that shadow; a wider one did little on the bench, so whether the shadow cost it marks in v0.28 is still not shown.
- The trip reads in full on the long box, in eleven pictures in v0.30 and five in v0.31. In v0.30, five of its readers also said the walker may step round it, which on the same five pictures went from four of five to one of five with nothing changed.
- The man on the seesaw's low end is drawn astride, his far leg behind the plank, and two of his three pictures still draw a remark, one that he could be "sitting just beside it with the plank behind his legs". The pose puts a knee up and a shin across a rising plank, and that is next to change. The stuck girl, raised with the rest, once "may look like she is hovering slightly".
- A rider on the seesaw is two pictures, the far leg drawn behind the plank as background and the rest of the figure in front. The far leg is in no count, mask or check of the scene's own.
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
