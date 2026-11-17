# Scores summary, set D (pic_76 to pic_100)

Coverage check: all 25 pictures and all 253 items in keys_d.json have exactly one score in scores_d.json. No item is missing and none is invented (checked by script against keys_d.json).

## Mean score by item type

| Type | Items | Sum | Mean |
|---|---|---|---|
| entity | 151 | 144 | 0.954 |
| action | 74 | 73.5 | 0.993 |
| inference | 16 | 15.5 | 0.969 |
| contradiction_notice | 6 | 6 | 1.000 |
| contradiction_explain | 6 | 6 | 1.000 |
| **all** | **253** | **245** | **0.968** |

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---|---|
| pic_76 | i07 | There are a few white clouds | 0 | Clouds not mentioned |
| pic_76 | i08 | There is a tree | 0 | No tree mentioned, only potted plants and a flower bed |
| pic_77 | i03 | There are a few white clouds | 0 | Clouds not mentioned |
| pic_77 | i04 | There is a tree | 0 | No tree mentioned |
| pic_86 | i04 | A girl is catching the ball | 0.5 | Girl holds her arms out "as if waiting to catch", but the ball is read as going over her head or over the fence |
| pic_88 | i11 | There are a few white clouds | 0 | Clouds not mentioned |
| pic_89 | i21 | There are a few white clouds | 0 | Clouds not mentioned |
| pic_91 | i07 | There are a few white clouds | 0 | Clouds not mentioned |
| pic_100 | i03 | The man is much heavier, so the girl is stuck up in the air | 0.5 | No weight reason. "Ignoring the girl and keeping her stuck up" is given as only one of two readings; the other is that he is just relaxing |

No item was scored misread.

## Judgement calls scored 1

| Pic | Id | Why it was a call |
|---|---|---|
| pic_78 | i03 | Fork named in the main text, but the unsure section also offers a garden fork or rake |
| pic_80 | i01 | Teenager called "boy" |
| pic_80 | i04 | "About to trip" is stated, and stepping past is offered as another reading |
| pic_81 | i02 | "Woman (or teenage girl)": the target is given beside another reading |
| pic_82 | i03 | Kite "seems stuck", and flying just in front of the tree is offered as another reading |
| pic_85 | i02 | Teenager called "boy" |
| pic_86 | i03 | Teenager called "boy" |
| pic_88 | i02 | Teenager called "boy" |
| pic_89 | i03 | Stealing is stated, and "just pecking at it" is offered as another reading |
| pic_89 | i04 | Teenager called "boy" |
| pic_89 | i10 | "Ice cream has fallen" is used, a near word for dropped |
| pic_89 | i14 | Feeding is stated, and a leaking bag is offered as another reading |
| pic_90 | i01 | Man called "boy" |
| pic_92 | i01 | Reading a newspaper rather than a book; the unsure section also asks whether he sits squarely on the seat |
| pic_94 | i01 | "Lead" is used, a near word for leash |
| pic_94 | i07 | Teenager called "boy" |
| pic_96 | i03 | Floating is stated, and thrown or falling is offered as a less likely reading |
| pic_97 | i03 | Kite "stuck in the tree", and flying in front of it is offered as another reading |
| pic_97 | i04 | Teenager called "boy" |
| pic_99 | i03 | Teenager called "boy" |
| pic_77 i01, pic_93 i01 | | "Puppy" is used, a near word for dog |
| pic_76 i01, pic_82 i04, pic_84 i02, pic_88 i05, pic_89 i01, pic_89 i17, pic_92 i01, pic_94 i03, pic_94 i05 | | Grandfather or grandmother called "older/old man" or "older woman": a near word, and the action is fully right |

## Unintended oddities, grouped by kind

**Depth, overlap or placement unclear (3)**
- pic_86: the ball overlaps the fence line, so it is unclear whether it is in front of or above the fence
- pic_88: the red bird on the lamp sits in front of a shop window and can look like it is at the window [bird, three-quarter front]
- pic_92: the old man seems to sit just in front of or beside the low end of the seesaw rather than squarely on its seat

**Trajectory or physics looks off (2)**
- pic_86: the thrown ball is high near the fence top, well above and behind the girl's waiting hands, as if it will sail over her or the fence
- pic_95: the washing is blown out at a steep angle, pointing right and downward, odd for pegged clothes and not quite matching the wind lines

**Animal identity or scale (2)**
- pic_93: the sleeping puppy could be read at a glance as a lamb or a cat [dog, three-quarter front]
- pic_89: the blue bird on the bench is quite large compared with the sandwich [bird, profile]

**Awkward hold or pose (1)**
- pic_91: the woman's arm and the box overlap awkwardly; the box looks held at one side of her body

**Facial expression unreadable (1)**
- pic_85: the picnicking man's face, with mouth open and eyes squinted, could be talking, shouting, laughing, yawning or chewing

Animal oddities by angle: three-quarter front 2 (pic_88 bird, pic_93 dog), profile 1 (pic_89 bird).

Pictures with no unintended oddity: 76, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 94, 96, 97, 98, 99, 100.
