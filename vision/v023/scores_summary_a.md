# v023 scoring summary, key set A (pic_01 to pic_22)

Sources: `desc_pic_01.md` to `desc_pic_22.md` (free description, inventory and unsure section) scored against `keys_a.json`. Scores are in `scores_a.json`.

## Completeness check

- `keys_a.json` has 22 pictures and 237 items. `scores_a.json` has 22 pictures and 237 items.
- Every key item has exactly one score. No item is missing, and no item or picture was added that is not in the key (checked by script against `keys_a.json`).
- Every score is 1, 0.5, 0 or "misread".

## Mean score by item type

| Item type | Items | Mean score |
|---|---:|---:|
| entity | 135 | 1.00 |
| action | 70 | 1.00 |
| inference | 14 | 1.00 |
| contradiction_notice | 9 | 1.00 |
| contradiction_explain | 9 | 1.00 |
| **All items** | **237** | **1.00** |

## Items scored 0, 0.5 or misread

None. All 237 items scored 1.

## Items scored 1 with a caveat (for review)

These items got full credit, but a stricter scorer might disagree.

| Pic | Item | Target | What the describer said |
|---|---|---|---|
| pic_03 | i05 | A teenager is throwing a ball | "a woman with a brown ponytail ... has just thrown a red ball" (teenager read as an adult woman) |
| pic_08 | i02 | A teenager is holding a kite string | "a woman (or girl) with a brown ponytail" |
| pic_15 | i02 | A teenager is kicking a ball | "an older girl or young woman" |
| pic_21 | i07 | A teenager is catching the ball | "a woman in a blue top with a brown ponytail" (teenager read as an adult woman) |
| pic_01 | i05 | A woman is digging | "a person with short dark hair in a yellow dress"; unsure: girl or young woman |
| pic_16 | i04 | A woman is raking leaves | "a girl or young woman" |
| pic_08 | i01 | A man is planting flowers | "placing or planting a pot"; credited because "kneeling by a flowerbed" is stated plainly |
| pic_09 | i01 | A grandfather is hanging up laundry | "hanging washing"; the unsure section says putting up or taking down |
| pic_11 | i06, i07 | Wheelbarrow wrong / square wheels, can't roll | "its wheel looks square instead of round"; unsure: "could be a deliberately wrong detail" (box alternative judged less likely); does not say it can't roll |
| pic_18 | i15 | Something is wrong with what is on her head | "a metal bucket turned upside down on her head"; states the absurd fact but never calls it odd |
| pic_18 | i18 | A child is jumping for joy | "jumps with both arms in the air"; the reason is hedged (cheering, or jumping for the cap) |
| pic_20 | i01 | A woman is planting flowers | "gardening" next to a potted flower; unsure: planting or weeding/tending |

Pattern: the teenager (brown ponytail, blue top) is read as an adult woman in all four pictures where she appears. The woman in the yellow dress is read as "girl or young woman" both times. Only the action is scored, so these did not lose credit.

## Unintended oddities, grouped by kind

These are oddities the describers reported that are not scored items.

### Figure placement and depth (character not cleanly on or in its object): 7
- pic_06: the girl sits slightly in front of the slide chute's edge, so she could look as if she is hovering above it.
- pic_07: the girl looks small and sits slightly in front of the seesaw plank, perched rather than seated.
- pic_13: the girl on the raised end of the seesaw sits low, "almost tucked behind" the plank.
- pic_15: the small girl kneels on the corner of the sandpit, partly on the frame or grass, and the sandcastle overlaps the wooden frame.
- pic_12: the woman's feet are on the path while the pram is on the grass beside it.
- pic_09: the clothesline passes just above the man's head, very close to his cap (not through it).
- pic_22: the goat's pose is awkward, with its head tucked down low near its front legs.

### Out-of-place but possible content: 4
- pic_04, pic_11, pic_22: a goat loose in a back garden is called unusual (3 pictures). In pic_04 it "might go for the laundry next", and in pic_22 it "could move on to eat the flowers".
- pic_05: the flying hat is an orange baseball cap, "slightly unexpected on an elderly woman", and is never shown on her head, so whose hat it is is uncertain.

### Physics or motion inconsistencies: 2
- pic_18: there are strong wind lines, but no one's clothes or hair are blowing ("a small inconsistency").
- pic_05: the swing seat hangs crooked, with its ropes at different angles; "looks a bit odd" (read as the wind moving it).

### Unclear objects or details: 3
- pic_01: there is a small dark shape by the grandmother's raised hand near her face, either a peg in her hand or a peg in her mouth.
- pic_09: there are light grey marks around the man's eyes, either glasses or just grey hair and beard.
- pic_17: the teal hose reel has no hose coming out of it, so it could be a wheel or a small fan.

### Gaze and layout: 2
- pic_10: the girl on the picnic blanket looks out of the picture, not at anything in it.
- pic_14: the jogger runs on the grass, not on the path.

Pictures with no unintended oddities: pic_02, 03, 08, 16, 19, 20, 21.
