# v0.58 isolation bench

The brief for v0.58 was Sam's: "Go for v0.58". The list is `flaws_v057.md`: the wheelbarrow's square wheel (R1), the templates that the strict count marks down, with the kite's reel as the one to draw (R2), the heavy seesaw's riders (R3), the oddities (O1 to O7), two rows of the keys (K1, K2) and three lines on placement. This file is about the drawings and the rules that were read; the keys are in `screen_prompts.md`.

Every drawing was put behind a switch whose `O` is v0.57's drawing, and each was read blind in whole pictures before it went into scenes. A scene's switch is `scene.sw58(NAME)`, which is `O` for any record older than revision 52; a cast's is `TPDB_<NAME>58` in `castlib`. With `TPDB_REV58=51` and `TPDB_ONLY58=<names>` the drawings act in v0.57's own records and nothing else moves, so a bench picture is a screened picture of v0.57 with one thing drawn another way (`tools/cycle/bench_build.py`).

There were two rounds, 248 readings:

1. **Round 1** (`isolation_v058/bench`): 23 of v0.57's pictures in up to three arms, 120 readings by 15 readers (`tools/cycle/bench_prepare.py`).
2. **Round 2** (`isolation_v058/bench2`): what round 1 left open, 16 pictures in two arms each, 128 readings by 16 readers (`tools/cycle/bench_round2.py`).

A reader is a fresh agent that is given the screen's own reader prompt and its pictures and nothing else; no reader has a scene twice. **A reader has a row's pictures in one arm only**, in both rounds, and the arms cross between the rows: v0.57's bench had found that a count by arm can be one reader's habit (four readers of sixteen wrote "watering can" for every pan they were given). So every count here is given by reading and can be given by reader, and an arm of ten readings is five readers. The arms of round 1: `S` is the reading v0.57's own screen had of a picture, `O` a fresh reading of the same picture, `B` the picture built again with the new drawing, `C` an alternative. Analysts who never saw a picture counted each row of both rounds from the readers' own lines (`isolation_v058/digest`, with their briefs and the tallies they read); I counted the wheelbarrow myself in both rounds, and the analyst's count and mine agree. Quotations are from the readers' own files.

## How the work was shared

Three workers drew at the same time, each a fresh agent with a package of rows, a scratch folder and one set of rules (a shared file is changed by exact replacement only; the old path stays byte for byte behind the switch; no readers). One drew the seesaw's riders, one the kite's child, one the barrow's wheel and the rule for the fence's rails; the last was called back after round 1 with the readers' own lines and drew the barrow wheeled by a gardener. I wrote the keys' and the scorers' changes, built the benches and decided.

## What was read, and what came of it

| Row | Drawn | Read | Taken |
|---|---|---|---|
| R1 the barrow's wheel | the bicycle's hub and spokes at the old size (B) and at the bicycle's size (C); then the barrow wheeled by a grown figure (H) | round 1: 10 readings an arm of O, B, C; round 2: 16 an arm of O and H | **H.** B and C changed nothing |
| R2 the kite's reel | the reel in a lowered hand, the other arm raised (B); the reel on the grass (C) | round 1: 10 an arm of O, B, C; round 2: 24 an arm of B and C | **B** |
| R3 the heavy seesaw's man | thighs along the seat's pad, shins upright; the pad longer | round 1: 20 readings of the new man, 15 of the old; round 2: 48 of the new | **taken** |
| R3 the stuck child | both fists on the handle, leaning back (B); bent forward, a leg feeling for the ground (C) | round 1: 10 an arm; round 2: 24 of B and 24 of v0.57's child with the new man (E) | **neither: v0.57's child stays** |
| O2 the plain seesaw's raised rider | on her pad, thighs along the plank, legs hanging, both fists on the handle | round 1: 7 of O, 8 of B, beside the screen's 5 | **taken** |
| the fence's rails | the thrown ball's disc 10 units off each rail | round 1: 7 of O, 8 of B, beside the screen's 2 | **taken** |

## R1: the wheelbarrow's square wheel

`square_wheel` read 0.967 in v0.57 and its wheelbarrow was hedged in three of five pictures: "- The wheelbarrow's wheel looks square or boxy with a cross inside rather than round. It may just be a stylised wheel seen from an angle, or it may be an odd shape." The list asked for a wheel with a rim as thick as the bicycle's.

**The premise was wrong.** The worker counted the pixels: the barrow's tyre and the bicycle's are 13 px each. What differs is the wheel's size (51 to 60 px across for 68 to 75) and its inside, a square hub with a cross of spokes. So two wheels were drawn: B, the bicycle's round hub and thin spokes at the old size, and C, the same at the bicycle's size.

**Round 1: no wheel changes what is written.** Ten readings an arm, five readers each:

| | O | B | C |
|---|---|---|---|
| the square wheel in the description or the inventory | 0 | 0 | 0 |
| only in the unsure section | 8 | 6 | 8 |
| of these, with another reading beside it | 2 | 2 | 1 |
| not seen | 2 | 4 | 2 |

Every reader wrote the same of both its pictures. The usual line is the unsure section's: "- The wheelbarrow's wheel looks like a square frame with spokes rather than a round wheel, which is odd." Or: "- The wheelbarrow's wheel looks square rather than round, which looks unintentionally odd." And the inventory has: "- Red wheelbarrow (centre, front): parked, empty." The new wheels changed the words only: "spokes" in eleven of the fourteen B and C readings that mention the wheel, and the wheel called a box or a frame in 6 readings of 10 in each, for 4 of 15 of the old. Nobody remarks on C's size. The screen's own reader had given two of the five pictures a plain square wheel in the description; no fresh reader of thirty did. The barrow is a prop parked at the side, and its wheel is a detail of a prop.

**The mend that had worked for the bicycle.** In v0.56 the bicycle with square wheels read 4 of 10 on its stand and 6 of 6 once its owner held it. So the barrow was drawn wheeled by a grown figure that no event has cast (H): a hand on each handle, the barrow's legs off the ground, the square wheel on the ground in front. No pose was added: the cast's `walk_dog` has both fists low and forward, and the barrow is sized to the hands. As the bicycle's owner does, the figure has an action, "pushing a wheelbarrow", in place of the entity.

**Round 2: wheeled, the wheel is read.** Sixteen readings an arm, eight readers each, two pictures a reader:

| | O (parked) | H (wheeled) |
|---|---|---|
| the square wheel in the description or the inventory | 0 | 9 (5 readers) |
| only in the unsure section | 12 | 7 |
| not seen | 4 (2 readers) | 0 |
| called wrong or impossible (O says odd) | 0 | 7 (4 readers) |
| tied to rolling | 0 | 4 (2 readers) |
| the figure said to push the barrow | | 16 |

"Its wheel is a square, not a round wheel, so it could not roll properly." And: "The wheelbarrow's wheel is drawn as a square rather than a circle, which would make it impossible to roll properly." Two readings of sixteen set tipping beside pushing: "- The man is holding the handles low and the wheelbarrow could be read as being pushed or being tipped to empty."

**What the round cannot show.** Other readers read each arm, and the wheeled barrow also stands in another place of its picture, so the bench cannot part the pushing from the place. And seven of the sixteen wheeled readings still have the wheel only in the unsure section. H's alternative with the larger wheel (HC) was drawn and not read.

**What it costs.** Free where the lawn is open; five seeds of twelve in a garden beside a raker and a digger (6 for 11). The busiest garden, the tier-4 cell, cannot hold it: its set of nine with the band placed on 0 seeds of 12 with the wheeled barrow, for 5 parked. The cell now has the man who sits on nothing in the barrow's place.

## R2: the kite in the tree

v0.57 had laid the kite's string on the grass, and the kite was caught with another reading beside it in three pictures of six. Two of its readers found the reel odd, held up over a slack line. The pose was `fly_kite`, the reel before the chest.

**Round 1** (ten readings an arm, five readers; S is the screen's six):

| | S + O | B | C |
|---|---|---|---|
| stuck, with nothing beside it | 7 of 16 | 7 of 10 | 9 of 10 |
| another reading only in the unsure section | 8 | 3 | 1 |
| the raised reel said not to fit a stuck kite | 7 | 1 | 0 |
| the child holds the reel or the string | 16 | 10 | 0 |

Of the old pose: "- The kite string lies slack on the ground in a loop before reaching the boy, which fits a stuck kite; but the boy holds the reel up as if still flying it."

**Round 2** (24 readings an arm, eight readers, three pictures a reader):

| | B | C |
|---|---|---|
| stuck, with nothing beside it | 17 (6 readers; 5 in all three) | 21 (8 readers; 6 in all three) |
| another reading only in the unsure section | 7 (3 readers) | 3 (2 readers) |
| the child holds the reel or the string | 24 | 0 |
| the child points or reaches up, in the description | 22 | 24 |
| the spool on the ground remarked in the unsure section | | 22 |
| whose kite it is doubted | 0 | 6 (3 readers) |
| nothing said of whose it is | 0 | 11 |

B: "On the left, a yellow kite is stuck in a tree; its string runs down to the grass, loops, and goes up to a boy in a yellow shirt and orange shorts who holds the reel and points up at the kite." C: "- The spool lies on the ground rather than in the boy's hand, so it could be his dropped spool or not his at all. With him pointing at the kite, the natural reading is that his kite got stuck."

**B was taken.** Over the two rounds stuck stands alone in 24 readings of 34 with B and 30 of 34 with C, for 7 of 16 of the old pose. The gap between B and C is four readings in round 2, which one reader's three pictures nearly make; and C costs the action (no reading says what the child holds, so the item would become a pointing), adds an object that 22 readings of 24 stop at, and lets three readers of eight doubt that the kite is the child's. In the tier-4 garden, where a second child reaches for a balloon, no reading of fourteen mixes the two.

## R3: the heavy seesaw

**The man.** After two rounds of v0.57's bench nine readers of ten had him in front of his seat. The worker found the hips already on the pad: the feet stood 34 cm ahead and 20 cm out to each side, so that the side view showed one long limb slanting from the hip across the plank, with no knee. Now the thighs lie along the pad and rise to the knee, the shins are upright, and the pad runs on to 15 units short of the near foot.

| | old (S 5, O 10) | new, round 1 (20) | new, round 2 (48) |
|---|---|---|---|
| off his seat or not surely seated | 6 | 1 | 0 |
| any remark on how he sits | 10 | 4 | 10 (his legs over the beam in 6) |
| keeping her up on purpose, offered | 7 | 2 | 3 |

Of the old: "- The man seems to sit slightly in front of the yellow seat, on the beam, rather than squarely on it. It might just be the drawing angle." And the on-purpose reading came with it: "- The old man's legs look like he is half standing / bracing on the ground rather than fully seated, which could mean he is holding the seesaw down for the girl." Taken.

**The child.** The list wanted her to grip the handle with both hands and lean back. Round 1 read that (B) and a second pose (C: bent forward over the handle, a leg stretched down), each with the new man:

| round 1 | old (15) | B (10) | C (10) |
|---|---|---|---|
| stuck or kept up, any form | 7 | 6 | 4 |
| his weight as the cause | 12 | 7 | 5 |
| an ordinary game, a bounce, a passing moment | 1 | 5 (3 readers) | 0 |
| a word on her face: worried, alarmed | 6 | 0 | 3 |
| slipping or sliding off her seat | 0 | 0 | 4 (2 readers) |

Neither was better than v0.57's child, whose face shows and whose arm is stretched toward him; B's bowed head hides the face. Round 2 set v0.57's child (E) against B, both with the new man, 24 readings an arm:

| round 2 | E | B |
|---|---|---|
| stuck or kept up | 20 (7 readers of 8) | 1 |
| his weight as the cause | 19 | 14 |
| weight and stuck in one reading | 18 | 1 |
| worried or afraid | 18 (6 readers) | 1 |
| an ordinary game as the reading | 0 | 4 (4 readers) |
| the tilt "fits" or "makes sense" | 4 | 10 |

E: "Her feet dangle well off the ground, so she seems to be stuck up in the air because he is much heavier." B: "The seesaw is tipped down toward the man, which fits him being much heavier." v0.57's child stays; B and C are behind the cast's switch `TPDB_STUCK58`.

What is still open: in E the word is hedged more often than not (stuck plainly in 6 readings of 24, with "seems" or "as if" in 8, only in the unsure section in 6), and of the 83 readings of both rounds none says that she wants down and two offer calling out, each beside another reading ("her mouth is open, as if she is calling out or worried").

## O2: the plain seesaw

v0.57's raised child sat as on a bench, level over a plank that falls away: "- The girl on the high end appears to sit slightly in front of or beside the seat handle rather than clearly on the seat; her placement looks a little floating." The new pose (`seesaw_high`) sits on the pad with the thighs along the plank and both fists on the handle. Off or above her seat, floating, or beside the handle: 3 readings of 12 old, none of 8. Any remark on her seat, legs or posture in the unsure section: 5 of 12, none of 8. Her legs are said to hang in 7 of 8, in the description: "A smaller girl in a pink outfit sits on the raised right end holding her handle, with her legs dangling." Nobody in either arm says that she is stuck. Taken.

## The fence's rails

v0.57's flat ball could stand on a rail of the garden's fence. The rule keeps its disc 10 units off each rail's band, so the game stands further forward and the ball is over the grass. All 17 readings state the throw and the catch. The ball is tied to the fence in 3 readings of 9 old and none of 8: "- The ball is level with the fence, quite high for the small girl. It might go over her head, or she might catch it." Taken; it costs one seed of twelve at most. Pushed off the rails, the ball lies across the fence's foot line a little more often (2 placed games of 12 for 1), which no reader of eight remarked on.

## What was not benched

- The other six templates that the strict count marks down. The floating box's tilt and its missing ground shadow are benches already run (`draw.floating_crate`); the lost balloon, the stalking cat, the windy hat, the upward water and the dog at the door have no plain mend, and each reads 1.00.
- The grown figures called young first (O1): no drawing. The scorers now write the word into a field of its own.
- The barrow wheeled with the larger wheel (HC).
- A tier-4 plan that cannot be cast in a second setting: `tools/cycle/t4_cell_iso.py` already refuses such a cell before it tries an isomorph, and the planner was left.
