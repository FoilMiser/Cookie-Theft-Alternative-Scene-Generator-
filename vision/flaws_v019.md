# v0.19 blind screen: what it found (the work list for v0.20)

The v0.19 screen used the same method and prompts as the fifteen before it (`screen_prompts.md`). Nine readers
who never saw the key described 65 pictures (`desc_pic_NN.md`): the 21 pictures of the set (16 showcase
pictures and 5 isomorphs) and 44 probe pictures. Three scorers with the same prompt scored pictures 1 to 22, 23 to 43
and 44 to 65 against `keys.json` (`scores_a.json` to `scores_c.json`, merged in `scores.json`). Per-template means are
in `../vision/screen_summary.json` (`by_template`; probes count there, not in the headline figures). The gate is in
`gate.json`.

## Headline (the 21 pictures of the set)

| | v0.4 (15) | v0.5 (21) | v0.6 (20) | v0.7 (21) | v0.8 (20) | v0.9 (21) | v0.10 (21) | v0.11 (21) | v0.12 (21) | v0.13 (21) | v0.14 (21) | v0.15 (21) | v0.16 (21) | v0.17 (21) | v0.18 (21) | v0.19 (21) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|------|
| Things | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 |
| Actions | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 |
| Inferences | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 |
| Contradictions | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.995 | 0.988 | 0.996 | 0.995 | 0.986 | 0.989 |
| Misread items | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 |

No item in any of the 65 pictures was misread or missed outright, as in v0.12, v0.13 and v0.16: 750 of 760 scored items
had full marks and ten had half points. For the eighth screen running no item in the set was misread, and every
contradiction in the set was read in full. The set's actions rose from 0.98 to 0.99 and its inferences from 0.95 to
0.96. Its six half points were in five pictures: in the tier-4 garden a boy jumping just below a perched bird read as
reaching for it, and the stalking cat on the fence as "stalking the birds or just walking along" in the unsure
section; in the tier-4 street whether the girl dropped her ice cream or the dog knocked it was left open; in a park
isomorph a girl on a bench held "something white ... as if drinking or eating" and the boy beside the dropped ice cream
was not said to have dropped it; and in another a teenager holding her cone walked toward that boy, "maybe to share
it". Oddities fell in the set from 40 to 27 and rose in the probes from 41 to 52, most of them small (below).

## The v0.18 failures and the visuals refined in v0.19

| Template | v0.18 | v0.19 | What the readers saw in v0.19 |
|---|---|---|---|
| `about_to_trip` | 0.875 (12 items, 4 pictures) | 1.00 (18, 6) | Read in full in all six, three of them tier-4 pictures (the playground, the street and a park isomorph): "walking to the right while reading an open book", "they look about to trip over it", "she looks about to trip over it". No reader said newspaper, map or papers in the wind |
| `cat_stalks_bird` | 0.889 (9, 3) | 0.944 (9, 3) | On the grass in two pictures, "crouched low and creeping ... about to pounce", "stalking towards the red bird"; on the tier-4 garden's fence, close to a perched bird, "creeping along towards a blue bird ... neither bird seems to notice", the unsure section adding "could be stalking the birds or just walking along" (a half point for the inference) |
| `pan_watering` | 0.833, 1 misread (9, 3) | 0.944 (9, 3) | With no hose reel beside it, read as "pouring the water out of a frying pan instead of a watering can" and "what looks like a frying pan or saucepan"; in one probe only as "a grey round object held by a handle", the pan one of two readings beside "the spray head of a hose or can drawn without its body" (a half point). No reader said nozzle or wand; three noticed a watering can lying unused on the lawn nearby (O1) |
| `run` | 0.833 (3, 3) | 1.00 (3, 3) | Read as running in all three, each time by the motion lines: "running fast to the right, with speed lines", "running/jogging with motion lines" |

The other visuals refined for the v0.18 oddities read as meant wherever they were screened. The child under a ball in a
tree now points at it: `ball_in_tree` read in full in all six of its pictures ("pointing up at a blue ball stuck in the
branches", "the girl wants someone to get the ball down"), and no reader said the child stood beside the trunk or was
cheering. Kicks (3 pictures) read as kicks, none as a miss; water from a hose (3) and the sprinkler's arcs (3) read as
water, none as a dotted line; the soaked box read in full in all three pictures. No reader saw anyone against a lamp
post, inside the swing frame or among the stall's legs, nor a hand on the stall's fruit, and the curly-haired boy drew
no remark about his head. The begging dog, clear of the eater's legs, read as begging in two pictures and "begging for
the ice cream or barking" in the third, and twice its body as "stretched" (O8).

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.6 | v0.7 | v0.8 | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|------|
| Pass | 35 | 55 | 60 | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 |
| Read well, but in fewer than two pictures | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 6 | 9 | 4 | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 |
| Scored items behind the verdicts | | | | 302 | 302 | 388 | 381 | 382 | 395 | 396 | 406 | 398 | 397 | 391 | 407 |

60 of 64 pass, every template screened in at least three pictures (54 in three, 5 in four, 1 in five, 3 in six, 1 in
seven). All four v0.18 failures pass. Four other templates fall short, each on a single half point in one picture (the
bucket hat on two), and all four passed in full in v0.18. The retest of the v0.9 pictures put the gate's reader variance
at about five templates between screens, but each of the four has a cause in its picture that can be fixed:

## What reads poorly (the v0.20 list)

| # | Sev | Template | v0.19 mean | What the readers saw | Fix for v0.20 |
|---|---|---|---|---|---|
| R1 | C | `bucket_hat` | 0.889 (9 items, 3 pictures) | In a probe, a man at the back of the garden: "a tall blue hat", "could be read as a blue bucket worn on the head, or as a fez- or chef-style hat", never called wrong. Read as "a blue bucket upside down on his head" in its two other pictures | Draw the bucket's wire handle hanging beside the head and its rim, so it reads as a bucket at any depth; bench it |
| R2 | C | `drink_bench` | 0.833 (3, 3) | In a park isomorph a girl on a bench holds "something white ... to her mouth, as if drinking or eating". Read as "drinking from a white cup" and "a cup or mug" in the two others | A coloured cup with a lid and straw, held at the mouth, so it reads as a drink; bench it |
| R3 | C | `ice_cream` | 0.875 (4, 4) | In a park isomorph a teenager "holding her own pink ice-cream cone" walks toward the boy whose ice cream lies on the ground, "maybe to share it"; eating only in the unsure section. Read as eating in its three other pictures | No ice-cream eater in a picture with the dropped ice cream (two cones invite a story), and the cone at the mouth |
| R4 | C | `jump` | 0.833 (3, 3) | In the tier-4 garden a boy jumps with his arms up just below a bird perched on the fence: "jumping with his arms up near a blue bird", read as reaching for it. Read in full in its two other pictures ("as if celebrating or overjoyed") | No bird, perched or flying, above or beside a jumper's raised hands |

## Unintended oddities

| # | Sev | Oddity | Where | Fix for v0.20 |
|---|---|---|---|---|
| O1 | C | Watering beside a spare tool: "a proper watering can sits unused on the grass while she waters with a pan" (3); hose or pan water landing "at the front edge of the bed / on the grass rather than on the flowers" (2) | 4 probes | No watering can left on the lawn in a picture with the pan (as the hose reel since v0.19); the stream's end inside the flower bed |
| O2 | C | The garden's wheelbarrow "very flat on the grass with no visible legs, looks tipped or squashed" (3) | 3 probes | Redraw it standing on its wheel and legs; bench it |
| O3 | C | Overlaps: an empty swing blown "so far it overlaps (or passes through)" the frame's leg; a bicycle overlapping its rack; a woman merged with a towel on the line; a dog's foot on the sandpit frame; a dug hole over the path's edge; a leaning ladder's top over the pond; painted boards behind the birdhouse pole; a pram on the grass beside its pusher on the path | 2 set pictures, 6 probes | The blown swing seat inside the frame; the hole, the ladder and dogs clear of the path, the pond and the sandpit frame; the rest each in one picture |
| O4 | C | Sizes and depth: two pecking birds "quite large compared with the people", a bird on a bench "fairly large for a bird"; small figures read as far away (a girl with balloons by a shop window, a kite flyer, a child much smaller than the man) | 4 set pictures, 1 probe | Check the birds' scale on the ground and on benches against their depth; small children at the back stay a note for the pilot |
| O5 | C | Unintended stories: in a park isomorph the jogger "could have bumped the child and knocked the ice cream off"; in the tier-4 street whether the girl dropped her ice cream or the dog knocked it; a bird flying close to a kite | 2 set pictures, 1 probe | The runner kept away from the dropped ice cream; the rest note for the pilot |
| O6 | C | Wind that blows off a cap, an empty swing and the washing but leaves the tree, bushes, flowers and hair still (3) | 3 probes | Note for the pilot, as since v0.18 (`limits`) |
| O7 | C | Goats "unusual" in a garden or park (3), one "kneeling or stooping" | 1 set picture, 2 probes | Note for the pilot, as since v0.11 |
| O8 | C | Drawing quirks: the begging dog "stretched" (2); a catcher's hands pressed together with the ball at her face; a kicker's face hard to see, another's head turned from her reaching arms; faces too small to read (an old man licking an ice cream); a white object in a bird-feeder's hand ("cup of seed, paper bag or a drink") and one on a bench; dog bowls away from any dog (2); grey puffs by a dustpan; a painter's brush "or a small roller"; a white patch on a dog's chest; seed and crumb trails in mid-air (2, both dismissed) | 6 set pictures, 8 probes | Bench the begging dog's stretch; the rest smaller remarks, each in one picture |
| O9 | C | Older ones: watering or washing out before a storm (2); a stall with nobody at it; a man reading on a seesaw; one swing on the frame; a dog with no lead; a delivery man and a woman digging in a park; a lamp post alone on the grass; sweeping with no dirt; leaves under no tree; a fisher back from the pond; jogging on the grass; a sparse playground | 6 set pictures, 4 probes | None needed (events, not contradictions, or drawing style); note for the pilot, as since v0.11 |

Smaller single remarks, each in one picture: a carrier's walking direction "unclear", motion lines beside a still
swing seat, a slide's ladder "detached from the platform", a girl drawn "slightly above the chute" and another's legs in
front of the seesaw plank, a jumper's feet well above his shadow (dismissed as mid-air), a boy's feet planted ahead of
his seesaw seat, a pan pouring "more than a pan would hold", a kite string across the path at head height, painted
boards a different shape from the plain ones and a painter painting to the left of her own body, a hose passing "close
behind/beside the man's legs" but not through them, and an old man's expression hard to read.
