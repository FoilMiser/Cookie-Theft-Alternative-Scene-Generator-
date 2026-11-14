# v0.55 isolation bench

The brief for v0.55 was Sam's: "go for v0.55 now, and fix up how the legs of the characters work when they are sitting like this:", with v0.54's sheet of the man in the red shirt seated at two angles and squatting on the seesaw's low end (`isolation_v054/trials/read_O_B.png`). The list beside it is `flaws_v054.md`. This file has four parts: the study of v0.54's seated figures, the new drawing and the four blind benches of pairs that judged it, the bench in whole scenes, and what of the list was looked at.

## The study of v0.54's seated figures

All ten people were rendered from v0.54's cast at 800 px per metre, twice the release's size, in eight seated views each: reading on a seat from the front, turned and from the side, sitting from the side, eating at three-quarters, reading on the seesaw's low end, on a swing from the front, and stuck on the seesaw's high end. What the sheets show:

- **A seated leg had no knee.** The trousers are one hull with three rings to a leg, at the hip, the knee and the cuff, and the knee's ring goes half with the thigh and half with the shin. Bent a right angle, a ring carried that way shrinks to seven-tenths of its width and the hull between the rings curves through the bend: the leg was a hose that thinned to its knee. A bare leg had the same ring at its knee.
- **The seat was a sack.** Where the two legs leave the hips the hull is stretched between rings that turn with a thigh and rings that stay with the hips, and it hung under the thigh, rounded, lower than the thigh's own underside. Nothing in the figure was flat where it sits.
- **The feet were set ahead of the knees.** On a seat a grown figure's feet were 32 cm ahead of the hips with a thigh of 30 cm, a child's 26 cm ahead with a thigh of 22 cm. The shins sloped forward, a child's by twenty degrees with the thigh sloping down to the knee, and in a picture the thighs ran off the bench's front edge with the feet far in front of it.
- **On the seesaw's low end** the hips are 20 cm off the ground and the feet were 19 cm ahead of them: the thigh rose steeply into a knee that the hull drew thin, under the forearm.

Thirty-three of v0.54's 99 screened pictures hold a seated figure, thirty of them on a seat, a swing, a seesaw or a slide.

## The new drawing (`TPDB_SEAT55` B and `TPDB_SIT55` B; O builds v0.54's)

**The lower body of a seated figure is drawn in stiff pieces** (`castlib/people.py`, `build_seat55`; `core.lathe`). In the seated postures (`build_cast.SEATED55`: on a seat, a swing, the seesaw and the slide) the standing trousers, skirt and bare legs are hidden and another set of objects is shown, each carried whole by one bone:

- **the hips as a block**, a lathe down the trunk's own line. Its rings at the waist and the hips are the standing trousers' own, a little less deep, so a top's hem lies on it as it does standing and the line between top and trousers is drawn as it is standing. Below, its wall is rounded into a flat underside as far under the hip joints as a thigh is thick;
- **a thigh** from the hip joint to the knee, and **a shin** from the knee to the cuff, as thick at the knee and the cuff as the standing trouser leg. Each stops six-tenths of the knee's radius short of the joint and ends there in a dome: the two domes are the knee, a rounded corner at any bend. The round end of the thigh at the hip lies inside the block whichever way the thigh points;
- **a cuff that rides up**: a seated trouser leg ends a centimetre above the ankle joint, where the standing one hangs 3.4 cm below it over the shoe, so the shoe shows whole;
- **bare legs** in the same way, a thigh from the hip joint and a shin with its calf, under a short sleeve of the shorts that is open at its hem, or under a skirt's wrap of the two thighs, open at its hem, each side of which goes with its own thigh;
- none draws a line where it passes into another: they are one cloth, or one leg.

**The feet are under the knees** (`castlib/actions.py`, `SIT55`). On a seat the thigh is level and the shin upright; the far foot is 4.5 cm ahead of its knee and the near one 1 cm, so a side view shows both shins and a three-quarter view shows them apart. The reader on the seesaw's low end has the feet 34 cm ahead and holds the book 10 cm higher, the knee showing under the forearm. A slider's feet are 0.95 of the way down the chute that the legs reach.

**Standing figures are v0.54's.** The standing objects are not touched: twelve variants that are not seated, drawn at random from the library's 249, render to the pixel alike from the trial cast and from v0.54's. The shirt's hull has v0.54's vertex counts in every figure (46 for the five grown figures in a tee, 50 for the two children, 78 for the two older figures, 88 for the teenager; `TPDB_HULLCHECK=1`). Sitting on the ground, with the legs out straight, is v0.54's drawing: it has no bent knee and no seat to rest on.

Each trial was built on two to ten figures in about a minute a figure and looked at on sheets before the next (`tpdb_work/v055/try.sh`). Four went to reviewers.

| Trial | What it is |
|---|---|
| B1 | The seat is the standing figure's waist piece with its rump, and under it a roll across the two hip joints; the thigh 8.0 cm thick at the hip; the near foot ahead; the low reader's feet 36 cm ahead |
| B2 | No rump, and the roll no further back than the back; the thigh 7.2 cm; the knee's domes 0.38 of its radius short of the joint; the far foot ahead; the low reader's feet 30 cm ahead and the book 7 cm higher |
| B4 | The seat is the hips as a block, which draws the hem's line; the knee's domes 0.50 short; the low reader's feet 34 cm ahead and the book 10 cm higher |
| B5 | A trouser's knee and shin as thick as standing (B2 to B4 had them thinner); the knee's domes 0.60 short; a slider's feet 0.985 of the legs' reach |
| B6, the release's | The seated cuff rides up; a slider's feet 0.95 of the reach. Not put to a round of pairs: read in whole scenes (below) |

**Two seats that failed between rounds.** B2's roll left a strip of the waist piece showing under the hem of a child's tee, with the roll's own line beneath it. A roll made taller, up to the hem, lay at the hem's own lid and the hem came out ragged; a waist piece made narrower left the hem with no line under it at all. The block is what the standing figure has under a hem, a wall that the hem lies on, and it was the third seat tried.

## The blind benches: pairs

Each sheet shows four seated figures drawn two ways, row a above and row b below, each figure whole and large and under it at the size it has in a picture (`tools/cycle/fig_pairs.py`). A fresh reviewer has one sheet, is told only that the lower body differs and that the seat itself is not drawn, says for each figure which row draws its seated lower body better, lists each row's faults and chooses a row. Every set of four is made twice, v0.54's drawing above and below, so that a row's place cancels. The map of which row is which lies outside the folder a reviewer may see. The six sets: four figures in trousers on a seat at three-quarters; four with bare legs, in a dress, a skirt or shorts, the same; four in trousers from the side; four with bare legs from the side; two men reading on the seesaw's low end and two children on its high end; and two children on a swing from the front and two on a slide from the side.

| Round | Against v0.54 | Reviewers | Chose the new drawing | Figures to the new, to v0.54, to neither |
|---|---|---|---|---|
| 1 (`isolation_v055/legs1`) | B1 | 12 | 12 | 40, 5, 3 |
| 2 (`legs2`) | B2 | 12 | 10 | 40, 5, 3 |
| 3 (`legs3`) | B4 | 12 | 10 | 41, 6, 1 |
| 4 (`legs4`), three sets | B5 | 6 | 4 | 17, 6, 1 |

By set and order, over the rounds each set was in:

| Set | v0.54 above | v0.54 below |
|---|---|---|
| Trousers from the side (4 rounds) | new, new, new, new | new, new, new, new |
| Bare legs from the side (3) | new, new, new | new, new, new |
| Bare legs at three-quarters (3) | new, new, new | new, new, new |
| The seesaw (3) | new, new, new | new, v0.54, new |
| Trousers at three-quarters (4) | new, new, new, new | new, new, v0.54, v0.54 |
| The swing and the slide (4) | new, new, new, new | new, v0.54, v0.54, v0.54 |

**What the benches say.** A figure on a seat seen from the side, in trousers or with bare legs, and one with bare legs at three-quarters, was given to the new drawing in both orders in every round, twenty reviewers of twenty. The seesaw's riders went to it by five reviewers of six. The swing and the slide went to the row drawn below in three rounds of four: there the two drawings are a toss-up. Trousers at three-quarters went to the new drawing in both orders in the first two rounds and to the row below in the last two. (Row b was chosen by 6 reviewers of 12, 8 of 12, 8 of 12 and 5 of 6.)

**Of v0.54's drawing**, from reviewers who did not know which row it was:
- the thigh: "- All four: the thigh slopes clearly downward from hip to knee, so the knee sits well below the hip and the pose reads as perching, leaning, or sliding off the edge."
- the seat: "- All four figures: the seat sags below the line of the thigh, as a rounded pouch, with no flat underside, so nothing suggests a seat surface."; "- All four: the seat hangs below the line of the thighs as a rounded U-shape, so the hip sits lower than it should and the figure looks like it is sinking into a hammock, not sitting on a seat."
- the knee: "- All four: the legs are soft, uniform tubes with weak knee definition. At the small size the knees almost vanish and the legs look rubbery."; "- All four: the knee is a soft rounded bend with no clear corner, so thigh and shin blur into one curve."

**Of the new drawing**, the reason most reviewers gave: "It reads clearly as sitting at both sizes, with a level lap, a clear knee and upright shins."

**The faults the reviewers named in the new drawing, and what each round did with them:**

| Round | Named | Done |
|---|---|---|
| 1 | The seat behind the back, by nine reviewers: "- All four: the seat is drawn as a rounded bulge that sticks out behind the back line of the torso, a bit like a cushion or padding; it is largest on the older man and the bearded man." | No rump, the seat no further back than the back (B2) |
| 1 | "- All four: the top line of the thigh is almost dead flat and the knee is a hard square corner, which looks stiff and blocky." | The knee's two domes set short of the joint, which rounds the corner off (B2, and further in B4 and B5) |
| 1 | "- All four: the lower legs are long, rigid columns, and the near and far shin nearly overlap, so each pair of legs reads as one thick block with a seam line down the middle." | The far foot ahead, not the near one: at three-quarters the two shins then stand apart (B2) |
| 1 | On the seesaw's low end: "- Bearded man: the knee is hidden behind the hands and book, so thigh and shin merge into one long straight diagonal." | The book held higher and the feet set so that the knee shows under the forearm (B2, B4) |
| 2 | Under a child's tee, by five reviewers: "- Child: a darker orange band shows between the shirt and the shorts, which looks like a separate strip rather than part of the shorts; the thighs are thick for a child." | The hips as a block (B4) |
| 3 | "- All four: the shins are very long compared with the thighs and torso, so every figure looks like it sits on a high bar stool. This is worst for the teenager and the woman." | A trouser's knee and shin as thick as standing (B5); the cuff rides up and the shoe shows whole (B6) |
| 3 | The slider, bent as v0.54 posed it: "- Child on slide (side): the seat is a sharp right-angle corner with a flat bottom. The thighs are perfectly level and long, then the shins drop steeply, like sitting on a chair edge rather than a slope. The shorts are a stiff box. The far leg is only a thin parallel line along the near shin." | The feet further down the chute (B5) |
| 4 | The slider again, all but straight: "- Child on slide, side: the thigh is long and almost level, and the knee bend is so small that the leg looks nearly straight and stiff." | A bend between the two (B6) |

**What stands at the end.** The grown figures' thigh is 30 cm and their shin 37 (v0.27 shortened the thigh and kept the shin, so that a sitter's feet reach the ground). With the thigh level and the shin upright that shows, most of all at three-quarters, where the thigh is foreshortened: the two reviewers who chose v0.54's trousers there in rounds 3 and 4 both wrote of long shins under a short thigh, and both wrote of v0.54's row that its thighs slope down and its figures look perched or slipping. The swing from the front shows no thigh in either drawing.

## The bench in whole scenes

A drawing judged as a drawing is not yet a picture that reads. Thirty of v0.54's pictures with a seated figure were built again from their own records with the release's cast (`tools/cycle/bench_build.py`): all thirty came back with the same templates, the same cast and no element moved by more than 12 units. Eighteen of them went to twelve fresh readers with the screen's own prompt, six pictures each, three as v0.54 screened them and three with the new cast and no picture twice, so that every picture was read by two readers each way (`bench_prepare.py`, `bench_tally.py`; the pictures and the 72 descriptions are in `isolation_v055/bench`, the map in `isolation_v055/bench_map.json`). The eighteen: three readers on a bench, three whose sandwich a bird takes, four eating or drinking on a bench, two sitting on nothing, two heavy seesaws, two seesaws at play and two swings.

| | v0.54's pictures | v0.55's cast |
|---|---|---|
| Readings in which the figure sits (of 36) | 36 | 36 |
| A reader on a bench, reading (of 12) | 12 | 12 |
| Eating or drinking on a bench (of 8) | 8 | 8 |
| Sitting on nothing, said so (of 4) | 4 | 4 |
| The heavy seesaw's child up in the air (of 4) | 4 | 4 |
| Readings with a doubt about a sitter's legs, feet or seat (of 36) | 10 | 6 |

Every event is read in both arms. What changes is the doubts. Of v0.54's pictures: "- The woman's legs go in front of the bench seat edge so she seems to sit on the very front of it; nothing clearly wrong though."; "- The man's legs and feet look a bit tangled with the seesaw plank, and it is hard to tell whether he is sitting on it or in front of it." Of the new cast's, the doubts that remain are of the same two pictures: "- The bench is very short and the woman sits at one end. Her legs look slightly in front of the bench rather than on it, a minor drawing quirk."; "- The man is sitting on the end of the seesaw, which is resting on the ground. He looks more like he is sitting on the ground than on a seat, but either reading works." One of the six is a reading of the event and not a doubt about the drawing: "- The man's feet are on the ground while sitting on the seesaw, so he could be holding it down deliberately or simply not noticing."

The figure that sits on nothing is read as sitting on a chair that is missing: "- The woman in yellow is drawn sitting but there is nothing under her: she appears to be sitting on thin air. This could be intended as sitting on the grass, but her knees are bent at chair height and her feet are on the ground, so it looks like a missing chair." The woman in the yellow dress in that picture is a woman to both readers of the new cast and a girl to both readers of v0.54's picture, as she was to v0.54's screen reader; that is two readers each way, and the screen counts her.

## What of the list was looked at

| `flaws_v054.md` | In v0.55 |
|---|---|
| R1 `square_wheel`, R2 `blocked_hose`, R3 the eight of the strict count | Not worked: the release is the seated legs |
| O3 the heavy seesaw's man | His pose is drawn again with the seated legs; in the whole-scene bench two readers of four have a doubt about where he sits in v0.54's pictures and one of four with the new cast |
| O6 a sitter's legs past the bench's front | The feet are under the knees: the thighs lie on the bench and the shins stand in front of it. In the picture where both of v0.54's readers had a sitter at the very front of her bench, one reader of two still has her legs in front of it |
| O1, O2, O4, O5, O7 | Not worked |
