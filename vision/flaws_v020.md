# v0.20 blind screen: what it found (the work list for v0.21)

The v0.20 screen used the same method and prompts as the sixteen before it (`screen_prompts.md`). Nine readers
who never saw the key described 65 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16 showcase
pictures and 5 isomorphs) and 44 probe pictures. Three scorers with the same prompt scored pictures 1 to 22, 23 to 43
and 44 to 65 against `keys.json` (`scores_a.json` to `scores_c.json`, merged in `scores.json`). Per-template means are
in `../vision/screen_summary.json` (`by_template`; probes count there, not in the headline figures). The gate is in
`gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) | v0.13 (21) | v0.14 (21) | v0.15 (21) | v0.16 (21) | v0.17 (21) | v0.18 (21) | v0.19 (21) | v0.20 (21) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.985 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.995 | 0.988 | 0.996 | 0.995 | 0.986 | 0.989 | 0.998 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 |

No item in any of the 65 pictures was misread or missed outright: 744 of 746 scored items had full marks and two had
half points, the fewest of any screen. For the ninth screen running no item in the set was misread, and every
contradiction in the set was read in full. The set's actions rose from 0.99 to 1.00 and its inferences from 0.96 to
0.985. Its one half point: in the tier-4 street a girl with an empty cone beside the dropped ice cream read as "crying"
over "a dropped ice cream", without saying it was hers. The other half point was in a probe, where the square-wheeled
wheelbarrow was offered two readings, "a square wheel ... or a normal round wheel inside a square frame". Oddities fell
in the set from 27 to 26 and rose in the probes from 52 to 68, almost all small (below). Two of three scorers gave no
half point at all; one listed seven hedged items it credited in full.

## The v0.19 failures and the visuals refined in v0.20

| Template | v0.19 | v0.20 | What the readers saw in v0.20 |
|---|---|---|---|
| `bucket_hat` | 0.889 (9 items, 3 pictures) | 1.00 (9, 3) | The silver pail read as a bucket in all three, at the back of the playground too: "wearing an upside-down metal bucket on his head like a hat, which is odd", "a grey metal bucket upside down on his head", "a white bucket upside down on her head like a hat". No reader said hat, fez or pot |
| `drink_bench` | 0.833 (3, 3) | 1.00 (3, 3) | "Drinking from a red cup through a straw" in all three |
| `ice_cream` | 0.875 (4, 4) | 1.00 (3, 3) | Never beside a dropped ice cream: "walking along the path holding a pink ice cream cone", "licking a pink ice-cream cone with his eyes closed, enjoying it", "holding up a pink ice-cream cone" |
| `jump` | 0.833 (3, 3) | 1.00 (3, 3) | No bird near: "leaping into the air with both arms raised, as if jumping for joy", "jumping in the air with both arms up and a big happy, open-mouthed face", "jumping in the air with both arms up and a happy face" |

The visuals and rules refined for the v0.19 oddities read as meant wherever they were screened. The wheelbarrow, standing,
drew no remark in any of its pictures (no screened picture had the blown swing seat); no reader saw a dug hole on the path, a ladder over
the pond or a foot on the sandpit frame, and the ladder read as "leaning on nothing" in all three of its pictures. The
dropped ice cream read in full in three of its four pictures with no second cone near it, and no runner shared a
picture with it. One reader still saw a watering can's water land "at the front edge of the flower bed" (O4).

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 | 395 | 396 | 406 | 398 | 397 | 391 | 407 | 390 |

All 64 templates pass, for the first time: every template screened in at least three pictures (51 in three, 10 in
four, 1 in five, 2 in six). All four v0.19 failures pass in full. The retest of the v0.9 pictures put the gate's reader
variance at about five templates between screens, so a full pass is not proof that nothing would fall short with other
readers: two templates (`ice_cream_drop` 0.969 and `square_wheel` 0.944) passed with a half point each.

## What reads poorly (the v0.21 list)

No template failed. The two half points:

| # | Sev | Template | v0.20 mean | What the readers saw | Fix for v0.21 |
|---|---|---|---|---|---|
| R1 | C | `ice_cream_drop` | 0.969 (16 items, 4 pictures) | In the tier-4 street, the girl with the empty cone was "crying" over "a dropped ice cream" but not said to have dropped it; a reading man and a dog walker overlapped just behind her (O6) | None needed for the item (read in full in three pictures); the overlap below |
| R2 | C | `square_wheel` | 0.944 (9, 3) | In a garden probe, the wheelbarrow's wheel: "a square wheel ... or a normal round wheel inside a square frame" | None needed (read in full in two pictures and noticed as odd in all three); note for the pilot |

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.21 |
|---|---|---|---|---|
| O1 | C | A worker in a hi-vis vest and cap painting or pointing in a home garden, "out of place" (3) | 3 probes | Keep the delivery outfit out of the garden's own chores |
| O2 | C | A dog bowl far from any dog, "a full food bowl with no pet near it" (5) | 1 set picture, 4 probes | The bowl only beside a dog, or not drawn |
| O3 | C | The washing line: a yellow shirt behind a head read as part of the clothes (3); jeans on the line against the blue-painted fence, washing "in front of the freshly painted fence" | 4 probes | Heads clear of the hanging washing; no painting under the line |
| O4 | C | Watering beside a spare tool: a can with an unused hose reel beside it (2), a hose with an unused can (1); a can's water "at the front edge of the bed" (1); a reel with "a very short loose end" (1); the sprinkler's hose off the picture's edge beside a second hose (1) | 6 probes | No hose reel beside the can (as beside the pan since v0.19), and no spare can beside a hose; the stream's end further into the bed |
| O5 | C | At the pond: a man "overlaps the right edge of the pond", cattails at his hip (1); a cattail behind a head (2); a runner "very close to the pond edge" (1) | 4 probes | People clear of the cattails and the pond's rim |
| O6 | C | Figures overlapping: in the tier-4 street a reading man and a dog walker "overlap closely in front of the stall" (60 px apart in depth); a goat behind a man "attached to his shoulder" | 1 set picture, 1 probe | A gap between figures of different events up to about 80 px apart in depth, not only 40 |
| O7 | C | Motion read oddly: a seesaw "almost level" (3); swing motion lines with the chains hanging straight (1); a jumper "floating" (1, dismissed as mid-air) | 1 set picture, 4 probes | Note for the pilot |
| O8 | C | Extra stories: a kicked ball heading for the sandcastle; a runner "may be running to catch the balloon"; a girl and a woman "heading toward each other"; the painted-paw dog about to spread more paint; the painter who "has not noticed" the dog | 3 set pictures, 2 probes | The kick's line clear of the sandpit; the rest note for the pilot |
| O9 | C | Gaze and facing: a kite flyer facing away from her string; wavers facing the viewer (2); a cat between two birds; a dog's head turned to the viewer; a jogger facing across the path | 2 set pictures, 5 probes | Note for the pilot (the cast is turned three-quarters by design) |
| O10 | C | Sizes: a bird on a bench "very large" (2); a woman at the back "nearly the same size as the man in front"; ground birds "a blue jay and a cardinal rather than park pigeons" | 2 set pictures, 2 probes | Note for the pilot, as since v0.19 |
| O11 | C | Older ones: a stall with nobody at it (2); goats (3); leaves on a path under no tree; digging in a park; a dog walker in a private garden; the bicycle standing on its own; wind that reaches only the cap; a pram on the grass (2); a playground with no swing set; a bird on wet paint | 7 set pictures, 8 probes | None needed (events, not contradictions, or drawing style); note for the pilot, as since v0.11 |

Smaller single remarks, each in one picture: a painter's brush "possibly a small roller" (2), marks on faces (glasses,
a moustache or a hearing aid, 3), small white objects (a paw or a ball, a napkin), the kite string "very close above the
man's bucket", a kite string "very close to the edge of the big tree", a lamp's head over an upper window, a bench cut off
by the picture's edge, a stretched begging dog, a lead "in the mouth or clipped to a collar", and a waving person's gesture
"cheering, waving or reacting to the balloon".
