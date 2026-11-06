# v0.33 isolation bench

Each visual was forced into a picture with little else and cut out, then read blind by fresh readers (the method of `isolation_v023.md`). One round: nine readers and 18 cut-outs, two to a reader, one of each thing and never two versions of one (`isolation_v033/round1`; `map.json` says which cut-out is which case). The drawings are switches in `scenegen/templates.py`, set by case name in `vision/isolation_bench.py`.

Each case's three cut-outs are three seeds of the same forced template, so they differ in who is drawn and which way the picture faces. Two drawings were set aside on looking, before any reader saw them: the hose led in front of the dog's front feet first rose straight from the ground to the hand, as a hose that read as "a pole" did in v0.11, and was redrawn to join its old curve; and kick arcs in front of the toes (`F`) lay on the plank, so `N` took their place.

## The stopped hose (`templates.HOSE33`)

"Only a single drop is shown, so it is unclear whether water is flowing. The dog's back foot looks as if it may be standing on the hose" (v0.32, picture 28, the gate's one failure, on a picture identical to v0.31's, where it read in full). The hose runs from the reel, swells against the dog's back foot, and runs on thin under its front feet as well, so every foot is on its line.

| Case | Drawn | What the readers said |
|---|---|---|
| `stpO_1` to `_3` | **O**: v0.32 | One reads the joke whole: "This reads as the dog blocking the water by standing on the hose, so the child gets only a drip" (`_1`). The others offer it as one of two: "The dog's back foot appears to stand on the hose. It could be stepping on it, or the foot may just overlap it" (`_2`); "Reading 1: the dog is stepping on the hose and blocking it. Reading 2: the hose just lies next to its feet" (`_3`). The swelling is "a kink or bulge in the hose, or a small puddle" (`_2`) |
| `stpF_1` to `_3` | **F**: past the foot the hose dips toward the viewer and runs in front of the front feet | No better: "the back paw sits at the end of the bulge, and the front paws are near the hose but seem slightly above it" (`_1`); "The dog's feet sit right on the hose line, so it looks as if the dog is standing on the hose (or the hose runs through its feet)" (`_2`); the swelling "almost like a blob or puddle" (`_3`) |
| `stpP_1` to `_3` | **P**: F, and the hose flattened wider under the foot | No better, and the dip drew remarks of its own: "the dog's back paw looks merged with the hose, and the hose dips oddly just past the dog" (`_1`); "Near the man's feet it seems to loop back on itself" (`_2`); the flat part "a puddle of water, a shadow, or a bulge in the hose drawing" (`_3`) |

**Chosen: O, unchanged.** Neither redraw read the foot on the hose more firmly, and both added a remark on the hose's path. In every reading the swelling is a bulge or a puddle, and that, not the foot, is what keeps the joke a second reading. The stopped hose read in full in two of its three screened pictures in v0.32, and on this same picture in v0.31, so it is watched, as the flaws list allowed.

## The stuck rider's kick arcs (`templates.KICK33`)

"The motion arcs under the girl's feet make her look as though she is hovering slightly above the plank" (v0.32, picture 18). The arcs were added in v0.16, when three readers of the stuck girl without them saw nothing wrong ("the tilt makes sense"). She has called out since revision 12 and holds a raised handle since revision 30.

| Case | Drawn | What the readers said |
|---|---|---|
| `kikO_1` to `_3` | **O**: v0.32, arcs round the feet, below them | No reader says she hovers. "Motion lines under her feet show her legs swinging or kicking" (`_2`). Stuck once: "his weight keeps the girl's end up in the air" (`_2`); otherwise "the seesaw may not really be in play" (`_3`) |
| `kikB_1` to `_3` | **B**: arcs behind the heels, clear of the plank | Two of three see her off the plank: "It is hard to tell whether she is firmly seated on it or hovering slightly above it" (`_1`); "She also looks perched just above or behind the plank rather than firmly on it" (`_2`) |
| `kikN_1` to `_3` | **N**: no arcs | No reader says she hovers, and all three have her stuck: "the light girl is stuck up in the air" (`_2`); "The man's weight seems to be keeping her stuck up high while he reads" (`_3`); "surprised or nervous about being stuck up high" (`_1`) |

**Chosen: N.** With the calling pose and the raised handle she reads as stuck without them, which she did not in v0.16, and nothing under her feet draws the eye to the gap between her and the plank. The man on the low end drew his remark in every case, as he has since v0.27 ("The red board seems to run behind his legs and lap"); he is off the list.

## No drawing

**The storm pointer by a cat on the fence.** In the v0.32 tier-3 garden a woman points up at the clouds, and a cat walks the fence right over her fingertip: "pointing upward at the cat with a surprised face" (picture 51). Revision 6 keeps the line from the fingertip to the clouds clear, and it was clear, as the arm pointed up and away from the cat. Revision 31 also keeps anything scored whose top is above the fingertip 100 units from it, whichever way the arm points (`templates.NEAR31`, `_rain_tip_clear`). With the pointer, a cat on the fence and a bird on a post forced into ten garden pictures, all ten placed under revision 30 and under revision 31, and the one picture that had the cat within 100 units of the fingertip (93) placed with it at 129 (`tpdb_work/place33.py`).

**The hose in the wind.** "The wind is strong enough to blow a cap off, but the hose water is not bent by it" (v0.32, picture 44). From revision 31 a hose does not spray in a picture with a wind template. The rule is in `HoseWater.place()`, not in the class body, so earlier records rebuild as they were (`RUNBOOK.md`, Lessons).

## The bench itself

v0.32 had given three of its cases the names of three of v0.31's, `ridO_1` to `_3`, and in a dict the later entry wins: the file as committed would have run v0.31's cases under v0.32's names. v0.32's own round 1 had run before v0.31's cases were put back, and its cut-outs show v0.32's cases, so `isolation_v032.md` stands. v0.31's three are now `ridO31_1` to `_3`, and the bench refuses a case name used twice.
