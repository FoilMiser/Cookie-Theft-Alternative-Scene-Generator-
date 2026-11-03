# TPDB v0.24: a teenager who looks like one, a slide with the face in view, sleepers clear of walkers' feet, read a twenty-first time

v0.23 ended with the twentieth blind screen at its ceiling: every one of 729 scored items had full marks and all 64 templates passed the gate, so what its readers still reported were oddities, and `vision/flaws_v023.md` listed them for v0.24. Above all, a sleeping cat on the path 50 px behind a walking man's back foot, "right by his feet, so he could trip over it or step on it". Going through the scorers' notes, two more stood out, both credited in full and both left as notes for the pilot in v0.23: no reader called the teenager a teenager ("a woman with a brown ponytail", 13 items), and figures at the back were "drawn as large as foreground people ... as if walking on the hilltop" (four pictures, each with the feet within 75 px of the horizon).

v0.24 works through those. The ones about how things look went to the isolation bench first, in two rounds, each drawn two or more ways and read blind on its own; the bench also found one nobody had listed, the raised arms of a child on the slide lying across the face. The rest are placement rules (revision 22). All of them were then read blind in whole test scenes among other events, the set was regenerated, and it was screened a twenty-first time.

The twenty-first screen read all 72 pictures, the set's 21 and 51 probes: 799 of 805 scored items had full marks, six had half marks, and none was misread. 63 of the 64 templates pass the gate (64 in v0.23). The teenager was named a boy in all 25 of his pictures and a woman in none; no reader put a sleeping animal at anyone's feet; no reader said a figure at the back was too large; and no reader had the child on the slide holding her head. The one failure is `carry_bag`, at 0.75: the older man's long, narrow yellow bag read as "something yellow" in two pictures from one reader. That drawing did not change in v0.24 and read in full in v0.23, so it may be variance, and it heads the list for v0.25 in `vision/flaws_v024.md`. Unintended oddities per picture rose from 1.0 to 5.2, and most of that is the instruments rather than the pictures: this release's scorers logged 83% of what the readers reported, against 22% in v0.23 (see the screen below).

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.23 readers saw | v0.24 |
|---|---|
| A sleeping cat 50 px behind a walking man's back foot: "right by his feet, so he could trip over it or step on it" | A sleeping animal kept clear of any walker's feet on both sides and in depth, not only ahead of a reading walker |
| The teenager never called a teenager: "a woman with a brown ponytail" (13 items, credited) | Redrawn on the bench (builder 0.24.0): shorter, a larger head, short hair and a red cap worn backwards. Bench readers: "a boy or young man", "a teenager or a slim adult" |
| A child on the slide with the arms raised across the face: "holding her head or hair" (and on the bench "covering the face or eyes ... upset, scared") | Redrawn on the bench: both arms up and ahead, the near one passing under the chin, the hands open toward the viewer: "sitting and sliding ... with both arms stretched up and forward" |
| A child "slightly in front of" the chute, "hovering a little above the slide" | The seat 8 px higher, on the chute's middle: "looks seated on the slide" |
| A figure at the back "drawn as large as foreground people ... as if walking on the hilltop" (four pictures) | In the park and on the playground, nobody on the ground in the 90 px of open ground before the horizon. No reader remarked on size in either setting in the design tests |

Tried and left as it was: the seesaw's riders, "perched rather than seated" in v0.23, read worse raised than where they were (bench, below). Left as they were, as notes for the pilot: water from a blocked hose that might spray the woman holding it (she is peering into the nozzle, and the reading fits), a figure at the back of the street against the shop fronts, goats in a garden or park, and the older ones (wind under a clear sky, a stall with nobody at it, sweeping a path with nothing on it).

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v024.md`, two rounds, 16 cut-outs, eight readers). The bench casts were built from the same cast library with the variants switched on (`TPDB_TEEN`, `TPDB_SLIDE`); the release cast builds with the chosen ones. The teenager with a cap worn backwards was "a boy or young man" and "a teenager or a slim adult"; with the old ponytail and an orange school backpack "a girl or young woman", the pack "a second ball", "a disc" or "shield-like". The seesaw's riders, raised 10 or 18 px, were said to "overlap the plank" or "float slightly above the seat", and where they were drew no remark, so they stayed; the 18 px drawing had looked best by eye before it was read. On the slide, the seat on the chute's middle "looks seated", 8 px below it "slightly above or in front of" and 8 px above it "hover just above". All three slide readers then said the raised arm merges with the face, which nobody had listed: arms raised out to the sides lie across the head in profile. With the arms up and ahead the child was "going down it ... as if waving or cheering", with the hands holding the chute "just sitting still". Two further candidates were dropped by eye before any reader saw them (a mop of hair; a backpack whose straps sank into the hoodie), and one refinement of the arms, which lay across the face again. The final arms were read first in the whole scenes.

## Design tests

After the bench, the new drawings and the rules of revision 22 were read blind in whole test scenes among other events (`vision/design_tests_v024.md`, six pictures, three readers): a tier-4 park with the older man and his bag, a sleeping cat and the reading walker; a playground with the teenager kicking and the riders on the seesaw; a park with the teenager's ice cream, a sleeping dog, a walker and a runner; a tier-4 street with the teenager as photographer, a flying cap and a bucket for a hat; a garden with the teenager catching and a sleeping cat behind a walker; and a playground with the other child on the slide. The teenager was named a boy in three pictures and "a boy or an adult" in the fourth, and no reader called him a woman. No reader put a sleeping animal at anyone's feet, none remarked on the size of a figure at the back in the park or on the playground, and the child on the slide was "sitting and sliding to the right, with both arms stretched up and forward". No new rule came out of them, so there was no second round. One remark stays a note for the pilot: a woman against the street's shop fronts "looks large compared with the door"; revision 22 leaves the street alone, as its tier-4 cell is already the hardest to place.

## Placement revision 22

Every record stores the placement revision it was made with. v0.24 pictures use revision 22, which adds the rules above to those of revisions 1 to 21: a sleeping animal clear of the ground round any other event's walker's feet, 170 px either side of them and in depth; and in the park and on the playground, nobody on the ground within 90 px of the horizon. The seat on the slide and the teenager's cap (kept out of the windy-hat picture, which casts someone bareheaded) are also gated on it. The cast is builder 0.24.0.

Building and inspecting the set and the probes found nothing more to fix. The tier-4 garden and park placed again on their v0.23 seeds with the same events, the cat now clear of the man. The tier-4 street came from a search from its v0.23 seed after eight failed seeds (33 in v0.22). The tier-4 playground took four searches side by side and 25 failed seeds, the tier-3 playground needed the unsteered search after 13 failed seeds under template-variety steering, and the tier-4 isomorph took about 230 tries over four batches: the strip before the horizon leaves the playground, already the tightest setting, less room. The set's isomorphs are two at tier 2, two at tier 3 and one at tier 4. All 72 records rebuild identical to the pixel.

The planner's difficulty priors are the calibration measured on the v0.24 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.23. The giant fork's cue salience moved by -0.013; every other template's by at most 0.001, as the redrawn templates' scored cues did not change.

## The twenty-first blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 51 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.23.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 |

Across all 72 pictures 799 of 805 scored items had full marks, and none was misread (729 of 729 in v0.23). The six half marks: the older man's bag, twice; a grandmother who "might walk into" a bucket; a teenager with the giant fork "as if using it as a shovel or broom"; a girl pointing "at the bird or at the man" rather than the sky; and a square wheel also offered as "a wheel seen oddly". The scorers listed the close calls they credited in full, eleven in one scorer's part alone; a stricter scorer would have given some of them half points.

**The oddity row does not compare across this release.** Logged oddities rose from 21 to 110 in the set and from 42 to 227 in the probes. The prompts are unchanged, but they do not say how much to log: v0.23's scorers logged 22% of what the readers wrote in their "unsure" sections, and v0.24's 83%. Readers wrote 31% more such remarks per picture (5.67, was 4.32). As a control, one current reader described eight unchanged v0.23 pictures, blind, and wrote 15% more than the v0.23 readers had on the same pictures (`vision/v024/control/`). The rest of that rise could be the pictures, their mix or that one reader's sample of eight, so nothing is claimed either way about oddities overall. The control does separate the drawings from the readers on the named items: the same current reader called the old teenager "woman in blue hoodie ... brown ponytail" in all six of the eight pictures he is in, and said of the old picture's sleeping cat that it "could trip up the walkers". What the v0.24 readers noticed instead: stiff, narrow figures with small hands, about a third of all reports; a large oval shadow under the wheelbarrow; a paint roller barely touching the fence; a bird oversized at the sandwich; and the older ones (goats, wind with nothing else blowing, strings ending in mid-air, a slide's chute hovering above the grass).

The templates whose drawing or placement v0.24 changed (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.23 | v0.24 | v0.24 meaning items |
|---|---|---|---|
| `kick_ball` | 1.00 (3 items) | 1.00 (3 items) | — |
| `play_catch` | 1.00 (6 items) | 1.00 (6 items) | — |
| `slide` | 1.00 (3 items) | 1.00 (3 items) | — |
| `cat_sleeping` | 1.00 (3 items) | 1.00 (4 items) | — |
| `dog_sleeping` | 1.00 (3 items) | 1.00 (3 items) | — |
| `carry_bag` | 1.00 (3 items) | 0.75 (4 items) | — |
| `windy_hat` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `bucket_hat` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (6) |

Every template in the table read in full but one. The teenager's templates held their scores while his name changed, as the key's accepted answers include "boy" and v0.23 had credited "woman" for the action alone: the gain is in who readers said he was, which the score does not show. No reader volunteered "teenager". The older man's bag fell from 1.00 to 0.75 and fails the gate, though neither the bag nor the rule set around it changed in a way that touches the drawing.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 |

Every template was screened in at least three pictures (49 in three, 6 in four, 7 in five, 2 in six), and 63 of 64 pass. The v0.9 retest put the gate's reader variance at about five templates between screens, and the scores are near the ceiling: the pilot with people is the test of difficulty.

Templates that did not pass (`vision/flaws_v024.md` gives what the readers saw and the next fix):

| Template | v0.24 mean | Pictures | Misreads |
|---|---|---|---|
| `carry_bag` | 0.75 (4 items) | 4 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.780 | — | 13 | 0.038 | drink bench, rake, wave |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.773 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s031 | 4 | 0 (0) | 2 | 0.780 | — | 14 | 0.045 | photo, water flowers |
| T1_playground_s1041 | 4 | 0 (0) | 2 | 0.783 | — | 14 | 0.030 | play catch, slide |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.711 | 0.393 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_garden_s6118_iso (isomorph of T2_playground_s042) | 8 | 1 (0) | 4 | 0.724 | 0.378 | 20 | 0.039 | dog begs, cat on fence, paint fence, dog playing |
| T2_park_s022 | 8 | 1 (0) | 4 | 0.711 | 0.370 | 16 | 0.025 | ice cream drop, fly kite, carry box, dog sleeping |
| T2_street_s2032 | 8 | 1 (0) | 4 | 0.710 | 0.370 | 16 | 0.046 | ice cream drop, carry bag, jump, push stroller |
| T2_street_s6109_iso (isomorph of T2_park_s022) | 8 | 1 (0) | 4 | 0.711 | 0.368 | 18 | 0.048 | ice cream drop, photo, birds flying, carry bag |
| T2_playground_s042 | 8 | 1 (0) | 4 | 0.706 | 0.372 | 17 | 0.035 | cat stalks bird, dog playing, ice cream, sandbox |
| T3_garden_s16013 | 12 | 3 (0) | 6 | 0.637 | 0.336 | 21 | 0.041 | about to trip, kite in tree, dog begs, hose water, bird perched, cat on fence |
| T3_garden_s8102_iso (isomorph of T3_street_s22133) | 12 | 3 (0) | 6 | 0.658 | 0.307 | 22 | 0.041 | about to trip, bird steals, kite in tree, birds flying, plant flowers, dog sleeping |
| T3_park_s5023 | 12 | 2 (0) | 4 | 0.660 | 0.362 | 20 | 0.031 | sprinkler package, ball in tree, kick ball, ice cream |
| T3_street_s22133 | 12 | 3 (0) | 6 | 0.667 | 0.315 | 20 | 0.049 | rain coming, bird steals, about to trip, walk dog, run, balloon |
| T3_street_s12104_iso (isomorph of T3_park_s5023) | 12 | 2 (0) | 4 | 0.667 | 0.360 | 20 | 0.048 | ball in tree, lost balloon, bird perched, feed birds |
| T3_playground_s14043 | 12 | 3 (1) | 6 | 0.640 | 0.298 | 20 | 0.034 | dog begs, kite in tree, bucket hat, cat sleeping, birds flying, play catch |
| T4_garden_s327962 | 18 | 5 (2) | 8 | 0.569 | 0.236 | 29 | 0.044 | paint tracks, lost balloon, cat stalks bird, dog reading, fish in tree, read bench, birds flying, cat sleeping |
| T4_park_s242971 | 18 | 5 (1) | 8 | 0.584 | 0.239 | 26 | 0.034 | ball in tree, lost balloon, bird steals, ducks bread, dog reading, ice cream, carry bag, cat sleeping |
| T4_street_s622941 | 18 | 5 (2) | 9 | 0.571 | 0.222 | 26 | 0.058 | about to trip, ball in tree, dog begs, water upward, dog reading, carry bag, sweep, bird perched, birds flying |
| T4_street_s42111_iso (isomorph of T4_playground_s1012995) | 18 | 5 (2) | 9 | 0.566 | 0.202 | 27 | 0.056 | about to trip, bird steals, ice cream drop, water upward, dog reading, sweep, carry box, birds flying, balloon |
| T4_playground_s1012995 | 18 | 5 (2) | 9 | 0.566 | 0.218 | 26 | 0.043 | ball in tree, bird steals, ice cream drop, sitting on air, dog reading, cat sleeping, bird perched, photo, carry box |

Isomorph pairs differ by at most 0.018 in content and 0.016 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 26,666 | 27 | 11,977 | 10^12.7 |
| garden | 3 | 2,497,856 | 296 | 338,691 | 10^18.4 |
| garden | 4 | 78,307,591 | 565 | 6,485,763 | 10^23.1 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 46,656 | 24 | 20,579 | 10^11.6 |
| park | 3 | 5,825,387 | 236 | 1,027,898 | 10^17.1 |
| park | 4 | 335,129,874 | 376 | 44,950,328 | 10^23.2 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,433 | 24 | 2,952 | 10^11.8 |
| street | 3 | 440,799 | 220 | 70,459 | 10^17.2 |
| street | 4 | 7,157,106 | 330 | 947,071 | 10^22.5 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.5 |
| playground | 3 | 749,671 | 183 | 113,624 | 10^17.9 |
| playground | 4 | 10,690,061 | 232 | 1,352,842 | 10^21.9 |

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.24 redraws the teenager and the slide's arms, and keeps the bench variants behind `TPDB_TEEN` and `TPDB_SLIDE` |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out024/` | The 18 `.blend` families (builder 0.24.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib024/` | Every variant the generated scenes and probes use, carried over from `lib023` where the cast did not change or rendered from `out024` |
| `assets/cast/gallery024/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (170, all pass the validator) |
| `scenegen/` | The generator (0.24.0, placement revision 22); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`) and the riders' bench offsets (`RIDE24`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.24 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v024.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v024.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v024.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all twenty-one screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out024                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out024 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s5023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_TEEN=A> python vision/isolation_bench.py tpdb_work/bench teenA_1 teenA_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v024   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v024 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery024 --old-gallery <v0.23 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.24 --single   # the release as one zip, tpdb_v0.24.zip
```

The release is one zip, `tpdb_v0.24.zip`, about 162 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.23 record rebuilds with the v0.23 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. All 21 v0.23 records rebuilt on Windows with identical SVGs: 18 were identical to the pixel, and the other three differed by one level on at most 96 of 1.6 million pixels, the rounding of a newer cairo. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so `lib024` mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- One template falls under the legibility gate after the v0.24 screen: `carry_bag` (0.75, two half marks from one reader on an
  unchanged drawing). 63 of 64 pass. `vision/flaws_v024.md` lists it and the oddities the readers reported for v0.25.
- The oddity figures do not compare across v0.24: its scorers logged 83% of the readers' remarks, v0.23's 22%, under the same
  prompt, and a current reader wrote 15% more than the v0.23 readers on eight unchanged pictures (`vision/v024/control/`). The
  control is one reader and eight pictures. Earlier screens did not record which model read them; v0.24's ran on Claude Opus 5.5.
- No reader says "teenager": the v0.24 redraw is read as a boy in all 25 pictures, which the key accepts, and in the
  isolation bench once as "a teenager or a slim adult". The redraw moved him from a woman to a boy, not to the key's own word.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 72 pictures 799 of 805 scored items had full marks (729 of 729 in v0.23). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, and a v0.24 scorer eleven, enough to move a template across the gate.
- Tier-4 pictures are the hardest to place, and revisions 14 to 22 make them harder (walkers' and runners' lanes, pointing
  lines, feet off benches and off other events' things, the photographer's line of sight, the waver's clear hand, body gaps, the gap
  from thin parts, heads clear of figures up to 80 px apart in depth, the ground clear past a reading walker's obstacle, jumpers in the
  front half, an obstacle a full step ahead, runners clear of other movers, ducks off a float, sleepers clear of walkers' feet, nobody in
  the strip before the horizon). The tier-4 garden and park came again on their v0.23 seeds with the same events; the street took a
  search of eight failed seeds; the playground, 25 failed seeds across four searches side by side. Their records rebuild them exactly.
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
- The planner's priors come from the v0.24 calibration, with f = 0 and a at its centre for every inference and
  contradiction, as in v0.20 to v0.23: the giant fork's cue salience moved by -0.013, every other template's by at most 0.001.
- Exact rebuilds hold within a release, on the pinned Pillow: the v0.24 cast (builder 0.24.0) and placement rules (revision 22) change how
  the teenager and the child on the slide look and where events go, so a v0.23 record rebuilds with the v0.23 package.
- Every variant comes from the v0.24 cast (builder 0.24.0, `out024`): the variants of the families and poses v0.24 did
  not change were carried over from `lib023` (rendered on Linux), the rest rendered anew with an installed Blender on Windows, whose
  renders differ only in sub-pixel anti-aliasing on the outlines. The library keeps only the 379 variants the v0.24 set and probes
  use. The bench variants (`TPDB_TEEN`, `TPDB_SLIDE`, `draw.RIDE24`) stay in the code, off by default.
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
- The strip before the horizon leaves the playground less room: the tier-3 playground placed only without template-variety steering,
  and no tier-3 isomorph came from it. The v0.24 isomorphs are two at tier 2, two at tier 3 and one at tier 4.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
