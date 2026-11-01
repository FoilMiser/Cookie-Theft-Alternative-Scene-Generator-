# v0.13 blind screen: what it found (the work list for v0.14)

The v0.13 screen used the same method and prompts as the nine before it (`screen_prompts.md`). Nine
readers who never saw the key described 61 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16
showcase pictures and 5 isomorphs) and 40 probe pictures, which put every template in at least three
screened pictures. Three scorers with the same prompt scored pictures 1 to 19, 20 to 39 and 40 to 61
against `keys.json` (`scores_a.json`, `scores_b.json`, `scores_c.json`, merged in `scores.json`;
`scores_summary_a.md` to `_c.md`). Per-template means are in `../vision/screen_summary.json`
(`by_template`; probes count there, not in the headline figures). The gate is in `gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) | v0.13 (21) |
|---|---|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 |

No item misread, for the third time in four screens; all items 0.988 (0.991 in v0.12). Across all 61
pictures 8 of 717 scored items fell short of full marks (8 of 694 in v0.12), every one a half point: a
reading offered as one of two, or the visible facts given without the meaning. Seven of the eight fall in
the set, where inferences dropped from 0.96 to 0.94: four of the set's 35 inference items lost a half
point, one each. The oddity count rose from 32 to 44; most are mild ("odd but possible"), several are
hedges the readers raised and then dismissed, and one scorer filed ages and drawing remarks that earlier
scorers mostly left out. The real ones are listed below.

## The template v0.12 failed, and the half points

| Template | v0.12 | v0.13 | What the readers saw in v0.13 |
|---|---|---|---|
| `blocked_hose` | 0.88 (12 items, 3 pictures) | 1.00 (12 items, 3 pictures) | "A white dog ... is standing right on the hose, and the hose is visibly swollen on the reel side of the dog, so the water is blocked"; "a white goat ... is standing on the hose, and the hose bulges just behind the goat, so the goat seems to be blocking the water" |
| `ducks_bread` | 0.94 | 1.00 (9, 3) | "Swimming quickly towards the food"; "the duck is swimming toward the food" |
| `play_catch` | 0.92 | 1.00 (6, 3) | No arc toward a cat; the ball read as thrown to the catcher |
| `cat_stalks_bird` | 0.90 (15, 5) | 0.89 (9, 3) | "Crouched low, creeping toward a red bird"; "creeping toward the blue bird"; but in the busiest street "an orange cat runs toward a red bird", "may be chasing the red bird or just running past the girl" |

The sleeping cats and dogs read as asleep first in seven of their eight pictures ("curled up asleep", "lying
curled up, apparently asleep"; one reader added that a cat "could be lying hurt"); in the eighth the small
black cat was "lying down on the pavement (resting or rolling)", which the key accepts. None read as collapsed; the kite in the tree as "caught in the leaves of a
big tree" in all three; the floating box and the square wheel kept full marks.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 |
|---|---|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 | 61 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 | 3 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 | 395 |

61 of 64 pass, every template screened in at least three pictures (49 in three, 13 in four, 2 in six).
`blocked_hose`, the one v0.12 failure, passes with full marks. The three that fail each lost one or two
half points in a single picture; the v0.9 retest put reader variance at about five templates of the gate's
movement between releases.

## What reads poorly (the v0.14 list)

| # | Sev | Template | v0.13 mean | What the readers saw | Fix for v0.14 |
|---|---|---|---|---|---|
| R1 | C | `cat_stalks_bird` | 0.89 (9 items) | In the busiest street picture, the paw-lifted cat beside a passing girl: "running/pouncing to the right toward the red bird", "may be chasing the red bird or just running past the girl" (in the other two "crouched low, creeping") | Room around the stalking cat and its bird, as the floating box has: nobody walking past them; to the bench with the cat among other people |
| R2 | C | `seesaw_heavy` | 0.89 (9 items) | In one set picture the girl "sits on the raised end ... holding the handle" and the reader, who saw "the heavier adult is on the low end", concluded "nothing looks wrong there" (in the other two "annoyed at being stuck" and "he is ignoring her and reading, so she is stuck up in the air") | The stuck girl's face and pose made plainer: an upset face and both hands gripping, the legs dangling; to the bench |
| R3 | C | `wave` | 0.83 (3 items) | A small boy whose raised hand is by his head, with motion lines beside it: "either waving or listening to something" | The waving hand raised clear above the head, away from the ear, for children as for adults |

Three inferences lost a half point once each and still pass: a balloon "floating away" without saying the
child let go (`lost_balloon`), a reader walking toward a bucket with the trip not predicted
(`about_to_trip`), and water rising from a watering can offered as one of two readings (`water_up`).

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.14 |
|---|---|---|---|---|
| O1 | C | A girl "overlaps the raised end of the seesaw; at a glance could look like she is standing on it"; "man might be sitting in front of the seesaw's low end" | 1 set picture, 1 probe | People keep clear of the seesaw's plank ends when nobody rides it too (v0.13 cleared them only round a ridden seesaw) |
| O2 | C | The square-wheeled bicycle "stands upright by itself with no stand or rack", twice | 2 set pictures | The heavier stand did not register: draw the stand thicker and splayed, or lean the bike on the bench, a wall or a rack |
| O3 | C | Wind that moves only the hat: "nobody else's hair or clothes is blowing"; "the washing on the line, the trees and the flowers are perfectly still" | 1 set picture, 1 probe | Where hair or a skirt is near the gust, draw it blown; washing on a line leaning with the gust (v0.13 kept balloons and washing being hung out of windy pictures, not washing already on the line) |
| O4 | C | The ball stuck in the tree "could be read as drawn on top of the tree rather than stuck in it", "a balloon or round ornament" | 2 set pictures | The leaf clusters the stuck kite now has, over the ball's edge too |
| O5 | C | The kite's string "seems to run to the bottom of the kite's tail rather than to the kite itself" | 1 probe (and on the bench) | The string from the bridle at the spars' crossing, the tail from the bottom point, kept apart near the kite |
| O6 | C | A small black sleeping cat "hard to make out: cat/kitten or small black dog" | 1 set picture | When the orange cat is busy elsewhere, a sleeping cat stays out of the picture rather than falling back to the black one |
| O7 | C | A dropped ice-cream scoop "about as big as the dog's head" | 1 set picture | The splat drawn smaller |
| O8 | C | A dog's lead "attaches around its middle/back rather than the collar" | 1 set picture | The lead ends at the collar anchor |
| O9 | C | A goat "in a back garden is unusual", five times | 1 set picture, 4 probes | None needed for legibility (an event, not a contradiction); note for the pilot, as in v0.11 and v0.12 |

None of the v0.12 oddities came back as reported then: no shadow with nothing above it, no kicked ball
heading for a child, no throw toward a cat, no leaves "pasted on top", no collapsed sleeping pet, no long
pram handle, no child on the sandbox rim. A reader listed one sleeping cat among the "wrong or impossible" things ("could be lying hurt") and another
said a cat "could be sleeping or rolling on its back"; both still read it as asleep first.
