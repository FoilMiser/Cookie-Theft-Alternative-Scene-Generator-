# v0.6 blind screen: what it found (the work list for v0.7)

The v0.6 screen used the same method as v0.4 and v0.5, with fresh readers. Four readers who never saw
the key described 25 pictures (`desc_pic_NN.md`): the 20 pictures of the set and five probe pictures
built for redrawn templates the set held fewer than twice. A fifth scored every description against
`keys.json` (`scores.json`, `scores_summary.md`). One reader cropped and enlarged parts of its
pictures before describing them, which is closer looking than a participant would do. Per-template
means are in `../vision/screen_summary.json` (`by_template`; probes count there, not in the headline
figures).

## Headline (the 20 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) |
|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 |
| Inferences | 0.86 | 0.72 | 0.86 |
| Contradictions | 1.00 | 0.75 | 0.91 |
| All items | 0.93 | 0.91 | 0.95 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 |

The oddity count depends on the reader as much as on the pictures: per reader it ran from 1.5 to 4.0
per picture this time. What matters is which kinds were reported (below).

## The templates v0.6 redrew

| Template | v0.5 | v0.6 | What the readers saw in v0.6 |
|---|---|---|---|
| `ice_cream_drop` | 0.42 | 0.94 | The scoop on the ground and the licking dog were always seen; once the cone was not clearly empty, so "dropped it" was hedged |
| `floating_box` | 0.50 | 1.00 | Always called floating, with nothing holding it up |
| `square_wheel` | 0.67 | 1.00 | Caught on wheelbarrows and bicycles alike |
| `pan_watering` | 0.67 | 1.00 | "Watering the flowers with a frying pan" |
| `dog_reading` | 0.83 | 1.00 | The dog holds the paper; never "a book standing by itself" |
| `ducks_bread` | 0.83 | 1.00 | |
| `lost_balloon` | 0.71 | 0.83 | No string was read as tied to anything; once the child read as cheering at a goat, so the balloon was only "perhaps" hers |
| `feed_birds` | 0.50 | 0.75 | The bird is always there now, but twice the grandfather's head faced the fruit stall, so "his bag is leaking" was offered as an equal reading |
| `seesaw_heavy` | 0.58 | 0.67 | The tilt is always described, never explained by weight (0 of 2 inferences) |
| `bird_steals` | 0.75 | 0.67 | Once read correctly; once the red bird at the sandwich was "a tipped-over red cup or flask" |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread of the main cue)

- **Pass (35 templates)**, among them the dropped ice cream, the floating box, the square wheel, the
  dog reading and the hose spray (first screened).
- **Read well but seen only once (18)**: pan watering, ducks and bread, paint tracks, the blocked hose,
  the dog that wants a walk, watering upward and 12 events. They need a second picture before the gate
  can pass them.
- **Fail (6)**: `sweep_fork`, `seesaw_heavy`, `bird_steals`, `feed_birds`, `lost_balloon`, `jump`.

## What reads poorly (the v0.7 list)

| # | Sev | Template | v0.6 mean | What the readers saw | Fix for v0.7 |
|---|---|---|---|---|---|
| R1 | A | `sweep_fork` (first screened) | 0.25 | Twice "holding a garden fork", "leaning on it", "about to dig": the sweeping and the fork-instead-of-broom were both misread | A sweeping pose (fork swept low and sideways, tines dragging), a small swept pile and dust in front of the tines, and a dining-fork shape (rounded neck, four slim tines) rather than a pitchfork |
| R2 | A | `seesaw_heavy` | 0.67 (meaning 0.00) | Positions described; nobody says heavier or stuck | Make the stuck child legible: legs dangling, both hands gripping, a worried face looking down; the grown-up settled and relaxed; consider a heavier build for the low end |
| R3 | B | `bird_steals` | 0.67 | A red bird against the red-crusted sandwich read as a cup | Songbird colour chosen to contrast with the sandwich; beak in the bread with a torn piece; the bird stands on the bench seat, not behind the sandwich |
| R4 | B | `feed_birds` | 0.75 | Seed falls to the birds, but the feeder's face is turned to the stall behind him | Head tilted down toward the birds (the gaze check already exists for other templates: use it here) |
| R5 | B | `lost_balloon` | 0.83 | One child reaching up read as cheering at something else | Keep other attention-getters (an animal, a jumper) out of the child's line of sight; an open-mouthed upset face |
| R6 | C | `jump` | 0.88 | A girl jumping, drawn low, read as kneeling with her arms up | Lift the jump higher off its shadow, legs tucked |

## Unintended oddities still reported

| # | Sev | Oddity | Where | Fix for v0.7 |
|---|---|---|---|---|
| O1 | B | A green blob sticking out of a tree's crown ("an attached bush") | 5 pictures | Draw the small side bush as a separate shrub on the ground, or drop it |
| O2 | B | Filler bicycles still read as standing by themselves | 4 pictures | Lean them on a rack or a wall only; never free-standing |
| O3 | C | Watering-can streams land at the front edge of the street flower box | 2 pictures | Aim at the middle of the box's soil, as the garden bed does |
| O4 | C | The seesaw man's legs lie along the plank awkwardly | 2 pictures | Redraw the seesaw-sit pose with knees bent over the plank |
| O5 | C | Unused props: empty picnic blankets, a café table with a cup and nobody, a red disc on the grass, two identical balls | 8 pictures | Fillers that read as someone's belongings only next to someone; no second ball beside a scored ball |
| O6 | C | A feeder or a photographer with nothing in front of them ("what is she photographing?") | 4 pictures | Photographer aimed at a scored event, checked like a gaze |
| O7 | C | Raking with no tree overhead; watering under storm clouds; a goat in a back garden | 3 pictures | Content model, not drawing: left as they are |

None of the v0.5 oddities came back: no pole, trunk or string touching a head or a hand, nobody
standing in a seesaw or on a bench, no string over a face, no stream past the bed, no throw into a
tree, no backward wake, no bench read as a picnic table.
