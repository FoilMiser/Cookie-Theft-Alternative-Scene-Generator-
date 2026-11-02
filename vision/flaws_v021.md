# v0.21 blind screen: what it found (the work list for v0.22)

The v0.21 screen used the same method and prompts as the seventeen before it (`screen_prompts.md`). Nine readers
who never saw the key described 65 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16 showcase
pictures and 5 isomorphs) and 44 probe pictures. Three scorers with the same prompt scored pictures 1 to 22, 23 to 43
and 44 to 65 against `keys.json` (`scores_a.json` to `scores_c.json`, merged in `scores.json`). Per-template means are
in `../vision/screen_summary.json` (`by_template`; probes count there, not in the headline figures). The gate is in
`gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) | v0.13 (21) | v0.14 (21) | v0.15 (21) | v0.16 (21) | v0.17 (21) | v0.18 (21) | v0.19 (21) | v0.20 (21) | v0.21 (21) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 0.996 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.985 | 1.00 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.995 | 0.988 | 0.996 | 0.995 | 0.986 | 0.989 | 0.998 | 0.989 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 |

738 of 744 scored items had full marks. One was misread, the first in the set since v0.11: in the tier-4 street a
woman watering a planter box with a frying pan read as "watering ... with a grey watering can", so the contradiction was
neither noticed nor explained (two of the set's 16 contradiction items; its contradictions mean fell to 0.84). In the
same picture a teenager jumping for joy in front of the fruit stall read as standing "with both arms up, smiling", "could
be cheering, celebrating, stretching or dancing" (a half point). Every other item of the set had full marks: the
inferences rose to 1.00, and the things stayed at 1.00. In the probes, three half points: a ladder leaning on nothing,
"standing up at a lean ... or lying flat", twice, and the square wheel of a wheelbarrow, once more "a square dark frame
with a spoked wheel inside it". Oddities fell in the set from 26 to 24 and in the probes by half, from 68 to 34.

## The v0.20 oddities and the rules of revision 19

None of the v0.20 oddities that revision 19 addressed came back. No reader saw a worker's vest in a garden, a dog bowl
away from a dog, a head among the hung washing, a hose reel or a spare can beside someone watering, a figure in the
cattails, walkers on each other's shoulders, or a kick aimed at the sandpit. The washing was hung in three pictures and
read in full; the two v0.20 half points read in full where they were screened again (the dropped ice cream 1.00 over 12
items; the square wheel 0.967 over 15, one half point). The pond's rim drew two remarks, both dismissed by the readers:
"figures by the pond overlap the water's edge ... feet are on the bank", and an angler whose "upper body overlaps the pond
outline; at first glance he seems to be standing in the pond".

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 | 395 | 396 | 406 | 398 | 397 | 391 | 407 | 390 | 396 |

61 of 64 templates pass; every template was screened in at least three pictures (54 in three, 4 in four, 4 in five,
1 in six, 1 in seven). The three that fall short each read in full in v0.20, and each did so here in two of its three
pictures: the frying pan (0.778, the misread), the jumper (0.833, the half point) and the ladder leaning on nothing (0.889,
two half points in one probe). The v0.9 retest put the gate's reader variance at about five templates between screens.

## What reads poorly (the v0.22 list)

| # | Sev | Template | v0.21 mean | What the readers saw | Fix for v0.22 |
|---|---|---|---|---|---|
| R1 | A | `pan_watering` | 0.778 (9 items, 3 pictures; 1 misread) | In the tier-4 street, the pan held up face-on at a raised planter box, against the slate-grey shop door: "a grey watering can" ("a grey can or pot"), "nothing looks physically impossible"; its stream fell beside the box, read as "water running down the side of the planter". Read as a frying pan in its two garden probes | To the isolation bench: the pan against a dark door or wall, at a planter's height. Keep the handle in view and the pan's face turned less toward the viewer, and keep it off dark backgrounds of the same grey; the stream into the planter's flowers, not past its end |
| R2 | B | `jump` | 0.833 (3, 3) | In the tier-4 street, a teenager with both arms up in front of the fruit stall: "stands ... with both arms up, smiling with eyes closed", "cheering, celebrating, stretching or dancing". His feet were about 40 px above his shadow, with the stall's table legs behind them | A clearer gap above the shadow in crowded pictures, and the jumper's feet clear of standing structures behind them; to the bench if a gap alone does not read |
| R3 | B | `ladder_nothing` | 0.889 (9, 3) | In a park probe, a ladder on the open grass whose top ended just below the foot of a lamp post: "its top doesn't rest on the post or on anything else", but "standing up at a lean ... or lying flat on the grass" | The ladder's top kept well clear of other uprights' feet, and a shadow or ground contact that shows it standing; to the bench |
| R4 | C | `square_wheel` | 0.967 (15, 5) | In the tier-4 garden isomorph, the wheelbarrow: "a square dark frame with a spoked wheel inside it rather than a plain round wheel" (noticed as odd, not explained). The same reading as v0.20's one half point | Second screen running for this reading: to the bench, the square wheel drawn without anything round inside it |

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.22 |
|---|---|---|---|---|
| O1 | C | The sprinkler's hose "rises straight up out of the bottom edge like a stiff pipe instead of lying on the grass" | 2 probes | The hose to the picture's edge lying low along the grass (a sideways run before it leaves the picture) |
| O2 | C | Hoses hard to follow: the hose and the jet "easy to confuse at a glance"; a hose that "rises from the grass and crosses in front of the flower bed's edge up to her hand" (judged plausible); a blocked hose's bulge "under the dog's back paws ... could read as a lump" | 3 probes | Note for the pilot; the hose now drawn in front of the bed (see the README) read as meant in all three of its pictures |
| O3 | C | Extra trip stories: the boy with the ice cream "about to trip over / run into the wheelbarrow handles", a reading walker who "may step on the sleeping cat" or "may also trip over the bicycle", a runner "heading straight for the flower bed and about to trample it", a kicked ball "flying toward the woman and the washing" | 2 set pictures, 2 probes | A walker's and a runner's lane kept clear of a second trip hazard (a wheelbarrow's handles, a sleeping animal, a bicycle) and of the flower bed; the kick's line clear of anyone standing |
| O4 | C | Contact read loosely: a slide's chute ending "a little above the grass" (2), a child "slightly above the chute", a seesaw sitter whose body "overlaps the end of the plank" (2), a woman "standing in the flowers" at the bed's front edge | 4 probes | Note for the pilot (drawing style); the seesaw sitter as v0.17 |
| O5 | C | Goats in a garden or park (5); a white goat "could be read as a young sheep or a white dog" | 2 set pictures, 3 probes | None needed (an event, not a contradiction); note for the pilot, as since v0.11 |
| O6 | C | Figures: a dog's paws "drawn as white cartoon-glove hands" (the dog reading); a grey beard "could be read as a mask"; a mark under a nose "a smear of ice cream or a small moustache"; a ponytail over the eyes; a seesaw reader's head "very dark"; an unidentifiable white object in a gardener's hands | 1 set picture, 5 probes | Note for the pilot (the cast is a stand-in) |
| O7 | C | Sizes and scale: a woman with a pram "very tall: the fence reaches only her waist"; a lamp post "very tall"; a dog "unusually long and stretched" (the begging dog) | 1 set picture, 2 probes | Note for the pilot, as since v0.19 |
| O8 | C | Older ones: leaves on a path under no tree; sweeping a path with no dirt; an empty swing tilted as if moving; swing motion lines with the boy hanging straight; a jumper "high above his shadow"; a runner in a dress; a picnic basket off the blanket; a sandcastle with no bucket or spade; a neat block of blue paint; bicycle wheels "solid black discs" | 4 set pictures, 7 probes | None needed; note for the pilot, as since v0.11 |

Smaller single remarks, each in one picture: a kite string hard to follow near the swing set, washing bunched near the
line's right-hand post, eating ice cream under storm clouds, an old woman painting the top of a tall fence, washing
that "will get wet if it rains" and a watering can left out before the rain, a bench overlapping the corner of the house
and a bin small against the fence rails (both read as depth).
