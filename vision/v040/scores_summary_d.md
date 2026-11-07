# Scores summary, set D (pic_72 to pic_94)

Sources: `desc_pic_72.md` to `desc_pic_94.md`, scored against `keys_d.json`. Per-item scores and evidence are in `scores_d.json`.

Coverage check: keys_d.json has 23 pictures and 241 items. scores_d.json has exactly one score for each of those 241 items. A script compared the two files id by id: no item is missing, no item is invented, and no id is duplicated.

## Mean score by item type

| Item type | Items | Mean score |
|---|---:|---:|
| entity | 145 | 1.00 |
| action | 67 | 1.00 |
| inference | 15 | 1.00 |
| contradiction_notice | 7 | 1.00 |
| contradiction_explain | 7 | 1.00 |
| **all** | **241** | **1.00** |

## Items scored 0, 0.5 or misread

None. Every item scored 1.

Some items were credited at 1 even though the describer hedged or gave a second reading in the "unsure" section, because the free description states the target reading:

| Pic | Id | Target | What the describer said |
|---|---|---|---|
| pic_72 | i03 | The water is going up into the air instead of falling down | The stream "rises up... as if the water were flowing uphill". The unsure section adds a second reading (water falling from above) but calls the upward reading the most natural. |
| pic_75 | i03 | The cat is about to catch the bird | "It looks as though the cat is about to pounce on the bird". The unsure section says the pose could also be walking or running. |
| pic_85 | i10 | The woman is going to trip over a box | "so she may be about to trip over it". The unsure section says she may pass beside it instead. |
| pic_91 | i06 | The teenager is going to trip over a box | "he looks about to bump into or trip over it". The unsure section says he may pass beside it. |
| pic_91 | i11 | A grandmother is pointing up at the sky | "pointing up toward the sky". The unsure section says she could be pointing at the red bird instead. |

## Unintended oddities (not scored items)

There are 11 oddities across 9 pictures. The other 14 pictures have none.

### Animal pose or shape hard to read (4)
- pic_75: the cat's legs are bunched up and hard to separate, so the crouch could read as walking or running [cat, three-quarter front]
- pic_79: the begging dog is stretched upright with its head tilted far back, so its shape looks odd and awkward; it could read as jumping up [dog, profile]
- pic_89: the dog's head is small and turned partly away, so it is hard to tell which way it faces (toward the boy or the man) [dog, profile]
- pic_89: the dog's upright sitting pose looks a little stiff and human-like [dog, profile]

### Animal out of place, with no owner (2)
- pic_73: a goat is loose in a public park with no owner or lead [goat, profile]
- pic_78: a goat is in a back garden with no owner or tether [goat, three-quarter back]

### Figure merging with a prop (1)
- pic_94: the man sits in front of the seesaw beam rather than on it; the beam runs behind or across his thighs, so he looks merged with it

### Odd object layout (2)
- pic_74: the swing frame has only one seat, hung off to the left, so most of the frame is empty
- pic_89: the street lamp stands in the middle of the grass rather than beside the path

### Gesture target unclear (1)
- pic_91: it is unclear what the grandmother is pointing at. Her finger points up and to the right, toward the sky, but the red bird on the lamp post is up and to her left.

### Mood does not match the weather (1)
- pic_91: the girl jumping for joy and the man eating ice cream look out of place under dark storm clouds

### Animal oddities by angle

| Angle | Count | Which |
|---|---:|---|
| profile | 4 | dog x3 (pic_79, pic_89 x2), goat x1 (pic_73) |
| three-quarter front | 1 | cat (pic_75) |
| three-quarter back | 1 | goat (pic_78) |

By animal: dog 3 (all profile, all in the sitting-up begging pose, pic_79 and pic_89), goat 2, cat 1. There were no oddities about the birds or the duck.
