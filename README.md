# TPDB v0.22: a square wheel with nothing round in it, jumpers at the front, ladders against the hedge, read a nineteenth time

v0.21 ended with an eighteenth blind legibility screen: 738 of 744 scored items in the set had full marks, and 61 of 64
templates passed the gate. One item was misread, the first in the set since v0.11: in the tier-4 street a woman watering a
planter box with a frying pan, held up against a slate-grey shop door, read as "watering ... with a grey watering can". Two
more templates fell short of the gate on a half point each: a teenager jumping for joy in front of the fruit stall read as
standing "with both arms up, smiling", and a ladder leaning on nothing, its top just below a lamp post's foot, read as
"standing up at a lean ... or lying flat on the grass". The barrow's square wheel took a half point for the second screen
running ("a square dark frame with a spoked wheel inside it rather than a plain round wheel"). The readers also reported
small oddities, none of them misreadings: a sprinkler's hose rising "straight up out of the bottom edge like a stiff pipe",
and stories the pictures did not mean to tell (a boy about to trip over a wheelbarrow's handles, a reading walker who "may
step on the sleeping cat" further along her path, a runner "heading straight for the flower bed", a kicked ball "flying
toward the woman and the washing").

v0.22 works through that list. The two that are about how things look, the square wheel and the leaning ladder, went to
the isolation bench first, where the wheel was redrawn three ways and read blind on its own; the rest are placement rules
(revision 20). All of them were then read blind in whole test scenes among other events, the set was regenerated, and it
was screened a nineteenth time.

Every v0.21 shortfall that revision 20 and the bench addressed read in full in the nineteenth screen: the jumper as jumping in all three of its pictures, the ladder leaning on nothing as standing by itself in all three, and the redrawn square wheel as square ("its wheel is square, which wouldn't roll"), with no reader seeing a round wheel inside it. No sprinkler hose rose from the bottom edge, no foot stood on a wheelbarrow's handles, and no kick was aimed at anyone. No item of the set was misread, its contradictions are back to 1.00, and 285 of its 287 scored items had full marks (0.997 over all items; 0.989 in v0.21). One template still falls short of the gate: the frying pan, now out of the street, read as a frying pan in two of its three garden probes and as "a grey, round watering can" in the third, held close in front of the flowers with its handle hidden. 63 of 64 templates pass (61 in v0.21). `vision/flaws_v022.md` sends the pan to the isolation bench for v0.23, with the older man's profile head, whose grey ring of hair read as a beard and turned his walk the other way.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Python
`bpy`, Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`.

## What was fixed

| What the v0.21 readers saw | v0.22 |
|---|---|
| The frying pan held up face-on at a raised planter box in the street, against the grey shop door: "a grey watering can" (the misread) | No watering with the frying pan in the street. It waters a flower bed on the ground, where it read as a frying pan in both v0.21 probes and in the v0.22 design test |
| A teenager with both arms up in front of the fruit stall: "cheering, celebrating, stretching or dancing" | A jumper clear of standing structures behind the feet, and in the front half of the ground (at least 200 px below the horizon), where the drawn gap above the shadow is large enough to read. At the back of the design tests two jumpers were still hedged; brought to the front, both read as "clearly jumping" |
| A ladder on the open grass, its top just below a lamp post's foot: "standing up at a lean ... or lying flat on the grass" | The ladder's top up past the lawn's far edge, against the hedge or the hills, and 30 px clear of other uprights. On the bench and in the design test it read as standing by itself, never as lying flat |
| The barrow's square wheel: "a square dark frame with a spoked wheel inside it rather than a plain round wheel" (second screen running) | Redrawn with nothing round in it: the open square tyre with eight straight spokes from a square hub to its corners and the middles of its sides, and a square axle plate. The bench chose it over a solid square plate and a square with a cross, which readers took for "a metal plate or box" and "a window frame or grate" |
| The sprinkler's hose "rises straight up out of the bottom edge like a stiff pipe" (two probes) | The sprinkler's hose never leaves by the picture's bottom edge; it lies along the grass to a side edge |
| A reading walker who "may step on the sleeping cat" further along her path, or "may also trip over the bicycle" | Nothing of another event further along a reading walker's way, up to 380 px past her obstacle |
| The boy with the ice cream "about to trip over / run into the wheelbarrow handles" | Nobody's feet over a thing of another event on the ground (the wheelbarrow, the reading walker's obstacle) |
| A runner 400 px short of the flower bed "heading straight for the flower bed and about to trample it" | No flower bed or rock anywhere on a runner's line, up to the picture's edge |
| A kicked ball "flying toward the woman and the washing" | The kick's line clear of people further back (320 px behind the ball's line, was 120) |

Left as they were, as notes for the pilot: hoses that are hard to follow at a glance, contact read loosely (a slide's chute
ending "a little above the grass", a seesaw sitter over the plank's end), goats in a garden or park, figures and faces (the
cast is a stand-in), sizes at the back, and the older ones (leaves under no tree, a stall with nobody at it, bicycle wheels
as "solid black discs").

## The isolation bench

The square wheel and the ladder were each forced alone into a picture, cut out with little else around it and read blind
by fresh readers (`vision/isolation_v022.md`, eight cut-outs, six readers). Three square wheels with nothing round in them
were each read twice: a solid plate (A), the open square with a cross (B), and the open square with eight straight spokes
(C). No reader saw a round wheel inside a square in any of them, and all six called the wheel strange because it could not
roll; but A was offered as "a metal box or plate" and B as "a window frame or grate" in both of their readings, while C
led both readings as a wheel. C is the v0.22 wheel. The ladder with its top up against the hedge read twice as standing on
its own at a slant, "physically odd", and never as lying on the grass.

## Design tests

After the bench, the new wheel and the rules of revision 20 were read blind in whole test scenes among other events (`vision/design_tests_v022.md`, two rounds, eight pictures): a tier-4 street with the square-wheeled bicycle, a jumper and the dropped ice cream; a tier-4 park with the reading walker, a sleeping cat placed after her, the barrow's new wheel and a runner; a garden with the sprinkler and a kick; a garden with the frying pan over a flower bed on the ground and a jumper; a park with the ladder against the hedge; and a tier-4 playground with the reading walker, the bicycle and a sleeping dog. Every rule read as meant but one. The bucket lay "right in her path, so she looks about to trip", the cat "curled up asleep", not linked to her; the barrow's "wheel is drawn as a square, which would be impossible to roll"; the sprinkler's hose came "in from off the left edge"; the pan "looks more like a frying pan or saucepan than a watering can"; the ladder "leans slightly with nothing to lean against". But the two jumpers at the back of the street and the playground, clear of the stall and the fence, were still hedged between jumping and standing with arms raised, while the one at the front of the garden was "jumping in the air". A jumper's lift is drawn to scale, so revision 20 also keeps a jumper in the front half of the ground; rebuilt there, both read as "clearly jumping".

## Placement revision 20

Every record stores the placement revision it was made with. v0.22 pictures use revision 20, which adds the rules above
to those of revisions 1 to 19: no frying pan in the street; a jumper clear of standing structures behind and in the front
half of the ground; a leaning ladder's top above the lawn's far edge and clear of other uprights; nobody's feet over a thing
of another event on the ground; nothing further along a reading walker's way past her obstacle; no flower bed or rock on a
runner's line to the picture's edge; the kick's line clear of people further back; and no sprinkler hose off the picture's
bottom edge. The barrow draws the square wheel the bench chose.

Building and inspecting the set and the probes found one more thing, fixed before the screen. In a garden probe a begging dog stood 40 px in front of a sprinkler's hose, and the hose was drawn running under its body, as if the dog stood on it; the sprinkler's hose now keeps clear of the legs of anyone just in front of it, not only of their feet. The two other pictures with a sprinkler, one of them in the set, rebuild exactly under the new rule; the probe could not be placed again in a garden in eight seeds, and was rebuilt in the park with the same three templates. The tier-4 street was the hardest cell to place under revision 20: it came on the 11th seed of a second search, after the showcase seed and 32 other seeds of up to 40 casts each had failed.

The planner's difficulty priors are the calibration measured on the v0.22 templates (`calibration.json`), with f = 0 and
a = 4.47 for every inference and contradiction, as in v0.20 and v0.21. The sprinkler's cue salience moved by +0.27 (its hose now off a side edge), the ladder's by -0.15 (its top against the hedge; measured in 3 scenes) and the frying pan's by +0.11 (measured in 9 scenes, none in the street); every other template's by at most 0.01.

## The nineteenth blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 44 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.21.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 |

Across all 65 pictures 4 of 755 scored items fell short of full marks (6 of 744 in v0.21): two half points in the set, and one misread in the probes, on both of its contradiction items. The two half points are both in the tier-4 street, from the same reader, each an inference offered as one of two readings: a dog with a paw raised in front of a man eating ice cream on a bench, "perhaps hoping for some ... or just walking by", and a reading walker whose box lay "to the side of / slightly ahead of" her, who "might trip over it, or ... might simply walk past it". In the probes, the frying pan held close in front of a flower bed was "a grey, round watering can ... a watering can, a bucket or even a stone" ("I saw nothing that looks impossible"). Two scorers gave no half point at all and listed eight and nine hedged items they credited in full. Unintended oddities were 25 in the set (24 in v0.21) and rose in the probes from 34 to 54, most of them small remarks on drawing. What the readers noticed: the older man's grey ring of hair, seen in profile, as a beard or a face mask, so that the way he faced was unclear (four probes) and, in the tier-4 park, he seemed to walk toward the sleeping cat behind him ("he might trip over it or step on it"); a runner and a woman with a pram heading toward each other in the tier-2 playground; a duck close to an angler's float that "might go for the bait" (two probes); a wheelbarrow's stand "like a boot" (two probes); hoses' bulges and bends; and the older ones (goats, wind under a clear sky, a stall with nobody at it).

The three templates that fell short of the gate in v0.21, the square wheel and the templates whose placement revision 20 changed (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.21 | v0.22 | v0.22 meaning items |
|---|---|---|---|
| `pan_watering` | 0.78 (9 items) | 0.78 (9 items) | 0.67 (6) |
| `jump` | 0.83 (3 items) | 1.00 (3 items) | — |
| `ladder_nothing` | 0.89 (9 items) | 1.00 (9 items) | 1.00 (6) |
| `square_wheel` | 0.97 (15 items) | 1.00 (9 items) | 1.00 (6) |
| `about_to_trip` | 1.00 (12 items) | 0.96 (12 items) | 0.88 (4) |
| `run` | 1.00 (3 items) | 1.00 (3 items) | — |
| `kick_ball` | 1.00 (3 items) | 1.00 (3 items) | — |
| `sprinkler_package` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (3) |

The three v0.21 failures and the square wheel all read in full except the frying pan: the jumper at 1.00 over three pictures (0.833 in v0.21), the ladder leaning on nothing at 1.00 over nine items (0.889), and the square wheel at 1.00 over nine (0.967), in its new drawing in one probe and on the bicycle in two set pictures. The frying pan stayed at 0.778: out of the street, it was misread once in a garden instead. Of the templates whose placement revision 20 changed, the runner, the kick and the sprinkler read in full; the reading walker took one half point in the tier-4 street, where her box lay a little to the side of her line (0.958 over 12 items).

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 |

Every template was screened in at least three pictures (54 in three, 6 in four, 1 in five, 3 in six), and 63 of 64 pass. The one that falls short is the frying pan, for the second screen running, both times with its handle hard to see: held up face-on at a raised planter in the v0.21 street, and held close in front of the flowers in a v0.22 garden probe. The street rule removed one cause; the drawing itself goes to the bench in v0.23. About five templates of the gate's movement between screens is reader variance (the v0.9 retest).

Templates that did not pass (`vision/flaws_v022.md` gives what the readers saw and the next fix):

| Template | v0.22 mean | Pictures | Misreads |
|---|---|---|---|
| `pan_watering` | 0.78 (9 items) | 3 | 2 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.778 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.773 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s031 | 4 | 0 (0) | 2 | 0.781 | — | 12 | 0.043 | read bench, water flowers |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.771 | — | 14 | 0.032 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.711 | 0.393 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_park_s4022 | 8 | 1 (0) | 3 | 0.710 | 0.420 | 20 | 0.024 | kite in tree, photo, walk dog |
| T2_park_s9118_iso (isomorph of T2_street_s032) | 8 | 1 (0) | 3 | 0.707 | 0.386 | 19 | 0.024 | ball in tree, picnic, dog sleeping |
| T2_street_s032 | 8 | 1 (0) | 3 | 0.710 | 0.376 | 16 | 0.048 | lost balloon, carry box, carry bag |
| T2_street_s9109_iso (isomorph of T2_park_s4022) | 8 | 1 (0) | 3 | 0.707 | 0.418 | 16 | 0.046 | lost balloon, feed birds, run |
| T2_playground_s2042 | 8 | 1 (0) | 4 | 0.686 | 0.373 | 16 | 0.030 | cat stalks bird, push stroller, run, seesaw |
| T3_garden_s3013 | 12 | 3 (1) | 6 | 0.640 | 0.308 | 21 | 0.041 | blocked hose, about to trip, sitting on air, bird perched, paint fence, dog sleeping |
| T3_garden_s7102_iso (isomorph of T3_street_s133) | 12 | 3 (1) | 5 | 0.650 | 0.306 | 20 | 0.041 | cat stalks bird, lost balloon, floating box, drink bench, rake |
| T3_park_s11023 | 12 | 2 (0) | 5 | 0.641 | 0.354 | 21 | 0.031 | sprinkler package, ice cream drop, balloon, birds flying, fly kite |
| T3_street_s133 | 12 | 3 (1) | 5 | 0.650 | 0.316 | 20 | 0.052 | dog begs, ball in tree, square wheel, ice cream, wave |
| T3_street_s7104_iso (isomorph of T3_park_s11023) | 12 | 2 (0) | 5 | 0.639 | 0.367 | 20 | 0.050 | about to trip, ice cream drop, push stroller, feed birds, balloon |
| T3_playground_s5043 | 12 | 3 (0) | 6 | 0.651 | 0.298 | 20 | 0.036 | cat stalks bird, bird steals, rain coming, sandbox, carry box, cat sleeping |
| T4_garden_s327962 | 18 | 5 (2) | 8 | 0.569 | 0.236 | 29 | 0.044 | paint tracks, lost balloon, cat stalks bird, dog reading, fish in tree, read bench, birds flying, cat sleeping |
| T4_park_s242971 | 18 | 5 (1) | 8 | 0.584 | 0.238 | 29 | 0.035 | ball in tree, lost balloon, bird steals, ducks bread, dog reading, ice cream, carry bag, cat sleeping |
| T4_park_s15111_iso (isomorph of T4_playground_s391818) | 18 | 5 (2) | 9 | 0.570 | 0.210 | 28 | 0.036 | about to trip, bird steals, ball in tree, dog reading, water upward, bird perched, balloon, jump, walk dog |
| T4_street_s87941 | 18 | 5 (2) | 9 | 0.592 | 0.240 | 27 | 0.060 | ball in tree, about to trip, dog begs, sitting on air, square wheel, ice cream, feed birds, water flowers, carry bag |
| T4_playground_s391818 | 18 | 5 (2) | 9 | 0.559 | 0.227 | 27 | 0.043 | ball in tree, bird steals, lost balloon, dog reading, sitting on air, jump, dog sleeping, birds flying, ice cream |

Isomorph pairs differ by at most 0.011 in content and 0.017 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 26,666 | 27 | 11,977 | 10^12.7 |
| garden | 3 | 2,497,856 | 296 | 338,691 | 10^18.2 |
| garden | 4 | 78,307,591 | 565 | 6,485,763 | 10^23.4 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 46,656 | 24 | 20,579 | 10^11.6 |
| park | 3 | 5,825,387 | 236 | 1,027,898 | 10^17.1 |
| park | 4 | 335,129,874 | 376 | 44,950,328 | 10^23.1 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,433 | 24 | 2,952 | 10^11.8 |
| street | 3 | 440,799 | 220 | 70,459 | 10^17.2 |
| street | 4 | 7,157,106 | 330 | 947,071 | 10^22.4 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.5 |
| playground | 3 | 749,671 | 183 | 113,624 | 10^17.9 |
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
| `assets/validate_assets.py` | Checks for every rendered variant |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; unchanged since v0.20 |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out022/` | The 18 `.blend` families (builder 0.20.0, unchanged), their render configs and `cast_catalog.json` |
| `assets/cast/lib022/` | Every variant the generated scenes and probes use, carried over from `lib021` or rendered from `out022` where first needed |
| `assets/cast/gallery022/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (170, all pass the validator) |
| `scenegen/` | The generator (0.22.0, placement revision 20); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.22 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v022.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v022.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v022.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all nineteen screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |

## How to run

```bash
pip install bpy==5.2.3 cairosvg pillow numpy scipy wordfreq==3.1.1 jsonschema --break-system-packages

cd assets/cast && python build_cast.py out022 && cd ../..           # build the cast (about a minute)
cd assets/cast && python gapcheck.py out022 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s11023.json --out /tmp/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
python vision/isolation_bench.py /tmp/bench sqA_g sqB_g sqC_g ladder_a   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v022   # then describe and score: vision/screen_prompts.md
python vision/summarize_screen.py vision/v04:<v0.4 scenes> vision/v05:<v0.5 scenes> vision/v06:<v0.6 scenes,probes> \
    vision/v07:<v0.7 scenes,probes> vision/v08:<v0.8 scenes,probes> vision/v09:<v0.9 scenes,probes> \
    vision/v010:<v0.10 scenes,probes> vision/v011:<v0.11 scenes,probes> vision/v012:<v0.12 scenes,probes> \
    vision/v013:<v0.13 scenes,probes> vision/v014:<v0.14 scenes,probes> vision/v015:<v0.15 scenes,probes> \
    vision/v016:<v0.16 scenes,probes> vision/v017:<v0.17 scenes,probes> vision/v018:<v0.18 scenes,probes> \
    vision/v019:<v0.19 scenes,probes> vision/v020:<v0.20 scenes,probes> vision/v021:<v0.21 scenes,probes> \
    vision/v022:scenes,probes
python vision/gate.py vision/v022 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery022 --old-gallery <v0.21 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.22 --single   # the release as one zip, tpdb_v0.22.zip
```

The release is one zip, `tpdb_v0.22.zip`, about 151 MB. Google Drive does not virus-scan a file over 100 MB, so it asks
to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that.
`package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the
same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.21 record rebuilds with the v0.21 package.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- One template falls under the legibility gate after the v0.22 screen: the frying pan, for the second screen running.
  Out of the street it read as a frying pan in two of its three garden probes and was misread once more as "a grey,
  round watering can", held close in front of the flowers with its handle hidden. 63 of 64 pass. `vision/flaws_v022.md`
  gives what the readers saw and the list for v0.23.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are at the ceiling: across 65 pictures only 4 of 755 scored items fell short of full marks (two half points,
  and the frying pan's two contradiction items misread in one probe). AI readers describe exhaustively, so the screen cannot rank templates by difficulty;
  that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine and v0.22 scorers two, eight and nine, enough to move a template across the gate.
- Tier-4 pictures are the hardest to place, and revisions 14 to 20 make them harder (walkers' and runners'
  lanes, pointing lines, feet off benches and off other events' things, the photographer's line of sight, the waver's
  clear hand, body gaps, the gap from thin parts, heads clear of figures up to 80 px apart in depth, the ground clear
  past a reading walker's obstacle, jumpers in the front half). All four tier-4 pictures came from wide seed searches
  with no template-variety steering, as in v0.15 to v0.21: the garden and the playground on the 5th and the 21st
  seed of new searches, the park on the v0.21 seed (which with the v0.22 priors draws other events), and the street,
  the hardest, on the 11th seed of a second search, after the showcase seed and 32 others of up to 40 casts each failed
  (a third search ran beside it).
  Their records rebuild them exactly.
- The square-wheeled bicycle still stands on its own: four stands have been tried on the bench, and each
  read as something else (pedals, legs) or not at all.
- The low kick's direction is ambiguous when the kicker's hair hides the face; the teenager kicks first,
  and the kick read in full in all its screened pictures.
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
- The planner's priors come from the v0.22 calibration, with f = 0 and a at its centre for every inference and
  contradiction, as in v0.20 and v0.21: the sprinkler's cue salience moved by +0.27 (its hose off a side edge), the
  ladder's by -0.15 (its top against the hedge; measured in 3 scenes), the frying pan's by +0.11 (measured in 9 scenes,
  none in the street), every other template's by at most 0.01.
- Exact rebuilds hold within a release: the v0.22 placement rules (revision 20) and the redrawn square wheel change
  where events go, what the planner picks and how the barrow looks, so a v0.21 record rebuilds with the v0.21 package.
- Every variant comes from the v0.20 cast unchanged (builder 0.20.0, copied to `out022`); the library keeps only the
  363 variants the v0.22 set and probes use.
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
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
