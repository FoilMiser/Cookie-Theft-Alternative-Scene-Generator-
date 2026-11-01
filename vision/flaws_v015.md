# v0.15 blind screen: what it found (the work list for v0.16)

The v0.15 screen used the same method and prompts as the eleven before it (`screen_prompts.md`). Nine readers
who never saw the key described 62 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16 showcase
pictures and 5 isomorphs) and 41 probe pictures, one of them built so that a waving child would be read (the
v0.14 failure was an adult's wave, and no child had waved in a screened picture). Three scorers with the same
prompt scored pictures 1 to 20, 21 to 40 and 41 to 62 against `keys.json` (`scores_a.json` to `scores_c.json`,
merged in `scores.json`). Per-template means are in `../vision/screen_summary.json` (`by_template`; probes count
there, not in the headline figures). The gate is in `gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) | v0.13 (21) | v0.14 (21) | v0.15 (21) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.995 | 0.988 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 |

For the first time no item anywhere in the screen was misread, set or probes. Across all 62 pictures 731 of 738
scored items had full marks (0.995), against 699 of 703 in v0.14: six half points and one zero, six of the seven
in three set pictures (below) and one in a probe (a dog at a bench "begging for the ice cream or wanting
attention"). The set's figures fall a little from v0.14's because three of its pictures each put one visual
where something else drew the eye; every one of those visuals read in full in its other pictures. Oddities
in the set held at 29 (28 in v0.14); in the probes they fell from 47 to 39.

## The v0.14 failure and the visuals redrawn in v0.15

| Template | v0.14 | v0.15 | What the readers saw in v0.15 |
|---|---|---|---|
| `wave` | 0.67 (3 items, 3 pictures) | 1.00 (3, 3) | A worker in a hi-vis vest waving; a man at a fruit stall waving "as if saying hello"; and the probe's waving child: "a small girl in a pink dress with her hair in buns is smiling and waving one raised hand, with small lines by her hand showing the waving motion" |

The visuals redrawn or moved for the v0.14 oddities read with full marks wherever they were screened: the walker
reading on the way to a bucket "about to trip over it" in all six of its pictures (18 of 18 items, against 0.93
in v0.14); the lost balloon in all four; the sprinkler and its wet package in all three; the kite flyer, the
swing, the sweep and the rake in all three; the sleeping cats and dogs in all seven; the picnic in all three.
No bird in the screened pictures sat in a tree's crown (the branch under one was read in the design tests); the
bird that lost half a point sat on the fence (below). No reader saw a leg come apart from a body, a hose across a path, a bush or a bird table behind the
fence, a sleeper on the pavement, a picnic or a sprinkler under storm clouds, or closed eyes on a chore.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 | 395 | 396 | 406 |

61 of 64 pass, every template screened in at least three pictures (48 in three, 10 in four, 3 in five, 3 in
six). The wave passes. Three templates fall short, none on a misread: each lost its points in one set picture,
where something next to it pulled the reading elsewhere, and read in full in its other pictures.

## What reads poorly (the v0.16 list)

| # | Sev | Template | v0.15 mean | What the readers saw | Fix for v0.16 |
|---|---|---|---|---|---|
| R1 | B | `cat_stalks_bird` | 0.89 (9 items, 3 pictures) | In the tier-4 garden isomorph a second cat walked the same fence just behind the stalking cat, and a teenager pointing up at a ball in the tree raised his hand right beside the stalker: the stalker "may be heading towards the red bird along the fence (stalking it), or just walking along", the other cat "sits", and the teenager "could be pointing at the black cat (his finger is right next to it) or at the blue ball". Read in full in its two other pictures | No other cat on the fence a cat is stalking along, and a pointing hand kept clear of every animal but what it points at |
| R2 | B | `seesaw_heavy` | 0.88 (12, 4) | In the tier-3 playground isomorph, among five events at the back right: the girl "sitting on the raised end holding the handle, legs dangling with motion lines", read as ordinary play; nothing of his weight or her being stuck. Read in full in its three other pictures ("stuck up in the air") | The motion lines at her feet read as play: try her without them, calling down to him, on the bench first; and the seesaw nearer the front in a busy picture |
| R3 | C | `bird_perched` | 0.83 (3, 3) | A bird on the garden fence just under the clothesline, "perched on the line" | A bird on the fence never under the stretch of a clothesline |

The begging dog lost a half point once and passes (`dog_begs`, 0.94): "begging for the ice cream or wanting
attention".

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.16 |
|---|---|---|---|---|
| O1 | C | Someone at the back drawn too big for the distance: "older woman at the back fence drawn about four times the fence height, looming over the hedge" (and in the design tests "a man waving at the back who looks a little large for his distance") | 1 set picture | People standing at the back of the playground scaled against its railing; check every setting's back row |
| O2 | C | Unrelated things that touch: a goat "partly through" a woman's legs; a pram's front on the foot of a ladder ("about to knock it over") or heading into a lamp post; the door knob "on the dog's head" (twice); a seated man's cap on the pond's edge; a child over the edge of a slide's chute; a hose bulge just behind the dog's paw | 1 set picture, 7 probes | A gap between unrelated people, animals and objects at the same depth; nothing in front of the door knob |
| O3 | C | A walker heading for something that is not their event: "child walking toward the ladder might bump into it", "girl and dog walking toward the hose ... might trip over it", a kicked ball "may be heading toward the painter"; a ball "may sail over his head" or "fall short into the water" | 2 set pictures, 3 probes | Walkers' and balls' lines kept clear of other events' objects (an unintended "about to happen" competes with the real ones) |
| O4 | C | The square-wheeled bicycle "stands upright on its own" | 2 set pictures | A kickstand drawn, or the bicycle leant against a wall or post |
| O5 | C | Jumpers high enough to seem to float ("level with the fence top; could be read as floating") | 2 set pictures | A lower jump, its shadow closer under it |
| O6 | C | Faces and directions: a dog on a lead facing away from where its walker goes; a kicker's head turned to us while he kicks to the side; a stiff stride; readers' downcast eyes "reading intently ... or dozing" | 2 set pictures, 3 probes | Lead dog faces the walking direction; the kicker looks at the ball; open eyes for reading, as for chores |
| O7 | C | Water drawn as "chunky linked blobs", pouring "from the side of the pan" | 1 set picture, 2 probes | A smooth stream from the pan's lip and the watering can's rose |
| O8 | C | A baby in a pram "has no face", "could be read as a pillow or ball" | 1 set picture, 1 probe | A face on the baby |
| O9 | C | Older ones, smaller now: wind that leaves hair and trees still; swing ropes hanging straight with motion lines; brown leaves under a green tree; a single swing on a wide frame; a hat that could be "caught against the upstairs window"; a scene recognised as "the same as in another street scene" | 1 set picture, 5 probes | Hair is the 3D cast's; the swing's ropes could tilt with its motion; the repeated group is the isomorph design, for the pilot to keep apart |
| O10 | C | A goat in a garden or park, digging in a park, a delivery in a park, an empty street, a pet bowl with no owner, a grown man on a child's seesaw | 5 set pictures, 2 probes | None needed for legibility (events, not contradictions); note for the pilot, as since v0.11 |

None of the v0.14 oddities came back as reported then: the washing lifts in the kite's breeze, the bushes and
the bird table stand in front of the fence, no hose crosses a path, no chore face looks closed, no lost balloon
shares a colour, no cat sleeps on the pavement, no picnic or sprinkler
runs under storm clouds, and the swing's hands hold its ropes. No reader reported a gap in anyone's body.
