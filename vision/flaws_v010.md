# v0.10 blind screen: what it found (the work list for v0.11)

The v0.10 screen used the same method and prompts as the six before it (`screen_prompts.md`), with one
change prompted by the test-retest (`retest_v09.md`): the probes now put every template in at least three
screened pictures instead of two. Nine readers who never saw the key described 57 pictures
(`desc_pic_NN.md`): the 21 pictures of the set (16 showcase pictures and 5 isomorphs) and 36 probe
pictures. Three scorers with the same prompt scored pictures 1 to 16, 17 to 38 and 39 to 57 against
`keys.json` (`scores_a.json`, `scores_b.json`, `scores_c.json`, merged in `scores.json`;
`scores_summary_a.md` to `_c.md`). Per-template means are in `../vision/screen_summary.json`
(`by_template`; probes count there, not in the headline figures). The gate is in `gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) |
|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 |

The best or equal best of the seven screens on every row. Across all 57 pictures only 12 of 683 scored items fell short
of full marks, and two were misread, both in probes. In the set, the inference points lost were all half
points: two kites "flying there or caught", two storm pictures where nobody said it was about to rain, and
the blocked hose in the busiest garden.

## The ten templates v0.9 failed

| Template | v0.9 | Retest (same v0.9 pictures) | v0.10 | What the readers saw in v0.10 |
|---|---|---|---|---|
| `ice_cream_drop` | 0.78 | 0.80 | 1.00 (20 items, 5 pictures) | Redesigned: the empty cone held out to the side, a hand rubbing an eye, the scoop right under the cone. In every picture the child is crying and holding an empty cone, "because her pink ice cream has fallen", and the dog is "sniffing or licking it" |
| `sweep_fork` | 0.75 | 0.83 | 1.00 (9, 3) | On the paved path, the heap on the paving with a dustpan beyond it: "sweeping with a giant silver dinner fork ... instead of a broom or rake" |
| `about_to_trip` | 0.88 | 0.88 | 1.00 (15, 5) | Walker and obstacle clear of the clothesline: "she looks about to trip over it" |
| `cat_on_fence` | 0.75 | 0.75 | 1.00 (3, 3) | Clear of the clothesline, the bird table and the swing frame: "walking along the top of the fence" |
| `birds_flying` | 0.83 | 0.83 | 1.00 (4, 4) | Smaller, in open sky clear of rooflines, trees, clouds and kites: "flying in the sky" every time |
| `floating_box` | 0.83 | 0.92 | 1.00 (9, 3) | Clear of the house, every standing structure and kite strings: "hangs in mid-air ... nothing holding it up" (twice also offered as falling or blown by wind) |
| `water_upward` | 0.83 | 0.92 | 1.00 (9, 3) | One unbroken stream rising straight out of the spout, ending in open air: "physically impossible for a watering can" |
| `slide` | 0.75 | 1.00 | 1.00 (3, 3) | Half way down the chute: "sliding down it with both arms raised" |
| `cat_sleeping` | 0.83 | 1.00 | 1.00 (4, 4) | Curled up, nearer the front: "lying with eyes closed ... seems to be asleep" |
| `ducks_bread` | 0.83 | 1.00 | 1.00 (9, 3) | Crumbs floating just ahead of the duck: swimming "toward the crumbs", "likely bread for the duck" (scored full marks; one called borderline) |

All ten pass with full marks, each in at least three pictures.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 |
|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 |

59 of 64 pass. Every template was screened in at least three pictures (54 in three, 10 in four to six). The
five that fail all passed in v0.9 and in its retest; two failed on a single misread in a probe, three on
half points. The retest put reader variance at about five templates between screens, so the count of 59
should not be read as no progress over the retest: the ten templates with causes fixed all reached full
marks, and the five new failures each have a cause visible in the picture (below).

## What reads poorly (the v0.11 list)

| # | Sev | Template | v0.10 mean | What the readers saw | Fix for v0.11 |
|---|---|---|---|---|---|
| R1 | B | `wave` | 0.67 (3 items, 1 misread) | In a probe the waving man stood against the house corner, his raised hand at the wall's edge: "standing behind the corner, peeking out or watching ... one hand looks like a loose fist". The other two pictures read "waving" | Keep people clear of the house walls by a margin (the house is a backdrop, so the structure check never saw it) |
| R2 | B | `ball_in_tree` | 0.89 (1 misread) | In a probe the teenager reaching up toward the ball stood where a hat was blowing away: "both arms raised above his head, mouth open, looking surprised; wind lines start just beside him". Both set pictures read fully | Never put the ball in the tree and the windy hat in one picture (both are a reach into the air) |
| R3 | C | `kite_in_tree` | 0.89 | Twice "as if flying there or caught in the branches": the kite is drawn whole in front of the canopy | Tuck the kite into the canopy, leaves over one corner, the string slack and drooping |
| R4 | C | `rain_coming` | 0.83 | In the busiest street the pointing child stood under the tree with the fish in it: "pointing up at the fish in the tree"; in a garden the pointing was one of three readings and nobody said rain | Keep the pointing line clear of trees and of anything else in the air; a worried face to the clouds |
| R5 | C | `dog_playing` | 0.83 | In the busiest park the play-bowing dog faced the square-wheeled wheelbarrow: "crouching and sniffing" it | The play bow faces a person or open ground, never an object |

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.11 |
|---|---|---|---|---|
| O1 | B | On the ordinary seesaw "the boy looks bigger than the girl, yet his end of the seesaw is up and hers is down" | 3 probes | Two children: the bigger child's end is the low one |
| O2 | C | The waving man "cut off by the house corner" | 1 probe | R1 |
| O3 | C | A picnic basket drawn over the sitter's legs: "as if it sits on or passes through his shins" | 2 probes | Basket beside the sitter, clear of the legs |
| O4 | C | The dog reading the newspaper "could be read as a goat or cat", "a fox or kangaroo" | 2 pictures | Rounder ears and a shorter tail for the sitting-up dog |
| O5 | C | The dustpan "lying on the grass rather than held, so the dirt may not end up in it"; a watering can "stands on or next to" it | 2 probes | The dustpan touching the heap, kept clear of fillers |
| O6 | C | The child on the slide "sits a little above the chute line, so he could look slightly 'stuck on' ... but it reads as sliding" | 1 probe | Seat a little lower into the chute |
| O7 | C | A cap "going the opposite way to the wind" | 1 picture | The hat flies with the wind |
| O8 | C | A swing hanging straight: "She doesn't seem to be swinging" | 2 pictures | A tilted swing (as in v0.5 to v0.8) only where the rider faces the viewer and clears the ropes |

None of the v0.9 oddities came back: no stepping stone behind a dog, no outsized sandwich, no teenager on
a barely tipped seesaw, no photographer from behind, no shins across the seesaw board, no dashed upward
stream.
