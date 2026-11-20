# v0.58 blind screen: what it found (the work list for v0.59)

The v0.58 screen read the set's 21 pictures and 117 probes with the readers' prompt of v0.48, unchanged, and a scorers' prompt with two changes: a field for the word a figure is called by when it is outside the key's names, and the flag for a second reading split in two (`screen_prompts.md`). There were eighteen readers, twelve of eight pictures and six of seven, and six scorers of 23 pictures each. Nothing was mended, swapped or read again after the screen: every number here is the first and only count.

v0.58's brief was Sam's: "Go for v0.58", the list of `flaws_v057.md`. Each drawing and each rule was read blind before it went into scenes, in v0.57's own pictures built again (120 readings, then 128 in a second round, a reader's pictures of a thing all of one arm); `isolation_v058.md` has the benches. What came of it:
- **the wheelbarrow with a square wheel** is wheeled by a grown figure, as the bicycle is held by its owner. The two new wheels the list had asked for changed nothing and were not taken;
- **the kite's child** holds the reel in a lowered hand and raises the other arm toward the kite;
- **the heavy seesaw's man** sits with his thighs along his seat's pad and his shins upright; the child is v0.57's, after two new poses of her were read and lost;
- **the plain seesaw's raised rider** sits on her pad with both fists on the handle and her legs hanging;
- **the thrown ball** keeps off the rails of a fence;
- **the scorers** write a figure's wrong name into a field of its own and tell a second reading in the description from a hedge in the unsure section.

**A like-for-like release again.** The planner's priors were left at v0.56's and every record of v0.57 was built again under revision 52 from its own regeneration data (`tools/cycle/carry_over.py`). Of v0.57's 136 pictures, 113 came back to the pixel; 22 were drawn again or moved, each with its own templates (the six kites, the ten seesaws, four wheelbarrows and two games of catch); one was replaced, the tier-4 garden, which cannot hold the wheeled barrow and has the man who sits on nothing in its place; and two probes with a wheeled barrow were added. The library was not rendered again: v0.57's files were kept for every pose that was not drawn again, after a render of all of them from the new cast had shown three single pixels of difference.

## Headline (the 21 pictures of the set)

| | v0.54 (21) | v0.55 (21) | v0.56 (21) | v0.57 (21) | v0.58 (21) |
|---|---|---|---|---|---|
| Things | 0.954 | 0.954 | 0.943 | 0.926 | 0.953 |
| Actions | 1.00 | 1.00 | 0.996 | 1.00 | 1.00 |
| Inferences | 0.984 | 0.953 | 1.00 | 1.00 | 1.00 |
| Contradictions | 0.929 | 0.946 | 0.982 | 1.00 | 1.00 |
| All items | 0.974 | 0.972 | 0.975 | 0.971 | 0.982 |
| Misread items | 0 of 286 | 1 of 286 | 0 of 277 | 0 of 277 | 0 of 277 |
| Readers' remarks per picture (all screened pictures) | 2.71 | 2.44 | 2.73 | 2.47 | 2.37 |
| Oddities per picture, as logged by the scorers | 0.4 (at most 3) | 0.4 (at most 2) | 0.5 (at most 2) | 0.3 (at most 2) | 0.1 (at most 2) |

Five of the set's 277 items are under full marks, and all five are the clouds, which their readers left out (pictures 26, 33, 35, 58, 60). Every item of an event, an inference or a contradiction in the set has full marks.

The scorers logged one oddity in the set's 21 pictures and 19 in the 117 probes, 0.1 a picture over all 138 (v0.57: 12 and 25 in 136, 0.3). The prompt's sentence on oddities is unchanged, so the fall is the scorers' and the readers' as much as the pictures'. The readers' own remarks are 2.37 a picture for 2.47.

Across all 138 pictures, 1,442 of the 1,458 scored items had full marks (v0.57: 1,391 of 1,435), and none was misread. The 16 under full marks:
- **Thirteen on the clouds and two on a tree,** all zeros on setting items that a reader left out, from four readers: one left the clouds out of six of its seven pictures (58 to 64) and another out of five of eight. v0.57 had forty such zeros, from eight readers. It is a reader's habit and not a drawing's fault.
- **The heavy seesaw's inference, one half mark** (54): "The man sits on the low end, which rests near the ground, and the girl is up on the raised end holding the handle, which fits the heavier person being lower." Whether she is stuck is left open. R1.

The scorers gave none, six, nine, none, none and one under full marks, of 230, 277, 266, 212, 226 and 247.

**The gate.** All 64 templates pass, as in v0.57. Sixty-three read 1.00 and one is under it, `seesaw_heavy` at 0.967 on fifteen items in five pictures. Every template was judged in at least three pictures (11 in three, 11 in four, 16 in five, 14 in six, 5 in seven, 3 in eight, and one each in eleven, twelve, sixteen and twenty-two). All (template, angle) pairs pass (`v058/gate_yaw.json`).

**What the full marks rest on.** The scorers flagged 70 full marks as judgement calls (10, 15, 15, 10, 7 and 13), for 67 in v0.57. With the flag split they are of three kinds:
- **3 where the free description or the inventory sets another reading beside the target** (`two`): the floating box twice (15, 22: "floating/falling with nothing holding it") and the frying pan once (55, a frying pan or a saucepan). With these halved all 64 templates still pass. This is the strict count from now on.
- **58 where the description gives the target plainly and the unsure section offers another reading** (`unsure`). By template: the stopped hose six; the thief bird and the floating box five each; the upward water and the kite in the tree four each; three each for the begging dog, the dropped ice cream, the walker about to trip, the heavy seesaw, the windy hat and the fork; two each for the ball in the tree, the fish in the tree and the stalking cat; and ten singles. v0.57's one flag took in both kinds, 57 of them: with `two` and `unsure` halved together, 55 of the 64 pass (54 in v0.57), and the nine under 0.9 are `floating_box` 0.767, `water_upward` 0.778, `sweep_fork` 0.833, `blocked_hose` 0.85, `bird_steals` 0.861, `seesaw_heavy` 0.867, `dog_begs` 0.875, `fish_in_tree` and `kite_in_tree` 0.889.
- **9 on a near word or a target partly said** (`near`; v0.57: 10): the lost balloon three times (escaped, with letting go not said), the thief bird twice (about to peck), the heavy seesaw twice (up in the air, and not said to be stuck or calling), a sleeping puppy and a girl who cheers and is not said to jump. With all 70 halved, 54 of 64 pass (v0.57: 51).

The six scorers flagged `unsure` 6, 14, 12, 9, 6 and 11 times of 212 to 277 items: the flags are still the scorers' own.

## What the screen says of the cast

- **The grown figures.** The scorers wrote a word under `who` for seven actions in six pictures: a man called a boy four times (eating an ice cream, 19; painting the fence, 65; "a boy or young man" with a shopping bag, 94; looking into the hose's nozzle, 107) and a woman called a girl three times (62, 65, 71). By the first inventory line that names each figure's clothes, the count v0.49 began, the four grown figures are called by a young name first in 7 of their 124 pictures (v0.57: 5 of 117): the man in the red shirt in 4 of 29, the woman in purple in 3 of 29, the woman in the yellow dress in none of 34, the man in green in none of 32. The two counts agree, so the field can stand for the hand count. It is the same two figures and the same activities as in the last three screens.
- **What a young name costs now: nothing, by rule.** v0.57's two half marks for a man called a boy are full marks with a word under `who` (the same two pictures, 65 and 94). `carry_bag` and `paint_fence` read 1.00 for that reason and no other.
- **Every animal's item has full marks.** Five oddities were logged with an animal in them: a goat in a park and its rope, four times in three pictures, and a bird large beside a sandwich once. v0.57 had twelve.
- **No oddity is about a seat.** v0.57's readers had a rider a little off its seat in five pictures. In the ten seesaw pictures of this screen the scorers logged none; one reader of the heavy seesaw writes: "- The man looks quite large for the seat; nothing physically wrong though." (128)

## The v0.57 list

`R` rows were at the gate or its edge; the counts in brackets are items and pictures.

| v0.57's row | The benches | In v0.58's screen |
|---|---|---|
| R1: the wheelbarrow's square wheel, 0.967, hedged in three pictures of five | Two new wheels: in no description in 30 fresh readings, unseen in 2, 4 and 2 of 10. Wheeled by a grown figure: in the description in 9 readings of 16 for none of 16 parked, unseen in none for 4 | **`square_wheel` 1.00** (33, 11). Of the six wheeled barrows the wheel is wrong or impossible in the description in four: "oddly, the wheelbarrow's wheel is drawn as a square, which could not roll." (30); "a little odd" with an `unsure` flag in one (61); and only in the unsure section in one (109). The garden that had the two half marks is in full (40). R3 |
| R2: the kite in the tree, a second reading in three pictures of six | The reel in a lowered hand: stuck with nothing beside it in 24 readings of 34, for 7 of 16 | `kite_in_tree` 1.00 (18, 6), with four `unsure` flags in three pictures of six, as many pictures as before: "it could also be read as flying just in front of the tree, but it overlaps the branches and the string is slack and looped on the ground, which suggests stuck." (51). No oddity is logged of the reel. R2 |
| R2: the other six strict-count templates | Looked at and left | `lost_balloon` three `near` and one `unsure`; `cat_stalks_bird` two `unsure`; `floating_box` two `two` and five `unsure`; `windy_hat` three; `water_upward` four; `dog_wants_walk` one. R2 |
| R3: the heavy seesaw's man, in front of his seat to nine bench readers of ten | Off his seat in 6 readings of 15, then 1 of 68; on purpose 7 of 15, then 5 of 68 | No reading of the five puts him off his seat or has him keep her up on purpose |
| R3: the heavy seesaw's child | Two new poses lost to v0.57's (stuck in 20 readings of 24 with hers, 1 of 24 with the new one) | **`seesaw_heavy` 0.967** (15, 5): one half mark on the inference (54), and her action flagged in all five pictures, `near` twice (54, 88: "with her mouth open as if talking or surprised") and `unsure` three times. R1 |
| O2: a rider a little off its seat | The raised rider on her pad: off her seat in 3 readings of 12, then none of 8 | `seesaw` 1.00 (10, 5), no flag and no oddity |
| O1: grown figures called young first | Not drawn; K1 | 7 of 124 for 5 of 117. O1 |
| O3 to O7 | Left | The seep at the hose's reel twice, the goat four times, a bird once. O2 to O5 |
| K1: what a wrong who-word costs | A field of its own, the action scored on the action | Seven words under `who`; no mark lost for one |
| K2: the flag split | `two` in the description or inventory, `unsure` only in the unsure section | 3 and 58. K1 |
| The fence's rails | The ball's disc off each rail: tied to the fence in 3 readings of 9, then none of 8 | `play_catch` 1.00 (12, 6), no flag and no oddity |
| A tier-4 plan that cannot be cast twice | The search already refuses it; the planner left | The tier-4 park and its isomorph are v0.57's, to the pixel and with the kite's child redrawn |

## A second reading of 113 pictures, and a first of 22

**The 113 that are v0.57's to the pixel.** 1,136 of 1,175 items have the score they had, 33 are higher and 6 lower. Thirty-seven of the 39 are the clouds or a tree; the other two are the men called boys, half marks then and full marks now by the rule. Apart from the setting items and that rule, a third set of fresh readers and scorers moved no item of 1,175.

**The 22 that were drawn again or moved.** 219 of 228 matched items have the score they had, 6 are higher and 3 lower. Six of the nine are the clouds or a tree; two are the wheelbarrow's contradiction items in the garden that had the half marks, in full now; one is the heavy seesaw's inference, a full mark then and a half now (`tools/cycle/retest.py`). Sixteen items have no match by text, since the wheeled barrow's figure has an action where the parked barrow was an entity.

## After the screen

Nothing was mended, swapped or read again. The count is the first and only one.

## What reads least well (the v0.59 list)

| | Template | v0.58 | What the readers wrote | For v0.59 |
|---|---|---|---|---|
| R1 | `seesaw_heavy` | 0.967 (15 items, 5 pictures); 0.867 with its `unsure` flags halved, 0.8 with all | "Because the man is heavier, his end is down and the girl is up in the air." (88) | The weight is given in every picture and the man sits on his seat. What is not said is that she is stuck: in two pictures of five the tilt is only what one would expect, and one of them lost the half mark. On the bench her v0.57 pose gave "stuck" in 20 readings of 24, but plainly in 6, and of 83 bench readings none says that she wants down and two offer calling out, each beside another reading; in the screen two readers of five have her mouth open "as if surprised or calling out" and the other three have her talking, surprised or worried. Her item's text says she is "calling out": either the drawing must say it (both arms stretched down to him, the body leaning toward him over the handle, a wide mouth) or the text should not. Bench the pose in the five pictures, a reader in one arm only |
| R2 | `floating_box`, `water_upward`, `sweep_fork`, `blocked_hose`, `bird_steals`, `dog_begs`, `fish_in_tree`, `kite_in_tree` | 1.00 each; 0.767 to 0.889 with `two` and `unsure` halved | "- Cardboard box: up in the sky above the fence, tilted, floating/falling with nothing holding it." (15) | Only the floating box has its second reading in the description itself (twice in five pictures), and it is the tilt that says falling: v0.13 tilted it so that it could not be a box standing further back, and a level box with its underside showing has not been read since. The others are hedges of the unsure section, where a reader is asked for two readings of anything: the hose's swelling a connector, the bird only standing by the sandwich, the water a spray, the kite flying in front of the tree. Split the flag has shown how few are second readings; leave them unless a bench is cheap |
| R3 | `square_wheel`, the wheelbarrow | 1.00 (33 items, 11 pictures) | "The wheelbarrow's wheel is drawn as a square-looking frame rather than a round wheel, which looks a little odd." (61) | Read in full, and in the description in four pictures of six. Two things are left. One reader of six still keeps the wheel to the unsure section (109). And the figure is one more in the picture: the tier-4 garden lost the barrow, and in one park a kite's string passes close behind the pusher's head (109). The pusher is checked as the bicycle's owner is, without the rules a figure of an event obeys (the pond's edge, the house's edges): give both owners those rules |

## Unintended oddities

Grade A is a remark in five or more pictures, or one that touches what a figure is; B in three or four; C in one or two.

| | Grade | What the readers wrote | Pictures | For v0.59 |
|---|---|---|---|---|
| O1 | A | Grown figures called young first, 7 of 124: the man in the red shirt a boy in four of his 29 pictures, the woman in purple a girl in three of her 29 | 19, 62, 65, 71, 94, 107 | The fourth screen at about one picture in twenty, on the same two figures. It costs no mark now and is counted by the scorers. A drawing of the two (the moustache shows in profile only; the woman has nothing that says grown) is the mend, and a bench of faces is a release of its own |
| O2 | B | A goat tethered in a park is unusual; its rope hard to follow | 48, 70, 110 | As v0.56 and v0.57. Left |
| O3 | B | The wind moves the cap and not the swing, a book's pages or the washing | 64, 116 | New in this count: three remarks in two pictures. v0.57 made the washing hang straighter in a gust, and one reader now finds it barely blown |
| O4 | C | Water at the hose reel: a leak, a puddle of unclear cause | 60, 107 | The seep is the cue that the tap is on. Left |
| O5 | C | The sprinkler's spray lands short of the box, which is wet | 79, 85 | Two pictures, one reader. Look at the arcs' end |
| O6 | C | A kite's string close behind the barrow's pusher (109); a roller above the fence's top (1); an angler far back from the pond (4); a ladder where a lamp post would be (37); a startled picnicker (56); a hand over the pond's rim (73); a red cap on an older woman (76); a man on the grass beside the pram on the path (87); a bird large beside a sandwich (100) | as given | None is in two pictures |
| O7 | C | Notes for the pilot: the setting's clouds and trees are left out by some readers and named by others (15 zeros; 40 in v0.57, 20 in v0.56) | 15 items | None for the drawing. The pilot's scoring should say whether setting items count |

## Keys and scoring

| | What | For v0.59 |
|---|---|---|
| K1 | The split flag works: three second readings in a description, 58 hedges in an unsure section. The scorers still differ on the second (6 to 14) | Keep both. The strict count is `two` alone; report `unsure` as what it is, a count of the readers' hedges, and do not gate on it |
| K2 | The `who` field agrees with the hand count (7 and 7) | Keep. `tools/cycle/who_cmp.py` can be retired once two screens agree |
| K3 | The heavy seesaw's child has "calling out" in her item's text; two bench readings of 83 and two screen readers of five offer it, each beside another reading | With R1: the text follows the drawing, or the drawing the text |
| K4 | The scorers logged 20 oddities for 37 with the same sentence in the prompt | Nothing to change; say it where the two are compared |

## Placement, priors and the library

Revision 52 (`scenegen/scene.py`, its header comment). Fifteen of the sixteen cells and all five isomorphs were carried over from v0.57's records.

- **The tier-4 garden.** v0.46's set of nine, forced on its seed since v0.53, placed on none of twelve seeds with the wheeled barrow and the band (five parked): the group needs a strip of about 430 px where the parked barrow needed 230. The cell is now the same set with the man who sits on nothing in the barrow's place, on the same seed (`tools/cycle/forced_cell.py`, `v058garden`). So no tier-4 picture holds a wheelbarrow, and the tier-4 street and playground hold the bicycle.
- **The priors were left** at v0.56's, for the second release. The calibration measured with the new cast under revision 52 moved in 6 of its 252 numbers, all the square wheel's. By it five priors would change a little: `square_wheel` (salience -0.03 to 0.03), `kite_in_tree` (-0.73 to -0.74), `windy_hat` (-1.28 to -1.32), `ducks_bread` (-1.34 to -1.36) and `seesaw_heavy` (its distance term by 0.003); and `pan_watering`'s prior still has no second cue. A release that builds a new set should take all six.
- **The library was kept**, not rendered again: `lib058` is `lib057`'s files without the two poses that were drawn again, and the new poses rendered from the new cast. A render of every one of v0.57's variants from the new cast, as a check, differed from the kept files in three single pixels.
- **Not done:** a forced set that holds the stopped hose beside the frying pan or the upward water stops the build (`KeyError: 'hose_reel'` in `WaterFlowers.place`); the planner never draws the two together. The fence's foot line, which the flat ball lies across a little more often now that it keeps off the rails, has no rule.
