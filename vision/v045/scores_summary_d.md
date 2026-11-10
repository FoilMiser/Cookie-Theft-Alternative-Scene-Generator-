# Scores summary, set D (pic_71 to pic_93, v0.45)

Scored from desc_pic_71.md to desc_pic_93.md against keys_d.json. A misread counts as 0 in the means.

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 145 | 1.000 |
| action | 70 | 1.000 |
| inference | 18 | 1.000 |
| contradiction_notice | 8 | 0.938 |
| contradiction_explain | 8 | 0.875 |
| all | 249 | 0.994 |

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_90 | i11 | contradiction_notice | Something is wrong with the dog | 0.5 | notices an oddity only about the newspaper (floating, or held up by the puppy), not that the dog is doing something dogs can't |
| pic_90 | i12 | contradiction_explain | The dog is reading a newspaper, but dogs can't read | misread | read as a puppy with paws on a newspaper that seems to float in the air; never says the dog is reading |

No item scored 0.

## Unintended oddities by kind

Figure posed against an object, contact unclear (3):
- pic_73: the man sits slightly past the end of the seesaw plank; his seating looks awkward
- pic_93: the man's legs and body overlap the seesaw board, unclear whether he sits on it
- pic_90: the newspaper hangs in the air in front of the puppy with nobody holding it [dog, profile]

Swing drawing (2):
- pic_75: the swing hangs still despite the strong wind
- pic_78: the swing seat hangs high off the ground on short ropes

Water or hose drawing (2):
- pic_86: water comes out of the pan's edge in a steady spout-like stream
- pic_91: the hose bulges between the dog and the reel; possibly a drawing glitch

Motion direction unclear (1):
- pic_72: the boy faces right but the ball is at his trailing foot, so the kick direction is unclear

Oddities about animals, by angle:
- profile: 1 (pic_90 dog, newspaper floating in front of it)
- three-quarter front: 0
- three-quarter back: 0

Pictures with no unintended oddity: pic_71, 74, 76, 77, 79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 92.

## Completeness check

keys_d.json lists 249 items across 23 pictures. scores_d.json has exactly one score for each, with the same ids in the same order; none is missing and none is invented (checked by script).
