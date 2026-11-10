# TPDB v0.45: a larger ice cream, a camera on a strap, a trowel, a roller, a kite's reel, a picnic with its food, a duck in the water and a balloon let go, read a forty-second time

v0.44 ended with 63 of 64 templates through the gate: `ice_cream` fell at 0.85 in 13 pictures, on the girl in pink's cone when she walks with it in profile, "a small pink thing", "a tiny pink dot". Sam's brief for v0.45 was the drawings: improve the visuals, find the flaws and fix them. The work list came from two places:
- `vision/flaws_v044.md`: the ice cream (R1), the camera "or binoculars" (R2), the lost balloon held "by its very tip" (R3), the thief bird (R4) and a walker's "black ice skates" (O2);
- a fresh look at v0.44's pictures and cut-outs by four reviewers, each with a share of the set or the library (`tpdb_work/review45/`). They named what the readers had not: a duck standing on the water, a picnic with no food, a hose inspector looking away from the viewer, a trowel that was a grey line, a roller that was "a paddle", a carried box the fence's colour.

What two or more of the reviewers named, or a reviewer and the flaws list, was drawn. v0.45 benched the changes in whole pictures, v0.44's drawing beside v0.45's on the same seed, in two rounds, and took all of them (builder 0.45.0):
- **The ice cream:** cone and scoop half as big again in a child's hand, a third in a teenager's and a fifth in an adult's, the cone the wood's brown and longer above the fist, the scoop below and in front of the mouth; the empty cone larger in a child's and a teenager's hand too.
- **The camera:** a fifth larger, with a prism hump, a longer lens in a wide silver ring and a bright strap hanging in a loop under it.
- **The shoes:** the sole plate no longer than the shoe's flat underside and no wider than the shoe, dark under every shoe (under a walker's tipped foot it stood clear of the toe and the heel like a blade).
- **The hose inspector's head** toward the viewer and a little down at the nozzle (v0.44's turned it away, a sign error).
- **The props:** the trowel a broad pointed blade seen from its side on a bright handle; the paint roller a blue sleeve with a cream cap at each end on a cranked wire frame; the carried box khaki with a brown tape; the kite's reel two bright flanges with the cream of the wound string between them.
- **The swimming duck:** its legs are not drawn.
- **Placement revision 43:**
  - the lost balloon's string ends 62 to 80 px above the reaching hand and hangs in a slow wave with no curl, off a playground's railing and, in the garden, above the wooden fence's pickets;
  - the wet paint begins below the roller, which lies on bare wood at the paint's edge, the painter a step closer and the tin with them;
  - the planter kneels at the bed's end and digs in the bed, a hole under the trowel's point, the pot in front;
  - the picnic's loaf and bottle stand out of the basket, and a plate with a slice of watermelon lies on the blanket where it has room;
  - the goat's stake is clear of every standing structure;
  - a swimming animal is cut at a waterline with a ripple round it, and has no ground shadow;
  - the slide's ladder is the frame's own end, in the frame's red, and the bird table's post stands in a tuft of grass;
  - after the screen, the reading dog's paper lies on its paws.
- **Looked at and left before the readers:** a grey remix (every picture's grey twin would move for a cosmetic gain), the leash, the goat's profile, the throw and the tucked jump.
- **Not worked:** the thief bird (R4), first on the v0.46 list.

The set was regenerated and screened a forty-second time. Every person and the duck is drawn anew, so no picture is identical to v0.44's.

The forty-second screen read 93 pictures, the set's 21 and 72 probes, with twelve readers and four scorers: 992 of 1,009 scored items had full marks, and none was misread. All 64 templates pass the gate, for the first time since v0.41. `ice_cream`, v0.44's one failure, reads 1.00 in fourteen pictures, "a pink ice-cream cone" in a child's hand, and `photo` and `lost_balloon` read 1.00 in five each. The gate's first count failed `dog_reading` on one picture, its paper "up in the air", the paper v0.44's readers had twice called floating. After the screen the paper was drawn onto the dog's paws and the three pictures were read again: 1.00 in all three. `bird_steals`, which this release did not work, is the lowest at 0.933. Twelve of the 17 items under full marks are clouds or a tree that two readers left out.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.44 readers, or the reviewers, saw | v0.45 |
|---|---|
| `ice_cream` under the gate at 0.85, the girl in pink's "a small pink thing", "a tiny pink dot" | Cone and scoop larger in a child's hand: 1.00 in 14 pictures, "a pink ice-cream cone"; a sweet or a lollipop in no description |
| `photo` at 0.90, "a camera (or binoculars)" | Larger, on a strap: 1.00 in five pictures, "holding a camera up to his eye, taking a photo, with a red strap hanging from it"; binoculars in no description |
| `lost_balloon` at 0.944, "holding the string by its very tip, or has just let go" | The string's end well above the hand, in a slow wave: 1.00 in five pictures, "has escaped and is floating up into the sky, its string dangling" |
| "black ice skates" under a walker's dark shoes | The sole plate inside the shoe's underside: no skates in 93 descriptions |
| The hose inspector's head turned away from the viewer | Toward the viewer and down at the nozzle: `blocked_hose` 1.00 in seven pictures |
| The roller "a paddle", blue on a blue board; the trowel a grey line | `paint_fence` 1.00 in nine pictures, "painting the fence blue with a paint roller on a long handle"; `plant_flowers` 1.00 in five, "digging with a small trowel next to a pink flower in a terracotta pot, about to plant it" |
| The duck standing on the water; the carried box the fence's colour | `ducks_swimming` 1.00 in four pictures; `carry_box` 1.00 in three |
| A picnic with no food in sight | `picnic` 1.00 in three pictures: "a plate with a slice of watermelon, and beside him a wicker picnic basket with a bottle and a baguette" |
| The goat's stake standing on a bench's rail | Clear of every structure: "a peg in the ground", "a short wooden stake", tethered in all four pictures |
| The kite flier with no spool; the slide's ladder apart from its frame | "a kite reel" or "a kite spool" in the hand in six of the seven pictures with a kite on its string; `slide` 1.00 in three, no remark on the ladder |
| The reading dog's paper "floating" beside it (v0.44's watch list) | Left as it was, and it failed the gate's first count on a paper "up in the air". Drawn onto the paws after the screen and read again: 1.00 in three pictures |
| `bird_steals` at 0.967, the bird beside the sandwich | **Not worked, and 0.933:** "about to steal the sandwich, or just be perched next to it". First on the v0.46 list |

Left as notes for the pilot: the goat in a park "a little unusual", the crying child who "covers their eyes instead of looking at the dropped ice cream", and a second cardboard box that "has no obvious purpose".

## The isolation bench

As in v0.44 the bench read whole pictures: a tier-3 picture with the changed templates forced among the planner's own, built once in v0.44's drawing and once in v0.45's on the same seed (`vision/isolation_v045.md`). Round 1 had fifteen readers of 30 pictures, two to a reader; the ten new pictures were read twice, by different readers, and the ten old ones once:
- **A child's ice cream:** "holding a pink ice-cream cone" in both readings; v0.44's was "very small and could be read as a lollipop or a pink sweet rather than an ice-cream cone".
- **The planting:** "digging with a trowel" in all four readings, the pot "apparently waiting to be planted"; v0.44's had no trowel in either reading ("tending the colourful flowers").
- **The picnic:** the baguette and the bottle named in all six readings, and the plate with the watermelon slice in both readings of the picture that has it; v0.44's was "a wicker basket beside it", with no food named.
- **The kite's reel:** named in all four readings ("holding a kite spool up in one hand"); v0.44's was "I cannot see whether he has a spool".
- **The lost balloon:** "its string dangling free", and it "dangles well above his hand, so it seems he has just let go of it and can't reach it". But on the playground the end lay at the railing's top line: "caught on/attached to the fence rather than floating free".
- **The roller:** "painting the wooden fence blue with a paint roller on a long handle", but it "hovers slightly above the fence top line on its left edge".
- **The slide's ladder**, v0.44's own: "drawn in front of/ beside the red frame", in the old drawing and the new alike.
- **The camera, the shoes, the hose inspector, the box and the duck** read as well as they had. The camera's and the shoes' misreadings were the screen's, one in ten and one in eighty, and a bench of four pictures does not show them either way.

Round 2, two readers of the three pictures that changed, read the three fixes:
- **The painter** a step further forward: "painting the fence blue with a roller on a handle; a few boards next to her are already blue". Nothing hovers.
- **The balloon's string** clear of the railing's top line: "The yellow balloon's string ends in mid-air well above the girl's hand; she seems to have just let go."
- **The slide's ladder** as the frame's own end: "Slide with red ladder (left)", and no remark on it in four readings.

Before any reader, the bench's own look caught the planting: its first drawing, a dug patch on the lawn, lay under the planter's shoe, and it was redrawn twice. The goat's stake stood clear of every bench on the bench's seeds, so its rule was seen at work afterwards, on the seed of the v0.44 probe that had shown the flaw (design test 6, below).

## Design tests

The cast of builder 0.45.0 and revision 43 were read blind in whole test scenes among other events (`vision/design_tests_v045.md`, six pictures, one fresh reader each). Three placed on their first seed, one on its second and one on its 25th: it asked for an ice cream in a child's hand beside a lost balloon and a slide, and the cast has two children, so the slide's rider became a reader on a bench. The sixth is a v0.44 probe's own seed, where the goat's stake had stood on a bench. Three flaws came out of the readings, all three were fixed in revision 43 before the set was built, and tests 3 and 4 were built and read again:
- **The lost balloon's string.** First reading, its end under the playground railing's rail: "Its string ends in a small curl/hook just above the fence rail". The end now lies nowhere on a railing (`templates.RAIL45`). Second reading: "looks like a hook rather than a loose end". The string now hangs in a slow wave with no curl (`templates.CURL45`). Third reading: "its string dangling loose, so it looks as though she has just let it go". The balloon read as lost in all three.
- **The bird table's foot.** "The green patch at the base of the birdhouse pole is unexplained" became "a tuft of grass at the base" (`settings.FOOT45`).
- **A child's ice cream and the camera:** "holding a pink ice-cream cone", a cone in all three readings, at the size v0.44's was "a lollipop"; "holding a camera up to his eye and taking a photo", "camera on a yellow strap".
- **The roller, the trowel and the reel:** "holding a paint roller and painting the fence blue. A few fence boards next to him are already blue, and a paint tin stands on the grass by his feet"; "kneels by a round flower bed full of colourful flowers and digs with a small trowel"; "a red-and-white kite handle".
- **The picnic, the duck, the box and the slide:** "A wicker picnic basket on the blanket holds a baguette and a green bottle"; "a white duck swimming on it"; "carrying a cardboard box" in all three readings; "a playground slide with a red ladder and frame and a yellow/orange chute".
- **The hose:** its cause read in both readings, "the dog seems to be squashing or kinking the hose and stopping the water"; the inspecting is one reading of two, "about to spray (and soak) the drying clothes or the woman, or she may simply be puzzled that no water is coming out".
- **The goat's stake:** "It is tied with a rope to a small stake in the ground", the bench not named with it.

## Placement revision 43

Every record stores the placement revision it was made with. v0.45 pictures use revision 43:
- **The lost balloon:** its string's end 62 to 80 px above the reaching hand at full size (`templates.BAL45`), the string a slow wave that grows toward its free end, with no curl (`CURL45`). On a playground the end lies nowhere on the railing (`RAIL45`). In the garden it lies above the wooden fence's pickets, 34 to 48 px at full size, and a child whose hand would be more than 200 px below it is not stood there (`WOOD45`).
- **The fence painter:** the wet paint on the board under the roller begins below the roller, so the roller lies on bare wood at the paint's edge; the painter stands a step further forward until the roller lies well below the boards' tops, the tin with them (`templates.PAINT45`).
- **The planter:** kneels at the bed's end and digs in the bed, a hole under the trowel's point, a few clods beyond it, the pot in front of the bed (`templates.PLANT45`).
- **The picnic:** a loaf and a bottle stand out of the basket, and where the blanket has room a plate with a slice of watermelon lies on it (`templates.PICNIC45`).
- **The goat:** its stake never drawn in front of a standing structure (`templates.TETHER45`).
- **A swimming animal:** cut along a waterline with a ripple round it, with no ground shadow (`library.SWIM45`).
- **The slide's ladder:** the frame's own end, in the frame's red: two rails to the ground with slate rungs between them, the near rail running on up into the hand rail over the deck (`settings.SLIDE45`).
- **The bird table:** its post stands in a tuft of grass (`settings.FOOT45`).
- **The reading dog** (after the screen): its paper drawn 12 px toward the dog and 6 px higher, at the dog's scale, so the forelegs cross the near page and the paws lie on it (`templates.READ45`).

Each switch is "B"; any other value gives the rule's v0.44 form. A v0.44 record rebuilds with the v0.44 package. The cast redraws every person and the duck (builder 0.45.0).

Every cell of the set placed under revision 43: tiers 1 to 3 on their base seeds, but the tier-3 playground, which placed on the first seed of a fresh list, as in v0.44; the tier-4 garden, park and street on v0.44's seeds with the same templates. One prior moved after the set was built: the garden's lost balloon was lifted above the fence late (`templates.WOOD45`), and with the new prior the tier-3 garden's base seed gave other templates and the tier-4 playground placed on the 16th seed of its list. Both replace the earlier pictures. The five isomorphs pair the same cells as v0.44's, two of them on v0.44's seeds. The probe pass gave `ice_cream`, `photo`, `lost_balloon`, `plant_flowers` and `paint_fence` five pictures each and built 54, the pass stratified by angle added 13, and five more were forced for the wash line and the fishing: 72 probes. Every picture was looked at before the screen. All 93 records rebuild identical to the pixel, and the library passes the validator in full, 382 of 382.

The planner's difficulty priors are the calibration measured on the v0.45 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.44. With the lost balloon's string ending higher above the hand and, in the garden, above the fence, 26 fields of the calibration moved by 0.002 or more, most of all `lost_balloon`'s inference (s from -1.20 to -1.14, d from 0.146 to 0.185).

## The forty-second blind screen

Twelve fresh readers, who had never seen the key, described every picture of the new set and 72 probe pictures; four separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.44.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) | v0.25 (21 pictures) | v0.26 (21 pictures) | v0.27 (21 pictures) | v0.28 (21 pictures) | v0.29 (21 pictures) | v0.30 (21 pictures) | v0.31 (21 pictures) | v0.32 (21 pictures) | v0.33 (21 pictures) | v0.34 (21 pictures) | v0.35 (21 pictures) | v0.36 (21 pictures) | v0.37 (21 pictures) | v0.38 (21 pictures) | v0.39 (21 pictures) | v0.40 (21 pictures) | v0.41 (21 pictures) | v0.42 (21 pictures) | v0.43 (21 pictures) | v0.44 (21 pictures) | v0.45 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 0.97 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 0.95 | 0.99 | 0.96 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 | 0.98 | 0.95 | 0.95 | 0.88 | 0.98 | 0.99 | 1.00 | 0.96 | 0.96 | 0.99 | 0.96 | 0.97 | 0.97 | 0.98 | 1.00 | 0.99 | 0.96 | 0.94 | 1.00 | 0.97 | 0.98 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 1.00 | 0.94 | 0.71 | 1.00 | 0.95 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.99 | 0.98 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 0.98 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.98 | 0.95 | 0.99 | 0.98 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 | 0 of 286 | 0 of 289 | 0 of 283 | 0 of 284 | 0 of 285 | 0 of 284 | 1 of 286 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 286 | 0 of 287 | 0 of 287 | 0 of 287 | 0 of 290 | 1 of 290 | 0 of 286 | 0 of 281 |
| Oddities per picture, as logged by the scorers | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 | 2.6 | 2.6 | 2.2 | 2.0 | 2.3 | 2.3 | 0.6 | 0.8 | 0.9 | 0.5 | 0.2 | 0.6 | 0.4 | 0.8 | 0.8 | 0.5 | 0.4 | 0.7 | 1.1 | 0.7 | 0.5 |
| Readers' remarks per picture (recounted in v0.26) | 8.8 | 5.4 | 6.4 | 4.8 | 4.7 | 4.8 | 4.9 | 4.4 | 4.3 | 4.4 | 4.4 | 4.4 | 3.9 | 3.9 | 4.4 | 4.0 | 4.0 | 3.9 | 4.2 | 3.9 | 5.6 | 5.9 | 5.3 | 5.8 | 5.1 | 5.2 | 5.2 | 3.5 | 3.3 | 3.2 | 3.1 | 2.9 | 3.1 | 2.8 | 3.4 | 3.1 | 3.0 | 3.2 | 3.0 | 3.1 | 3.3 | 2.6 |

Across all 93 pictures 992 of 1,009 scored items had full marks, and none was misread. Of the 17 under full marks:
- twelve are setting items that two readers left out, ten the clouds and two a tree, all zeros (v0.44 had one);
- two are the thief bird's in one picture, half marks both: "it might be about to steal the sandwich, or just be perched next to it";
- two are the square wheels, the bicycle's "a bit squared/boxy" and "a wheelbarrow parked in front of a square box, or a wheelbarrow with an odd square wheel";
- one is the bird the cat stalks, "standing on the grass", where the key has it pecking.

The set's headline is all items 0.977 (0.991 in v0.44). Its things lost four items to the clouds and the tree, its contradictions two half marks to the square wheels (0.955, from 1.00), its actions and inferences three half marks to the two birds. None of the fall is on a thing v0.45 redrew.

**After the screen.** The gate first failed `dog_reading` at 0.833 on one picture, the tier-4 garden isomorph: "standing on its hind legs with its front paws on an open newspaper that seems to be up in the air", a half mark and a misread. The paper is now drawn 12 px toward the dog and 6 px higher (`templates.READ45`), so the forelegs cross the near page and the paws lie on it, hiding 17 to 18% of it. The three pictures with the reading dog were regenerated, every record still rebuilds identical, and each was read again by a fresh reader and scorer: full marks in all three, "sitting up on its hind legs holding an open newspaper as if reading it". A re-read rolls every item of its picture again: of the 66 items the fix did not touch, 64 scored the same and two went down, the thief bird's in one picture, on nearly the same words as at the first read. That took `bird_steals` from 1.00 to 0.933. The second scores stand, and the first are kept in `vision/v045/first/`.

**What the full marks rest on.** The scorers' notes mark 9 items they credited in full where the free description commits and the unsure section adds another reading (7 in v0.44). Halved, they take no template under the gate.

**Remarks were 2.58 a picture, 240 on 93 pictures**, from 1.88 to 3.50 a reader, the fewest of the forty-two screens.

What this release redrew or ruled, and the thief bird, which it did not work (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.44 | v0.45 | v0.45 meaning items |
|---|---|---|---|
| `ice_cream` | 0.85 (13 items) | 1.00 (14 items) | — |
| `ice_cream_drop` | 1.00 (16 items) | 1.00 (24 items) | 1.00 (6) |
| `photo` | 0.90 (5 items) | 1.00 (5 items) | — |
| `lost_balloon` | 0.94 (9 items) | 1.00 (15 items) | 1.00 (5) |
| `dog_reading` | 1.00 (15 items) | 1.00 (9 items) | 1.00 (6) |
| `paint_fence` | 1.00 (7 items) | 1.00 (9 items) | — |
| `plant_flowers` | 1.00 (3 items) | 1.00 (5 items) | — |
| `picnic` | 1.00 (3 items) | 1.00 (3 items) | — |
| `fly_kite` | 1.00 (3 items) | 1.00 (3 items) | — |
| `blocked_hose` | 1.00 (24 items) | 1.00 (28 items) | 1.00 (7) |
| `goat_grazing` | 1.00 (4 items) | 1.00 (4 items) | — |
| `ducks_swimming` | 1.00 (4 items) | 1.00 (4 items) | — |
| `carry_box` | 1.00 (4 items) | 1.00 (3 items) | — |
| `slide` | 1.00 (3 items) | 1.00 (3 items) | — |
| `bird_steals` | 0.97 (15 items) | 0.93 (15 items) | 0.90 (5) |

`ice_cream`, half as big again in a child's hand, reads 1.00 in fourteen pictures, a lollipop or a sweet in no description. `ice_cream_drop`, its empty cone larger as well, reads 1.00 in six. `photo` reads 1.00 in five, "holding a camera up to his eye, taking a photo, with a red strap hanging from it", binoculars in no description. `lost_balloon` reads 1.00 in five: "has escaped and is floating up into the sky, its string dangling". `dog_reading` reads 1.00 in three after the fix. `paint_fence` reads 1.00 in nine pictures and `plant_flowers` in five, the roller and the trowel named. `picnic` reads 1.00 in three, with "a plate with a slice of watermelon, and beside him a wicker picnic basket with a bottle and a baguette". `fly_kite` reads 1.00 in three, and the reel is "a kite reel" or "a kite spool" in six of the seven pictures with a kite on its string. `blocked_hose` reads 1.00 in seven pictures, `goat_grazing` and `ducks_swimming` in four each, `carry_box` and `slide` in three each. `bird_steals`, not worked, reads 0.933: 1.00 at the first count, and two half marks in one picture's re-read.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 | v0.27 | v0.28 | v0.29 | v0.30 | v0.31 | v0.32 | v0.33 | v0.34 | v0.35 | v0.36 | v0.37 | v0.38 | v0.39 | v0.40 | v0.41 | v0.42 | v0.43 | v0.44 | v0.45 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 | 61 | 59 | 63 | 61 | 64 | 63 | 63 | 63 | 63 | 64 | 63 | 64 | 63 | 64 | 64 | 64 | 64 | 63 | 62 | 63 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 | 3 | 5 | 1 | 3 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 0 |

Every template was screened in at least three pictures (38 in three, 11 in four, 10 in five, 1 in six, 1 in seven, 1 in nine, 1 in thirteen and 1 in fourteen), and all 64 pass, for the first time since v0.41. The first count was 63 and one failure, `dog_reading` at 0.833 with a misread; the table has the count after the fix and the three re-reads. The lowest that pass are `bird_steals` (0.933), `square_wheel` (0.933) and `cat_stalks_bird` (0.958), and every other template reads 1.00. Per angle (`vision/v045/gate_yaw.json`), 21 of the 22 (template, angle) pairs pass: the thief bird in profile reads 0.889 over 9 items in 3 pictures, on the re-read's two half marks, and 1.00 at the three-quarter angle. The gate is a filter, and the pilot with people is the test of difficulty.

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 4 | 0 (0) | 3 | 0.781 | — | 15 | 0.035 | rake, paint fence, birds flying |
| T1_park_s1021 | 4 | 0 (0) | 3 | 0.774 | — | 16 | 0.021 | cat sleeping, kick ball, ice cream |
| T1_street_s031 | 4 | 0 (0) | 2 | 0.781 | — | 14 | 0.046 | photo, read bench |
| T1_playground_s5041 | 5 | 0 (0) | 3 | 0.781 | — | 14 | 0.033 | walk dog, run, drink bench |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.711 | 0.411 | 17 | 0.038 | dog wants walk, jump, sweep, play catch |
| T2_garden_s7118_iso (isomorph of T2_playground_s042) | 8 | 1 (0) | 4 | 0.688 | 0.393 | 17 | 0.039 | sprinkler package, walk dog, cat on fence, paint fence |
| T2_park_s3022 | 8 | 1 (0) | 4 | 0.707 | 0.403 | 21 | 0.028 | kite in tree, plant flowers, dog sleeping, run |
| T2_park_s8109_iso (isomorph of T2_street_s032) | 8 | 1 (0) | 4 | 0.712 | 0.365 | 18 | 0.027 | dog begs, jump, push stroller, walk dog |
| T2_street_s032 | 8 | 1 (0) | 4 | 0.710 | 0.361 | 18 | 0.049 | cat stalks bird, carry box, feed birds, wave |
| T2_playground_s042 | 8 | 1 (0) | 4 | 0.686 | 0.388 | 18 | 0.036 | kite in tree, sandbox, dog playing, wave |
| T3_garden_s5013 | 12 | 2 (1) | 6 | 0.641 | 0.313 | 20 | 0.044 | sprinkler package, square wheel, kick ball, read bench, play catch, dog playing |
| T3_garden_s6102_iso (isomorph of T3_street_s15133) | 12 | 2 (0) | 5 | 0.662 | 0.319 | 22 | 0.042 | cat stalks bird, lost balloon, rake, cat sleeping, jump |
| T3_park_s7023 | 12 | 2 (1) | 5 | 0.664 | 0.297 | 23 | 0.031 | ice cream drop, bucket hat, fly kite, goat grazing, carry bag |
| T3_street_s15133 | 12 | 2 (0) | 5 | 0.662 | 0.319 | 20 | 0.052 | dog begs, ball in tree, bird perched, push stroller, balloon |
| T3_street_s11104_iso (isomorph of T3_park_s7023) | 12 | 2 (1) | 5 | 0.664 | 0.303 | 21 | 0.053 | ice cream drop, sweep fork, sweep, water flowers, wave |
| T3_playground_s32043 | 12 | 2 (0) | 4 | 0.655 | 0.338 | 20 | 0.037 | ice cream drop, ball in tree, cat sleeping, bird perched |
| T4_garden_s540013 | 18 | 5 (1) | 9 | 0.568 | 0.215 | 28 | 0.046 | about to trip, ball in tree, cat stalks bird, bird steals, square wheel, dog playing, carry box, rake, jump |
| T4_garden_s24111_iso (isomorph of T4_street_s430752) | 18 | 5 (2) | 9 | 0.577 | 0.228 | 26 | 0.046 | bird steals, ball in tree, about to trip, dog reading, square wheel, cat sleeping, cat on fence, sweep, rake |
| T4_park_s728923 | 18 | 5 (2) | 8 | 0.570 | 0.259 | 33 | 0.037 | ice cream drop, ducks bread, kite in tree, dog reading, pan watering, birds flying, goat grazing, sweep |
| T4_street_s430752 | 18 | 5 (2) | 9 | 0.569 | 0.232 | 26 | 0.058 | bird steals, about to trip, ball in tree, dog reading, square wheel, birds flying, sweep, jump, carry bag |
| T4_playground_s502878 | 18 | 5 (1) | 8 | 0.565 | 0.227 | 26 | 0.040 | bird steals, ice cream drop, kite in tree, cat stalks bird, square wheel, balloon, cat sleeping, dog playing |

Isomorph pairs differ by at most 0.008 in content and 0.006 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,167 | 9 | 1,671 | 10^10.0 |
| garden | 2 | 22,678 | 27 | 9,831 | 10^12.4 |
| garden | 3 | 1,980,031 | 296 | 255,371 | 10^18.5 |
| garden | 4 | 55,032,378 | 565 | 4,320,056 | 10^23.2 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 45,955 | 24 | 19,978 | 10^11.1 |
| park | 3 | 5,569,417 | 236 | 972,951 | 10^17.5 |
| park | 4 | 307,551,136 | 376 | 41,212,001 | 10^23.0 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,298 | 24 | 2,847 | 10^11.7 |
| street | 3 | 386,503 | 220 | 58,895 | 10^17.3 |
| street | 4 | 5,450,566 | 330 | 701,036 | 10^21.6 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.1 |
| playground | 3 | 738,151 | 183 | 110,468 | 10^17.6 |
| playground | 4 | 10,363,379 | 232 | 1,312,634 | 10^20.9 |

In all 387,170,683 structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.

## Key words, frequency and age of acquisition


Unchanged from v0.20: every item record carries its key word's Zipf frequency (f, for things and actions only) and its
age of acquisition (a, from the bundled excerpt of Kuperman, Stadthagen-Gonzalez and Brysbaert, 2012) at weight 0;
`scenegen/norms/aoa_kuperman2012.tsv` keeps the citation and source in its header and every record stores its sha256.
The licence note and what the pilot should test are in the v0.20 README section of the same name (the CC BY-NC-ND 3.0
question about shipping an excerpt; the model with AoA against the model without, pre-registered; AoA kept varying apart
from frequency when choosing the pilot's pictures). Before the pilot, check the bundled rows against the original file
(`python -m scenegen.difficulty --check-aoa <the original .xlsx or .csv>`).

## Folders

| Folder | What it holds |
|---|---|
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts; from v0.31 a pose name with `~near` or `~far` draws a figure in two pieces at its far leg, and from v0.32 `~body` and `~legs` at both legs, for the bench) |
| `assets/blender_run.py` | Lets the `bpy` scripts run with plain `python`, inside an installed Blender where the `bpy` module is missing |
| `assets/validate_assets.py` | Checks for every rendered variant; from v0.32 a piece of a split figure is checked by its base pose, and the manifest schema takes the `~` suffix |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, v0.41 folds the begging dog's forelegs, v0.42 redraws the goat, the dogs, the trousers' waist, the shoes and the woman in yellow's hair, v0.43 lays the reading dog down and redraws the dogs' legs, the goat's horns and beard and the two women's heads, v0.44 sits the reading dog up in reading glasses, redraws the cats' ears, the goat's beard and the dogs' noses, gives props colours of their own and redraws the run, the sand spade, the nozzle's inspection, the call from the seesaw and the content face, and v0.45 enlarges the ice cream, redraws the camera, the shoes' soles, the trowel, the paint roller, the carried box and the kite's reel, turns the hose inspector's head to the viewer and hides the swimming duck's legs |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out045/` | The 18 `.blend` families (builder 0.45.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib045/` | Every variant the generated scenes and probes use, rendered from `out045` (every person and the duck) or carried over from `lib044` (the songbirds, the cats, the dogs and the goat) |
| `assets/cast/gallery045/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (180, all pass the validator) |
| `scenegen/` | The generator (0.45.0, placement revision 43); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.45 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v045.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v045.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v045.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all forty-two screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out045                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out045 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s7023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v045   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v045 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery045 --old-gallery <v0.44 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.45 --single   # the release as one zip, tpdb_v0.45.zip
```

The release is one zip, `tpdb_v0.45.zip`, about 244 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.44 record rebuilds with the v0.44 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- No template falls under the legibility gate after the v0.45 screen, the first release since v0.41 with none. A first count failed one, `dog_reading` (0.83, 3
  pictures), with the screen's one misread: in the tier-4 garden isomorph the dog stood "with its front paws on an open newspaper that seems to be up in the air", the
  paper v0.44's readers twice called "floating", left on the watch list. After the screen the paper was drawn onto the paws, the three pictures with the dog were
  rebuilt and read again by a fresh reader and scorer each, and it read as reading in all three (1.00). v0.44's one failure, `ice_cream`, passes at 1.00 in 14 pictures
  with the cone drawn larger in a child's hand. The lowest are `bird_steals` and `square_wheel` (0.93, 5 pictures each) and `cat_stalks_bird` (0.96, 4 pictures). Of the
  22 (template, angle) pairs placed, 21 pass on their own in two or more pictures: the thief bird in profile is at 0.89 over three, on two half marks from one of the
  re-reads, where nearly the same words had full marks at the first read. Read strictly, the full marks the scorers themselves called hedged take none under the gate
  (`vision/flaws_v045.md`, which lists the oddities for v0.46, first among them the bird at the sandwich).
- A single half mark is noise. 19 pictures were identical to the pixel in v0.29 and v0.30, and 223 of their 230 items scored the same across fresh readers and scorers, with four templates moving by a half mark and no picture changed (`vision/flaws_v030.md`, A retest nobody planned). In v0.31, 12 pictures came back identical once more, and 137 of their 141 items scored the same; the one that went down is the gate's one failure. In v0.32, 19 came back identical, and 242 of their 246 items scored the same; the four that went down are again the gate's one failure, and a begging dog's half mark. In v0.33, 21 came back identical, and 274 of their 281 items scored the same, three moving up and four down. In v0.34, 26 came back identical, and 296 of their 299 items scored the same, two moving up and one down. In v0.35, 78 came back identical, and 806 of their 830 items scored the same, 7 moving up and 17 down, 12 of the 17 the clouds of two readers who named nothing in the sky. In v0.36, 60 came back identical, and 563 of their 576 items scored the same, 12 moving up, every one those clouds, and one down. In v0.37, 75 came back identical, and 775 of their 783 items scored the same, three moving up and five down, one of the five the gate's one failure. In v0.38, 22 came back identical, and 291 of their 294 items scored the same, three moving up and none down. With v0.39's cast redrawn none could; on the 7 pictures with the same seed and events in both screens, each in its own cast, all 75 items scored the same. In v0.40, 28 came back identical, and 326 of their 328 items scored the same, two moving up and none down, both on templates of v0.39's list. In v0.41, 43 came back identical, and 523 of their 532 items scored the same, three moving up and six down, three of the nine the clouds. In v0.42 none could: every person, dog and goat was drawn anew. Nor in v0.43, with both dogs, the goat and the two women redrawn, nor in v0.44, with every dog, cat, goat and person redrawn, nor in v0.45, with every person and the duck redrawn. In v0.45 three pictures were read twice, before and after the reading dog's paper moved: of the 66 items the change did not touch, 64 scored the same and two went down by a half mark, the thief bird's (above). A template with few items can cross the gate on that alone: `read_bench` and `hang_laundry` have one item to a picture.
- What the trip's long box costs a fresh tier-4 search is as v0.29 found it, 166 failed seeds against 80. In v0.32 the garden, park and playground cells came back on their seeds; the street's did not under revision 30, in 39 seeds, and placed at once with v0.31's template set forced. In v0.33 all four came back unchanged, the street's on the same forced set, and in v0.34 to v0.38 all four came back on their seeds again, identical to the pixel in v0.37 and v0.38. With v0.39's redrawn cast the garden and park came back on their seeds and the street on its forced set; the playground's seed and the next 39 placed nothing, and the 41st did. In v0.40 all four placed again on v0.39's seeds and layouts, and in v0.41 all four came back identical to the pixel. With v0.42's redrawn cast the park placed on its seed and layout and the street on its forced set; the garden took three seeds and the playground forty. In v0.43 the park, the playground and the street placed on v0.42's seeds and layouts, and the garden on the fourth seed of its search. In v0.44 the park and the playground placed on v0.43's seeds with the same templates, the street on its forced set with the square wheel for the upward water (which revision 42 keeps out of the street), and the garden on a new seed list after v0.43's seed and 44 more placed nothing. In v0.45 the garden, the park and the street placed on v0.44's seeds with the same templates; so did the playground, until the lost balloon's prior moved after the set was built, and then its seed and the next 14 placed nothing, and the 16th did.
- The oddities come in two rows. Readers' remarks per picture are counted directly from their descriptions and compare across
  screens, with the caveat that current readers write about 18% more than the v0.23 readers on the same pictures (`vision/v024/control/`,
  one reader and eight pictures). The row was recounted in v0.26, as the counter had taken bullets saying nothing is wrong for remarks, so its
  figures differ from those published up to v0.25. The scorers' logged oddities do not compare: v0.23's logged 25% of the remarks, v0.24's 83%, and
  from v0.25 the prompt caps them at three per picture. Earlier screens did not record which model read them; v0.24's to v0.45's ran on Claude Opus 5.5. Readers differ widely: on v0.28's nine, from 4.25 to 6.38 remarks a picture, on v0.29's from 4.50 to 5.75, and on v0.30's from 4.50 to 6.12. v0.31's nine wrote from 2.62 to 4.43, every one fewer than the fewest of v0.30's, and on 12 pictures identical in both screens remarks fell from 65 to 45. So a screen's readers can move the row by a third, and its fall to 3.51 in v0.31 says nothing about the drawings. v0.32's nine wrote from 2.71 to 4.43, 3.28 a picture, and on 19 pictures identical in both screens remarks fell from 79 to 67. v0.33's nine wrote from 2.44 to 4.11, 3.19 a picture, and on 21 identical pictures remarks rose from 77 to 88. v0.34's nine wrote from 2.40 to 4.50, 3.13 a picture, and on 26 identical pictures remarks were 96 in both. v0.35's nine wrote from 2.44 to 3.50, 2.88 a picture, and on 78 identical pictures remarks fell from 243 to 222. v0.36's nine wrote from 2.33 to 3.89, 3.10 a picture, and on 60 identical pictures remarks rose from 163 to 175. v0.37's nine wrote from 1.89 to 4.44, 2.82 a picture, and on 75 identical pictures remarks fell from 226 to 209. v0.38's nine wrote from 2.22 to 4.25, 3.38 a picture, and on 22 identical pictures remarks rose from 73 to 94. v0.39's twelve, eight pictures each, wrote from 2.62 to 4.00, 3.10 a picture, and on 7 pictures of the same events in both screens remarks fell from 28 to 25. v0.40's twelve wrote from 2.62 to 3.62, 3.04 a picture, and on 28 identical pictures remarks fell from 106 to 93. v0.41's twelve wrote from 2.25 to 3.88, 3.17 a picture, and on 43 identical pictures remarks rose from 151 to 156. v0.42's twelve wrote from 2.25 to 4.00, 3.05 a picture over all 93 screened, v0.43's twelve from 2.50 to 4.12, 3.12 a picture over 94, v0.44's eleven from 2.29 to 3.86, 3.27 a picture over 82, and v0.45's twelve from 1.88 to 3.50, 2.58 a picture over 93, the fewest of any screen.
- No reader says "teenager": he is read as a boy, a boy or young man, or a person, which the key mostly accepts. The v0.24 redraw moved him
  from a woman to a boy, and v0.26's cap worn forwards moved him no further toward the key's own word. It read once as "worn backward or sideways" in v0.27.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 93 pictures 992 of 1009 scored items had full marks, twelve of the 17 others the clouds or a tree that two readers left out
  (920 of 927 in v0.44, four of the seven others the girl in pink's ice cream; 977 of 1003 in
  v0.43, ten of the 26 others the clouds of two readers who wrote "sunny" and ten the reading dog's; 1010 of 1020 in v0.42; 999 of 1008 in v0.41, five of the nine others the clouds of one reader; 1011 of 1014 in v0.40, 1025 of 1030 in v0.39, 841 of 842 in v0.38, 870 of 876 in v0.37, 873 of 876 in v0.36, and 855 of 877 in v0.35, 17 of
  whose 22 others were the clouds of two readers who named nothing in the sky). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, a v0.24 scorer eleven, and all three scorers of v0.25 to v0.38 listed such calls, enough to move a template across the gate. A v0.29 scorer listed 18 items that hold full marks because the free description committed and only the unsure section hedged, and a v0.30 scorer gave nothing under full marks in 302 and listed 22 it thought a stricter scorer might halve. Two v0.31 scorers gave nothing under full marks, in 236 and 253 items, among them a bird "about to take it" credited as pecking. v0.32's three gave one, three and three items under full marks, in 244, 288 and 244, v0.33's four, one and three, in 301, 255 and 306, v0.34's one, none and ten, in 314, 282 and 289, where the second listed four inferences a stricter scorer might halve, v0.35's twelve, one and nine, in 304, 283 and 290, v0.36's none, two and one, in 304, 283 and 289, where the first listed eight hedged inferences it credited in full, v0.37's four, one and one, in 304, 283 and 289, where the second listed seven items it credited in full on a committed free description, and two birds seen standing, not pecking, and v0.38's none, none and one, in 298, 268 and 276, where the first listed eleven items it credited in full though the reader gave a second reading, and the second twelve more. Halved, those 23 would take six templates under the gate; 11 of them are on pictures identical to v0.37's, whose scorers had credited all 11 in full (`vision/flaws_v038.md`). v0.39's four (for 96 pictures) gave two, two, none and one, in 282, 246, 269 and 233, where two listed 11 items they credited in full on a committed free description; halved, those would take one template under the gate (`vision/flaws_v039.md`). v0.40's four, and a fifth for one picture read again, gave one, one, one, none and none, in 228, 270, 260, 241 and 15, and listed 21 items they credited in full on a committed free description; halved, those would take five templates under the gate (`vision/flaws_v040.md`). v0.41's four gave one, two, five and one, in 255, 263, 253 and 237, the five the clouds of one reader, and their notes mark 16 items they credited in full on a committed free description; halved, those would take two templates under the gate (`vision/flaws_v041.md`). v0.42's four gave none, three, five and one, in 225, 270, 237 and 250 (scorer a's old picture 10 left out, read again with one of 25 under), and their notes mark 10 items they credited in full on a committed free description; halved, those would take two more templates under the gate (`vision/flaws_v042.md`). v0.43's four gave two, five, twelve and seven, in 231, 284, 262 and 226, and their notes mark seven; halved, those take none under the gate (`vision/flaws_v043.md`). v0.44's four gave one, three, three and none, in 250, 225, 232 and 220, three more one each on three pictures read again after the screen, and their notes mark seven; halved, those take none under the gate (`vision/flaws_v044.md`). v0.45's four gave ten, four, one and two, in 260, 262, 238 and 249, three more none, two and none on three pictures read again after the screen, and their notes mark nine; halved, those take none under the gate (`vision/flaws_v045.md`). A misread is a call too: the
  rake in v0.26's picture 37 could have been marked as sweeping half right.
- Tier-4 pictures are the hardest to place, and revisions 14 to 26 make them harder (walkers' and runners' lanes, pointing
  lines, feet off benches and off other events' things, the photographer's line of sight, the waver's clear hand, body gaps, the gap
  from thin parts, heads clear of figures up to 80 px apart in depth, the ground clear past a reading walker's obstacle, jumpers in the
  front half, an obstacle a full step ahead, runners clear of other movers, ducks off a float, sleepers clear of walkers' feet, nobody in
  the strip before the horizon, a person's box off the lamp post, the ground kept clear round a begging dog). A tier-4 playground plan now holds the bird stealing a sandwich and the
  square wheel, has no swing set as scenery and counts the railing up to 30% hidden, each of which alone placed nothing from 12 seeds, where all three placed 2 (`vision/flaws_v028.md`). So every tier-4 playground has those two, and none
  has the begging dog. A tier-4 street plan holds the bird too, on the evidence of one picture. A picture that also holds a floating, carried or soaked box falls back to the bucket from the long box, and none of the eleven screened pictures of the trip did.
- The square-wheeled bicycle still stands on its own: four stands have been tried on the bench, and each
  read as something else (pedals, legs) or not at all.
- The low kick's direction is ambiguous when the kicker's hair hides the face; the teenager kicks first,
  and the kick read in full in all its screened pictures. His cap now points the way he faces, but two readers still took it for sideways or backwards.
- The stuck girl on the seesaw always calls out, and from v0.33 no kick arcs are drawn at her feet: the tilt, the man's weight, her open mouth and
  the raised handle carry the reading, and in the v0.33 and v0.34 screens she was stuck in all three of her pictures.
- The body check (`assets/cast/gapcheck.py`) finds parts that come apart, not parts that pass through one
  another: a hand inside a hip or a lobe of skirt inside the bell is allowed, and only the outline drawn
  in the render shows whether the join looks right.
- The wind reaches the hat, the washing, an empty swing, the tree and the sky, but not hair or clothes, nor the
  bushes and flowers (three v0.19 probe readers noticed): the cast is posed and rendered in 3D, and a blowing
  fringe or skirt would be a new rig. From revision 32 no can, pan, hose or sprinkler pours in a windy picture, and from revision 33 no pile is
  swept or raked in one (in v0.34 one lay still: "yet the woman's pile of leaves stays neatly in place").
- The isolation bench reads one template cut out of its picture. A visual that reads alone can still be
  misread among other events, so the bench comes before the test scenes and the screen, never instead of them.
- The planner's priors come from the v0.45 calibration, with f = 0 and a at its centre for every inference and contradiction, as in
  v0.20 to v0.44. 26 fields moved by 0.002 or more, most of all `lost_balloon`'s inference (s from -1.20 to -1.14 and d from 0.146 to 0.185, the string's end lifted above the reaching hand and, in the garden, above the fence) (24 in v0.44, most of all `lost_balloon`'s inference, the balloon high on its long string; 42 in v0.43, most of all `dog_reading`'s contradiction, the dog lying down; 34 in v0.42, with the cast redrawn). The ladder's still rests on one sampled placement, since v0.29's lamp rule.
- Exact rebuilds hold within a release, on the pinned Pillow: the v0.45 placement rules (revision 43) end the lost balloon's string 62 to 80 px above the reaching hand,
  in a slow wave with no curl, off a playground's railing and above a garden fence's pickets; begin the wet paint below the roller, the painter close enough for the roller
  to lie on the boards; kneel the planter at the bed's end with a hole under the trowel's point; stand the picnic's loaf and bottle out of the basket beside a plate; keep the
  goat's stake clear of every standing structure; cut a swimming animal at a waterline; draw the slide's ladder as the frame's own end and a tuft of grass at the bird table's
  foot; and lay the reading dog's paper on its paws. Each rule's v0.44 form is kept behind its switch (`BAL45`, `PAINT45`, `PLANT45`, `PICNIC45`, `TETHER45`, `RAIL45`,
  `CURL45`, `WOOD45` and `READ45` in `templates.py`, `library.SWIM45`, `settings.SLIDE45`, `settings.FOOT45`). A v0.44 record rebuilds with the v0.44 package. Revisions 31 to 43 keep their rules in the templates'
  placement and binding, the planner's features and plans, the setting or `fits`, each behind its revision; revision 30's sky rule is still read at import (`RUNBOOK.md`).
- Every variant comes from the v0.45 cast (builder 0.45.0, `out045`), which redraws every person (the shoes' soles, the ice cream, the camera, the hose inspector's head, the trowel, the paint roller, the carried box, the kite's reel) and the duck (its legs out of sight when it swims): the songbirds', the cats', the dogs' and the goat's renders carried over from `lib044`, and the seesaw's riders are in two pieces each, as before. The library keeps only the 382 variants the v0.45 set and probes use. The bench
  variants (`TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ`, `TPDB_BEARD`, `TPDB_BROW`, `TPDB_BLUSH`, `draw.WHEEL27`, `draw.SPLAT28`, `draw.SEESAW_IN28`, `draw.SWING35`, `library.SHADOW28`, `library.SHADOW29`, and `SLEEP29`, `TRIP29`, `TRIP_OBJ29`, `DUCK29`, `DOOR29`, `HOSE29`, `BULGE29`, `FISH29`, `LADDER_LAMP29`, `HOSE30`, `FISH30`, `TRIP_W30`, `TRIP_LANE30`, `CRUMB30`, `SEESAW31`, `RIDE31`, `CASTLE31`, `LIMB31`, `LOW32`, `LOW_IN32`, `LOW_RISE32`, `LOW_RISE_B32`, `STUCK32`, `HANDLE32`, `HOSE33`, `KICK33` and `BASKET38` in `templates.py`, `REEL30` and `REEL31` in `settings.py`, and `TPDB_VEST`, `TPDB_CONE`, `TPDB_BOX`, `TPDB_LOW`, `TPDB_SEAT34`, `TPDB_HAIR34`, `TPDB_MOUSTACHE36`, `TPDB_MOUSTACHE36_FLAT`, `TPDB_BUCKET36`, `TPDB_ISECT39`, `TPDB_SHOE39`, `TPDB_KNEE39`, `TPDB_MID39`, `TPDB_BELT39`, `TPDB_BEN39`, `TPDB_QUAD39`, `TPDB_ART39`, `TPDB_GOAT39`, `TPDB_REACH40`, `TPDB_HOSE40`, `TPDB_GRAZE40`, `TPDB_WALK40`, `TPDB_BEG41`, `TPDB_STALK41`, `TPDB_MEI41`, `TPDB_GOAT42`, `TPDB_DOG42`, `TPDB_BEG42`, `TPDB_CAT42`, `TPDB_MID42`, `TPDB_BELT42`, `TPDB_FOOT42`, `TPDB_MEI42`, `TPDB_DOG43`, `TPDB_GOAT43`, `TPDB_READ43`, `TPDB_ADULT43`, `TPDB_READ44`, `TPDB_CAT44`, `TPDB_GOAT44`, `TPDB_NOSE44`, `TPDB_PROP44`, `TPDB_RUN44`, `TPDB_THROW44`, `TPDB_SPADE44`, `TPDB_INSPECT44`, `TPDB_CALL44`, `TPDB_CONTENT44`, `TPDB_ICE45`, `TPDB_CAM45`, `TPDB_SOLE45`, `TPDB_HOSE45`, `TPDB_TROWEL45`, `TPDB_PAINT45`, `TPDB_BOX45`, `TPDB_KITE45` and `TPDB_DUCK45` in the cast, and `YAW39`, `TUFT40`, `ICE40`, `BOX41`, `SEASON41`, `GOAT42`, `BIRD42`, `KINK42`, `BEG40`, `TRIP43`, `READ43`, `HOSE43`, `CAT43`, `BEGX43`, `TETHER43`, `READ44`, `READ44T`, `LEAD44`, `GOAT44`, `CAT44`, `BAL44`, `BAL45`, `PAINT45`, `PLANT45`, `PICNIC45`, `TETHER45`, `RAIL45`, `CURL45`, `WOOD45` and `READ45` in `templates.py`, `SWIM45` in `library.py`, `SLIDE45` and `FOOT45` in `settings.py` and `HEAP39`, `HEAP40`, `WATER44` and `WHEEL44` in `draw.py`) stay in the code.
- The figures are still narrow. Legs an eighth shorter and limbs 14% thicker took the bench from eight remarks to three, on four cut-outs a side, but the screen's remarks on
  thin or long bodies did not fall (six pictures to eight in v0.27, to thirteen in v0.28 and v0.29, and back to six in v0.30, with nothing changed, and one each in v0.31 and v0.32, with readers who remark less; by keyword, so that row says little). A real change of build is a larger job than these.
- A person in full profile has the head turned 35 degrees to the viewer, baked as a twin action of the pose (`__p`), except where a hand-held thing at the face would be left behind
  (`PROFILE_SKIP`). Those poses keep the hidden face readers remark on.
- Age of acquisition is recorded at weight 0, so it moves nothing until the pilot's pre-registered test says it
  should. The bundled ratings are a verbatim excerpt of Kuperman et al. (2012) under CC BY-NC-ND 3.0, taken from a
  copy in the lftk package; they have not yet been checked against the original file at crr.ugent.be.
- Key words follow one rule (the word the first accepted answer names: an action's verb, or the thing that names
  it), applied by hand in v0.20 and unchanged since; a key that is itself an accepted answer was left alone.
- The sleeping cat, 1.4 times its v0.17 size, read as "small" in one v0.18 probe and drew no remark in its four
  v0.19 pictures; drawn larger, the standing and stalking cats would come out as big as the small white dog.
- Twenty-seven actions in the cast are used by no template; they are kept for later templates and left
  out of the gallery and the screen, so they have never been read blind.
- Edge density is not part of the isomorph rule. Street pictures stay the busiest, so a street
  isomorph of a park or playground picture carries more visual detail at the same object count.
- The top third of park and playground pictures is still mostly sky.
- A filler closer than 24 px to the picture's side edge is now moved 30 px inside it, and no reader said one
  was cut off; the sun can still sit partly off the top edge, where the backdrop draws it.
- The strip before the horizon leaves the playground less room: the tier-3 playground placed only without template-variety steering in
  v0.24 and v0.25, and with it from v0.26. The v0.44 isomorphs were new, the second of tier 2 a park drawn from the tier-2 street, as the park's own drifted in inference and the garden's dog by the door has no isomorph outside gardens. v0.45's pair the same five cells, the tier-2 park and the tier-4 garden on v0.44's seeds with v0.44's templates and the other three on new seeds; the tier-3 playground itself placed in v0.43 to v0.45 only on a fresh seed list without template-variety steering, after the showcase pass and its search failed 13 base seeds; an animal whose template its partner shares is drawn at the
  partner's angle (revision 37), a constraint `calibrate.py` has not yet tested for difficulty.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- A shadow from the figure's own footprint is smaller, and a body lying down has little of it showing. The sleeping dog now reads in full on its new pose and that shadow; a wider one did little on the bench, so whether the shadow cost it marks in v0.28 is still not shown.
- The trip reads in full on the long box, in eleven pictures in v0.30 and five each in v0.31 to v0.41. In v0.42 it read in two of three: the third reader, a reading dog beside the walker, saw the box and no trip. From v0.43 the reading dog is kept away from it (revision 41), and it read in all five of its pictures, in v0.44 as well, and in all three in v0.45. In v0.30, five of its readers also said the walker may step round it, which on the same five pictures went from four of five to one of five with nothing changed.
- The man on the seesaw's low end is drawn astride, his far leg behind the plank. The v0.32 bench turned him away, or put both legs behind the plank, and readers of each still doubted his seat (legs out was set aside on looking);
  in the v0.32 screen he drew one remark in three pictures, that "the seesaw plank seems to pass behind or among the old man's legs". He is off the list; in v0.33 his legs over the plank drew a remark once more. The stuck girl holds a handle raised with her,
  and once a reader saw her hover, from the kick arcs under her feet, which v0.33 does not draw.
- A rider on the seesaw is two pictures, the far leg drawn behind the plank as background and the rest of the figure in front. The far leg is in no count, mask or check of the scene's own.
  Until v0.32 the validator failed the 12 pieces on their names; it now checks each by its base pose and leaves the ground rule to the piece with the body.
- The child on the swing is swung out 12 degrees (revision 33), turned in the picture with its seat and ropes, not posed so in the cast. The frame is widened on the
  side away from the path when a child swings, so its legs stay off the path, and an empty seat keeps the frame it had. One v0.35 reader found the ropes not quite
  "directly above the seat", and read the child as swinging.
- The gate's knob is kept 16 px clear of every figure's drawing, hair, hands and props included (revision 35; revision 34's box round the face missed the back of a
  head in profile). The sweeper it was for now stands lower on the path, and was "a boy with short dark hair". A storm pointer's garden has no clothesline
  (revision 35): with the washing off it (revision 34) the empty line was offered as what she pointed at, and the planner had long noted that an empty line reads
  as a bare wire. Her readers still offer the tree or the roof as a second reading. From revision 36 no cat walks the fence in her picture (one storm pointer was offered
  the cat on the fence in three screens running) and the stalking cat stays on the ground, and in the garden no bird perches up high either; the three v0.38 storm pointers
  read at the clouds. The bird is dropped from the plan in the garden only: dropped in every setting, it changed a playground cell whose picture has neither, as an earlier try of its seed drew the pair.
- The broom's and the rake's heaps have been drawn three ways, and each drew a remark on the season: v0.38's autumn leaves "under green trees" (seven pictures),
  v0.39's summer heap, whose green leaves were "a little odd for raked fallen leaves" (five), and v0.40's dry leaves, leaf-shaped (`draw.HEAP40` "D"), "The brown leaves
  are slightly odd when the trees are green" (five pictures, from three readers). Cut grass read as a dome or dustpan on the bench, and grit as dust or a rock.
  In v0.41, the heap unchanged, no reader remarked on the season in 93 pictures; trees turning over the heap read as fruit on the bench (`vision/isolation_v041.md`).
- Animals are drawn at 45 or 135 as well as 90 for eight templates (revision 37), and the songbirds and the duck at 45 for four more (revision 40); the stalking cat is drawn in profile only from revision 41, its legs tangled at 45 and at 135, and the grazing goat not at 135 from revision 42; people are not. The dog walked on a lead is drawn at 90 only: at 45 its lead
  crossed its back at every spot tried, which revision 12 forbids. Every (template, angle) placed read at 1.00 in two or more pictures in v0.39, and at 0.94 or more in v0.40 to v0.42 and 1.00 in v0.43, the four bird templates at 45 too; in v0.44 all 24 passed, and in v0.45 21 of 22, the thief bird in profile at 0.89 after one of its pictures was read again,
  and the scorers' oddities by angle were about the goat out of place, the begging dog's upright pose in profile and the stalking cat's legs at 45, not about an
  angle as such.
- The begging dog's forelegs are folded from v0.41, the elbows forward and the paws tipped down at the chest: held out level, they were "stiff rods" to the bench's readers
  (`vision/isolation_v041.md`). From v0.42 it sits on its haunches with a shorter trunk, and no screen reader saw it kneel; once it was "jumping up". Nobody else with an
  ice cream comes near it (revision 40), and in both v0.42 pictures with another eater in view the reader gave the one on the bench. From v0.43 its mouth is closed;
  a head lowered to look at the eater rather than the sky did not place at 45, where the gaze check found it facing the viewer (`vision/isolation_v043.md`).
- The goat is tethered when it grazes, a rope from its collar to a peg (revision 40): out of place twice in v0.42, both softened ("a little unusual, but it is tethered
  and calm"), where it was seven times in v0.41. From v0.43 its rope is slack and it is never drawn untethered or on the stopped hose; unusual in four of six
  pictures, and twice, from behind, possibly a sheep. From v0.44 it grazes in the park only: tethered in all four pictures, "a little unusual" in all four, never a sheep. In v0.45, its stake clear of every standing structure (revision 43), it is tethered in all four pictures again and "unusual" in two. The reading dog sat with its hind legs folded
  in v0.42, and its paper "stands upright on its own" in three descriptions; v0.43 laid it down over the paper, which read as lying on it; v0.44 sits it up again in
  reading glasses, its paper hung from its raised paws and tilted, and it read as reading in all five of its pictures, its paper twice "floating" beside it. In v0.45, the paper as it was, it failed the gate's first count on a paper "up in the air" in one picture of three; with the paper drawn onto the paws after the screen it read as reading in all three, and two of the three readers offered beside it that the dog might only be holding the paper ("could simply be holding/carrying the paper").
- A reader can describe the wrong picture. v0.40's reader 7 described picture 56 under picture 55's name, and wrote of picture 56 that it "couldn't find any difference between this
  picture and pic_55"; the files were distinct and right. Picture 55 was read again by a fresh reader and scored by a fresh scorer, and reader 7's description is kept aside
  (`vision/flaws_v040.md`). A scorer who finds a description that does not fit its key, as this one did, is the check.
- The washing's hanger is read hanging it out from the basket at her feet and the drops, not from the pose: on the bench, with neither, three readers of three could
  not tell up from down, and some design-test readers still said the pose alone could go either way (none of v0.38's three did, and of v0.39's five, one raised taking it down and settled it on the drips and the basket). All the washing drips, the jeans and the sleeve over the basket's rim too: with
  the shirt alone wet, a design test read the basket's clothes as dry and "about to get wet". The washing and a watering can placed 0 of 12 together, with the
  basket or without it.
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
