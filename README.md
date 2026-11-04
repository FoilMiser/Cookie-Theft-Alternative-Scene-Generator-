# TPDB v0.27: faces turned to the viewer, a broom that is a broom, read a twenty-fourth time

v0.26 ended with five gate failures: `sweep` at 0.67, with a fan of bristles read as "a long yellow-headed rake", the one misread; `ice_cream` at 0.83 ("looking at or eating it"); `photo` at 0.83 ("binoculars or a camera"); `about_to_trip` at 0.89, its obstacle off the walker's line; and `sprinkler_package` at 0.89 ("a wooden crate standing in a puddle"). Its oddities were led by a seesaw's plank through its sitter, a stiff hose and faces hidden by a tilted head, and the tier-4 playground had taken 89 failed seeds, for a reason not traced.

v0.27 works through those. Looking closely at crops before drawing anything changed the list: the walkers' feet did point the right way, the hose did reach the fist, and in full profile the eye sits on the head's outline, whichever face it is. Each change went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a twenty-fourth time, on a slightly shorter, thicker cast.

The twenty-fourth screen read all 67 pictures, the set's 21 and 46 probes: 743 of 756 scored items had full marks, and none was misread. The gate recovered: 63 of the 64 templates pass, against 59, and all five of v0.26's failures pass. `sweep` went from 0.67 to 1.00, with no reader saying rake, and `ice_cream` to 1.00 in 13 pictures. How much of that is the drawings is not cleanly separated: `photo` recovered without being changed, and the v0.9 retest put the gate's reader variance at about five templates. The one failure, `dog_begs` at 0.89, is on a drawing this release did not change, as readers were unsure whose food the dog wants. Readers' remarks per picture went the other way, up 10% from 5.27 to 5.81, across all the readers. Remarks on hidden faces fell by half, the main aim of the release, while remarks on shadows and on marks on a face rose. The shorter legs, which looked good on a small bench sample, did not reduce the remarks on thin figures in whole pictures. And the tier-4 playground was not found by search at all: 219 free seeds placed nothing, so it uses the v0.26 picture's template set.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.26 readers saw | v0.27 |
|---|---|
| `sweep`'s fan of bristles: "a long yellow-headed rake", that screen's one misread (0.67) | Bristles dense and nearly parallel, with two bindings at the neck (builder 0.27.0). Read beside a rake on the bench: "a long-handled rake", "a yellow-bristled broom". No reader said rake of it in its three screened pictures: 1.00 |
| Faces in full profile: "the face is mostly turned away and hidden", with the eye on the head's outline | The head turned 35 degrees to the viewer in every pose of a person in full profile, as a twin of the pose; a pose with a hand-held thing at the face keeps its profile. Remarks on a face hidden or hard to read fell from 22 pictures to 10, by keyword |
| `about_to_trip`: "his head and arms face left", "his legs and feet look like they stride towards the right" (0.89) | The back heel lifted, on its toe, with the head turned. The trip was offered unprompted in all four pictures, "he may be about to walk into or trip over it": 0.96. The obstacle's line still draws remarks ("headed roughly past it") |
| `ice_cream`: "looking at or eating it" (0.83) | The scoop at the lips. 1.00 in 13 pictures |
| `sprinkler_package`: "a wooden crate standing in a puddle" (0.89) | Two short drips from the lid in place of long ones. "The box looks like it is getting soaked": 1.00 |
| `photo`: "binoculars or a camera" (0.83) | Not changed. 1.00, so the half mark was probably reader variance |
| The bird at the ground: "a bird toppling forward", its tail "a party hat or a funnel" | The body less tipped, the head in front of it, an eye on its side: "pecking at seeds" |
| The bicycle: "solid black disc wheels" | Spokes, and no remark on its wheels |
| The dress: "two separate yellow shapes" at the waist | A thin belt at the join. A yellow dress in 16 of 18 pictures; both others are the pose sitting on air |
| A mouth near the edge of the face read as "a small beard or moustache" | The line thinner and in a lip colour. No moustache in 67 pictures |
| Narrow figures: "long thin legs" | Legs an eighth shorter and limbs 14% thicker. The bench went from eight remarks to three, on four cut-outs a side. The screen's remarks did not fall |
| The hose: "like a stiff loop standing in the air" | Hanging from the fist in a slack hook. Fewer remarks, but still "almost like a pipe" in one picture |
| The tier-4 playground's 89 failed seeds, not traced | Traced as far as this: the placement rules are not the cause, nor the room, but which sets of events the planner draws (below) |

Left as they were: the seesaw's plank, looked at closely on the bench, as the leg does lie over it; the leaf clumps over a caught kite; water; the roller's head. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, a wind that reaches only some things.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v027.md`, two rounds, 51 cut-outs, 20 readers). The bench casts were built from the same cast library with the variants switched on (`TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ`, `TPDB_BEARD`); the release cast builds with the chosen ones. The broom took two rounds: dense flared bristles were still "a long-handled broom or rake with a yellow fanned head", and a yard broom "a broom or a rake-like tool", so round 2 narrowed them to nearly parallel, and all four cut-outs said broom, one of them beside a rake. With the head turned and the heel lifted the trip was offered unprompted in both cut-outs and in neither of the old, though the two changes were not separated. The scoop at the mouth was first "smelling it like a flower", so it went lower. The bench also found what nobody had listed: a hand past the edge of the book, and a mouth read as a beard. The bearded man's beard read as "a dark face covering or mask", and now stops short of the ear.

## Design tests

After the bench, the new drawings were read blind in whole test scenes among other events (`vision/design_tests_v027.md`, six pictures, three readers). The broom and a rake stood in one picture, "sweeping a small pile of orange, yellow and red leaves with a straw broom" beside "raking a small pile of green and brown leaves". The walker with the book was "not looking where they are going". The soaked box was read inference and all, "so whatever is inside looks likely to get ruined", and the sitter off the path as "impossible". No beard read as a mask or a strap in these six, though the screen later found two. Two small fixes came out of them and were not read again: a shadow under a ball in a walker's way ("it looks slightly as if it is floating"), and a seated adult's feet closer in, as the thigh is shorter ("he looks as if he is sliding"). The hose still read as "a pole or stand" at first, and was left.

## Placement revision 25

Every record stores the placement revision it was made with. v0.27 pictures use revision 25, which adds to those of revisions 1 to 24 the hose's slack hook to the fist, the lumpy heap beside a hole, the sitter on air kept clear of the path, a duck's wake kept on the pond, and a shadow under a ball in a walker's way. The turned heads, the lifted heel, the broom, the scoop, the hand on the book, the mouth, the shorter figure, the belt, the beard and the pecking bird are in the cast (builder 0.27.0), and the spoked wheel and the short drips in `draw.py`.

Building and inspecting the set and the probes found one thing this release could not search its way past. The tier-4 garden placed again on its v0.26 seed, the park took 24 failed seeds and the street 14, each across three searches side by side, and the tier-3 street one search seed past its showcase seed. The tier-4 playground did not come at all: 219 free seeds across six searches placed nothing. The same 24 seeds under revisions 23, 24 and 25 failed with almost the same counts (`about_to_trip` named 378, 379 and 379 times), so the rules added since v0.25 are not the cause. The template sets that placed in v0.24, v0.25 and v0.26, forced, each placed within seconds on one of two seed lists, so the room is not the cause either: the planner keeps drawing sets of nine events that cannot fit this setting. Why that got worse after v0.25 is still not shown, and `vision/flaws_v027.md` has what to test next. This release's tier-4 playground is the v0.26 picture's template set, forced (`regen.forced`), so it repeats v0.26's events. The tier-4 isomorph took 123 failed attempts (676 in v0.26). The set's isomorphs are two at tier 2, two at tier 3 and one at tier 4. All 67 records rebuild identical to the pixel.

The planner's difficulty priors are the calibration measured on the v0.27 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.26. The trip's cue salience moved by -0.034 and the heavy seesaw's by +0.032, the two largest, with the figures' new heads and legs; 39 fields in 14 templates moved by 0.002 or more.

## The twenty-fourth blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 46 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.26.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) | v0.25 (21 pictures) | v0.26 (21 pictures) | v0.27 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 1.00 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 | 0.98 | 0.95 | 0.95 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.99 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 | 0 of 286 | 0 of 289 |
| Oddities per picture, as logged by the scorers | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 | 2.6 | 2.6 | 2.2 |
| Readers' remarks per picture (recounted in v0.26) | 8.8 | 5.4 | 6.4 | 4.8 | 4.7 | 4.8 | 4.9 | 4.4 | 4.3 | 4.4 | 4.4 | 4.4 | 3.9 | 3.9 | 4.4 | 4.0 | 4.0 | 3.9 | 4.2 | 3.9 | 5.6 | 5.9 | 5.3 | 5.8 |

Across all 67 pictures 743 of 756 scored items had full marks. Five had half marks, eight were missed, and none was misread. The eight missed items are all things in probes, six "a few white clouds" and two "there is a tree", and one reader, of pictures 9 to 16, names no cloud and no sun in any of its eight pictures, which accounts for seven of them. The half marks are on meaning: the dog that begs, twice ("could be hers, begging from her bag, or could be doing its own trick"); the trip, once ("headed roughly past it"); the teenager with the fork ("I am not sure what the boy is doing with it"); and the dog at the door ("or could just be an odd pose"). The set's headline is all items 0.993 (0.988 in v0.26), with things and contradictions at 1.00, actions at 0.996 and inferences at 0.950, on three half marks.

**Remarks went up, 389 against 353.** They are spread across the readers, on the same model and prompts as v0.26, so this release did not make the pictures read as cleaner in general. `vision/remark_topics.py` sorts them roughly by keyword. A face hidden or hard to read fell from 22 pictures to 10, the release's main change. Shadows rose from 13 to 20 with nothing changed ("a very wide oval, much wider than the puppy"), and marks on a face from 4 to 9, as faces are more on view ("dark marks around her nose and mouth"). Thin or long bodies went from 6 to 8, where the bench had suggested a fall: whole pictures did not confirm that small bench sample. Water drawn solid went from 2 to 0 with nothing changed, which shows the size of this count's noise.

The five that failed in v0.26, and the one that fails now (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.26 | v0.27 | v0.27 meaning items |
|---|---|---|---|
| `sweep` | 0.67 (3 items) | 1.00 (3 items) | — |
| `ice_cream` | 0.83 (6 items) | 1.00 (13 items) | — |
| `photo` | 0.83 (3 items) | 1.00 (3 items) | — |
| `about_to_trip` | 0.89 (9 items) | 0.96 (12 items) | 0.88 (4) |
| `sprinkler_package` | 0.89 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `dog_begs` | 1.00 (9 items) | 0.89 (9 items) | 0.67 (3) |

`sweep` and `ice_cream` read in full on their redraws. `about_to_trip` rose with the lifted heel and the turned head, its meaning item from 0.67 to 0.88, and was offered in all four pictures, though the obstacle's line still draws remarks. `sprinkler_package` read in full with its short drips and no crate. `photo` was not changed and read in full, as the v0.26 list guessed. `dog_begs` is the one failure, and it read in full in v0.26 on the same drawing, so placement is the first thing to try.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 | v0.27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 | 61 | 59 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 | 3 | 5 | 1 |

Every template was screened in at least three pictures (54 in three, 6 in four, 1 in five, 2 in six, 1 in thirteen), and 63 of 64 pass, up from 59. `dog_begs` fails on two half marks in three pictures, and read in full where the dog sits right beside the eater. The v0.9 retest put the gate's reader variance at about five templates between screens, about the size of this recovery, so it is good news without being a measure of what the drawings gained. The gate is a filter, and the pilot with people is the test of difficulty.

Templates that did not pass (`vision/flaws_v027.md` gives what the readers saw and the next fix):

| Template | v0.27 mean | Pictures | Misreads |
|---|---|---|---|
| `dog_begs` | 0.89 (9 items) | 3 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.777 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.772 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s1031 | 4 | 0 (0) | 3 | 0.776 | — | 12 | 0.043 | birds flying, jump, run |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.771 | — | 14 | 0.033 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.709 | 0.393 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_park_s022 | 8 | 1 (0) | 4 | 0.707 | 0.410 | 19 | 0.028 | kite in tree, push stroller, carry box, dog sleeping |
| T2_park_s12118_iso (isomorph of T2_playground_s2042) | 8 | 1 (0) | 4 | 0.702 | 0.367 | 21 | 0.030 | dog begs, carry box, ducks swimming, fishing |
| T2_street_s1032 | 9 | 1 (0) | 4 | 0.710 | 0.368 | 16 | 0.048 | lost balloon, balloon, wave, ice cream |
| T2_street_s14109_iso (isomorph of T2_park_s022) | 8 | 1 (0) | 4 | 0.707 | 0.427 | 17 | 0.050 | about to trip, drink bench, carry bag, photo |
| T2_playground_s2042 | 8 | 1 (0) | 4 | 0.701 | 0.377 | 17 | 0.036 | cat stalks bird, fly kite, sandbox, push stroller |
| T3_garden_s7013 | 12 | 2 (1) | 6 | 0.654 | 0.327 | 22 | 0.043 | about to trip, sweep fork, paint fence, water flowers, bird perched, play catch |
| T3_park_s1023 | 12 | 2 (1) | 5 | 0.648 | 0.336 | 20 | 0.032 | sprinkler package, sitting on air, read bench, carry bag, ducks swimming |
| T3_park_s9104_iso (isomorph of T3_playground_s043) | 12 | 2 (1) | 6 | 0.665 | 0.331 | 25 | 0.032 | ducks bread, dog reading, water flowers, goat grazing, carry box, dig |
| T3_street_s16233 | 12 | 3 (1) | 5 | 0.647 | 0.318 | 20 | 0.054 | ball in tree, ice cream drop, square wheel, walk dog, photo |
| T3_playground_s043 | 12 | 2 (1) | 6 | 0.668 | 0.339 | 21 | 0.041 | dog begs, dog reading, fly kite, ice cream, run, jump |
| T3_playground_s18102_iso (isomorph of T3_street_s16233) | 12 | 3 (1) | 5 | 0.646 | 0.332 | 23 | 0.040 | lost balloon, ice cream drop, square wheel, bird perched, carry box |
| T4_garden_s327962 | 18 | 5 (2) | 8 | 0.572 | 0.238 | 29 | 0.044 | paint tracks, lost balloon, cat stalks bird, dog reading, fish in tree, read bench, birds flying, cat sleeping |
| T4_park_s2423977 | 18 | 5 (1) | 9 | 0.569 | 0.252 | 27 | 0.036 | about to trip, dog begs, ball in tree, cat stalks bird, dog reading, carry bag, goat grazing, ice cream, ducks swimming |
| T4_park_s42111_iso (isomorph of T4_street_s1412004) | 18 | 5 (2) | 8 | 0.574 | 0.254 | 28 | 0.034 | bird steals, lost balloon, kite in tree, dog reading, bucket hat, ducks swimming, dog playing, birds flying |
| T4_street_s1412004 | 18 | 5 (2) | 8 | 0.591 | 0.254 | 26 | 0.059 | bird steals, ball in tree, about to trip, dog reading, sweep fork, carry bag, birds flying, sweep |
| T4_playground_s1605000 | 18 | 5 (2) | 9 | 0.544 | 0.203 | 26 | 0.042 | ball in tree, bird steals, ice cream drop, bucket hat, square wheel, photo, cat sleeping, sandbox, birds flying |

Isomorph pairs differ by at most 0.017 in content and 0.017 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 26,666 | 27 | 11,977 | 10^12.7 |
| garden | 3 | 2,497,856 | 296 | 338,691 | 10^18.5 |
| garden | 4 | 78,307,591 | 565 | 6,485,763 | 10^23.3 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 46,656 | 24 | 20,579 | 10^11.6 |
| park | 3 | 5,825,387 | 236 | 1,027,898 | 10^17.4 |
| park | 4 | 335,129,874 | 376 | 44,950,328 | 10^22.9 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,433 | 24 | 2,952 | 10^11.8 |
| street | 3 | 440,799 | 220 | 70,459 | 10^17.4 |
| street | 4 | 7,157,106 | 330 | 947,071 | 10^22.2 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.5 |
| playground | 3 | 749,671 | 183 | 113,624 | 10^17.7 |
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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.27 turns the heads in profile, lifts the walker's heel, redraws the broom, the mouth, the belt, the beard and the pecking bird, shortens the figure, and keeps the bench variants behind `TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ` and `TPDB_BEARD`, with `TPDB_OLD`, `TPDB_TEEN`, `TPDB_READDOG`, `TPDB_RDTAIL`, `TPDB_FEED`, `TPDB_BAG`, `TPDB_ROLLER` and `TPDB_SLIDE` from earlier releases |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out027/` | The 18 `.blend` families (builder 0.27.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib027/` | Every variant the generated scenes and probes use, carried over from `lib026` where the cast did not change or rendered from `out027` |
| `assets/cast/gallery027/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (170, all pass the validator) |
| `scenegen/` | The generator (0.27.0, placement revision 25); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) and the bicycle's two wheels (`WHEEL27`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.27 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v027.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v027.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v027.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all twenty-four screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out027                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out027 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s1023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v027   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v027 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery027 --old-gallery <v0.26 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.27 --single   # the release as one zip, tpdb_v0.27.zip
```

The release is one zip, `tpdb_v0.27.zip`, about 170 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.26 record rebuilds with the v0.26 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- One template falls under the legibility gate after the v0.27 screen: `dog_begs` (0.89), which this release did not change, on two half marks about
  whose food the dog wants. 63 of 64 pass. `vision/flaws_v027.md` lists it and the oddities for v0.28.
- The oddities come in two rows. Readers' remarks per picture are counted directly from their descriptions and compare across
  screens, with the caveat that current readers write about 18% more than the v0.23 readers on the same pictures (`vision/v024/control/`,
  one reader and eight pictures). The row was recounted in v0.26, as the counter had taken bullets saying nothing is wrong for remarks, so its
  figures differ from those published up to v0.25. The scorers' logged oddities do not compare: v0.23's logged 25% of the remarks, v0.24's 83%, and
  from v0.25 the prompt caps them at three per picture. Earlier screens did not record which model read them; v0.24's to v0.27's ran on Claude Opus 5.5.
- No reader says "teenager": he is read as a boy, a boy or young man, or a person, which the key mostly accepts. The v0.24 redraw moved him
  from a woman to a boy, and v0.26's cap worn forwards moved him no further toward the key's own word. It still reads once as "worn backward or sideways" in v0.27.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 67 pictures 743 of 756 scored items had full marks (743 of 752 in v0.26). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, a v0.24 scorer eleven, and all three scorers of v0.25, v0.26 and v0.27 listed such calls, enough to move a template across the gate. A misread is a call too: the
  rake in v0.26's picture 37 could have been marked as sweeping half right.
- Tier-4 pictures are the hardest to place, and revisions 14 to 25 make them harder (walkers' and runners' lanes, pointing
  lines, feet off benches and off other events' things, the photographer's line of sight, the waver's clear hand, body gaps, the gap
  from thin parts, heads clear of figures up to 80 px apart in depth, the ground clear past a reading walker's obstacle, jumpers in the
  front half, an obstacle a full step ahead, runners clear of other movers, ducks off a float, sleepers clear of walkers' feet, nobody in
  the strip before the horizon, a person's box off the lamp post). The tier-4 garden came again on its v0.26 seed, the park took 24 failed seeds and the
  street 14. 219 free seeds found no tier-4 playground, so it is the v0.26 picture's template set, forced, which placed at once: the rules since v0.25 are not the
  cause and the room is not either, but which sets the planner draws (`vision/flaws_v027.md`). It repeats v0.26's events, as the tier-4 garden repeats v0.24's. Their records rebuild them exactly.
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
- The planner's priors come from the v0.27 calibration, with f = 0 and a at its centre for every inference and contradiction, as in
  v0.20 to v0.26: the trip's cue salience moved by -0.034 and the heavy seesaw's by +0.032, the two largest, with shorter figures and turned heads;
  39 fields in 14 templates moved by 0.002 or more.
- Exact rebuilds hold within a release, on the pinned Pillow: the v0.27 cast (builder 0.27.0) and placement rules (revision 25) change how
  every person looks, so a v0.26 record rebuilds with the v0.26 package.
- Every variant comes from the v0.27 cast (builder 0.27.0, `out027`): every person and the pecking bird were rendered anew on an installed Blender, and the
  families v0.27 did not change were carried over from `lib026`. Some carried variants date from Linux renders, which differ from an installed Blender's
  only in sub-pixel anti-aliasing on the outlines. The library keeps only the 361 variants the v0.27 set and probes use. The bench
  variants (`TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ`, `TPDB_BEARD`, `draw.WHEEL27`) stay in the code.
- The figures are still narrow. Legs an eighth shorter and limbs 14% thicker took the bench from eight remarks to three, on four cut-outs a side, but the screen's remarks on
  thin or long bodies did not fall (six pictures to eight, by keyword). A real change of build is a larger job than these.
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
  v0.24 and v0.25, and with it in v0.26 and v0.27. The v0.27 isomorphs are two at tier 2, two at tier 3 and one at tier 4; the tier-4 one
  took 123 failed attempts.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
