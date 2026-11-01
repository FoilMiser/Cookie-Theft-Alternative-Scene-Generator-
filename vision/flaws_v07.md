# v0.7 blind screen: what it found (the work list for v0.8)

The v0.7 screen used the same method as the three before it, with fresh readers and one added
sentence in the reader prompt (look at each picture whole; no cropping or enlarging). Six readers who
never saw the key described 41 pictures (`desc_pic_NN.md`): the 21 pictures of the set and 20 probe
pictures built so that every template appeared in at least two screened pictures. Two scorers with
the same prompt scored the two halves against `keys.json` (`scores_a.json`, `scores_b.json`, merged in
`scores.json`; `scores_summary.md`). Per-template means are in `../vision/screen_summary.json`
(`by_template`; probes count there, not in the headline figures). The gate is in `gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) |
|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 |

Every contradiction item the set lost belongs to one template: the giant fork, read twice as a rake
(four of 22 items). Without it the set's contradictions were all caught and explained, and all 11
contradictions in the probes were too.

## The six templates v0.7 redrew

| Template | v0.6 | v0.7 | What the readers saw in v0.7 |
|---|---|---|---|
| `seesaw_heavy` | 0.67 | 0.92 | Both times the girl sits high holding the handle ("raised up in the air with her feet dangling") and the man on the low end; once the tilt was put down to him "pushing it down" rather than his weight (0.5 on the inference). Passes |
| `feed_birds` | 0.75 | 1.00 | Both times "sprinkling seeds" down to the birds; the head-down pose ended the leaking-bag reading. Passes |
| `jump` | 0.88 | 1.00 | "Jumping in mid-air ... with a happy face", "jumping in the air with her arms up"; the shadow told one reader the jumper was "clearly airborne rather than floating". Passes |
| `lost_balloon` | 0.83 | 0.88 | The balloon is always seen floating away and the child always reaching up, but twice the reaching was hedged ("or cheering", "just excited"), and three readers noted the balloon is far from the child |
| `bird_steals` | 0.67 | 0.67 | Read as theft once ("as if about to steal it"); once the blue bird, drawn against a kite-flyer's shoulder, was "a blue cap-shaped object", and the sandwich could have been "a stack of books" |
| `sweep_fork` | 0.25 | 0.17 | Twice raking leaves, once "with a long fan rake" (or "a litter picker"): the swept pile and the low diagonal stroke read as raking, and a dining fork at this size is a rake head |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 |
|---|---|---|
| Pass | 35 | 55 |
| Read well, but in fewer than two pictures | 18 | 0 |
| Fail | 6 | 9 |

All 18 templates that v0.6 had seen only once were screened at least twice; 16 pass. The probes did
their job: every template was judged.

## What reads poorly (the v0.8 list)

| # | Sev | Template | v0.7 mean | What the readers saw | Fix for v0.8 |
|---|---|---|---|---|---|
| R1 | A | `sweep_fork` | 0.17 (2 misreads) | A rake, "a long fan rake", "a litter picker": the tool is never seen as wrong | Three redraws have not made a fork legible at sweeping size. Retire it, or replace it with a sweeping contradiction whose object cannot pass for a garden tool (a giant spoon reads as a shovel; something soft or tiny would be better). Decide before drawing |
| R2 | B | `cat_stalks_bird` | 0.58 (1 misread) | The crouch read as running twice; once the cat seemed to flee a dog walking past | A lower, flatter crouch (belly on the ground, tail low and straight); the cat nearer the bird and facing it; no dog within reach of the cat |
| R3 | B | `dog_wants_walk` | 0.63 (1 misread) | The small white dog at the door read as a white cat with a leash in its mouth | Cast the larger brown dog for this event, or give the small dog a longer muzzle and floppy ears |
| R4 | B | `bird_steals` | 0.67 (1 misread) | The bird against a person's shoulder became a cap; the sandwich could be books | Keep songbirds clear of people's heads and shoulders (the clearance rule animals already have for structures); draw the sandwich with a visible bite and filling at the bird's end |
| R5 | B | `sandbox` | 0.50 | The child sits beside the castle, "resting" | A building pose: spade in hand, patting the castle |
| R6 | B | `goat_grazing` | 0.50 | "Grazing or about to butt", "eating grass or sniffing the ground" | Muzzle in the grass with a tuft in the mouth; consider whether a loose goat belongs in a park or garden at all (three readers flagged it) |
| R7 | C | `wave` | 0.75 | One raised arm offered as waving among other readings | Hand open at head height, palm out, toward another person in the picture |
| R8 | C | `lost_balloon` | 0.88 | Reaching "or cheering"; the balloon far from the child | Balloon just out of reach above the child, string end just above the hands; the head tilted up at it (the gaze check exists but is not required) |
| R9 | C | `rain_coming` | 0.88 | A pointer read as pointing at a ball in a tree or a cat on the fence; once the storm clouds without a pointer were not read as rain coming | Require the pointing line to clear other salient things (a ball, a kite, an animal on the fence) |

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.8 |
|---|---|---|---|---|
| O1 | B | An ordinary seesaw tipped the wrong way for its riders: the bigger girl up, the smaller one down | 1 picture | A plain seesaw sits level, or the heavier rider sits on the low end; an empty seesaw rests with one end down |
| O2 | B | A seesaw rider's lower legs pass through the plank | 1 picture | Redraw the low seated pose with the feet beside the plank |
| O3 | C | Bucket and spade left on the grass outside the sandbox | 3 pictures | Put them in the sandbox |
| O4 | C | The dog leaves blue paw prints but its paws are white | 2 pictures | Tint the paws |
| O5 | C | A hi-vis road worker at a picnic or pushing a pram | 2 pictures | Keep the worker's outfit to work events |
| O6 | C | A fruit stall with nobody minding it | 3 pictures | Content model: left as it is, or a stallholder filler |
| O7 | C | A frying pan pouring a long hose-like stream | 2 pictures | A shorter splash from the pan |
| O8 | C | A wind-blown cap overlapping the top of a lamp post | 1 picture | Keep the flying hat clear of poles |

None of the v0.6 oddities came back: no green blob on a tree, no free-standing bicycle, no stream on
the front of a flower box, no empty blanket or café cup, no two identical balls, no photographer
without a subject.
