# v0.5 blind screen: what it found (the work list for v0.6)

The v0.5 screen used the same method as v0.4: three readers who never saw the key described seven
pictures each (`desc_pic_NN.md`), and a fourth scored them against `keys.json` (`scores.json`,
`scores_summary.md`). Per-template means are in `../vision/screen_summary.json` (`by_template`).

## What improved

Unintended oddities fell from 99 in 15 pictures (6.6 per picture) to 37 in 21 (1.8 per picture).
Every template the v0.4 screen flagged reads better except the lost balloon (R5 below): play catch 0.69 → 0.96, waving 0.33 → 1.00,
drinking on a bench 0.25 → 1.00, dog begging 0.67 → 0.92, kite in a tree 0.83 → 1.00, rain coming
0.67 → 1.00, taking a photo 0.75 → 1.00, sleeping animals 0.50–0.75 → 1.00. Actions overall rose from
0.87 to 0.92. The new playground events (seesaw, slide, sandbox, stroller), hanging laundry, painting
the fence and all three new contradictions (sitting on air, ladder leaning on nothing, dog reading)
were read correctly.

## What reads poorly (scored items)

| # | Sev | Template | Mean | What the readers saw | Fix for v0.6 |
|---|---|---|---|---|---|
| R1 | A | `ice_cream_drop` (first screened) | 0.42 | The ice cream on the ground was "a pink object" (bag, cake, shoe, frisbee); the empty cone was not seen, so the child was "pointing" | Draw a scoop with drips, highlight and a cone lying beside it; larger cone in the child's hand, held up and looked at |
| R2 | A | `floating_box` (first screened) | 0.50 | The box read as standing on the pavement; its shadow was "a stray shadow with nothing above it" | Lift the box clearly (at least half its height above the shadow) and put the shadow straight under it |
| R3 | A | `seesaw_heavy` (new) | 0.58 | The tipped seesaw was described, but nobody explained it by weight; one reader called the man "a boy" | Exaggerate the size difference (adult on the low end, small child high up, legs dangling); keep the low end on the ground |
| R4 | A | `square_wheel` on a wheelbarrow | 0.67 | Missed twice on the wheelbarrow ("an ordinary empty wheelbarrow"), caught on bicycles; a black square inside a square read as a box hiding the wheel | Draw the square wheel as a tyre with a hub and spokes, bigger, and side-on to the viewer |
| R5 | A | `lost_balloon` | 0.71 | Strings ending at a man's cap or at the clothesline read as tied there; children reaching up read as "pointing" | Keep the air under the string free of every element, not only people (revision 3 does people); reach-up pose with open hands, upset face kept |
| R6 | B | `bird_steals` (first screened) | 0.75 | The sandwich on the bench read as a stack of books | Draw the sandwich with bread crust, lettuce and filling, bigger; the bird's beak on it |
| R7 | B | `pan_watering` (first screened) | 0.67 | The frying pan read as a hose wand with no hose | A round pan seen from above at an angle, with a handle and water pouring over the rim |
| R8 | B | `feed_birds` (first screened) | 0.50 | The small seed bag in the worker's hand read as a brush or sanding block | Bigger paper bag held open, seeds visibly falling between hand and bird |
| R9 | C | `dog_reading` | 0.83 | The contradiction was always caught, but the paper was "a book standing up by itself" three times | The dog's front paws holding the paper's edges |

## Unintended oddities still reported

| # | Sev | Oddity | Where | Fix for v0.6 |
|---|---|---|---|---|
| O1 | A | A thin structure touching a person without crossing them: a lamp post standing on a cap, a catcher's hands against the lamp post, a dog's head against the post, a head against a tree trunk | 5 pictures | Extend the crossing rule with a clearance margin around heads and hands (tangency counts) |
| O2 | B | A person in front of the seesaw or overlapping its riders | 3 playground pictures | Treat a person's whole body (not only thin parts) against structures they do not use |
| O3 | B | A balloon held by its owner, with the string drawn straight over the face | T2 street | Hold the balloon to the side, string from the raised hand |
| O4 | B | A bicycle on its kickstand still read as standing on its own | T4 street | Larger kickstand, or lean it on the rack or a wall only |
| O5 | B | Watering streams that pass in front of the flower box or through the bed | 2 pictures | Aim the stream end at the soil inside the bed or box and draw it behind the front edge |
| O6 | B | A thrown ball's dotted path heading into the tree | T3 garden isomorph | Reject throws whose arc passes through a canopy |
| O7 | C | A duck's wake on the side it faces | T4 park isomorph | Mirror the wake with the duck |
| O8 | C | Pots on stepping stones, a dog bowl at the edge of a dug hole, lone ball and rock in corners | 4 pictures | Keep fillers off paths and away from scored props |
| O9 | C | Bench drawn with seat and back at similar size read as a picnic table | T2 playground | Thinner back rail, legs under the seat only |
| O10 | C | Not reported by the readers, seen on inspection: the grandfather's grey fringe looks like a pad over the ear in some side views, and like a band from behind | gallery; scenes at 45° and 90° read as hair | Hair behind the ear only, tufted edge, down to the nape |

Readers also named weather and activity mismatches (storm clouds over people hanging washing) and a
goat in a back garden as odd. Those come from the content model, not the drawing, and stay.
