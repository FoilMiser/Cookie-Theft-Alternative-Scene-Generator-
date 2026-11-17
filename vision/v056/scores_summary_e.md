# v0.56 description scores, key E (pic_101 to pic_126)

Coverage check: keys_e.json has 26 pictures and 262 items. scores_e.json scores every one of them exactly once. No item is missing and none is invented (the item ids match the key for every picture).

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 164 | 1.000 |
| action | 70 | 1.000 |
| inference | 12 | 1.000 |
| contradiction_notice | 8 | 1.000 |
| contradiction_explain | 8 | 0.938 |
| **All** | **262** | **0.998** |

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---|---|
| pic_114 | i03 | The person is watering the flowers with a frying pan instead of a watering can | 0.5 | Free description and inventory call it a (dark grey) watering can. The unsure section says it "looks odd", held by a long thin handle "like a frying pan or ladle", and "could be read as a pan or a scoop rather than a watering can". The pan reading is only offered as an alternative. |

No item was scored 0 or misread.

## Judgement calls scored 1

| Pic | Id | Target | Why it was a call |
|---|---|---|---|
| pic_102 | i02 | The dog wants to go for a walk | Stated ("as if asking to be taken for a walk"), but the unsure section adds "or simply holding it". |
| pic_106 | i01 | A man is painting the fence | Near word: "a boy". |
| pic_106 | i05 | A woman is reading while walking | Near word: "a girl". |
| pic_106 | i07 | The woman is going to trip over a bucket | Stated, but the unsure section adds that the bucket "might be just off to her side". |
| pic_107 | i02 | A man is sweeping | "a man (or older boy)": target beside another reading. |
| pic_107 | i06 | There is a bird feeder | Near word: "bird box". |
| pic_108 | i04 | A woman is walking a dog | "a woman or girl": target beside another reading. |
| pic_109 | i01 | A teenager is watering the flowers | Near word: "a boy". |
| pic_110 | i03 | The kite got stuck in the tree | Stated ("stuck in the branches"), but the unsure section adds "or flying just in front of the tree" (stuck called most likely). |
| pic_110 | i05 | A woman is walking a dog | "a woman or girl": target beside another reading. |
| pic_111 | i02 | A teenager is carrying a shopping bag | Near word: "a boy". |
| pic_112 | i01 | A woman is watering the flowers with a hose | "a woman or girl": target beside another reading. |
| pic_112 | i05 | There is a bird feeder | Near word: "bird box". |
| pic_114 | i01 | A teenager is watering the flowers | Near word: "a boy". |
| pic_114 | i02 | Something is wrong with what the person is watering with | Noticed only in the unsure section ("looks odd"). |
| pic_115 | i01 | A man is carrying a shopping bag | "a man (or teenage boy)": target beside another reading. |
| pic_116 | i02 | A girl is catching the ball | Stated twice ("ready to catch"), but the unsure section says the pose "could equally be read as reaching or waving". |
| pic_117 | i02 | A man is eating an ice cream | "a man or boy": target beside another reading. |
| pic_118 | i03 | The duck has come to eat the bread | Conveyed by "swimming toward the crumbs" and bread dropped "for a white duck"; the duck's motive is not stated in so many words. |
| pic_119 | i02 | A bird is pulling a slice of bread off a sandwich | Bird is beside the sandwich "about to peck or steal it", not yet pulling bread off. |
| pic_119 | i03 | The bird is stealing the sandwich while the woman is busy reading | "About to steal" next to the reading woman; not said to be happening already, and her not noticing is left implied. |
| pic_119 | i09 | The child let go of one of the balloons | "has escaped" and he reaches after it, but the unsure section adds "or someone else's balloon drifting past". |
| pic_119 | i16 | A teenager is running | Near word: "a boy". |

## Unintended oddities, by kind

Contact, overlap or a part that seems to go through something (6)
- pic_113: the boy's hand and knee merge into a dark blob at the seesaw handle; hard to tell where his arm ends
- pic_114: the kite string passes very close to the digging man and nearly touches him
- pic_115: the man's leg seems to pass behind or through the bicycle frame
- pic_117: the goat's rope crosses in front of its front leg; unclear whether it wraps around the leg [goat, three-quarter front]
- pic_118: the man's lower body overlaps the pond's edge; he could be partly in the water
- pic_120: the girl on the high end seems to hover slightly above the seesaw board

Scale (2)
- pic_113: the girl is much smaller than the boy for how high up she sits
- pic_119: the sandwich on the bench is very large compared to the woman

Pose that does not fit the action (2)
- pic_116: the girl's arms point toward the boy rather than up at the ball
- pic_116: the ball is very high for the girl to catch

Direction of motion (1)
- pic_126: the cap flies ahead of the wind lines, so the wind seems to blow the wrong way

Object in the wrong place (1)
- pic_118: one crumb sits on the sand rim or grass, outside the pond

Unexpected presence (1)
- pic_103: a goat in a park is the one odd thing (it is tethered) [goat, three-quarter front]

Total: 13 oddities across 9 pictures; 17 pictures had none.

### Oddities about animals, by angle

| Angle | Count | Oddities |
|---|---|---|
| three-quarter front | 2 | pic_103 goat in a park; pic_117 goat's rope across its leg |
| profile | 0 | none |
