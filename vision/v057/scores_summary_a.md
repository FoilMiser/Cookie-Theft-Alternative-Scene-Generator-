# Scores summary (set a, v057)

Check: all 27 pictures in keys_a.json are scored. Every key item has exactly one score. No item is missing and none was invented (292 items, matched by id per picture).

## Mean score by item type

| Type | Items | Sum | Mean |
|---|---|---|---|
| action | 83 | 83 | 1.000 |
| entity | 174 | 162 | 0.931 |
| inference | 17 | 17 | 1.000 |
| contradiction_notice | 9 | 9 | 1.000 |
| contradiction_explain | 9 | 9 | 1.000 |
| **all** | **292** | **280** | **0.959** |

## Items scored 0, 0.5 or misread

No items were scored 0.5 or misread. All 12 zeros are background entities:

| Pic | Id | Target | What the describer said |
|---|---|---|---|
| pic_12 | i06 | There are a few white clouds | no clouds mentioned (only "sunny") |
| pic_14 | i07 | There are a few white clouds | no clouds mentioned |
| pic_15 | i06 | There are a few white clouds | no clouds mentioned |
| pic_16 | i05 | There are a few white clouds | no clouds mentioned |
| pic_17 | i07 | There are a few white clouds | no clouds mentioned |
| pic_17 | i08 | There is a tree | no tree mentioned (only potted plants) |
| pic_18 | i06 | There are a few white clouds | no clouds mentioned (only wind lines) |
| pic_19 | i06 | There are a few white clouds | no clouds mentioned |
| pic_19 | i07 | There is a tree | no tree mentioned |
| pic_20 | i07 | There are a few white clouds | no clouds mentioned |
| pic_21 | i06 | There are a few white clouds | no clouds mentioned |
| pic_23 | i11 | There are a few white clouds | no clouds mentioned |

## Judgement calls (score 1)

| Pic | Id | Call | Why |
|---|---|---|---|
| pic_03 | i03 | two | the bird takes the sandwich and she has not noticed, but the unsure section says it may just be pecking |
| pic_09 | i03 | two | the girl is stuck because he is heavier, but the unsure section says he may be teasing her on purpose |
| pic_10 | i05 | two | the balloon escaped from her, but the unsure section says it could be caught or tied behind the fence |
| pic_15 | i03 | two | the girl is stuck because he is heavier, but the unsure section says he may keep her up on purpose |
| pic_17 | i03 | two | the cat is about to pounce, but the unsure section says it may be just playing |
| pic_19 | i03 | two | the balloon escaped and she lost it, but the unsure section says it may never have been hers |
| pic_21 | i03 | two | the kite is stuck, but the unsure section says the child may be about to launch it |
| pic_23 | i04 | two | the ball is stuck, but the unsure section says it may be caught mid-fall |
| pic_27 | i03 | two | the parcel is getting wet, but the unsure section says this may be an incidental detail |
| pic_22 | i02 | near | the ice-cream eater is called a "boy", which is not among the man's names |
| pic_24 | i02 | near | the girl is on the raised end, but is not described as stuck or calling out |
| pic_24 | i03 | near | says the tilt "makes sense because he is much heavier", but not that she is stuck; framed as normal |

## Unintended oddities, grouped by kind

**Animal hard to recognise or odd-looking (4)**
- pic_03: the blue bird on the bench is very large for a bird [bird, profile]
- pic_03: the small red bird could be read as a red object or fruit [bird, profile]
- pic_08: the small dark blue bird could be read as a small object [bird, profile]
- pic_13: the goat could be a sheep [goat, three-quarter front]

**Out-of-place element (1)**
- pic_13: a tethered goat in a city-style park is a little unusual [goat, three-quarter front]

**Figure placement / contact (1)**
- pic_07: the girl sits slightly above the see-saw seat, a bit off the board

**Prop placement that confuses the scene (2)**
- pic_04: an unused watering can stands right beside the man watering with a pan
- pic_26: the ladder stands where a lamp post would be; unclear whether a lamp post is meant to be missing

**Animal oddities by angle**
- profile: 3 (all birds: pic_03 x2, pic_08)
- three-quarter front: 2 (goat: pic_13 x2)
