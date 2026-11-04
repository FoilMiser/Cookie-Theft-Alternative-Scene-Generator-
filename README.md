# TPDB v0.28: shadows from the feet, a splat, a dog beside the food, read a twenty-fifth time

v0.27 ended with one gate failure, `dog_begs` at 0.89, its readers unsure whose food the dog wanted ("could be hers, begging from her bag"). Its oddities were led by shadows ("a very wide oval, much wider than the puppy"), eyes shut on a walker, and a fallen ice cream read as "a pink hat or a pink frisbee". And it had not been able to place a tier-4 playground at all: 219 free seeds placed nothing, so it forced an old picture's events.

v0.28 works through those. Each drawing went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a twenty-fifth time.

The twenty-fifth screen read all 70 pictures, the set's 21 and 49 probes: 766 of 775 scored items had full marks, and none was misread. `dog_begs`, the one failure of v0.27, went from 0.89 to 1.00, and whose food the dog wants is no longer asked. Shadows, the commonest named oddity, went from 20 pictures to 11 by keyword, and none of the eleven calls one too wide or off the feet. The flying saucer is a splat. Readers' remarks per picture fell 12%, from 5.81 to 5.14, though the readers themselves differ widely. The gate went the other way: 61 of the 64 templates pass, against 63, and three fail. `dog_sleeping` (0.67) is on a drawing this release did not change but whose shadow it did, and the smaller shadow may have made it harder to read. `ducks_bread` (0.83) and `dog_wants_walk` (0.83) were not touched: on the ducks the readers wrote much what v0.27's did and scored half marks where those scored in full. And the question left open for two releases was answered: the tier-4 playground draws sets that place again, with three rules that did nothing one at a time.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.27 readers saw | v0.28 |
|---|---|
| `dog_begs`: "could be hers, begging from her bag", "or be watching the kite" (0.89) | At the end of the bench the eater sits nearest, its gaze on the food, and nobody else near it, now or later. Not redrawn. "Begging for the ice cream": 1.00 in its three pictures |
| Shadows: "a very wide oval, much wider than the puppy", "a bit wide and offset from her feet" | From the figure's own footprint: a person's from the feet, anything else's from the columns the body fills, under its lowest part. Drawn objects' are flatter too. Pictures remarking on shadows fell from 20 to 11, none calling one wide. The sleeping dog may have paid for this (below) |
| The fallen ice cream: "a pink hat or a pink frisbee", a flying saucer | A flat splat, with flecks thrown clear of it and the sprinkles still on, and the dog's mouth over it. "A pink splat with coloured sprinkles": in full in its three pictures |
| The seesaw: "almost past it", and "the girl has none of her own" | Riders and handles further in from the ends, and one shadow under the whole seesaw. No remark on either. The heavy rider's leg over the plank stays |
| Eyes shut on a walker: "Walking with eyes shut is slightly odd" | No walker has closed eyes, in 70 pictures |
| Marks on a face: "dark marks around her nose and mouth", "a pink smudge on the cheek" | No brows over closed eyes and a smaller blush. Pictures remarking on them fell from 9 to 5 |
| The beard: "a thin dark strap along the jaw" | A fuller one read as "a mask or scarf", so a goatee and moustache: "a small beard". No strap or mask in 70 pictures |
| The ball in the tree: "a blue planet-like sphere", on "a small bare branch drawn on top of the crown" | A beach ball, in all four of its pictures, on a limb from a fork at the top of the trunk. Once now "as if the leaves had been cut away to display the ball" |
| "Two bins so close to each other seem like more bins than the scene needs" | One bin to a picture |
| The tier-4 playground: 219 failed seeds, not explained | Explained, and placing again with events of its own (below) |

Left as they were: `about_to_trip`, as the obstacle is already on the line of the stride by rule and by eye, and its meaning item fell again; the hose in `hose_water`, which drew more remarks; the heavy rider's leg; the narrow figure. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, a wind that reaches only some things.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v028.md`, three rounds, 37 cut-outs, 17 readers). The variants are behind `TPDB_BROW`, `TPDB_BLUSH` and `TPDB_BEARD` in the cast, and `draw.SPLAT28`, `draw.SEESAW_IN28` and `library.SHADOW28` in the scene; the release builds with the chosen ones. Shadows took four remarks on four old cut-outs and none on four new. A first new shadow vanished under the sleeping dog, which reaches below its ground point, and two bands across the ball looked like a target: both were looked at and fixed before any reader saw them. The splat without a dome beat the one with a low lump, which was once "some other spilled food or slime". The ball's branch took two rounds: with leaves over both ends it "does not visibly connect to the trunk", three of three, and with a limb to the trunk it was "a single bent pipe", so the top of the trunk became a fork. The beard took three: a fuller one was worse, and the answer was less of it.

## Design tests

After the bench, the new drawings were read blind in whole test scenes among other events (`vision/design_tests_v028.md`, six pictures, six readers). The begging dog was offered in full in both of its pictures, with "right beside" in each: "begging with its front paws raised and its nose pointed up at the ice cream". The fallen ice cream "lies as a splat on the pavement with sprinkles around it". In six pictures no shadow was called wide, large or offset, the nearest being "her shadow sits under her, so she looks grounded". No reading showed a new problem, so there was no second round. Test 4's "could also be a mask" sent the bearded man back to the bench, so the goatee is first read in a whole picture in the screen. The hose still "looks a little stiff", and was left.

## Placement revision 26

Every record stores the placement revision it was made with. v0.28 pictures use revision 26, which adds to those of revisions 1 to 25 the begging dog's end of the bench, its gaze and the ground kept clear round it; shadows from the figure's own footprint; the seesaw's riders further in on one shadow; the splat and the dog's mouth over it; no closed eyes on a walker; the beach ball on a limb, and a bird's branch the same way; one bin to a picture; and three rules for a tier-4 playground and one for a tier-4 street. The faces and the goatee are in the cast (builder 0.28.0).

Building the set answered the question v0.26 and v0.27 left open. v0.27 could not place a tier-4 playground from 219 free seeds. This time the same 12 seeds were tried one change at a time, and nothing placed: not with the trip never drawn, the failing templates placed first, a search that learns from its failures, plans limited to six people, or the ground-hungry templates left out. What found it was to take away the difficulty band and try 226 random sets. Five placed. All five held the bird stealing a sandwich and the square-wheeled bicycle (5 of 72 sets with both, none of 154 without), none had a swing set, and all were a thing or two short of the tier's 18 things, the long railing having just failed the rule that a scored thing be 80% in view. Being short, plans went back for the swing and the sandbox, which took the ground they needed. Revision 26 therefore requires the pair, leaves out the swing as scenery and counts the railing up to 30% hidden. Each alone placed nothing from the 12 seeds; all three placed 2 of 12, in under a minute each. The picture itself is on one of those two seeds, and has events of its own. It costs something: every tier-4 playground now holds those two, and none can hold the begging dog, which needs the same bench (`vision/flaws_v028.md`, Placement).

The tier-4 street failed 57 seeds, so requiring the bird stealing a sandwich, which both its last pictures held, was tried, and placed after 13 more. One picture does not show the rule did it. The garden placed on its v0.27 seed and the park after 9 failed seeds. The tier-3 street and playground each took a search past their showcase seeds, and the tier-4 isomorph 226 failed attempts. The first probe pass left three templates short, tried in crowded groups in the garden, and six more probes filled them. All 70 records rebuild identical to the pixel.

The planner's difficulty priors are the calibration measured on the v0.28 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.27. The fallen ice cream's cue salience moved by -0.194, the flat splat being smaller than the dome, and the ball in the tree's by +0.063; 11 fields in 4 templates moved by 0.002 or more.

## The twenty-fifth blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 49 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.27.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) | v0.25 (21 pictures) | v0.26 (21 pictures) | v0.27 (21 pictures) | v0.28 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 | 0.98 | 0.95 | 0.95 | 0.88 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.99 | 0.98 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 | 0 of 286 | 0 of 289 | 0 of 283 |
| Oddities per picture, as logged by the scorers | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 | 2.6 | 2.6 | 2.2 | 2.0 |
| Readers' remarks per picture (recounted in v0.26) | 8.8 | 5.4 | 6.4 | 4.8 | 4.7 | 4.8 | 4.9 | 4.4 | 4.3 | 4.4 | 4.4 | 4.4 | 3.9 | 3.9 | 4.4 | 4.0 | 4.0 | 3.9 | 4.2 | 3.9 | 5.6 | 5.9 | 5.3 | 5.8 | 5.1 |

Across all 70 pictures 766 of 775 scored items had full marks. Eight had half marks, one was missed, and none was misread. Eight of those nine are in the set, seven of them inferences. The trip lost three half marks, the readers having the walker go past the obstacle ("he is moving past it, not squarely into it"). The duck and the bread lost three, on the wording of its intent ("swimming towards those crumbs"). The dog at the door lost the one missed item ("sits with a red lead in its mouth", no more). The sleeping dog lost two half marks, one on what kind of animal it is. No cloud or tree was missed, where v0.27 lost eight such items to one reader's habit. The set's headline is all items 0.984 (0.993 in v0.27), with things and contradictions at 1.00, actions at 0.996 and inferences at 0.879.

**Remarks went down, 360 on 70 pictures against 389 on 67.** The pictures were a little less busy, 3.06 templates a picture against 3.18, which is not enough to account for it, but the readers range from 4.25 to 6.38 a picture on the same split of the pictures, against 5.29 to 6.29, so this is one screen and readers differ. `vision/remark_topics.py` sorts them roughly by keyword. Shadows fell from 20 pictures to 11, this release's main change, and marks on a face from 9 to 5. A beard as a strap or mask fell from 2 to 0, and a branch to hold something from 5 to 3. Not changed, and not better: thin or long bodies went from 8 to 13, and a hidden face from 10 to 12. A keyword count is a rough sort, not a measure.

The one that failed in v0.27, the splat, and the four weakest now (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.27 | v0.28 | v0.28 meaning items |
|---|---|---|---|
| `dog_begs` | 0.89 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `ice_cream_drop` | 1.00 (12 items) | 1.00 (12 items) | 1.00 (3) |
| `dog_sleeping` | 1.00 (3 items) | 0.67 (3 items) | — |
| `ducks_bread` | 1.00 (9 items) | 0.83 (9 items) | 0.50 (3) |
| `dog_wants_walk` | 0.92 (6 items) | 0.83 (6 items) | 0.67 (3) |
| `about_to_trip` | 0.96 (12 items) | 0.92 (18 items) | 0.75 (6) |

`dog_begs` read in full in its three pictures with the placement rule, and the dog was not redrawn. `ice_cream_drop` read in full on its splat. The other four rows did not change: `dog_sleeping` has the same drawing on a new shadow, and `ducks_bread`, `dog_wants_walk` and `about_to_trip` nothing at all. `about_to_trip` has fallen for two releases, and its meaning item is now the weakest that passes, at 0.75.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 | v0.27 | v0.28 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 | 61 | 59 | 63 | 61 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 | 3 | 5 | 1 | 3 |

Every template was screened in at least three pictures (47 in three, 12 in four, 2 in five, 3 in six), and 61 of 64 pass, against 63. Of the three that fail, one is on a drawing whose shadow this release changed, and two were not touched at all. The v0.9 retest put the gate's reader variance at about five templates between screens, so 63 to 61 is not a measure of the drawings getting worse, as 59 to 63 was not one of their getting better. The gate is a filter, and the pilot with people is the test of difficulty.

Templates that did not pass (`vision/flaws_v028.md` gives what the readers saw and the next fix):

| Template | v0.28 mean | Pictures | Misreads |
|---|---|---|---|
| `dog_sleeping` | 0.67 (3 items) | 3 | 0 |
| `dog_wants_walk` | 0.83 (6 items) | 3 | 0 |
| `ducks_bread` | 0.83 (9 items) | 3 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.777 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.772 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s1031 | 4 | 0 (0) | 3 | 0.776 | — | 12 | 0.043 | birds flying, jump, run |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.771 | — | 14 | 0.033 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.709 | 0.393 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_garden_s11118_iso (isomorph of T2_playground_s042) | 8 | 1 (0) | 4 | 0.712 | 0.381 | 17 | 0.042 | sprinkler package, cat on fence, drink bench, play catch |
| T2_park_s022 | 8 | 1 (0) | 4 | 0.707 | 0.410 | 19 | 0.028 | kite in tree, push stroller, carry box, dog sleeping |
| T2_street_s1032 | 8 | 1 (0) | 4 | 0.710 | 0.376 | 16 | 0.048 | cat stalks bird, balloon, wave, read bench |
| T2_street_s14109_iso (isomorph of T2_park_s022) | 8 | 1 (0) | 4 | 0.707 | 0.427 | 17 | 0.050 | about to trip, drink bench, carry bag, photo |
| T2_playground_s042 | 8 | 1 (0) | 4 | 0.710 | 0.361 | 18 | 0.035 | lost balloon, sandbox, dog playing, play catch |
| T3_garden_s7013 | 12 | 2 (1) | 6 | 0.654 | 0.327 | 22 | 0.043 | about to trip, sweep fork, paint fence, water flowers, bird perched, play catch |
| T3_garden_s8102_iso (isomorph of T3_street_s21933) | 12 | 3 (0) | 5 | 0.668 | 0.360 | 20 | 0.039 | about to trip, kite in tree, cat stalks bird, birds flying, kick ball |
| T3_park_s8023 | 12 | 2 (1) | 5 | 0.669 | 0.313 | 21 | 0.028 | ducks bread, sitting on air, carry bag, ice cream, fly kite |
| T3_park_s10104_iso (isomorph of T3_playground_s19143) | 12 | 2 (0) | 5 | 0.650 | 0.294 | 23 | 0.031 | ice cream drop, ducks bread, birds flying, balloon, carry bag |
| T3_street_s21933 | 12 | 3 (0) | 5 | 0.669 | 0.351 | 20 | 0.052 | ball in tree, about to trip, dog begs, walk dog, photo |
| T3_playground_s19143 | 12 | 2 (0) | 5 | 0.650 | 0.308 | 20 | 0.038 | ice cream drop, seesaw heavy, fly kite, carry box, bird perched |
| T4_garden_s327962 | 18 | 5 (2) | 8 | 0.572 | 0.238 | 29 | 0.044 | paint tracks, lost balloon, cat stalks bird, dog reading, fish in tree, read bench, birds flying, cat sleeping |
| T4_garden_s63111_iso (isomorph of T4_playground_s621959) | 18 | 5 (2) | 9 | 0.559 | 0.218 | 26 | 0.047 | bird steals, about to trip, ball in tree, square wheel, sweep fork, bird perched, dog sleeping, carry box, cat sleeping |
| T4_park_s443959 | 18 | 4 (2) | 9 | 0.568 | 0.245 | 27 | 0.037 | ducks bread, cat stalks bird, square wheel, dog reading, ice cream, carry bag, feed birds, read bench, goat grazing |
| T4_street_s3438959 | 18 | 5 (1) | 8 | 0.569 | 0.250 | 27 | 0.057 | bird steals, ice cream drop, ball in tree, about to trip, dog reading, carry bag, birds flying, sweep |
| T4_playground_s621959 | 18 | 5 (2) | 9 | 0.560 | 0.201 | 26 | 0.040 | bird steals, ball in tree, lost balloon, square wheel, bucket hat, run, dog playing, ice cream, bird perched |

Isomorph pairs differ by at most 0.002 in content and 0.020 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 26,666 | 27 | 11,977 | 10^12.7 |
| garden | 3 | 2,497,856 | 296 | 338,691 | 10^18.4 |
| garden | 4 | 78,307,591 | 565 | 6,485,763 | 10^23.5 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 46,656 | 24 | 20,579 | 10^11.2 |
| park | 3 | 5,825,387 | 236 | 1,027,898 | 10^17.6 |
| park | 4 | 335,129,874 | 376 | 44,950,328 | 10^23.0 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,433 | 24 | 2,952 | 10^11.8 |
| street | 3 | 440,799 | 220 | 70,459 | 10^17.2 |
| street | 4 | 7,157,106 | 330 | 947,071 | 10^21.6 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.3 |
| playground | 3 | 749,671 | 183 | 113,624 | 10^17.9 |
| playground | 4 | 10,690,061 | 232 | 1,352,842 | 10^20.8 |

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.28 takes the brows off closed eyes, shrinks the blush and gives the bearded man a goatee |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out028/` | The 18 `.blend` families (builder 0.28.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib028/` | Every variant the generated scenes and probes use, carried over from `lib027` where the cast did not change or rendered from `out028` |
| `assets/cast/gallery028/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (170, all pass the validator) |
| `scenegen/` | The generator (0.28.0, placement revision 26); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`) and the seesaw's inset (`SEESAW_IN28`); `library.py` the shadow's two (`SHADOW28`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.28 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v028.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v028.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v028.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all twenty-five screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out028                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out028 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s8023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v028   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v028 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery028 --old-gallery <v0.27 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.28 --single   # the release as one zip, tpdb_v0.28.zip
```

The release is one zip, `tpdb_v0.28.zip`, about 180 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.27 record rebuilds with the v0.27 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- Three templates fall under the legibility gate after the v0.28 screen: `dog_sleeping` (0.67), whose shadow this release changed; `ducks_bread` (0.83) and `dog_wants_walk` (0.83), which it did not touch.
  61 of 64 pass. `vision/flaws_v028.md` lists them and the oddities for v0.29.
- The oddities come in two rows. Readers' remarks per picture are counted directly from their descriptions and compare across
  screens, with the caveat that current readers write about 18% more than the v0.23 readers on the same pictures (`vision/v024/control/`,
  one reader and eight pictures). The row was recounted in v0.26, as the counter had taken bullets saying nothing is wrong for remarks, so its
  figures differ from those published up to v0.25. The scorers' logged oddities do not compare: v0.23's logged 25% of the remarks, v0.24's 83%, and
  from v0.25 the prompt caps them at three per picture. Earlier screens did not record which model read them; v0.24's to v0.28's ran on Claude Opus 5.5. Readers differ widely: on v0.28's nine, from 4.25 to 6.38 remarks a picture.
- No reader says "teenager": he is read as a boy, a boy or young man, or a person, which the key mostly accepts. The v0.24 redraw moved him
  from a woman to a boy, and v0.26's cap worn forwards moved him no further toward the key's own word. It read once as "worn backward or sideways" in v0.27.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 70 pictures 766 of 775 scored items had full marks (743 of 756 in v0.27). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, a v0.24 scorer eleven, and all three scorers of v0.25, v0.26, v0.27 and v0.28 listed such calls, enough to move a template across the gate. A misread is a call too: the
  rake in v0.26's picture 37 could have been marked as sweeping half right.
- Tier-4 pictures are the hardest to place, and revisions 14 to 26 make them harder (walkers' and runners' lanes, pointing
  lines, feet off benches and off other events' things, the photographer's line of sight, the waver's clear hand, body gaps, the gap
  from thin parts, heads clear of figures up to 80 px apart in depth, the ground clear past a reading walker's obstacle, jumpers in the
  front half, an obstacle a full step ahead, runners clear of other movers, ducks off a float, sleepers clear of walkers' feet, nobody in
  the strip before the horizon, a person's box off the lamp post, the ground kept clear round a begging dog). A tier-4 playground plan now holds the bird stealing a sandwich and the
  square wheel, has no swing set as scenery and counts the railing up to 30% hidden, each of which alone placed nothing from 12 seeds, where all three placed 2 (`vision/flaws_v028.md`). So every tier-4 playground has those two, and none
  has the begging dog. A tier-4 street plan holds the bird too, on the evidence of one picture. The tier-4 garden repeats its v0.27 seed.
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
- The planner's priors come from the v0.28 calibration, with f = 0 and a at its centre for every inference and contradiction, as in
  v0.20 to v0.27: the fallen ice cream's cue salience moved by -0.194 and the ball in the tree's by +0.063, the two largest;
  11 fields in 4 templates moved by 0.002 or more.
- Exact rebuilds hold within a release, on the pinned Pillow: the v0.28 cast (builder 0.28.0) and placement rules (revision 26) change faces, shadows and which things count,
  so a v0.27 record rebuilds with the v0.27 package.
- Every variant comes from the v0.28 cast (builder 0.28.0, `out028`): faces with closed eyes or a blush and the bearded man were rendered anew on an installed Blender, and what
  v0.28 did not change was carried over from `lib027`. Some carried variants date from Linux renders, which differ from an installed Blender's
  only in sub-pixel anti-aliasing on the outlines. The library keeps only the 408 variants the v0.28 set and probes use. The bench
  variants (`TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ`, `TPDB_BEARD`, `TPDB_BROW`, `TPDB_BLUSH`, `draw.WHEEL27`, `draw.SPLAT28`, `draw.SEESAW_IN28`, `library.SHADOW28`) stay in the code.
- The figures are still narrow. Legs an eighth shorter and limbs 14% thicker took the bench from eight remarks to three, on four cut-outs a side, but the screen's remarks on
  thin or long bodies did not fall (six pictures to eight in v0.27, and to thirteen in v0.28, with nothing changed, by keyword). A real change of build is a larger job than these.
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
  v0.24 and v0.25, and with it from v0.26. The v0.28 isomorphs are two at tier 2, two at tier 3 and one at tier 4; the tier-4 one
  took 226 failed attempts.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- A shadow from the figure's own footprint is smaller, and a body lying down has little of it showing. The sleeping dog read in full on a wide oval and lost two half marks on the new one; whether the shadow is the cause is not shown (`vision/flaws_v028.md`).
- The trip's meaning item has fallen for two releases, to 0.75, with the obstacle on the line of the stride by rule and by eye: readers have the walker going past it.
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
