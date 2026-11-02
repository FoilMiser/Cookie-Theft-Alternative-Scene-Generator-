# Scores summary: v022, key A (pic_01 to pic_22)

Sources: `desc_pic_01.md` … `desc_pic_22.md`, scored against `keys_a.json`. Each item was judged on the whole description file (free description + inventory + unsure section). Item-level scores and evidence are in `scores_a.json`.

## Completeness check

- The key has 22 pictures (pic_01 to pic_22) and 247 items. `scores_a.json` has the same 22 pictures and the same 247 item ids, in key order.
- Every key item has exactly one score. No item is missing, and no item or picture was invented. A script checked this before and after the file was written.
- Every score is one of 1, 0.5, 0 or "misread".

## Mean score by item type

"Misread" counts as 0 in the means.

| Item type | n | Mean | 1 | 0.5 | 0 | misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 138 | 1.000 | 138 | 0 | 0 | 0 |
| action | 72 | 1.000 | 72 | 0 | 0 | 0 |
| inference | 15 | 0.933 | 13 | 2 | 0 | 0 |
| contradiction_notice | 11 | 0.909 | 10 | 0 | 0 | 1 |
| contradiction_explain | 11 | 0.909 | 10 | 0 | 0 | 1 |
| **all items** | **247** | **0.988** | 243 | 2 | 0 | 2 |

## Items scored 0, 0.5 or misread

No item scored 0.

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_01 | i03 | contradiction_notice | Something is wrong with what the person is watering with | misread | Read the pan as "a grey, round watering can". In the unsure section the describer said it was a plain grey round shape with no visible spout or handle, possibly "a watering can, a bucket or even a stone", and also said "I saw nothing that looks impossible". |
| pic_01 | i04 | contradiction_explain | The person is watering the flowers with a frying pan instead of a watering can | misread | The frying pan was never named. It was read as a watering can (or a bucket or stone). |
| pic_18 | i03 | inference | The dog wants some of the food | 0.5 | Said the dog is "perhaps hoping for some", but the unsure section gives two readings: "could be begging for the older man's ice cream … or just walking by". |
| pic_18 | i10 | inference | The woman is going to trip over a box | 0.5 | Said "she might trip over it", but the unsure section gives two readings: "she might be about to trip over it, or she might simply walk past it". |

The same frying-pan contradiction was caught in pic_17, where the describer saw "a grey frying pan by its handle". In pic_01 the describer reported seeing no handle. This suggests the pan in pic_01 may be drawn too small or without a clear handle. That is an inference from the text only, since the picture was not opened.

## Unintended oddities (not scored items), grouped by kind

There are 13 oddities across 12 pictures. pic_05's hose appears under two kinds below but is one entry in `scores_a.json`. Pictures 01, 03, 10, 11, 12, 14, 15, 18, 19 and 20 have none.

**Hose drawn oddly (4 pictures, the most common kind)**
- pic_02: a large swollen bulge in the hose beside the dog. The describer read it as trapped water but said it could be a lump or kink.
- pic_04: the hose bends sharply from the ground back up to the nozzle beside the person watering ("awkward but not impossible").
- pic_05: the hose rises in front of the woman's legs, and it is unclear whether it passes in front of her or beside her.
- pic_08: a large bulge of trapped water in the hose between the reel and the dog.

**Overlap or depth ambiguity: things that could look as if they pass through each other (4 pictures)**
- pic_05: the hose and the woman's legs (also listed above).
- pic_16: the kite string crosses the clothesline. The describer couldn't tell whether it is in front, behind or snagged.
- pic_21: the woman and the older man overlap the edge of the pond. The describer read them as standing on the grass, not in the water.
- pic_22: the man's head overlaps the clothesline. The describer read him as standing in front of it, not passing through it.

**Awkward drawing of an object or pose (2 pictures)**
- pic_06: the dog's pose is hard to read. It is sitting up begging with a paw raised, but its back legs and tail stretch out as if it were half-lying.
- pic_09: the wheelbarrow's support leg is a dark blocky shape that looks like a boot.

**Objects that are hard to identify (3 pictures)**
- pic_07: the grey object by the sandpit reads as a rock but could be a mound or a shell.
- pic_08: the blue section of fence could be freshly painted boards or a separate blue gate.
- pic_13: the bucket and spade are drawn very close together. The spade may be leaning on the bucket or stuck in the sand.

**Something unplanned that the describer flagged as odd (1 picture)**
- pic_17: a goat grazing in an ordinary back garden was listed among "the odd things". The goat itself is scored item i08 and got 1; the oddness is not a scored contradiction.

## Scoring conventions used

- **Age and gender labels were not penalised.** The character the key calls the "teenager" (brown ponytail, blue hoodie) was described as a woman, a girl, a boy, a young person or "a person". The key's "woman" in pic_04 was described as a girl or young woman. Action items were scored on the action.
- **Box material was not penalised.** In pic_11 and pic_20 the key says "wooden box", but the describer said "cardboard box, taped shut". "Box" is an accepted phrasing, so these items scored 1.
- **Hedges on action items still scored 1 when the visible action matched an accepted phrasing.** In pic_01 i02 the describer wrote "water pouring out of" the can at the flower bed, and the unsure section hedged between watering and leaking. "Pouring water" is an accepted phrasing, so the item scored 1.
- **Inferences needed a stated reading.** An inference offered as one of two readings with no preference scored 0.5 (pic_18 i03 and i10). An inference whose main reading was stated, or named as "the likely reading", scored 1 (pic_03 i03, pic_08 i08).
- **pic_11 i03 scored 1.** The describer called the box in the sky "the odd thing" and described it as in mid-air with nobody nearby who could have thrown it. The unsure section also mentions falling or thrown, but the impossible fact itself (a box in the air with nothing holding it up) is described either way.
- **Ambiguities about meaning were not listed as oddities.** These include who someone is waving at, what is being photographed, and a character's gender.
