# v0.16 blind screen: what it found (the work list for v0.17)

The v0.16 screen used the same method and prompts as the twelve before it (`screen_prompts.md`). Nine readers
who never saw the key described 64 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16 showcase
pictures and 5 isomorphs) and 43 probe pictures. Three scorers with the same prompt scored pictures 1 to 21, 22 to 43
and 44 to 64 against `keys.json` (`scores_a.json` to `scores_c.json`, merged in `scores.json`). Per-template means are
in `../vision/screen_summary.json` (`by_template`; probes count there, not in the headline figures). The gate is in
`gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) | v0.13 (21) | v0.14 (21) | v0.15 (21) | v0.16 (21) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.995 | 0.988 | 0.996 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 |

For the second screen running no item anywhere was misread, set or probes. Across all 64 pictures 743 of 746 scored
items had full marks (0.998, against 0.995 in v0.15): three half points, two in the set and one in a probe, and no
zero. The set's inferences rose from 0.95 to 0.99, the highest of any screen. Oddities in the set fell from 29 to 23,
and in the probes from 39 to 37.

## The v0.15 failures and the visuals refined in v0.16

| Template | v0.15 | v0.16 | What the readers saw in v0.16 |
|---|---|---|---|
| `cat_stalks_bird` | 0.89 (9 items, 3 pictures) | 0.96 (12, 4) | Read as stalking in all four pictures, three of them crowded tier-4 pictures: "creeping along the top of the fence toward the bird ... as if about to pounce"; on a street, "creeping ... low and stretched out ... as if stalking". The half point: on the ground in the tier-4 park, the crouch read as "leaping/running toward" the bird, though "as if about to pounce" was right. No second cat shared a stalked fence, and no reader saw a pointing hand aimed at an animal |
| `seesaw_heavy` | 0.88 (12, 4) | 1.00 (9, 3) | Stuck in all three, the set picture a busy playground again: "stuck up in the air on the high end, kicking her legs ... the man doesn't seem to notice she can't get down"; "Because he is heavy and sitting still, the other end is stuck up in the air". No reader mentioned her calling out |
| `bird_perched` | 0.83 (3, 3) | 1.00 (5, 5) | On the garden fence, the lamp and the railing; none on a clothesline. One, on the playground railing just where the slide's platform stands in front of it, was read "on top of the slide" (scored right, as the item asks only for a perched bird; below, O2) |

The other visuals refined for the v0.15 oddities read in full wherever they were screened: the star jump in all
three of its pictures (no reader said "floating"; one wondered whether the shadow under the feet was "a drawing offset"), the watering can's
shower and the frying pan's pour (12 items), the sleeping baby in the pram (4), the lower catch (8), the dog by the door
(6), the readers' open-eyed faces (3), the low kick (3) and the square-wheeled bicycle (9). No reader saw a figure too
big for the playground's railing, a door knob on a dog's head, a figure standing over another's feet, a pointing hand
aimed at the wrong thing, water as "linked blobs", a baby with no face or a pram's blanket as "a lid", or a jumper
reaching for the washing.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 | 395 | 396 | 406 | 398 |

63 of 64 pass, every template screened in at least three pictures (52 in three, 7 in four, 3 in five, 2 in six). All
three v0.15 failures pass. One template falls short on a single hedge, in a probe:

## What reads poorly (the v0.17 list)

| # | Sev | Template | v0.16 mean | What the readers saw | Fix for v0.17 |
|---|---|---|---|---|---|
| R1 | C | `photo` | 0.83 (3 items, 3 pictures) | In a probe that put the photographer in a park with nobody else: "holds binoculars or a camera up to his face ... birdwatching or taking a photo", "looks ... at nothing visible". In another probe, read as taking a photo, "the object at the photographer's face could be binoculars"; in the set, "unclear what the photographer is photographing". Read in full in its two other pictures (v0.15: 1.00) | The camera drawn so it cannot be binoculars (one lens pushed forward, a flash on top), and the photographer placed only with someone or something to photograph in front of the lens (a probe falls back to the pond today) |

Two more half points, both passing: `ducks_bread` (0.94), a duck's motion lines "could mean it is swimming quickly
toward the food, or just that it is moving"; and the stalking cat on the ground above.

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.17 |
|---|---|---|---|---|
| O1 | C | The sprinkler's drops above the box it soaks "could be water coming out of the box"; a sprinkler and a box on a park path, "an odd thing to find in a park" | 3 set pictures | The drops drawn landing on the box (the arcs ending on its lid, a splash there), none above it; the park's sprinkler on the lawn, off the path |
| O2 | C | A bird on the playground railing where the slide's platform stands in front of it read "on top of the slide" (its key said "on the fence") | 1 set picture | Railing perches clear of the slide, the swing frame and the seesaw, as the garden fence's are clear of the clothesline |
| O3 | C | A pram "heading toward the birds and the man feeding them, might run into them" | 1 probe | The lane reached only a little behind the pusher's own depth; the pram's lane to take in figures standing just behind it too |
| O4 | C | Things at the same depth that touch: a man whose feet are at the back edge of a bench ("standing behind it or partly overlapping it"), a man overlapping the pond's edge, a dog "on the doorstep behind the bench or perched on top of the bench", a sandwich "on his lap or on the bench" | 2 set pictures, 2 probes | The feet rule extended to benches and the pond's rim |
| O5 | C | Animals taken for others: the dog reading a newspaper "could be a goat"; the goat "a goat, lamb or kid", "a lamb or a white dog" | 2 set pictures, 2 probes | The goat's horns and beard drawn larger; the reading dog's ear less like a horn |
| O6 | C | Runners with "no visible reason": "running to the left with no visible reason", "may be running after something" | 2 set pictures | None needed for legibility (a jogger is an ordinary event); note for the pilot |
| O7 | C | Drawing quirks: a rubbish bin cut off by the picture's edge (3 pictures); wheelbarrow handles raised "as if tipped" (2); a hose's bulge "much fatter than a real hose could swell"; a bicycle's wheels "solid black discs with no spokes"; swing ropes straight while motion lines show swinging | 2 set pictures, 6 probes | Fillers kept inside the frame; the wheelbarrow's handles resting low; a smaller bulge |
| O8 | C | Older ones: wind that leaves the trees and people still; leaves on a path far from any tree; a goat in a garden or park; a market stall with nobody at it; a kite near the sun | 5 set pictures, 2 probes | None needed (events, not contradictions, or drawing style); note for the pilot, as since v0.11 |

Smaller single remarks, each in one probe: a kicker whose face is hidden by the hair ("could be ... back-heeling the
ball", as in v0.15), a dog's lead that "could read as a red hose" beside the hose reel, a carrier with one hand
clearly on the box, a swing frame "with only one seat", unreadable marks on a hi-vis vest, and a duck whose beak near
the float read as "about to take the bait".

None of the v0.15 oddities came back as reported then: no one stood too big at the back of the playground, no door
knob sat on a dog's head, no figure stood over another's feet, no walker or ball headed for another event's objects
(the pram above was a near miss behind its lane), no jumper seemed to float, no water read as blobs, and every baby in
a pram had a sleeping face.
