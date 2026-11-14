# Scores summary, set C (pic_51 to pic_75)

Coverage check: all 25 pictures and all 299 key items in keys_c.json have exactly one score in scores_c.json. No item is missing and none is invented. This was checked by comparing the ids in the two files.

## Mean score by item type

A misread counts as 0 in the means.

| Type | Items | Mean |
|---|---|---|
| action | 85 | 1.000 |
| entity | 170 | 0.971 |
| inference | 26 | 0.962 |
| contradiction_notice | 9 | 0.944 |
| contradiction_explain | 9 | 0.889 |
| **all** | **299** | **0.975** |

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---|---|
| pic_51 | i18 | Something is wrong with the bicycle | 0.5 | Called the bike odd only because it "seems to be lying flat/on its side ... parked oddly". Nothing about the wheels. |
| pic_51 | i19 | The bicycle has square wheels, so it could not roll | misread | Read the bicycle as lying on its side on the grass. Square wheels were never mentioned. |
| pic_52 | i06 | There is a tree | 0 | No tree mentioned. |
| pic_63 | i03 | The bird is stealing the sandwich while the woman is busy reading | 0.5 | Given as one of two readings: the bird is eating her sandwich unnoticed, or it is "simply sitting next to food". |
| pic_63 | i10 | The child dropped the ice cream | 0.5 | Said the ice cream "has fallen". In the unsure section: dropped by the girl, or "the dog could have caused it". |
| pic_72 | i11 | There are a few white clouds | 0 | No clouds mentioned. |
| pic_73 | i09 | There are a few white clouds | 0 | No clouds mentioned. |
| pic_74 | i05 | There are a few white clouds | 0 | No clouds mentioned. Only wind lines in the sky. |
| pic_75 | i10 | There are a few white clouds | 0 | No clouds mentioned. Only wind lines in the sky. |

## Judgement calls scored 1

| Pic | Id | Target | Why it was a call |
|---|---|---|---|
| pic_51 | i03 | Bird stealing the sandwich | Stated only in the unsure section ("eating it unnoticed ... reads as a sneaky theft"), but stated firmly. |
| pic_52 | i01 | Girl throwing a ball | The describer also offered that the dotted line could be a string. They chose the throw reading. |
| pic_53 | i02 | Dog wants to go for a walk | Target given beside another reading: "or it is simply carrying it". |
| pic_58 | i09 | Grandmother waving | Target given beside other readings: hailing, or checking for raindrops. |
| pic_60 | i04 | Dog blocking the water | Stated in the free description. The unsure section says "not completely clear". |
| pic_60 | i11 | Man going to trip over the box | "Looks about to trip", with "might step over the box" as an alternative. |
| pic_64 | i03 | Dog wants the food | "Begging" stated in the free description. The unsure section adds "just sitting up to greet". |
| pic_67 | i02 | A man reading while walking | Near word: the key says man, the describer said boy. |
| pic_67 | i04 | Man going to trip over the box | Stated, but direction hedged ("if he is going right, he has just passed it"). |
| pic_68 | i03 | Package going to get soaked | Stated as soaked. The unsure section adds "simply where the sprinkler happens to point". |
| pic_70 | i03 | Cat about to catch the bird | "About to pounce", with "or just playing or creeping" as an alternative. |
| pic_72 | i02 | Dog wants to go for a walk | Target given beside another reading: "or it is just carrying it". |
| pic_73 | i07 | Girl jumping for joy | Jumping and smiling, with "or jumping to try to catch the red balloon" as an alternative. |
| pic_75 | i08 | Wind blew the grandmother's hat off | "Blown away" and windy, with "or something blowing past" as an alternative. |

Near words that were not treated as calls:
- Age labels: teenager and boy, grandmother and elderly or older woman, grandfather and old man.
- Object words: cardboard box for package, pram for stroller, lead for leash, sandpit for sandbox, cap for hat.

## Unintended oddities, grouped by kind

There are 11 oddities across 9 pictures. The other 16 pictures have none.

**Object contact or placement (things look floating, overlapping or pasted on): 4**
- pic_54: the two potted plants look slightly as if they float just above the grass.
- pic_64: the woman's feet seem to stand at or just inside the pond's edge, overlapping the water.
- pic_65: the roller head looks small and sits above the painted planks, almost at the top rail.
- pic_70: the branch holding the red bird sticks out of the leaf canopy at an odd angle, as if pasted on.

**Figure pose, direction or expression unclear: 4**
- pic_67: the walking boy's direction is unclear; his body and book face left while his legs stride right.
- pic_71: the seesaw is barely tilted, and the girl on the raised end still has her feet near the ground.
- pic_71: the girl looks small and hunched over the handle, so it is hard to see how she is sitting.
- pic_58: the man pushing the pram looks alarmed with no clear cause.

**Story cue confusing or misleading: 3**
- pic_52: the ball's dotted flight line could be read as a string attached to the ball.
- pic_57: the puppy lies right on the hose yet water still flows, so it is unclear whether that matters [dog, three-quarter front].
- pic_65: it is unclear which way the man is painting; the blue planks are beside him, not under the roller.

**Oddities about key animals, by angle**
- dog, three-quarter front: 1 (pic_57)
- profile (any animal): 0
- The pic_70 branch oddity is about the perch, not the bird, so it has no angle tag.
