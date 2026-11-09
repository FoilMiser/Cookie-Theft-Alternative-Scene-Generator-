# v0.44 description scoring, set B (pic_22 to pic_42)

Scored from `desc_pic_22.md` … `desc_pic_42.md` against `keys_b.json`. Scores are in `scores_b.json`.

**Completeness check:** all 21 pictures and all 225 key items have exactly one score each. No item is missing, none is invented, and no item id is duplicated. This was checked by script against `keys_b.json`. No picture has more than three unintended oddities.

## Mean score by item type

| Type | Items | Mean | Scored 1 | Scored 0.5 | Scored 0 | Misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 126 | 1.000 | 126 | 0 | 0 | 0 |
| action | 70 | 0.986 | 68 | 2 | 0 | 0 |
| inference | 17 | 0.971 | 16 | 1 | 0 | 0 |
| contradiction_notice | 6 | 1.000 | 6 | 0 | 0 | 0 |
| contradiction_explain | 6 | 1.000 | 6 | 0 | 0 | 0 |
| **all** | **225** | **0.993** | 222 | 3 | 0 | 0 |

## Items scored 0, 0.5 or misread

No item was scored 0 or misread. Three items got 0.5:

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---:|---|
| pic_23 | i03 | inference | The bird is stealing the sandwich while the man is busy reading | 0.5 | The blue bird "looks about to take or peck at the sandwich". It "could be read as about to steal it or just perching", so the theft is one of two readings. The man not noticing is never stated. |
| pic_23 | i19 | action | A grandfather is taking a photo | 0.5 | He holds "a camera (or binoculars)" to his face and is "watching or photographing" something, so the photo is one of two readings. |
| pic_32 | i04 | action | A girl is eating an ice cream | 0.5 | She holds "something small and white up to her mouth". The describer offers three readings (a dandelion seed-head, "a sweet or snack she is eating", or a flower she is smelling) and never names ice cream. |

Hedged items that still scored 1:
- pic_23 i09: "seems to have just let it go", or he is reaching to grab it again. Either way the balloon got away.
- pic_36 i04: "holding up a small pink ice-cream cone", but it is unclear whether the child is eating it or carrying it. The key accepts "ice cream cone".
- pic_41 i02: "about to plant it", or he is weeding or picking flowers.

## Unintended oddities (not scored items), by kind

7 oddities in 6 pictures. The other 15 pictures have none.

**Animal drawing (3)**
- pic_24: an unidentifiable small white shape at the cat's chest/front paws. It could be a paw, a bib marking or something in its mouth. [cat, profile]
- pic_36: the dog's begging pose looks "a bit squashed and compact". [dog, three-quarter front]
- pic_37: the dog's face is turned to the viewer with its eyes closed (it could read as a grin) while its body points left. [dog, three-quarter front]

Animal oddities by angle:

| Angle | Count | Animals |
|---|---:|---|
| three-quarter front | 2 | dog (pic_36), dog (pic_37) |
| profile | 1 | cat (pic_24) |

**Play equipment drawing (2)**
- pic_27: the man sits partway along the seesaw beam rather than on a seat at the end, which "looks a bit odd for a seesaw".
- pic_38: the swing's frame and ropes are "a little hard to separate", and the seat hangs displaced to the right of the top bar.

**Figure placement / overlap (1)**
- pic_28: the fishing woman stands back from the bank on the grass, yet she slightly overlaps the end of the pond.

**Figure pose / direction (1)**
- pic_36: the child's walking direction can't be read. The face is turned left and the feet are spread, so the child could be walking either way.

**Left out as hedges about small details.** In each of these the describer raised the point and then said it reads as normal:
- pic_22: the hose runs close to the woman's leg, but "does not look like it passes through her".
- pic_31: the cap hangs in the air, but the wind lines show it is being blown.
- pic_34: the fishing woman's body overlaps the pond outline, but her feet are on the grass. This is the same overlap as pic_28.
- pic_35: the ball's arc touches the birdhouse pole, but the ball is "probably just passing in front of it".
- pic_40: the foreground is large, empty grass and the scene "feels sparse".
- pic_41: the kneeling man looks a little as if he is inside the flower bed's edge, but this "reads as normal overlap". The white mark at the old man's mouth is "probably a moustache" but might be a pipe.
