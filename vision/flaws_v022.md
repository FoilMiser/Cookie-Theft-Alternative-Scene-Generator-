# v0.22 blind screen: what it found (the work list for v0.23)

The v0.22 screen used the same method and prompts as the eighteen before it (`screen_prompts.md`). Nine readers
who never saw the key described 65 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16 showcase
pictures and 5 isomorphs) and 44 probe pictures. Three scorers with the same prompt scored pictures 1 to 22, 23 to 43
and 44 to 65 against `keys.json` (`scores_a.json` to `scores_c.json`, merged in `scores.json`). Per-template means are
in `../vision/screen_summary.json` (`by_template`; probes count there, not in the headline figures). The gate is in
`gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) | v0.13 (21) | v0.14 (21) | v0.15 (21) | v0.16 (21) | v0.17 (21) | v0.18 (21) | v0.19 (21) | v0.20 (21) | v0.21 (21) | v0.22 (21) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 0.996 | 1.00 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.985 | 1.00 | 0.971 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.995 | 0.988 | 0.996 | 0.995 | 0.986 | 0.989 | 0.998 | 0.989 | 0.997 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 |

285 of 287 scored items had full marks and none was misread. The v0.21 misread (a frying pan held against a grey shop
door in the street) is gone with the pan out of the street, and the contradictions are back to 1.00. Both half points
are inferences in the tier-4 street, from the same reader, each offered as one of two readings: a dog in front of a man
eating ice cream on a bench, "perhaps hoping for some ... or just walking by", and a woman reading as she walks with a
box "to the side of / slightly ahead of" her, who "might trip over it, or ... might simply walk past it". In the probes
one item was misread, both of its contradiction items: in a garden a woman watering the flower bed with the frying pan,
held close in front of the flowers, read as holding "a grey, round watering can" ("I could not clearly see a spout or
handle"; "I saw nothing that looks impossible"). Every other probe item had full marks. Oddities were 25 in the set
(24 in v0.21) and 54 in the probes (34), most of them small remarks on drawing.

## The v0.21 list and the rules of revision 20

Every v0.21 shortfall that revision 20 and the bench addressed read in full. The jumper read as jumping in all three
of its pictures (1.00); the ladder leaning on nothing, its top up against the hedge, in all three ("a ladder could not
stay up on its own", never "lying flat"); the square wheel in all three, the barrow's new eight-spoked wheel included
("its wheel is square, which wouldn't roll"), with no reader seeing a round wheel inside a square. No sprinkler hose rose
from the bottom edge (one, run behind a flower bed to the side edge, was offered as "a narrow stream or ditch", the hose
the main reading); no kick was aimed at anyone; no foot stood on a wheelbarrow's handles; and no reader gave the reading
walker a second hazard further along her way. The frying pan read as a frying pan in two of its three garden probes,
where its handle showed against the fence or the grass, and was misread in the third.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 | 395 | 396 | 406 | 398 | 397 | 391 | 407 | 390 | 396 | 394 |

63 of 64 templates pass; every template was screened in at least three pictures (54 in three, 6 in four, 1 in five,
3 in six). The one that falls short is the frying pan (0.778, the probe misread), for the second screen running. The
two half points of the set leave `dog_begs` at 0.944 and `about_to_trip` at 0.958, both passing. The v0.9 retest put
the gate's reader variance at about five templates between screens.

## What reads poorly (the v0.23 list)

| # | Sev | Template | v0.22 mean | What the readers saw | Fix for v0.23 |
|---|---|---|---|---|---|
| R1 | A | `pan_watering` | 0.778 (9 items, 3 pictures; 1 misread) | In a garden probe the pan held close in front of the flower bed, the hand over its short handle and the flowers behind it: "a grey, round watering can ... could be read as a watering can, a bucket or even a stone". Read as a frying pan in its other two probes, where it was held further out and its handle showed against the fence or grass ("a frying pan is a strange thing to water with") | To the isolation bench: the pan held out from the body with the whole handle in view, its silhouette against the grass rather than the flowers, and its face turned more edge-on |
| R2 | C | `dog_begs` | 0.944 (9, 3) | In the tier-4 street a dog with one paw raised in front of the man eating ice cream: "perhaps hoping for some ... or just walking by"; in the tier-3 street "sitting up begging with a paw raised, but its back legs and tail stretch out as if it were half-lying" | The beg pose to the bench: haunches down and tail curled in, so the dog sits up |
| R3 | C | `about_to_trip` | 0.958 (12, 4) | In the tier-4 street the box "to the side of / slightly ahead of" the reading walker, 25 px ahead of her leading foot and a little in front of her line | The obstacle squarely on her line and a full step ahead of her leading foot |

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.23 |
|---|---|---|---|---|
| O1 | B | The older man's grey ring of hair, seen in profile, read as "a beard" or "a face mask", so the way he faces was unclear ("in which case he would seem to be facing the other way"); in the tier-4 park he was read as walking toward the sleeping cat on the path behind him, "so he might trip over it or step on it" | 1 set picture, 4 probes | The cast: the older man's profile head with the grey hair kept to the back, above the ear, and a nose or face line in front so the facing reads; to the bench |
| O2 | C | Other extra stories: a runner and a woman pushing a pram "heading toward each other ... might bump into each other" (60 px apart in depth); a duck "swimming close to the float, so the duck might go for the bait or get tangled in the line" (2); a runner "with an outstretched arm toward nothing visible" | 1 set picture, 3 probes | A runner's lane clear of anyone heading toward her on the same line; ducks kept clear of a fishing line and float |
| O3 | C | Hoses: the blocked hose's bulge read as trapped water (2, as meant), a hose rising in front of a woman's legs, a sharp bend up to the nozzle, upward water "drawn as a solid outlined tube" | 4 probes | Note for the pilot |
| O4 | C | The wheelbarrow's stand "looks a bit like a boot" | 2 probes | Redraw the barrow's stand as a thin leg |
| O5 | C | Figures: an angler's upper body over the pond, his feet on the bank (2); a dog's red bandana read as "a hat, bow or red ear" (2); a dog's paws "like white cartoon hands"; an older woman at the back "drawn too large" (2); a digger looking away from her hole (2) | 1 set picture, 8 probes | Note for the pilot (the cast is a stand-in; sizes at the back as since v0.19) |
| O6 | C | Older ones: goats in a garden or park (3); a stall with nobody at it; sweeping a path with nothing on it; wind under a clear sky (2); a neat painted rectangle; paw prints out of step; a seesaw "almost level"; an empty middle to the playground; the sun cut by the top edge | 2 set pictures, 9 probes | None needed; note for the pilot, as since v0.11 |

Smaller single remarks, each in one picture: a kite string sagging into a dip and one crossing the clothesline, the
thing under a sandwich (plate or wrapper), a picnicker's closed eyes (dozing or wincing), an unclear object in a
gardener's hand, a goat with one horn, and the storm that only the pointing man reacts to.
