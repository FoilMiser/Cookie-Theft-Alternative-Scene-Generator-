# Scores summary, set D (pic_70 to pic_92), v0.42

Scored from vision/v042/desc_pic_70.md to desc_pic_92.md against vision/v042/keys_d.json. Per-item scores are in scores_d.json.

## Coverage check

- Pictures in key: 23; pictures scored: 23.
- Items in key: 250; items scored: 250. Every key item has exactly one score; no item is missing and no item id was invented (checked by script against keys_d.json).
- Misread counts as 0 in the means.

## Mean score by item type

| Type | Items | Mean | Below 1 |
|---|---:|---:|---:|
| entity | 141 | 1.000 | 0 |
| action | 76 | 1.000 | 0 |
| inference | 17 | 1.000 | 0 |
| contradiction_notice | 8 | 1.000 | 0 |
| contradiction_explain | 8 | 0.938 | 1 |
| **all** | 250 | 0.998 | 1 |

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_78 | i14 | contradiction_explain | The dog is reading a newspaper, but dogs can't read | 0.5 | 'as if reading it', but the unsure section offers two readings: reading (impossible) or just holding a fetched paper |

Counts: 0 scored 0, 1 scored 0.5, 0 misread.

## Unintended oddities, grouped by kind

14 oddities in 10 of 23 pictures; 13 pictures had none.

### animal drawing unclear (4)

- pic_74: the white bird on the pond could be a goose or a swan; its wing shape is hard to make out [duck, profile]
- pic_75: the goat's tether rope is thin and partly hard to follow [goat, three-quarter back]
- pic_76: the cat's legs are drawn bunched together in a tangle of lines, so its pose is a little hard to read [cat, three-quarter front]
- pic_88: the begging dog is drawn awkwardly: bent legs and raised paws bunched together, so it could be read as jumping up [dog, three-quarter front]

### contact/overlap (3)

- pic_72: the kite string seems to be drawn across the edge of the left tree's leaves, odd for a free-flying string
- pic_73: the low end of the seesaw does not quite reach the ground; the boy's feet hang just below the plank
- pic_81: the woman's body overlaps the front of the bench a little

### human detail (2)

- pic_77: the man's face in profile is slightly hard to read
- pic_86: the waving man's raised arm has a dark grey sleeve under the vest while his lowered arm is bare

### human pose (2)

- pic_72: the kicking boy's hands are spread out stiffly to the sides, slightly awkward
- pic_77: the man's reaching pose (legs slightly bent, leaning) looks slightly stiff

### animal placement (1)

- pic_70: the cat walking along the narrow pointed tops of the fence is 'a bit of a stretch', though plausible [cat, profile]

### lighting (1)

- pic_75: the grass and objects look brightly lit despite the grey storm sky

### prop design (1)

- pic_73: the swing frame has only one seat, slightly unusual

### Animal oddities by angle

| Angle | Count | Where |
|---|---:|---|
| profile | 2 | pic_70 cat, pic_74 duck |
| three-quarter front | 2 | pic_76 cat, pic_88 dog |
| three-quarter back | 1 | pic_75 goat |

Rule used for oddities: listed only things the describer called odd, awkward, unusual, a stretch, or hard to read or follow, or an apparent physical or overlap fault, that are not scored items. Hedges about who is looking where, age or gender, and small-detail doubts (crumbs on the pond edge, a mark near a ladder rung, a moustache or smear) were left out.
