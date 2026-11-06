# Scores summary, set C (pic_56 to pic_83)

Scored from `desc_pic_56.md` ... `desc_pic_83.md` against `keys_c.json`. Full per-item scores and notes are in `scores_c.json`.

## Mean score by item type

| Item type | Items | Mean score | Scored 1 | Scored 0.5 | Scored 0 | Misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 165 | 0.952 | 157 | 0 | 8 | 0 |
| action | 84 | 0.994 | 83 | 1 | 0 | 0 |
| inference | 16 | 0.969 | 15 | 1 | 0 | 0 |
| contradiction_notice | 12 | 1.000 | 12 | 0 | 0 | 0 |
| contradiction_explain | 12 | 1.000 | 12 | 0 | 0 | 0 |
| **all** | 289 | 0.969 | 279 | 2 | 8 | 0 |

Misread counts as 0 in the means. No item was scored misread.

## Items scored 0, 0.5 or misread

| Picture | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---:|---|
| pic_75 | i08 | entity | There are a few white clouds | 0 | clouds not mentioned (no sky items in the inventory) |
| pic_77 | i05 | entity | There are a few white clouds | 0 | clouds not mentioned (no sky items in the inventory) |
| pic_78 | i07 | entity | There are a few white clouds | 0 | clouds not mentioned (no sky items in the inventory) |
| pic_80 | i06 | entity | There are a few white clouds | 0 | clouds not mentioned (no sky items in the inventory) |
| pic_81 | i02 | action | The goat is standing on the hose | 0.5 | 'its hooves seem to be standing on the hose', but inventory says 'on or right next to the hose' and the unsure section gives two readings |
| pic_81 | i04 | inference | The goat is blocking the water by standing on the hose | 0.5 | 'which would explain why the water has stopped', offered as one of two readings (other: hose just runs past, water off for another reason) |
| pic_81 | i07 | entity | There are a few white clouds | 0 | clouds not mentioned (no sky items in the inventory) |
| pic_81 | i08 | entity | There is a tree | 0 | no tree mentioned anywhere |
| pic_82 | i06 | entity | There are a few white clouds | 0 | clouds not mentioned (no sky items in the inventory) |
| pic_83 | i21 | entity | There are a few white clouds | 0 | clouds not mentioned (no sky items in the inventory) |

## Unintended oddities, grouped by kind

Only things the describer presented as looking wrong, impossible or confusing that are not scored items.

### Animal out of place (goat in a garden or park) (4)

- pic_59: goat in a small suburban back garden (a little unusual)
- pic_67: goat grazing in a public park (a little unusual)
- pic_81: goat in a back garden (unusual)
- pic_83: goat grazing in a public park (unusual)

### Figure not clearly on its support or in the wrong spot (5)

- pic_56: elderly woman pushing the pram walks on the grass beside the path rather than on it (slightly odd placement)
- pic_57: girl seems to sit slightly above the seesaw plank rather than firmly on it
- pic_62: grandfather sits on the very edge of the picnic blanket with legs on the grass: unclear if on it or beside it
- pic_65: child sits on the very edge of the picnic blanket: unclear if on it or beside it
- pic_72: fisherman's legs drawn over the pond outline, so at first glance he can look as if standing in the water

### Action with no visible reason or unclear relation (5)

- pic_60: woman running straight towards the boy with the balloon: possible collision, and nothing visible that she is chasing
- pic_65: child having a picnic alone with no adult in sight
- pic_71: begging dog has no lead and no owner nearby (unclear whose it is)
- pic_79: boy jumping and cheering with no visible reason
- pic_79: runner hurrying with nothing ahead of them to chase

### Hard-to-read drawing detail (4)

- pic_67: goat's head drawn small and oddly (seen from above or bent sharply down); reads as a goat mainly from horns and body
- pic_72: fishing line so thin and faint that the float can look like a separate object in the water
- pic_74: sweeper's sex unclear: gate knob behind the head reads as a hair bun, and the top has a frilly neckline
- pic_75: thrown ball looks still rising above and left of the catcher's hands, so it may go over them

Pictures with no unintended oddity reported (14): pic_58, pic_61, pic_63, pic_64, pic_66, pic_68, pic_69, pic_70, pic_73, pic_76, pic_77, pic_78, pic_80, pic_82.

## Completeness check

Checked by script against `keys_c.json`: 28 pictures, 289 key items, 289 scores written. Every key item has exactly one score, item ids and order match the key for every picture, no item is missing and no item was invented. Every score is 1, 0.5, 0 or misread, and no picture has more than three unintended oddities.

## Borderline calls, noted for review

- pic_70 i05 (bird pecking): credited because the key accepts plain "bird", but pecking was not described. The describer said the bird stands on the grass facing the cat.
- pic_58 i02 (dog wants a walk) and pic_75 i01 (hanging laundry): the free description gives the target reading. The unsure section adds an alternative ("simply carrying the lead"; "or taking down"). Credited as stated.
- pic_83 i02/i03 (frying pan): called "a strange thing to water with", and later "odd but possible". Credited, since the describer calls it odd and states the fact.
- Age or sex of the agent was hedged but the action was right: pic_58 i07 digger ("girl or young woman"), pic_74 i03 sweeper (man or woman), pic_75 i02 man with hands on hips (age not judged). All credited.
- pic_81 i02/i04 got 0.5, not 1, because the describer was uncertain in the inventory as well as the unsure section. Compare pic_59, the same goat-on-hose scene, where both items were stated without a hedge.
