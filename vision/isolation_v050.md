# v0.50 isolation bench

The brief for v0.50 was Sam's "go for v0.50!", with nothing in the pictures named, so the work is the list of `flaws_v049.md`: the lost balloon (R1), the stopped hose (R2), the game of catch (R3), the dogs (R4), the heavy seesaw's call (R5), and the oddities O1 to O8, of which two had grade A: grown figures read as children (O1) and riders above their seat (O2). This file is the bench: what was tried on its own, what blind readers wrote of it, and what was taken. The whole scenes are in `design_tests_v050.md`.

Every reader was a fresh one that saw only its pictures. Each change is behind a switch whose "O" is v0.49's drawing (`TPDB_<NAME>50` in the cast, `templates.<NAME>50` in the scene), and every old and new drawing was read on the same seeds.

| | Tried | Taken |
|---|---|---|
| O1 grown figures read young | marks of age, smaller heads, both (`TPDB_AGE50`) | **both** |
| O2 the seesaw's riders | seated by their own measured underside; then with the handle as a grab bar (`SEAT50`) | **the second** |
| O2 the slider | three other places for the slider (`SLIDE50`) | none: v0.49's |
| R1 the lost balloon | its string's end by the hand; a head's height above it (`LOST50`) | **the second** |
| R2 the stopped hose | no swelling before the paw (`HOSE50`) | none: v0.49's |
| O4 the goat's stake | taller, the rope round its upper part (`STAKE50`) | **taken**, the readings alike |
| O5 a held balloon's string | a loose S (`TPDB_STRING50`) | **taken** |
| O3 the painter's roller | a dark metal pole (`TPDB_ROLLER50`) | **taken** |

## Grown figures read as children: the age bench in whole scenes (O1)

In v0.49's screen the four grown figures without grey hair (the woman in purple, the woman in the yellow dress, the man in the red shirt, the man in green) were called a girl or a boy first in 20 of their 89 pictures. v0.49 had built a bench for it, strips of four small figures cut out and read alone, and that bench could not see the fault: whatever the cast, one figure of fourteen was called young. The readers call a figure young in a scene, where there are children and things to do, and not on a strip. So this bench reads whole scenes.

**Method** (`tools/cycle/age_scenes.py`). Thirty-two of v0.49's own screened pictures were picked: every one with the woman in purple whose record took at most two tries (19), and 13 more with the woman in yellow or the man in green. Each was built again from its record with three other casts, on the same seed and with the same forced set; all 96 came back with the same templates and the same poses for the same people. With v0.49's own pictures that is four casts on 32 pictures, 128 readings. Sixteen readers had eight pictures each, two of every cast, and no reader saw a picture twice. The prompt is the screen's own. The count is `who_cmp.py`'s: the first inventory line that names the figure's clothes, and whether the first word for a person in it is girl, boy, teenager, child or kid.

**The casts.**
- **O**: v0.49's.
- **M**, marks of age: the woman in purple as tall as the woman in yellow, and both with a woman's bust (the chest node of the torso set forward and deeper, `people.py`); the yellow dress to below the knee; the man in green with a fuller beard that stands off the chin. Her hair up in a bun was tried first for the woman in purple and dropped on my own look: with her whole face bare she looked younger.
- **P**, proportions: every grown figure's head 0.86 of its size against the same body (about five heads tall, for four and a third). The teenager and the children are as they were.
- **MP**: both.

**Called young first**, of the appearances in the 32 pictures:

| Cast | Woman in purple | Woman in yellow | Man in red | Man in green | All four |
|---|---|---|---|---|---|
| O, v0.49 | 7 of 19 | 2 of 12 | 1 of 6 | 3 of 8 | **13 of 45** |
| M, marks | 2 of 19 | 1 of 12 | 0 of 6 | 0 of 8 | **3 of 45** |
| P, smaller heads | 3 of 19 | 0 of 12 | 1 of 6 | 1 of 8 | **5 of 45** |
| MP, both | 1 of 19 | 0 of 12 | 0 of 6 | 0 of 8 | **1 of 45** |

The bench finds the screen's fault where it is: 13 of 45 with v0.49's cast, for the screen's 16 of 45 on the same pictures. Each change cuts it by itself, and together they leave one.

The same picture in two casts. Of the walker with an ice cream, v0.49's cast: "Girl (left, front-middle): dark hair in a ponytail, purple top, teal trousers; walking beside the path while eating a pink ice-cream cone." (who, pic_012); both changes: "Woman, left: purple top, teal trousers, dark ponytail. Walking on the path, eating a pink ice-cream cone." (pic_073). Of the digger, v0.49's cast: "Boy/young man (centre, front): short dark hair, green T-shirt, beige trousers; digging with a shovel, bent forward, frowning in effort." (pic_111); both changes: "Man, centre: green T-shirt, beige trousers, dark skin, beard. Bent over, digging with a spade, looking focused or strained." (pic_089).

The one left is the runner in the playground, a girl in all four casts: "Girl, front centre: dark hair in ponytail, purple top, teal trousers; running to the right, speed lines behind her." (pic_100).

**What the readers named.** The fuller beard is seen: a beard is named in 5 of the man in green's 8 pictures with either cast that has it (M and MP), in 1 of 8 with v0.49's and in none of 8 with P. The moustache is named in 3, 5, 2 and 2 of its wearer's 6 pictures (O, M, P, MP): the smaller head shows it a little less. Its wearer was called a boy once with O and once with P, and not with M or MP. No reader of any cast wrote of a head's size, of a bust or of the dress's length; the women's hair is "a ponytail" in about half the pictures of every cast (16, 13, 16 and 15 of 30).

**Taken: MP** (`specs.AGE50`). It is the first change to this fault that was measured where the fault happens. It changes how every grown figure looks, so a sheet of the four casts with the counts on it went to Sam before the cast was built (`isolation_v050/age_candidates.png`), with D, both, named as the one the release goes ahead with.

**Limits.** One bench, 45 appearances a cast, and the pictures were picked for holding these figures. Sixteen readers are sixteen habits, which is why every reader had every cast. The screen will count it again on new pictures (`who_cmp.py`).

## Rules in the scene, cut out (rounds 1 to 3)

Each thing was forced alone into a picture and cut out (`isolation_bench.py`, cases with the third letter q; `isolation_v050/round1` to `round3`). Round 1 was ten readers and 30 cut-outs, three to a reader; round 2 four readers and 11; round 3 three readers and one each. No reader saw two takes of one thing.

### The seesaw's riders (`templates.SEAT50`)

On the list since v0.45: "perches a little above the plank". The riders were raised 14 units in v0.31, when that seated them. Their bodies have been drawn again twice since, and measured in the sprites the hips now lay 4 to 10 units above the plank's top edge. The rule that replaces the constant measures each child's own drawing (`_under50`: how far it reaches below its seat anchor, at the hips) and sets that edge on the plank.

| Case | Drawn | What the readers said |
|---|---|---|
| `ssqO_1` to `_3`, `shqO_1`, `_2` | **O**: v0.49 | "The right child appears to sit slightly above/in front of the plank rather than firmly on it" (round1 iso_29). A handle held in two of the three seesaws |
| `ssqN_1` to `_3`, `shqN_1`, `_2` | **N**: seated by measure | "Nothing appears to float or pass through anything else." (iso_04). But the handle was gone, in three of three: "Neither child seems to have handles to hold; their hands are just held in front of their bodies or in their laps." (iso_06); "Neither child holds a handle; their hands rest on their own knees, so it is a little unclear how they keep hold of the seesaw." (iso_04). One rider of the heavy seesaw "slightly floaty" (iso_24) |
| `ssqA_1` to `_3`, `shqA_1`, `_2` | **A**: N, and the handle a grab bar that comes down to the plank ahead of the knees | A handle held in five of five: "Each child holds a dark grip handle in front of them." (round2 iso_02); "holding a black curved handle" (iso_04, iso_08, iso_09). No rider above the plank in any of the five |

Seated, the riders hid the old handle's post in their laps, and what had shown of it before was the part under a floating thigh. The handle is now a bar that leaves the post's top and comes down to the plank in front of the rider (`draw.seesaw`, `arch`), and an empty seesaw has the same bars (`settings.SEESAW50`).

What every drawing gets, old and new, is the legs: "it is hard to tell whether he is sitting on top of the board or the board passes through his legs" (round2 iso_04), and the grown rider of the heavy seesaw, whose seat was not changed: "the board seems to pass through or behind his legs" (iso_09). That is v0.31's note and stays one.

**Taken: A.**

### The slider (`templates.SLIDE50`)

"The girl seems to sit slightly above the chute surface" (v0.49). Three other places for the slider were read against v0.49's:

| Case | Drawn | A remark on how the child sits |
|---|---|---|
| `slqO_1` to `_3` | **O**: v0.49, the figure in front of the chute | 2 of 3: "She seems to sit slightly above/in front of the slide surface rather than clearly on it" (round1 iso_01) |
| `slqN_1` to `_3` | **B**: the chute's near wall drawn again over the slider | 2 of 3: "so she looks like she is floating next to it rather than sliding on it" (iso_09) |
| `slqA_1` to `_3` | **A**: B, the slider sunk until the wall hides the hips | 3 of 3: "Her legs are mostly hidden. Only one small foot shows, so the lower body looks cut off or merged into the slide." (round2 iso_03) |
| `slqT_1` to `_3` | **T**: the slider on top of the far rail, the whole figure above the slide | 3 of 3: "The child appears to be sitting slightly above the chute rather than clearly resting on it" (round3 iso_02) |

In front of the chute, behind its wall, deep in it or on top of it, the child sits "slightly above" it. Where the slider is put is not what the readers see. **Taken: none.** The slider stays where v0.49 had it, and what is left to try is the drawing of the chute and the pose, which is said in the next list.

### The stopped hose (`templates.HOSE50`)

v0.49: the dog "on the hose, or on its connector", in three pictures of five. The short round swelling before the paw has been a connector since it was drawn, and a long low one was a puddle before it. N draws no swelling: the hose runs full and thick from the reel to the paw, lies flat under it and runs on thin.

| Case | Drawn | What the readers said |
|---|---|---|
| `hsqO_1` to `_3` | **O**: v0.49, the swelling | A connector in three of three, and the stopped water offered in two: "The hose has a bulge/kink right where the dog's front paw is, so it reads as the dog stepping on the hose (blocking the water) - or it could just be a hose fitting/joint." (round1 iso_15) |
| `hsqN_1` to `_3` | **N**: no swelling | No connector in any. The dog on the hose in three, and the stopped water offered in one: "This could be read as the dog stepping on the hose and blocking the water (which would explain why no water comes out), or just as the dog standing there by chance." (iso_20). No reader wrote of a thick run and a thin one |

The swelling is misnamed, and it is also what says that something happens at the paw. Without it the remark goes and so does half of the inference. **Taken: none**, and R2 is closed with that: the connector has now been read against its own absence.

### The lost balloon (`templates.LOST50`)

All six of v0.49's pictures of the template were garden ones, and in the garden a rule of v0.45 (`WOOD45`) lifts the string's free end onto the hedge above the fence, up to 200 units above the reaching hand. That rule came from my own look at two pictures and from no reader. The half mark of v0.49 was "The red balloon may belong to the girl (she let go) or to someone else".

| Case | The string's end | What the readers said |
|---|---|---|
| `lbqO_1` to `_3` | **O**: lifted above the fence | Escaped from this child in three of three; "so the link between him and that balloon is implied rather than shown" (round1 iso_03) |
| `lbqN_1` to `_3` | **N**: by the hand, as in the other settings | Two of three were not sure it had left the hand: "as the child still holding it with a small drawing gap" (iso_28); "the child is still holding it and the gap is a drawing error" (iso_23) |
| `lbqM_1` to `_3` | **M**: a head's height above the hand | Escaped from this child in three of three; once "a string that should connect to her hand and doesn't" (round2 iso_11) |

Too near is held, as v0.44 found, and far is somebody else's. **Taken: M.** The cut-outs do not choose between M and O; M was taken because its string ends by the child and no reader of it held the balloon.

### The goat's stake (`templates.STAKE50`)

v0.49: "The goat's tether stake looks very short; the goat could be tethered or just standing by a stake." N is half as tall again, with the rope in two turns round its upper part and not in a ring at its foot. One cut-out each: "A tan rope runs from its collar down to a short brown stake (with a ring on top) driven into the ground, so the goat is tethered." (round1 iso_07, O); "A tan rope runs from its collar down to a short brown wooden stake in the ground, so the goat seems to be tethered." (iso_11, N). Tethered both ways, and a short stake both ways: a bench that found nothing between them. **Taken: N**, since the rope is now tied on the stake where it lay at its foot, and it costs nothing.

## The cast's two props (round 4)

Six readers, twelve cut-outs, two to a reader (`isolation_v050/round4`). N is v0.50's cast and O v0.49's, with revision 47's rules both times.

### A held balloon's string (`TPDB_STRING50`)

v0.49: "The balloon's string is perfectly straight and stiff, so it could be a balloon on a stick, or a lollipop/ice lolly on a stick; most likely a balloon." The string now hangs in a loose S from the balloon to the fist.

| Case | Drawn | What the readers said |
|---|---|---|
| `blqO_1` to `_3` | **O**: straight | A stick in two of three: "The balloon string is a stiff straight line, so it could read as a stick (a balloon on a stick) rather than a string." (round4 iso_10); "She holds a long stick in one raised hand, with a yellow oval on top of it." (iso_06) |
| `blqN_1` to `_3` | **N**: a loose S | A string in three of three: "The balloon string runs from the hand up to the balloon in a slightly wavy line; it looks fine" (iso_11). Once still "almost like a lollipop or paddle on a stick" (iso_09) |

**Taken: N.**

### The painter's pole (`TPDB_ROLLER50`)

v0.49: "The roller looks a little small and oddly held, high above the woman's hand, but it reads as painting.", in three pictures of eight. On looking at the pictures, the pole was drawn in the wood's colour and lay on a fence of the same colour, so the roller's head stood alone above the hands. N's pole is a dark metal one, a little thicker.

All six cut-outs were read as a long-handled roller painting the fence. With v0.49's pole two readers of three offered something else for the head: "the roller could also be taken for a can or cylinder held against the fence" (round4 iso_01); "it could also be taken for a brush or a sign on a pole" (iso_08). With the dark pole none did: "The roller handle runs from his hands at chest height up to the roller" (iso_03). **Taken: N.**

## Looked at and left

- **R3, the game of catch.** The catcher's hands are open already and the ball's path is drawn from the thrower's hand; one reader of four pictures offered the catcher as the thrower. Left.
- **R4, the dogs.** The sleeper's eye is a shut line and its head is on its paws; "asleep" beside "lying with its head down" is a hedge that a sleeping dog earns. No cartoon symbol may say sleep. Left.
- **R5, the heavy seesaw's call.** "worry, surprise, or calling out": the item accepts both a scared child and a calling one. Both hands round the mouth would hide the mouth in a side view, which is why v0.44 cupped the far hand. Left.
- **O6, the reading dog's glasses.** Named plainly in three of six v0.49 pictures. Left.
- **O7, the catcher's "tear".** On looking, it is no mark on the cheek: it is the white of the wide eye of the surprised face, at the edge of a face seen from the side. One picture. Left, and named for what it is.

## What the rules cost in placement

Each changed template alone, twelve seeds, with its rule on and off (`tools/cycle/yield_set.py`, `BAND=0`): the lost balloon in the garden, the goat in the park, the seesaw and the heavy seesaw in the playground each placed on 12 of 12 both ways.
