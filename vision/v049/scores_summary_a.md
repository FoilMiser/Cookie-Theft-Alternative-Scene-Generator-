# v0.49 scoring summary (keys_a)

21 pictures, 210 scored items. Completeness check: every item id in keys_a.json for pic_01 to pic_21 has exactly one score in scores_a.json; no item is missing and none was invented (per-picture counts 10, 8, 9, 8, 14, 9, 10, 8, 9, 5, 25, 4, 11, 11, 9, 9, 10, 10, 14, 7, 10).

## Mean score by item type

| Type | Items | Sum | Mean |
|---|---|---|---|
| entity | 136 | 131 | 0.963 |
| action | 53 | 53 | 1.000 |
| inference | 9 | 9 | 1.000 |
| contradiction_notice | 6 | 6 | 1.000 |
| contradiction_explain | 6 | 6 | 1.000 |
| **all** | **210** | **205** | **0.976** |

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---|---|
| pic_18 | i05 | There are a few white clouds | 0 | "sunny park", no sky detail beyond that |
| pic_19 | i10 | There are a few white clouds | 0 | "sunny back garden", no clouds |
| pic_19 | i11 | There is a tree | 0 | lists fence, gate, path, house, flower bed, can, wheelbarrow; no tree |
| pic_20 | i03 | There are a few white clouds | 0 | "sunny playground", no clouds |
| pic_21 | i04 | There are a few white clouds | 0 | "sunny park", no clouds |

No 0.5 scores and no misreadings.

## Judgement calls scored 1

| Pic | Id | Target | Why it was a call |
|---|---|---|---|
| pic_01 | i03 | watering with a frying pan | "frying pan or saucepan"; either is a pan, not a watering can |
| pic_01 | i04 | child jumping for joy | jumping with a happy face; unsure also offers jumping to reach something |
| pic_02 | i02 | dog wants a walk | two readings (waiting for owner / took the lead itself), both about a walk |
| pic_05 | i01 | man sweeping | "sweep or scrape"; unsure also offers digging into the pile |
| pic_05 | i06 | teenager catching | near word "boy"; "ready to catch" |
| pic_07 | i02 | girl stuck in the air, calling out | stuck is clear; calling out offered beside worry or surprise |
| pic_08 | i01 | dog sleeping | sleeping beside "lying with its head down/sniffing" |
| pic_09 | i01 | dog playing | play bow beside "stretching" |
| pic_11 | i07 | girl throwing bread | "seems to have thrown the bread" (action inferred from result) |
| pic_11 | i09 | duck came to eat the bread | stated as "swimming toward bread pieces"; the food motive is implicit, not spelled out |
| pic_12 | i02 | dog sleeping | sleeping beside "lying with its head down/sad" |
| pic_14 | i02 | bird pecking at sandwich | sandwich beside "just crumbs beside it" |
| pic_15 | i04 | kite got stuck in the tree | stuck beside "just flying low in front of it" |
| pic_15 | i06 | woman running | near word "girl" |
| pic_16 | i01 | dog playing | playful beside "sniffing/nudging the ball" |
| pic_17 | i03 | teenager going to trip | trip implied, but unsure allows "bump into it or walk past it" |
| pic_19 | i07 / i08 | teenager throws, woman catches | throw to the woman beside "she could also be the one who threw it" |
| pic_21 | i02 | grandmother eating ice cream | eating beside "just holding it up to smell/look" |

## Unintended oddities, grouped by kind

**Person floating or detached from a seat (3)**
- pic_03: the girl perches a little above the seesaw plank, possibly floating above the seat
- pic_07: the girl looks a little detached from the seesaw seat, at the very tip of the plank
- pic_20: the girl seems to sit slightly above the chute surface

**Pose or gesture that does not fit the action (1)**
- pic_19: the woman's hands are oddly placed together near her chest rather than out wide to catch

**Prop looks incomplete (1)**
- pic_20: only one swing seat on a frame wide enough for two, possibly a missing seat

**About animals: none.** No unintended oddity was reported about any animal, so the count by angle is 0 for every angle (three-quarter front: 0, profile: 0).

Left out as hedges about small details: pic_10 girl "might look very slightly above" the chute but "reads as normal sliding"; pic_11 goat's tether stake looks short; pic_14 bench partly hidden behind the woman; pic_21 bird might read as a lamp decoration but "looks like a real bird"; pic_02 lead could be a rope toy.
