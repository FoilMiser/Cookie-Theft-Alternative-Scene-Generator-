# Scores summary, set b (pic_26 to pic_50)

Completeness check: all 25 pictures and all 278 items in keys_b.json have exactly one score in scores_b.json. No item is missing and none was invented. I checked this with a script that compares item ids in the key and the scores.

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 174 | 0.931 |
| action | 72 | 1.000 |
| inference | 20 | 1.000 |
| contradiction_notice | 6 | 0.917 |
| contradiction_explain | 6 | 1.000 |
| **all** | **278** | **0.955** |

No item was scored as a misreading.

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---|---|
| pic_26 | i06 | There are a few white clouds | 0 | no clouds mentioned |
| pic_27 | i05 | There are a few white clouds | 0 | no clouds mentioned |
| pic_27 | i06 | There is a tree | 0 | no tree mentioned |
| pic_28 | i04 | There are a few white clouds | 0 | no clouds mentioned |
| pic_29 | i08 | There are a few white clouds | 0 | no clouds mentioned |
| pic_29 | i09 | There is a tree | 0 | no tree mentioned |
| pic_30 | i09 | There are a few white clouds | 0 | no clouds mentioned |
| pic_30 | i10 | There is a tree | 0 | no tree mentioned |
| pic_31 | i04 | There are a few white clouds | 0 | no clouds mentioned |
| pic_31 | i05 | There is a tree | 0 | only bushes mentioned |
| pic_32 | i08 | There are a few white clouds | 0 | only wind lines in the sky, no clouds |
| pic_32 | i09 | There is a tree | 0 | only a bush mentioned |
| pic_42 | i04 | Something is wrong with the wheelbarrow | 0.5 | the unsure section says the wheel "looks like a square frame rather than a round wheel", but never calls it wrong, and the free description says everything looks ordinary |

All 12 zeros are background clouds or trees, and all fall in pic_26 to pic_32.

## Judgement calls scored 1

| Pic | Id | Why it was a call |
|---|---|---|
| pic_26 | i04 | kite "seems caught"; the unsure section allows it to be flying in front of the tree |
| pic_27 | i03 | stealing given as the main reading; the unsure section allows the bird to be just sitting beside the sandwich |
| pic_29 | i04 | the dog blocking the hose is "presumably why"; the unsure section also allows that she has not turned it on |
| pic_30 | i03 | begging is the main reading; the unsure section allows the dog to be just sitting up |
| pic_31 | i01 | the woman is digging with a trowel next to a potted flower, which is "seems to be planting" (inferred, not seen directly) |
| pic_32 | i05 | blown off is the main reading; the unsure section allows that he threw the cap |
| pic_33 | i02 | pointing at the clouds is the main reading; the unsure section allows the birdhouse |
| pic_34 | i01 | same trowel and pot reading as pic_31 |
| pic_34 | i02 | near word: "boy" for teenager |
| pic_35 | i01 | near word: "boy" for teenager |
| pic_35 | i02 | "ready to catch" is the main reading; the unsure section allows that she just threw it |
| pic_36 | i02 | near word: "boy" for teenager |
| pic_37 | i04 | near word: "boy" for teenager |
| pic_37 | i05, i06 | stuck in the tree is the main reading; the unsure section allows the kite to be flying in front of it |
| pic_38 | i04 | the bird is "about to steal"; the unsure section allows it to be just sitting there |
| pic_38 | i07 | let go is the main reading; the unsure section allows that the balloon was never his |
| pic_39 | i03 | stalking is the main reading; the unsure section allows the cat to be just walking |
| pic_39 | i04 | near word: "boy" for teenager |
| pic_40 | i03 | the duck is eating floating bread, not shown swimming toward the shore; credited on "duck" |
| pic_41 | i06 | the wheel is called "a bit odd" in the unsure section only, while the free description says nothing seems wrong |
| pic_41 | i07 | the wheel is "square-ish ... rather than a round wheel"; hedged, and in the unsure section only |
| pic_42 | i05 | the square wheel is described, but in the unsure section only and not flagged as wrong |
| pic_44 | i04 | dropped is the main reading; the unsure section allows that the dog knocked it down |
| pic_46 | i02 | near word: "boy" for teenager |
| pic_47 | i04 | pointing at the sky is the main reading; the unsure section allows the birdhouse |
| pic_49 | i03 | near word: "boy" for teenager |

## Unintended oddities, grouped by kind

**Overlap and placement (4)**
- pic_37: the girl with the bread overlaps the pond outline, with her feet very close to the water
- pic_41: the hose seems to run behind or through the lower edge of the flower bed
- pic_46: the boy's legs stick out past the front of the bench awkwardly
- pic_48: the washing seems pegged slightly below the line on the right

**Hose and water drawing (2)**
- pic_43: the hose loops up beside the woman in a stiff, unnatural curve
- pic_43: the water stream seems to start from the hose loop and is hard to match to the nozzle

**Hard to see or hard to identify (4)**
- pic_27: the small bird is hard to make out against the bench and sandwich [bird, profile]
- pic_46: the blue bird blends with the boy's blue hoodie [bird, profile]
- pic_47: the paint roller has a short handle and a squarish head, hard to tell from a brush
- pic_35: the ball's dotted trail ends above and left of the woman's hands, so it may be going past her

**Scene logic and staging (4)**
- pic_32: very windy, yet the flowers, plants and sleeping dog show no sign of wind [dog, three-quarter front]
- pic_32: the wind lines in the empty sky could be read as birds or decoration
- pic_37: a goat in a public park is unusual [goat, three-quarter front]
- pic_31: the two women look almost identical, maybe the same person drawn twice

**Oddities about animals, by angle**
- profile: 2 (both birds: pic_27, pic_46)
- three-quarter front: 2 (dog in pic_32, goat in pic_37)
