# v0.54 picture-description scores (key A)

Coverage check: all 25 pictures in keys_a.json are in scores_a.json, and every one of the 269 key items has exactly one score. No item is missing and none was added; the item ids match the key in order for every picture.

## Mean score by item type

| Type | Items | Sum | Mean |
|---|---|---|---|
| entity | 161 | 150 | 0.932 |
| action | 76 | 76 | 1.000 |
| inference | 18 | 18 | 1.000 |
| contradiction_notice | 7 | 7 | 1.000 |
| contradiction_explain | 7 | 7 | 1.000 |
| **all** | **269** | **258** | **0.959** |

## Items scored 0, 0.5 or misread

There are no 0.5 scores and no misreads. All 11 zeros are background entities.

| Pic | Id | Target | What the describer said |
|---|---|---|---|
| pic_15 | i21 | There are a few white clouds | Not mentioned (only "sunny town square") |
| pic_16 | i04 | There are a few white clouds | Not mentioned (only "sunny town square") |
| pic_18 | i07 | There are a few white clouds | Not mentioned (only "sunny park") |
| pic_19 | i04 | There are a few white clouds | Not mentioned (only "sunny park") |
| pic_20 | i07 | There are a few white clouds | Not mentioned (only "sunny playground") |
| pic_21 | i11 | There are a few white clouds | Not mentioned (only "busy sunny park") |
| pic_22 | i10 | There are a few white clouds | Not mentioned (only "sunny back garden") |
| pic_23 | i04 | There are a few white clouds | Not mentioned (only "sunny park") |
| pic_24 | i03 | There are a few white clouds | Not mentioned (only "sunny back garden") |
| pic_25 | i06 | There are a few white clouds | Not mentioned (only "sunny back garden") |
| pic_25 | i07 | There is a tree | Not mentioned; the setting lists fence, house, path, gate, plants and flower bed, but no tree |

Pattern: clouds are named in every description from pic_01 to pic_14 and in pic_17. They are left out in pic_15, pic_16 and every picture from pic_18 to pic_25.

## Judgement calls scored 1

| Pic | Id | Why it was a call |
|---|---|---|
| pic_02 | i02 | Dog "apparently resting or asleep", but "sniffing the ground" is offered as a second reading |
| pic_05 | i03 | Inference credited from "swims towards the crumbs and pecks at them" (eating the bread). The duck's wish for the bread is not stated in so many words |
| pic_18 | i03 | Same as pic_05: swims toward the crumbs and pecks at them |
| pic_07 | i02 | Hand at mouth read as calling out or worried. Both are accepted meanings, but they are given as alternatives |
| pic_13 | i02 | Same as pic_07: worried or surprised, with calling out as an alternative |
| pic_08 | i06 | Teenager described as "a boy in a red cap" (near word) |
| pic_08 | i07 | Woman "ready to catch it", with waving or clapping offered as alternatives (catching judged best) |
| pic_11 | i04 | Dog "seems to be blocking the water", with the alternative that it is just standing near the hose |
| pic_22 | i04 | Same as pic_11: "seems to be why the water is blocked", with the alternative that it is just next to the hose |
| pic_11 | i05 | The woman is described as "a girl in a yellow dress" (age misread). The action, sitting and drinking, is correct |
| pic_12 | i05 | Teenager described as "a boy" |
| pic_14 | i03 | Teenager described as "a boy" |
| pic_15 | i19 | Teenager described as "a boy" |
| pic_20 | i05 | Teenager described as "a boy" |
| pic_15 | i04 | The ball is "stuck in the branches", but the describer does not say it is the girl's ball |
| pic_21 | i03 | Frying pan read as "a cooking pot or saucepan" (near word). The point, a pan used instead of a watering can, is stated |

## Unintended oddities (not scored items), grouped by kind

**Figures overlapping the pond outline (3):**
- pic_18: the woman overlaps the pond outline and could look as if she is standing in the water
- pic_19: the woman's body overlaps the pond outline
- pic_21: the man and the woman in yellow overlap the pond outline

**Odd placement or pose (3):**
- pic_09: the lamppost stands alone in open grass, slightly odd
- pic_09: the woman walks on the grass rather than on the path
- pic_17: the boy sits slightly behind the seesaw beam rather than squarely on top of it

**Props and colours (2):**
- pic_25: the woman's arms and the roller pole look awkward; the pole looks short for a roller
- pic_25: the house door is the same blue as the paint, as if she painted it too

**About animals (3):**
- pic_12: the dog's own paws look mostly white although it left blue paw prints [dog, profile]
- pic_05: a goat in a public park with a pond is slightly unexpected [goat, profile]
- pic_21: the running child is very close to the bird and might run into it [bird, three-quarter front]

Animal oddities by angle: profile 2 (dog, goat), three-quarter front 1 (bird).

Pictures with no unintended oddity: 01, 02, 03, 04, 06, 07, 08, 10, 11, 13, 14, 15, 16, 20, 22, 23, 24.
