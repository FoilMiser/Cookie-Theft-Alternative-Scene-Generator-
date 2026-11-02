# v021 scoring summary, key set A (pic_01 to pic_22)

Inputs: `keys_a.json` and `desc_pic_01.md` to `desc_pic_22.md`. No other files were opened.
Scores: 1 = clearly conveyed, 0.5 = partly or only one of two readings, 0 = not mentioned, misread = element mentioned but read as something else. Each item was judged on the whole description file (free description, inventory and unsure section). In the means, a misread counts as 0.

**Coverage check:** `keys_a.json` has 22 pictures and 223 items. `scores_a.json` scores all 223 items exactly once. No item is missing, no item or picture was invented, and every score is one of 1, 0.5, 0 or "misread".

## Mean score by item type

| Type | n | Mean | 1 | 0.5 | 0 | misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 123 | 1.000 | 123 | 0 | 0 | 0 |
| action | 66 | 0.992 | 65 | 1 | 0 | 0 |
| inference | 12 | 1.000 | 12 | 0 | 0 | 0 |
| contradiction_notice | 11 | 0.909 | 10 | 0 | 1 | 0 |
| contradiction_explain | 11 | 0.909 | 10 | 0 | 0 | 1 |
| **all items** | **223** | **0.989** | 220 | 1 | 1 | 1 |

## Items scored 0, 0.5 or misread

| Pic | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_18 | i05 | contradiction_notice | Something is wrong with what the person is watering with | 0 | Did not flag it. Says the vessel "looks like a grey can or pot" and that "nothing looks physically impossible". |
| pic_18 | i06 | contradiction_explain | Watering the flowers with a frying pan instead of a watering can | misread | Read the frying pan as "a grey watering can" (hedged as "a grey can or pot"). Took the water running down the side of the planter as possible overwatering or spilling. |
| pic_18 | i19 | action | A teenager is jumping for joy | 0.5 | "Stands ... with both arms up, smiling with eyes closed"; "could be cheering, celebrating, stretching or dancing". Did not see a jump; the joy is only one of several readings. |

All three items below 1 are in pic_18, the busiest scene (24 items). The only contradiction missed in the whole set is the frying pan, and it was missed because the pan was read as a watering can.

## Credited, with caveats (scored 1)

- **Box material (pic_02 i02, pic_16 i01):** the box was called "cardboard", but the key says wooden. Credited because the box itself was identified.
- **What he is pointing at (pic_06 i11, pic_11 i06):** "pointing up" toward the sky is stated. The unsure section adds that he might be pointing at the bird (pic_06) or the cat (pic_11) instead of the clouds. Credited because the accepted phrasing "pointing up" is met and the rain inference was also stated.
- **Grandfather heavier (pic_13 i03):** the stated cause is that he is not paying attention ("so she is stuck up in the air"), not his weight. Credited through the accepted phrasing "he isn't noticing she's stuck".
- **Dropped ice cream (pic_18 i13):** "her pink scoop has fallen" is stated plainly. The unsure section asks whether the dog knocked it off.
- **Emotion or speech in the target text not mentioned:** upset in pic_03 i01 and calling out in pic_13 i02. Credited because the key's accepted phrasings ("reaching up", "up in the air") were met.
- **Who the teenager is:** the same teenager (ponytail, blue hoodie) is called "girl or young woman", "child", "person" and, in pic_16 and pic_19, "boy". The actions were all correct.

## Unintended oddities (reported by the describer, not scored), by kind

**Figure drawing and anatomy (5)**
- pic_06: a dark mark under the eating woman's nose could be read as a smear of ice cream or a small moustache.
- pic_09: the dog's paws are drawn as white cartoon-glove hands, so the dog looks half-human.
- pic_09: the grey area on the man's lower face could be read as a mask instead of a beard.
- pic_14: a pinkish-red mark on the child's cheek could be blush, sunburn or food.
- pic_21: the begging dog's body is unusually long and stretched, with its back legs far behind.

**Contact, support and overlap (4)**
- pic_05: the old woman and her watering can overlap the front of the flower bed, so she looks as if she is standing in the flowers.
- pic_12: the girl's legs stick out past the edge of the picnic blanket (the describer thinks this is probably just her pose).
- pic_13: the child on the slide seems to sit slightly above the chute.
- pic_13: the man's body overlaps the end of the seesaw beam, so it is unclear where he is sitting.

**Object and line drawing (3)**
- pic_04: the kite string is long and thin and hard to follow near the swing set.
- pic_09: the hose line and the water-stream line are easy to confuse.
- pic_19: the bicycle wheels are solid black discs with no spokes.

**Odd staging or implausible details (6)**
- pic_05: the washing line sags a lot, and both pieces of laundry are bunched at the right-hand post.
- pic_06: people are eating ice cream outdoors under storm clouds.
- pic_08: an old woman is painting the top of a tall fence with a roller.
- pic_14: the picnic basket is on the grass, off the edge of the blanket.
- pic_18: the water runs down the side of the planter instead of onto the flowers. This sits next to the frying-pan item, which was missed.
- pic_20: the painted part is unusually neat, a clean block of blue in the middle of an unpainted fence.

**Implied mishap not in the key (1)**
- pic_17: the kicked ball is flying toward the woman and the washing, and "might hit the laundry, the woman or the flower bed".

No unintended oddities were reported for pic_01, 02, 03, 07, 10, 11, 15, 16 or 22.
