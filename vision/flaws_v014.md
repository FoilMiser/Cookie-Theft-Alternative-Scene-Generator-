# v0.14 blind screen: what it found (the work list for v0.15)

The v0.14 screen used the same method and prompts as the ten before it (`screen_prompts.md`). Nine readers
who never saw the key described 59 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16 showcase
pictures and 5 isomorphs) and 38 probe pictures. Three scorers with the same prompt scored pictures 1 to 18,
19 to 39 and 40 to 59 against `keys.json` (`scores_a.json` to `scores_c.json`). A tier-3 garden picture
had to be rebuilt before the screen (its first layout put a kite string between the stalking cat and its
bird, and the rule added for that changed it), which left the stalking cat and the reading dog in only two
screened pictures; one more probe (picture 60) was built for them and read by a tenth reader and scored by a
fourth scorer with the same prompts (`scores_d.json`). The four were merged in `scores.json`. Per-template
means are in `../vision/screen_summary.json` (`by_template`; probes count there, not in the headline
figures). The gate is in `gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) | v0.13 (21) | v0.14 (21) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.995 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 |

The best of the eleven screens on actions and all items (0.995, against 0.991 in v0.12), equal best on things
and contradictions, and no item in the set misread for the fourth time in five screens. Across all 60
pictures only 4 of 703 scored items fell short of full marks: three half points on inferences in the set (two
walkers heading for a bucket "that he may bump into ... or he may just pass it", and a bird pecking at a
sandwich never said to be stealing it) and one misread in a probe (below). Oddities fell from 44 to 28 in the
set, 1.3 per picture.

## The templates v0.13 failed

| Template | v0.13 | v0.14 | What the readers saw in v0.14 |
|---|---|---|---|
| `cat_stalks_bird` | 0.89 (9 items, 3 pictures) | 1.00 (9 items, 3 pictures) | "Crouches low ... 'ready to pounce', 'stalking it'"; "crouched low, creeping up behind the bird ... as if about to pounce"; "the cat looks like it is stalking the bird and about to pounce, and the bird does not seem to have noticed" |
| `seesaw_heavy` | 0.89 (9, 3) | 1.00 (9, 3) | "Girl on the high end, 'stuck up in the air' ... 'reading ... instead of playing, so the girl is stuck'"; "'His weight is keeping the girl up ... he doesn't seem to notice her, so she's stuck'"; "'stuck up high' ... 'apparently not paying attention to her'" |
| `wave` | 0.83 (3, 3) | 0.67 (3, 3) | Two adults "waving a raised hand", "waves her hand"; a third adult, waving toward a woman whose hose had stopped, read as "scratching his head ... looking puzzled" (below). No child waved in the screened pictures |

The visuals refined for the v0.13 oddities kept full marks: the ball in the tree "stuck on a branch", "stuck in
the branches" in all five of its pictures; the square-wheeled bicycle and barrow caught in all three; the
windy hat in all three ("It is windy ... just had his orange cap blown off"); the dropped ice cream in all
six; the sleeping cats and dogs "curled up asleep" in all six.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 |
|---|---|---|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 | 61 | 63 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 | 3 | 1 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 | 395 | 396 |

63 of 64 pass, every template screened in at least three pictures (54 in three, 6 in four, 2 in five, 2 in
six). All three v0.13 failures that were redrawn or given room pass with full marks except the wave, which
fails on one misread.

## What reads poorly (the v0.15 list)

| # | Sev | Template | v0.14 mean | What the readers saw | Fix for v0.15 |
|---|---|---|---|---|---|
| R1 | B | `wave` | 0.67 (3 items) | In a probe, an older man waving toward a woman whose hose had stopped (a goat on it): "scratching his head ... looking puzzled", "it is also possible he is waving, but the motion lines and hand on head suggest scratching". His hand was above his head; the event he faced made it a reaction | Wave only toward someone free of any inference event, and clear of mishaps; a probe with a waving child, so the v0.14 child's wave is screened |

Three inferences lost a half point once each and still pass: two walkers reading on their way to a bucket set
a little to one side of their path ("he may walk into it, or he may just pass it") (`about_to_trip`, 0.93), and
a bird at a sandwich never said to be stealing it (`bird_steals`, 0.94). The bucket could be set squarely on the
walker's line.

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.15 |
|---|---|---|---|---|
| O1 | C | Wind that leaves hair still: "the painter's cap and the woman's hair are unaffected by the wind"; "hair, ponytail, flowers and tree are still"; and a new one, "the kite flies high (needs wind) but the washing hangs straight down" | 3 probes | Washing on the line swung a little in any picture with a kite flying; hair is the 3D cast's (a blown fringe or ponytail would be a new rig) |
| O2 | C | A low bush at the foot of the garden fence "looks cut off ... its top half hidden by the fence though it is on the lawn side" | 3 probes | Draw that bush in front of the fence, or off the fence line |
| O3 | C | The bird table's pole "disappears behind the fence; unclear which garden it is in" | 4 probes | The bird table stands on the lawn, its pole to the ground in front of the fence |
| O4 | C | A hose across a path "could trip" someone | 2 set pictures | Hoses run on the grass, off paths |
| O5 | C | Eyes that look closed on people working ("sweeping boy's eyes look closed or squinting") | 2 set pictures, 1 probe | Open eyes for every chore pose |
| O6 | C | A balloon floating away "the same colour as the boy's balloon; could belong to someone other than the girl" | 1 set picture | The lost balloon never shares a colour with another child's balloon |
| O7 | C | A bird in a tree's crown "with no visible branch under it" | 1 set picture | A short branch under a bird perched in a crown |
| O8 | C | A sleeping cat "out in the middle of a busy pavement"; a picnic under a storm sky; a swing set's legs on the path | 1 set picture each, 1 probe | Sleepers off the busiest ground; no picnic under storm clouds; the garden swing off the path |
| O9 | C | A goat "in a home back garden", "in a public park" | 2 set pictures, 4 probes | None needed for legibility (an event, not a contradiction); note for the pilot, as since v0.11 |

None of the v0.13 oddities came back as reported then: nobody seemed to stand on an empty seesaw, no bicycle
stood "by itself", no ball was "drawn on top of the tree", no kite string met the tail, no black cat slept
unreadably, no dropped scoop was outsized and no lead ran round a dog's middle. The wind now reaches the washing
and the sky; the readers still noticed hair.
