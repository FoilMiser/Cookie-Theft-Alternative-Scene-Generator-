# v0.11 blind screen: what it found (the work list for v0.12)

The v0.11 screen used the same method and prompts as the seven before it (`screen_prompts.md`). Nine
readers who never saw the key described 61 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16
showcase pictures and 5 isomorphs) and 40 probe pictures, which put every template in at least three
screened pictures. Three scorers with the same prompt scored pictures 1 to 17, 18 to 38 and 39 to 61
against `keys.json` (`scores_a.json`, `scores_b.json`, `scores_c.json`, merged in `scores.json`;
`scores_summary_a.md` to `_c.md`). Per-template means are in `../vision/screen_summary.json`
(`by_template`; probes count there, not in the headline figures). The gate is in `gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) |
|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 |

The best of the eight screens on inferences, all items and oddities, and equal best on things, actions
and contradictions. Across all 61 pictures only 11 of 705 scored items fell short of full marks (12 of
683 in v0.10). Four of the 11, the one misread among them, are in a single picture, the busiest isomorph
(`T4_park_s17111_iso`, 23 items).

## The five templates v0.10 failed

| Template | v0.10 | v0.11 | What the readers saw in v0.11 |
|---|---|---|---|
| `wave` | 0.67 (3 items, 1 misread) | 1.00 (3 items, 3 pictures) | Clear of the house walls: "waving" every time |
| `ball_in_tree` | 0.89 (1 misread) | 1.00 (9, 3) | Never with the wind, the reaching child under the ball |
| `kite_in_tree` | 0.89 | 1.00 (9, 3) | Twig and leaves over the kite: stuck in the tree every time |
| `rain_coming` | 0.83 | 1.00 (9, 3) | Worried, clear of trees, kites and structures: "about to rain" every time |
| `dog_playing` | 0.83 | 0.83 (3, 3) | Two pictures read the play bow; the busiest park again offered "stretch or play-bow" |

Four of the five reach full marks. The play bow fails again by the same half point, both times in the
busiest park picture, both times as "a stretch or play-bow".

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 |
|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 |

59 of 64 pass. Every template was screened in at least three pictures (53 in three, 11 in four to six).
Each of the five that fail lost points in one picture only, and four of them passed in v0.10: one half
point or two on a single picture (four templates), or a single misread (one). The retest of v0.9
(`retest_v09.md`) put reader variance at about five templates, which is the size of this list; two of
the five come from the one busiest picture.

## What reads poorly (the v0.12 list)

| # | Sev | Template | v0.11 mean | What the readers saw | Fix for v0.12 |
|---|---|---|---|---|---|
| R1 | B | `kick_ball` | 0.75 (4 items, 1 misread) | In the busiest isomorph (a set picture) a small girl kicking far back by the tree: her outstretched leg and yellow shoe read as "a wooden bat with a yellow end", the ball "hovering at her hip height". The other three pictures read "kicking a ball" | The kicker no smaller than the people nearer the front, and the ball on the ground just ahead of the foot or on the ground-shadow line, never level with the hip |
| R2 | C | `dig` | 0.83 | The same picture: the digger at the front edge, head bowed, eyes closed, a hand at the chest: "leans on the spade ... as if tired or unwell" | A digging pose with a foot on the spade and the eyes open, looking at the hole |
| R3 | C | `dog_playing` | 0.83 | In the busiest park, front and centre: "in a stretch or play-bow pose" | Something to play with: a ball or stick on the ground in front of the bowing dog, the person it faces looking back at it |
| R4 | C | `floating_box` | 0.89 | In a probe the tilted box hung low against the fence: "tipped over and resting at the foot of the fence" or "floating or falling" | The box's lower edge well above the fence base, so it cannot be standing against it; a ground shadow directly under it |
| R5 | C | `square_wheel` | 0.89 | In a probe the square wheel read two ways: "the wheelbarrow's wheel but drawn square" or "a separate box ... the real wheel hidden behind it" | The wheel's hub on the axle line of the tray's front bracket, the bracket drawn over the wheel, so it cannot be a box in front |

`about_to_trip` scored 0 once (the reading woman's box in the same busiest isomorph, nobody predicting
a fall) and still passes on its other four pictures.

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.12 |
|---|---|---|---|---|
| O1 | C | A swing drawn with motion arcs but the ropes "hang straight down", the child's arms "wider than the swing chains" | 2 probes | The swinging pose tilted a little with the ropes (the arcs alone read in the design tests and in the set) |
| O2 | C | A goat "odd for a small back garden", "loose in a public park" | 4 pictures | None needed for legibility (it is an event, not a contradiction); note for the pilot |
| O3 | C | The slide's ladder "looks a little detached from the frame", "doubled" | 2 probes | Redraw the ladder rails meeting the platform |
| O4 | C | The bicycle in its rack "looks squashed: oversized wheels almost touching" | 2 street pictures | Wider wheelbase in the rack filler |
| O5 | C | Large birds "about knee height", "the size of his lower leg" for birds pecking seeds | 2 pictures | Pecking birds at the flying birds' smaller size |
| O6 | C | A person or the seesaw plank overlapping the pond's edge or a man's legs | 3 pictures | Depth checks against the pond edge for standing people |
| O7 | C | A play-bowing dog "by the house corner ... its back end is cut off by the house wall" (still read as a play bow) | 1 set picture | The house-edge rule (revision 9) for animals as well as people |

None of the v0.10 oddities came back: no bigger child up on an ordinary seesaw, no basket over the
sitter's shins, no goat-or-fox reading dog, no dustpan lying away from the heap, no child above the
chute, no hat flying against the wind.
