# v0.9 blind screen: what it found (the work list for v0.10)

The v0.9 screen used the same method as the five before it, with fresh readers and the same prompts
(`screen_prompts.md`). Six readers who never saw the key described 41 pictures (`desc_pic_NN.md`): the
21 pictures of the set (16 showcase pictures and 5 isomorphs) and 20 probe pictures built so that every
template appeared in at least two screened pictures. Two scorers with the same prompt scored pictures 1
to 20 and 21 to 41 against `keys.json` (`scores_a.json`, `scores_b.json`, merged in `scores.json`;
`scores_summary.md`). Per-template means are in `../vision/screen_summary.json` (`by_template`; probes
count there, not in the headline figures). The gate is in `gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) |
|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 |

Inferences rose from 0.83 to 0.91, the best of the six screens: all four redesigns carried their
inference in the set. The set lost 3 inference points, 1.5 of them to the dropped ice cream. Contradictions
fell from 1.00 to 0.95 on two half points: an upward watering stream read as "drip[ping] down from [the
awning] into the can", and a bucket on the head offered as "a tall blue hat". The one misread in the set
was a sleeping cat, "crouched low".

## The four templates v0.9 redesigned

| Template | v0.8 | v0.9 | What the readers saw in v0.9 |
|---|---|---|---|
| `seesaw_heavy` | 0.75 | 1.00 | "The man's weight is holding his end down, so the girl is stuck up in the air while he reads"; "the seesaw is stuck with the girl up in the air", the man "seemingly ignoring her". Passes |
| `dog_begs` | 0.78 | 1.00 | "Begging for the ice cream", "as if it wants her ice cream", "as if trying to get it", in all three pictures. Passes |
| `lost_balloon` | 0.83 | 1.00 | "It looks like she has just let go of it"; "a blue balloon has got away"; "has floated away, and its string is just out of reach", in all four set pictures. Passes |
| `about_to_trip` | 0.79 | 0.88 | The open book reads as a book, and three of four pictures read fully ("walking along reading a red book ... about to trip over it"). In the busiest garden the walker stood between the clothesline posts: her open book was "a book or papers" (or laundry to hang), and the bucket beside her drew no prediction |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 |
|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 |

Three of the four redesigns pass with full marks, and the fourth improved. But nine templates that
passed in v0.8 fall under the gate on their new pictures, so the count falls from 60 to 54. Eight of the
ten failures are within one half point of passing: with two pictures and two to six items, one reader's
hedge decides the gate. Most of the slips have a cause visible in the picture (below); the duck's two half points look
like scoring strictness on the wording of an inference.

## What reads poorly (the v0.10 list)

| # | Sev | Template | v0.9 mean | What the readers saw | Fix for v0.10 |
|---|---|---|---|---|---|
| R1 | A | `ice_cream_drop` | 0.78 (20 items, 5 pictures) | The child "holds a cone to her mouth"; nobody can tell the cone is empty, nobody says upset, and the scoop on the ground is once "a pink cake or jelly". 1.5 of the set's 3 lost inference points | A new pose: the empty cone held out and looked at, the other hand to the face, an open-mouthed upset face; the scoop drawn as a round ball with a splat and drips, directly below the cone; no dog's white head over the scoop (it "merges" with it twice) |
| R2 | B | `sweep_fork` | 0.75 (1 misread) | In a probe, sweeping on the garden's stepping-stone path read as "jabbing it into the path ... breaking a stepping stone", a digging tool. Both set readings in v0.8 were full marks | Sweep only on a continuous path or pavement, never on stepping stones; the dust heap on plain paving |
| R3 | B | `floating_box` | 0.83 (1 misread) | A box floating beside the house corner read as "sticking out of the house wall", its shadow "a faint grey patch" | Keep the floating box clear of buildings and structures by a margin, with open sky or fence behind it |
| R4 | B | `about_to_trip` | 0.88 | Between clothesline posts the open book read as laundry, and the bucket sat beside her | Keep the walker away from the clothesline and other props that compete with the book; the obstacle straight ahead in the walking direction |
| R5 | C | `cat_on_fence` | 0.75 | A cat on the fence top behind a clothesline read as walking the washing line | Keep the fence cat clear of the clothesline's span |
| R6 | C | `birds_flying` | 0.83 | A bird crossing a roof edge read as "perched ... or flying just above it" | Flying birds in open sky, clear of rooflines, awnings and clouds |
| R7 | C | `water_upward` | 0.83 | On the street, the upward stream reached the awning and read as dripping from it into the can | The upward stream ends in open air, clear of awnings and lamp posts |
| R8 | C | `slide` | 0.75 | A child at the foot of the slide: "has just come down the slide or is simply resting" | At the foot, legs still on the chute and arms up; or only the child at the top |
| R9 | C | `cat_sleeping` | 0.83 (1 misread) | A small sleeping cat in the busiest park read as "crouched low" | A curled sleeping pose with the tail round the body, a little larger |
| R10 | C | `ducks_bread` | 0.83 | "Swimming toward the food", twice given half credit for not saying the duck will eat it | Content model: the scoring of this inference, or a duck with its bill at a crumb |

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.10 |
|---|---|---|---|---|
| O1 | B | A stepping stone drawn over a lying dog | 1 picture | Draw path stones in the ground layer, under animals |
| O2 | C | The bolder sandwich now looks "unusually large" | 3 pictures | Scale it down to about 0.8 |
| O3 | C | The white dog's head "merges" with the pink ice cream it sniffs | 2 pictures | Cast the brown dog for the dropped ice cream |
| O4 | C | An ordinary seesaw with a grown-up only slightly tilted; the grown-up's end off the ground | 1 probe | With a grown-up on one end, rest the low end on the ground |
| O5 | C | The low seesaw rider's lower legs cross the board | 1 probe | Feet beside the board, as for the other low pose |
| O6 | C | A plain upward stream "like a string of beads" | 1 picture | A continuous stream |
| O7 | C | Flying birds and songbirds larger than life | 3 pictures | Scale flying birds down |
| O8 | C | A camera-holder seen from behind as "a plain dark round shape with no face" | 1 picture | Three-quarter view for the photographer |

None of the v0.8 oddities came back: no sprinkler without a hose, no painter without paint, no
ring-binder newspaper, no one-handled wheelbarrow, no rope through the swing rider, no matching balls of
different events, and no child standing on the slide platform.
