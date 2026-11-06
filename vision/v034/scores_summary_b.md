# Scores summary, set B (pic_28 to pic_55)

Scored from desc_pic_28.md to desc_pic_55.md against keys_b.json. Per-item scores and evidence are in scores_b.json.

## Mean score by item type

| Item type | Items | Mean score |
|---|---:|---:|
| entity | 176 | 1.00 |
| action | 76 | 1.00 |
| inference | 16 | 1.00 |
| contradiction_notice | 7 | 1.00 |
| contradiction_explain | 7 | 1.00 |
| **all items** | **282** | **1.00** |

## Items scored 0, 0.5 or misread

None. Every one of the 282 items was mentioned with the right meaning somewhere in its description file.

### Credited 1, but with a reservation

These items scored 1 because the free description commits to the target reading. In each case, though, the "unsure" section offers an alternative, or a part of the target is missing. If you want a stricter count, these are the items to drop to 0.5.

| Pic | Id | Target | Reservation |
|---|---|---|---|
| pic_45 | i03 | Bird stealing the sandwich while the man reads | "apparently about to take it", but the unsure section adds "or just sitting next to it". The describer never says the man fails to notice. |
| pic_49 | i09 | Child let go of one balloon | "seems to be floating away", but the unsure section also offers "him still (almost) holding it". |
| pic_54 | i04 | Cat about to catch the bird | "as if about to pounce", but the unsure section also offers "or just walking past it". |
| pic_55 | i02 | Dog wants to go for a walk | "as if asking to go for a walk", but the unsure section also offers "or just sitting there with the lead". |
| pic_52 | i04 | Cat about to catch the bird | Pounce is the preferred reading. The describer adds "could also just be walking/playing". |
| pic_49 | i06 | Teenager will trip over the box | "looks like he might trip". The describer notes his walking direction is not completely clear. |
| pic_54 | i03 | Bird pecking at the ground | Described as "standing on the pavement". Pecking is never described, but "bird" alone is an accepted phrasing. |
| pic_45 | i07 | Child reaching for a balloon, upset | Reaching up with balloons, but "upset" is not mentioned. |
| pic_49 | i07 | Child reaching for a balloon, upset | Reaching up with balloons, but "upset" is not mentioned. |
| pic_31 | i01 | Man planting flowers | "as if he is about to plant it" and "gardening scene". The unsure section says planting vs tending is unclear. |
| pic_32 | i01 | Grandmother sitting with a drink | An "elderly person". The describer can't tell if it is an old woman or an old man. |
| pic_34 | i05 | Teenager jumping for joy | Jumping for joy is the main reading. The alternative is reaching toward the cat. |

## Unintended oddities (not scored items), grouped by kind

There are 8 in total, across 7 pictures. The other 21 pictures have none.

**Motion or wind drawn inconsistently**
- pic_30: The swing ropes hang straight down (at rest), but motion lines say the swing is moving.
- pic_40: The swing chains hang straight down, but motion lines show the toddler swinging.
- pic_38: The wind blows the cap and the washing sideways, yet the woman's leaf pile stays put and her hair and dress don't move.

**Season inconsistent**
- pic_43: Fallen leaves are autumn-coloured, but the trees are fully green and the flowers are blooming.

**Action with no visible reason**
- pic_45: The woman in yellow runs fast, but nothing is ahead of her or behind her.

**Situation implausible**
- pic_40: The toddler looks too small to be alone on the swing, and nobody seems to be watching her (the older man is reading).
- pic_39: A goat grazing in an ordinary house garden is "slightly unexpected".

**Pose awkward**
- pic_36: The man's crossed-leg pose while sitting on the seesaw plank looks a little awkward.

Some hedges were left out on purpose because they are about small details. They are: people's walking direction (pic_44, pic_49, pic_54), slight overlaps (the man and the flower bed in pic_34, the ladder rail and the path in pic_35), how the cat is lying (pic_48, pic_51), and who someone is looking at or waving to (pic_42, pic_47, pic_54).

## Completeness check

A script checked scores_b.json against keys_b.json:
- The same 28 pictures (pic_28 to pic_55) are in both files.
- All 282 key items have exactly one score each: 176 entity, 76 action, 16 inference, 7 contradiction_notice, 7 contradiction_explain.
- No item is missing and none is invented.
- Every score is 0, 0.5, 1 or "misread".
- No picture lists more than three unintended oddities.
