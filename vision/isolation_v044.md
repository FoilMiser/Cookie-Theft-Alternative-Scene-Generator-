# v0.44 isolation bench

v0.43's lesson was that a cut-out can read differently from a whole picture: the lying reading dog read as reading in three of three cut-outs and as "lying on an open newspaper" in four of the screen's five pictures. So the v0.44 bench read whole pictures, a tier-3 picture with the changed templates forced among the planner's own, each built in v0.43's drawing and in v0.44's. There were two rounds, with the screen's own whole-picture reader prompt (`tpdb_work/iso_round44.py`):
- round 1: nine readers of 17 pictures, two to a reader (one had one), never two pictures of one scene (`isolation_v044/round1`);
- round 2: four readers of 8 pictures, two to a reader (`isolation_v044/round2`).

`map.json` in each says which picture is which case. The first three letters of a case name the scene; the fourth the drawing: O v0.43's cast (`BENCH_CAST=assets/cast/out043`) and revision 41's rules; N the cast with every v0.44 switch on (`tpdb_work/bench44/out_N`) and every revision-42 rule on; A and G the reading dog's two v0.44 drawings; T, B and C round 2's.

What was drawn is three lists: `flaws_v043.md`'s and Sam's two notes on the v0.43 figures (`figure-fixes-v043.md`, the screen's findings ranked, and `figure-review-v043.md`, a review of every v0.43 render; both kept in `tpdb_work/`). Ten changes are in the cast, behind switches read when it is built:
- `TPDB_READ44` (R1, the notes' item 1, the review's item 7): the reading dog sitting up again as v0.42, both forepaws raised to eye level to hold the paper's top edge, the head bowed about 25 degrees toward the page and turned a little to the viewer, so the face still shows (bowed right over it in v0.26 it was "a monkey, an otter, or a person in a costume"); a "read" expression in round reading glasses.
- `TPDB_CAT44` (the review's item 3): the cat's ears turned 40 degrees about the vertical and taller, so the triangle shows in profile (edge on, the head was a plain ball); the muzzle further forward; the whiskers angled forward as well as out.
- `TPDB_GOAT44` (the review's item 25): the goat's beard a short blunt tuft angled back, so it hangs down when the head is lowered (grazing, it "sticks out as a hard grey wedge").
- `TPDB_NOSE44` (the review's item 16): the dog's nose set into the muzzle, its tongue rooted in the mouth.
- `TPDB_PROP44` (the review's item 1): a prop takes the first colour of its list whose hue is 40 degrees or more from every saturated garment its holder wears: the bag on the woman in yellow's dress, the watering can on the grandmother's teal cardigan, a pink scoop on a pink dress, a yellow balloon over a yellow shirt.
- `TPDB_RUN44` (the review's item 2): running off the ground, the back shin kicked up behind, the front foot just lifted, the hips up and a lean of 16 degrees, no sole under the raised shoe (it read as a lunge).
- `TPDB_SPADE44` (the review's item 6): the sand spade's handle running into a blade twice the size with a pointed foot (a red square apart from a blue handle, "a floating red cross").
- `TPDB_INSPECT44` (the review's item 15): looking into the hose's nozzle with the head level and turned 20 degrees to the viewer, so the puzzled face shows.
- `TPDB_CALL44` (the review's item 13): stuck up on the seesaw and calling, one hand on the handle and the other cupped at a wider open mouth (both hands at the chest, "nervous or praying").
- `TPDB_CONTENT44` (the review's item 18): the "content" face's closed eyes as the happy face's upward arcs, the brows level and a little raised (it read as a wince, "><").

Seven changes are in placement revision 42:
- `templates.READ44`: the reading dog's paper hung from its raised forepaws by the top edge, 1.05 to 1.30 times v0.42's paper as the ground allows, its foot clear of the ground; the dog in the front half of the picture, off the path and at least 400 px from any other dog (the review's item 7: in v0.43 it was small, far back, on the path or beside another dog); and always the tan dog (the white dog's raised paws are too low to hang the paper clear of the ground), so it and the dog by the door, who wants the tan dog too, are never drawn together. **A** without glasses, **G** with them. `READ44T` **T**, made after round 1: the paper tilted 9 degrees about the paws, its far side sagging.
- `templates.LEAD44` (R2, the notes' item 2): the waiting dog's lead in a colour of its own, hanging from its mouth to a loop clear of the ground. Blue in the first build hung against the garden's blue door, so round 1 read green; round 2 yellow, hanging (**B**) or lying on the grass as v0.43's (**C**).
- `templates.GOAT44` (O1, the notes' item 3): the grazing goat in the park only, and never at 135 (in gardens "unusual"; from behind at 135 twice "possibly a sheep").
- `templates.CAT44` (the review's item 4): the stalking cat at least its own length clear of a tree (in front of a dark canopy its face was a blob).
- `templates.BAL44` (the review's item 5): the lost balloon high above the reaching hand on a string at least nine-tenths of the child's height, against open sky, the string's free end curled and clear of everything for 60 px (its end landed on a handlebar, the hedge, between two players).
- `draw.WATER44` (the review's item 8): the upward water a ribbon tapering as it rises, drops breaking off its top third, and never in the street (an even band before the slate shop door, "like a bent tube").
- `draw.WHEEL44` (the review's item 10): the square wheel a rounded-square tyre on thin spokes round a round hub, as the round wheels are drawn, and the bicycle's other wheel round.

Tried and left before the readers: the throw's follow-through (`TPDB_THROW44`, the review's item 14). The arm across the body at shoulder height read as reaching, and swung down across the body as walking with the arms out; neither looked better than v0.43's, which passes. Not drawn this time (the review's other items, kept for later or for the pilot): the buildings' scale, the far eye at 90, the hose's path, the begging dog from behind, the seed sack, the camera's subject, the windy hat's gap, small props, the ducks, kite strings, grey contrast, the thief bird by the reel, speed lines, the planting, the giant fork, the seesaw seat (inset 22 already puts the rider over the plank's last tenth) and the C list.

## Round 1

| Case | What the readers said |
|---|---|
| Reading dog, O (v0.43, lying) | Reading in all three, each with another reading: "or as the dog lying on it / chewing or tearing it" (rd6O_1), "just lying on the paper and sniffing or about to chew or tear it" (rd6O_2), "just sniffing or lying on paper it found" (rd6O_3) |
| Reading dog, A (sitting, no glasses) | Reading in all three ("Its pose and the way it faces the page make it look like reading", rd6A_1), with "holding, grabbing or fetching it" or "carrying the paper it has fetched". The paper "seems to stand upright on its own or float slightly above the grass, held up only by the paw" (rd6A_1); "unclear whether the newspaper is resting on the ground or held up entirely by the dog" (rd6A_3) |
| Reading dog, G (sitting, glasses) | Reading in all three. The glasses: "a dark ring around the dog's eye that could be a pair of glasses (which would fit the 'reading' joke) or ... a large dark eye marking" (rd6G_1), "a dark mark over its eyes that might be glasses" (rd6G_3), not mentioned once. The paper "looks stiff and upright, almost standing on its own beside the dog" (rd6G_2), "stands upright without visible support apart from the dog's paws" (rd6G_3) |
| Waiting dog's lead, green (N) | "The green thing in the dog's mouth could be a garden hose (the dog bringing a hose to help with watering) or a lead ... Its coiled shape and green colour look more like a hose" (gd6N_2). v0.43's red: "holds the end of a red lead in its mouth and seems to be waiting to go for a walk" (gd6O_2) |
| Square wheel (N) | The barrow's "looks boxy or square-ish rather than round, which looks a bit odd" (pk6N_1), where v0.43's was "a square, grille-like frame instead of a round wheel" (pk6O_1); the bicycle's one rounded square "looks wrong or broken. It could be a buckled or squashed wheel" (rd6G_3), where v0.43's two were "clearly drawn as rounded squares, not circles ... a deliberate 'impossible' detail" (rd6O_3) |
| Sand spade | N: "digging with a red spade" (pg6N_1); O: "hard to make out: it looks like a small blue spade with a reddish bit, but it could be a stick or a toy" (pg6O_1) |
| Stuck on the seesaw, calling | N: "her open mouth and raised hand could mean she is calling the man to bounce her or let her down" (pg6N_1); O: "mouth open in a surprised or worried 'o'", and the plank "seems to run across or through his lower legs" (pg6O_1) |
| Upward water | N: "curves upwards and to the right, ending in drops above the flowers instead of falling onto them" (gd6N_2); O read two ways, "(a) It shoots upwards ... (b) It is meant to fall from above" (gd6O_2) |
| Running | Running in both drawings, "arms pumping", speed lines (pg6, pk6, rd6_3) |
| Goat, cat, balloon, props | The goat tethered in all five pictures, its beard unremarked in both drawings; the cat stalking in all five; the loose balloon "just slipped away", its string "in a little curl just above her raised hand" (rd6G_1); the grandmother's "grey watering can", the woman in yellow's "blue shopping bag" |

So after round 1: the reading dog sitting up reads as reading as the lying one does, without "lying on it" or "tearing it", and in glasses it gains a cue two readers saw; but its paper hung square stands up by itself again. The green lead is a hose, and the rounded square wheel is less plainly square than v0.43's. The spade, the seesaw's call and the upward water read better; the running, goat, cat, balloon and props read as well.

## Round 2

Round 2 read four new pictures of the reading dog in glasses with its paper tilted 9 degrees about the paws, its far side sagging (rd7T), and the waiting dog's lead in yellow, hanging (wn7B) or on the ground (wn7C), two of each:
- **The reading dog, tilted:** reading in all four ("holding an open newspaper with both front paws, apparently reading it", rd7T_1), the paper never standing by itself ("the newspaper's lower edge rests just above the ground at the dog's paws"). The glasses: "the dark rings around the dog's eye look like spectacles" (rd7T_1), "could be glasses" (rd7T_2, rd7T_4). Other readings: "grabbed or is playing with a newspaper" (rd7T_1), "picked up or caught the newspaper and is carrying or chewing it" (rd7T_3, "The upright, paper-held-open pose looks more like reading").
- **The lead, yellow and hanging:** "holding a yellow lead in its mouth, as if it wants to go for a walk" (wn7B_1); "it reads as a dog fetching its own lead to ask for a walk" (wn7B_2).
- **The lead, yellow on the ground:** "a dog lead, or possibly a thin yellow hose" (wn7C_1), "a dog lead with a handle loop ... or a thin yellow garden hose" (wn7C_2).

## Taken

- The cast (builder 0.44.0): `TPDB_READ44` A, `TPDB_CAT44` A, `TPDB_GOAT44` A, `TPDB_NOSE44` A, `TPDB_PROP44` A, `TPDB_RUN44` A, `TPDB_SPADE44` A, `TPDB_INSPECT44` A, `TPDB_CALL44` A, `TPDB_CONTENT44` A. `TPDB_THROW44` stays O. The nose and the content face were not in a bench picture and are read in the design tests.
- Revision 42: `templates.READ44` **G** with `READ44T` **T**, `LEAD44` **B** (yellow), `GOAT44` **B**, `CAT44` **B**, `BAL44` **B**, `draw.WATER44` **B**. `draw.WHEEL44` stays O.
