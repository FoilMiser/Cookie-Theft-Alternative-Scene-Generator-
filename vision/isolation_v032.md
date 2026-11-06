# v0.32 isolation bench

Each visual was forced into a picture with little else and cut out, then read blind by fresh readers (the method of `isolation_v023.md`). Round 1 was nine readers and 15 cut-outs, at most two to a reader and never two versions of one thing (`isolation_v032/round1`; `map.json` says which cut-out is which case). Round 2 was three readers and three cut-outs, round 3 three readers and six (`round2`, `round3`).

The seesaw cut-outs all hold the same two riders, the bearded man in green and the girl in pink, as the template prefers them, so the three of a case differ by little more than which way the picture faces. Each reader saw one.

## The man on the seesaw's low end (`templates.LOW32`; the cast's `TPDB_LOW`)

"Sitting on the plank end or sitting just beside it with the plank behind his legs", in two of v0.31's six seesaw pictures, and both men in its design tests. He sits astride with his knees up and his feet planted near the seat, so his near shin crosses the rising plank.

| Case | Drawn | What the readers said |
|---|---|---|
| `ridO_1` to `_3`, `ridG_1` to `_3` | **O**: v0.31 (`G` the girl lower, the man the same) | All six on his seat: "It could look like the bar passes through his legs" (`ridO_1`); "His seat looks like it hangs in the air just behind and above the board" (`ridO_3`); "whether the beam passes behind or through his thighs" (`ridO_2`); "the plank could be passing through his legs. He doesn't clearly sit on top of it" (`ridG_1`); "his lower legs look slightly tangled with it" (`ridG_3`) |
| `ridX` | **X**: his legs out along the ground under the plank | Not read. Up close the plank lay across his lap and his feet ran into the pivot's base |
| `ridF_1` to `_3` | **F**: turned away from the plank, near its end, his feet on the ground past it | All three still doubt the seat: "sitting just in front of the plank's end instead of on it" (`_3`), "perched in front of it with his feet planted" (`_2`), "awkward and cramped against the end of the board" (`_1`). And a new remark: "The man's direction looks unusual for a seesaw" (`_2`). It also placed less often: 14 of 20 seeds with the seesaw and three events forced, against 18 of 20 for O (`tpdb_work/place32.py`) |
| `ridB_1` to `_3` (round 2) | **B**: both legs behind the plank, the rest in front (`~body` and `~legs`, a new cut in `render_assets.split_leg`) | All three: "the board and handle pass through his thighs" (`_1`), "the beam runs in front of or through his legs rather than under him" (`_2`), "the plank seems to pass across his lap or thighs" (`_3`). It bared the handle's post at his lap as well |

**Chosen: O, unchanged.** The old drawing and the two new ones that were read each drew a doubt about his seat from every reader. The remark has been on the list since v0.27. v0.24 had raised the riders, v0.28 moved them in from the plank's end and v0.31 cut the rider in two, and this bench tried three more ways. Through all of it every reader has had him on the low end, and `seesaw_heavy` has read 1.00 in every screen from v0.27 to v0.31. It comes off the list, as the hose's "stiff" did in v0.31. The switches stay, for the record.

## The girl stuck up high (`templates.HANDLE32`, `STUCK32`)

"May look like she is hovering slightly", once in v0.31. The flaws list proposed less of the raise.

| Case | Drawn | What the readers said |
|---|---|---|
| `ridO_1` to `_3` | raised 14 units (v0.31) | No reader says she hovers |
| `ridG_1` to `_3`, `ridF`, `ridB` | raised 8 | No reader says she hovers either. "The girl's legs hang in front of the board, which is plausible" (`ridG_2`) |

Lowering her found nothing to choose. What the readers did say, again and again, was about her hands: "a little above the handle rather than clearly around it" (`ridF_3`), "just above the handle. They don't clearly grip it" (`ridG_1`), "not on the black handle in front of her, so she does not seem to be holding on" (`ridB_1`). That was 7 of the 15 seesaw readings of rounds 1 and 2, and one more read her "clasped hands" as perhaps "clapping". Raised 14 units in v0.31 and the handle not, her fists sat above its bar, the more so the higher she sat.

| Case | Drawn | What the readers said |
|---|---|---|
| `ridH_1` to `_3` (round 3) | **H**: raised 14, and the handle as much taller | None of the three says anything about her hands. "Nothing is clearly floating or passing through anything else. The girl's legs hang in front of the beam, which looks fine" (`_2`) |

**Chosen: H**, with the rise as it was. The handle of any rider who grips it (the stuck girl, and the child stuck up with a teenager) stands taller by her rise (`draw.seesaw(up=...)`).

## The box carried at the side (`TPDB_BOX`, in the cast)

"As if it is half floating", once in v0.31. In profile the near hand lies flat on the box's face.

| Case | Drawn | What the readers said |
|---|---|---|
| `boxO_1` to `_3` | **O**: v0.31, the hands pressed to the box's sides | All three: "The box looks a little stuck to the front of the torso rather than clearly gripped" (`_1`), "it isn't clearly supported from below, so it could read as only lightly held or slightly floating" (`_2`), "almost floating in front of him" (`_3`) |
| `boxU_1` to `_3` | **U**: higher, on the hands, the near hand at the box's corner by the body | All three again: "as if held by one hand at one corner" (`_1`), "floating slightly in front of her, since the support looks thin for a box that size" (`_2`), "The box seems to float slightly in front of his body, held up by that one hand" (`_3`) |
| `boxV_1` to `_3` (round 3) | **V**: the near forearm under the whole box, the hand at its far corner | No reader says it floats. "As if the box rests on that hand more than being held" (`_1`); "he could be either holding it up from underneath or pressing it against his chest" (`_3`); "the hold looks slightly awkward" (`_2`), the box "right at her chin" |

**Chosen: V.** Every walker and stander with a box re-renders (the gallery's one, the library's on demand).

## No drawing

**Watering under storm clouds.** A hose spraying under storm clouds "could be read as ironic or pointless, but she does not seem to have noticed the clouds" (v0.31, picture 59). `water_flowers` and `hose_water` now ask for a clear sky, as the washing has since v0.31, and so do `water_upward` and `pan_watering`, which are drawn as the first is. The stopped hose is left out, as nobody waters with it.

**The jump by a ball in a tree.** The gate's one failure in v0.31, `jump`, was a boy jumping 12 px from a ball stuck in a tree: he "could be trying to reach the ball or just cheering". The jumper now keeps 200 units from a ball or kite in a tree, side to side (`templates.JUMP_CLEAR30`). The ball is placed first, so the jump can see it.

## The bench itself

The bench's switches were set case by case from the name's prefix, each with a default for names that matched none, and many defaults were older drawings: a v0.32 case would have drawn v0.30's seesaw riders, the reel where v0.30 had it and the old trip. Every case now starts from the release's values (`_REL`), the old cases keep their prefixes as before, and the v0.32 cases are set by name.
