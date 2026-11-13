# Scores summary, set B (pic_27 to pic_51)

Completeness check: all 25 pictures and all 290 items in keys_b.json got exactly one score each. No item is missing and none was invented. Item ids match the key in order for every picture (checked by script).

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 170 | 0.94 |
| action | 77 | 1.00 |
| inference | 19 | 1.00 |
| contradiction_notice | 12 | 1.00 |
| contradiction_explain | 12 | 1.00 |
| **all** | **290** | **0.97** |

## Items scored 0, 0.5 or misread

No item was scored 0.5 or misread. All 10 losses are background entities scored 0 (not mentioned):

| Pic | Id | Target | What the describer said |
|---|---|---|---|
| pic_27 | i04 | There is a tree | no tree; lists potted plants, bench, house |
| pic_30 | i21 | There are a few white clouds | no clouds (just "sunny town street") |
| pic_31 | i07 | There are a few white clouds | no clouds ("sunny back garden") |
| pic_32 | i05 | There are a few white clouds | no clouds (only the box "up in the sky") |
| pic_33 | i07 | There are a few white clouds | no clouds |
| pic_34 | i05 | There are a few white clouds | no clouds |
| pic_34 | i06 | There is a tree | no tree |
| pic_35 | i11 | There are a few white clouds | no clouds |
| pic_35 | i12 | There is a tree | no tree |
| pic_37 | i07 | There are a few white clouds | no clouds ("sunny park") |

Pattern: 7 of the 10 are clouds, and 3 are trees. All are in pictures with a busy foreground.

## Judgement calls scored 1

| Pic | Id | Why it was a call |
|---|---|---|
| pic_28 | i04 | Kite "stuck in the leaves", but the unsure section also offers "flying just in front of the tree" (stuck called most likely) |
| pic_29 | i02 | "digging or planting". The unsure section adds "or just dug it up" (planting called more likely). Boy for teenager |
| pic_29 | i03 | Reaching for the hat, beside the reading "could be waving" (rejected by the describer) |
| pic_30 | i07 | "as if about to pounce", beside "or just walking past" |
| pic_30 | i11 | Dropping is not stated as an act: "his ice cream lies splattered". The unsure section has "crying over his dropped ice cream" |
| pic_32 | i03 | Floating box called impossible, beside "falling, blown or thrown" readings |
| pic_33 | i03 | The same: floating, beside "falling or blown/thrown" |
| pic_34 | i02/i03 | Bird pecking/stealing, beside "could be just sitting next to the sandwich" |
| pic_38 | i01 | Reaching for the cap, beside "or has just thrown it" (wind reading preferred) |
| pic_40 | i06 | Sitting on nothing, beside "could be intended as squatting" |
| pic_41 | i03 | Stalking, beside "could also just be walking" |
| pic_42 | i05 | No "sweeping" wording: "pushing dirt with a fork toward a dustpan, as if it were a broom" |
| pic_42 | i07 | Giant dinner fork, beside "possibly meant to be a rake" |
| pic_42 | i08 | Near word: "girl" for the woman sweeping |
| pic_44 | i06 | "about to trip", beside "might step around it" |
| pic_47 | i02 | Near word: "girl" for the woman eating ice cream |
| pic_48 | i03 | Fish in the tree, beside "could be a fish-shaped decoration" |
| pic_49 | i04 | Dog squashing the hose, beside "not clear it's actually pinched" |
| pic_49 | i07 | Giant dinner fork, beside "could be read as a garden fork/rake" |
| pic_51 | i03 | Near word: "girl" for the woman pointing |
| pic_51 | i04 | Rain coming, beside "or simply a cloudy day" |

General: "boy" was accepted for teenager throughout (pic_29, 30, 34, 35, 36, 41, 42, 49).

## Unintended oddities (not scored items)

6 oddities in 5 pictures. 20 pictures had none.

**Pose / support**
- pic_28: the reclining man has no visible arm propping him up, so he looks like he is floating at an angle

**Physics inconsistency**
- pic_38: the washing hangs straight down even though there is a strong wind

**Unexplained props / missing agent**
- pic_30: seeds by the red bird are far from the boy feeding the birds; unclear who put them there
- pic_42: the fruit stall has no stall-keeper

**Animals**
- pic_46: a goat in a park is a bit unusual [goat, three-quarter front]
- pic_46: the rope loops near the goat's face, so it could be read as the goat chewing the rope [goat, three-quarter front]

Animal oddities by angle: three-quarter front 2 (both goat, pic_46); profile 0.

Not counted as oddities (the describer offered them as readings, not as problems): pic_47, the woman might trip over the rock (an extra story, not in the key); pic_39, the empty seesaw is tilted (the describer calls it fine); pic_43, the man's feet sit at the pond edge.
