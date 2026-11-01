# v0.12 blind screen: what it found (the work list for v0.13)

The v0.12 screen used the same method and prompts as the eight before it (`screen_prompts.md`). Nine
readers who never saw the key described 60 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16
showcase pictures and 5 isomorphs) and 39 probe pictures, which put every template in at least three
screened pictures. Three scorers with the same prompt scored pictures 1 to 18, 19 to 38 and 39 to 60
against `keys.json` (`scores_a.json`, `scores_b.json`, `scores_c.json`, merged in `scores.json`;
`scores_summary_a.md` to `_c.md`). Per-template means are in `../vision/screen_summary.json`
(`by_template`; probes count there, not in the headline figures). The gate is in `gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) |
|---|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 |

The best of the nine screens on actions, inferences and all items (0.991), equal best on things and
contradictions, and no item misread. Across all 60 pictures only 8 of 694 scored items fell short of full
marks (11 of 705 in v0.11), every one of them a half point: a reading offered as one of two, or a visible
motion given without its purpose. The oddity count rose from 22 to 32 in the set; three of the 32 are
near-misses the readers raised and then dismissed themselves ("judged not floating"), which earlier
scorers mostly left out, and most of the rest are mild ("slightly odd but plausible"). The real ones are
listed below.

## The five templates v0.11 failed

| Template | v0.11 | v0.12 | What the readers saw in v0.12 |
|---|---|---|---|
| `kick_ball` | 0.75 (4 items, 1 misread) | 1.00 (3 items, 3 pictures) | "Arms out to the sides, one leg swung out kicking"; "swinging one leg to kick an orange ball"; "mid-kick, one leg swung out towards the ball" |
| `dig` | 0.83 | 1.00 (3, 3) | "Digging with a shovel, looking down at the hole"; "digging a hole with a shovel ... looking down"; "bent forward pushing a shovel into a hole in the lawn" |
| `dog_playing` | 0.83 | 1.00 (3, 3) | "In a play bow with a yellow-green tennis ball by its nose and motion lines by its tail (wagging)", three times |
| `floating_box` | 0.89 | 1.00 (9, 3) | "In the sky above the fence, tilted at an angle; in mid-air", three times |
| `square_wheel` | 0.89 | 1.00 (9, 3) | "Its wheel is drawn as a square with spokes"; "square black wheels" |

All five reach full marks, in every picture. None of the readings the isolation bench chased came back:
no bat, no resting digger, no stretch, no box resting on the fence, no crate in front of the wheel.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 |
|---|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 |

63 of 64 pass, the most of any screen. Every template was screened in at least three pictures (59 in
three, 5 in four to six). The one that fails, `blocked_hose`, passed in v0.10 and v0.11 and loses three
half points here, two of them in one probe picture.

## What reads poorly (the v0.13 list)

| # | Sev | Template | v0.12 mean | What the readers saw | Fix for v0.13 |
|---|---|---|---|---|---|
| R1 | C | `blocked_hose` | 0.88 (12 items) | A goat "appears to be standing on or right next to the hose", the water stopped as "one reading", "another: the water simply hasn't been turned on yet"; a dog on the hose read as blocking the water, or the woman "just adjusting the nozzle" | The hose pinched under the hoof or paw: a flattened kink drawn over the foot, the hose swelling behind it, and a last drip at the nozzle; take it to the isolation bench first |

Three more inferences lost a half point once each and still pass: the stalking cat (twice "creeping ... or
just running past"), the duck "swimming toward the crumbs" without wanting them, and a catch whose ball
flew toward the cat on the fence (below).

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.13 |
|---|---|---|---|---|
| O1 | C | The floating box's shadow on the lawn "with nothing above it to cast it", "not directly under the floating box" | 1 set picture, 2 probes | Now that the box hangs high above the fence, a fainter, smaller shadow straight below it, or none |
| O2 | C | A kicked ball "may be heading for the child" building a sandcastle; in a probe "flying toward the tree or the girl" | 1 set picture, 1 probe | The kept-clear zone ahead of the ball runs further, to the frame or to open ground, clear of people |
| O3 | C | A throw whose ball "arcs toward the fence top and the cat", the catcher "facing away from it" | 1 set picture | The ball's arc kept clear of every other figure, the cat on the fence included |
| O4 | C | Sleeping cats and dogs lying flat "could also be read as collapsed", "unwell" | 3 pictures | A curled, tucked sleeping pose with the tail wrapped round (no "z" symbols, which stay out) |
| O5 | C | Leaf clumps over the stuck kite "look pasted on top" | 3 pictures | Smaller leaf clumps in the canopy's own green, drawn behind the kite's frame where it enters the leaves |
| O6 | C | Wind that moves only the hat: "balloons, tree and awnings are unaffected by the gust" | 1 set picture, 2 probes | A few leaves blown off the nearest tree and laundry or balloons leaning with the gust where they share the picture |
| O7 | C | A square-wheeled bicycle "stands upright on its own with no rider and no stand visible" | 1 set picture | The stand drawn heavier on the square-wheeled bike (the parked one in its rack read as "using its kickstand") |
| O8 | C | A girl "so close to the raised seesaw end she could look as if standing on the plank"; a seesaw board "behind or through the man's thighs" | 2 pictures | People keep clear of the seesaw's plank ends; the seated rider's thighs drawn over the plank |
| O9 | C | The pram "hard to tell which end is being pushed", its handle "very long and steeply angled" | 2 pictures | A shorter handle and the hood at the pusher's end |
| O10 | C | A goat "loose in an ordinary town park", "unusual in a back garden" | 4 pictures | None needed for legibility (an event, not a contradiction); note for the pilot, as in v0.11 |

None of the v0.11 oddities came back as reported then: no swing hanging straight, no detached ladder, no
squashed bicycle, no outsized pecking birds, no dog cut off by the house wall. One came back as a near-miss
in a probe: a man in red "overlaps the edge of the pond; at a glance his upper body looks over the water".
