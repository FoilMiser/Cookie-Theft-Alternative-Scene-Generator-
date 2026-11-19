# Scores summary, set e (pic_109 to pic_134)

Completeness check: I compared every picture and item id in keys_e.json with scores_e.json. All 26 pictures and all 254 items have exactly one score each. No item is missing and none was added.

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 162 | 0.926 |
| action | 62 | 0.984 |
| inference | 12 | 1.000 |
| contradiction_notice | 9 | 1.000 |
| contradiction_explain | 9 | 1.000 |
| **all** | **254** | **0.949** |

## Items scored 0, 0.5 or misread

No item was scored misread.

| Pic | Id | Score | Target | What the describer said |
|---|---|---|---|---|
| pic_113 | i05 | 0 | There are a few white clouds | no clouds mentioned (wind lines only) |
| pic_114 | i06 | 0 | There are a few white clouds | no clouds mentioned |
| pic_115 | i10 | 0 | There are a few white clouds | no clouds mentioned |
| pic_116 | i06 | 0 | There are a few white clouds | no clouds mentioned |
| pic_118 | i14 | 0 | There are a few white clouds | no clouds mentioned |
| pic_119 | i03 | 0 | There are a few white clouds | no clouds mentioned |
| pic_122 | i04 | 0 | There are a few white clouds | no clouds mentioned |
| pic_122 | i05 | 0 | There is a tree | no tree mentioned |
| pic_123 | i03 | 0 | There are a few white clouds | no clouds mentioned |
| pic_125 | i12 | 0 | There are a few white clouds | no clouds mentioned |
| pic_126 | i04 | 0 | There are a few white clouds | no clouds mentioned |
| pic_127 | i07 | 0 | There are a few white clouds | no clouds mentioned |
| pic_120 | i01 | 0.5 | A man is carrying a shopping bag | "a boy in a red T-shirt and blue jeans ... carrying a yellow shopping bag": action right, figure called a boy |
| pic_125 | i01 | 0.5 | A man is painting the fence | "a boy in a red T-shirt and jeans is painting the fence": action right, figure called a boy |

## Judgement calls (score 1)

There were no "near" calls. All 14 calls are "two".

| Pic | Id | Call | Why |
|---|---|---|---|
| pic_109 | i02 | two | says the upward water is odd, but also offers "a stylised pour" |
| pic_109 | i03 | two | water arcs upward "rather than pouring down", with splash or stylised pour also offered |
| pic_109 | i05 | two | play-bow wanting to play, but "or as crouching" is also offered |
| pic_111 | i02 | two | eating the ice cream, "or just holding it near her face" |
| pic_113 | i03 | two | wind blew the hat off, but the cap might have been thrown up by the woman |
| pic_114 | i03 | two | box floating with no support, "could be falling (dropped or blown)" |
| pic_117 | i03 | two | kicking the ball, "or ... about to kick it" |
| pic_125 | i04 | two | dog stepped in the paint (likely), "or being painted on purpose" |
| pic_125 | i07 | two | about to trip over the bucket, "or may walk past it" |
| pic_125 | i10 | two | floating box is impossible, but "could be read as falling or thrown" |
| pic_127 | i03 | two | water goes up instead of down, but a hose-spray reading is also mentioned |
| pic_129 | i02 | two | dog wants a walk, "could also just be carrying it" |
| pic_130 | i04 | two | square wheel, or "a badly drawn wheel seen from an odd angle" |
| pic_131 | i02 | two | dog's play-bow wanting to play, "or stretching" |

## Unintended oddities, grouped by kind

Only 3 of the 26 pictures had one (one each). None concerns an animal, so there is no count by animal angle (all animal angles: 0).

- **Object construction:** pic_130: the wheelbarrow handles point right while the tray faces left, so it looks oddly constructed.
- **Figure contact or placement:** pic_131: the child sits slightly above the slide surface and looks detached from the chute.
- **Figure contact or placement:** pic_133: the man walks on the grass beside the path while the pram is on the path.

Animal oddities by angle: none (three-quarter front 0, profile 0).
