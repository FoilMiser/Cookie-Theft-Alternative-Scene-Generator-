# v0.51 blind screen: what it found (the work list for v0.52)

The v0.51 screen read the set's 21 pictures and 81 probes with the prompts of v0.50 (`screen_prompts.md`). There were thirteen readers, eleven of eight pictures and two of seven, and four scorers of 25 or 26. The legibility gate passed all 64 templates, where it had passed 62 in v0.50, 64 in v0.49 and 63 in v0.48 and in v0.47. No item of the 1,114 was misread, and nothing was redrawn, swapped or read again after the screen (below). Keys, descriptions and scores are in `v051/`.

v0.51 worked the list of `flaws_v050.md` on Sam's "go for v0.51!". The work is in the placement rules (revision 48) and in three poses of the cast (builder 0.51.0), each change read on a bench against v0.50's drawing before it went in (`isolation_v051.md`):
- **the game of catch** (R1, under the gate in v0.50): the ball early on its path, a third of the way from the thrower's hand, and a catcher with two open hands; chosen on a bench in whole scenes;
- **the square wheel on the wheelbarrow** (R2, under the gate in v0.50): no hose by the barrow, and four pictures of the barrow in the screen where v0.50 had one;
- **the bread for the ducks** (R5): a slice of bread in the feeder's hand;
- **the lost balloon's string** (O1): its end off the fence's rails, the backdrop's lines and the pond;
- **the fence painter** (O3): the tin at the heel, the roller's caps dark;
- **the stopped hose under storm clouds** (O7): no longer planned together;
- tried on the bench and not taken: the swelling of the stopped hose ending short of the paw (R4), and a wider moustache for the man in the red shirt (O2). Looked at and left: R3, R6, O4 to O6 and O8.

Seven of the sixteen cells have v0.50's templates, the tier-4 park, street and playground on v0.50's seeds among them; the other nine are new sets. Six pictures of the 102 are v0.50's to the pixel.

## Headline (the 21 pictures of the set)

| | v0.47 (21) | v0.48 (21) | v0.49 (21) | v0.50 (21) | v0.51 (21) |
|---|---|---|---|---|---|
| Things | 0.985 | 0.990 | 0.917 | 0.911 | 0.944 |
| Actions | 1.00 | 0.996 | 1.00 | 0.980 | 0.996 |
| Inferences | 0.968 | 0.985 | 0.985 | 0.953 | 0.985 |
| Contradictions | 1.00 | 1.00 | 1.00 | 0.942 | 1.00 |
| All items | 0.991 | 0.993 | 0.967 | 0.949 | 0.976 |
| Misread items | 1 of 283 | 0 of 276 | 0 of 284 | 1 of 285 | 0 of 287 |
| Readers' remarks per picture (all screened pictures) | 2.66 | 2.38 | 2.32 | 2.72 | 2.59 |
| Oddities per picture, as logged by the scorers | 0.3 (at most 1) | 0.1 (at most 1) | 0.2 (at most 2) | 0.6 (at most 3) | 0.3 (at most 1) |

The set's 0.976 is above v0.50's 0.949. Eight of its 287 items are under full marks. Six are the clouds, which a reader did not mention (pictures 16, 19, 30, 42, 62, 94); the other two are the stopped hose's two half marks in one picture, the tier-3 garden (62). The game of catch, the square wheel, the thief bird and the bread for the ducks, which had nine of v0.50's eighteen, have none.

The scorers logged 6 oddities in the set's 21 pictures and 26 in the 81 probes, 0.3 a picture over all 102 (v0.50: 13 and 19 in 90, 0.4 a picture). The readers' own remarks are 2.59 a picture for 2.72.

Across all 102 pictures, 1,067 of the 1,114 scored items had full marks (v0.50: 946 of 992), and none was misread. The 47 under full marks:
- **Thirty-three on the clouds and eleven on a tree,** all zeros on setting items that a reader left out. One reader left the clouds out of all eight of its pictures (14 to 21) and a second out of all eight of its own (54 to 61), a third out of seven of eight (78, 80 to 85), a fourth out of six of eight (62 to 64, 66, 68, 69), and four more out of one each (4, 30, 42, 94). The eleven trees are the same four readers'. v0.50 had thirty-five such zeros, from six readers. It is a reader's habit and not a drawing's fault.
- **The stopped hose, two half marks** in one picture (62). R1.
- **An ice cream, one half mark** (47). R2.

The scorers gave 13, three, 21 and ten items under full marks, of 282, 290, 293 and 249.

**What the full marks rest on.** The scorers listed 95 judgement calls they scored 1 (22, 19, 18 and 36), for v0.50's 82 in 90 pictures. The 95 are of two kinds:
- **44 where the target stands beside another reading**, in the description or in its unsure section (v0.50: 33). By template: the floating box five; the stalking cat and the thief bird four each; the sleeping dog, the dog that wants a walk, the planted flowers and the blown hat three each; the kite in the tree, the stopped hose, the storm watcher, the lost balloon and the game of catch two each; and one each for nine more. Halved, as the scoring rule's "only offered as one of two readings" read strictly, they take eight templates under 0.9: `dog_sleeping` and `plant_flowers` (0.7, five items each), `floating_box` (0.722), `cat_stalks_bird` and `windy_hat` (0.833), `dog_wants_walk` (0.85), `rake` (0.875, four items) and `bird_steals` (0.889). 56 of 64 pass (v0.50: 52).
- **51 on a near word or a target partly said** (v0.50: 49). Twenty-three are a word for a person: the teenager a boy eight times, the grandparents an older man or woman nine times, the man in the red shirt a boy three times, the woman in purple a girl twice and once a "young woman or teenage girl". Seven are the square wheel, named only among the unsure things or without its consequence (R4). With these halved as well, 42 of 64 pass (v0.50: 35).

The gate's 64 is therefore the count under the rule as the scorers applied it. The strict counts show how many of the full marks carry a hedge (`tools/cycle/strict_count.py`).

**Six pictures came back identical, and their scores with them.** Two set pictures, three probes and the tier-4 isomorph are v0.50's to the pixel. Of their 71 items, 70 have the score they had in v0.50; one went down, the clouds of a probe, left out by its reader.

## What the screen says of the cast

- **The grown figures.** By the first inventory line that names each figure's clothes, the four grown figures of v0.49's count are called by a young name first in 5 of their 85 pictures (v0.50, by the same rule: 3 of 79): the woman in purple in 3 of 25, the woman in the yellow dress in none of 23, the man in the red shirt in 2 of 12, the man in green in none of 25. The five: "Girl sweeping (left, front): dark hair in a ponytail, purple top, teal trousers; sweeping a pile of leaves with a yellow broom." (42), and the same woman walking with an ice cream (47) and pointing at the storm (51); "Right, front: boy in red shirt and blue jeans sitting on a wooden bench, reading a red book." (62), and "Boy, right, front-ish, brown hair, red T-shirt, blue trousers: standing on the path sweeping leaves with a broom." (87). O1.
- **The marks of age.** The beard of the man in green is in his line in 14 of his 25 pictures (v0.50: 16 of 20). The moustache of the man in the red shirt is in his line in 1 of 12 (v0.50: 7 of 23), and the older man's in none of 19. The bench had said that a wider moustache would not change how he is called, and the release kept v0.50's; it is now a mark almost nobody names.
- **Every animal was named for what it is,** with one doubt of the duck: "the duck's small head and beak could read as a goose or swan" (83, a scorer's note). All 19 (template, angle) pairs pass, each at 1.00.
- **The teenager is a boy**, in every item the scorers listed. He is one, and the key's word is the scorer's to match.

## The v0.50 list

| v0.50 | In v0.51 |
|---|---|
| R1: `play_catch` 0.80, **under the gate**: "has just thrown a red ball (a dashed line shows its arc) toward a girl" | The ball early on its path, the catcher's two open hands, the thrower's planted feet. **1.00** (10 items, 5 pictures), and the thrower the thrower in all five: "A small child in a yellow shirt and orange shorts has just thrown a red ball (a dotted line shows its path) towards a man in a green shirt, who holds his arms out ready to catch it." (65). Two of the five add the other way and set it aside: "it could also be read as the man having thrown it to her, but the girl's outstretched arm suggests she threw it." (73) |
| R2: `square_wheel` 0.875 with a misread, **under the gate**: "looks like a hose reel or a fan-like grate" | No hose by the barrow. **1.00** (24 items, 8 pictures, four of them the barrow), and no reel in any: "The wheelbarrow in the middle has a square wheel, which is impossible." (73). In three pictures of the eight the wheel is named only among the unsure things: "The wheelbarrow's wheel is drawn as a square frame with crossed spokes rather than a round wheel, which looks odd." (11). R4 |
| R3: `bird_steals` 0.90: "or he may be sharing it" | Looked at and left. **1.00** (18 items, 6 pictures), four of the eighteen on a second reading: "The bird could be read either as simply sitting next to the sandwich or as actively eating/stealing it; it looks like it is pecking it." (55). R5 |
| R4: `blocked_hose` 0.95: "whether the dog's paw is actually on the hose or just behind the bulge" | Benched with the swelling ending short of the paw and left as it was: it read as two pieces of hose. **0.95** again (20 items, 5 pictures), two half marks in one picture: "Whether the brown dog is actually standing on the hose (blocking the water) or just standing next to it; its back feet are right at the hose." (62). R1 |
| R5: `ducks_bread` 0.944: "her hand item is small and hard to make out" | A slice of bread in the hand. **1.00** (15 items, 5 pictures), and bread in the hand or thrown in all five: "a girl in a pink dress at the pond's edge holds a slice of bread, so she seems to be feeding the duck." (2) |
| R6: `jump`, `dog_sleeping`, `dog_wants_walk`, `dog_begs`, `plant_flowers`, full marks on a hedge | Left. Each **1.00** by the gate. On the strict count `dog_sleeping` and `plant_flowers` 0.7, `dog_wants_walk` 0.85; `jump` has no second reading this time, and `dog_begs` one. R6 |
| O1: the lost balloon's string "tied to something on the fence", "anchored in the pond" | The end off the rails, the backdrop's lines and the pond. **1.00** (15 items, 5 pictures). No reader has it tied or anchored: "Its string ends in mid-air near the fence top, not near her hand." (22). Whose balloon it is, the older doubt, is offered in three of the five. O4 |
| O2: the man in the red shirt a boy when he sweeps, 2 of 23 | The wider moustache was benched in whole scenes and not taken. **2 of 12** (above). O1 |
| O3: the painter's "pale cylinder", the tin "several steps behind" | The roller's caps dark, the tin at the heel. Painting in all nine pictures, no pale cylinder and nothing of the tin. Two readers ask which boards are being painted: "it is unclear whether she has just painted those planks or is about to start on the next unpainted ones." (101). O5 |
| O4: the slider "slightly above the chute surface" | Not worked. One picture of three: "The girl appears slightly above the slide surface rather than sitting firmly on it; could read as just sliding fast or as floating a little." (39). O2 |
| O5: the heavy seesaw's grown rider | Not worked. One picture of three (7). O2 |
| O6: figures at the pond's rim | Not worked. Four pictures (46, 47, 81, 83). O3 |
| O7: a hose in use under storm clouds | No longer planned together. Not said in any picture |
| O8: the swing's one seat and others | Not worked. The swing's one seat is not remarked; the swung child "seems to sit slightly in front of the seat" (29). O2 |
| O9: setting items left out | 44 zeros from eight readers (35 from six). O8 |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

Every template was screened in at least three pictures (30 in three, 12 in four, 16 in five, 2 in six, and one each in eight, nine, fifteen and nineteen). All 64 pass. Per angle (`v051/gate_yaw.json`), all 19 (template, angle) pairs pass.

| Template | Mean | Items | Pictures | Verdict |
|---|---|---|---|---|
| `blocked_hose` | 0.95 | 20 | 5 | pass |
| `ice_cream` | 0.967 | 15 | 15 | pass |
| the other 62 | 1.00 | | 3 to 19 | pass |

A full gate is not the end of the reading. v0.49's was full as well, and v0.50's then had two failures, one of them on a doubt that v0.49's strict count had shown. The strict count above is the list to read: eight templates pass on a reading that stands beside another.

## After the screen

Nothing was mended, swapped or read again. The count is the first and only one.

## What reads least well (the v0.52 list)

| | Template | v0.51 | What the readers wrote | For v0.52 |
|---|---|---|---|---|
| R1 | `blocked_hose` | 0.95 (20 items, 5 pictures), the lowest of the 64 | "Whether the brown dog is actually standing on the hose (blocking the water) or just standing next to it; its back feet are right at the hose." (62); "could be a kink/swelling from the dog stepping on it, or a hose connector" (84) | Two benches have left the drawing as it is: the swelling stays (v0.50) and so does the paw at its end (v0.51). Untried: both forepaws on the hose, and the holder looking down the hose at the dog. Or carry it: the doubt is one picture of five in each of the last two screens |
| R2 | `ice_cream` | 0.967 (15 items, 15 pictures) | "She may be looking at the ice cream, or about to lick it." (47) | The walker's cone at the mouth, as the standing eater's is since v0.49; look at the walk in profile first |
| R3 | `floating_box` | 1.00 (9 items, 3 pictures); 0.722 on the strict count | "could be falling (just thrown over the fence from the other side) or floating impossibly; there is no motion line to tell which." (32) | Five of its nine marks stand beside a throw or a fall. The box level and still, lower over the lawn than the fence's top, with its shadow on the grass under it; bench it against v0.51's on the same seeds |
| R4 | `square_wheel` | 1.00 (24 items, 8 pictures); 0.854 with its seven calls halved | Named among the unsure things only, in three pictures (9, 11, 102): "The wheelbarrow's wheel is drawn as a square-ish frame with crossed spokes rather than a round wheel, which looks odd." (102); "The bicycle's wheels look oddly square." (97) | The wheel is seen as square in all eight, on the barrow and on the bicycle alike. Nothing to draw. See that the next probes hold both carriers again (`tools/cycle/extra_probes.py`) |
| R5 | `bird_steals`, `cat_stalks_bird` | 1.00 each; 0.889 and 0.833 on the strict count | "The bird could be read either as simply sitting next to the sandwich or as actively eating/stealing it" (55); "The cat may be stalking the red bird, or just walking past." (30) | v0.48's R5 and R6 and v0.50's R3, carried. The thief bird has not been drawn since v0.47; a piece of the sandwich in the beak was a dark blob then, and is worth one more bench in bread's own colour |
| R6 | `dog_sleeping`, `plant_flowers`, `windy_hat`, `dog_wants_walk`, `rake` | 1.00 each; 0.7, 0.7, 0.833, 0.85 and 0.875 on the strict count | "The puppy could be read as sleeping, sulking, or crouching ready to pounce; its pose is low with chin on paws." (22) | Left again unless a release has a bench to spare: each hedge is a reading that the thing drawn would earn in life |

## Unintended oddities

Grade A is a remark in five or more pictures, or one that touches what a figure is; B in three or four; C in one or two.

| | Grade | What the readers wrote | Pictures | For v0.52 |
|---|---|---|---|---|
| O1 | A | Grown figures called young first, 5 of 85: the woman in purple a girl three times, the man in the red shirt a boy twice (above). His moustache is named in 1 of his 12 pictures | 42, 47, 51; 62, 87 | The bench of v0.51 found the man a boy in three of eight readings of him sweeping, and in one of 24 otherwise, whatever the moustache: the sweeper's pose, bent over the broom with the face down, drawn more upright and looking ahead, and counted on the whole-scene bench (`tools/cycle/age_scenes.py`). The woman in purple is a girl in three poses: her marks of age (v0.50) against the ponytail, on the same bench |
| O2 | A | A figure off its seat, five seats: "the girl seems to sit slightly in front of the seat" (the swing); "The girl appears slightly above the slide surface rather than sitting firmly on it" (the slide); "she seems to sit just above the plank rather than firmly on it, a minor drawing oddity." (the seesaw); the heavy seesaw's man "as if sitting slightly in front of it"; the reader on the bench "as if perched on the very edge" (a scorer's note) | 29; 39; 50; 7; 55 | One picture each, and one question: a sitter is drawn in front of what it sits on. v0.50 measured the seesaw child's underside and seated it (`templates._under50`); the same measure for the swing's seat and the bench's, and for the slide the chute's own drawing, as v0.50's list has it |
| O3 | B | Figures over the pond's near edge: "his upper body overlaps the water in the picture, though his feet are on the grass." (81); "it could look as if she is partly in front of/over the water." (83) | 46, 47, 81, 83 | v0.48's O2 and v0.50's O6, now in four pictures. A walker's or a runner's box kept wholly below the pond's near rim, or wholly beside it; the duck feeder, who must stand at the water, at an end of the pond with the feet a clear strip off the rim |
| O4 | B | The lost balloon, whose it is: "alternatively she could be reaching to grab a balloon that belongs to nobody." (22); "or it could be a separate balloon floating by; its string ends in mid-air near the fence." (78); "whether he just let go or someone else's balloon is drifting is not certain, but likely his." (66) | 22, 66, 78 | The string's end is no longer by anything, and the doubt is the gap itself, as in v0.49's R1. Each nearer or farther end has been benched (v0.47, v0.50). Untried: the hand open with the fingers spread just under the string's end, or a third string's stub still in the fist |
| O5 | B | The wind and the leaves: "windy enough to blow off a hat and leaves, yet the clouds and swing look calm" (29, a scorer's note); a pile of leaves "with no visible source" (70, a scorer's note); "a pile of leaves on the path with no tree overhead" (99, a scorer's note) | 29, 75; 70, 99 | The sweeper's heap was drawn for summer in v0.39 and v0.40. A few leaves on the ground round the heap; for the wind, what else it would move in that picture |
| O6 | C | The fence painter, which boards: "it is unclear whether she has just painted those planks or is about to start on the next unpainted ones." (101); "The paint roller head looks like a blue cylinder held to the side, could be read as a sponge or brush." (23) | 23, 101 | The roller on the wet edge of the painted boards, half on blue; v0.45 had moved it onto bare wood for another remark |
| O7 | C | One picture each: the puppy "very small next to the girl"; the runner with an ice cream "about to trip over or step on the bird"; the square-wheeled bicycle "upright with no rider and no visible stand"; the ball in the tree "very high" for the small girl; the bird's branch "at an odd angle"; the jumper's shadow "far below and to the right"; a stride that "looks reversed"; a back foot that "looks detached"; the fishing rod "very long"; a seesaw "nearly level although the boy looks bigger than the girl"; the kite flyer looking the other way; a goat tied up in a park; a woman running for no reason; a garden with nobody in it; the sweeper "crowded against" the gate (all scorers' notes) | 10; 19; 53; 62; 72; 73; 81; 87; 86; 98; 102; 24; 24; 32; 61 | The bicycle's stand was v0.12's; the jumper's shadow v0.50's O8. None is in two pictures |
| O8 | C | Notes for the pilot: the setting's clouds and trees are left out by some readers and named by others of the same pictures (44 zeros; 35 in v0.50) | 44 items | None for the drawing. The pilot's scoring should say whether setting items count |

## Placement

Revision 48 is six rules and a rank: the thrown ball a third of the way along its path; the square-wheeled barrow or bicycle placed after every template that lays a hose, its box off each hose's run, off the ground nobody may stand on and off the garden's reel; a slice of bread in the duck feeder's hand; the lost balloon's string end on no rail of the garden's fence, by no gate, on no line of the backdrop and over no pond; the painter's tin at the heel; and the stopped hose kept to a clear sky. What each costs is in `isolation_v051.md`: one garden seed of twelve for the barrow with a sprinkler, and nothing measured for the others. The swelling of the stopped hose ending short of the paw was benched and left out.

The calibration moved in four numbers of 252, all the lost balloon's. Seven cells of sixteen have v0.50's templates, and two set pictures are v0.50's to the pixel. Tiers 1 to 3 placed on their showcase seeds. The tier-4 park, street and playground placed on v0.50's seeds with v0.50's templates, the street and the playground in another layout, since the bicycle is placed last now. The tier-4 garden placed on v0.50's base at its twenty-sixth step with other templates: v0.50's had the stopped hose under the storm clouds. The five isomorphs came in the first pass, the tier-4 one on v0.50's seed and identical to v0.50's. `probes.py` left one template short, the begging dog, and `more_probes.py` filled it with three small groups; the pass by angle added nine; and three probes were forced for the wheelbarrow (`tools/cycle/extra_probes.py`), which the counts by template do not see.
