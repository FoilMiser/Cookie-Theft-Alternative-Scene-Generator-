# Scores summary, key set A (pic_01 to pic_24)

Scored from desc_pic_01.md to desc_pic_24.md against keys_a.json. The per-item scores and evidence are in scores_a.json.

**Completeness check:** keys_a.json lists 255 items across 24 pictures. scores_a.json gives every one of them exactly one score. No item is missing, no item id is invented or duplicated, and the picture set matches the key exactly (pic_01 to pic_24). A script compared the item ids picture by picture against keys_a.json.

## Mean score by item type

| Item type | Items | Mean | Scored 1 | Scored 0.5 | Scored 0 / misread |
|---|---|---|---|---|---|
| entity | 155 | 1.000 | 155 | 0 | 0 |
| action | 64 | 1.000 | 64 | 0 | 0 |
| inference | 16 | 0.969 | 15 | 1 | 0 |
| contradiction_notice | 10 | 1.000 | 10 | 0 | 0 |
| contradiction_explain | 10 | 1.000 | 10 | 0 | 0 |
| **all items** | **255** | **0.998** | 254 | 1 | 0 |

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_06 | i07 | inference | The child dropped the ice cream | 0.5 | The free description says only that the ice cream "has fallen on the ground". The unsure section offers two readings: "the dog knocked the ice cream down, or the child dropped it and the dog is just taking advantage". |

No item scored 0 and no item was misread.

## Scored 1 with a caveat (for review)

- pic_10 i01 (teenager reading on the bench): the action is right, but the reader is called "a man in a red cap and blue hoodie". In pic_04, 06, 16, 22 and 23 the describer calls the same character a boy.
- pic_10 i03 (bird stealing the sandwich): the free description says the bird "looks about to take it, and he does not seem to notice". The unsure section adds that the bird "may just be standing next to it".
- pic_15 i04 (bird pecking at the ground): the bird is described as "standing on the grass" and pecking is not mentioned. It got 1 because the key accepts "bird" on its own.
- pic_02 i03 (box floating with nothing holding it up): the box is said to have "nothing for it to hang from". The describer also offers "falling from nowhere" or thrown over the fence as an alternative.

## Unintended oddities, grouped by kind (11 in total, 10 pictures)

**Odd or unidentifiable drawn shapes (4)**
- pic_01: the dog's white chest and belly patch is drawn as a separate white shape between its legs and looks like a bib or nappy [dog, three-quarter front]
- pic_04: the big right-hand tree has small lighter-green bush-shaped blobs on its leaves that look like separate bushes pasted onto the tree
- pic_08: there is a small dark mark near the ladder's top rungs that the describer could not make out
- pic_17: the branch holding the fish looks shaped specifically to reach it

**A figure overlaps the scenery so its position is unclear (3)**
- pic_05: the fisherman's upper body overlaps the pond, so at a glance he seems to stand in the water
- pic_23: the walking man's upper body overlaps the pond, so at a glance he seems to stand in the water
- pic_07: the man's crossed legs overlap the seesaw board, so it is hard to see where he sits. He seems to sit just above the board, not quite at its low end.

**A person is not looking at their task (2)**
- pic_02: the sweeping man looks off to the right, not at what he is sweeping
- pic_13: the digging woman looks away to the right, not at the hole she is digging

**A trail does not connect to its source (1)**
- pic_24: the blue paw prints begin just to the right of the paint tray, not inside it

**Unusual content (1)**
- pic_04: a goat in a public park is unusual [goat, three-quarter front]

**Oddities about animals, by angle**

| Angle | Count | Oddities |
|---|---|---|
| three-quarter front | 2 | pic_01 dog (bib or nappy-like chest patch); pic_04 goat (unusual in a park) |
| profile | 0 | none |

The pic_24 paw-print gap involves the dog's trail, not the dog's body, so it is not counted as an animal oddity. Only the pic_01 dog oddity is about how the animal is drawn.

Pictures with no unintended oddity: pic_03, 06, 09, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22.

Some hedges about small details were left out of the oddity list:
- Motion-line direction: the wind in pic_03, the duck in pic_04, the swing in pic_09.
- What a small item is: pan or saucepan in pic_04, moustache or clothes peg in pic_12, pram blanket or bonnet in pic_15, birdhouse or feeder in pic_21, spade or stick in pic_22, roller or brush in pic_24.
- Who or what an action is aimed at: the camera in pic_10, the wave in pic_15, why there are two boxes in pic_06, why she digs in the middle of the lawn in pic_13.
- The small ladder hand-rail in pic_19, where the describer says "nothing looks broken".
