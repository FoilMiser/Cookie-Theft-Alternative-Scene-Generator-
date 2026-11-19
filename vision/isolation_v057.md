# v0.57 isolation bench

The brief for v0.57 was Sam's: "Go for v0.57". The list is `flaws_v056.md`: one template under the gate (R1, the game of catch), two at its edge (R2 the frying pan, R3 the heavy seesaw), one to watch (R4), the templates that the strict count marks down (R5), the oddities (O1 to O7), two rows of the keys (K1, K2) and one of grey (G1). This file is about the drawings and the rules that were read; the keys are in `screen_prompts.md`.

Every drawing was put behind a switch whose `O` is v0.56's drawing, and each was read blind in whole pictures before it went into scenes. A scene's switch is `scene.sw57(NAME)`, which is `O` for any record older than revision 51; a cast's is `TPDB_<NAME>57` in `castlib`. With `TPDB_REV57=50` and `TPDB_ONLY57=<names>` the drawings act in v0.56's own records and nothing else moves, so a bench picture is a screened picture of v0.56 with one thing drawn another way (`tools/cycle/bench_build.py`).

There were two rounds:

1. **Round 1** (`isolation_v057/bench`): 27 of v0.56's pictures in up to four arms and five new pictures of the game of catch in two, 125 readings by 16 readers (`tools/cycle/bench_prepare.py`).
2. **Round 2** (`isolation_v057/bench2`): what round 1 left open, 50 readings by 12 readers (`tools/cycle/bench_round2.py`).

A reader is a fresh agent that is given the screen's own reader prompt and its pictures and nothing else; no reader has a scene twice. The arms of round 1: `S` is the reading v0.56's own screen had of a picture, `O` a fresh reading of the same picture, `B` the picture built again with the new drawing, `C` an alternative, `P` v0.55's pan, `F` a new picture with the new drawing and `G` the same new picture with the old one. Five analysts who never saw a picture counted round 1 from the readers' own lines (`isolation_v057/digest`, with their briefs); I counted round 2 myself, and the pan again by reader. Quotations are from the readers' own files.

## How the work was shared

Four workers drew at the same time, each with a scratch folder and classes of its own: the game of catch (R1), the pan (R2), the heavy seesaw (R3, O4), and the pond, the wind and the greys (O2, O5, G1). The kite (R5), the keys and the counts were mine. Two workers were called back after round 1 with the readers' own words.

## What was read, and what came of it

| Row | Switch | The drawing or rule | Round 1 | Round 2 | Result |
|---|---|---|---|---|---|
| R1 the game of catch | `ARC`, `CATCHLINE` | a flat flight, 45 units over the straight line from hand to hands; the ball and its dashes off the fence's or railing's top line, 150 units from a cat on the fence, off the pond | no doubt of any kind: 0 of 6 as it was, 4 of 6 flat; in new pictures 4 of 10 flat for 1 of 5 with the old arc | | taken |
| R1 | `CATCHCAST` | the catcher is a child or a teenager, and the taller of the two throws | who threw it was asked in 4 readings of 8 where a grown figure caught, in none of 8 where a child did | no doubt in 6 of 10; who threw it asked in 2 | taken |
| R2 the pan | cast `PAN57`, scene `PANFLOW` | a hollow pan on a wooden handle, tipped, the water leaving over its rim as a sheet; `B` with a pale inside, `C` with a dark one | a watering can first: 3 of 10 as it was, 4 of 9 for v0.55's, 4 of 10 pale, 1 of 10 dark | 0 of 10 dark | `C` taken |
| R2 | `CANBY` | an unused watering can on the grass behind the holder | | a frying pan, plainly, in 20 readings of 20 | taken |
| R3 the heavy seesaw | `SEAT` and cast `SEAT57` | a yellow seat with a back at each end of the plank, rubber buffers under the plank's ends; `D`: the seat drawn where its rider sits | where he sits doubted in 9 of 10 as it was, 9 of 10 and 7 of 10 with the seat | 9 of 10 with `D` | `D` taken; the doubt is not settled |
| R3 | `HEAVY` and cast `HEAVY57` | the man without his book: a hand on each knee, looking up at the child | his weight given plainly: 5 of 10 as it was, 1 of 10 with the book on the new seat, 6 of 10 without it | 10 of 10 | taken |
| R5 the kite in the tree | `KITESLACK` | the string drops from the reel to the grass, lies there in a curl and runs along the ground before it rises to the branch | stuck with nothing beside it: 0 of 8 as it was, 6 of 8 | | taken |
| O2 the pond's own figures | `PONDOWN` | the bread thrower and the angler stand where at most 0.30 of their height is above the near shore | over the rim or the edge: 7 of 8 as it was, 1 of 8 | | taken |
| O5 the wind | `WINDLINE` | in a park the cap and the wind's lines are off the pond, with open air ahead of the cap; the washing hangs straight from its pegs and curves out at the hem | the cap about to land in the pond: 4 of 4 park readings as it was, 0 of 4 | | taken |
| G1 grey | `GREYCOL` | a deeper pink for the paint, a darker box in the walker's way, a purple cap where the draw gave orange | the paint is pink to all 8; the box is a box to all | | taken |

## R1: the game of catch

v0.56 screened the game in three pictures, and in the two gardens the ball stood at the fence's top above the catcher. The six readings of those three pictures as they were (the screen's and three fresh ones) all doubt the ball: "- The ball's direction: it could be a throw to the girl that is still rising, or a throw that is going too high and could go over the fence; it is roughly level with the fence top and close to the cat." All four readings that tie the ball to the fence or the cat are of the old arc.

With the flat flight four readings of six are plain and the other two doubt mildly: "- The ball is still close to the thrower and quite high relative to the small girl; it could sail over her, but it reads as a throw to her." No reading of the flat flight, in 16, names a fence, a cat or the pond with the ball.

The five new pictures showed what the three old ones could not. Where a child threw to a grown figure with raised hands, the flat flight left the ball halfway between two raised arms, and who threw it was asked in four readings of eight: "- The ball could be thrown by the child to the woman, or thrown by the woman to the child; the dashed line from the child's hand suggests the child threw it." With the old arc on the same pictures nobody asked it, and three of five doubted the path. Where the catcher was a child, nobody asked it in eight readings. So the catcher is now cast young and the taller of the two throws (`CATCHCAST`; the first draw is kept, so that v0.56's three games are cast as they were).

Round 2 read five new pictures with that rule, two readers each. Six of ten are plain: "In the front of the garden, a boy in a red cap and blue hoodie has just thrown a red ball (a dotted line shows its path) toward a smaller child in a yellow top and orange shorts, who has both arms out ready to catch it." Two ask who threw it and settle it by the dashes, both in the two pictures where two small children of one height play; one has the catcher's arms as reaching or pointing; one has the ball high: "- The ball is quite far from the girl and well above her hands; it could be a throw that falls short or goes over her, or simply a ball in flight that she will catch."

What the rules cost, in seeds placed of twelve with the band off: the line rule one seed in the park alone (9 for 10), one in a garden with a cat on the fence (10 for 11) and two in a park with two other events (4 for 6), where the flat flight itself places more often than the old arc; the casting rule nothing, and it places more often in three sets of five (12 for 10, 10 for 7, 10 for 7), since two children need less room than a child and a grown figure. A playground with two other events that need a child cannot cast the game at all.

Not done: the garden fence's two rails have no anchor, and the flat ball can stand on one.

## R2: the frying pan

The list asked for the two pans again with eight readings or more an arm, and a third with its flat inside turned to the viewer. That third had lost in v0.19 and v0.23, so the worker drew another: a pan that is hollow, on a wooden handle, tipped toward the viewer so that its round inside shows, with the water running over its low rim as a sheet. v0.56's pan had no hollow and let its water go from its far tip in an arc.

Round 1, 39 readings. A reading that calls the vessel a watering can first or only:

| Arm | Readings | A watering can first | Says a pan is the wrong thing to water with |
|---|---|---|---|
| v0.56's shallow pan (`S` and `O`) | 10 | 3 | 6 |
| v0.55's deep pan (`P`) | 9 | 4 | 5 |
| the hollow pan, pale inside (`B`) | 10 | 4 | 3 |
| the hollow pan, dark inside (`C`) | 10 | 1 | 7 |

The pale inside was "a grey watering can" each time. But counted by reader the table says less than it seems to: all ten of those readings come from four readers of sixteen, and each of the four wrote it for every pan it was given, whichever arm: "- Watering can, in the man's hand: grey, pan-shaped with a long handle; pouring water." Water poured on flowers makes the vessel a watering can to such a reader, and no pan converts it. The dark inside was taken on the table, and the question for round 2 was the habit.

Round 2 put an unused watering can on the grass behind the holder (`CANBY`), so that the picture shows the right tool beside the wrong one. A reader had pan pictures of one arm only: eight readers the can's, four the pan alone. With the can, 20 readings of 20 call the vessel a frying pan in the free description and say the can stands unused: "The strange thing is that he waters the flowers with a frying pan while the watering can is right beside him." Alone, the dark pan is a frying pan, or a frying pan or saucepan, in 10 of 10, and seven add that it could be an oddly drawn watering can or scoop.

Revision 18 had taken the garden's own watering can out of every picture with the pan, after readers of v0.19 remarked on a watering can standing unused; it was logged then as an oddity. `CANBY` reverses that on purpose: the remark is the contradiction, read. The can is a second cue of both contradiction items (`CANBY` `C`), which lowers their predicted difficulty by 0.30.

The side-only stand: with the tipped pan the holder stands beside the bed and not in front of it, where the sheet was a stub. It costs nothing against v0.56 (the same six seeds of twelve in the garden).

## R3: the heavy seesaw

Two things were on the list: where the man sits, and what says he is the heavier.

**The book.** Both half marks of v0.56 came where the reader had the man ignoring the child. Round 1 read the five pictures with the new seat and the book (`B`) and with the new seat and no book (`C`): the man with a hand on each knee, looking up at the child.

| Arm | Readings | His weight, plainly | His weight beside another reading | Stuck, no weight given | Neither |
|---|---|---|---|---|---|
| as it was (`S` and `O`) | 10 | 5 | 0 | 5 | 0 |
| the seat, the book (`B`) | 10 | 1 | 2 | 6 | 1 |
| the seat, no book (`C`) | 10 | 6 | 1 | 2 | 1 |
| the seat where he sits, no book (round 2) | 10 | 10 | 0 | 0 | 0 |

With the book the usual reading is that she is up because he reads: "On the low end sits an older man with grey hair, a flat cap and a brown waistcoat, reading a newspaper or book instead of playing, so the girl stays up in the air." Without it: "The seesaw tilts down on his side, as you would expect since he is much heavier, so the girl is up in the air." In round 2 three readings of ten say she is stuck, and most call the tilt what one would expect. Under `HEAVY` the man's item is `sitting on the low end of the seesaw, looking up at the child`, and the inference no longer accepts that he is not noticing.

**The seat.** v0.56's stops were small dark blocks, the raised one alone on the grass under the child. Now each end of the plank carries a yellow seat with a back and has a rubber buffer under it; the raised buffer goes up with its end. No reading of 30 calls the seats or the buffers odd, and a reading that has the man beside the seesaw, on something hidden or leaning on it from the ground goes from five of ten as it was to three of ten and one of ten. But the readers then saw him in front of his seat: "- The man appears to sit slightly in front of the yellow seat rather than squarely on it, so it is a little unclear whether he is seated on the seat or on the beam." The worker drew the seat where its rider sits, its back upright directly behind his hips and the pad under his thighs (`SEAT` `D`), and round 2 read it: nine readings of ten still doubt it. "- The man looks as if he is sitting slightly in front of the yellow seat rather than squarely on it, but it reads as sitting on the seesaw." `D` is taken, since nothing reads worse with it and the blocks are gone; the doubt goes to the next list.

One of v0.56's plain seesaws (`T3_playground_s24739`) comes back as another picture: the pram that failed on its first seed now places there.

## R5: the kite in the tree

On the strict count the kite was caught with flying in front of the tree beside it in four pictures of five, a second screen running, and v0.56's new kite had read no better. The eight readings of the four benched pictures as they were all have it: "- The kite: it could be stuck in the tree, or just flying low in front of it; it overlaps the leaves and the string droops, so stuck seems more likely." The string hung in one sagging curve from the branch to the child's raised hand, which is how a low kite's line looks.

Now the string drops from the reel to the grass, lies there in a curl and runs along the ground before it rises to the branch. Six readings of eight have the kite stuck with nothing beside it, and all eight name the string on the ground: "The kite string runs from the tree down to the grass, lies slack in a loop on the ground, and then goes up to the child's hand, so the kite is stuck and not flying." Three find the slack line itself a little odd for a string that is held up.

Its cost: the ground under the line is kept clear, and the tier-4 park, which held the kite, no longer places on its seed.

The other templates of R5 were looked at and left. The jumper's two calls are a jump given beside cheering, which the key accepts, and one reader who has him standing; the begging dog's and the walked dog's are hedges about who greets or pulls whom; the fish in the tree is called impossible with a toy beside it; and the walker may step past the box.

## O2, O5 and G1

**The pond's own figures.** Their feet were already well under the shore; what the readers saw was the shore across legs and hips: "- The man's arm reaches over the pond's rim and his lower body overlaps the pond edge; he appears to stand on the grass at the edge, but at a glance it could look like he is standing in the water's rim." Standing lower on the lawn, seven of eight readings have the figure on the grass, four of them remarking that it stands back from the edge: "- The boy stands a little back from the pond's edge; the rod is long enough to reach, so it looks plausible." Both readings of one bread thrower have a piece of bread in the air over the grass.

**The wind.** The lines already stood behind the cap; the two oddities of v0.56 are one reader's sentence, which reads the direction right. What the bench found instead is the pond: all four fresh and screen readings of the two parks have the cap about to land in the water, and one takes the lines for ripples. With the cap over hills and sky none of four does. Every reading in every arm has the cap blown off with a hedge beside it, whose cap it is or whether the hand waves. The straighter washing was blowing to one reader and "could be read as blowing or simply hanging" to the other.

**Grey.** The deeper pink is pink to both readers of each paint picture, bright pink to two of the four; the prints and the dog that made them are named by all. The darker box is a cardboard box to both. The five records that v0.56's check flagged pass it.

## O1: the grown figures called young first

Counted by pose before anything was drawn (`tools/cycle/who_pose.py`): the man in the red shirt is a boy as he paints (once in three), eats an ice cream (twice in three, one reader) and looks into the hose (once); the woman in purple is a girl as she looks into the hose and as she walks reading. Looking into the hose's nozzle made both grown figures young, to two readers. Four readers of sixteen wrote the six. It is the activity as much as the drawing, and nothing was drawn.

## What was not benched

R4, the man who sits on nothing, was a half mark in one picture where he is small at the picture's edge: left to watch. O3, the thief bird's size, is the list's own mend of v0.56 and no misreading: left.
