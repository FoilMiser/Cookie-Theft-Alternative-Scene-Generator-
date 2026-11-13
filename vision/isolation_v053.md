# v0.53 isolation bench

v0.53 works the list of `flaws_v052.md`. Sam's brief was "go for v0.53!" and named no part of the drawing, so the list set the work: the square wheel, which failed v0.52's gate (R1), and the woman in purple, a girl to the readers of four pictures in each of the last two screens (O1). Every flagged picture of v0.52 was looked at again at full size before anything was drawn, and the code's own comments were read for each proposal on the list. Two things came of that look before any bench: three proposals had been tried before and are left, and two were measured and are left (the last section).

One bench decided the rest. It reads whole pictures, as v0.52's lessons ask for a fault that is a thing not noticed or a figure taken for someone else: v0.52's own records built again with one change each, and read by fresh readers with the screen's prompt.

## The wheelbarrow's square wheel (`draw.WHEEL53` B; O draws v0.52's)

v0.52's wheel is a dark open square 50 units across at the barrow's front, eight spokes from a square hub, half of it under the fork that carries it. Two readers of the screen's four wheelbarrows did not notice it, and v0.51's readers of the same pictures had named it only among the things they were unsure of. The drawing was arrived at over many releases (a filled square was a crate, a cross of two bars a window, rounded corners a round wheel drawn badly), so its shape is kept and only its size changes:

- **B**: the same wheel 34 units from hub to side for 25, so 68 across. The tub, the handles and the legs are raised by as much, and the barrow stands on the wheel as it did. The tyre is 0.27 of the radius for 0.30 and the spokes 0.10 for 0.085, which at the larger size are both a little heavier in the picture than v0.52's.

The barrow alone places on twelve seeds of twelve in the garden with the old wheel and with the new (`tools/cycle/yield_set.py`). The two drawings side by side are `isolation_v053/trials/wheel_O_B.png`, and cut from v0.52's and v0.53's pictures, `isolation_v053/wheel_v052_v053.png`.

## The woman in purple (`specs.ANA53`; O builds v0.52's)

She was a girl first in 4 of her 25 pictures in v0.52's screen and in 4 of v0.51's, in three poses. The list asked for her ponytail to be tried against a woman's hair. On a sheet of her alone at twice the release's size (`python build_cast.py <dir> person.ana`, then eight views) her hair is not a ponytail: it hangs loose down her back in one narrow fall, which from the side looks like one. Six drawings were tried on that sheet, each a letter of the switch (the sheets are `isolation_v053/trials/ana_O.png` and so on by letter):

| Trial | What it is | On the sheet |
|---|---|---|
| N | Her hair drawn back into a low bun at the nape | From the front, a boy with short hair. Set aside |
| S | Her hair cut to the shoulders and full behind the neck (`people.SHOULDER53`) | Hardly differs from v0.52's at any view. Set aside |
| K | A skirt to the knee for the trousers | Bare legs under a short skirt: younger, not older. Set aside |
| F | A woman's figure: waist 0.84, hips 1.16 and bust 1.5 of the standard figure's | Shows a little, most from the side |
| FL | F, and a skirt to below the knee, as the woman in yellow's dress is | To the bench |
| FC | F, and a cardigan in her purple over a cream top, the trousers kept | To the bench |

## The bench in whole scenes (`isolation_v053/who`)

Nine fresh readers had eight pictures each and the screen's own prompt, 72 pictures in all. The map of which picture is which lay outside the folder until the readings were in (`isolation_v053/who_map.json`).

**The wheel.** Three of v0.52's four wheelbarrows (pictures 11, 18 and 102; the tier-4 garden's did not build again with the larger wheel) in two arms: O as screened, and W built again from the same records with the larger wheel acting at the records' own revision (`templates.WHEEL53_REV`). All three came back with the same templates, the same people and the same places. A reader had two barrows, both of one arm, so that what a reader carries from the first barrow to the second stays inside its arm: four readers had O and five had W.

| Arm | Readings | The wheel square in the description or the inventory | Only in the unsure section | Not named |
|---|---|---|---|---|
| O, v0.52's wheel | 8 | 4 (two readers of four, both their barrows) | 4 (two readers, both theirs) | 0 |
| W, the larger wheel | 10 | 10 (five readers of five) | 0 | 0 |

With v0.52's wheel half the readers wrote a description like "On the far right a grey wheelbarrow sits on the grass." and came to the wheel at the end: "The wheelbarrow wheel looks square/framed rather than round." With the larger wheel every reader has it in the description or in the barrow's own line: "On the left of the lawn stands an empty grey wheelbarrow, but its wheel is drawn as a square, which would not roll."

Two things the count does not show. No reader of either arm missed the wheel altogether, as two of the screen's did, so the bench's first arm shows the fault in a milder form than the screen had it: named late, where the screen had it unnamed. And the larger wheel has a second reading that v0.52's did not get here. Eight of W's ten readings call it the barrow's wheel outright; one reader of two barrows wrote "- Wheelbarrow: grey, bottom right, with a square dark frame at its front." and gave the wheel as one of two readings, and another, who called it the wheel, added: "It could alternatively be read as a crate or grate placed in front of the wheelbarrow, but it sits where the wheel should be." A third offered "a wheel seen at an odd angle".

**Taken: B.** The fault was a wheel not noticed, and the larger wheel is in every reader's description. The second reading goes on the list for v0.54.

**The woman in purple.** Eighteen of v0.52's pictures of her, the four in which the screen's readers called her a girl among them, in three arms: O as screened, FC and FL built again from the same records with her alone built again. All 36 came back with the same templates and cast. A reader had six of them, two of every arm and no picture twice.

| Arm | Readings | A woman first | A girl first |
|---|---|---|---|
| O, v0.52's | 18 | 18 | 0 |
| FC, the figure and a cardigan | 18 | 18 | 0 |
| FL, the figure and a longer skirt | 18 | 18 | 0 |

The count is by the first word for a person in the first inventory line that names her purple, the screen's own rule, each line read. She is a woman in all 54, in v0.52's drawing as in the others: "Left, front: woman in purple top and teal trousers, sweeping leaves with a yellow broom." is one of the screen's four girls, as screened and read again.

So the first arm does not show the fault, and the bench has nothing to choose between the three. The screen says why. v0.52's four girls were written by three readers of thirteen: one of them called her a girl in one of her three pictures, one in two of two, one in her one. The nine other readers who had her, with 19 pictures of her between them, never did (one reader had no picture of her). Nine fresh readers here had none of that habit among them.

**Left: O.** Her drawing stays v0.52's, and with it the whole cast (builder 0.52.0). The two drawings stay behind the switch for a release that finds a bench that shows the fault.

## The jump beside a game of catch (`templates.JUMP53`)

The list asked to keep the jump out of the ball's path. A first rule (the switch at B) kept the jumper's box 150 units to the side of the span from one player to the other, whichever was placed first. It was read in two design tests (`design_tests_v053.md`), the jumper standing just behind the catcher in both, and both readers still offered the jump as a try for the ball. So the two are never planned into one picture (the switch at X: a shared exclusive tag, read when the planner asks, so that revision 48's records keep their plans). The gap stays for a forced set.

What the gap alone cost, the two forced together on twelve seeds with the band left out: in the garden 12 with the rule off and 10 with it on, in the park 3 and 2, in the playground 7 and 6.

## Looked at and left

| From the list | What was found |
|---|---|
| R3, the floating box lower over the lawn with its shadow under it | Revisions 10 and 11 took the box up from there: low, it read as a box resting at the foot of the fence, and its shadow as a shadow with nothing above it. A level box was benched in v0.41 and not taken. Left |
| R4, a piece of the sandwich in the thief bird's beak | That was the drawing until v0.46. v0.47's bench took the bite with the beak's tip in it over the piece in the beak. Left |
| O2, the heavy seesaw's man in front of the plank | Measured as the children were in v0.50: the rise he sits at, 5 units, is within 1.6 units of what the children's measure gives, so his seat is right. The remark is the one v0.32 found in every drawing of him. Left |
| O3, figures over the pond's near edge | The grown duck feeders stand at the bank's front (the pond's ends are kept clear for the cattails), and the two other figures stand as revision 45 lets them, hips below the rim. All four readers say the figure stands on the bank. A rule that took the overlap away would take the park's front left from every figure. Left, and off the list |

## The list

| From `flaws_v052.md` | In v0.53 |
|---|---|
| R1 `square_wheel`, under the gate | The barrow's wheel larger (`WHEEL53` B), chosen in whole pictures |
| R2 `jump` beside a game of catch | Never planned together (`JUMP53` X), after a gap of 150 units read no better |
| R3 `floating_box`, R4 `bird_steals` | Looked at and left: both proposals had been the drawing before |
| R5, R6 | Carried |
| O1 the woman in purple a girl | Two drawings benched in whole scenes; the bench's first arm did not show the fault. Left |
| O2 the seesaw's man, O3 the pond | Measured and left |
| O4, O5, O6 | Carried |
