# Picture-description scoring, set C (v018, pic_40 to pic_60)

Inputs: `desc_pic_40.md` to `desc_pic_60.md` and `keys_c.json`. Output: `scores_c.json`.

## Completeness check

- Key items: 236 across 21 pictures. Scored items: 236.
- Every key item has exactly one score: yes. Missing items: none. Invented items or pictures: none.
- Scale: 1 / 0.5 / 0 / misread. For the means, misread counts as 0.

## Mean score by item type

| Type | n | Mean | 1 | 0.5 | 0 | misread |
|---|---|---|---|---|---|---|
| entity | 133 | 1.000 | 133 | 0 | 0 | 0 |
| action | 69 | 0.986 | 67 | 2 | 0 | 0 |
| inference | 12 | 0.875 | 10 | 1 | 1 | 0 |
| contradiction_notice | 11 | 0.955 | 10 | 1 | 0 | 0 |
| contradiction_explain | 11 | 0.909 | 10 | 0 | 0 | 1 |
| **all** | 236 | 0.983 | 230 | 4 | 1 | 1 |

## Items scored 0, 0.5 or misread

| Pic | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_40 | i02 | contradiction_notice | Something is wrong with what the person is watering with | 0.5 | flagged the watering implement as odd, but the reason given was a spray nozzle not attached to any hose; hedged in unsure section (impossible vs hose hidden) |
| pic_40 | i03 | contradiction_explain | The person is watering the flowers with a frying pan instead of a watering can | misread | frying pan read as a dark grey hose spray nozzle / watering wand; never mentions a pan |
| pic_52 | i03 | action | A woman is running | 0.5 | only as one of two readings: 'striding or jogging', 'walking briskly or jogging', 'jogging or walking quickly' |
| pic_53 | i06 | inference | The duck is coming to eat the bread | 0.5 | duck 'swimming toward' the crumbs, but wanting/coming to eat the bread is never stated (direction only) |
| pic_53 | i07 | action | A teenager is reading while walking | 0.5 | person (read as woman) 'walks along reading or holding an open newspaper'; reading hedged with holding papers / map / struggling in wind |
| pic_53 | i09 | inference | The teenager is going to trip over a bucket | 0 | bucket noted only as having 'no obvious owner or purpose'; no trip or bump prediction |

Related observations (not score deductions):
- Character age or gender labels sometimes differ from the key while the action is right: pic_40 i01 (woman for teenager), pic_43 i02 (girl for woman), pic_43 i03 (gender unsure for man), pic_49 i01 (woman for teenager), pic_53 i07 (woman for teenager), pic_54 i04 (man for teenager). All of these were scored on the action.
- pic_57 i02 and pic_59 i03: the box was read as cardboard, not wooden. It was credited as a box (1).
- pic_54 i06: the 'ball is stuck' inference was stated outright. That it is the teenager's ball was offered as one of two readings, but the key's accepted phrasings credit 'the ball is stuck'.
- Judgement call: pic_53 i06 got 0.5 because 'swimming toward the crumbs' gives the direction but not the purpose. In pic_55 the same item got 1 because the duck 'seems to have a crumb at its beak'.

## Unintended oddities (reported by the describer, not scored items), grouped by kind

### Drawing, scale or overlap quirks (5)
- pic_50: goat's head drawn a little oddly (round, one curved horn) (drawing quirk)
- pic_51: girl very small compared with the adults (resolved as standing far back) (scale)
- pic_53: child's upper body overlaps the pond in the picture (read as standing in front of it) (overlap, resolved)
- pic_54: dog's body drawn long and low with back legs trailing, 'looks slightly odd' (drawing quirk)
- pic_59: woman's head drawn in front of the striped item on the line, looks crowded (not impossible) (drawing quirk)

### Unusual but possible presence (3)
- pic_42: goat in a back garden (unusual but possible)
- pic_48: workman in hi-vis vest in a home garden (unusual but possible)
- pic_50: goat grazing loose in a public park ('the most unusual thing'; maybe escaped) (unusual but possible)

### Unattended or unexplained objects (3)
- pic_42: full pet-food bowl on the grass that no animal is eating from (unexplained detail)
- pic_46: fruit stall with nobody serving (unexplained detail)
- pic_54: fruit stall has no seller (unexplained detail)

### Possible floating or hovering (hedged) (2)
- pic_40: girl's feet above the ground with a separate shadow could be read as floating/hovering (describer favours jumping) (possible floating, hedged)
- pic_47: girl at the left end barely touches the plank and could be read as hovering (most likely sitting) (possible floating, hedged)

### Minor placement details (2)
- pic_43: water drops land at the front edge of the flowerbed rather than on the flowers (minor, called probably fine)
- pic_60: woman running on the grass rather than on the path (minor placement)

### Extra predictions or interpretations (2)
- pic_46: the runner may be about to hug/greet the cheering person, or they may collide because the cheerer's eyes are closed (extra prediction, hedged)
- pic_48: when the dog steps off, the water will burst out and spray the worker in the face (extra prediction)

### Social oddity (1)
- pic_56: grown man sitting on a children's seesaw reading and ignoring the stranded girl, called 'the odd part' (social oddity)

No unintended oddities reported: pic_41, pic_44, pic_45, pic_49, pic_52, pic_55, pic_57, pic_58.

Not listed above: in pic_40 the describer called the woman's spray nozzle 'not attached to any hose'. That is their misreading of the scored frying-pan contradiction (i02/i03), so it is recorded under those items and not counted as unintended.
