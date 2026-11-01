# v0.17 blind screen: what it found (the work list for v0.18)

The v0.17 screen used the same method and prompts as the thirteen before it (`screen_prompts.md`). Nine readers
who never saw the key described 65 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16 showcase
pictures and 5 isomorphs) and 44 probe pictures. Three scorers with the same prompt scored pictures 1 to 22, 23 to 42
and 43 to 65 against `keys.json` (`scores_a.json` to `scores_c.json`, merged in `scores.json`). Per-template means are
in `../vision/screen_summary.json` (`by_template`; probes count there, not in the headline figures). The gate is in
`gate.json`.

One reader saved three of its seven descriptions under rotated numbers (its description of pic_56 as
`desc_pic_58.md`, of pic_57 as `desc_pic_56.md`, of pic_58 as `desc_pic_57.md`). The scorer found the rotation from
the descriptions alone and scored each key against the description that matches it; the files were then renamed to the
pictures they describe, and the files as saved are kept in `v017/reader8_as_saved/` with a note.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) | v0.13 (21) | v0.14 (21) | v0.15 (21) | v0.16 (21) | v0.17 (21) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.995 | 0.988 | 0.996 | 0.995 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 |

For the third screen running no item anywhere was misread, set or probes. Across all 65 pictures 744 of 748 scored
items had full marks: three zeros, all the "few white clouds" of a picture whose reader named only the sun, and one
half point. Every inference and every contradiction in all 65 pictures was read in full (the set's inferences 1.00 for
the first time). Oddities in the set rose from 23 to 27 and fell in the probes from 37 to 35.

## The v0.16 failure and the visuals refined in v0.17

| Template | v0.16 | v0.17 | What the readers saw in v0.17 |
|---|---|---|---|
| `photo` | 0.83 (3 items, 3 pictures) | 1.00 (3, 3) | Read as a camera in all three, each time with someone to photograph: in the set, a woman "taking a photo with a camera pointed to the right" at a woman reading on a bench; in the probes, "holding a camera up to their face and taking a photo pointed to the left, toward the man" on his picnic blanket, and "holding a camera up to his eye and taking a picture towards the right" at a dog. No reader said binoculars |

The other visuals refined for the v0.16 oddities read in full wherever they were screened. The soaked box (9 items,
3 pictures, two in the set): "The water is landing on a cardboard box ... The box is getting soaked: water is running
down its side"; "has a puddle and drips around it"; "standing in a puddle, so the box is getting soaked"; no reader saw
water coming out of the box, or the box as a crate or a bale. The goat (3 pictures): "a white goat with small horns"
each time, though two readers added in their unsure section that it "could be read as a lamb or kid". The white dog
reading (3 pictures): "a white dog with brown spots ... sitting up ... holding an open newspaper and reading it, which is
impossible"; no reader saw a goat or a horn. Wheelbarrows (19 pictures): "a grey wheelbarrow rests empty on the grass",
none tipped. No reader saw a bird on the slide, a pram heading into anyone, feet on a bench, or a photographer with
nothing in front of the lens.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 | 395 | 396 | 406 | 398 | 397 |

63 of 64 pass, every template screened in at least three pictures (53 in three, 7 in four, 1 in five, 3 in six). The
v0.16 failure passes. One template falls short on a single hedge, in the set, with no misread; it passed in full in
v0.15 and v0.16:

## What reads poorly (the v0.18 list)

| # | Sev | Template | v0.17 mean | What the readers saw | Fix for v0.18 |
|---|---|---|---|---|---|
| R1 | C | `wave` | 0.83 (3 items, 3 pictures) | In the tier-4 park, a small girl far back on the path with one arm up, her hand right on the dark outline of the hedge line behind her: "a thin curly line near her raised hand. It could be (a) a string she is holding (for example a balloon string with no balloon visible), or (b) just a wave with a motion line. I could not tell which." Read in full in its two other pictures ("waving with one arm raised") | The waving hand and its motion lines kept clear of the backdrop's outlines (hill and hedge lines, fence tops, rooflines, awnings), as the pointing hand's line is kept clear of figures; and no waver at the far back, where the hand is a few pixels across |

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.18 |
|---|---|---|---|---|
| O1 | C | Two figures of different events drawn into each other: an old man reading as he walks and a man catching a ball "drawn overlapping, 'squashed together', one partly inside the other", and the ball "could hit the reading old man instead of reaching the catcher" | 1 set picture | A body gap between figures of different events at the same depth (revision 14 keeps only their feet apart), and the catch's flight clear of other figures, as the kick's already is |
| O2 | C | "Woman in yellow has no visible face; head is a round dark shape": the dark-haired woman in profile (catching, and reading as she walks), whose hair covers most of the head at that angle | 2 set pictures | Bench her profile head: more of the face showing in profile, or a three-quarter view for those poses |
| O3 | C | Sizes: a man at the back "a little too large for how far back he is"; a sleeping cat in front "very small compared with the people"; a pecking bird "fairly large compared with the cat" | 2 set pictures, 1 probe | Check the depth scale of the walk-with-bag figure at the back and of the small sleeping cat; the pecking bird's size against the cat's |
| O4 | C | A rubbish bin "partly cut off by the edge", though it now stands 6 px inside the frame | 1 probe | Fillers moved in further from the edge (about 30 px), so none reads as cut off |
| O5 | C | Goats "unusual to see in a back garden", "a goat in a city park" (a source of false contradictions), and twice "could be read as a lamb or kid" in the unsure section | 2 set pictures, 2 probes | Note for the pilot, as the goat has been since v0.11; the template stays (read in full in all three pictures) |
| O6 | C | Drawing quirks: a watering can's stream "drawn as separate light-blue segments; could read as a second hose"; a hose passing close to a figure's legs, "unclear whether it goes behind or loops around him" (2); the dog's lead by the hose reel "could be read as a red hose" (again); a pecking bird's head "pressed into the ground"; a fence painter's tool "brush or small roller on a stick" (2); a duck's wake lines running "to just above the man's head"; no shadow under the raised girl on a seesaw | 8 probes | The duck's wake lines kept short of figures; the rest smaller remarks, each in a probe |
| O7 | C | Older ones: a market stall with nobody at it (2); a dog with no lead or owner (2); people walking on the grass beside a path (3); watering before a storm (2); reading on a seesaw; the riderless square-wheeled bicycle standing on its own | 5 set pictures, 5 probes | None needed (events, not contradictions, or drawing style); note for the pilot, as since v0.11 |

Smaller single remarks, each in one picture: a kick "slightly above and behind" the ball, a carrier whose face and
stride "point opposite ways" (2), a man perched "just in front of the seesaw seat", a sleeping cat at two women's feet
"they might step on it", a kite string reaching a tree behind the fence "without clearly passing over the fence", a
dog-food bowl "on its own mid-lawn", leaves blown with a cap "with no tree near".
