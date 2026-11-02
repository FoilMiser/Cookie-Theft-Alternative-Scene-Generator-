# TPDB v0.20: a silver pail and a cup with a straw, the dropped ice cream on its own, no bird over a jumper, item key words and age of acquisition, read a seventeenth time

v0.19 ended with a sixteenth blind legibility screen: no item in 65 pictures was misread, 750 of 760 scored items had
full marks, and all four v0.18 failures passed, but 60 of 64 templates passed the gate, as in v0.18. Four that had read
in full fell short, each on a single half point in one picture: the blue bucket on a man's head at the back of a garden,
"a tall blue hat ... or a fez"; a girl's white cup on a park bench, "something white ... as if drinking or eating"; a
teenager eating her ice cream beside a boy who had dropped his, walking over "maybe to share it"; and a boy jumping just
below a bird perched on the fence, read as reaching for it. The readers also reported a spare watering can beside the
pan and water landing short of the flowers, a wheelbarrow lying flat, a blown swing seat through its frame's leg, a dug
hole on the path's edge, a ladder's top over the pond, a dog's foot on the sandpit frame, sizes off for their depth, a
jogger who "could have bumped the child and knocked the ice cream off", and the older ones noted for the pilot.

v0.20 works through that list as v0.12 to v0.19 did: each weak visual is taken to the isolation bench (forced alone into a
picture, cut out, read blind, redrawn and read again until it reads as intended), each placement rule is read blind in
whole test scenes among other events, and only then does it all go back into the set, which is regenerated and screened
a seventeenth time. It also takes in a review of the item key words and adds an age-of-acquisition feature at weight 0
(below).

All four templates that failed the v0.19 gate pass the seventeenth screen in full: the silver pail read as "an upside-down metal bucket on his head like a hat" in all three of its pictures, at the back of the playground too; the cup with its straw as "drinking from a red cup through a straw" in all three; the ice-cream eater, never beside a dropped ice cream, as eating; and no jumper as reaching for a bird. For the first time all 64 templates pass the gate. No item in any of the 65 pictures was misread or missed outright: 744 of 746 scored items had full marks and two had half points, the fewest of any screen. The set scored 0.998 over all items (0.989 in v0.19), and its unintended oddities fell from 1.3 to 1.2 per picture. `vision/flaws_v020.md` lists the small oddities left for v0.21.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Python
`bpy`, Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`.

## The v0.19 failures

| Template | What the v0.19 readers saw | v0.20 |
|---|---|---|
| `bucket_hat` | In a garden probe, a man at the back: "a tall blue hat", "could be read as a blue bucket worn on the head, or as a fez- or chef-style hat". Read as a bucket in its two other pictures | A tapered silver pail down over the head (the cap under it hidden), one ridge, a grey rim and a dark wire handle. On the bench, at the back of the park and in the garden: "a large silver-grey metal bucket (pail) upside down on their head like a hat"; in three test scenes "an upside-down bucket on her head like a hat" |
| `drink_bench` | In a park isomorph, "something white ... to her mouth, as if drinking or eating" | A red cup with a sleeve, a white lid and a yellow straw at the mouth, a quarter bigger than the first try. On the bench at the back of the park: "drinking from it through a straw"; in a test scene "drinks from a red cup with a straw" |
| `ice_cream` | In a park isomorph a teenager with her cone walked toward the boy whose ice cream lay on the ground, "maybe to share it" | Never in a picture with the dropped ice cream (and no ice cream eaten on a bench beside it). In three test scenes the dropped ice cream had no second cone near it |
| `jump` | In the tier-4 garden, a boy jumping with his arms up just below a perched bird: "jumping with his arms up near a blue bird" | No bird perched or flying in the air above or beside a jumper's raised hands, placed before or after. In three test scenes: "jumping in the air with both arms raised, looking happy", "as if jumping for joy" |

## The oddities fixed

| What the v0.19 readers saw | v0.20 |
|---|---|
| "A proper watering can sits unused on the grass while she waters with a pan"; water landing "at the front edge of the bed / on the grass rather than on the flowers" | No watering can in a picture with the pan; the can's or pan's stream, and a hose's jet, end inside the flower bed |
| The garden's wheelbarrow "very flat on the grass with no visible legs, looks tipped or squashed" | Standing on its wheel and a leg, the tub raised, the handles sloping up. On the bench: "standing empty and at rest. Nothing looks like it is floating" |
| An empty swing blown "so far it overlaps (or passes through)" the frame's leg | The seat pushed a little downwind and tilted, its ropes following, inside the frame |
| A dug hole over the path's edge; a leaning ladder's top over the pond; a dog's foot on the sandpit frame | The hole clear of the path, the ladder clear of the pond (and of the bench), animals' feet clear of the sandpit frame |
| A jogger who "could have bumped the child and knocked the ice cream off" | No runner in a picture with the dropped ice cream; and, from the test scenes, a runner's lane longer and deeper, so nobody stands or sits in her way |

Left as they were: wind that reaches only the hat, the swing and the washing (a note for the pilot); goats in a garden
or park; small children at the back read as far away (the depth scale is the same for everyone); the older ones (a stall
with nobody at it, a dog with no owner, a man on a seesaw, sweeping with no dirt, the square-wheeled bicycle standing on
its own).

## The isolation bench

Two rounds, 14 cut-outs, each read blind by fresh readers two at a time with the isolation prompt (`vision/isolation_v020.md`
gives every reading). The wheelbarrow, the pan with no can beside it and the hose's jet read at the first try. The pail
took a second round (at first "a bucket (or pot)", "a stack of metal bowls", then "a metal bucket (pail) upside down"),
the cup too (small at the back, "white with a red top", then "a red-and-white cup ... through a straw"), and the swing a
look in the test scenes (its seat first through the frame's leg, then inside it, "slightly tilted, which might hint that
the wind is moving it").

## Design tests

The refined visuals and the new placement rules were then read blind in seven whole test scenes among other events (`vision/design_tests_v020.md`), the four templates the v0.19 gate failed put in them: the bucket hat in three (once at the back of the park), a drink on a park bench, the dropped ice cream in three with no ice-cream eater beside it, and a jumper in three with a bird nearby. The bucket hat read as a bucket worn as a hat in all three; the drink as "a red cup with a straw"; no jumper was read as reaching for a bird, and no dropped ice cream shared a picture with another cone. The frying pan read as a frying pan with no watering can near it, the standing wheelbarrow and the hose drew no remark, and the blown swing seat, now inside its frame, read as moved by the wind "or just how it was drawn".

Two remarks led to changes before the set was built: two runners ran at someone off their line (a man's feet on a bench 115 px behind it, a jumping girl in the air above it), so a runner's lane is now longer and deeper; and a ladder whose feet stood just behind a bench "could also be read as propped on ... the bench", so the ladder keeps clear of the bench.

## Placement revision 18

Every record stores the placement revision it was made with. v0.20 pictures use revision 18, which adds the rules above
to those of revisions 1 to 17: no ice-cream eater, eater on a bench or runner in a picture with the dropped ice cream; no
bird above or beside a jumper's raised hands; no watering can beside the pan, and water that ends in the flower bed; the
garden's wheelbarrow standing; the blown swing seat inside its frame; the dug hole off the path, the ladder off the pond
and the bench, animals' feet off the sandpit frame; a runner's longer, deeper lane; and, found while building the set,
never the garden's bench with the dog waiting at the door (the bench stands in front of the door, so the dog could never
be placed: in the tier-4 garden that one clash failed most attempts).

Inspecting every picture of the set and the probes found nothing new to fix.

## Key words, frequency and age of acquisition

v0.20 also takes up a review of the item key words and a proposal for an age-of-acquisition (AoA) feature
(`feedback-v020-key-words-and-aoa.md`, Nov 1 2026, kept outside the package). Every point that applies to the code was taken; the order matters,
because the AoA field must not move any picture and the key fixes must.

1. **AoA recorded at weight 0.** `scenegen/norms/aoa_kuperman2012.tsv` is a verbatim excerpt (116 rows: every key
   word's form or lemma and a few spares) of the Kuperman, Stadthagen-Gonzalez and Brysbaert (2012) ratings, columns as in
   the original, with the citation and source in its header; every record stores its sha256. `aoa(key)`
   looks a key up as rated, else by its lemma (flowers → flower, leaves → leaf, sweeping → sweep), takes the latest-learned
   word of a phrase (as `zipf` takes the rarest), and uses an override for compounds (ice cream → icecream, 3.33 years).
   `WEIGHTS["aoa"] = 0.0` with the term `w_aoa × (a − 4.47)` in the item difficulty, centred on the mean over the keys.
   Every item record carries `a` and `aoa_raw`, and every picture record the norms file, its hash, the centre, the
   wordfreq version and all the weights (`versions.lexical`). Before any key was changed, all 21 v0.19 set pictures were
   rebuilt from their records with the AoA field in place: every SVG identical, 21 of 21.
2. **Action items keyed on what their first accepted answer names.** The review's list: sweeping (was broom), reading
   (book, in the reading walker, the reader on the bench and the reader under the bird), drinking (coffee), stroller
   (baby), pointing (sky); and the absence item "No water is coming out" keyed on hose (was water). The same rule caught
   five more the review did not list, each keyed on a prop that is not itself an accepted answer: raking (was leaves),
   digging (shovel, twice), eating on the bench (apple or ice cream), reaching up after the lost balloon (balloon, twice)
   and the child stuck up in the air on the seesaw (seesaw, twice; now air). Keys that are an accepted answer on their own
   stay (camera, birds, bread, footprints).
3. **The word terms only for things and actions.** For inferences and contradictions f = 0 and a = 4.47 (the centre), in
   the planner's features and its priors alike: they are scored on meaning, with many accepted phrasings, so no one word is
   their name. Their key, its raw Zipf and its raw AoA stay in the record for reference. To keep the predictions where they
   were, each of these type weights came down by 0.3 × the mean f of the v0.19 set's items of that type: inference 0.60 →
   0.39, noticing a contradiction 0.80 → 0.58, explaining it 1.40 → 1.18. On the v0.19 set the predicted completeness of
   each tier moved by at most 0.01.
4. **Guards on Zipf.** `zipf()` raises an error on a word wordfreq does not know (it gave Zipf 0, so f = −4) and on any
   spaced or hyphenated key without an explicit override ("see-saw" scored 5.27 through "see" and "saw"; "seesaw" is 2.47);
   "leaves" is looked up as "leaf" (wordfreq and the norms both read it as the verb). wordfreq is pinned at 3.1.1 in the
   install line and its version is stored in every record.

The licence: the norms are distributed under CC BY-NC-ND 3.0, which allows sharing them unchanged, with attribution, for
non-commercial use. The excerpt keeps the original rows and columns unaltered and cites the source, but it is a subset of
rows, and whether a subset counts as an unaltered copy under the no-derivatives term is not settled; if the lab would
rather not rely on that, ship the full original file in its place (the loader reads the same columns). The values came
from the copy in the lftk package (1.0.9), which agreed with a second copy on Hugging Face on every word checked; before
the pilot, check them against the original file at crr.ugent.be (`python -m scenegen.difficulty --check-aoa <the original
.xlsx or .csv>` compares every bundled row).

What the pilot should test (no code): the model with AoA against the model without, by likelihood ratio and ΔR² on item
difficulty, pre-registered; and, when choosing the pilot's pictures, AoA kept varying apart from frequency (the review found
r(Zipf, AoA) = −0.52 across the keys; keep the early-learned rare words such as seesaw and sandcastle and the late-learned common ones such
as fence, path and package), with the AoA gap within a rule-4 isomorph pair or an asset swap capped at about 1.5 years on top
of the frequency match. A Spanish version needs Spanish AoA norms.

The planner's difficulty priors are the calibration measured on the v0.20 templates (`calibration.json`), with f = 0 and
a = 4.47 for every inference and contradiction: the frying pan's contradiction, its stream now kept inside the flower bed,
came out a little less salient (cue salience -0.055 to -0.10); the bucket hat's, the pail down over the head, moved by
0.009; every other template by at most 0.01.

## The seventeenth blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 44 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.19.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 |

Across all 65 pictures only 2 of 746 scored items fell short of full marks (10 of 760 in v0.19), both by half a point, and none was misread. In the set the one half point was in the tier-4 street, where the girl with the empty cone beside the dropped ice cream was "crying" over "a dropped ice cream" but not said to have dropped it; in a probe the square-wheeled wheelbarrow was offered two readings, "a square wheel ... or a normal round wheel inside a square frame". Two of the three scorers gave no half point at all; the third listed seven hedged items it credited in full. Unintended oddities fell from 27 to 26 in the set and rose from 52 to 68 in the probes, almost all small. None of the v0.19 oddities came back as reported then: no spare watering can beside the pan, no flat wheelbarrow, no swing through its frame, no hole on the path, no ladder over the pond, no foot on the sandpit frame, no runner beside the dropped ice cream. What the readers noticed instead: a worker in a hi-vis vest painting or pointing in a home garden (three probes); a dog bowl far from any dog (five pictures); a shirt on the washing line behind a head read as part of the clothes (three probes); a can with an unused hose reel beside it, or a hose with an unused can (three probes); figures by the pond's cattails; a reading man and a dog walker overlapping in the tier-4 street; seesaws tilted only a little; and the older ones (a stall with nobody at it, goats, leaves under no tree, the bicycle standing on its own).

The templates that failed the v0.19 gate and the templates whose visuals or placement were refined for its oddities (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.19 | v0.20 | v0.20 meaning items |
|---|---|---|---|
| `bucket_hat` | 0.89 (9 items) | 1.00 (9 items) | 1.00 (6) |
| `drink_bench` | 0.83 (3 items) | 1.00 (3 items) | — |
| `ice_cream` | 0.88 (4 items) | 1.00 (3 items) | — |
| `jump` | 0.83 (3 items) | 1.00 (3 items) | — |
| `ice_cream_drop` | 0.96 (28 items) | 0.97 (16 items) | 0.88 (4) |
| `pan_watering` | 0.94 (9 items) | 1.00 (9 items) | 1.00 (6) |
| `water_flowers` | 1.00 (4 items) | 1.00 (4 items) | — |
| `hose_water` | 1.00 (3 items) | 1.00 (3 items) | — |
| `ladder_nothing` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (6) |
| `dig` | 1.00 (3 items) | 1.00 (3 items) | — |
| `run` | 1.00 (3 items) | 1.00 (3 items) | — |
| `windy_hat` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `dog_wants_walk` | 1.00 (6 items) | 1.00 (6 items) | 1.00 (3) |

The four v0.19 failures pass at 1.00, the bucket hat over nine items in three pictures. The frying pan, its stream now ending inside the flower bed and no watering can near it, rose from 0.944 to 1.00, every reader naming a frying pan. The dropped ice cream read in full in three of its four pictures, the fourth missing half a point for not saying whose it was. The watering, the hose, the ladder (clear of the pond and the bench), the dig (clear of the path), the runner (with its longer lane), the windy hat and the dog at the door (never with the bench in front of it) all read with full marks.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 |

Every template was screened in at least three pictures (51 in three, 10 in four, 1 in five, 2 in six), and all 64 pass, for the first time. Two passed with a half point: the dropped ice cream (0.969 over 16 items) and the square-wheeled wheelbarrow (0.944 over 9), which read in full in v0.19. About five templates of the gate's movement between screens is reader variance (the v0.9 retest), so a full pass is not a guarantee that other readers would pass every template; it does say that none of the 64 has a cause in its pictures left to fix.

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.778 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.773 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s031 | 4 | 0 (0) | 2 | 0.779 | — | 15 | 0.045 | birds flying, read bench |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.772 | — | 15 | 0.033 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.712 | 0.393 | 18 | 0.037 | dog wants walk, dog playing, sweep, play catch |
| T2_garden_s8118_iso (isomorph of T2_playground_s042) | 8 | 1 (0) | 3 | 0.711 | 0.393 | 19 | 0.043 | kite in tree, swing, rake |
| T2_park_s4022 | 8 | 1 (0) | 3 | 0.710 | 0.420 | 18 | 0.024 | kite in tree, photo, walk dog |
| T2_street_s032 | 8 | 1 (0) | 3 | 0.710 | 0.398 | 17 | 0.050 | lost balloon, carry box, wave |
| T2_street_s6109_iso (isomorph of T2_park_s4022) | 8 | 1 (0) | 3 | 0.710 | 0.408 | 16 | 0.047 | lost balloon, jump, run |
| T2_playground_s042 | 8 | 1 (0) | 3 | 0.711 | 0.394 | 16 | 0.034 | lost balloon, slide, carry box |
| T3_garden_s3013 | 12 | 3 (1) | 6 | 0.642 | 0.344 | 21 | 0.038 | about to trip, cat stalks bird, dog reading, bird perched, paint fence, dog sleeping |
| T3_park_s8023 | 12 | 2 (1) | 5 | 0.667 | 0.321 | 22 | 0.032 | dog begs, square wheel, carry bag, ice cream, fly kite |
| T3_park_s10102_iso (isomorph of T3_street_s133) | 12 | 3 (0) | 6 | 0.630 | 0.281 | 27 | 0.032 | kite in tree, ice cream drop, bird steals, plant flowers, sweep, birds flying |
| T3_park_s6104_iso (isomorph of T3_playground_s13243) | 12 | 3 (1) | 6 | 0.649 | 0.284 | 23 | 0.032 | ball in tree, dog begs, pan watering, photo, bird perched, cat sleeping |
| T3_street_s133 | 12 | 3 (0) | 6 | 0.643 | 0.291 | 21 | 0.053 | rain coming, ice cream drop, bird steals, push stroller, balloon, sweep |
| T3_playground_s13243 | 12 | 3 (1) | 6 | 0.647 | 0.301 | 20 | 0.038 | about to trip, seesaw heavy, bucket hat, dog sleeping, slide, jump |
| T4_garden_s121279 | 18 | 4 (1) | 8 | 0.572 | 0.264 | 27 | 0.048 | cat stalks bird, blocked hose, ball in tree, dog reading, swing, dog sleeping, birds flying, play catch |
| T4_park_s4224 | 18 | 5 (2) | 9 | 0.548 | 0.221 | 26 | 0.035 | sprinkler package, ducks bread, ball in tree, sitting on air, pan watering, dig, read bench, ice cream, bird perched |
| T4_street_s134299 | 18 | 4 (1) | 8 | 0.569 | 0.239 | 27 | 0.057 | ice cream drop, about to trip, lost balloon, fish in tree, walk dog, water flowers, sweep, birds flying |
| T4_street_s8111_iso (isomorph of T4_park_s4224) | 18 | 5 (2) | 9 | 0.549 | 0.206 | 26 | 0.058 | ball in tree, cat stalks bird, about to trip, water upward, sweep fork, birds flying, balloon, carry box, carry bag |
| T4_playground_s117095 | 18 | 5 (2) | 9 | 0.550 | 0.248 | 26 | 0.043 | bird steals, about to trip, kite in tree, dog reading, square wheel, dog sleeping, birds flying, balloon, carry box |

Isomorph pairs differ by at most 0.013 in content and 0.017 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,471 | 9 | 1,927 | 10^10.0 |
| garden | 2 | 27,943 | 27 | 12,545 | 10^12.7 |
| garden | 3 | 2,866,694 | 296 | 370,470 | 10^18.6 |
| garden | 4 | 114,496,999 | 565 | 8,231,999 | 10^23.3 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 47,033 | 24 | 20,904 | 10^11.6 |
| park | 3 | 6,015,245 | 236 | 1,068,009 | 10^17.5 |
| park | 4 | 371,870,373 | 376 | 50,031,202 | 10^23.1 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,433 | 24 | 2,952 | 10^11.8 |
| street | 3 | 480,097 | 220 | 78,700 | 10^17.2 |
| street | 4 | 8,526,054 | 330 | 1,143,561 | 10^22.6 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.5 |
| playground | 3 | 749,671 | 183 | 113,624 | 10^17.9 |
| playground | 4 | 10,690,061 | 232 | 1,352,842 | 10^21.9 |

In all 515,801,098 structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.

## Folders

| Folder | What it holds |
|---|---|
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts) |
| `assets/validate_assets.py` | Checks for every rendered variant |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions; v0.20: the silver pail worn as a hat, the cup with a lid and straw), `animals.py`, `specs.py` |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out020/` | The 18 `.blend` families (builder 0.20.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib020/` | Every variant the generated scenes and probes use: those of unchanged poses carried over from `lib019`; the bucket hats, the drinks and every variant first needed in v0.20 rendered from `out020` |
| `assets/cast/gallery020/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (170, all pass the validator) |
| `scenegen/` | The generator (0.20.0, placement revision 18); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.20 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v020.md` and their rounds), flaw lists (`flaws_v04.md` to `flaws_v020.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v020.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all seventeen screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |

## How to run

```bash
pip install bpy==5.2.3 cairosvg pillow numpy scipy wordfreq==3.1.1 jsonschema --break-system-packages

cd assets/cast && python build_cast.py out020 && cd ../..           # build the cast (about a minute)
cd assets/cast && python gapcheck.py out020 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s8023.json --out /tmp/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
python vision/isolation_bench.py /tmp/bench pail_d drink_c swing_b   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v020   # then describe and score: vision/screen_prompts.md
python vision/summarize_screen.py vision/v04:<v0.4 scenes> vision/v05:<v0.5 scenes> vision/v06:<v0.6 scenes,probes> \
    vision/v07:<v0.7 scenes,probes> vision/v08:<v0.8 scenes,probes> vision/v09:<v0.9 scenes,probes> \
    vision/v010:<v0.10 scenes,probes> vision/v011:<v0.11 scenes,probes> vision/v012:<v0.12 scenes,probes> \
    vision/v013:<v0.13 scenes,probes> vision/v014:<v0.14 scenes,probes> vision/v015:<v0.15 scenes,probes> \
    vision/v016:<v0.16 scenes,probes> vision/v017:<v0.17 scenes,probes> \
    vision/v018:<v0.18 scenes,probes> vision/v019:<v0.19 scenes,probes> vision/v020:scenes,probes
python vision/gate.py vision/v020 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery020 --old-gallery <v0.19 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.20 --single   # the release as one zip, tpdb_v0.20.zip
```

The release is one zip, `tpdb_v0.20.zip`, about 146 MB. Google Drive does not virus-scan a file over 100 MB, so it asks
to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that.
`package_release.py` replaces the `package_v0XX.sh` scripts and checks, file by file, that the zip holds every file of
the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's
pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.19 record rebuilds with the v0.19 package.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- No template falls under the legibility gate after the v0.20 screen, for the first time: all 64 pass, the four
  v0.19 failures in full. Two passed with a half point each (the dropped ice cream in the tier-4 street, said to be
  dropped but not by whom; the square-wheeled wheelbarrow in a probe, "a square wheel ... or a normal round wheel inside
  a square frame"). `vision/flaws_v020.md` gives what the readers saw and the oddities left for v0.21.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are at the ceiling: across 65 pictures only 2 of 746 scored items fell short of full marks, both by
  half a point, and none was misread. AI readers describe exhaustively, so the screen cannot rank templates by difficulty;
  that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six
  and a v0.20 scorer seven, enough to move a template across the gate.
- Tier-4 pictures are the hardest to place, and revisions 14 to 18 make them harder (walkers' and runners'
  lanes, pointing lines, feet off benches, the photographer's line of sight, the waver's clear hand, body gaps, the
  gap from thin parts). The v0.19 code places them no more often: on the same seeds it placed no tier-4 garden or street
  in 72 and 15 casts. The tier-4 garden, playground and street pictures came from wide seed searches with no
  template-variety steering, as in v0.15 to v0.19: the garden after 64 seeds of up to 40 casts each (found once the
  planner stopped pairing the dog at the door with the bench in front of it), the street after 58 and the playground
  after 6; the tier-4 park came from a search past the showcase seed. Their records rebuild them exactly.
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
- The planner's priors come from the v0.20 calibration, with f = 0 and a at its centre for every inference and
  contradiction: the frying pan's contradiction, its stream now kept inside the flower bed, came out a little less
  salient (cue salience -0.055 to -0.10); the bucket hat's, the pail down over the head, moved by 0.009; every other
  template by at most 0.01.
- Exact rebuilds hold within a release: the v0.20 placement rules (revision 18), the redrawn pail and cup, the key
  words and the frequency rule change where events go and what the planner picks, so a v0.19 record rebuilds with the
  v0.19 package.
- Variants whose pose did not change are carried over from the v0.19 library; rendered again from the
  v0.20 cast they come out the same, or within a few levels of grey at anti-aliased edges.
- Age of acquisition is recorded at weight 0, so it moves nothing until the pilot's pre-registered test says it
  should. The bundled ratings are a verbatim excerpt of Kuperman et al. (2012) under CC BY-NC-ND 3.0, taken from a
  copy in the lftk package; they have not yet been checked against the original file at crr.ugent.be.
- Key words follow one rule (the word the first accepted answer names: an action's verb, or the thing that names
  it), applied by hand in v0.20; a key that is itself an accepted answer was left alone.
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
