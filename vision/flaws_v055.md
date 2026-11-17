# v0.55 blind screen: what it found (the work list for v0.56)

This file has two parts. The first is the screen's own list, as v0.55 shipped it. The second, **Quality check after the release**, was added afterwards: it corrects R1 and O2 and fills the list out from three screens read side by side, six fresh reviewers and the records' geometry (`review_v055/`).

The v0.55 screen read the set's 21 pictures and 78 probes with the prompts of v0.54 (`screen_prompts.md`). There were thirteen readers, eight of eight pictures and five of seven, and four scorers of 24 or 25. The legibility gate passed 63 of the 64 templates, as in v0.54 (64 in v0.53, 63 in v0.52). One item of the 1,102 was scored a misread, the first since v0.50, and nothing was redrawn, swapped or read again after the screen (below). Keys, descriptions and scores are in `v055/`.

v0.55's brief was Sam's: the legs of a seated figure (`isolation_v055.md`). The placement rules are revision 49, unchanged; the cast is built again (builder 0.55.0):
- **the lower body of a seated figure is drawn in stiff pieces** (`castlib.people.SEAT55`): the hips as a block that is flat underneath, a thigh and a shin that keep their thickness and end in a dome at the knee, a cuff that rides up, bare legs and a skirt's wrap in the same way; standing figures are v0.54's;
- **the feet are under the knees** (`castlib.actions.SIT55`): on a seat the thigh is level and the shin upright; the reader on the seesaw's low end sits with the legs out and the book held higher;
- four blind benches of pairs chose the new drawing in 36 reviews of 42, and a bench in eighteen whole pictures read both ways by twelve readers found every event read as before and fewer doubts about a sitter's legs (6 readings of 36 for 10);
- the list of `flaws_v054.md` was not worked: R1 to R3 stand as they were.

**Sixty-nine of the 99 pictures are v0.54's to the pixel**, thirteen of the set's 21 and 56 of the 78 probes. The thirty that changed are the thirty that hold a figure on a seat, a swing, a seesaw or a slide, and each of them has v0.54's templates and v0.54's people in v0.54's places: only the sitter is drawn anew. The planner's priors were left at v0.54's so that it would be so (`README.md`). So this screen is, for 69 pictures, a third reading of v0.53's and v0.54's own, and for 30 a reading of the same pictures with the new legs.

## Headline (the 21 pictures of the set)

| | v0.51 (21) | v0.52 (21) | v0.53 (21) | v0.54 (21) | v0.55 (21) |
|---|---|---|---|---|---|
| Things | 0.944 | 0.981 | 0.972 | 0.954 | 0.954 |
| Actions | 0.996 | 1.00 | 1.00 | 1.00 | 1.00 |
| Inferences | 0.985 | 0.955 | 1.00 | 0.984 | 0.953 |
| Contradictions | 1.00 | 0.982 | 0.946 | 0.929 | 0.946 |
| All items | 0.976 | 0.986 | 0.984 | 0.974 | 0.972 |
| Misread items | 0 of 287 | 0 of 287 | 0 of 286 | 0 of 286 | 1 of 286 |
| Readers' remarks per picture (all screened pictures) | 2.59 | 2.46 | 2.62 | 2.71 | 2.44 |
| Oddities per picture, as logged by the scorers | 0.3 (at most 1) | 0.2 (at most 1) | 0.3 (at most 2) | 0.4 (at most 3) | 0.4 (at most 2) |

Ten of the set's 286 items are under full marks: the clouds in four pictures and a tree in one, which their readers left out (21, 39, 78, 89, 92), the two contradiction items of the square-wheeled bicycle in the tier-4 playground (51), a half and a misread, two half marks in the tier-4 street (63), on the thief bird and on the dropped ice cream, and a half mark on the stopped hose of the tier-4 garden (97).

The scorers logged 12 oddities in the set's 21 pictures and 26 in the 78 probes, 0.4 a picture over all 99 (v0.54: 8 and 32). The readers' own remarks are 2.44 a picture for 2.71.

Across all 99 pictures, 1,074 of the 1,102 scored items had full marks (v0.54: 1,072), and one was misread. The 28 under full marks:
- **Sixteen on the clouds and seven on a tree,** all zeros on setting items that a reader left out, from five readers: two left the clouds out of six of their seven pictures (72 to 78, 86 to 92). v0.54 had twenty-six such zeros, from five readers. It is a reader's habit and not a drawing's fault.
- **The square-wheeled bicycle of the tier-4 playground, a half mark and a misread** (51). R1.
- **The thief bird and the dropped ice cream of the tier-4 street, a half mark each** (63). R3.
- **The stopped hose, a half mark** (97). R4.

The scorers gave six, four, nine and nine items under full marks, of 269, 278, 299 and 256.

**The seated figures.** Every template that draws one reads 1.00, as in v0.54: the reader on a bench in four pictures, the drinker in three, the figure that sits on nothing in three, the heavy seesaw in three, the seesaw at play in three, the swing in three and the slide in three. Their 37 items have, each one, the score they had in v0.54's screen. A reader on a bench: "- Man, right front: brown hair, moustache, red shirt, blue trousers; sitting on a bench reading a red book." (29). The figure that sits on nothing: "- The old man appears to be sitting on nothing; there is no chair, stool or bench under him. This looks impossible / unintentionally strange (or a missing chair)." (22).

**What the readers doubted about a sitter.** A line of the unsure section names a sitter's legs, feet or seat in seven of the thirty pictures (1, 7, 13, 17, 27, 46, 71), for four of the same thirty in v0.54's screen (17, 46, 71, 94), each read by another reader. They are of three kinds:
- the man on the seesaw's low end, in two of his three pictures: "- The man seems to sit almost on the grass at the end of the seesaw rather than clearly on the seat; could be read as sitting on the ground holding the end down." (13). R2;
- a sitter's legs in front of a bench, in two pictures: "- The boy's legs come forward off the front of the bench; seated pose looks a little awkward but fine." (46), which v0.54's reader of that picture had too. O3;
- a child's feet off the ground, in three pictures, which is how a child sits: "- The girl's feet do not reach the ground; normal for a child." (1).

No reader names a knee, a thigh, a shin or a seat as strange. The bench in whole pictures, where one reader read both ways, had fewer doubts with the new legs, 6 readings of 36 for 10; the screen, with one reader a picture, has more, 7 for 4. Both are small counts, and both leave the same two things: the low rider's seat, and a bench that is shallower than a sitter's thigh is long.

**A second reading of the pictures that came back, and a first of the pictures that changed.** The 69 pictures that are v0.54's to the pixel hold 717 items. Item for item against v0.54's screen, 690 have the same score, fourteen are higher and thirteen lower. Twenty-six of the 27 are the clouds or a tree; the other is a wheelbarrow's wheel, named in the description where v0.54's reader had it only among the unsure things (42). The 30 pictures that changed hold 385 items: 371 have the same score, eight are higher and six lower. Ten of the 14 are the clouds or a tree. The other four are in the two tier-4 pictures of R1 and R3: the bicycle's notice item up a half (51), its explain item a misread where it was a zero, and the thief bird and the dropped ice cream of the street each down a half (63). None is an item of a seated figure.

**What the full marks rest on.** The scorers listed 85 judgement calls they scored 1 (20, 28, 14 and 23), for v0.54's 82. Not counted, as in v0.54: a fence named by its gate, which is the key's own accepted phrasing; and, listed for the first time by two scorers, eleven marks of a grandparent called an older man or woman, which is what the figure is. The 85 are of two kinds:
- **48 where the target stands beside another reading** (v0.54: 42). By template: the stopped hose and the thief bird five each; the upward water and the dog at the door three each; two each for eleven, the heavy seesaw among them; and one each for ten more. Halved, they take twelve templates under 0.9: `bird_steals` and `jump` (0.80 each), `water_upward` and `wave` (0.833 each), `blocked_hose` and `dog_wants_walk` (0.85 each), and `about_to_trip`, `cat_stalks_bird`, `floating_box`, `seesaw_heavy`, `sweep_fork` and `windy_hat` (0.889 each). 52 of 64 pass (v0.54: 54).
- **37 on a near word or a target partly said** (v0.54: 40). Twenty are a word for a person: the teenager a boy seventeen times, the woman in purple "girl/woman" once, the woman in the yellow dress a girl once and the man in the red shirt a boy once. With these halved as well, 42 of 64 pass (v0.54: 44).

The four scorers differ in how much they list, so the strict counts compare with v0.54's only roughly (`tools/cycle/strict_count.py`).

## What the screen says of the cast

- **The grown figures.** By the first inventory line that names each figure's clothes, the four grown figures of v0.49's count are called by a young name first in 3 of their 81 pictures (v0.54: 4 of 81): the woman in purple in 1 of 25, the woman in the yellow dress in 1 of 21, the man in the red shirt in 1 of 19, the man in green in none of 16. The three: "- Right, near the gate: girl/woman with dark hair, purple shirt, teal trousers, raking leaves." (87), "- Left: girl with dark hair, yellow dress, red shoes; seated pose drinking from a red cup with a straw, no visible seat." (11), and the man walking with a book: "- Boy, centre front: brown hair, red T-shirt, blue jeans. He walks or hurries while reading an open book, and motion lines trail behind him." (67). The same three pictures as in v0.54, by three readers of thirteen. O1.
- **The man in the red shirt seated** is a man in all three of his seated pictures (29, 60, 77), as in v0.54.
- **The marks of age.** The moustache of the man in the red shirt is in his line in 2 of his 19 pictures (v0.54: 5 of 19). The beard of the man in green is in his line in 11 of his 16 (12 of 16). The older man's moustache is in none of his 18.
- **Every animal was named for what it is.** All 19 (template, angle) pairs pass. The four oddities logged of an animal are a goat in a park, a bird a boy runs at, a bird large on a lamp and a puppy lying on a hose that still runs.
- **The teenager is a boy**, in every item the scorers listed. He is one, and the key's word is the scorer's to match.

## The v0.54 list

| v0.54 | In v0.55 |
|---|---|
| R1: `square_wheel` 0.896, under the gate | Not worked. **0.938 with a misread, and under the gate again** (24 items, 8 pictures): the tier-4 playground's bicycle lying on its side to a second reader running, its wheels unnamed a third screen running; the four barrows and the three other bicycles in full. R1 |
| R2: `blocked_hose` 0.975 | Not worked. **0.975** again (20 items, 5 pictures), a half mark and five full marks beside another reading. R4 |
| R3: eight templates of the strict count | Not worked. Each **1.00**; `seesaw_heavy`, `dog_wants_walk`, `sweep_fork` and `water_upward` are under 0.9 on the strict count again. R5 |
| O1: grown figures young first, 4 of 81 | Not worked. **3 of 81**, the same three pictures. O1 |
| O2: figures over the pond's near edge, six pictures | Not worked. Four pictures (5, 18, 64, 79). O2 |
| O3: the heavy seesaw's man | His pose is drawn again with the seated legs. His template reads **1.00**; two readers of his three pictures have him on the ground at the plank's end. R2 |
| O4: a pram over a bench's back; O5: a lamp post alone | No picture |
| O6: a sitter's legs past the bench's front, and other singles | The sitter's feet are under the knees. Two pictures still have the legs in front of the bench (27, 46). O3 |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

Every template was screened in at least three pictures (33 in three, 8 in four, 16 in five, 2 in six, and one each in seven, eight, ten, thirteen and sixteen). 63 of 64 pass. Per angle (`v055/gate_yaw.json`), all 19 (template, angle) pairs pass.

| Template | Mean | Items | Pictures | Verdict |
|---|---|---|---|---|
| `square_wheel` | 0.938, one misread | 24 | 8 | **fail** |
| `bird_steals` | 0.967 | 15 | 5 | pass |
| `blocked_hose` | 0.975 | 20 | 5 | pass |
| `ice_cream_drop` | 0.982 | 28 | 7 | pass |
| the other 60 | 1.00 | | 3 to 16 | pass |

**The failure is one bicycle's, again.** The mean is over the gate's 0.9; the misread is what fails it. The tier-4 playground's bicycle stands in the front right corner of the picture with the most events, and its part of the picture is v0.54's to the pixel: "- Red bicycle, bottom right: lying on its side on the grass." and, among the unsure things, "- The bicycle seems to be lying flat/on its side — could be dropped by the boy pointing at the tree, or just parked oddly." v0.54's reader wrote the same of it, and v0.53's did not name its wheels. v0.54's scorer gave the two items zeros; v0.55's gave a half and a misread. The other seven pictures of the square wheel read in full, a bicycle's too: "- Red bicycle (right, middle): parked, with square wheels." (58).

## After the screen

Nothing was mended, swapped or read again. The count is the first and only one.

## What reads least well (the v0.56 list)

| | Template | v0.55 | What the readers wrote | For v0.56 |
|---|---|---|---|---|
| R1 | `square_wheel` | 0.938 with a misread (24 items, 8 pictures), under the gate | "- Red bicycle, bottom right: lying on its side on the grass." (51) | Three screens and a bench have now read the tier-4 playground's bicycle six times: its wheels are square in the description twice, among the unsure things once, and not named three times, two of them as a bicycle lying on its side. No other bicycle is read so. It is the bicycle's place and stand in that one picture, as `flaws_v054.md` had it: bench the bicycle nearer the middle and standing plainly upright (a stand under it, or a wall or a post it leans on), in that picture, with more than six readers an arm. It is the gate's one failure two releases running and the first row of the list |
| R2 | `seesaw_heavy` | 1.00 (9 items, 3 pictures); 0.889 on the strict count | "- The man's body overlaps the seesaw plank; his legs seem to sit across/in front of the plank rather than clearly astride it, so it is slightly unclear whether he is sitting on the seesaw or on the ground in front of its low end." (7) | New with the new legs, and v0.54's doubt in another form (there he sat "on the seesaw end or on something behind it"). The plank's low end lies on the ground and his seat with it, so a man with his legs out sits on the grass. Of the six pair reviewers who had him, two gave him to v0.54's squat. Bench the plank's end raised a hand's height off the ground under him, or a seat on the plank that shows behind his hips, in the three pictures, read whole |
| R3 | `bird_steals` | 0.967 (15 items, 5 pictures); 0.80 on the strict count | "- The blue bird on the bench could be eating the woman's sandwich without her noticing (she is reading), or simply sitting next to food." (63) | A half mark, and five full marks beside the same other reading, in four pictures of five (27, 38, 46, 63). The bird is small against the sandwich. v0.47 drew the bite and the crumbs; the next thing to try is the bird's size or a piece in its beak, on a bench in whole pictures |
| R4 | `blocked_hose` | 0.975 (20 items, 5 pictures); 0.85 on the strict count | "- The hose: no water is visible coming out; it could be because the dog is standing on it, or she may simply not have turned it on. She is looking at the nozzle as if puzzled." (97) | As v0.54's R2: the paw's place on the hose, on a bench in whole pictures |
| R5 | `jump`, `water_upward`, `wave`, `dog_wants_walk`, `about_to_trip`, `cat_stalks_bird`, `floating_box`, `sweep_fork`, `windy_hat` | 1.00 each; 0.80 to 0.889 on the strict count | "- The dog standing on the hose: it may be blocking the water (bulge in hose under its foot), or it may be an accident of placement; the woman's hose gives no water either way." (22, of the hose) | Each reader gives the target as the likelier reading. Left unless a release has a bench to spare; `water_upward` and `dog_wants_walk` are there a third screen running |

## Unintended oddities

Grade A is a remark in five or more pictures, or one that touches what a figure is; B in three or four; C in one or two.

| | Grade | What the readers wrote | Pictures | For v0.56 |
|---|---|---|---|---|
| O1 | A | Grown figures called young first, 3 of 81: the man in the red shirt a boy as he walks with a book; the woman in purple "girl/woman" raking; the woman in the yellow dress a girl, sitting on nothing with a drink | 11, 67, 87 | The same three pictures as v0.54, each by another reader. As `flaws_v054.md` O1: look at what differs between the walker's two pictures before drawing; count the woman in purple by pose |
| O2 | B | Figures over the pond's near edge: "- The woman's feet seem to stand at or just inside the pond's edge; she may be standing on the bank or slightly overlapping the water." | 5, 18, 64, 79 | Four pictures for six. As v0.54's O2: draw the bank |
| O3 | C | A sitter's legs in front of the bench: "- The woman sits right at the left edge of the picture and partly overlaps the house wall; her legs extend in front of the bench." | 27, 46 | The bench is drawn from the front with a seat a few units deep, and a sitter turned three-quarters has a thigh three times that. Draw the seat deeper (its top seen from above) or seat the figure further back on it, a placement rule, and read it whole |
| O4 | C | Children on the seesaw at play: "- The girl looks small and partly hunched over the handle, so it is hard to see exactly how she is sitting." and feet that come near the ground on the raised end | 17, 71 | Two pictures; v0.54's readers had the feet too. Watch |
| O5 | C | One picture each: a sitter half off a picnic blanket (26); a kneeling planter read as a lunge (31); a hose's bulky joint under the dog (29), a hose behind a flower bed (41) and one that loops up (43); a bird large on a lamp (45); the ball's trail read as a string (52); two pots above the grass (54); a puppy on a hose that runs (57); the roller above the planks and the way the man paints (65); the walker's body and legs facing two ways (67); a bird's branch pasted on (70); a bicycle upright with nobody holding it (78); a man running worried at nothing (81, 84); a ball kicked away from the others (88); a goat in a park (5) | as given | None is in three pictures |
| O6 | C | Notes for the pilot: the setting's clouds and trees are left out by some readers and named by others of the same pictures (23 zeros; 26 in v0.54) | 23 items | None for the drawing. The pilot's scoring should say whether setting items count |

## Placement

Revision 49, as in v0.54. The showcase pass placed the twelve cells of tiers 1 to 3 on their showcase seeds with v0.54's templates. The tier-4 park placed on the v0.43 seed, the street on v0.49's, on its twenty-second step, the playground on v0.53's base, on its seventh step, and the garden is v0.46's set forced on v0.46's seed, all four as in v0.54. The five isomorphs are v0.54's by name. The probes came in four passes: 61, two forced for the begging dog, twelve by angle and three forced for the wheelbarrow, 78 in all, with v0.54's names. All 99 pictures have every figure where v0.54 had it. The calibration moved in six of its 252 numbers, on the two templates whose sitter is measured, and the priors were left at v0.54's (`README.md`).

# Quality check after the release: the v0.56 list filled out

After v0.55 was released Sam asked for a thorough quality check, to fill this list out before v0.56 is planned. Everything above this heading is the list as the screen left it and as v0.55 shipped it. Everything below was added afterwards, on 14 November 2026. It changes no number above; it corrects two rows (R1 and O2), and it adds what a screen's scores cannot show.

## How the check was done

- **Three screens side by side.** The 99 pictures of this screen have the names of v0.53's and v0.54's, so each has been read by three readers who never saw another's words: 297 readings by 39 readers. Ninety-five of the pictures are the same to the pixel from v0.53 to v0.54, and 69 from v0.54 to v0.55. `review_v055/screens_digest.md` sets the three readers' unsure lines, the scorers' oddities and judgement calls and every item under full marks side by side, picture by picture: 874 unsure lines, 108 oddities, 76 items. A fresh analyst who saw no picture and no list counted what recurs (`review_v055/digest_report.md`). Its counts were checked again by keyword on the same file. One sentence of it is wrong: it says three readers where there were 39.
- **Six fresh lookers.** Readers say what they see and seldom what is missing (`RUNBOOK.md`, Lessons, of v0.45). So six reviewers were asked what is wrong with the drawing: one for the set's 21 pictures, three for the 78 probes (26 each, dealt by name), one for the set's 21 grey versions, and one for the cast, all 355 sprites on thirty sheets. Each had its pictures, their records and its brief, was told to read nothing under `vision/`, looked at every event in an enlarged crop and at every picture at 800 x 500. They wrote 88 findings, 7 high, 39 medium and 42 low, and found nothing wrong in 31 of the 99 colour pictures (`review_v055/review_set.md`, `review_p1.md` to `review_p3.md`, `review_grey.md`, `review_lib.md`, each with its brief).
- **The records' own geometry.** Every element's box in the 99 records: what covers what, what the frame cuts, depth against size, figures at the pond and at the picture's edges, the size of each scored thing (`review_v055/geom.py`); and the grey level of each scored element's fill against what is around it (`review_v055/greyaudit.py`).
- **A second look.** Every row below that rests on a reviewer was looked at again in a crop before it was written down, and the grey levels were read again from the pixels.

A row is in the lists below when two independent sources name it: two reviewers of different shares, a reviewer and the readers, or a reviewer and a measurement. What one source alone names is in the last table.

**What is sound.** No scored element is cut by the frame, nothing nearer is drawn behind something farther, and size follows depth in all 99 records. Of the 105 readings of a contradiction over three screens, 93 see it for what it is. Forty-nine of the 64 templates have not been under 1.00 in the last twelve screens. Every reviewer of pictures found the seated figures on their seats, and the cast's reviewer wrote of the new legs: "The seated poses (sit_ice_cream, sit_drink, sit_read) have thighs level, knees bent at the seat edge and shins down, with the lower body correctly drawn."

## What the check changes in the list above

**R1, corrected: it is not the bicycle's place.** The bicycle that fails in the tier-4 playground (51) and the bicycle of the tier-3 playground isomorph (78) are one drawing at one place and one size on the same grass: their boxes are [1090,792,1310,934] and [1124,784,1342,926]. All three readers of 78 saw square wheels. None of the three readers of 51 did: "- The bicycle has no rider; it is upright on a kickstand, slightly odd-looking but plausible." (v0.53), then lying on its side twice. So the row's advice to move it nearer the middle is withdrawn. Two things are left. On grass, how the bicycle stands is doubted in 5 readings of 6, in both pictures: "- The bicycle seems to be standing upright with nobody holding it, near a kickstand-like part." (78); on paving, in none of 6 (58, 63). And 51 holds eight templates where 78 holds five: in the busiest picture a prop that nobody holds is not looked at.

**The wheelbarrow is the weaker square wheel, and it was not on the list.** Counted by reading over three screens, the bicycle's square wheels are seen and called impossible outright in 7 readings of 12, and the wheelbarrow's in 3 of 12: three more call it a slip of the drawing, three offer a grate, a frame or an odd angle, and three name it without calling it wrong. Three reviewers, of all four barrows, say why: "The dark square sits behind the tray, is as tall as the tray, and has a thick dark frame, so it looks like a crate, a box or a window frame behind the barrow rather than its wheel." (`review_set.md`). The scorers gave the barrows full marks.

**O2, corrected: the pond is thirteen pictures, not four.** Over three screens a figure that overlaps the pond's outline is doubted in 23 readings of 13 pictures, by all three readers in 18, 64 and 79: "- The man seems to be walking very close to / in front of the pond edge; his body overlaps the pond visually, but he appears to be on the grass in front of it." (79). The records say no figure's feet are inside the pond's box: 22 figures in 20 pictures overlap it with the body alone. It is how the overlap reads on a pond drawn as a flat oval with no bank.

**Three templates are chronic.** The list has carried each as one release's row. Over the last twelve screens, v0.44 to v0.55:

| Template | Screens under 1.00, of 12 | Fails of the gate | Lowest |
|---|---|---|---|
| `bird_steals` | 7 | none | 0.90 (v0.50) |
| `square_wheel` | 6 | 4 (v0.50, v0.52, v0.54, v0.55) | 0.81 (v0.52) |
| `blocked_hose` | 6 | 1 (v0.46) | 0.89 (v0.46) |
| `lost_balloon` | 5, none since v0.49 | none | 0.93 (v0.48) |
| the other 60 | 3 or fewer; 49 never | | |

**Most of what is wrong costs no mark.** A reader gives the planned reading and another beside it, and the scorer credits the first. Counted by reading over three screens, with what a reviewer found in the drawing:

| Template | Readings with another reading | The other reading | What a reviewer saw |
|---|---|---|---|
| `blocked_hose` | 15 of 15 | the dog only stands beside the hose; the hose is not on; the bulge is a connector | the nozzle is 14 to 20 units across; the paw is beside the bulge (below) |
| `sprinkler_package` | 14 of 15 | the box is just a box put there | nothing marks it as a parcel; in one picture it is already soaked |
| `rain_coming` | 15 of 15 for the gesture, none for the rain | pointing at the birdhouse, the building or a bird (8); pointing for oneself | the arm goes up at about 45 degrees and the eyes look level (two reviewers) |
| `dog_wants_walk` | 10 of 15 | the dog is just carrying the lead, or a toy | the lead is a short strap that ends in a ring (two reviewers, all five pictures) |
| `dog_begs` | 10 of 18 | just sitting up to greet or be noticed | read well by the reviewers |
| `cat_stalks_bird` | 9 of 9 | just walking past | the cat's belly is high; the bird faces the cat |
| `kite_in_tree` | 8 of 12 | flying in front of the tree or behind it | in grey the kite has the leaves' grey |
| `ice_cream_drop` | 8 of 21 | rubbing the eyes, not crying; the dog caused it | the child's hand covers the face |
| `windy_hat` | 7 of 9 | he threw the cap; she is holding the gate | in one picture the reaching hand lies on the gate's corner |
| `bird_steals` | 7 of 15 | the bird just sits next to the sandwich | the bird is 42 units across in the two tier-4 pictures |
| `about_to_trip` | 6 of 9 | will step over the box, or has passed it | the man in green looks ahead and not at his book; the woman who reads walking looks at hers |
| `water_upward` | 8 of 9 offer a hose and put it aside | a hose | the stream is a solid outlined tube (two reviewers) |
| `floating_box` | 9 of 9 offer thrown or falling and put it aside | thrown or falling | the box is drawn tilted; in one picture a raised hand points at it |
| `ladder_nothing` | 9 of 9 offer a support behind it and put it aside | leaning on something behind | the top ends at the hedge line in all three pictures (three reviewers) |

Two of these were not on any list: the kite in the tree, and the parcel in the sprinkler, where 14 readings of 15 doubt that the box matters: "- It is unclear whether the box is a delivered parcel or something else (e.g. a storage box); either way it seems out of place on a lawn being watered." (10, v0.54).

**The grey pictures have faults that the colour pictures have not.** The screens read the colour pictures. Grey is the Rec. 709 luma of the colour (`compose.to_gray`), and five things that colour alone sets apart have nearly the grey of what is behind them (below).

**v0.55's own drawing has one new fault.** The seated skirt (below, C1).

## The v0.56 list, filled out

### The gate and its edge

| | Template | What the check adds | To bench |
|---|---|---|---|
| R1a | `square_wheel`, the bicycle | Not its place (above). On grass its standing is doubted in 5 readings of 6; in the busiest picture the wheels are not looked at, three readers of three | In picture 51, eight readers an arm or more: (a) the bicycle held, its owner standing with a hand on the saddle or pushing it, so that the wheels are part of what somebody does; (b) the bicycle leaning on the tree, the fence or a post, with no stand and no flat shadow. v0.54's larger wheels were a rack and are not tried again |
| R1b | `square_wheel`, the wheelbarrow | A firm sighting in 3 readings of 12 (above). The square is about 95 units across where the round wheel of the plain barrow is about 45, it is dark, and it stands beside the tray: "The square wheel is drawn much larger than the round wheel of the same wheelbarrow in other pictures (about 80 px against about 45 px), filled dark grey with a spoked inner frame, and it sits beside the tray rather than under it, so at reduced size it looks like a black box or a framed grate standing next to the barrow." (`review_p2.md`) | The wheel at the round wheel's size and place, under the tray's nose on its axle, in the tyre's and hub's own colours, so that its shape is the one thing changed. v0.22's bench chose the open square with barrows read alone; this one is read in whole pictures |
| R2 | `seesaw_heavy` | As above, and two things more. The low end has no handle and no seat that shows, where the child's end has a hoop. And the child's hand at her mouth reads two ways in 9 readings of 9: "- The girl's hand at her mouth could be read as calling out, whistling or shouting to the man, or as nervousness, nail-biting or surprise. Her expression is hard to read." (07, v0.54). Every reader still has her stuck | The low end's handle in front of the man and a pad under his seat (`draw.seesaw` has `pad` and `arch`), or the end on a bumper a hand's height off the grass. The child calling with both hands cupped at the mouth, or with one arm stretched down toward him |
| R3 | `bird_steals` | Under 1.00 in 7 screens of 12. The bird is 42 by 38 units in the two tier-4 pictures and 48 to 64 across in the garden probes, the sandwich 58 to 70: "The thief bird is about 42 x 40 px, which is about 21 px wide at 800 x 500, and it sits half hidden behind the bench back next to an equally small sandwich." (`review_set.md`). In grey it is 78 against the bench back's 38. In one garden probe it touches a hose reel of nearly its colour; in the tier-4 street a second pecking bird, being fed, stands in line with it. In the three garden probes the reader sits 8, 16 and 22 units from the picture's left edge | The bird and the sandwich half as large again or twice as large, on the open seat with nothing dark behind; a piece of bread in the beak, or the bird pulling a slice away; no fed bird and no hose reel within a figure's width of the bench; the bench a figure's width in from the edge |
| R4 | `blocked_hose` | 15 readings of 15 give another reading, in all five pictures; in one the bulge is a connector to all three readers: "- It is not completely clear that the dog is pressing the hose flat; the hose has a slightly thicker connector-like bulge right where the dog's paw is, which could be read as a hose joint rather than a kink." (29, v0.53). The nozzle is 14 to 20 units across: "The nozzle is a 20 x 18 px yellow tip held at the grandmother's chin; at 800 x 500 it is about 10 px, and she looks as if she is simply holding the hose up." (`review_set.md`). Nothing shows that the tap is on | The swelling has been drawn in four releases and reads as a fitting. Bench without it: the hose folded flat under the paw, the paw squarely on it; the nozzle twice the size, held out and looked into, with one drop at its tip; water seeping at the reel's tap, to say the tap is on |

### Inferences and contradictions that are read two ways

| | Template | Evidence | To bench or to place |
|---|---|---|---|
| I1 | `sprinkler_package` | 14 readings of 15 (above). In grey the jets are 171 on grass at 168 | A label and tape, so that the box is a parcel; set down on the path by the door or the gate and not in the middle of a lawn; the water falling short of it, since the item is that it is going to get soaked |
| I2 | `dog_wants_walk` | 10 readings of 15; two reviewers of all five pictures: "The strap is about 70 px long, ends in a loop in mid-air, has no clip and no length trailing to the ground, and at 800 x 500 it is a small yellow ring by the dog's chin." (`review_p3.md`). v0.45's reviewer named the same thing, and it was looked at and left (`isolation_v045.md`) | A lead of the collar's colour with a clip, trailing on the step; the dog facing the door with a paw up on it |
| I3 | `kite_in_tree` | 8 readings of 12: "- The kite could be read as flying just in front of the tree rather than caught in it, but it overlaps the canopy and its tail hangs inside the leaves, so it looks stuck." (26). In grey the kite is 104 on leaves at 115 | The string wound round a branch and the kite tilted, a leaf clump over one corner only; a kite that is light in grey |
| I4 | `cat_stalks_bird` | 9 readings of 9, each leaning to stalking; the set's reviewer, three pictures of three: "In the stalk_paw pose the cat stands on fairly straight legs with its hips high and its belly well clear of the ground, so it reads as a cat walking or sneaking, not one crouched flat and ready to pounce." | The crouch lower, belly at the ground; the bird turned away from the cat |
| I5 | `rain_coming` | Nobody doubts the rain. The gesture has a second reading in 15 readings of 15, and two reviewers name the pose, on two figures: "Her arm goes up and to the left at about 45 degrees, the pointing finger is a small pale nub, and her eyes look level to the side; in s23027 her gaze and arm aim at the painter and the freshly painted boards, so she reads as pointing at the painting." (`review_p2.md`) | `point_up` with the arm nearer upright, the head back and the eyes up; and a rule that no birdhouse, building or scored figure stands in the line of the arm |
| I6 | `windy_hat` | 7 readings of 9: "- The cap is just beyond the man's fingertips; it could be read as him having just thrown it or trying to catch it, but the wind lines and his surprised face suggest it blew off." (32, v0.53). In one picture the hand lies on the gate's corner, to a reviewer and to two readers | The hand clear of gate and fence; more of the wind in the picture than its lines (hair, a tree's lean, washing) |
| I7 | `about_to_trip` | 6 readings of 9. The set's reviewer: "In both the walk_read_open and the sit_read pose his head is upright and his eyes look forward over the open book, while the other readers (mei, ben, tomas, ana) look down at their books." It is the head v0.54 raised so that a man with a moustache is a man (`READ54`); the man in the red shirt walking is still a boy to all three readers (67) | The head as v0.54 has it and the eyes turned down to the page; the box nearer the leading foot |
| I8 | `water_upward` | Seen as wrong in 9 readings of 9, and 8 offer a hose first: "- The water from the watering can goes upward in an arc instead of pouring down; it could be read as a fountain-like spray, or as a hose, but as drawn it seems physically wrong for a watering can." (03, v0.53). A reviewer of two pictures of two: "the solid pale tube reads as a hose looped from the can, so the upward water may be missed" | The rising water in the broken streaks and drops of the water that falls (`draw.water_stream`), with no outline round it |
| I9 | `ladder_nothing` | Seen in 9 of 9; a support behind is offered in 9 of 9; three reviewers, the three pictures: "The top of the ladder ends exactly at the skyline of the background hedge and hill, so at 800 x 500 it looks propped against the bushes behind it, which removes the contradiction." (`review_p2.md`) | A placement rule: the ladder's top third against open sky |
| I10 | `floating_box` | Seen in 9 of 9; thrown or falling is offered in 9 of 9. One reviewer of one picture had it thrown by a waving boy whose hand points at it; another of two pictures had it floating at once | The box level; no raised hand within reach of it. One reviewer's finding beyond that: a faint shadow on the grass under it |
| I11 | `pan_watering`, `bucket_hat` | The pan is a pot or a saucepan in 6 readings of 9, still a thing to cook in; one reviewer has a saucepan, another a frying pan. The bucket is taken for a hat or a joke in 3 readings of 9, and has no handle in three pictures of three | A shallow black pan with a long handle; a wire handle on the bucket. Small, and each still reads |

### The cast

| | What | Evidence | To draw |
|---|---|---|---|
| C1 | A seated skirt reads as shorts | New in v0.55. The cast's reviewer, about 17 of the 24 seated or kneeling sprites of the woman in the dress, the grandmother and the girl: "The skirt wraps each thigh separately with a crease between the legs, so from the front it looks like a pair of shorts and the figure's clothes change from pose to pose." v0.55's wrap is weighted to each thigh and its hem follows both; v0.54 drew one hem straight across at the front view. | One sheet over both thighs with one hem, from the front and at three-quarters; read in pairs against v0.55's and v0.54's rows, as the legs were |
| C2 | The feeder's bag is held by no hand | Three reviewers: all ten feeding sprites and the six pictures two of them had. "The bag hangs behind the forearm at waist height, and no hand, strap or arm grips it, so it looks pasted onto the figure." (`review_p3.md`). The feeding hand is a fist in one pose and a pointing finger in the other | The far hand round the bag's rolled top; the feeding hand open, palm down, with crumbs leaving it |
| C3 | `hang_washing`: the near arm starts at the chest | The cast's reviewer, six sprites of six: "Both arms go straight up and forward with the palms pressed flat together like a diver, so the hands hold no peg or cloth and give no sign of reaching to a line." Seen again in the sprite: the grandfather's sleeve rises out of his waistcoat. The template reads 1.00 | The upper arms at the shoulders, the hands apart at head height, pinching a peg or the cloth's corners |
| C4 | The sleeping dog may be awake | 10 readings in five pictures, all three readers of two: "- The puppy could be asleep, or lying down sniffing / chewing something on the grass; its eyes look closed so asleep seems most likely." (02, v0.53). In grey one sleeping dog is 153 on grass at 168 | Curled, chin on the paws, the eyes two closed arcs; no emote marks (Sam's rule) |
| C5 | The paint roller | 14 readings in seven pictures, all three readers of 25, 47 and 65: "- The roller head looks quite small and sits somewhat above the planks, almost at the top rail." (65). A reviewer of four pictures: the roller's cylinder is upright, the tray reads as a dog's water bowl, and the paint is the blue of the house door | The roller's head larger and level, on the boards at the painted part's edge; a ribbed tray with the roller's colour thick in it; a paint colour no door has |
| C6 | Planting, or digging up | 15 readings in seven pictures; the kneeling planter is a lunge to all three readers of 31 | A seedling in the hand and a tray of seedlings beside the bed; the kneel with both knees under the body |
| C7 | The child who dropped the ice cream | The hand covers the face in six pictures of six (the set's reviewer); 6 readings have the child rubbing the eyes; the cone's dark mouth reads as a scoop still in it (two reviewers) | The head down toward the ice cream, the hand at the cheek and off the eyes; an empty, pale cone |
| C8 | The seesaw at play is nearly level | 8 readings in three pictures: "- The tilt of the see-saw is quite small, so it could be read either as the left child being heavier/pushing down, or as the see-saw nearly level and mid-swing." (17); one reviewer | A tilt of about 15 degrees, the low child's feet on the ground |
| C9 | The child on the swing does not hold the ropes | One reviewer, two pictures of two; the hands meet at the chest | A hand round each rope |
| C10 | Walking, or running | 14 readings in seven pictures: the walk's long stride | A shorter stride for the walk, both feet near the ground |
| C11 | Faces | An open mouth that reads as talking, coughing or alarm, 10 readings in four pictures (34, 52, 58, 61). The cast's reviewer: in side view 37 pairs of sprites that differ only in expression differ in fewer than 200 pixels, and a moustache or beard covers the mouth of the three men | Watch; the side view's mouth longer and set in from the jaw |
| C12 | The teenager is a boy of about ten | Two reviewers, and the readers: a boy in 17 of this screen's near words. The key accepts boy (K2) | None for the drawing unless the pilot needs a teenager |

### Placement (a revision 50)

| | What | Evidence | Rule |
|---|---|---|---|
| P1 | Figures over the pond | 23 readings in 13 pictures (above); no feet in the pond | Draw the near bank; a figure that has nothing to do with the pond does not overlap its outline; one that feeds or fishes stands with the feet a clear step below it |
| P2 | Feet at the picture's bottom | 12 figures in eight pictures, eight of them people, stand 4 to 12 units from the bottom edge (58 and 33 at 4), and a shadow is cut by it; one reviewer | No base lower than 970 |
| P3 | The sun is cut by the top edge | In all seven street pictures that have a sun its box runs from 0 to 178; two reviewers | The street's sun 30 units lower |
| P4 | Hoses under things | The sprinkler's hose runs under a flower bed, to all three readers of 41 and a reviewer; a sleeping dog lies on a hose that runs (57), to all three readers and a reviewer, where a dog on a hose is another picture's inference | A hose crosses no bed and no animal but the one that blocks it |
| P5 | A figure in another event's way | The jumper beside a swing, a balloon or the washing, read as reaching for it by all three readers of 46, 73 and 80; a child with an ice cream heading straight at a fed bird (21, all three readers and a reviewer); a pram headed for a rock (83, all three); a duck by a fishing float (56, all three) | A clear figure's width between one event's moving figure and another event's things, in the line it moves or reaches |
| P6 | Things off the path | 15 readings in nine pictures: "- The pram sits on the grass rather than on the path, which is a little unusual but not impossible." (93, v0.54) | A pram on the path; lamp posts and bins at its edge |
| P7 | The thrown ball's trail | It starts at the fingertip: "The short dashed line begins exactly at the thrower's fingertip and ends at the ball, so the ball looks tethered to the hand like a ball on a string or a yo-yo." (`review_set.md`, three pictures of three; a second reviewer; all three readers of 52) | A gap after the hand; short marks behind the ball |
| P8 | The picnic's sitter is half off the blanket | One reviewer, two pictures of two, and a reader of 26 | The sitter in the blanket's middle |
| P9 | What the photographer photographs | 9 readings of 9: "- It is unclear what the photographer is photographing. The camera points right, possibly at the fisherman or the pond, or possibly just the view." (36) | The camera aimed at a figure or an animal of the picture |
| P10 | Singles a rule would catch | The lost balloon a short way above the fence with its string in the rails (20); the dropped ice cream far back and small in one street (15); one duck, small, on the pond's far rim, as a picture's only event (66); the painter standing a long step in front of the fence he paints (65, 97) | As given |

### Grey

Read from the pixels of the grey pictures. G1 to G7 are the grey reviewer's, from the set, and five of them were read again from the pixels (G1 to G4 and G6); G8 is from the audit of all 99.

| | Thing | Its grey | Behind it | Pictures |
|---|---|---|---|---|
| G1 | The dropped ice cream's pink | 167 | grass 168 | the four on grass of seven: "The splat's pink fill (238,145,183) becomes grey 167 and the grass (114,192,90) is grey 168, so on grass the ice cream is only a black outline with a darker 134 rim around a patch the same grey as the lawn, and it reads as a hole or a wet patch, not as ice cream." |
| G2 | The kite in the tree | 104 | leaves 115 | four of four |
| G3 | The sprinkler's water | 171 | grass 168 | every sprinkler; the streaks on the box 172 on 178 |
| G4 | The pond | 155 | grass 168 | every park |
| G5 | The loose balloon | 193 | sky 210 | three of three in the set |
| G6 | The thief bird | 78 | bench back 38 | the tier-4 playground |
| G7 | An ice cream at the mouth | 134 | skin 148, shirt 142 | one picture of two |
| G8 | Paint tin and tray; the wheelbarrow's tray; the parcel; baskets | 159; 159; 178; 159 to 161 | grass 168 | 10 and 5; 4; 5; 6 |

Sam's rule stands: colour first, grey derived. So the mending is in the colours: a darker pink, a kite that is light, water with a white core, a darker pond or ripples on it, a loose balloon of the held ones' colours. And a check in the build that fails a scored element whose largest fill is within about twenty grey levels of what is behind it; `greyaudit.py` is a first draft of it and is too rough to gate on.

### Keys and scoring

| | What | Evidence | To do |
|---|---|---|---|
| K1 | Accepted phrases with a fixed pronoun | `bird_steals` accepts `she doesn't notice the bird`, `the bird is eating her lunch` and `he isn't watching his sandwich` whoever sits on the bench; `about_to_trip` accepts `not looking where he's going` for a woman | The pronoun from the figure |
| K2 | Who-words listed as judgement calls | The teenager's accepted words include boy, and the scorers list it as a near word 17 times of this screen's 37 | A line in the scorer's brief: a who-word the key accepts is not a call. The strict count then says more |
| K3 | The setting's items | Clouds left out in 48 readings of 34 pictures over three screens, a tree in 17 of 16 | O6 above: the pilot's rule |
| K4 | Words the drawing does not carry | The record has the child looking down at the ice cream, and the hand is over the eyes; it has a girl throwing bread to the ducks, and she holds it | With C7; a throwing arm for the girl |

### One source only, and where the sources disagree

- **The cast's reviewer, alone:** `jump_tuck` with straight spread legs reads as cheering on the spot; brooms and rakes held upright beside the feet (16 sprites), where two reviewers of pictures found every grip and sweep to read and all 16 sweeping pictures score 1.00; the grazing goat seen from the side with its head folded away; two women with one face and one hairstyle; skin showing through a dress in two sprites. Its finding that cats are dog-sized and birds duck-sized does not carry: the scenes scale each kind (cats about 104 units tall, the brown dog 142), though a perched bird is drawn large on purpose and one reader remarked on it.
- **One reviewer each:** a dark cloud resting on a roof like smoke; bread on the pond that reads as pebbles; a spade beside a mirrored hand; jeans hung at a slant; paw prints pointing up the picture; a goat's beard like a beak and its tuft of grass as black spikes; motion lines across a runner's back; a walker's foot on a flower bed's edge; the plain watering can half a bucket.
- **Disagreement:** the frying pan is plain to the set's reviewer in two pictures and a saucepan to another in a third; the floating box floats at once to one and is thrown to another, in different pictures.
- **Readers' habits, not the drawing's:** why somebody runs or jumps, whose the dog is, where a carried box is going, an empty garden. They ask for a story the events do not need.

## An order of work for v0.56

This is more than one release's work. One order that keeps each change read blind before it goes into scenes:

1. **The gate's three, on benches in whole pictures:** R1a and R1b, R3, R4, and R2 with them. Eight readers an arm or more for R1a, since its failure is one picture's.
2. **One cast build (0.56.0)** with what the cast owes: C1 first, since it is v0.55's own; C2, C3 and `point_up` (I5); the stalking cat (I4) and the sleeping dog (C4); the child with the cone (C7); the eyes of the man who reads walking (I7); the swing's hands (C9). Each in pairs against v0.55's row before it is built into scenes.
3. **Drawn props and marks in the scene:** the lead (I2), the parcel (I1), the kite (I3), the rising water (I8), the roller and tray (C5), the ball's trail (P7), the seesaw's tilt (C8).
4. **Placement revision 50:** P1 to P6, P8 to P10, and the ladder's top (I9), with design tests.
5. **Colours for grey** (G1 to G5, G8), and the grey check.
6. **Keys and the scorer's brief** (K1, K2, K4).

A revision 50 and a new cast give other pictures on every seed, so three things follow. The three priors that v0.55 left at v0.54's are taken with the new calibration. The comparison with this screen is by template and no longer by picture: the pictures that were the same to the pixel for three screens are gone. And the square wheel's bench should hold its picture still while the rest moves, or its result cannot be told from the picture's.

If v0.56 is to be one thing again, as v0.55 was, the first cut is step 1 with C1.
