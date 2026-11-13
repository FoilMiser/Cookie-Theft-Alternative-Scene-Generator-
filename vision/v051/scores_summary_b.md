# Scores summary, set B (pic_27 to pic_51)

Completeness check: all 25 pictures and all 290 key items in keys_b.json have exactly one score in scores_b.json. No item is missing, none is duplicated and none is invented. This was checked by script against the key ids.

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 170 | 0.988 |
| action | 77 | 0.994 |
| inference | 19 | 1.000 |
| contradiction_notice | 12 | 1.000 |
| contradiction_explain | 12 | 1.000 |
| **all** | **290** | **0.991** |

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---|---|
| pic_30 | i21 | There are a few white clouds | 0 | Says "sunny town square" but never mentions clouds |
| pic_42 | i11 | There are a few white clouds | 0 | Says "sunny town street/plaza" but never mentions clouds |
| pic_47 | i02 | A woman is eating an ice cream | 0.5 | A "girl" holds a cone up and looks down at it. Eating comes up only as a hedge ("or about to lick it") |

No item was scored misread.

## Judgement calls scored 1

| Pic | Id | Target | Why it was a call |
|---|---|---|---|
| pic_28 | i04 | Kite got stuck in the tree | Says stuck, but the unsure section also offers "flying just in front of the tree" |
| pic_29 | i03 | Grandmother reaching up for the hat | The unsure section also offers "waving at someone" |
| pic_30 | i07 | Cat about to catch the bird | Says "as if about to pounce", but the unsure section also offers "just walking past" |
| pic_30 | i08 | Child holding an empty cone, upset | Crying is clear, but the empty cone is only "may be holding" |
| pic_30 | i11 | Child dropped the ice cream | Never says "dropped it" outright. Credited from "dropped pink ice cream" plus "cone presumably in the crying boy's hand" |
| pic_32 | i02 | Something is wrong with the box | Offers "falling, blown by the wind, or impossible", with impossible as one of three readings |
| pic_32 | i03 | Box floating with nothing holding it up | Describes the fact itself ("nothing holding it"), but also offers falling or thrown |
| pic_33 | i02 | Something is wrong with the box | Says only "no explanation". Floating or thrown are both offered |
| pic_33 | i03 | Box floating with nothing holding it up | States "nothing holding it up", but the unsure section offers thrown over the fence |
| pic_34 | i02 | Bird pecking at the sandwich | "next to/pecking at". The unsure section says it could just be standing beside it |
| pic_35 | i03 | Dog wants some of the food | Credited from "begging", which the key accepts. No explicit "wants the food" |
| pic_38 | i03 | Wind blew the man's hat off | The unsure section also offers "the man having just thrown it" |
| pic_40 | i05 | Something wrong with how the person sits | The free text only says "but there is no chair". "Odd" appears as one of two readings in the unsure section |
| pic_41 | i03 | Cat about to catch the bird | Says "about to pounce", with "could just be walking" as the other reading |
| pic_42 | i08 | A woman is sweeping | Near word: calls her a "girl" (purple top, teal trousers) |
| pic_44 | i03 | Dog wants some of the food | Credited from "begging toward the ice cream", which the key accepts |
| pic_46 | i02 | Man eating an ice cream | The free text says eating, but the unsure section says "eating or about to bite" |
| pic_49 | i02 | Dog standing on the hose | Says "looks like its feet are on the hose", with "just standing beside it" offered |
| pic_51 | i03 | A woman is pointing up at the sky | Near word: calls her a "girl" (purple top, teal trousers) |

## Unintended oddities, grouped by kind

**Person not resting on their support (floating a little or offset)**: 3
- pic_29: the girl seems to sit slightly in front of the swing seat
- pic_39: the girl appears slightly above the slide surface, as if floating a little
- pic_50: the girl seems to sit just above the seesaw plank rather than on it

**Person overlapping or placed at the edge of scenery (depth or placement)**: 2
- pic_46: the man stands right at or slightly over the pond's edge, almost stepping into it and almost touching the lamp post
- pic_47: the girl's upper body overlaps the pond's front edge

**Unclear motion or direction**: 1
- pic_47: the girl's walking direction is unclear (toward the rock or away)

**Scene-level inconsistency**: 2
- pic_29: windy enough to blow off a hat and leaves, yet the clouds and swing look calm
- pic_32: the garden being empty of people seems unusual

**About animals**: none. No unintended oddity concerned an animal, so the count by angle is zero for every angle (profile 0, three-quarter front 0).

Most common kind: a child drawn slightly off their seat or slide (swing, slide, seesaw), 3 of 8 oddities.
