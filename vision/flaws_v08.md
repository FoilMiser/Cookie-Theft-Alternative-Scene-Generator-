# v0.8 blind screen: what it found (the work list for v0.9)

The v0.8 screen used the same method as the four before it, with fresh readers and the same prompts
(`screen_prompts.md`). Six readers who never saw the key described 39 pictures (`desc_pic_NN.md`): the
20 pictures of the set (16 showcase pictures and 4 isomorphs) and 19 probe pictures built so that every
template appeared in at least two screened pictures. Two scorers with the same prompt scored pictures 1
to 16 and 17 to 39 against `keys.json` (`scores_a.json`, `scores_b.json`, merged in `scores.json`;
`scores_summary.md`). Per-template means are in `../vision/screen_summary.json` (`by_template`; probes
count there, not in the headline figures). The gate is in `gate.json`.

## Headline (the 20 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) |
|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 |

Every contradiction in the set and in the probes was noticed and explained, the giant fork's included.
The one misread: a walking woman's small red book read as a phone. Inferences are the one row that did
not rise; all of their lost points are in the four templates that fail the gate (below).

## The nine templates v0.8 redrew

| Template | v0.7 | v0.8 | What the readers saw in v0.8 |
|---|---|---|---|
| `sweep_fork` | 0.17 | 1.00 | Both set pictures: "sweeping a small pile of litter and dust using a giant silver fork instead of a broom, which looks absurd"; "a huge silver dinner fork held like a broom". One reader added that it "could also be read as a pitchfork or garden fork, but either way it is the wrong tool". Passes |
| `cat_stalks_bird` | 0.58 | 0.96 | Three of four pictures: "crouched low and stretched out, creeping", "creeps low", "clearly stalking". In the busiest playground the cat was once "running toward" the bird (inventory: "running or stalking"); the pounce was still read. Passes |
| `dog_wants_walk` | 0.63 | 1.00 | The brown dog at the door "with its red leash in its mouth ... as if asking to go for a walk". Passes |
| `bird_steals` | 0.67 | 1.00 | "Pecking at it ... does not seem to notice, so the bird looks about to steal or eat his sandwich"; no cap, no books. Passes |
| `sandbox` | 0.50 | 1.00 | "Kneels and builds a sandcastle", twice. Passes |
| `goat_grazing` | 0.50 | 1.00 | "Nibbles grass", "eating a tuft of grass". Passes |
| `wave` | 0.75 | 1.00 | "Waves with one raised hand (motion lines)", three times; twice the reader could not tell whom she waves at (an oddity, not a lost point). Passes |
| `rain_coming` | 0.88 | 1.00 | "Points up at the dark clouds", "warning everyone about the coming rain": the pointing line no longer meets anything else. Passes |
| `lost_balloon` | 0.88 | 0.83 | The balloon is now near the child in all three pictures, but the letting go is hedged every time: "could belong to the boy, who has just let go of it, or it could simply be floating past"; once "the child holding the balloon, or ... having just let go" |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 |
|---|---|---|---|
| Pass | 35 | 55 | 60 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 |
| Fail | 6 | 9 | 4 |

Eight of the nine v0.7 failures pass. Three templates that passed in v0.7 fail on their new pictures,
each for a reason the pictures show.

## What reads poorly (the v0.9 list)

| # | Sev | Template | v0.8 mean | What the readers saw | Fix for v0.9 |
|---|---|---|---|---|---|
| R1 | B | `seesaw_heavy` | 0.75 | Positions read ("sits on the low end", "feet dangling") but not the stuck child: "the bigger boy is down and the smaller girl is up, so this doesn't look wrong"; once no weight reason at all. The heavy man was once "a boy" | v0.8 made ordinary seesaws tip toward the heavier rider, so a tipped seesaw is no longer the cue. Make the stuck child the cue: hands gripping, legs kicking, worried face, the plank end hard on the ground; cast a clearly grown, heavier man (beard), never the youngest adult |
| R2 | B | `dog_begs` | 0.78 | A grandmother's apple read as "a cherry, small apple or sweet ... or a red clown nose", and with it the begging (0); once the white dog's sitting-up pose read as "rearing up ... or jumping up" | Give the eater a food that reads at any size (ice cream, sandwich); drop the apple. Use the plain sit, head up, for the begging dog |
| R3 | B | `about_to_trip` | 0.79 (1 misread) | In the busiest garden the small red book read as a phone; in the busiest playground the box lay beside the walker and was "not linked to [his] path" | A larger open book with pages showing; the obstacle placed one or two strides straight ahead on the walker's ground line, with nothing else between |
| R4 | C | `lost_balloon` | 0.83 | "Let go, or just floating past" every time | A cue that the balloon was the child's: the child holding a bunch with one rising from it, or the string trailing from just above the open fingers with an upset face |

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.9 |
|---|---|---|---|---|
| O1 | C | A sprinkler spraying with no hose or pipe | 2 probes | Run a hose from the reel to the sprinkler |
| O2 | C | A fence being painted with no paint tin | 2 probes | A tin at the painter's feet |
| O3 | C | The dog's newspaper drawn with ring-binder holes | 2 pictures | Redraw it as a folded newspaper |
| O4 | C | A wheelbarrow with one handle showing | 3 pictures | Draw both handles |
| O5 | C | Teenagers read as grown-ups or children (4 times) | several | Content model: age cues for the teen figures (or accept it; no scored item was lost) |
| O6 | C | A swing chain passing through the rider; feet off the seat's end | 1 probe | Seat the swing rider between the chains |
| O7 | C | Seesaw riders' shadows offset from their feet | 2 probes | Shadow under the feet of seated riders |
| O8 | C | Two identical red balls in one picture (a ball in the air for catch, another on the grass to trip over) | 1 picture | Different colours for balls of different events |
| O9 | C | Standing on top of the slide "looks unsafe" | 2 probes | Content model: a child sitting at the top instead |

None of the v0.7 oddities came back: no seesaw tipped the wrong way and no empty seesaw in the air, no
legs through the plank, no bucket and spade on the grass, no white paws leaving blue prints, no hi-vis
worker at leisure events, no long hose-like stream from a pan, no flying cap over a lamp post, and no
green lump on the tree crown.
