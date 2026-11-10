# v0.45 picture-description scores, key A

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 150 | 0.947 |
| action | 77 | 0.994 |
| inference | 17 | 1.000 |
| contradiction_notice | 8 | 1.000 |
| contradiction_explain | 8 | 0.938 |
| all | 260 | 0.965 |

Misread would count as 0 in the means; no item was scored misread.

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---|---|
| pic_09 | i04 | There are a few white clouds | 0 | clouds not mentioned (only 'sunny') |
| pic_10 | i08 | A bird is pecking at the ground | 0.5 | red bird seen 'standing on the grass', not pecking |
| pic_10 | i16 | The bicycle has square wheels, so it could not roll | 0.5 | wheels 'a bit squared/boxy', hedged; not said it could not roll |
| pic_11 | i04 | There are a few white clouds | 0 | clouds not mentioned (only 'sunny') |
| pic_12 | i06 | There are a few white clouds | 0 | clouds not mentioned (only 'sunny') |
| pic_13 | i03 | There are a few white clouds | 0 | clouds not mentioned (only 'sunny') |
| pic_14 | i06 | There are a few white clouds | 0 | clouds not mentioned (only 'sunny') |
| pic_15 | i08 | There are a few white clouds | 0 | clouds not mentioned (only 'sunny') |
| pic_16 | i08 | There are a few white clouds | 0 | clouds not mentioned (only 'sunny') |
| pic_16 | i09 | There is a tree | 0 | no tree mentioned (only a hedge behind the fence) |

## Unintended oddities (6, in 6 of 24 pictures)

### Overlaps / layering
- pic_14: the man's lower body overlaps the seesaw plank, as if the plank passes through his legs
- pic_21: the jeans hang slanted and overlap the washing-line post

### Objects unsupported or incomplete
- pic_10: the bicycle stands upright with no rider or kickstand visible
- pic_22: only one swing hangs on a frame wide enough for two

### Scene plausibility
- pic_05: eating ice cream under storm clouds is a little odd
- pic_19: a goat in a park is a little unusual [goat, profile]

### Oddities about animals, by angle

| Angle | Count |
|---|---|
| profile | 1 (pic_19 goat) |
| three-quarter front | 0 |

## Completeness check

Every item in keys_a.json got exactly one score: 260 items across 24 pictures (pic_01 to pic_24). Checked by script that each picture's scored ids match the key's ids in order: none missing, none invented.
