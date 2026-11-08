# Picture-description scores, set B (pic_25 to pic_48)

Sources: `desc_pic_25.md` to `desc_pic_48.md` and `keys_b.json` in `vision/v041/`. Per-item scores and evidence are in `scores_b.json`.
Scoring: 1 = clearly mentioned with the right meaning, 0.5 = partly, 0 = not mentioned, misread = mentioned but read as something else (misread counts as 0 in the means).

## Completeness check

- keys_b.json lists 24 pictures and 263 scored items; scores_b.json gives exactly one score to each of the 263 items.
- Checked by script against keys_b.json: no item is missing and no item is invented, in any picture.

## Mean score by item type

| Type | Items | Mean | 1 | 0.5 | 0 | Misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 156 | 1.000 | 156 | 0 | 0 | 0 |
| action | 71 | 0.993 | 70 | 1 | 0 | 0 |
| inference | 14 | 0.964 | 13 | 1 | 0 | 0 |
| contradiction_notice | 11 | 1.000 | 11 | 0 | 0 | 0 |
| contradiction_explain | 11 | 1.000 | 11 | 0 | 0 | 0 |
| **all** | 263 | 0.996 | 261 | 2 | 0 | 0 |

## Items scored 0, 0.5 or misread

| Pic | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---:|---|
| pic_28 | i05 | action | A man is sweeping | 0.5 | man 'sweeps or rakes' leaves with 'a yellow broom or fan rake'; unsure section repeats broom vs fan rake (two readings) |
| pic_38 | i12 | inference | It is about to rain | 0.5 | calls them 'storm'/'rain clouds' and 'gloomy weather', and offers the clouds as one of three possible targets of the pointing, but never says rain is coming |

No item was scored 0 and none was misread.

## Unintended oddities, grouped by kind

15 oddities across 13 of the 24 pictures; 11 pictures had none. Only things the describer presented as wrong, impossible, confusing or out of place are listed; hedges about small details and remarks about the scored (intended) story are left out.

### Figure pose or overlap looks wrong (drawing flaws) (3)

- pic_31: the swing ropes cross in front of the child's body at an angle, which looks awkward
- pic_41: the man's feet point left while his upper body and head face right, so his pose looks twisted
- pic_44: the see-saw plank seems to cross the man's legs, so it is unclear whether he sits on the end or the plank passes through or in front of his legs

### Something seems to hang or float in the air (2)

- pic_42: the jumping girl seems to float slightly above her shadow, which could read as floating
- pic_43: the drips from the laundry are drawn hanging in the air below the clothes

### Person not looking at what they are doing (2)

- pic_31: the woman watering looks left past the flowers rather than at what she is watering
- pic_32: the man watering faces the viewer rather than looking down at the flowers he is watering

### Odd placement of a prop (1)

- pic_29: the rubbish bin sits oddly far forward in the bottom-left corner, apart from everything else

### Task result looks unrealistic (1)

- pic_30: the painted fence patch is a neat block with clean edges, more like a finished panel than work in progress

### Scene logic (activity does not fit the weather) (1)

- pic_38: eating ice cream under dark storm clouds seems slightly odd

### Animal out of place in the setting (plausibility, not a drawing flaw) (5)

- pic_25: a loose goat wandering in a public park seems a bit unusual (describer adds that nothing looks impossible) [goat, three-quarter back]
- pic_36: a goat in an ordinary back garden seems a little unusual (describer adds that nothing looks impossible) [goat, three-quarter back]
- pic_39: a goat loose in a park seems a little unusual (describer adds that nothing looks impossible) [goat, profile]
- pic_40: a goat in a back garden seems slightly unusual (describer adds that nothing looks impossible) [goat, three-quarter front]
- pic_41: the goat seems out of place in a suburban back garden, with no lead or pen [goat, three-quarter front]

### Oddities about animals, counted by angle

| Animal | Angle | Count | Pictures |
|---|---|---:|---|
| goat | profile | 1 | pic_39 |
| goat | three-quarter back | 2 | pic_25, pic_36 |
| goat | three-quarter front | 2 | pic_40, pic_41 |

All animal oddities are remarks that a goat is unusual in a park or back garden. None is about how an animal is drawn, so they say nothing about which angle renders well. No oddity was reported about the ducks, dogs or birds at any angle.
