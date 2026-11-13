# v0.51 picture-description scores (key set a)

26 pictures, 282 scored items. Completeness check: every item id in keys_a.json for pic_01 to pic_26 has exactly one score in scores_a.json. None is missing and none is invented (checked by comparing the id sets of the two files).

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| action | 79 | 1.00 |
| entity | 169 | 0.92 |
| inference | 18 | 1.00 |
| contradiction_notice | 8 | 1.00 |
| contradiction_explain | 8 | 1.00 |
| **all** | **282** | **0.95** |

## Items scored 0, 0.5 or misread

Every one is a 0, and every one is a background entity the describer did not mention. There are no 0.5 scores and no misreads.

| Pic | Id | Target | What the describer said |
|---|---|---|---|
| pic_04 | i04 | There are a few white clouds | no clouds mentioned |
| pic_14 | i07 | There are a few white clouds | no sky or clouds mentioned |
| pic_14 | i08 | There is a tree | no tree mentioned |
| pic_15 | i03 | There are a few white clouds | no clouds mentioned |
| pic_16 | i21 | There are a few white clouds | no clouds mentioned |
| pic_17 | i04 | There are a few white clouds | no clouds mentioned |
| pic_18 | i09 | There are a few white clouds | no clouds mentioned |
| pic_18 | i10 | There is a tree | no tree mentioned |
| pic_19 | i11 | There are a few white clouds | no clouds mentioned |
| pic_20 | i03 | There are a few white clouds | "the sky is clear" |
| pic_20 | i04 | There is a tree | no tree mentioned |
| pic_21 | i03 | There are a few white clouds | no clouds mentioned |
| pic_21 | i04 | There is a tree | no tree mentioned (bushes only) |

Clouds were missed in 9 pictures and a tree in 4.

## Judgement calls scored 1

| Pic | Id | Why it was a call |
|---|---|---|
| pic_01 | i01 | the dog "could be sleeping or just lying with eyes shut", but reads as asleep (target beside another reading) |
| pic_02 | i06 | the kite is "caught", but the unsure section says it could be flying behind the tree (target beside another reading) |
| pic_02 | i07 | the girl holds a slice of bread toward the pond rather than throwing it (near wording) |
| pic_02 | i09 | the duck swims toward the crumbs; the purpose comes only through "she seems to be feeding the duck" |
| pic_03 | i03 | "perhaps because she is stuck up high while the man ignores her": hedged, with no mention of weight (matches the accepted "he isn't noticing") |
| pic_06 | i02 | the dog is "as if asking to go for a walk", or simply carrying the lead (target beside another reading) |
| pic_06 | i03 | planting, or weeding (target beside another reading) |
| pic_07 | i03 | the girl "seems stuck high up while the man reads"; no weight cause given |
| pic_08 | i02 | "man (or older boy)" (target beside another reading) |
| pic_09 | i07, i08 | the square wheels appear only in the unsure section, as "looks odd" |
| pic_10 | i02 | the puppy is asleep, or crouching or creeping (target beside another reading) |
| pic_11 | i04, i05 | the square wheel appears only in the unsure section, as "looks odd" |
| pic_13 | i03 | the dog is begging, or "just sitting up to say hello" (target beside another reading) |
| pic_14 | i04 | the dog is blocking the flow, or the bulge is just a hose connector (target beside another reading) |
| pic_19 | i06 | the balloon slipped away, or she let it go; both convey losing it |
| pic_19 | i08 | the child is running while holding a cone; eating is not stated (accepted phrasing "ice cream cone") |
| pic_21 | i01 | planting, or "digging something out" (target beside another reading) |
| pic_22 | i04 | the puppy is sleeping, sulking or crouching (target beside another reading) |
| pic_23 | i01 | a paint roller that "could be read as a sponge or brush" (near wording) |
| pic_25 | i01 | a rake or a broom (target beside another reading) |

## Unintended oddities (not scored items)

5 oddities across 5 pictures; 21 pictures had none.

**Animal scale or pose (2)**
- pic_10: the puppy is very small next to the girl, reading as far away or a tiny dog [dog, three-quarter front]
- pic_19: the child running with the ice cream looks about to trip over or step on the bird [bird, three-quarter front]

**Out-of-place animal (1)**
- pic_24: a goat tied up in a public park is a little unusual [goat, profile]

**Figure and prop contact (1)**
- pic_07: the man's legs overlap the seesaw board oddly, as if he sits slightly in front of it

**Unexplained action (1)**
- pic_24: the running woman has no clear reason to run; she could be hurrying or fleeing

**Animal oddities by angle**
- three-quarter front: 2 (dog in pic_10, bird in pic_19)
- profile: 1 (goat in pic_24)

Hedges about small details were left out, for example the detached water stream in pic_02, the water drawn in front of the flowers in pic_26, and how far the balloon is from the girl's hand in pic_22.
