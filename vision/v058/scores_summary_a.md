# v0.58 scores, key set A (23 pictures, 230 items)

Coverage check: every item in keys_a.json (23 pictures, 230 items) has exactly one score in scores_a.json. No item is missing, none was invented, and there are no extra pictures.

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 143 | 1.00 |
| action | 59 | 1.00 |
| inference | 6 | 1.00 |
| contradiction_notice | 11 | 1.00 |
| contradiction_explain | 11 | 1.00 |
| **all** | **230** | **1.00** |

## Items scored 0, 0.5 or misread

None. Every item scored 1.

## Items scored 1 as a judgement call

| Pic | Id | Call | Why |
|---|---|---|---|
| pic_06 | i02 | unsure | Free description says the upward water "looks physically impossible"; the unsure section also offers a spray/fountain reading. |
| pic_06 | i03 | unsure | Water plainly curves upward from the spout; the spray/fountain reading appears only in the unsure section. |
| pic_07 | i02 | unsure | Water shoots upward "instead of falling down"; the unsure section adds "could be read as a spray". |
| pic_07 | i03 | unsure | Same as i02: the upward water is plain, the spray reading appears only in the unsure section. |
| pic_11 | i03 | unsure | "The dog seems to hope for a taste"; the unsure section adds that it could be "simply looking up". |
| pic_14 | i05 | near | "The escaped red balloon" she reaches after, "will probably be lost"; it does not say outright that she let go. |
| pic_15 | i03 | two | Box floating with nothing holding it, but the inventory says "floating/falling" and the unsure section gives the falling reading. |
| pic_17 | i03 | near | The red balloon is "escaping" and she reaches after it; it does not say outright that she let go. |
| pic_21 | i04 | unsure | Arms raised, smiling, "as if cheering or celebrating" (jumping not said); the unsure section adds waving or reacting. |
| pic_22 | i03 | two | Box in the sky with nothing holding it up and "looks like it is floating", but the free description also says "may be read as falling". |

## Items with a word under "who"

| Pic | Id | Describer's word | Item's names |
|---|---|---|---|
| pic_19 | i02 | boy | man, guy, father, dad, person |

(pic_10 i04: "A man (or teenager)". The first word, "man", is among the names, so "who" is null.)

## Unintended oddities

Grouped by kind:

- **Pose and tool contact (people):** 1
  - pic_01: the paint roller sticks up above the fence top, as if touching the air, and the man's hands and roller handle overlap his body awkwardly.
- **Distance and scale (people):** 1
  - pic_04: the fisherman stands well back from the pond, with the rod and line stretched over a long distance (an unusually long rod).
- **Animals:** none. By angle: three-quarter front 0, profile 0.

These were left out as hedges or as not presented as wrong:
- pic_17: the wheelbarrow is "a little oddly drawn but is recognisable".
- pic_19: a tethered goat in a park is "a little unusual but drawn plausibly".
- pic_10: the man's legs overlap the pond outline, but the describer says he is "in front of the pond, not in it".
