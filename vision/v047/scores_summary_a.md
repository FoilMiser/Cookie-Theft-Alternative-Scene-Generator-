# v0.47 scoring summary (set A, pic_01 to pic_22)

Coverage check: all 22 pictures and all 249 keyed items in keys_a.json have exactly one score in scores_a.json. No item is missing and none was invented (checked against the key by script).

## Mean score by item type

| Item type | Items | Mean |
|---|---|---|
| entity | 140 | 0.950 |
| action | 72 | 1.000 |
| inference | 13 | 1.000 |
| contradiction_notice | 12 | 1.000 |
| contradiction_explain | 12 | 1.000 |
| **all** | **249** | **0.972** |

## Items scored 0, 0.5 or misread

There were no 0.5 scores and no misreads. All seven zeros are the same item, "There are a few white clouds". In each case the describer mentioned the sun or a sunny day but never the clouds.

| Pic | Id | Target | What the describer said |
|---|---|---|---|
| pic_09 | i06 | There are a few white clouds | 0: "It is a sunny day"; no clouds |
| pic_10 | i06 | There are a few white clouds | 0: "A sunny back garden"; no clouds |
| pic_11 | i05 | There are a few white clouds | 0: "sunny playground"; no clouds |
| pic_13 | i05 | There are a few white clouds | 0: "sunny back garden"; no clouds |
| pic_14 | i08 | There are a few white clouds | 0: "sunny public park"; no clouds |
| pic_15 | i07 | There are a few white clouds | 0: kite "high in the sky"; no clouds |
| pic_16 | i07 | There are a few white clouds | 0: "sunny back garden"; no clouds |

## Judgement calls scored 1

| Pic | Id | Why it was a call |
|---|---|---|
| pic_01 | i02 | Says the dog wants a walk, but the unsure section adds "could also just be holding the leash" |
| pic_01 | i03 | Hanging up vs taking down the washing; "hanging up seems more likely" |
| pic_02 | i03 | Begging is stated, but the unsure section offers "or just sitting up" |
| pic_03 | i02 | Target is a girl; describer says a "child in pink" and can't tell girl or boy |
| pic_04 | i11 | Joyful jump vs reaching up; "looks like a joyful jump" |
| pic_08 | i03 | Begging is stated, but the unsure section offers "or just sitting up" |
| pic_09 | i03 | Water going up is stated, but the unsure section offers "a thin hose" |
| pic_10 | i03 | Water going up is stated, but the unsure section offers "a thin hose" |
| pic_10 | i04 | Near word: "girl or young woman" for the woman |
| pic_12 | i04 | Stuck vs flying behind the tree; "stuck seems more likely" |
| pic_12 | i07 | Ready to catch vs clapping |
| pic_16 | i03 | Water going up is stated, but the unsure section offers "a thin hose" |
| pic_19 | i10 | Will trip vs walk past the box; "Most likely he will trip over it" |
| pic_21 | i01 | Near word: "girl" for the woman fishing |
| pic_22 | i01 | Target is a girl; describer says "small child in pink" (gender not stated) |

## Unintended oddities

The describers raised four oddities that are not scored items, in two pictures.

**Seesaw and swing rendering (2)**
- pic_03: the seesaw child's lower legs seem to pass through the plank
- pic_03: the swing set has only one swing, as if a second one is missing

**Hands and props (2)**
- pic_17: the pan is held level, yet water pours sideways out of its rim
- pic_17: the man's arm looks long

**Animals (0)**
- None. Count by angle: profile 0, three-quarter front 0.

Hedges left out as small details: pic_11 (the girl seems to sit slightly above the seesaw board, "could just be the drawing angle"), pic_12 (the ball's arc ends slightly beyond the woman's hands), pic_15 (the washing hangs at a slant, maybe from wind), pic_16 (the paint tin is a few steps from the painter), pic_20 (the hose reel is not connected to a tap).
