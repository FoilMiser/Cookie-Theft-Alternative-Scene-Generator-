# v0.37 picture-description scores, key set A

Scored 27 pictures (pic_01 to pic_27), 304 key items, from desc_pic_NN.md against keys_a.json. Scores are in scores_a.json.

Scale: 1 = clearly mentioned with the right meaning; 0.5 = partly or only one of two readings; 0 = not mentioned; misread = seen but read as something else (counted as 0 in the means).

## Mean score by item type

| Type | Items | Mean | Below 1 |
|---|---:|---:|---:|
| entity | 175 | 1.000 | 0 |
| action | 86 | 0.994 | 1 |
| inference | 19 | 0.947 | 2 |
| contradiction_notice | 12 | 1.000 | 0 |
| contradiction_explain | 12 | 0.958 | 1 |
| **all** | 304 | 0.993 | 4 |

## Items scored 0, 0.5 or misread

4 items: 4 scored 0.5. No item scored 0 and none was misread.

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_10 | i05 | inference | The child dropped the ice cream | 0.5 | says the scoop 'has fallen', but unsure whether the brown dog caused it to fall; child dropping it not settled |
| pic_12 | i01 | action | A man is hanging up laundry | 0.5 | 'a boy' in red T-shirt at the washing line 'pegging up or taking down the T-shirt': hanging up only one of two readings, and read as a boy |
| pic_21 | i06 | contradiction_explain | The water is going up into the air instead of falling down onto the flowers | 0.5 | only in unsure section: curves up 'could be read as water pouring onto the planter, or as water shooting upward/sideways'; free description just says watering |
| pic_23 | i03 | inference | The bird is stealing the sandwich while the man is busy reading | 0.5 | free description only places the bird beside the sandwich; stealing only 'seemingly' in inventory and 'just standing there, or about to steal' in unsure |

## Unintended oddities, grouped by kind

8 oddities in 8 pictures; the other pictures had none the describer presented as wrong or confusing.

**Figure and prop contact (seesaw sitter's legs and beam)** (2)
- pic_11: seesaw beam seems to pass behind or through the man's legs; hard to see how he is sitting on the board
- pic_14: man's legs drawn over the front of the seesaw beam; unclear exactly how he is seated on it

**Layout / placement** (1)
- pic_02: planter placed right in front of a shop door, blocking the doorway (describer: probably just placement)

**Physics not consistent with the event** (1)
- pic_08: wind is strong enough to blow the cap off, but the tree, plants and flowers are not bending at all

**Scene content (empty scene)** (1)
- pic_15: garden has no people at all; describer wonders whether a person was meant to be there and is missing

**Drawing glitch (prop merged into object)** (1)
- pic_18: rightmost painted fence board looks flatter, as if the roller is drawn as part of the board (small drawing oddity)

**Unsupported object** (1)
- pic_23: bicycle stands upright by itself in the open with no rack (perhaps a kickstand)

**Scale / depth** (1)
- pic_25: man looks small compared with the washing-line posts and fence, though his feet put him between the posts (scale/depth)

## Completeness check

Checked by script against keys_a.json: every one of the 304 items in the 27 pictures has exactly one score, no item id or picture is missing, and no item or picture was invented. Every picture has an unintended list (empty where nothing was reported).
## Scoring notes

- Different age or sex labels for a character (a "girl" for the key's woman in pic_01, a "boy" for a teenager) were not marked down when the action was right. The one exception is pic_12 i01, where the label was wrong and the action was also uncertain.
- When the free description committed to the target reading and only the unsure section offered an alternative, the item got 1 (pic_01 i07, pic_21 i03, the bird about to take the sandwich). When the describer never settled on the target reading, it got 0.5 (pic_10 i05, pic_23 i03).
- A problem in the key, not scored: the accepted phrasings for the bird-and-sandwich inference use the wrong pronoun for the reader in places ("she doesn't notice the bird" for a man in pic_01 and pic_23, "he isn't watching his sandwich" for a woman in pic_21).
