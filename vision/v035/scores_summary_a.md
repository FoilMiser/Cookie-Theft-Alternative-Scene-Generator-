# Picture-description scores, set A (v0.35)

Scored from desc_pic_01.md to desc_pic_27.md against keys_a.json only. Scores: 1 = clearly mentioned with the right meaning, 0.5 = partly or only one of two readings, 0 = not mentioned, misread = mentioned but read as something else (counted as 0 in the means).

## Coverage check

Checked by script against keys_a.json: all 27 pictures present, 304 items scored, every key item has exactly one score in key order, no item missing, no item invented, no duplicate ids, every score is 1, 0.5, 0 or misread. No picture has more than three unintended oddities.

## Mean score by item type

| Type | Items | Mean | 1 | 0.5 | 0 | misread |
|---|---|---|---|---|---|---|
| entity | 175 | 0.943 | 165 | 0 | 10 | 0 |
| action | 86 | 0.994 | 85 | 1 | 0 | 0 |
| inference | 19 | 0.974 | 18 | 1 | 0 | 0 |
| contradiction_notice | 12 | 1.000 | 12 | 0 | 0 | 0 |
| contradiction_explain | 12 | 1.000 | 12 | 0 | 0 | 0 |
| **all** | 304 | 0.964 | 292 | 2 | 10 | 0 |

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_01 | i02 | action | The dog is standing on the hose | 0.5 | dog 'standing on or right beside the hose'; unsure whether it is on it |
| pic_01 | i04 | inference | The dog is blocking the water by standing on the hose | 0.5 | 'so the dog may be blocking the water', but also offers that it 'may just be standing next to the hose' |
| pic_02 | i11 | entity | There are a few white clouds | 0 | clouds not mentioned |
| pic_03 | i05 | entity | There are a few white clouds | 0 | clouds not mentioned |
| pic_04 | i07 | entity | There are a few white clouds | 0 | clouds not mentioned |
| pic_05 | i05 | entity | There are a few white clouds | 0 | clouds not mentioned |
| pic_06 | i06 | entity | There are a few white clouds | 0 | clouds not mentioned |
| pic_07 | i07 | entity | There are a few white clouds | 0 | clouds not mentioned |
| pic_08 | i05 | entity | There are a few white clouds | 0 | clouds not mentioned (only wind lines in the sky) |
| pic_09 | i03 | entity | There are a few white clouds | 0 | clouds not mentioned |
| pic_10 | i12 | entity | There are a few white clouds | 0 | clouds not mentioned |
| pic_12 | i07 | entity | There are a few white clouds | 0 | clouds not mentioned |

All 10 zeros are the same entity, "There are a few white clouds": the descriptions of pic_02 to pic_10 and pic_12 never mention clouds, while every description from pic_13 on (and pic_11) lists "two clouds". No item was scored misread.

Credited but worth knowing (scored 1):

- The man in the red shirt and blue jeans was called "a boy" in pic_12 (i01, hanging laundry) and pic_23 (i18, eating ice cream), and "man or older boy" in pic_09 (i01). The actions were right, so they got full credit.
- These inferences were stated as the main reading, with another reading offered only as a less likely hedge: pic_08 i03 (could have thrown the hat), pic_13 i04 (the balloon could be someone else's), pic_21 i03 and pic_23 i03 (the sandwich could be the bird's own find), pic_21 i12 (he might be walking away from the box). pic_25 i01 said "hanging up (or taking down)" the washing.
- pic_01 i16: the square wheel was described, and called possibly "a drawing error". It was credited as describing the impossible fact, although they did not say it could not roll.

## Unintended oddities (not scored items), grouped by kind

Pose or contact unclear:

- pic_11: the man's legs are drawn over the seesaw beam, so how he sits on it is "not fully clear".
- pic_14: the same, the older man's legs are drawn over the seesaw beam.

Direction of movement unclear:

- pic_08: wind direction unclear. The hat sits at the left end of wind lines that run right, so it could be moving either way.
- pic_21: the man reading while walking may be heading left toward the box or right away from it.

Physics inconsistent with the story:

- pic_08: only the hat and a few leaves move in the wind. The tree, flowers, potted plants and the woman's hair stay still.

Prop that does not fit the action:

- pic_02: the walking reader's glasses look dark, like sunglasses, "which would be odd for reading".

Not counted, because they are hedges about small details the describer said look fine: pic_01, the cat walks on the narrow pointed tops of the fence boards ("possible, but worth noting"). pic_25, the man's feet are slightly behind the bottoms of the line posts ("does not look clearly wrong").

The other 22 pictures have no unintended oddity. Every other oddity the describers reported is a scored contradiction item.
