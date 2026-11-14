# v0.55 picture-description scores (key set a)

25 pictures, 269 scored items. Every item in keys_a.json has exactly one score in scores_a.json. I checked this per picture against the key's id lists and per type against the key's counts (76 action, 161 entity, 18 inference, 7 contradiction_notice, 7 contradiction_explain). No item is missing and none is invented. There were no misreads.

## Mean score by item type

| Type | Items | Sum | Mean |
|---|---|---|---|
| action | 76 | 76 | 1.00 |
| entity | 161 | 155 | 0.96 |
| inference | 18 | 18 | 1.00 |
| contradiction_notice | 7 | 7 | 1.00 |
| contradiction_explain | 7 | 7 | 1.00 |
| **all** | **269** | **263** | **0.98** |

## Items scored 0, 0.5 or misread

All six are background entities the describer did not mention (score 0). There were no 0.5 scores and no misreads.

| Pic | Id | Target | What the describer said |
|---|---|---|---|
| pic_18 | i07 | There are a few white clouds | Clouds not mentioned. "Sunny park" only. |
| pic_21 | i11 | There are a few white clouds | Clouds not mentioned. "Busy sunny park" only. |
| pic_22 | i10 | There are a few white clouds | Clouds not mentioned. "Sunny back garden" only. |
| pic_22 | i11 | There is a tree | Tree not mentioned. Lists house, fence, gate, clothesline, flower bed, bench, hose reel. |
| pic_24 | i03 | There are a few white clouds | Clouds not mentioned. "Sunny back garden" only. |
| pic_24 | i04 | There is a tree | Tree not mentioned. |

## Judgement calls scored 1

- pic_02 i02 (dog sleeping): the free text says "apparently resting or asleep". The unsure section adds a second reading, crouching or creeping. The main reading is the target.
- pic_03 i01 / i03 (watering, water going up): it says "watering (or trying to water)". The unsure section adds a second reading, a blue hose or sprayer, but says it "looks wrong either way". The free text states plainly that the water shoots upward.
- pic_05 i03 and pic_18 i03 (duck came to eat the bread): the describer says the duck swims toward the crumbs and pecks at them. That matches the accepted phrasing "the duck is eating the bread", but it is close to describing what is visible rather than stating an intention.
- pic_07 i01 and pic_13 i01 (grandfather on the low end): the target is given, but the unsure section says he might be sitting on the ground in front of the seesaw end.
- pic_08 i04 (kite stuck): the target is given, with a second reading in the unsure section: the kite may be flying low in front of the tree.
- pic_08 i07 (woman catching): it says "ready to catch". The unsure section adds that she may be waving or reacting.
- pic_08 i06, pic_12 i05, pic_14 i03, pic_15 i19 (teenager): the describer calls him a "boy in a red cap" (near word). The actions were all correct.
- pic_11 i04 (dog blocking the water): the free text states it as the cause ("which is why the water is blocked"). The unsure section adds a second reading: the hose is just turned off.
- pic_11 i05 (woman sitting and drinking): the describer calls her a "girl" in a yellow dress (near word). The action was correct.
- pic_15 i07 (cat about to catch the bird): it says "as if about to pounce". The unsure section adds a second reading: the cat may just be walking past.
- pic_15 i16 (notice: odd thing on the head): the only notice word is "which is silly". It counts because the explanation (a bucket worn as a hat) is given.
- pic_21 i06 (girl let go of a balloon): it says "likely escaped from her hand, though it is not certain".
- pic_22 i04 (dog blocking the water): it says "may be why no water comes out". The unsure section adds a second reading: the dog's position may be an accident of placement.
- pic_22 i08 (child jumping for joy): it says "appears happy". The unsure section adds a second reading: the boy may be about to be sprayed.

## Unintended oddities, grouped by kind

**People and props overlapping in the wrong depth or at the wrong height (5)**
- pic_05: the man's upper body overlaps the pond, so at a glance he looks as if he is standing in the water.
- pic_18: the woman's upper body and hands overlap the pond, so she looks as if she is standing over the water.
- pic_07: the man's legs sit across or in front of the seesaw plank, so it is unclear whether he is on the seesaw or on the ground.
- pic_13: the man sits almost at ground level beside the seesaw end, as if on the grass rather than the seat.
- pic_21: the trail of seeds seems to curve on behind the bird toward the boy's feet.

**Drawing detail that can be misread (2)**
- pic_08: lighter leaf clumps in the tree canopy look like small bushes inside the tree.
- pic_25: the paw prints are spaced oddly in small clusters and could be mistaken for spilled paint drops.

**Unscored story or setting oddities (2)**
- pic_21: the boy is running straight at the bird and seems about to trip over it or scare it away [bird, three-quarter front].
- pic_05: a goat tethered in a town park is a little unusual [goat, profile].

**Oddities about animals, counted by angle**
- profile: 1 (goat, pic_05)
- three-quarter front: 1 (bird, pic_21)

Eighteen pictures had no unintended oddities (pic_01, 02, 03, 04, 06, 09, 10, 11, 12, 14, 15, 16, 17, 19, 20, 22, 23, 24).
