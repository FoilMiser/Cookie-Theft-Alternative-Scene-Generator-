# v0.38 picture-description scores, set C (pic_51 to pic_76)

Scored from desc_pic_51.md to desc_pic_76.md against keys_c.json. Scale: 1 = clearly mentioned with the right meaning, 0.5 = partly or only one of two equal readings, 0 = not mentioned, misread = mentioned but read as something else (counted as 0 in the means).

## Mean score by item type

| Item type | Items | Mean | Scored below 1 |
|---|---:|---:|---:|
| entity | 152 | 1.000 | 0 |
| action | 85 | 1.000 | 0 |
| inference | 19 | 0.974 | 1 |
| contradiction_notice | 10 | 1.000 | 0 |
| contradiction_explain | 10 | 1.000 | 0 |
| **all** | 276 | 0.998 | 1 |

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_72 | i05 | inference | The child dropped the ice cream | 0.5 | says the ice cream 'has fallen', but is unsure whether the boy dropped it or the dog knocked it out of his hand |

No item was scored 0 or misread.

### Credited items with the agent misidentified

These kept a score of 1 because the action was described correctly and the key's accepted phrasings do not name the agent, but the figure was read as someone else:

- pic_72 i01 (A grandmother is sitting on the bench with a drink): grandmother read as an old man with white hair, glasses, teal jacket and grey shorts.
- pic_60 i03 (A man is sitting and reading): man read as a boy.

## Unintended oddities, grouped by kind

### autumn leaves with green trees (2)

- pic_65: autumn-coloured leaves are being swept but the only tree is fully green: 'a little odd where the leaves came from'
- pic_71: pile of autumn leaves although every tree is green; 'they seem to come from nowhere'

### relative size / scale (2)

- pic_69: girl is 'quite a bit smaller than the boy' she plays catch with; 'the size difference is noticeable'
- pic_72: small girl flying the kite is 'drawn much smaller than the old man' on the bench

### scene logic (4)

- pic_69: stormy weather, yet everyone carries on outdoors with no umbrellas or coats
- pic_70: grandfather pushes the pram across the grass towards the flowerbed and rock, not along the path: 'a slightly odd route'
- pic_73: fruit stall has no seller, 'a little odd but not impossible'
- pic_75: woman digging a hole in the middle of the park lawn with no plant or reason shown, possibly 'something odd'

### overlap / depth (1)

- pic_62: man's head overlaps the fruit stall table, so 'at a glance he looks partly in the stall'

### pose hard to read (1)

- pic_59: sleeping cat's pose is 'a bit hard to read' (on its back or side with one paw up); describer adds it does not look hurt

### odd shape of a drawn element (1)

- pic_57: branch holding the fish curves out from the trunk unusually, 'almost like an arm holding the fish up'

Pictures with no unintended oddity reported (16): pic_51, pic_52, pic_53, pic_54, pic_55, pic_56, pic_58, pic_60, pic_61, pic_63, pic_64, pic_66, pic_67, pic_68, pic_74, pic_76.

## Completeness check

Checked by script against keys_c.json: 26 pictures, 276 items in the key, 276 scores written. Every key item has exactly one score; no item is missing, duplicated or invented, and no picture has more than three unintended oddities.
