# Scores summary, set b (pic_23 to pic_44), v0.48

Completeness check: all 22 pictures in keys_b.json are scored. Every key item got exactly one score: 257 items in the key and 257 in scores_b.json. No item is missing and none was invented. I checked each picture's ids against the key by hand.

## Mean score by item type

| Type | Items | Sum | Mean |
|---|---|---|---|
| entity | 136 | 133.0 | 0.978 |
| action | 78 | 78.0 | 1.000 |
| inference | 21 | 19.5 | 0.929 |
| contradiction_notice | 11 | 11.0 | 1.000 |
| contradiction_explain | 11 | 11.0 | 1.000 |
| **all** | **257** | **252.5** | **0.982** |

No item was scored misread.

## Items scored 0, 0.5 or misread

| Pic | Id | Score | Target | What the describer said |
|---|---|---|---|---|
| pic_23 | i03 | 0.5 | The bird is stealing the sandwich while the man is busy reading | Only "a blue bird on the bench beside him pecks at his sandwich". Neither theft nor the man's inattention is stated. |
| pic_23 | i11 | 0 | There are a few white clouds | Not mentioned. |
| pic_23 | i12 | 0 | There is a tree | Not mentioned. Only "a bush stands by the fence in the middle", which may be the tree read as a bush. |
| pic_24 | i03 | 0 | There are a few white clouds | Not mentioned. |
| pic_34 | i04 | 0.5 | The dog is blocking the water by standing on the hose | "which may be why no water is flowing". The unsure section gives the tap simply being off as the other reading. |
| pic_40 | i04 | 0.5 | The dog is blocking the water by standing on the hose | "which may be pinching it". The unsure section gives the tap being off as the other reading. |

## Judgement calls scored 1

| Pic | Id | Target | Why it was a call |
|---|---|---|---|
| pic_25 | i03 | Bird stealing the sandwich while the grandfather reads | Theft is stated only as "about to steal or peck at", the man's reading is not linked to it, and the unsure section says the bird may just be perched. |
| pic_29 | i16 | Something wrong with what is on the person's head | The bucket is described, but the unsure section also offers "a tall grey hat" (target beside another reading). |
| pic_29 | i17 | Wearing a bucket as a hat | The same alternative "tall grey hat" reading. |
| pic_33 | i08 | A woman sitting and having a drink | Described as a "girl" (near word for the person). |
| pic_34 | i01 | Teenager holding a hose, looking into the nozzle | Holding a hose is stated. Looking into the nozzle and puzzlement are not. |
| pic_35 | i02 | A girl eating an ice cream | Only "holding" a cone, not eating it. |
| pic_36 | i04 | A woman eating an ice cream | Described as a "girl" (near word for the person). |
| pic_40 | i01 | Woman holding a hose, looking into the nozzle | Holding a nozzle is stated. Looking into it and puzzlement are not. |
| pic_40 | i08 | The kite got stuck in the tree | "Stuck" is stated firmly, but the unsure section says it could be flying in front of the tree. |
| pic_40 | i11 | The girl let go of one of the balloons | "As if she has just let it go", but the unsure section says the balloon could be unrelated. |

## Unintended oddities (not scored items), grouped by kind

**Contact, overlap or support looks off (4)**
- pic_24: the girl looks small for how near she is and could be read as hovering just above the slide chute.
- pic_31: the man overlaps the pond's edge outline, so he could look as if he stands partly in front of or in the water.
- pic_39: the paint roller does not quite touch the fence beside the painted section.
- pic_40: the kite seems partly behind or inside the foliage, with lighter leaf blobs overlapping it.

**Object standing unsupported (1)**
- pic_25: the bicycle stands upright on its own, with no rider or kickstand clearly visible.

**Incomplete object (1)**
- pic_24: the swing set has only one seat, as if a second is missing.

**Physical inconsistency (1)**
- pic_26: the boy's cap stays firmly on in the strong wind while the man's blows off.

**Framing or cropping (1)**
- pic_35: the dog is cut off slightly at the bottom edge of the picture [dog, profile].

**Oddities about animals, counted by angle:** profile 1 (pic_35 dog), three-quarter front 0.
