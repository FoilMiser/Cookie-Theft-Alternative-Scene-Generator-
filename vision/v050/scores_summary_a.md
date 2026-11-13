# v0.50 picture-description scores (key set a)

Completeness check: all 280 items in 23 pictures of keys_a.json have exactly one score in scores_a.json. No item is missing and none was invented. I checked this by matching ids per picture.

## Mean score by item type

| Type | Items | Sum | Mean |
|---|---|---|---|
| action | 89 | 88.5 | 0.994 |
| entity | 146 | 128 | 0.877 |
| inference | 21 | 20 | 0.952 |
| contradiction_notice | 12 | 12 | 1.000 |
| contradiction_explain | 12 | 12 | 1.000 |
| **all** | **280** | **260.5** | **0.930** |

No item was scored "misread".

## Items scored 0, 0.5 or misread

### 0.5
| Pic | Id | Target | What the describer said |
|---|---|---|---|
| pic_04 | i03 | The bird is stealing the sandwich while the grandfather is busy reading | "pecking at (or stealing)"; unsure section: stealing while he is distracted, or he may be sharing it |
| pic_11 | i02 | The dog is standing on the hose | "a back paw on or beside the hose"; unsure: not clear whether the paw is on the hose |
| pic_11 | i04 | The dog is blocking the water by standing on the hose | "looks as if the dog is stopping the water", but the unsure section gives reading 2: the bulge is a hose fitting and the dog just stands next to it |

### 0 (all "There are a few white clouds", 18 items)
The describer never mentioned clouds. Where the picture was sunny they said "sunny" only.

| Pic | Id |
|---|---|
| pic_02 | i07 |
| pic_03 | i05 |
| pic_05 | i07 |
| pic_07 | i13 |
| pic_08 | i04 |
| pic_09 | i07 |
| pic_10 | i21 |
| pic_11 | i06 |
| pic_12 | i09 |
| pic_13 | i05 |
| pic_14 | i21 |
| pic_16 | i07 |
| pic_17 | i10 |
| pic_18 | i07 |
| pic_19 | i05 |
| pic_20 | i03 |
| pic_21 | i03 |
| pic_23 | i04 |

Clouds were credited only in pic_01 ("a few white clouds") and pic_06 (dark storm clouds).

## Judgement calls scored 1

| Pic | Id | Target | Why it was a call |
|---|---|---|---|
| pic_02 | i01 | Teenager planting flowers | Digging with a trowel beside a potted flower, "as if he is about to plant it"; also offered: weeding |
| pic_02 | i04 | Box floating with nothing holding it up | They say nothing holds it up and that floating would be impossible, but also offer "thrown and falling" |
| pic_04 | i09 | Cat about to catch the bird | Hedged: "may be about to pounce"; "stalking" is in the inventory |
| pic_04 | i13 | Child dropped the ice cream | Near word: "has fallen on the grass", without saying the child dropped it |
| pic_06 | i12 | Man pointing up at the sky | Pointing at the bird on the lamp post, or at the clouds |
| pic_09 | i04 | Dog blocking the water | States "blocking the water"; the unsure section says the bulge could be a fitting |
| pic_10 | i11 | Child dropped the ice cream | Hedged in the unsure section ("crying because the ice cream fell or something else"), with the drop favoured |
| pic_14 | i03 | Bird stealing the sandwich while the woman reads | "without her noticing"; the unsure section adds "or just perched on the bench" |
| pic_14 | i10 | Child dropped the ice cream | Near word: "spilled on the ground" |
| pic_15 | i07 | Woman catching the ball | "ready to catch", or clapping |
| pic_16 | i04 | Kite got stuck in the tree | "reads as stuck", or it may be flying behind the tree |
| pic_17 | i08 | Child jumping for joy | Jumping/cheering, or reacting to the wet box or the dog |
| pic_18 | i02 | Man watering the flowers | Holds a watering can over the flower bed but is not said to be watering; the water rises instead |
| all | - | "teenager" agents (pic_02, 03, 04, 07, 10, 14, 15, 16, 18, 21) | The describer always says "boy" (red cap, blue hoodie); the action was credited |

## Unintended oddities (not scored items)

Only three were reported, each in a different picture. None of them is about an animal, so there is no count by angle (all animal angles: 0).

- **Rendering or drawing problems (2)**
  - pic_17: the boy's shadow is detached from his feet (he is either mid-jump or the shadow is offset).
  - pic_18: the upward water stream looks like a thin hose or wand attached to the can, possibly a drawing error.
- **Unexplained prop placement (1)**
  - pic_10: the red bird's seeds lie by the cat, far from the boy, and it is unclear where they came from. The oddity is about where the seeds came from, not about the bird itself, so it has no angle tag.

Describers also said "nothing looks unintentionally strange" in pic_01, 03, 08, 19, 20, 21, 22 and 23. Hedges about small details were left out: the seesaw being nearly level (pic_19, pic_23), how much of the fence is painted and where the paint tin sits (pic_21), and whether the red tool is a spade or a bucket (pic_22).
