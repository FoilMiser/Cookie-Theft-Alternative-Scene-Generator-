# v0.56 isolation bench

The brief for v0.56 was Sam's: "I will compact, go for v0.56, work the whole list". The list is the second part of `flaws_v055.md`, what seven reviewers and three counts found in v0.55's 99 pictures after its release: five rows at the gate (R1a to R4), eleven inferences and contradictions that are read two ways (I1 to I11), twelve rows of the cast (C1 to C12), ten of placement (P1 to P10), eight of grey (G1 to G8) and four of the keys (K1 to K4). This file is about the drawings. The placement rules, a revision 50, are in `design_tests_v056.md`.

Every drawing was put behind a switch whose `O` is v0.55's drawing, and each was read blind before it went into scenes. There were three benches:

1. **Pairs** for the cast's drawings: v0.55's figures against the trial cast's, large and at a picture's size, each set in both orders (46 reviews in three rounds).
2. **Whole pictures, round 1**: 60 of v0.55's pictures in up to four arms and 19 new pictures, 268 readings by 34 readers.
3. **Whole pictures, round 2**: what round 1 left open, 50 readings by 12 readers.

A reader or a reviewer is a fresh agent that is given one prompt's text and its pictures and nothing else. Quotations are from their own files, under `isolation_v056/`.

## How the work was shared

Eight workers drew at the same time, each with files of its own and a scratch folder, each drawing behind its switch: the square wheels (R1a, R1b), the thief bird and the hose (R3, R4), the seesaw (R2, C8), the seated skirt, the reading eyes and the faces (C1, I7, C11), five poses (C2, C3, I5, C7, C9), five more with their props (C5, C6, C10, I11, K4), the animals (I4, C4, I2) and the props of the scene (I1, I3, I8, I10, P7, the greys). A scene's switch is `scene.sw56(NAME)`, which is `O` for any record older than revision 50; a cast's is `TPDB_<NAME>56` in `castlib`. With `TPDB_REV56=49` and `TPDB_ONLY56=<names>` the drawings act in v0.55's own records and the placement rules of revision 50 do not, which is how the bench built v0.55's pictures again.

## The pair bench (`r1`, `r2`, `r3`)

`tools/cycle/fig_pairs.py` makes a sheet of two rows, v0.55's cast and the trial cast, four figures a row (three for the cone and the hose, two for the cats), each figure whole at 800 px per metre and under it the same figure at a picture's size. Each set is made twice, one drawing above and then the other; a reviewer has one sheet, says what each figure is doing in each row, lists each row's faults and chooses a row. The map of which row is which was kept outside the folder until the reviews were in (`r1/map.json` now). A set whose choice follows the row's place in both orders is a toss-up.

| Set | Switch | Round 1, new above | Round 1, v0.55 above | Round 2 | Result |
|---|---|---|---|---|---|
| Hanging washing | `HANG56` | new | new | | taken |
| The child with the dropped cone | `CONE56` | new | new | | taken |
| The child on the swing | `SWING56` | new (a toss-up) | new | | taken |
| The pan | `PAN56` | new for both pans | new for both pans | | taken |
| The bucket's handle | `BUCKET56` | v0.55 for both | v0.55 for both | | not taken |
| The sleeping dog | `SLEEP56` | new for both | new for both | | taken |
| The dog at the door | `DOOR56` | v0.55 for both | no difference | | no gain; to whole pictures |
| The feeder's bag | `FEED56` | v0.55 | new | new, new | taken after a mend |
| The painter | `ROLLER56` | v0.55 | v0.55 | v0.55, v0.55 | not taken |
| The stalking cat | `STALK56` | v0.55 | v0.55 | v0.55, v0.55 | not taken |
| The storm pointer's arm | `POINT56` | v0.55 | v0.55 | v0.55, v0.55 (a toss-up) | not taken |
| The reader's eyes | `EYES56` | no difference | no difference | | not taken |
| The seated skirt at three-quarters | `SKIRT56` | new | v0.55 | v0.55, v0.55 | not taken |
| The seated skirt from the front and the side | `SKIRT56` | no difference in the skirt | no difference in the skirt | one each | not taken |
| Kneeling to plant | `KNEEL56` | v0.55 | new | v0.55, new | a toss-up by place; to whole pictures |
| The child stuck on the seesaw | `CALL56` | v0.55 | new | | a toss-up by place; to whole pictures |
| The hose's nozzle | `NOZZLE56` | v0.55 | new (a toss-up) | | a toss-up by place; to whole pictures |
| The walk's stride (round 3) | `STRIDE56` | v0.55 | new | | a toss-up by place; not taken |

What the reviewers wrote, set by set:

- **Hanging washing (C3).** v0.55's arms go up with the palms together: "It could be diving, stretching or praying, and there is no object to explain it." The new arms are apart, a peg in the far fist. Both reviewers chose them.
- **The cone (C7).** Of v0.55's row: "All three: the face is almost fully hidden by the hand and the bowed head; at the small size there is no readable face at all, only hair and a hand." The new head is bent toward the cone with a hand at the cheek, and the cone's mouth is wafer-coloured.
- **The swing (C9).** Of v0.55's hands at the chest: "At the small size the arms are almost invisible and the figures look armless or hunched." A fist on each rope was chosen in both orders.
- **The sleeping dog (C4).** "Row a's angled eye strokes make the sleeping dogs look cross." (v0.55's row.) The new dog is curled, chin on its paws, the eyes two closed arcs.
- **The bucket (I11).** The wire handle was "a stick-like handle across the face that looks wrong at both sizes". The bucket stays as it was; the shallow pan with a long handle was the better pan to both reviewers.
- **The feeder's bag (C2).** Round 1's bag sat on a box: "in a the sack-on-box stack looks like a vase and is hard to read". Mended to one paper bag held by its neck in front of the thigh, it was chosen in both orders, four figures of four each time.
- **The painter (C5, P10).** A level sleeve held out at belly height lost twice. Of v0.55's raised roller: "The raised roller reads at once as painting a wall, while in b the hand at her mouth and the low roller make the action unclear." Of the mended one, upright with a pole: "in b the flat roller in its frame could be a tray, a rolling pin or a cart handle". v0.55's pose is kept, with the sleeve pink (`ROLLER56` `D`), so the painter still stands where v0.55 put him: P10's long step is not mended.
- **The cat (I4).** A flat crouch lost its legs: "row b turns the body into a long low lump with no readable legs". A low creep on four legs lost again, and the reviewer of round 2 wrote of v0.55's own cat that it moves "as if creeping or stalking". v0.55's cat is kept.
- **The pointing arm (I5).** Nearer upright it stopped pointing: "the vertical arm in b looks more like raising a hand to ask a question"; at about sixty degrees, "row a's nearly upright arm with a small hand looks more like asking to speak". v0.55's arm is kept, and the fault goes to a placement rule (`RAINLINE`).
- **The reader's eyes (I7).** Lowered lids on the two men who read with the head up: "I cannot see a real difference between the rows". Not taken.
- **The skirt (C1).** One sheet over both thighs with one hem. In round 1 it made the seated pose plain, "Her knees and thighs make the seated pose obvious, where row b's lap looks like a box she is sitting inside.", and left stray shapes at the hem. Mended to a straight hem it lost in both orders: "Row a's lap is so short that she looks like she is standing with bent knees; row b is clearer, though its lap is a little boxy." and "In b the skirt bulges out behind like a pillow and the torso looks heavy for a slight older woman." Eight reviews had v0.55's seated skirts in front of them and none called them shorts; one wrote it of the new row, "in row a the skirt looks like shorts". v0.55's skirt is kept.
- **The seesaw's child (R2).** One arm stretched down toward the man: "the straight arm looks like a sleepwalker or someone pointing". Alone on a sheet the gesture has nobody to go to; whole pictures decide.
- **The nozzle (R4).** Twice the size and turned to the viewer it is seen, and looked into: "row b's big nozzle aimed at the face invites a telescope reading". Looking into it is the intended reading, with a hose; whole pictures decide.
- **The stride (C10).** Three quarters of v0.55's stride. Each reviewer chose its lower row, and the one who had the new row above wrote: "Row a's bent-knee crouch makes several figures look sneaky or unsteady." v0.55's walk is kept.

The faces (C11) were looked at by their worker and not put to reviewers: a side view's mouth set further in is a red oval on the cheek, and smile and sad are no easier to tell apart.

## Whole pictures, round 1 (`bench`)

**The arms.** `tools/cycle/bench_build.py` builds a picture of v0.55 again on its own record's plan, the same seed and forced set at revision 49, with only the drawing switches acting.

| Arm | What | Pictures | Readers a picture |
|---|---|---|---|
| O | v0.55's picture as it was screened | 61 | 1 (picture 51: 8) |
| B | the trial cast and every drawing of the scene at its first value | 60 | 2 |
| C | the alternatives, where a picture holds one: the wheelbarrow's open square wheel, the hose pressed flat with no swelling, the larger bird still pecking, the seesaw's seat backs with the child's cupped hands, the red lead | 17 | 2 |
| L | picture 51 (`T4_playground_s512950`) with the bicycle leaning on a post and nothing else changed, v0.55's cast | 1 | 8 |
| F | new pictures under revision 50 with the trial cast, forced sets (`tpdb_work/v056/bench/build_F.py`) | 19 | 2 |

`bench_prepare.py` chose 60 of v0.55's pictures row by row, up to four pictures for each row of the list, those first that serve the most rows, and dealt 268 readings to 34 readers, at most eight pictures a reader and no picture twice for a reader in any arm. Six of v0.55's 99 pictures did not place again on their own plan with the new sprites' boxes, picture 51 among them: the larger thief bird moved its other events. So picture 51, where the bicycle's fault was found, was read with the bicycle's drawing alone changed (arm L), and the held bicycle was read in new pictures (arm F).

**The counting.** `bench_tally.py` wrote, for every row, each reading's own sentences, inventory lines and unsure lines that hold one of the row's words (`digest/tally_<row>.txt`). Six analysts, fresh agents that never saw a picture, were told the arms and the intended reading of each row, counted the readings and quoted every one that was not the plain intended reading (`digest/analyst_1.txt` to `analyst_6.txt` are their briefs, `digest/digest_<row>.md` their counts). The counts below are theirs; the bicycle's and the wheelbarrow's were read again line by line. A count is of readings, not of lines.

### The gate's rows

| Row | Counted | O | B | C | L | F |
|---|---|---|---|---|---|---|
| R1a, the bicycle | square wheels called wrong in the description or the inventory | 4 of 10 | 2 of 4 (leaning) | | 0 of 8 | 6 of 6 (held) |
| | how it stands is doubted, or it lies down | 5 of 10 | 1 of 4 | | 6 of 8 | 0 of 6 |
| R1b, the wheelbarrow | square wheel called wrong in the description or the inventory | 1 of 4 | 2 of 8 (solid) | 5 of 6 (open) | | 0 of 2 (solid) |
| | the wheel a box or a block, or not named | 0 of 4 | 2 of 8 | 0 of 6 | | 0 of 2 |
| R2, the heavy seesaw | where the man sits is doubted | 2 of 3 | 1 of 6 | 0 of 6 | | 0 of 2 |
| | stuck because he is heavier, plainly | 1 of 3 | 4 of 6 | 3 of 6 | | 0 of 2 |
| R3, the thief bird | stealing or eating, with no other reading | 4 of 11 | 3 of 6 | 4 of 4 | 4 of 8 | 2 of 6 |
| R4, the hose | the dog as the one cause | 0 of 4 | 6 of 8 | 1 of 8 | | 2 of 2 |

- **The bicycle is held (R1a, `BIKE` `H`).** Its owner, a grown figure in a new pose (`hold_bike`), stands on its far side with a hand on the handlebar; there is no stand. All six readers of three new pictures named the square wheels as the wrong thing and none doubted how the bicycle stands: "On the left a man in a green shirt and beige trousers is walking with a red bicycle, holding its handlebars; the bicycle has square wheels, which is impossible." On its stand in picture 51 two readers of eight said so in the description or the inventory and four only among the things they were unsure of. **Leaning on a post it read worse than on its stand**, the same picture and eight readers each: none of eight, four who did not name the wheels at all, and six who doubted the post: "The bicycle and the wooden post overlap so the post seems to go through the middle of the bike frame; it could be read as the bike being locked/leaning against the post, or as the post passing through the bike." Leaning is not in the release; a bicycle with nobody free to hold it is not placed. The held bicycle was not read in picture 51 itself, which has no room for an owner.
- **The wheelbarrow's wheel is the open square (R1b, `BARROW` `C`).** At the round wheel's size and under the tub's nose, as the list asked, the solid square was a block: "A red wheelbarrow stands near the fence, with a black box-shaped thing at its front." Seven readers of eight used the word block or box for it. The same square open on its spokes was named as a square wheel and as wrong by five of six. The tub is red in both (`BARROWCOL`), grey 96 on grass at 168 where the grey tub was 159.
- **The seesaw's ends rest on stops, and the child stretches an arm down to the man (R2, `LOWEND` `B`, `CALL56` `B`).** With the low end on a stop the man sits on the plank: of v0.55's, "The man's body looks partly next to/behind the seesaw board rather than clearly on the seat; he could be read as sitting on the low end or as sitting on the ground and leaning against it."; with stops one reader of fourteen doubted it. Seat backs on top of the stops (arm C) were named by nobody. The child's cupped hands (arm C) were the old two-way reading again, worried, surprised or giggling, in six readings of six; the stretched arm was calling or pointing in two readings and went unremarked in six, and no reader of it wrote of nervousness. The stops were named by three readers of this seesaw and three of the plain one, as small dark or black blocks, bumpers to some.
- **The hose keeps its swelling and gains a nozzle, a drop and a seep (R4, `HOSE` `N`).** The nozzle is twice the size and turned to the viewer (`NOZZLE56`), one drop forms at its mouth (`DRIP`) and a little water seeps where the hose leaves the reel (`SEEP`). Eight readers of ten gave the dog as the one cause, where none of four did for v0.55's drawing. Pressed flat under the paw with no swelling, as the list proposed, it was one of eight: seven doubted that the dog is on the hose or blocks it, or offered a leak at the reel instead. v0.50's bench found the same of a hose with no swelling (`HOSE50`). Every reader saw the water at the reel and most called it a leak: "The water by the hose reel: could be a leak at the reel, or water backing up because the dog is blocking the hose." Round 2 asked whether the seep earns its place.
- **The thief bird (R3)** was not decided by round 1: four of four for the larger pecking bird is two pictures and four readers. It went to round 2.

### The other rows

| Row | Counted | O | B | C | F | Taken |
|---|---|---|---|---|---|---|
| I1, the parcel | called a parcel or a delivery, plainly or as one of two | 1 of 4 | 6 of 8 | 3 of 4 | 2 of 2 | `PARCEL` |
| I2, the lead | called a garden hose | 0 of 4 | 6 of 8 (yellow) | 2 of 10 (red) | 2 of 2 (yellow) | no |
| I3, the kite | caught, with flying in front of or behind the tree beside it | 3 of 4 | 8 of 8 | | 2 of 2 | `KITE`, for its grey |
| I4, the cat | stalking, with nothing beside it | 0 of 3 | 1 of 6 | | 0 of 2 | no |
| I8, the rising water | going up and wrong | 3 of 3 | 4 of 6 | 2 of 2 | 0 of 2 | no |
| I10, the floating box | thrown, falling or blown offered beside floating | 2 of 2 | 4 of 4 | 2 of 2 | 2 of 2 | a rule |
| I11, the pan | called a frying pan first | 2 of 3 | 6 of 6 | | 2 of 2 | `PAN56` |
| C2, the feeder's bag | said to be held | 1 of 4 | 5 of 7 | | 3 of 4 | `FEED56` |
| C4, the sleeping dog | asleep, with nothing beside it | 2 of 4 | 3 of 8 | 0 of 2 | 2 of 4 | `SLEEP56` |
| C6, planting | planting, with nothing beside it | 2 of 4 | 5 of 8 | | 2 of 2 | `KNEEL56`, `SEEDLING` |
| C7, the cone | a word about the eye | 9 of 12 | 2 of 8 | | 2 of 4 | `CONE56` |
| C8, the seesaw at play | level, or its tilt doubted | 2 of 3 | 0 of 6 | | | `TILT` |
| P7, the ball's trail | who threw it, or where it goes, doubted | 1 of 4 | 6 of 8 | | | no |
| P8, the picnic | the sitter off the blanket | 0 of 3 | 2 of 6 | | 0 of 4 | the larger blanket |
| G5, the loose balloon | whose it is doubted | 6 of 12 | 2 of 8 | 0 of 2 | 2 of 2 | `LOSTCOL` |

(In arm C the parcel, the dog and the box are arm B's drawings in arm C's pictures. The eight readings of arm L, picture 51 as v0.55 drew it but for the bicycle, add to arm O: a word about the eye in 7 of 8, the balloon doubted in 4 of 8.)

- **The long lead is a garden hose (I2, not taken).** A lead of real length with a clip, trailing onto the step and ending in a hand loop: "On the far right, by the house door, a brown dog sits up holding a yellow garden hose in its mouth." In red it was a hose to two readers of ten and a doubt to more. v0.55's short strap was called a lead by four readers of four. The dog's pose at the door goes back with it (`DOOR56` `O`).
- **The rising water as streaks is a spray (I8, not taken).** Without the solid band there is nothing to say the water comes from the can: "The water from the watering can arcs in a loop shape back over the flowers with drops rising above them — slightly odd water path, but readable as watering." Both readers of the new picture described ordinary watering.
- **The trail only behind the ball loses the thrower (P7, not taken).** Nobody had the ball on a string in either drawing. With the dashes starting at the hand one reader of four doubted who threw; with them only behind the ball six of eight did: "The red ball's trail starts above the middle boy's hand but the ball is ahead and above him; it could be read as thrown by him to the girl, or as coming from elsewhere."
- **The bird turned away from the cat changes nothing (I4, not taken).** Every reader of every arm had the cat stalking, and all but one added that it might only be walking: "The cat could be stalking the bird to catch it, or just walking; its low crouch suggests stalking."
- **The kite on its limb reads as it did (I3).** Tipped on a limb at the crown's edge with its string wound round the limb: "The kite could be read as flying just in front of the tree rather than stuck in it, but it overlaps the branches and leaves, so stuck in the tree is the more natural reading." No reader named the wound string. It is taken for its colour: yellow or orange, grey 193 on leaves at 115, where the purple kite was 104 (G2).
- **The parcel is a parcel more often (I1).** With tape and a blank label, on the path at its edge: "The box looks like a delivered parcel (it has a label), but it could just be any box left outside." Every reader of every arm had it getting wet.
- **The floating box (I10).** No reader of v0.55's pictures tied the box to a hand; seven of eight wrote that nobody is near enough to have thrown it. In the new picture a child jumped for joy below it: "The floating box: it might have been thrown up by the jumping boy (he has his arms up as if he has just tossed it or is about to catch it), or it may simply be floating impossibly. It is far above him and to the right." The jumper and the box are no longer in one picture (`design_tests_v056.md`).
- **Planting (C6).** Kneeling on both knees with a seedling in the hand and a tray of seedlings by the bed. The second reading moved from digging to pulling out: "The man could be planting the flower or pulling one out (weeding); the hole, loose soil and seedling tray suggest planting." No reader of either drawing wrote of a lunge.
- **The cone (C7).** With the hand at the cheek the doubt is no longer the eye; four of the five doubts in arm B name the mouth, the nose or surprise.
- **Read as before, in both drawings:** hanging washing (15 readings of 15 plain), feeding the birds (15 of 15), bread for the duck (14 of 14), painting the fence (18 of 18, and the dog walked through the paint in every picture with prints), the swing (no reader of five wrote of the hands), the walker about to trip, the seated skirts (no line among the things a reader was unsure of, in 48 readings).

## Whole pictures, round 2 (`bench2`)

`tools/cycle/bench_round2.py` dealt 50 readings to twelve readers: the three scenes of round 1 that hold the thief bird, built three times each on their seeds under revision 50, four readers a picture, a reader having each scene once and each arm once; round 1's four pictures of the hose with no water at the reel and nothing else changed, two readers each as arm B had; and three pictures of a photographer (`design_tests_v056.md`). These 50 I counted myself from `digest/tally2_<row>.txt`, by the analysts' rules.

| The thief bird, stealing or eating with no other reading | Playground | Street | Park | Round 2 | Both rounds |
|---|---|---|---|---|---|
| B: half as large again, pulling the top slice off a larger sandwich | 2 of 4 | 4 of 4 | 1 of 4 | 7 of 12 | 12 of 24 |
| C: as large, pecking as v0.55's does | 1 of 4 | 1 of 4 | 2 of 4 | 4 of 12 | 8 of 16 |
| O: v0.55's bird | 0 of 4 | 3 of 4 | 1 of 4 | 4 of 12 | 12 of 31 |

- **The bird pulls a slice, and is no likelier to be read as stealing (R3, `STEAL` `B`).** Round 1's four of four for the larger pecking bird did not hold. In every arm about half the readers add that the bird may only be standing by the sandwich or eating crumbs, whatever the bird does. What the larger bird mends is its size: of v0.55's, "The bird and sandwich on the bench are small and hard to make out; could be read as the boy's lunch with a bird beside it, or a bird taking it."; of the new, "Next to him on the bench, a blue bird is pulling at his sandwich, lifting the top of the bread off; the man does not seem to notice." The item's words follow the drawing: a bird is pulling a slice of bread off a sandwich on the bench. With it go two rules of place (`STEALAT`): nobody's feet near either end of the bench, and no thief bird in a garden whose hose reel another template uses.
- **The seep stays (R4, `SEEP`).** Without the water at the reel three readers of eight gave the dog as the one cause, for six of eight with it in the same four pictures, and the tap came back: "The hose: the dog standing on it may be blocking the water (no spray is shown), or the woman may simply not have turned it on yet." The seep is read as a leak and does its work all the same.

## What is in the release

**The cast (builder 0.56.0).** New drawings of `hang_washing`, `cone_dropped`, `sit_swing`, `water_pan`, `feed_birds` and `feed_birds_low`, `kneel_plant`, `hose_inspect`, `seesaw_low` and `seesaw_low_read`, `seesaw_stuck_call`, the dogs' `sleep_paws_turn` and sleeping face, and the painter's sleeve in pink; new poses `hold_bike`, `throw_bread` (K4: the record said a figure throws bread, and she held it) and the songbirds' `tug`. Everything else is v0.55's: v0.55's whole library of 345 variants was rendered again from the new cast, and all but the variants of those poses came out alike, thirteen of them but for one pixel.

**Not taken, each kept behind its switch:** the seated skirt as one sheet (`SKIRT56`), the lowered eyes (`EYES56`), the steeper pointing arm (`POINT56`), the crouching cat (`STALK56`), the bucket's handle (`BUCKET56`), the shorter stride (`STRIDE56`), the level roller (`ROLLER56` `B`), the dog's raised paw at the door (`DOOR56`), the child's cupped hands (`CALL56` `C`); and in the scene the long lead (`LEAD`), the bird turned from the cat (`STALKBIRD`), the rising streaks (`UPW`), the short trail (`TRAIL`), the bicycle on a post (`BIKE` `L`), the solid square wheel (`BARROW` `B`), the hose pressed flat (`HOSE` `B`), the seesaw's seat backs (`LOWEND` `C`) and the larger bird pecking (`STEAL` `C`).

**What the list's rows became** is in `flaws_v056.md`, beside what the screen says of each.
