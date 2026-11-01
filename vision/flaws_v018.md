# v0.18 blind screen: what it found (the work list for v0.19)

The v0.18 screen used the same method and prompts as the fourteen before it (`screen_prompts.md`). Nine readers
who never saw the key described 60 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16 showcase
pictures and 5 isomorphs) and 39 probe pictures. Three scorers with the same prompt scored pictures 1 to 18, 19 to 39
and 40 to 60 against `keys.json` (`scores_a.json` to `scores_c.json`, merged in `scores.json`). Per-template means are
in `../vision/screen_summary.json` (`by_template`; probes count there, not in the headline figures). The gate is in
`gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) | v0.13 (21) | v0.14 (21) | v0.15 (21) | v0.16 (21) | v0.17 (21) | v0.18 (21) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.995 | 0.988 | 0.996 | 0.995 | 0.986 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 |

For the seventh screen running no item in the set was misread; one probe item was (a frying pan read as a hose
nozzle). Across all 60 pictures 710 of 720 scored items had full marks: one misread, one zero and eight half points.
Every contradiction in the set was read in full. The set's actions fell from 1.00 to 0.98 and its inferences from 1.00
to 0.95, nearly all of it in two tier-4 pictures: in the garden a cat on the fence read as walking, not stalking, and a
boy's raised arms as "cheering, stretching or waving"; in the park a teenager reading as she walks read as "holding an
open newspaper" and was not seen as about to trip, and a duck swimming to the bread was not said to want it. The one
other half point in the set was a girl's reach toward a ball in a tree, read as "reaching up ... or waving or cheering".
Oddities rose in the set from 27 to 40 and in the probes from 35 to 41.

## The v0.17 failure and the visuals refined in v0.18

| Template | v0.17 | v0.18 | What the readers saw in v0.18 |
|---|---|---|---|
| `wave` | 0.83 (3 items, 3 pictures) | 1.00 (4, 4) | Read as a wave in all four, twice with the motion marks named: in the set, a young man "facing left with one hand raised, waving (motion marks around the hand)"; in the probes, "right arm raised waving", "waving one arm high above her head", "waving one raised hand, with motion lines around it". No reader saw a string, a held object or a line at the raised hand |

The other visuals refined for the v0.17 oddities read as meant wherever they were screened. The dark-haired woman, her side
hair now behind the ear, was in 16 of the 60 pictures, ten of them in profile (reading as she walks, carrying a parcel,
painting, watering, walking a dog, feeding ducks, hanging washing): "walking left while reading an open book and not
looking where she is going"; no reader said her face was missing or hidden. The sleeping cat, 1.4 times its v0.17 size, read as "curled up asleep" in all three of its pictures, but one
probe reader added "it is small", as the bench had predicted (`isolation_v018.md`). The larger stalking cat on the grass
read in full in both its pictures ("crouched low and moving to the right, stalking or chasing the bird"), and no reader
said the bird was large next to it; on the fence it read as walking (R2 below). Catches (4 pictures) read in full, with
no catcher drawn into another figure and no ball heading for someone else; no duck's wake reached anyone; and no filler
read as cut off by the picture's edge. No sprinkler stood under storm clouds, no fishing line crossed a figure (one
reader added that a float was "not far from the duck"), and the picnic never met the soaked box.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 | 395 | 396 | 406 | 398 | 397 | 391 |

60 of 64 pass, every template screened in at least three pictures (50 in three, 11 in four, 1 in five, 1 in six, 1
in seven). The v0.17 failure passes. Four templates fall short, each in a single picture, and all four passed in full in
v0.17 (the reading walker in six pictures). The retest of the v0.9 pictures put the gate's reader variance at about
five templates between screens, but each of the four has a cause in its picture that can be fixed:

## What reads poorly (the v0.19 list)

| # | Sev | Template | v0.18 mean | What the readers saw | Fix for v0.19 |
|---|---|---|---|---|---|
| R1 | C | `about_to_trip` | 0.875 (12 items, 4 pictures) | In the tier-4 park, which is windy, a teenager at the back holds her open book wide: "walks along reading or holding an open newspaper", "could be reading a newspaper, a map, or struggling to hold papers in the wind"; the bucket ahead of her "has no obvious owner or purpose", so no trip was predicted. Read in full in its three other pictures | No reading walker in a windy picture (open pages beside wind lines read as papers blowing); the walker not at the far back, as the waver, so the bucket reads as in her path; bench the head bend again: v0.18 raised every reading walker's head from 30 to 20 degrees for the dark-haired woman's face, and the others may need the 30 back |
| R2 | C | `cat_stalks_bird` | 0.889 (9 items, 3 pictures) | In the tier-4 garden the cat on the fence top read as "walking along the top of the fence, facing left toward the blue bird", stalking "possibly" only in the unsure section; the bird pecking on the fence "in an awkward pose with its wing up". Read in full on the grass in both other pictures | On the fence, the cat closer to the bird (it was well over a cat's length away) and the bench to say whether the crouch reads on the fence top, where the rail hides the legs; the fence bird perched rather than pecking |
| R3 | C | `pan_watering` | 0.833, 1 misread (9 items, 3 pictures) | In a probe, the pan held nearly edge-on beside a hose reel read as "a dark grey hose nozzle or watering wand ... not attached to any hose", noticed as odd but never as a pan. Read as a frying pan in its two other pictures | No hose reel or hose beside the pan waterer (a shared exclusive resource), and the pan turned so its inside shows |
| R4 | C | `run` | 0.833 (3 items, 3 pictures) | In a probe a woman on the grass read as "striding or jogging", "walking briskly or jogging". Read as running in its two other pictures | Motion lines behind the runner, or a stride with both feet off the ground |

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.19 |
|---|---|---|---|---|
| O1 | C | Figures drawn tight against things: a begging dog's paws "overlap the woman's legs and the bench (cramped)"; a photographer "inside the swing frame"; a woman "tightly overlapping the lamp post"; a man against a fruit stall's legs and a lamp post "right behind the reading woman"; a hose "very tightly behind/around the old man's legs" (again); a reed behind a head; a head in front of the washing; a picnic basket over a lap | 4 set pictures, 4 probes | Revision 16's body gap extended to the tall structures of the backdrop (lamp posts, the swing frame, the stall) and to the begging dog against the seat; the hose kept a body width from the waterer's legs |
| O2 | C | The child reaching for a ball in a tree stands "beside the trunk, not under the stuck ball", "nowhere near the ball, so she cannot be literally reaching it" (and twice the reaching read as "cheering or waving", the two half points of `ball_in_tree`) | 3 set pictures | The child under the ball's side of the crown, close enough that the reach reads as a reach |
| O3 | C | Kicks and painting: the kicker's foot "stretched past/over the ball, which is still on the ground: may be a swing-and-miss" (2); a kicked ball with no shadow; the painted fence section "to the right of the painter, not in front of her" (2); no paint tin near a painter | 1 set picture, 5 probes | The ball just ahead of the kicking foot; the painted boards in front of the painter's brush |
| O4 | C | Water drawn as dashes: a hose's water "drawn as a dashed line with gaps (could read as a dotted line)", a sprinkler's "readable as a dotted trajectory rather than water", a stream that "starts slightly to the side of the hose nozzle" | 1 set picture, 2 probes | A solid stream for hose and sprinkler water (dotted lines are kept for a ball's flight) |
| O5 | C | Sizes: a red bird "quite large for the top of the lamp"; an old woman at the back "almost the same size as the people in front"; a sleeping puppy "small enough to be mistaken for a lamb or rabbit"; the sleeping cat "small" (above) | 2 set pictures, 2 probes | Check the bird on the lamp and the puppy against their depth; the sleeping cat stays a note for the pilot |
| O6 | C | Goats "unusual" in a garden or park (4), and a goat's head "turned at an awkward, twisted angle", "drawn a little oddly (round, one curved horn)" (2) | 1 set picture, 3 probes | Note for the pilot, as since v0.11; bench the grazing head |
| O7 | C | Drawing quirks: a dog's head "twisted and almost upside down" eating the dropped ice cream; a dog "long and low with back legs trailing"; a boy's head "almost seen from behind while the body is side-on"; the back of a head on the slide; a waterer's head "mostly dark"; a grey rock that "could be a rock or a half-buried ball" (2); a picnicker leaning back "with no visible arm support"; a blocked hose's bulge "like a balloon"; duck food "could be read as small pebbles" | 6 set pictures, 4 probes | Bench the dog eating the ice cream and the boy's walking head; the rest smaller remarks, each in one picture |
| O8 | C | Older ones: a market stall with nobody at it (4); a dog with no lead or owner; a swing with no one pushing; a man on a seesaw (3); a workman in a home garden; running on the grass beside a path; fallen leaves under green trees; wind that does not reach the trees or a dress; a fisher standing back from the water (2), a float near the duck; a pram heading toward a sleeping puppy | 10 set pictures, 5 probes | None needed (events, not contradictions, or drawing style); note for the pilot, as since v0.11 |

Smaller single remarks, each in one picture: a carrier facing right "while the path runs toward the viewer", a cat on
the fence top "overlaps the tree's leaves", hedged readings of a jumping girl and a seesaw rider as "floating", a pet
bowl no animal eats from, the old woman's feet on the path beside her pram on the grass, extra predictions (a hose about
to burst over a worker, a runner about to collide with a cheering girl), and a sun drawn partly off the top edge, noted
in passing.
