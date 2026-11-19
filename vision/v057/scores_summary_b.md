# Scores summary, set B (pic_28 to pic_54)

Check: every item in keys_b.json got exactly one score. That is 27 pictures and 292 items. No item is missing and none is invented, because the picture and item ids match the key exactly.

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 181 | 1.000 |
| action | 67 | 1.000 |
| inference | 12 | 1.000 |
| contradiction_notice | 16 | 0.969 |
| contradiction_explain | 16 | 0.969 |
| **All** | **292** | **0.997** |

## Items scored 0, 0.5 or misread

| Pic | Id | Score | Target | What the describer said |
|---|---|---|---|---|
| pic_38 | i04 | 0.5 | Something is wrong with the wheelbarrow | Only in the unsure section: the wheel "looks square or boxy", but it "may just be a stylised wheel seen from an angle" |
| pic_38 | i05 | 0.5 | The wheelbarrow has square wheels, so it could not roll | Square/boxy offered as one of two readings (the other is a stylised round wheel); does not say it could not roll |

No item scored 0 or misread.

## Items given a "call"

| Pic | Id | Call | Why |
|---|---|---|---|
| pic_35 | i03 | two | The box is "hanging in mid-air with nothing holding it up", but "falling" or "being thrown" are also offered |
| pic_36 | i04 | two | The dog would pinch the hose and stop the water; the unsure section also offers "the hose is simply not turned on" |
| pic_40 | i03 | near | "No water" is not said outright; it is implied by "dog seems to be stopping the water" and "about to get sprayed when the dog steps off" |
| pic_40 | i06 | two | The girl points up, either at the cat on the fence or at the ball in the tree |
| pic_40 | i17 | near | Only in the unsure section: the wheel "looks square or boxy rather than round"; not called wrong |
| pic_40 | i18 | near | Says square/boxy, not round, but not that it could not roll |
| pic_41 | i07 | two | The cap is blown away by the wind; the unsure section adds "her having just tossed it" |
| pic_45 | i02 | near | The bird is next to the sandwich and "about to take" it; it may already be pecking, but pulling the bread off is not plainly said |

## Unintended oddities (not scored items)

**Water and hose rendering (2)**
- pic_36: water leaks and puddles at the hose reel while nothing comes out of the nozzle
- pic_40: water drips or leaks at the hose reel end

**Object grounding or cut-off (1)**
- pic_35: the watering can looks half-sunk or cut off at the bottom, as if sinking into the grass

**Figure placement or pose (2)**
- pic_52: the man sits on the end of the seesaw plank rather than on the seat
- pic_54: the woman and dog walk on the grass beside the path rather than on it [dog, profile]

**Oddities about animals, by angle**
- profile: 1 (pic_54, dog)
- three-quarter front: 0

Total: 5 oddities in 5 pictures. The other 22 pictures have none.
