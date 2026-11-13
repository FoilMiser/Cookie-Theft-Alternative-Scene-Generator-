# v0.52 isolation bench

The brief for v0.52 was Sam's: "Go for v0.52 and fix up upper arms, shoulders, and sleeves!" The list beside it is `flaws_v051.md`. This file has four parts: the study of v0.51's drawing, the new drawing and the three blind benches that judged it, the bench in whole scenes, and what of the list was looked at.

## The study of v0.51's arms, shoulders and sleeves

All ten people were rendered from v0.51's cast at 800 px per metre, twice the release's size: standing at five angles, and two of them in twenty-five poses that lift, bend or reach an arm, at two angles each. What the sheets show:

- **A tee's sleeve was a cap.** It ended above the armpit in the rounded end that every chain of the body's hull has, and that end is narrower than the arm it holds. The bare arm is a part that draws no line where it passes into another (v0.39), so the sleeve had no hem: cloth and skin met along a ragged edge with nothing drawn, and the arm stepped out wider under the cap.
- **The sleeve stayed behind.** Raised, the arm went up bare from a stub of cloth at the armpit.
- **A long sleeve was one thick tube** from a round shoulder to a rounded end at the wrist, on the hooded top, the cardigan and the shirt under the waistcoat alike.
- **Under the safety vest** the tee's cap was a slate pad on the shoulder.

## The new drawing (`TPDB_SLEEVE52` B; O builds v0.51's)

The sleeve is cloth round the arm (`castlib/people.py`, `core.open_branch`).

- **A tee's sleeve** runs 0.44 of the way from the shoulder to the elbow. It is as wide as the figure's own arm and four millimetres more, and tapers a little to its hem. The hem is cut straight across the arm and left open; a lid just inside the opening draws the line where the arm comes out, as the seated skirt's lid has since v0.47. The sleeve is carried by the upper arm, so it goes up with a raised arm.
- **A long sleeve** has a node on the upper arm and tapers from the shoulder to an open cuff a little above the wrist. The forearm begins well up inside it and comes out through the cuff's lid.
- **The shoulder's ball** is where v0.51 had it (below).

Seven trials were built, each on two to ten figures in under a minute a figure, and looked at on sheets before the next (`tpdb_work/v052/try.sh`). Three went to reviewers.

| Trial | What it is |
|---|---|
| B4 | The tee's sleeve 0.58 of the way to the elbow, one width on every arm (a man's); the long sleeve thinner than v0.51's, 0.044 of the limb's scale at the elbow and 0.036 at the cuff |
| B6 | The tee's sleeve 0.50 of the way, as wide as the wearer's own arm and tapering; a node on the long sleeve's upper arm; the hem's ring drawn in a twentieth |
| B7, the release's | The tee's sleeve 0.44 of the way; the long sleeve as wide as the garment on anyone, 0.051, 0.047 and 0.040 from the upper arm to the cuff |

**A broken hull.** The body's hull is built by Blender's Skin modifier, and at the node where the neck, the chest and the two shoulders meet it is fragile. With the shoulder's ball scaled to the arm's width, the woman in purple, alone of five figures, was drawn with a plate of cloth through her chest: her hull had 54 vertices for 46. Moving the ball a centimetre outward broke her again and changed the count of three other figures. The ball therefore keeps v0.51's place and size. `TPDB_HULLCHECK=1` prints each hull's vertex count at build time, and a count that differs from the last build's is looked at on a sheet before anything else. In the release's cast the counts are 46 for the five grown figures in a tee, 50 for the two children, 78 for the two older figures and 88 for the teenager, and every figure was looked at standing at four angles.

## The blind benches: pairs

Each sheet shows four figures drawn two ways, row a above and row b below, the upper part large and the whole figure under it at the size it has in a picture (`tools/cycle/fig_pairs.py`). A fresh reviewer has one sheet, is told only that the upper arms, the shoulders and the sleeves differ, says for each figure which row draws them better, lists each row's faults and chooses a row. Every set of four is made twice, v0.51's drawing above and below, so that a row's place cancels. The map of which row is which lies outside the folder a reviewer may see. The six sets: a man standing from the front, turned, from the side, and a woman from behind; four more standing figures in a tee; four with an arm raised; four at work with the arms held out; four standing in long sleeves or a vest; and four acting in long sleeves.

| Round | Against v0.51 | Reviewers | Chose the new drawing | Figures to the new, to v0.51, to neither |
|---|---|---|---|---|
| 1 (`isolation_v052/arms1`) | B4 | 12 | 10 | 34, 9, 5 |
| 2 (`arms2`) | B6 | 12 | 10 | 35, 9, 4 |
| 3 (`arms3`), three sets | B7 | 6 | 4 | 13, 7, 4 |

By set and order, over the rounds each set was in:

| Set | v0.51 above | v0.51 below |
|---|---|---|
| The man standing, three views, and the woman from behind (3 rounds) | new, new, new | new, new, new |
| Four more standing in a tee (2) | new, new | new, new |
| Four at work with the arms out (2) | new, new | new, new |
| Four standing in long sleeves or a vest (2) | new, new | new, new |
| Four with an arm raised (3) | new, new, new | v0.51, v0.51, v0.51 |
| Four acting in long sleeves (3) | new, new, new | v0.51, v0.51, v0.51 |

**What the benches say.** For standing figures and for figures at work the new drawing was chosen in both orders in every round. For raised arms and for long sleeves in action the reviewer chose the row drawn below, in three rounds of three: there the two drawings are a toss-up, and a row's place decides. (Row b was chosen by 8 reviewers of 12, 8 of 12 and 5 of 6.) Two reviewers of one set in round 3 show it: each chose row b, and each gave the same reason for opposite drawings. With the new drawing below: "Row b gives the upper arms a wider root where they meet the body, so the raised and reaching arms grow out of the shoulder rather than out of a narrow joint." With v0.51's below: "In a both arms look thin, like sticks, next to the bulky hoodie."

**Of v0.51's drawing**, from reviewers who did not know which row it was:
- the cap: "the puffed caps sit on the arm like small pads"; "the sleeve is a round bump with no hem"
- the side view: "The arm's rounded top sits flat on the shirt like a sticker."
- the raised arm: "the raised arm comes almost straight out of the body like a tank top"
- the long sleeves: "sleeves are uniformly inflated, sausage-like tubes"; "it reads as a puffed costume sleeve"; "both shoulders bump up above the line of the chest, like pads or a shrug"

**Of the trials**, and what each remark changed:
- B4's sleeves were one width on every arm and stood off the slimmer ones: "the sleeves flare out like wings, much wider than the arms". B6 made the sleeve as wide as its wearer's arm.
- B6's sleeve on a raised arm: "a long tube that climbs beside the chin". B7's is shorter. The remark was made again of B7, by the reviewer who had v0.51's drawing below: "the sleeve on the raised arm is a long thin tube stretched along the upper arm".
- B6's long sleeves, as wide as a slim arm on the older woman: "The raised arm looks like a stick". B7's are as wide as the garment on anyone.

**The choice: B7.** It was chosen in both orders wherever a figure stands or works, it draws a hem on every sleeve, and where it is not chosen in both orders v0.51's is not either. A sheet of the two drawings went to Sam before the release's cast was built (`isolation_v052/arms_v051_v052.png`), with B7 named as the one the release goes ahead with.

**What stays open**, named of B7 in round 3 and not drawn again: the tee's sleeve on a raised arm is still a tube to some; the shoulders are "over-broad" on the woman from behind to one reviewer who chose the new drawing; and in the side view the top of the sleeve has no line over the shoulder.

## The bench in whole scenes (`isolation_v052/who`)

A cast that changes what every figure looks like is read in whole scenes too (v0.50), for one question a pair of cut-outs cannot answer: is a grown figure still read as grown. Eighteen of v0.51's screened pictures were built again from their own records with two trial casts: ten that hold a grown figure sweeping, the two in which a grown figure was called young for another pose, and six more with two or more grown figures (`tools/cycle/who_build.py`). All eighteen came back with the same templates and the same people in each cast. Three arms: O, v0.51's pictures as screened; B, the new sleeves; S, the new sleeves and an upright sweeper (`TPDB_SWEEP52` B: the trunk bent four degrees for ten, the head six for eighteen). Nine fresh readers had six pictures each, two of every arm and no picture twice, with the screen's own prompt (`tools/cycle/age_scenes.py`).

| Arm | Grown figures called young first | The woman in purple | The man in the red shirt | The sweeper, ten pictures |
|---|---|---|---|---|
| O, v0.51 | 4 of 35 | 3 of 11 | 1 of 7 | grown in 9 |
| B, the new sleeves | 3 of 35 | 2 of 11 | 1 of 7 | grown in 10 |
| S, and the upright sweeper | 1 of 35 | 0 of 11 | 1 of 7 | grown in 10 |

- **The new sleeves do not make a grown figure young.** 3 of 35 and 1 of 35, for 4 of 35. The eight pictures of arm S that hold no sweeper are arm B's own files, read by other readers: the woman in purple walking with an ice cream and pointing at the storm is a girl in B and a woman in S, in the same two pictures. That is the size of a reader's part in these counts.
- **The upright sweeper was not taken.** `flaws_v051.md` (O1) had the sweeper's bent pose as what makes the man in the red shirt a boy. Here the sweeper is grown in nine pictures of ten as screened, and in ten of ten in each trial cast, upright or bent. The bench shows the fault once in ten and has nothing to choose between the poses, so v0.51's stays.
- **The man in the red shirt reading on the bench is a boy in all three arms**: "Right, front: boy in red shirt and blue jeans; sitting on a bench reading a red book." It is the pose, seated and small over a book, and it goes on the list.
- **No reader remarked on a sleeve, a shoulder or an arm as drawn**, in any of the 54 descriptions' unsure sections: at a picture's size the change is one a reader does not name. It is a change of how the figures look, which is what the brief asked for.

## The list

Of `flaws_v051.md`, this release drew nothing but the cast, and the placement rules are revision 48's, unchanged.

- **O1, the sweeper**: benched in whole scenes and left (above).
- **R2, the walker's cone**: looked at large, in profile. The scoop is at the mouth already, as the standing eater's is; nothing to draw.
- **R1, R3 to R6, O2 to O6**: not worked. They are scene drawing and placement, and stand for v0.53.
