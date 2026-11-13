# Scores summary, set d (pic_78 to pic_102)

Completeness check: I compared scores_d.json against keys_d.json. All 249 keyed items across the 25 pictures have exactly one score each. No item is missing and no item was added.

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 151 | 0.934 |
| action | 72 | 1.000 |
| inference | 16 | 1.000 |
| contradiction_notice | 5 | 1.000 |
| contradiction_explain | 5 | 1.000 |
| **all** | **249** | **0.960** |

## Items scored 0, 0.5 or misread

All 10 are entity items scored 0. No item was scored 0.5 or misread.

| Pic | Id | Target | What the describer said |
|---|---|---|---|
| pic_78 | i08 | There are a few white clouds | nothing about clouds ("sunny back garden") |
| pic_80 | i05 | There are a few white clouds | nothing about clouds |
| pic_81 | i04 | There are a few white clouds | nothing about clouds |
| pic_82 | i07 | There are a few white clouds | nothing about clouds |
| pic_82 | i08 | There is a tree | no tree mentioned (lists house, fence, gate, path, flower bed, hose reel) |
| pic_83 | i05 | There are a few white clouds | nothing about clouds |
| pic_84 | i07 | There are a few white clouds | nothing about clouds |
| pic_84 | i08 | There is a tree | no tree mentioned |
| pic_85 | i06 | There are a few white clouds | nothing about clouds |
| pic_94 | i04 | There are a few white clouds | nothing about clouds ("sunny town square") |

## Judgement calls scored 1

**The describer used a near word for a person:**
- "teenager" described as a "boy": pic_79 i03, pic_84 i05, pic_85 i04, pic_88 i04, pic_89 i04, pic_90 i05, pic_93 i03, pic_97 i04, pic_99 i02. The action was always right.
- pic_87 i02: the key's "man" sweeping was described as a "boy" sweeping. The action was right but the age was not.
- pic_98 i03: "woman" described as a "young woman or teenage girl".
- "grandfather" or "grandmother" described as an "older man", "old man", "older woman" or "old woman": pic_81 i02, pic_91 i01, pic_93 i01, pic_95 i01, pic_96 i01, pic_97 i01, pic_100 i04, pic_100 i05, pic_101 i01.

**The describer gave the target beside another reading, or gave it only partly:**
- pic_78 i02: the free description says the dog is asking for a walk, but the unsure section adds "or just carrying it".
- pic_78 i04: "holding balloons, reaching up" is there, but "upset" is not.
- pic_78 i06: the free description says she let the balloon go, but the unsure section offers a separate balloon floating by.
- pic_82 i03: the free description says "nothing holds the box up", but the box is also called "flying or falling", and the unsure section offers "thrown".
- pic_83 i03: the duck is "pecking at bread pieces". The key accepts this as "the duck is eating the bread", but the motive is not stated.
- pic_88 i04: pointing at the sky or clouds, with "or the man/fence" in the unsure section.
- pic_89 i06: "frying pan (or saucepan)".
- pic_96 i03: the describer said she is stuck up high, the man does not notice and she wants to come down. They did not say he is heavier. Credited through the key's accepted phrasings "the child can't get down" and "he isn't noticing she's stuck".
- pic_97 i03: the inventory says "stealing", but the unsure section says the bird "might be just standing next to it".
- pic_97 i09: "as if about to pounce", but the unsure section says it "could also be a cat simply walking".
- pic_97 i13: "has fallen on the ground", which is close to "dropped".
- pic_97 i19: square wheels were noted, but the describer did not say the bike could not roll.
- pic_102 i06 and i07: the wheelbarrow's "square-ish" wheel appears only in the unsure section.

**Accepted near words:**
- pic_81 i07: "trees and bushes around" for "big tree".
- pic_87 i06: "birdhouse" for "bird feeder".
- pic_100 i13: "flower boxes" for "flowers".

## Unintended oddities, grouped by kind

There are 8 oddities across 7 pictures. The other 18 pictures had none.

- **Figure drawing or pose (2)**
  - pic_81: the man's stride looks reversed, as if he is stepping backward.
  - pic_87: the man's back foot looks detached from his leg.
- **Overlap or depth (2)**
  - pic_81: the man's upper body overlaps the pond's water.
  - pic_83: the woman's body overlaps the pond outline, as if she is partly over the water.
- **Animal identity (1)**
  - pic_83: the duck's small head and beak could read as a goose or swan [duck, profile].
- **Scale or proportion (1)**
  - pic_86: the fishing rod is very long, reaching nearly across the pond.
- **Physical or scene logic (2)**
  - pic_98: the seesaw is nearly level although the boy looks bigger than the girl.
  - pic_99: there is a pile of leaves on the path with no tree overhead.
- **Gaze direction (1)**
  - pic_102: the boy looks up and to the left while his kite is up and to the right.

**Oddities about animals, by angle:** profile 1 (the duck in pic_83); three-quarter front 0.
