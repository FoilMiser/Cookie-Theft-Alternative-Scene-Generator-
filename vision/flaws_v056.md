# v0.56 blind screen: what it found (the work list for v0.57)

The v0.56 screen read the set's 21 pictures and 105 probes with the readers' prompt of v0.55 and the scorers' prompt with one clause added (`screen_prompts.md`). There were sixteen readers, fourteen of eight pictures and two of seven, and five scorers of 25 or 26. The legibility gate passed 63 of the 64 templates, as in v0.55 and v0.54. No item of the 1,320 was scored a misread, and nothing was redrawn, swapped or read again after the screen (below). Keys, descriptions and scores are in `v056/`.

v0.56's brief was Sam's, the whole list of the second part of `flaws_v055.md`: 50 rows from a check of v0.55's 99 pictures by seven reviewers. Each drawing was read blind before it went into scenes, in pairs (46 reviews), in v0.55's own pictures built again and in new ones (268 readings), and in a second round (50 readings); `isolation_v056.md` and `design_tests_v056.md` have the benches. What came of it:
- **the cast is built again** (builder 0.56.0): new drawings of hanging the washing, the child with the dropped cone, the child on the swing, the pan, the feeder's bag, kneeling to plant, the hose's nozzle, the heavy seesaw's two riders and the sleeping dog; new poses for a figure that holds a bicycle, one that throws bread and a bird that pulls;
- **placement revision 50**: the pond's shore and figures kept clear of it, no figure at the picture's bottom edge, the street's sun lower, walkers' lanes, the ladder against open sky, the picnic's larger blanket, the photographer from the side with a subject, and a dozen smaller rules;
- **the scene's drawings**: the bicycle with square wheels held by its owner, the wheelbarrow's square wheel small and open, the hose with a large nozzle, a drop and a seep, the seesaw on stops, the thief bird larger and pulling a slice, pink paint, the parcel, the kite on a limb, colours that stand off in grey;
- **eight of the cast's drawings and four of the scene's were read and not taken**, the seated skirt among them, and a few rows were left with reasons.

**Every picture is new.** The cast and the rules move every figure, so no picture is v0.55's, and the three priors that v0.55 left were taken with all the others from the new calibration. This screen compares with v0.55's by template, not by picture.

## Headline (the 21 pictures of the set)

| | v0.52 (21) | v0.53 (21) | v0.54 (21) | v0.55 (21) | v0.56 (21) |
|---|---|---|---|---|---|
| Things | 0.981 | 0.972 | 0.954 | 0.954 | 0.943 |
| Actions | 1.00 | 1.00 | 1.00 | 1.00 | 0.996 |
| Inferences | 0.955 | 1.00 | 0.984 | 0.953 | 1.00 |
| Contradictions | 0.982 | 0.946 | 0.929 | 0.946 | 0.982 |
| All items | 0.986 | 0.984 | 0.974 | 0.972 | 0.975 |
| Misread items | 0 of 287 | 0 of 286 | 0 of 286 | 1 of 286 | 0 of 277 |
| Readers' remarks per picture (all screened pictures) | 2.46 | 2.62 | 2.71 | 2.44 | 2.73 |
| Oddities per picture, as logged by the scorers | 0.2 (at most 1) | 0.3 (at most 2) | 0.4 (at most 3) | 0.4 (at most 2) | 0.5 (at most 2) |

Eight of the set's 277 items are under full marks: the clouds in six pictures, which their readers left out (16, 42, 63, 88, 89, 91), a half mark on the man who sits on nothing in the tier-4 isomorph (16), and a half mark on the girl who catches the ball in the tier-3 garden (45).

The scorers logged 14 oddities in the set's 21 pictures and 46 in the 105 probes, 0.5 a picture over all 126 (v0.55: 12 and 26 in 99). The readers' own remarks are 2.73 a picture for 2.44.

Across all 126 pictures, 1,292 of the 1,320 scored items had full marks (v0.55: 1,074 of 1,102), and none was misread. The 28 under full marks:
- **Sixteen on the clouds and four on a tree,** all zeros on setting items that a reader left out, from five readers: one left the clouds out of seven of its eight pictures (71 to 77) and another out of four (63, 65, 66, 68). v0.55 had twenty-three such zeros, from five readers. It is a reader's habit and not a drawing's fault.
- **The frying pan, three half marks** in two pictures of five (53, 114). R2.
- **The heavy seesaw, two half marks** on its inference (10, 100). R3.
- **The girl who catches the ball, two half marks** in two pictures of three (45, 86). R1.
- **The man who sits on nothing, a half mark** (16). R4.

The scorers gave three, two, thirteen, nine and one items under full marks, of 278, 266, 261, 253 and 262.

**What the full marks rest on.** The scorers listed 79 judgement calls they scored 1 (22, 7, 8, 19 and 23), for v0.55's 85 in 99 pictures. Not counted, as in v0.55: sixteen marks of a grandparent called an older man or woman, which is what the figure is; and, new, a lead for the leash and two puppies for the dog. The 79 are of two kinds:
- **33 where the target stands beside another reading** (v0.55: 48). By template: the kite in the tree five; the fish in the tree and the begging dog three each; two each for the walked dog, the floating box, the heavy seesaw, the windy hat, the thief bird, the jumper and the walker about to trip; and one each for eight more. Halved, they take nine templates under 0.9: `play_catch` (0.75), `jump` (0.80), `fish_in_tree`, `kite_in_tree` and `walk_dog` (0.833 each), `pan_watering` and `seesaw_heavy` (0.867 each), `dog_begs` (0.875) and `about_to_trip` (0.889). 55 of 64 pass (v0.55: 52).
- **46 on a near word or a target partly said** (v0.55: 37). Thirty-one are a word for a person: the teenager a boy eighteen times, and a grown figure a boy or a girl, or given beside one, thirteen times. With these halved as well, 47 of 64 pass (v0.55: 42).

The five scorers differ in how much they list, so the strict counts compare with v0.55's only roughly (`tools/cycle/strict_count.py`).

## What the screen says of the cast

- **The grown figures.** By the first inventory line that names each figure's clothes, the four grown figures of v0.49's count are called by a young name first in 6 of their 108 pictures (v0.55: 3 of 81): the man in the red shirt in 4 of 24, the woman in purple in 2 of 25, the woman in the yellow dress in none of 31, the man in green in none of 28. The man in the red shirt is a boy as he paints, eats an ice cream walking and seated, and looks into the hose: "- Boy on bench: centre; brown hair, red T-shirt, blue jeans; sitting eating pink ice cream." (42). The woman in purple is a girl as she walks reading and as she looks into the hose: "- Girl, centre: dark hair in ponytail, purple top, teal trousers; holding the hose nozzle up and peering into it." (68). Four readers of sixteen wrote the six, two of them two each. O1.
- **Every animal was named for what it is.** All 19 (template, angle) pairs pass (`v056/gate_yaw.json`). Fifteen oddities were logged of an animal: a goat in a park twice and its rope once, a bird large beside a sandwich or a figure three times, a bird hard to make out twice, one on a lamp that seems to be at a shop's window, a duck near a float, a duck that could be a goose and its wake outside the water, a dog that walks the other way from its walker, and a sleeping puppy that could be playing, or a lamb or a cat.
- **The teenager is a boy**, eighteen times in the scorers' lists. K2's clause did not stop the listing (below).

## The v0.55 list

`R` rows were at the gate or its edge; the counts in brackets are items and pictures.

| v0.55's row | The benches | In v0.56's screen |
|---|---|---|
| R1a: the bicycle with square wheels, under the gate | Held by its owner, 6 readings of 6 named the wheels as wrong; leaning on a post, none of 8 | **`square_wheel` 1.00** (30 items, 10 pictures), five held bicycles and five wheelbarrows, every one in full: "At the far left an older man in a flat cap and brown waistcoat stands holding a teal bicycle whose wheels are square, which is impossible." (119, the tier-4 playground) |
| R1b: the wheelbarrow's square wheel | Small and open on its spokes, 5 of 6; small and solid, 2 of 8 | In full in all five; in one the wheel is named only among the unsure things (73) |
| R2: the heavy seesaw, where the man sits and what the child's hand says | Stops under the plank's ends: his seat doubted in 1 reading of 14 for 2 of 3; the child's arm stretched down | **`seesaw_heavy` 0.933** (15, 5): two half marks where the weight is not given, and his seat is doubted in three pictures of five. Not mended. R3 |
| R3: the thief bird, 0.967 | Larger and pulling a slice: no likelier read as stealing (12 of 24 for 12 of 31), no longer small | **`bird_steals` 1.00** (18, 6), with two full marks beside another reading and three on a near word or a target partly said, for v0.55's half mark and five. The size is remarked four times. O3 |
| R4: the stopped hose, 0.975 | Nozzle, drop and seep with the swelling kept: the dog as the one cause in 8 of 10 for none of 4 | **`blocked_hose` 1.00** (20, 5), with one full mark beside another reading, for v0.55's half mark and five |
| I1: the sprinkler's box | A taped parcel on the path: a parcel to 6 readers of 8 for 1 of 4 | `sprinkler_package` 1.00 (15, 5), no call |
| I2: the dog's lead | A long lead was a garden hose to 8 readers of 10. Not taken | `dog_wants_walk` 1.00 (6, 3), one call: the dog may only be holding it |
| I3: the kite in the tree | On a limb, light in grey: caught, with flying in front beside it, as before | `kite_in_tree` 1.00 (15, 5), with five full marks beside flying in front of the tree, in four pictures of five. Not mended. R5 |
| I4: the stalking cat | A crouch lost twice in pairs; the bird turned away changed nothing. Not taken | `cat_stalks_bird` 1.00 (9, 3), no call |
| I5: what the storm pointer points at | A steeper arm lost in pairs; the bird table kept out of the arm's line: 2 of 2 | `rain_coming` 1.00 (15, 5), one call |
| I6: the windy hat | The hand clear of the gate | `windy_hat` 1.00 (15, 5), two calls, the reach beside a wave; the wind's lines are on the wrong side of the cap to two readers. O5 |
| I7: the walker about to trip | Lowered eyes made no difference in pairs. Not taken | `about_to_trip` 1.00 (9, 3), three calls |
| I8: the upward water | Streaks were a spray. Not taken | `water_upward` 1.00 (9, 3), one call |
| I9: the ladder that leans on nothing | Longer, against open sky: a support offered by none of 2 for 4 of 9 | **`ladder_nothing` 1.00 (15, 5), no call**, where a support was offered in 9 readings of 9 over the last three screens |
| I10: the floating box | No raised hand near it, and no jumper in its picture | `floating_box` 1.00 (15, 5), two calls, for 9 readings of 9 over the last three screens |
| I11: the pan and the bucket | The shallow pan was a frying pan to 8 readers of 8; the bucket's handle lost | **`pan_watering` 0.900** (15, 5): a watering can first to two readers of five. Worse than v0.55's. R2 |
| C1: the seated skirt | Lost two rounds of pairs. Not taken | No oddity was logged of a seated skirt |
| C2 to C4, C6, C7, C9: the feeder's bag, hanging washing, the sleeping dog, planting, the dropped cone, the swing's hands | Taken on pairs, and read as well or better in whole pictures | Each 1.00, with three calls among them. The sleeping puppy could be playing, or a lamb, to two readers |
| C5: the roller and tray | A level roller lost; pink paint and a ribbed tray taken | `paint_fence` and `paint_tracks` 1.00; a roller above the painted part once (65) |
| C8: the seesaw at play nearly level | Tilted fifteen degrees: level to none of 6 for 2 of 3 | `seesaw` 1.00 (10, 5); the stops look odd to one reader (44) |
| C10 to C12: the stride, the faces, the teenager | Not taken, or not drawn | The teenager is a boy in eighteen calls |
| P1: figures over the pond | The shore, and other events clear of it: a doubt in none of 10 readings | Three pictures, each the pond's own figure, a bread thrower or an angler (57, 72, 118). O2 |
| P2 to P4, P6, P8: the bottom edge, the sun, hoses, the pram, the picnic | Rules | No remark on any |
| P5: a figure in another event's way | Lanes, the float's gap, the jumper's exclusions | A duck by the float once (62) and a kite's string by a digger once (114) |
| P7: the ball's trail | A trail only behind the ball lost the thrower. Not taken | **`play_catch` 0.833, under the gate**, on v0.55's drawing. R1 |
| P9: what the photographer photographs | From the side, a subject near and alone on that side | `photo` 1.00 (5, 5), no call and no oddity |
| P10: singles | Rules; the painter's long step not mended | The roller above the painted part (65) |
| G1 to G8: grey | Colours changed; each record now says whether every scored thing stands off in grey | The screen is read in colour. 121 of the 126 records pass the check and five are flagged. G1 below |
| K1: fixed pronouns in accepted phrases | By the figure | Done |
| K2: who-words listed as calls | A clause in the scorer's prompt | Three scorers of five still listed them, 18 of the teenager and 16 of a grandparent: an action item's accepted phrasings do not hold its figure's names, so the clause had nothing to match. K1 below |
| K3: the setting's items | The pilot's rule | Twenty zeros, as every screen |
| K4: words the drawing does not carry | The cone child looks at the cone; bread is thrown | `ducks_bread` 1.00 (15, 5), five calls on a target partly said (pieces of food, the duck's motive) |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

Every template was screened in at least three pictures (15 in three, 12 in four, 26 in five, 4 in six, 2 in seven, and one each in eight, nine, ten, sixteen and twenty-two). 63 of 64 pass.

| Template | Mean | Items | Pictures | Verdict |
|---|---|---|---|---|
| `play_catch` | 0.833 | 6 | 3 | **fail** |
| `pan_watering` | 0.900 | 15 | 5 | pass |
| `seesaw_heavy` | 0.933 | 15 | 5 | pass |
| `sitting_on_air` | 0.958 | 12 | 4 | pass |
| the other 60 | 1.00 | | 3 to 22 | pass |

**The failure is a drawing v0.56 did not change, in pictures it did.** The game of catch is v0.51's: the ball a third of the way along its arc at the end of a dashed line from the thrower's hand. It read 1.00 in v0.55's five pictures. v0.56 screened it in three, since nothing of it had changed, and in the two gardens the ball is at the height of the fence's top with the catcher below it: "- The red ball thrown by the boy is heading up and to the left, away from the girl, who has her arms out to the right of him; it is unclear whether she is meant to be catching it (the throw seems to be going the wrong way/over the fence) or just reaching for something else." (45) and "- The ball's direction: it is going up and to the right, well above the girl's hands. Could be read as a throw to the girl that is going too high (over her head / over the fence), or as a throw at the cat on the fence." (86). The third picture, in the street, read in full, with the ball very high for the catcher among its oddities (116). With three pictures one half mark is 0.917 and two are 0.833.

**The four rows that were at the gate pass.** `square_wheel`, which failed in v0.52, v0.54 and v0.55, reads 1.00 in ten pictures, the tier-4 playground's among them; `bird_steals` and `blocked_hose` read 1.00 for 0.967 and 0.975; `seesaw_heavy` is under 1.00 where it was at it.

## After the screen

Nothing was mended, swapped or read again. The count is the first and only one.

## What reads least well (the v0.57 list)

| | Template | v0.56 | What the readers wrote | For v0.57 |
|---|---|---|---|---|
| R1 | `play_catch` | 0.833 (6 items, 3 pictures), under the gate; 0.75 on the strict count | "- The ball's direction: it is going up and to the right, well above the girl's hands. Could be read as a throw to the girl that is going too high (over her head / over the fence), or as a throw at the cat on the fence." (86) | The ball stands high above the catcher's hands, and in a garden it stands on the fence's top line. Bench a flatter arc with the ball between the two players' heads, and a rule that keeps the ball and its trail off the fence's top line and away from a cat on the fence; five pictures in the next screen, as before v0.56. The bench of v0.56 already had the thrower doubted in 1 reading of 4 of this drawing |
| R2 | `pan_watering` | 0.900 (15 items, 5 pictures), on the gate's line; 0.867 on the strict count | "- The watering can the boy holds is dark grey and fairly flat; it could be read as a frying pan or a pot rather than a watering can, though the water pouring from it makes "watering can" the likely reading." (53) | New in v0.56, and the bench did not show it: eight readers of eight had the shallow pan a frying pan, and here two of five have a watering can first and a third offers a ladle. v0.55's deep pan was a pot or a saucepan to most and still the wrong thing to water with. Bench the two pans again in whole pictures with eight readers or more an arm, and a third with the pan's flat inside turned to the viewer and the water leaving over its rim |
| R3 | `seesaw_heavy` | 0.933 (15 items, 5 pictures); 0.867 on the strict count | "- The old man appears to be sitting on the seesaw end but his feet are on the ground and his body is quite far forward of the seat; he could be read as sitting on the plank or just leaning/perched on it." (51) | Two half marks where the reader has the man ignoring the child and does not give his weight (10, 100), and his seat doubted in three pictures of five (10, 51, 92). The stops did less in the screen than in the bench. What is left is the list's other proposal: a seat on the plank that shows behind his hips, and the child's end with nothing she could climb down by |
| R4 | `sitting_on_air` | 0.958 (12 items, 4 pictures) | "- The seated elderly man on the left: I can't see a chair, stool or bench under him; he appears to be sitting on nothing (could be a missing seat, or something hidden I can't make out)." (16) | One half mark, in the tier-4 isomorph, where the sitter is small and at the picture's left edge. Watch |
| R5 | `kite_in_tree`, `fish_in_tree`, `walk_dog`, `jump`, `dog_begs`, `about_to_trip` | 1.00 each; 0.80 to 0.889 on the strict count | "- The bird could be eating the sandwich or just standing next to it; it looks like it is pecking at it." (17, of the thief bird) | Each reader gives the target as the likelier reading. The kite is there a second screen running, after a new drawing that the bench had already found no better; the fish in the tree is new on the count, a toy or an ornament to three readers |

## Unintended oddities

Grade A is a remark in five or more pictures, or one that touches what a figure is; B in three or four; C in one or two.

| | Grade | What the readers wrote | Pictures | For v0.57 |
|---|---|---|---|---|
| O1 | A | Grown figures called young first, 6 of 108: the man in the red shirt a boy in four of his 24 pictures, the woman in purple a girl in two of her 25 | 40, 42, 68, 90, 106 (both) | Double v0.55's share, on new pictures; two readers wrote four of the six. The man in the red shirt is a boy eating an ice cream twice: count by pose (`tools/cycle/who_pose.py`) before drawing |
| O2 | B | The pond's own figures over its rim: "- The man stands on the pond's rim, and his lower body overlaps the water's edge. He could be standing just in front of the pond or partly in it." | 57, 72, 118 | Revision 50 keeps the figures of other events clear of the pond and left the bread thrower and the angler where they were. The list's P1 asked for their feet a clear step below the rim: do that |
| O3 | B | The thief bird and its sandwich are large: "- The blue bird is quite large relative to the sandwich; it could be read as stealing the sandwich or just pecking at it." and a lifted slice that could be floating bread | 60, 65, 89, 119 | The size was the list's own mend, and the remark is not a misreading. Leave, or draw the sandwich a little smaller than the bird |
| O4 | B | The heavy seesaw's man perched on the plank's end (R3); the seesaw's stops as small dark blocks, the high end's far below the plank | 10, 44, 51, 92 | With R3 |
| O5 | B | The wind's lines beside the cap they blew: "the wind streaks are on the far side of the blowing cap", a cap that flies ahead of them, washing blown at a steep angle, lines over the pond read as ripples | 13, 66, 95, 126 | The lines follow the cap in two pictures and lead it in two. Draw them behind the cap, on the side it came from, and off the pond |
| O6 | C | One or two pictures each: a duck by the angler's float (62); a kite's string close to a man digging (114); the sleeping puppy rolled over as if to play (69) or like a lamb or a cat (93); the seep at the reel as a leak (4) and a girl who could be drinking from the nozzle (68); the roller above the painted part (65); the sprinkler's arcs as separate lines (1); soil on a spade like a bag (3); a very short hose (7); a bottle like wine beside a child's picnic (12); a walker and a dog facing two ways (12); a fork held under the arm (16); an empty park (38) and sparse playgrounds (69, 75); a man's feet at the fence's line (51); a bird hard to make out (59, 63); seeds like a string (59); a child small for the slide (75) or the seesaw (113); a face hard to read (85); a bird on a lamp before a shop window (88); a box held at one side (91); a leg behind a bicycle's frame (115); a catcher's arms toward the thrower (116); a goat's rope across its leg (117); a girl who hovers on the seesaw's high end (120); a goat in a park (19, 103) | as given | None is in three pictures |
| O7 | C | Notes for the pilot: the setting's clouds and trees are left out by some readers and named by others (20 zeros; 23 in v0.55) | 20 items | None for the drawing. The pilot's scoring should say whether setting items count |

## Keys and scoring

| | What | For v0.57 |
|---|---|---|
| K1 | The scorers cannot see which who-words an item accepts: `keys.json` gives an action item its text and its accepted phrasings for the action, and the figure's accepted names are in the record only. K2's clause asked them to leave accepted names out of their calls, and three of five listed the teenager's boy and the grandparents' older man or woman all the same (34 marks) | Write each figure's accepted names into the item of `keys.json` (`vision/prepare_screen.py`), so that the clause has something to match and the strict count stops resting on a hand's sorting |
| K2 | The strict count's two lists are sorted by hand from five scorers' prose, and the scorers differ fourfold in how much they list (7 to 23) | Ask for the list as a JSON field beside each score: a flag for a target beside another reading and a flag for a near word |

## Grey

The build's check (`compose.grey_check`) asks of every scored thing, cue and prop of at least 150 px that 35 % of it be 20 grey levels or more from what is round it; it records its verdict and fails no picture.

| | What | Where | For v0.57 |
|---|---|---|---|
| G1 | Five records of 126 are flagged: the hat the wind took in two parks (grey 152 on grass at 168 and on the pond at 141), the box or bucket in the walker's way in two pictures (153 on 168), and the boards a dog's painter has painted pink in one (134 on boards at 142) | 31, 65, 66, 80, 126 | A cap and an obstacle of a darker or a lighter colour; and the pink of the paint, which v0.56 chose so that no door has it, is the unpainted boards' own grey: take a pink that is lighter, or a deep one. Then let the check fail a layout (`GREY` `B`) |

## Placement

Revision 50 (`scenegen/scene.py`, its header comment, and `design_tests_v056.md`). The showcase pass placed eleven of the twelve cells of tiers 1 to 3 on their showcase seeds and the tier-3 garden on a seed search past its own. Of the four tier-4 cells two came from the free search, the park on its fifth base and the playground on a second range of seeds, and two were built from forced sets after the free search failed, the garden from v0.46's set as in v0.53 to v0.55 (fourteen bases) and the street from v0.55's set with the dog that reads a newspaper in place of the man who sits on nothing (46 bases): the bicycle with square wheels now has an owner, a ninth figure in a street that had room for eight. Four isomorphs of tiers 2 and 3 came from two passes and the tier-4 isomorph, from the park to the street, after more than a hundred tries. The probes came in four passes: 65, 27 in small forced groups for the fourteen templates the first pass left short (the playground's own had no picture at all, each group of three asking for more children than the cast's two), eight by angle and five forced for the square wheel's two carriers, 105 in all. All 126 records rebuild to the pixel. The calibration moved in 85 of its 252 numbers and every prior was taken from it (`README.md`).
