# v0.52 scores, key set A (26 pictures, 282 items)

Coverage check: every item in keys_a.json (26 pictures, 282 items) got exactly one score. The ids in scores_a.json match the key's ids one for one and in order. No item is missing and none was added.

## Mean score by item type

| Type | Items | Sum | Mean |
|---|---|---|---|
| entity | 169 | 168 | 0.99 |
| action | 79 | 79 | 1.00 |
| inference | 18 | 16.5 | 0.92 |
| contradiction_notice | 8 | 7 | 0.88 |
| contradiction_explain | 8 | 6.5 | 0.81 |
| **All** | **282** | **277** | **0.98** |

No item was scored "misread".

## Items scored 0, 0.5 or misread

| Pic | Id | Score | Target | What the describer said |
|---|---|---|---|---|
| pic_02 | i09 | 0.5 | The duck has come to eat the bread | Bread floats near the duck and the girl "seems to be feeding the duck". The describer never says the duck has come for the bread. |
| pic_09 | i08 | 0.5 | The bicycle has square wheels, so it could not roll | Only the back wheel is called "square-ish", and only in the unsure section. The front wheel and the fact that it cannot roll are not mentioned. |
| pic_11 | i04 | 0 | Something is wrong with the wheelbarrow | The wheelbarrow is described as "fine", and the describer says "Nothing looks floating or impossible". |
| pic_11 | i05 | 0 | The wheelbarrow has square wheels | The square wheel is not mentioned. |
| pic_16 | i03 | 0 | The bird is stealing the sandwich while the woman is busy reading | The describer gives only what is visible: a bird pecks at a sandwich beside the woman. Stealing and her not noticing are not mentioned. |
| pic_16 | i21 | 0 | There are a few white clouds | Clouds are not mentioned anywhere. |

## Judgement calls scored 1

| Pic | Id | Why it was a call |
|---|---|---|
| pic_01 | i01 | "Apparently asleep", with "sleeping or just resting" in the unsure section. Sleeping is the main reading. |
| pic_02 | i04 | The teenager is called a "boy". |
| pic_02 | i13 | The ice cream "has fallen on the ground" while the child holds an empty cone. The describer says fallen, not dropped. |
| pic_03 | i01 | Reading a newspaper, where the key says reading. |
| pic_03 | i02 | Hand to mouth is read as worried or surprised, with calling out given only as one option. "Stuck up in the air" is stated plainly. |
| pic_07 | i03 | The describer says he "is ignoring the stuck girl" (an accepted reading) but never mentions his weight. |
| pic_09 | i07 | The back wheel is "slightly odd", said only in the unsure section. |
| pic_09 | i11 | Pointing at the sky is the main reading. The describer also offers pointing at a building. |
| pic_12 | i07 | Ready to catch, with "reaching/clapping" offered as another reading. |
| pic_16 | i05/i06 | A "beach ball" stuck in the tree, where the key says a ball. |
| pic_19 | i06 | "As if she has just let it go". The girl's reach is also read as possibly waving. |
| pic_22 | i01 | Reaching for the balloon, with waving offered as another reading. |
| pic_22 | i05 | The teenager is called a "boy". |

## Unintended oddities (6 in 6 pictures)

**Figure not attached to its support or overlapping the scenery (4)**
- pic_03: the man's body sits in front of the seesaw board rather than on it, so he looks detached.
- pic_07: the same detached-from-the-seesaw look.
- pic_13: the old man overlaps the front edge of the pond and looks too close to it.
- pic_24: the elderly woman overlaps the pond's outline and could be standing at the water's very edge.

**Missing part or missing source (2)**
- pic_15: the swing frame has only one seat although it is wide enough for two.
- pic_18: the hose comes in from the left edge with no visible tap or reel.

**About animals:** none. No unintended oddity concerns a keyed animal, so the count by angle is 0 for every angle (profile 0, three-quarter front 0).

Left out as hedges about small details:
- pic_02: a tethered goat in a park is "a little unusual", but the describer calls it deliberate.
- pic_21: the man's kneeling pose is "slightly awkward".
- pic_23: the roller handle bends at an odd angle, which the describer calls "minor".
