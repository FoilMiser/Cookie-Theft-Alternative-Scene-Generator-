# TPDB v0.19: the reader out of the wind, the cat by its bird, the pan away from the hose, a runner's speed lines, and the v0.18 oddities refined, read a sixteenth time

v0.18 ended with a fifteenth blind legibility screen: the waver it had been fixing passed in all four of its pictures, the
dark-haired woman's face showed in profile, and 710 of 720 scored items had full marks, but 60 of 64 templates passed the
gate, against 63 in v0.17. Four that had read in full fell short, each in one picture: a teenager reading as she walked
at the back of a windy park, whose open book read as "an open newspaper ... or papers in the wind" and whose bucket
"has no obvious owner or purpose"; a cat on a garden fence, well over a cat's length from a pecking bird, read as
"walking along the top of the fence"; a frying pan beside a hose reel, misread as "a dark grey hose nozzle or watering
wand"; and a runner with no marks of speed, "striding or jogging". The readers also reported eight kinds of unintended
oddity: figures drawn tight against lamp posts, the swing frame and the stall's legs; a child reaching for a ball in a
tree from "beside the trunk"; kicks that looked like a miss; hose and sprinkler water drawn as dashes, "a dotted line";
sizes off for their depth; goats out of place; drawing quirks (a curly-haired boy whose head looked "seen from behind");
and the older ones noted for the pilot.

v0.19 works through that list as v0.12 to v0.18 did: each weak visual is taken to the isolation bench (forced alone into a
picture, cut out, read blind, redrawn and read again until it reads as intended), each placement rule is read blind in
whole test scenes among other events, and only then does it all go back into the set, which is regenerated and screened
a sixteenth time.

All four templates that failed the v0.18 gate pass the sixteenth screen: the reading walker read in full in all six of its pictures, three of them tier-4 ("she looks about to trip over it"), with no reader saying newspaper or papers in the wind; the runner read as running in all three, each time by its speed lines; the stalking cat on the fence and the frying pan away from the hose reel scored 0.944. No item in any of the 65 pictures was misread or missed outright: 750 of 760 scored items had full marks and ten had half points. The set scored 0.989 over all items (0.986 in v0.18), and its unintended oddities fell from 1.9 to 1.3 per picture. 60 of 64 templates pass the gate, as in v0.18: four others, each read in full in v0.18, fall short on a single half point in one picture: a bucket on a man's head at the back of a garden, read as "a tall blue hat"; a girl's drink on a bench, "something white ... as if drinking or eating"; a teenager's ice cream beside a boy who dropped his, "maybe to share it"; and a boy jumping just below a perched bird, read as reaching for it. `vision/flaws_v019.md` lists them with their fixes for v0.20.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Python
`bpy`, Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`.

## The v0.18 failures

| Template | What the v0.18 readers saw | v0.19 |
|---|---|---|
| `about_to_trip` | In the windy tier-4 park, a teenager at the back holding her open book wide: "walks along reading or holding an open newspaper", "could be reading a newspaper, a map, or struggling to hold papers in the wind"; the bucket ahead of her "has no obvious owner or purpose". Read in full in its three other pictures | Never in a picture with the windy hat's gust, and never at the far back (feet above y = 650); every reading walker but the dark-haired woman bends the head 30 degrees again, as in v0.17. In two busy test scenes the walker read as "reading an open book ... about to trip over it" |
| `cat_stalks_bird` | On the tier-4 garden's fence, well over a cat's length from a bird pecking at the fence top: "walking along the top of the fence ... toward the blue bird", the bird "in an awkward pose with its wing up". Read in full on the grass | On the fence the bird sits perched and the cat is close to it (120 to 190 px between them, by the knob, instead of up to 360). On the bench and in a test scene it read as "stalking or sneaking up on the bird", "about to pounce" |
| `pan_watering` | In a probe, beside the garden's hose reel, the pan held nearly edge-on was misread as "a dark grey hose nozzle or watering wand ... not attached to any hose" | No hose reel and no hose template in a picture with the pan; the pan turned toward the viewer, grey inside a black rim, on a shorter, stouter handle. On the bench: "a frying pan or saucepan ... than a watering can" |
| `run` | In a probe, a woman running on the grass: "striding or jogging", "walking briskly or jogging" | Three motion lines trailing from the runner's back at shoulder, waist and hip height, off the pond. On the bench and in three test scenes: "running ... speed lines behind her show she is moving fast" |

## The oddities fixed

| What the v0.18 readers saw | v0.19 |
|---|---|
| A woman "tightly overlapping the lamp post"; a photographer "inside the swing frame"; a man against the fruit stall's legs | A gap between a person and the thin parts (poles, legs, rails) of standing structures the event does not use; anyone across the stall's width stands well in front of it |
| A begging dog whose paws "overlap the woman's legs and the bench (cramped)" | The dog clear of the eater's legs |
| A hose passing "very tightly behind/around the old man's legs" | The hose comes up to the hand from the ground in front of the waterer |
| A child reaching for a ball in a tree "beside the trunk, not under the stuck ball", the raised arms read as "cheering, stretching or waving" | The child points up at the ball, standing on the ball's side of the trunk below it |
| The kicker's foot "stretched past/over the ball, which is still on the ground: may be a swing-and-miss" | The ball against the toe of the kicking foot |
| Hose and sprinkler water drawn as dashes, "a dotted line", "a dotted trajectory rather than water" | The hose's jet an unbroken ribbon widening as it goes, with drops spraying off it; the sprinkler's arcs unbroken and outlined, with drops breaking off them |
| A curly-haired boy whose head looked "almost seen from behind while the body is side-on" | Below the temples his hair stays behind the ear and no curls cover the front of his head, so a profile shows his face |

Left as they were: the painted fence boards beside the painter rather than in front of her (the painter is drawn side on);
the goat (a note for the pilot, as since v0.11); the sizes of a bird on a lamp and a sleeping puppy, and the sleeping cat
still "small" (the depth scale is the same for everyone); the older ones (a stall with nobody at it, a dog with no owner,
a man on a seesaw, fallen leaves under green trees, wind that reaches only the hat, the square-wheeled bicycle standing on
its own).

## The isolation bench

Two rounds, 15 cut-outs, each read blind by fresh readers two at a time with the isolation prompt (`vision/isolation_v019.md`
gives every reading). The runner, the cat on the fence, the sprinkler and the kick read at the first try. The pan took a
second round (at first "a frying pan ... or the spout and rose of a watering can", then "a frying pan or saucepan"), the
curly-haired boy too (his face "a thin brown strip", then no remark), and the hose's jet a third look in the test scenes
(the first ribbon was "a thin second tube or wire").

## Design tests

The refined visuals and the new placement rules were then read blind in six whole test scenes among other events (`vision/design_tests_v019.md`), the four templates the v0.18 gate failed put in them: the reading walker in two busy tier-4 scenes with no wind, the stalking cat on a garden fence by a perched bird, the frying pan in a garden with no hose reel, and a runner in three. The reading walker read as reading and about to trip in both scenes, as reading "an open book" or "an open newspaper", with no reader saying papers in the wind; the cat on the fence as stalking, "about to pounce"; and the runner as running in all three, each time by the speed lines. The hose's jet and the sprinkler's arcs read as water, and the begging dog, the child pointing at the ball in the tree and the kick read as meant. No reader saw anyone against a lamp post, inside the swing frame or among the stall's legs.

Two remarks led to changes before the set was built: the runner's speed lines drawn over the pond (they now stay off the water), and the frying pan, read at first as "a grey can" before the reader added that its shape "looks more like a pan" (left as it is: on the bench both readers named a frying pan or a saucepan). A pram that seemed pulled rather than pushed is the pram pusher's pose, unchanged since v0.6.

## Placement revision 17

Every record stores the placement revision it was made with. v0.19 pictures use revision 17, which adds the rules above
to those of revisions 1 to 16: no reading walker under the windy hat's gust or at the far back; on the fence the stalking
cat close to a perched bird; no hose reel beside the frying pan; motion lines behind a runner, off the pond; a gap
between a person and the thin parts of standing structures, and none among the stall's legs; the begging dog clear of
the eater's legs; the hose up to the hand from in front; the child under a ball stuck in a tree pointing at it; the
kicked ball against the toe; and hose and sprinkler water drawn unbroken.

Inspecting the set added three more: no hand over the stall's crates of fruit (a runner's hand lay on the apples, as if snatching one); a runner and the runner's motion lines clear of the stall (drawn on its counter, the lines looked like marks on the wood); and the playground's seesaw never planned with its bench, right in front of which it stands (with the gap kept from thin parts nobody could sit there, and no busy playground with both could be placed).

The planner's difficulty priors are the calibration measured on the v0.19 templates (`calibration.json`): the soaked box's
inference, its sprinkler's arcs now unbroken, came out more salient (cue salience -0.46 to -0.27); the begging dog's,
placed clear of the eater, and the ball in the tree's, now pointed at, moved by at most 0.06; every other template by at
most 0.011.

## The sixteenth blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 44 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.18.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 |

Across all 65 pictures only 10 of 760 scored items fell short of full marks (10 of 720 in v0.18), all by half a point, and none was misread (one in v0.18). In the set the six half points were in five pictures: in the tier-4 garden a boy jumping below a perched bird read as reaching for it, and the cat on the fence as "stalking the birds or just walking along" in the unsure section; in the tier-4 street whether the girl dropped her ice cream or the dog knocked it was left open; and in two park isomorphs a girl's drink was "something white", the boy beside the dropped ice cream was not said to have dropped it, and a teenager walking toward him with her cone was "maybe" going "to share it". Unintended oddities fell from 40 to 27 in the set and rose from 41 to 52 in the probes (44 probe pictures, 39 in v0.18). None of the v0.18 oddities came back as reported then: no one against a lamp post, inside the swing frame or among the stall's legs, no child beside the trunk under a ball in a tree, no kick read as a miss, no water read as a dotted line, no remark on the curly-haired boy's head. What the readers noticed instead: a watering can lying unused beside the frying pan (three probes) and water landing short of the flowers; the garden's wheelbarrow "very flat ... with no visible legs, looks tipped" (three probes); an empty swing blown through the frame's leg and other single overlaps; birds large next to people; wind that blows off a cap but leaves the trees and flowers still; and, again, goats out of place and a stall with nobody at it.

The templates that failed the v0.18 gate and the templates whose visuals or placement were refined for its oddities (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.18 | v0.19 | v0.19 meaning items |
|---|---|---|---|
| `about_to_trip` | 0.88 (12 items) | 1.00 (18 items) | 1.00 (6) |
| `cat_stalks_bird` | 0.89 (9 items) | 0.94 (9 items) | 0.83 (3) |
| `pan_watering` | 0.83 (9 items) | 0.94 (9 items) | 0.92 (6) |
| `run` | 0.83 (3 items) | 1.00 (3 items) | — |
| `ball_in_tree` | 0.93 (15 items) | 1.00 (18 items) | 1.00 (6) |
| `kick_ball` | 1.00 (3 items) | 1.00 (3 items) | — |
| `hose_water` | 1.00 (3 items) | 1.00 (3 items) | — |
| `sprinkler_package` | 1.00 (12 items) | 1.00 (9 items) | 1.00 (3) |
| `dog_begs` | 1.00 (9 items) | 0.94 (9 items) | 0.83 (3) |

The reading walker passes at 1.00 over six pictures and the runner at 1.00 over three. The stalking cat read in full on the grass and on the fence by its perched bird, "creeping along towards a blue bird", the unsure section adding "or just walking along" (a half point); the frying pan read as "a frying pan instead of a watering can" in two pictures and as "a grey round object held by a handle" in the third (a half point), and no reader said nozzle or wand. The child under a ball in a tree, the kick, the hose's jet and the sprinkler's soaked box all read with full marks; the begging dog, clear of the eater's legs, missed half a point only where its reader added "or barking".

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 |

Every template was screened in at least three pictures (54 in three, 5 in four, 1 in five, 3 in six, 1 in seven). Four fail, each on a single half point in one picture (the bucket hat on two), and all four read in full in v0.18: the bucket hat at the back of a garden probe, the drink on a bench in a park isomorph, the ice cream beside the dropped one in another, and the jump below a perched bird in the tier-4 garden. About five templates of the gate's movement between screens is reader variance (the v0.9 retest), but each of these has a cause in its picture that can be fixed. The v0.20 fixes: the bucket's handle and rim drawn, a coloured cup with a lid and straw, no ice-cream eater beside the dropped ice cream, and no bird above or beside a jumper's raised hands.

Templates that did not pass (`vision/flaws_v019.md` gives what the readers saw and the next fix):

| Template | v0.19 mean | Pictures | Misreads |
|---|---|---|---|
| `drink_bench` | 0.83 (3 items) | 3 | 0 |
| `jump` | 0.83 (3 items) | 3 | 0 |
| `ice_cream` | 0.88 (4 items) | 4 | 0 |
| `bucket_hat` | 0.89 (9 items) | 3 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 5 | 0 (0) | 3 | 0.780 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.773 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s1031 | 4 | 0 (0) | 3 | 0.776 | — | 14 | 0.044 | birds flying, jump, run |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.772 | — | 15 | 0.033 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.710 | 0.420 | 18 | 0.037 | dog wants walk, dog playing, sweep, play catch |
| T2_park_s022 | 8 | 1 (0) | 4 | 0.713 | 0.377 | 18 | 0.026 | kite in tree, carry box, dog sleeping, dig |
| T2_park_s7118_iso (isomorph of T2_street_s032) | 8 | 1 (0) | 3 | 0.707 | 0.401 | 18 | 0.023 | ice cream drop, ice cream, run |
| T2_street_s032 | 8 | 1 (0) | 3 | 0.710 | 0.402 | 16 | 0.049 | ice cream drop, carry bag, wave |
| T2_street_s10109_iso (isomorph of T2_park_s022) | 8 | 1 (0) | 4 | 0.715 | 0.358 | 16 | 0.049 | ball in tree, wave, drink bench, sweep |
| T2_playground_s042 | 8 | 1 (0) | 4 | 0.707 | 0.377 | 17 | 0.035 | cat stalks bird, dog playing, ice cream, sandbox |
| T3_garden_s13013 | 12 | 3 (0) | 6 | 0.636 | 0.333 | 21 | 0.045 | about to trip, sprinkler package, cat stalks bird, bird perched, fly kite, walk dog |
| T3_park_s2023 | 12 | 3 (0) | 6 | 0.640 | 0.302 | 20 | 0.031 | ball in tree, lost balloon, dog begs, ice cream, balloon, ducks swimming |
| T3_park_s8102_iso (isomorph of T3_street_s7133) | 12 | 3 (1) | 6 | 0.655 | 0.295 | 21 | 0.032 | about to trip, ice cream drop, water upward, drink bench, sweep, cat sleeping |
| T3_street_s7133 | 12 | 3 (1) | 6 | 0.663 | 0.315 | 21 | 0.052 | rain coming, ice cream drop, sitting on air, read bench, photo, water flowers |
| T3_street_s7104_iso (isomorph of T3_park_s2023) | 12 | 3 (0) | 6 | 0.641 | 0.317 | 23 | 0.053 | lost balloon, ball in tree, cat stalks bird, push stroller, feed birds, water flowers |
| T3_playground_s10043 | 12 | 3 (0) | 5 | 0.657 | 0.318 | 20 | 0.038 | lost balloon, about to trip, bird steals, slide, push stroller |
| T4_garden_s21016 | 18 | 5 (2) | 9 | 0.557 | 0.236 | 30 | 0.049 | sprinkler package, ball in tree, paint tracks, sitting on air, dog reading, read bench, bird perched, cat sleeping, jump |
| T4_park_s124 | 18 | 5 (1) | 9 | 0.552 | 0.224 | 28 | 0.037 | kite in tree, ducks bread, bird steals, sprinkler package, dog reading, carry bag, photo, dog sleeping, water flowers |
| T4_park_s15111_iso (isomorph of T4_playground_s73039) | 18 | 5 (1) | 8 | 0.585 | 0.250 | 26 | 0.035 | ice cream drop, about to trip, bird steals, ball in tree, dog reading, ice cream, fishing, carry bag |
| T4_street_s91001 | 18 | 4 (1) | 8 | 0.590 | 0.272 | 28 | 0.060 | ball in tree, about to trip, ice cream drop, dog reading, water flowers, read bench, feed birds, carry bag |
| T4_playground_s73039 | 18 | 5 (1) | 8 | 0.570 | 0.253 | 27 | 0.042 | ice cream drop, kite in tree, bird steals, about to trip, dog reading, slide, cat sleeping, bird perched |

Isomorph pairs differ by at most 0.015 in content and 0.020 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,471 | 9 | 1,927 | 10^10.0 |
| garden | 2 | 28,489 | 27 | 13,003 | 10^12.7 |
| garden | 3 | 3,073,032 | 296 | 387,320 | 10^18.5 |
| garden | 4 | 137,732,137 | 565 | 9,554,664 | 10^23.6 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 47,870 | 24 | 20,959 | 10^11.5 |
| park | 3 | 6,337,617 | 236 | 1,095,206 | 10^17.5 |
| park | 4 | 428,700,564 | 381 | 54,909,608 | 10^23.4 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,720 | 24 | 2,983 | 10^11.8 |
| street | 3 | 533,226 | 224 | 82,853 | 10^17.7 |
| street | 4 | 11,356,979 | 345 | 1,388,400 | 10^22.6 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 14,405 | 24 | 5,770 | 10^12.4 |
| playground | 3 | 821,255 | 183 | 118,206 | 10^17.8 |
| playground | 4 | 13,647,230 | 232 | 1,572,795 | 10^22.2 |

In all 602,310,049 structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.

## Folders

| Folder | What it holds |
|---|---|
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts) |
| `assets/validate_assets.py` | Checks for every rendered variant |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py` (v0.19: the curly hair that leaves a profile's face open), `actions.py` (77 actions; v0.19: the frying pan, and the reading walker's head bent 30 degrees again but for the bob), `animals.py`, `specs.py` |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out019/` | The 18 `.blend` families (builder 0.19.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib019/` | Every variant the generated scenes and probes use: those of unchanged families and poses carried over from `lib018`; the curly-haired boy, the frying pans, every reading walker but the dark-haired woman and every variant first needed in v0.19 rendered from `out019` |
| `assets/cast/gallery019/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (170, all pass the validator) |
| `scenegen/` | The generator (0.19.0, placement revision 17); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.19 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v019.md` and their rounds), flaw lists (`flaws_v04.md` to `flaws_v019.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v019.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all sixteen screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |

## How to run

```bash
pip install bpy==5.2.3 cairosvg pillow numpy scipy wordfreq jsonschema --break-system-packages

cd assets/cast && python build_cast.py out019 && cd ../..           # build the cast (about a minute)
cd assets/cast && python gapcheck.py out019 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s2023.json --out /tmp/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.combos --out combos.json
python vision/isolation_bench.py /tmp/bench pan_c run_a fence_a   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v019   # then describe and score: vision/screen_prompts.md
python vision/summarize_screen.py vision/v04:<v0.4 scenes> vision/v05:<v0.5 scenes> vision/v06:<v0.6 scenes,probes> \
    vision/v07:<v0.7 scenes,probes> vision/v08:<v0.8 scenes,probes> vision/v09:<v0.9 scenes,probes> \
    vision/v010:<v0.10 scenes,probes> vision/v011:<v0.11 scenes,probes> vision/v012:<v0.12 scenes,probes> \
    vision/v013:<v0.13 scenes,probes> vision/v014:<v0.14 scenes,probes> vision/v015:<v0.15 scenes,probes> \
    vision/v016:<v0.16 scenes,probes> vision/v017:<v0.17 scenes,probes> \
    vision/v018:<v0.18 scenes,probes> vision/v019:scenes,probes
python vision/gate.py vision/v019 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery019 --old-gallery <v0.18 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.19 --single   # the release as one zip, tpdb_v0.19.zip
```

The release is one zip, `tpdb_v0.19.zip`, about 140 MB. Google Drive does not virus-scan a file over 100 MB, so it asks
to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that.
`package_release.py` replaces the `package_v0XX.sh` scripts and checks, file by file, that the zip holds every file of
the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's
pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.18 record rebuilds with the v0.18 package.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- Four templates fall under the legibility gate after the v0.19 screen, each on a single half point in one
  picture (the bucket hat on two), all four read in full in v0.18: the bucket on the head of a man at the back of a
  garden probe ("a tall blue hat ... or a fez"), a girl's drink on a bench in a park isomorph ("something white ...
  as if drinking or eating"), a teenager's ice cream beside the boy who dropped his ("maybe to share it") and a boy
  jumping just below a perched bird (read as reaching for it). `vision/flaws_v019.md` gives what the readers saw and
  the next fixes.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are at the ceiling: across 65 pictures only 10 of 760 scored items fell short of full marks, all by
  half a point, and none was misread. AI readers describe exhaustively, so the screen cannot rank templates by difficulty;
  that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls and a v0.19
  scorer six, enough to move a template across the gate.
- Tier-4 pictures are the hardest to place, and revisions 14 to 17 make them harder (walkers' lanes,
  pointing lines, feet off benches, the photographer's line of sight, the waver's clear hand, body gaps, the
  gap from thin parts). With that gap no one could sit on the playground's bench behind its seesaw, and no busy
  playground was placed in 88 seed searches of 40 casts each until revision 17 stopped planning the two together. The tier-4
  garden, playground and street pictures came from wider seed searches with no template-variety steering, as in
  v0.15 to v0.18; the tier-4 park came from the batch's own seed search past the showcase seed. Their records
  rebuild them exactly. One of the four gate failures was in a tier-4 set picture, where many events meet, and
  two in isomorphs.
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
- The planner's priors come from the v0.19 calibration: the soaked box's inference, its sprinkler's arcs now
  unbroken, came out more salient, the begging dog's and the ball in the tree's moved by at most 0.06, and every
  other template by at most 0.011.
- Exact rebuilds hold within a release: the v0.19 placement rules (revision 17), the redrawn pan and the
  curly-haired boy's hair change where events go and how they look, so a v0.18 record rebuilds with the
  v0.18 package.
- Variants whose pose did not change are carried over from the v0.18 library; rendered again from the
  v0.19 cast they come out the same, or within a few levels of grey at anti-aliased edges.
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
