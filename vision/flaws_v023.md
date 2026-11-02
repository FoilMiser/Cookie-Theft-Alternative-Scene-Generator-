# v0.23 blind screen: what it found (the work list for v0.24)

The v0.23 screen used the same method and prompts as the nineteen before it (`screen_prompts.md`). Nine readers
who never saw the key described 65 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16 showcase
pictures and 5 isomorphs) and 44 probe pictures. Three scorers with the same prompt scored pictures 1 to 22, 23 to 43
and 44 to 65 against `keys.json` (`scores_a.json` to `scores_c.json`, merged in `scores.json`). Per-template means are
in `../vision/screen_summary.json` (`by_template`; probes count there, not in the headline figures). The gate is in
`gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) | v0.13 (21) | v0.14 (21) | v0.15 (21) | v0.16 (21) | v0.17 (21) | v0.18 (21) | v0.19 (21) | v0.20 (21) | v0.21 (21) | v0.22 (21) | v0.23 (21) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 0.996 | 1.00 | 1.00 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.985 | 1.00 | 0.971 | 1.00 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.995 | 0.988 | 0.996 | 0.995 | 0.986 | 0.989 | 0.998 | 0.989 | 0.997 | 1.00 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 |

All 729 scored items of the 65 pictures had full marks, the set's 283 and the probes' 446: the first screen with no item
below full marks in twenty. None was misread. Oddities in the set fell from 25 to 21 and in the probes from 54 to 42. The
three scorers credited between six and twelve items each in full whose description also offered a second reading in its
"unsure" section, or left out part of the key's wording ("calling out", "upset", "can't roll"), each listed in its summary
file (`scores_summary_a.md` to `_c.md`); the prompt allows that, and a stricter scorer would have given some of them half
points.

## The v0.22 list and the bench

Every v0.22 shortfall read in full. The frying pan, redrawn on the bench, read as a frying pan in all three of its
pictures (1.00 over nine items; 0.778 in v0.21 and v0.22, a misread in each); the begging dog sitting up with its paws at
its chest as begging in all three (1.00; 0.944); the reading walker's obstacle, now a full step ahead, as a trip in all
three (1.00; 0.958). No runner and walker were said to be about to collide, no duck went for an angler's float, and no
reader saw a boot under a wheelbarrow. The older man's new profile was read as an older man in a cap in every picture he
was in, with no beard or mask; but in the tier-4 park, where the v0.22 readers had him walking toward the sleeping cat
behind him, a reader again put the cat "right by his feet, so he could trip over it or step on it", though "it is not
completely clear which way the old man is walking". The cat lies about 50 px behind his back foot on the path.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 | 395 | 396 | 406 | 398 | 397 | 391 | 407 | 390 | 396 | 394 | 382 |

All 64 templates pass, as in v0.20; every template was screened in at least three pictures (56 in three, 4 in four, 3 in
five, 1 in six). The v0.9 retest put the gate's reader variance at about five templates between screens, and the scores
are at the ceiling: the screen no longer separates the templates, and the pilot with people is the test that can.

## What reads poorly (the v0.24 list)

No template reads poorly. The list for v0.24 is oddities only.

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.24 |
|---|---|---|---|---|
| O1 | B | A sleeping cat on the path about 50 px behind a walking man's back foot: "right by his feet, so he could trip over it or step on it" (the same tier-4 park as the v0.22 reading, with the man's facing now clear) | 1 set picture | A lying or sleeping animal kept clear of any walker's feet on both sides, not only ahead of a reading walker |
| O2 | C | A small girl on playground equipment seen "slightly in front of" the slide chute or the seesaw plank, "perched rather than seated", "almost tucked behind" the plank; a seesaw plank passing behind a seated man (2) | 6 probes | Note for the pilot (contact read loosely, as since v0.21); the seesaw sitter as v0.17 |
| O3 | C | Extra stories: water from a blocked hose about to spray "into the woman's face" when the animal steps off (2); a cat beside the wet paint; a goat that "might go for the laundry next" or "eat the flowers" | 4 probes | Note for the pilot |
| O4 | C | Sizes at the back: a background figure as large as the foreground ones (3), a child small for the slide | 2 set pictures, 2 probes | Note for the pilot, as since v0.19 |
| O5 | C | Older ones: goats in a garden or park (4); wind lines with no hair or clothes blowing; a swing seat hanging crooked; a loose dog with no owner; a hole dug in the middle of the lawn; potted plants on the open lawn; a jogger on the grass, not the path | 2 set pictures, 8 probes | None needed; note for the pilot, as since v0.11 |
| O6 | C | Figures and objects: a peg by the grandmother's mouth; grey marks round a man's eyes; a hose reel with no hose read as "a wheel or a small fan"; the wooden box read as cardboard (3); the teenager read as a woman (13 items, credited) | 1 set picture, 6 probes | Note for the pilot (the cast is a stand-in); the box's key word is "box", so its material is not scored |

Smaller single remarks, each in one picture: an orange cap flying off an elderly woman's head, a picnicker looking out of
the picture, a kite string near the top of the slide, crumbs that might float, a doughnut-like pink lump, a puppy that
could be a cat.
