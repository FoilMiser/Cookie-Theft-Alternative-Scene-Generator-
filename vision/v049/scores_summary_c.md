# v0.49 picture-description scores, set c (pic_43 to pic_64)

Coverage check: all 22 pictures and all 239 key items in keys_c.json have exactly one score in scores_c.json. None is missing and none is invented (checked by comparing item ids against the key).

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 150 | 0.967 |
| action | 61 | 1.000 |
| inference | 16 | 1.000 |
| contradiction_notice | 6 | 1.000 |
| contradiction_explain | 6 | 1.000 |
| **all** | **239** | **0.979** |

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Describer said |
|---|---|---|---|
| pic_44 | i08 | There are a few white clouds | 0: clouds not mentioned (only "a sunny back garden") |
| pic_45 | i03 | There are a few white clouds | 0: clouds not mentioned |
| pic_47 | i11 | There are a few white clouds | 0: clouds not mentioned |
| pic_48 | i05 | There are a few white clouds | 0: clouds not mentioned |
| pic_49 | i06 | There are a few white clouds | 0: clouds not mentioned |

No item scored 0.5 or misread. All five misses are the clouds item, in pictures 44 to 49. From pic_50 on, the describer lists "two clouds" or "sun and clouds" every time.

## Judgement calls scored 1

| Pic | Id | Why it was a call |
|---|---|---|
| pic_43 | i09 | "boy" for the teenager who is waving |
| pic_44 | i05 | the girl is "throwing a ball between them" with the woman, but which way the ball goes is left open; credited through "playing catch" |
| pic_44 | i06 | the woman is "catching or just having thrown it", so catching is one of two readings; credited through "playing catch" |
| pic_46 | i03 | pointing up at the clouds is credited; the unsure section adds that he may be warning the man |
| pic_47 | i01 | "boy" for the teenager, and he holds a kite reel rather than a string |
| pic_48 | i01 | the unsure section says he may be perched beside the seesaw rather than on it |
| pic_48 | i02 | her hand near her mouth is read three ways (calling, thinking, worried); "stuck up in the air" is stated outright |
| pic_49 | i01 | "boy" for the teenager |
| pic_49 | i02, i03 | "begging, or just looking up at the boy"; the describer settles on begging |
| pic_52 | i01 | "girl or young woman" for the woman |
| pic_53 | i03 | "as if begging"; the unsure section says "about to beg or jump" |
| pic_53 | i04 | "boy or young man" for the man |
| pic_54 | i01 | "man (or teenage boy)" |
| pic_54 | i02 | the bird "may be eating the sandwich or just standing next to it"; settles on pecking |
| pic_54 | i05 | the sun appears only in the inventory's background line |
| pic_55 | i08 | kite "stuck in the tree or flying just in front of the tree"; stuck is judged more likely |
| pic_55 | i09 | reaching up and holding balloons are both stated; upset is not |
| pic_55 | i11 | the balloon "has escaped", but the unsure section says it "may belong to someone else" |
| pic_56 | i01 | goat stated, but the unsure section says it might be a sheep or a kid |
| pic_56 | i02 | "girl or young woman" for the woman |
| pic_57 | i05 | the sun appears only in the inventory's background line |
| pic_61 | i08 | the free description calls it "a windy day"; the sun is only in the inventory |
| pic_62 | i02 | the raised arm "could be reaching for the escaped balloon or waving"; settles on reaching, and he looks upset |
| pic_62 | i09 | only "gate" is named, no fence; "gate" is an accepted phrasing |
| pic_64 | i02 | "boy" for the teenager |

## Unintended oddities, grouped by kind

**Animal rendering or identity (4)**
- pic_57: the dog seems to be wearing glasses, or its dark eye area could be markings [dog, profile]
- pic_58: the dog seems to be wearing glasses or goggles, or they may be face markings [dog, profile]
- pic_56: the goat's small dark horns could be read as ears, so it might be a sheep or a kid [goat, profile]
- pic_47: the bird is sitting on the freshly painted, still-wet part of the fence, which looks like a problem [bird, profile]

**Unclear placement or contact (1)**
- pic_48: the man sits near the low end of the seesaw rather than at the very end, so he may be beside it rather than on it

**Object pose (1)**
- pic_61: the empty swing seat is tilted, maybe by the wind or maybe just an odd drawing

Oddities about animals, counted by angle: profile 4 (dog 2, goat 1, bird 1); three-quarter front 0.

The sprinkler soaking the box (pic_43, pic_47), the ladder (pic_50), the fork (pic_51, pic_52), the dog reading (pic_57, pic_58) and the bucket hat (pic_61) were also reported as wrong, but they are scored items, so they are not listed here.
