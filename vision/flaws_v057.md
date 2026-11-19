# v0.57 blind screen: what it found (the work list for v0.58)

The v0.57 screen read the set's 21 pictures and 115 probes with the readers' prompt of v0.48, unchanged, and a scorers' prompt that asks for a flag beside each score (`screen_prompts.md`). There were nineteen readers, fifteen of eight pictures, two of seven and two of one, and six scorers, five of 26 or 27 pictures and one of two: the tier-4 park and its isomorph were found after the screen of the other 134 pictures had begun, and were read and scored as pictures 135 and 136. The legibility gate passed all 64 templates, for 63 in v0.56, v0.55 and v0.54. No item of the 1,435 was scored a misread, and nothing was redrawn, swapped or read again after the screen (below). Keys, descriptions and scores are in `v057/`.

v0.57's brief was Sam's: "Go for v0.57", the list of `flaws_v056.md`. Each drawing and each rule was read blind before it went into scenes, in v0.56's own pictures built again and in new ones (125 readings, then 50 in a second round); `isolation_v057.md` and `design_tests_v057.md` have the benches. What came of it:
- **the game of catch** has a flat flight, kept off the fence's top line and away from a cat on it, and its catcher is a child or a teenager, the taller of the two throwing;
- **the frying pan** is hollow and dark inside on a wooden handle, the water leaves over its rim as a sheet, and an unused watering can stands on the grass behind the holder;
- **the heavy seesaw's** man has no book and looks up at the child, and the seesaw has seats and rubber buffers;
- **the kite's string** lies on the grass; the pond's own figures stand lower on the lawn; in a park the blown cap is off the pond; the paint is a deeper pink, the walker's box darker, an orange cap purple;
- **the key** lists the names each figure may be called by, and the scorers flag their judgement calls.

**A like-for-like release.** The planner's priors were left at v0.56's and every record of v0.56 was built again under revision 51 from its own regeneration data (`tools/cycle/carry_over.py`). Of v0.56's 126 pictures, 65 came back to the pixel and 17 more within 24 pixels (three sprites of the new library differ from the old by a pixel); 41 were drawn again or moved, each with its own templates; three were replaced, the tier-4 park, its isomorph and one plain seesaw; and ten probes were added, so that every changed template is in five pictures or more. `v057/carry_over.json` says which is which.

## Headline (the 21 pictures of the set)

| | v0.53 (21) | v0.54 (21) | v0.55 (21) | v0.56 (21) | v0.57 (21) |
|---|---|---|---|---|---|
| Things | 0.972 | 0.954 | 0.954 | 0.943 | 0.926 |
| Actions | 1.00 | 1.00 | 1.00 | 0.996 | 1.00 |
| Inferences | 1.00 | 0.984 | 0.953 | 1.00 | 1.00 |
| Contradictions | 0.946 | 0.929 | 0.946 | 0.982 | 1.00 |
| All items | 0.984 | 0.974 | 0.972 | 0.975 | 0.971 |
| Misread items | 0 of 286 | 0 of 286 | 1 of 286 | 0 of 277 | 0 of 277 |
| Readers' remarks per picture (all screened pictures) | 2.62 | 2.71 | 2.44 | 2.73 | 2.47 |
| Oddities per picture, as logged by the scorers | 0.3 (at most 2) | 0.4 (at most 3) | 0.4 (at most 2) | 0.5 (at most 2) | 0.3 (at most 2) |

Eight of the set's 277 items are under full marks, and all eight are the setting's: the clouds in seven pictures (17, 20, 21, 23, 57, 61, 118) and a tree in one (17), which their readers left out. Every item of an event, an inference or a contradiction in the set has full marks.

The scorers logged 12 oddities in the set's 21 pictures and 25 in the 115 probes, 0.3 a picture over all 136 (v0.56: 14 and 46 in 126, 0.5). The readers' own remarks are 2.47 a picture for 2.73.

Across all 136 pictures, 1,391 of the 1,435 scored items had full marks (v0.56: 1,292 of 1,320), and none was misread. The 44 under full marks:
- **Thirty-six on the clouds and four on a tree,** all zeros on setting items that a reader left out, from eight readers: one left the clouds out of all eight of its pictures (14 to 21) and four more out of five to seven. v0.56 had twenty such zeros, from five readers. It is a reader's habit and not a drawing's fault.
- **The wheelbarrow's square wheel, two half marks** in one garden (38). R1.
- **A man called a boy, two half marks** on the man's own action, carrying a bag (120) and painting the fence (125), from one scorer of six. K1.

The scorers gave twelve, two, eleven, five, fourteen and none under full marks, of 292, 292, 300, 249, 254 and 48.

**What the full marks rest on.** The scorers flagged 67 full marks as judgement calls (12, 8, 19, 10, 14 and 4), for v0.56's 79 in 126 pictures, which were sorted by hand from their prose. The 67 are of two kinds:
- **57 where the target stands beside another reading** (v0.56: 33). By template: the lost balloon seven; the stalking cat, the floating box and the windy hat five each; the kite in the tree and the upward water four each; the thief bird, the dog at the door and the ice cream three each; two each for the heavy seesaw, the ball in the tree, the stopped hose, the fork, the walker about to trip and the playing dog; and one each for six more. Halved, they take ten templates under 0.9: `dog_wants_walk` (0.75), `water_upward` (0.778), `cat_stalks_bird` (0.792), `floating_box`, `lost_balloon` and `windy_hat` (0.833 each), `dog_playing` (0.857), `plant_flowers` (0.875), `kite_in_tree` and `sweep_fork` (0.889 each). 54 of 64 pass (v0.56: 55).
- **10 on a near word or a target partly said** (v0.56: 46, thirty-one of them a word for a person). Three are the heavy seesaw's, where the weight is given and "stuck" is not said; two each the wheelbarrow's square wheel and the stopped hose; one each the thief bird, the ducks and the ice cream. Two of the ten are a word for a person. With these halved as well, 51 of 64 pass (v0.56: 47).

The flags are the scorers' own, by a rule they were given, and the six differ in how much they flag (from four of each kind to eighteen and one), so the strict counts compare with v0.56's only roughly (`tools/cycle/strict_count.py`).

## What the screen says of the cast

- **The grown figures.** By the first inventory line that names each figure's clothes, the four grown figures of v0.49's count are called by a young name first in 5 of their 117 pictures (v0.56: 6 of 108): the man in the red shirt in 3 of 26, the woman in purple in 2 of 28, the woman in the yellow dress in none of 33, the man in green in none of 30. It is the activity again: the man in the red shirt is a boy as he carries a shopping bag, paints the fence and eats an ice cream, and the woman in purple a girl as she looks into the hose and eats an ice cream. "- Left-centre: boy with brown hair in red T-shirt and blue jeans, painting the fence pink with a roller." (125). O1.
- **What a young name costs now.** With the figure's names in the key, a man called a boy is no longer credited in silence: one scorer gave two half marks for it, two flagged it as a near word, and one flagged "a girl or young woman" as two readings. K1.
- **Every animal's item has full marks.** All (template, angle) pairs pass (`v057/gate_yaw.json`). Twelve oddities were logged with an animal in them: a goat in a park twice, its rope once, and once it could be a sheep; a bird large beside a sandwich, on a bench or against the clouds, three times; a bird that could be an object twice; a cat large for its fence; a curled dog hard to read; and a dog walked on the grass beside the path.
- **The teenager is a boy**, and is no longer a call: the key shows the scorers that the item accepts it.

## The v0.56 list

`R` rows were at the gate or its edge; the counts in brackets are items and pictures.

| v0.56's row | The benches | In v0.57's screen |
|---|---|---|
| R1: the game of catch, 0.833 and under the gate | The flat flight: no doubt in 4 readings of 6, for none of 6; the catcher young: who threw it asked in 2 of 10, for 4 of 8 with a grown catcher | **`play_catch` 1.00** (12, 6), with no call: "A boy in a red cap and blue hoodie has thrown a red ball (dotted arc line) toward a small girl in a pink dress, who has her arms out to catch it." (61). One oddity: "- The ball and the thrower's hand are drawn at fence height against the fence, but read as in front of it." (101) |
| R2: the frying pan, 0.900 | The hollow pan with a dark inside: a watering can first in 1 reading of 20; with an unused can beside the holder, a frying pan in 20 of 20 | **`pan_watering` 1.00** (15, 5), with no call. The can is logged as an oddity once, and it is the cue: "- Using a frying pan to water the plants is odd/wrong, especially with a watering can nearby; it looks deliberate." (4) |
| R3: the heavy seesaw, 0.933 | Without the book his weight is given in 6 readings of 10 and then 10 of 10, for 1 of 10 with it; where he sits is doubted in 9 of 10 with either seat | **`seesaw_heavy` 1.00** (15, 5), with five calls: twice he may hold her up on purpose, and three times his weight is given and she is not said to be stuck: "That balance makes sense because he is much heavier." (24). His seat is doubted once, a child's twice. R3 |
| R4: the man who sits on nothing, 0.958 | Not benched | `sitting_on_air` 1.00 (9, 3), no call. The tier-4 isomorph that held the half mark was replaced |
| R5: the kite in the tree | The string on the grass: stuck with nothing beside it in 6 readings of 8, for none of 8 | `kite_in_tree` 1.00 (18, 6), with four calls in three pictures of six, for five in four of five: flying in front of the tree twice, and "or the child is about to launch it" once. Two oddities of the string. R2 |
| R5: the fish in the tree, the walked dog, the jumper, the begging dog | Looked at and left | No call on any of the four in this screen; two on the walker about to trip, as before |
| O1: grown figures called young first | Counted by pose; nothing drawn | 5 of 117 for 6 of 108. O1, K1 |
| O2: the pond's own figures over its rim | Standing lower: over the rim in 1 reading of 8 for 7 of 8 | No remark on a bread thrower or an angler in their eleven pictures. One figure of another event has her head over the pond's edge (100) |
| O3: the thief bird's size | Left | Remarked twice (3, 59); `bird_steals` 1.00 (18, 6) with four calls |
| O4: the seesaw's stops | Buffers under the plank's ends | No remark on a buffer. The seats: R3 |
| O5: the wind's lines | Off the pond in a park | No oddity of the wind in five pictures; `windy_hat` has five calls, the cap tossed or the hand waving |
| K1: the figure's names in the key | Written into every action item | Calls on a near word 10 for 46 |
| K2: calls as flags | A flag beside each score | 67 flags; the six scorers differ. K2 |
| G1: five grey flags | New colours; the check refuses a layout | All 136 records pass the check |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

Every template was screened in at least three pictures (12 in three, 11 in four, 17 in five, 12 in six, 6 in seven, 2 in eight, and one each in ten, twelve, sixteen and twenty-two). 64 of 64 pass, for the first time since v0.53.

| Template | Mean | Items | Pictures | Verdict |
|---|---|---|---|---|
| `carry_bag` | 0.938 | 8 | 8 | pass |
| `paint_fence` | 0.958 | 12 | 12 | pass |
| `square_wheel` | 0.967 | 30 | 10 | pass |
| the other 61 | 1.00 | | 3 to 22 | pass |

**The four templates that v0.56 had under 1.00 read 1.00.** Their eight half marks of v0.56 are all full marks now: the catcher in two gardens, the frying pan in two pictures, the heavy seesaw's inference in two, and the man who sits on nothing (in a picture that was replaced). Item for item in the 41 pictures that were drawn again or moved, 410 of 436 items have the score they had, eleven are higher and fifteen lower; sixteen of the 26 are the clouds or a tree, seven are those mends, and three are new: the wheelbarrow's wheel twice and a painter called a boy (`tools/cycle/retest.py`).

**A second reading of 82 pictures.** In the 82 pictures that are v0.56's to within a few pixels, 791 of 823 items have the score they had, ten are higher and 22 lower. Thirty-one of the 32 are the clouds or a tree; the other is the man with the shopping bag, called a boy by this reader and a man by v0.56's.

## After the screen

Nothing was mended, swapped or read again. The count is the first and only one.

## What reads least well (the v0.58 list)

| | Template | v0.57 | What the readers wrote | For v0.58 |
|---|---|---|---|---|
| R1 | `square_wheel` | 0.967 (30 items, 10 pictures); the wheelbarrow hedged in three of its five pictures | "- The wheelbarrow's wheel looks square or boxy with a cross inside rather than round. It may just be a stylised wheel seen from an angle, or it may be an odd shape." (38) | Two half marks in one garden, a near word in the tier-4 garden (40) and a second reading in a third (130); the other two barrows and the five bicycles are in full. The barrow is v0.56's in all five pictures (two of them have only their paint drawn again), and v0.56's readers had all five in full: the small open wheel is at its edge, and one reader's doubt moves it. Bench it again beside a wheel with a rim as thick as the bicycle's |
| R2 | `lost_balloon`, `cat_stalks_bird`, `floating_box`, `windy_hat`, `water_upward`, `dog_wants_walk`, `kite_in_tree` | 1.00 each; 0.75 to 0.889 on the strict count | "- The kite string goes down to the ground and loops before rising to the kite. It reads as a slack string lying on the grass, but it is a little odd that it touches the ground between the boy and the tree." (76) | Each reader gives the target as the likelier reading and sets another beside it: the balloon may never have been hers (6 pictures of 7), the cat may only be walking (4 of 4), the box may be thrown or falling (4 of 5), the cap tossed or the hand waving (4 of 5), the water a hose or a stylised pour (3 of 3), the lead a toy (2 of 3). The kite's string helped (calls in three pictures of six for four of five), and a child who holds the reel up over a slack line is the next thing to draw: a hand that has let the reel drop |
| R3 | `seesaw_heavy` | 1.00 (15 items, 5 pictures); 0.833 with all its calls halved | "- The man appears to be sitting on the end of the plank rather than squarely on the yellow seat." (52) | Without the book the weight is given, and the tilt is then what a reader expects: in two pictures of five she is not said to be stuck, and in three he may be holding her up on purpose. Her arm stretched toward him is all that says she wants down. And the seat, after two rounds of the bench: he is in front of it to nine readers of ten. Both are drawings of the pose, not of the seesaw: his hips against the seat's back with the thighs along the pad, and the child gripping the handle with both hands and leaning back |

## Unintended oddities

Grade A is a remark in five or more pictures, or one that touches what a figure is; B in three or four; C in one or two.

| | Grade | What the readers wrote | Pictures | For v0.58 |
|---|---|---|---|---|
| O1 | A | Grown figures called young first, 5 of 117: the man in the red shirt a boy in three of his 26 pictures, the woman in purple a girl in two of her 28 | 22, 81, 100, 120, 125 | As v0.56 found by pose: the ice cream (22, 100), the hose's nozzle (81), and now a shopping bag and the paint roller. The share holds at about one picture in twenty over three screens. With K1 it is what costs marks now |
| O2 | B | A rider a little off its seat: "- The girl on the high end appears to sit slightly in front of or beside the seat handle rather than clearly on the seat; her placement looks a little floating." and the same of a child on a slide's chute | 7, 52, 79, 98, 131 | The seats are new and the children sit above their pads; the slide's is v0.55's. With R3 |
| O3 | B | Water at the hose reel: a leak, a puddle of unclear cause | 36, 40, 105 | The seep is the cue that the tap is on (v0.56's bench: the dog the one cause in 6 readings of 8 with it, 3 of 8 without). Left; it is a remark and not a misreading |
| O4 | B | A goat tethered in a park is unusual; its rope hard to follow | 13, 108, 135 | As v0.56. Left |
| O5 | B | A bird large for what is beside it, or small and like an object | 3, 8, 59, 99 | As v0.56 |
| O6 | C | The kite's reel held up over a slack line (64, 76); the ball and the throwing hand at the height of the fence's rails (101); a figure of another event with her head over the pond's edge (100); a walker and a dog, or a man with a pram, on the grass beside the path (54, 133); a lamp post missing where the ladder stands (26); a watering can half sunk in the grass (35); a swing's ropes at a slant (56); a picnicker's open mouth (68); a rock (98); a leaf pile with no fallen leaves round it (99); a barrow's handles and tray (130); a roller loose in the hand (136); the beach ball's branch drawn on top of the leaves (61); a cat large for its fence (61); a curled dog hard to read and a foot on the sandpit's rim (82); leaf clumps round the kite (97) | as given | None is in three pictures |
| O7 | C | Notes for the pilot: the setting's clouds and trees are left out by some readers and named by others (40 zeros; 20 in v0.56) | 40 items | None for the drawing. The pilot's scoring should say whether setting items count |

## Keys and scoring

| | What | For v0.58 |
|---|---|---|
| K1 | The key now shows which names a figure accepts, and the rule does not say what a name outside them costs. A man called a boy was a half mark to one scorer (120, 125), a full mark flagged as a near word to two (22, 81), and "a girl or young woman" two readings to a fourth (100) | Say it in the scorer's prompt: the action is scored on the action, and a who-word outside the item's names is flagged in a field of its own. Then the young-first count can be read from the scores |
| K2 | The flags work and the scorers still differ: 12, 8, 19, 10, 14 and 4 flags, from four of each kind to eighteen and one. Fifty-seven are a second reading in the unsure section | The prompt's `sets another reading beside the target` takes in every hedge of the unsure section. Split the flag: another reading in the description or the inventory, and one only in the unsure section. The strict count should halve the first alone |

## Placement, priors and the tier-4 isomorph

Revision 51 (`scenegen/scene.py`, its header comment). Every cell but the tier-4 park was carried over from v0.56's record: fifteen cells on their seeds with their templates, six of them to the pixel and two more within a pixel, and four of the five isomorphs.

- **The tier-4 park.** v0.56's cell held the kite in the tree and no longer places with the string on the grass. A free search found a new cell on its ninth base, whose set holds three inferences of one class and so has no isomorph in any setting (`batch.iso_map`); and 260 tries from the street's and the playground's cells placed none, as about 120 had in v0.56. The cell and its isomorph were then searched for together (`tools/cycle/t4_cell_iso.py`): a park on base 905959, its thirty-fourth step, with an isomorph in the garden on its fourth seed. For v0.58: the planner could refuse a tier-4 plan whose set cannot be cast in a second setting.
- **The priors were left.** The calibration measured with the new cast under revision 51 moved in 19 of its 252 numbers. By it four priors would change a little: `windy_hat` (salience -1.28 to -1.32), `ducks_bread` (-1.34 to -1.36), `seesaw_heavy` and `kite_in_tree` (their distance terms by 0.003 and 0.001). And `pan_watering`'s prior has no second cue, though its items now have the unused can (their predicted difficulty is 0.30 lower). A release that builds a new set should take all five.
- **Not done:** the garden fence's two rails have no anchor, and the flat ball can stand on one (101).
