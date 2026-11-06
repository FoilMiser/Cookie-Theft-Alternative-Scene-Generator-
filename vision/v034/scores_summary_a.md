# Picture description scores, set A (v0.34)

Inputs: `vision/v034/desc_pic_01.md` to `desc_pic_27.md` and `vision/v034/keys_a.json`. Output: `vision/v034/scores_a.json`.

Scoring: 1 = clearly conveyed; 0.5 = partly (element seen, meaning half right, or one of two readings); 0 = not mentioned; misread = mentioned but read as something else (counted as 0 in means). Inference items needed the stated cause, prediction or intention; contradiction items needed the describer to call it wrong/impossible/odd or state the impossible fact. Where the free description committed to a reading and the unsure section only offered an alternative, the committed reading was scored.

## Completeness check

- Pictures in key: 27; pictures scored: 27.
- Items in key: 314; items scored: 314.
- Missing items: 0. Invented items (ids not in the key): 0. Extra pictures: 0.
- Every item of every picture in keys_a.json has exactly one score.

## Mean score by item type

| Type | Items | 1 | 0.5 | 0 | Misread | Mean |
|---|---:|---:|---:|---:|---:|---:|
| entity | 178 | 178 | 0 | 0 | 0 | 1.000 |
| action | 87 | 87 | 0 | 0 | 0 | 1.000 |
| inference | 23 | 22 | 1 | 0 | 0 | 0.978 |
| contradiction_notice | 13 | 13 | 0 | 0 | 0 | 1.000 |
| contradiction_explain | 13 | 13 | 0 | 0 | 0 | 1.000 |
| **all** | 314 | 313 | 1 | 0 | 0 | 0.998 |

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_04 | i07 | inference | The bird is stealing the sandwich while the man is busy reading | 0.5 | bird 'pecks at the sandwich' ('the man's sandwich') while he reads, but stealing or him not noticing is never stated |

No item was scored 0 and none was a misread.

## Identity notes on items scored 1

The action was credited, but the describer did not identify the character as the key does:

- pic_03 i01: grandmother described as an 'old man' (teal top, grey shorts, glasses); action credited.
- pic_04 i11: grandmother described as an 'old person', 'grey shorts or a short skirt'; gender left open; action credited.

## Borderline items scored 1

- pic_01 i04 (duck has come to eat the bread): describer says the duck 'swims toward the crumbs' and the bag is 'for the duck'; the purpose is implied, not stated outright.
- pic_21 i03 (bird stealing while the woman reads): bird 'looks about to peck at or steal it'; stealing is stated, but her not noticing is not.
- pic_21 i18 (child jumping for joy): jumping clearly described; 'for joy' offered as one of two readings (the other is reaching for something). Credited because plain 'jumping' is an accepted phrasing.

## Unintended oddities (not scored items), grouped by kind

**depth / overlap** (2)

- pic_22: boy's feet are well in front of the flower bed but a yellow flower touches or overlaps his face/cap brim, which looks odd for depth
- pic_25: second box by the market stall covers the bottom of the stall's leg; unclear whether it stands in front of the leg or the leg rests on it

**pose or gaze hard to read** (2)

- pic_07: man's legs and feet are partly hidden behind/under the seesaw beam, so it is hard to see how he is sitting
- pic_21: dog holding the newspaper faces up and to the side, not at the paper

**drawing simplification** (1)

- pic_26: part of the freshly painted fence section next to the roller looks like a solid blue block rather than separate planks

**possible floating / attachment** (1)

- pic_02: beach ball sits at the outer edge of the foliage and could look like it is floating in front of the tree rather than stuck in it

No unintended oddity reported for 21 of 27 pictures: pic_01, pic_03, pic_04, pic_05, pic_06, pic_08, pic_09, pic_10, pic_11, pic_12, pic_13, pic_14, pic_15, pic_16, pic_17, pic_18, pic_19, pic_20, pic_23, pic_24, pic_27.
