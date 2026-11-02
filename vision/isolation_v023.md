# The v0.23 isolation bench: the frying pan, the begging dog, the older man's profile and the barrow's leg

v0.23 takes the v0.22 flaws that are about how things look (`flaws_v022.md`) to the bench first, as in v0.12 to v0.22:
the template forced alone into a picture, cut out with little else around it, and read blind by fresh readers with the
isolation prompt given in `isolation_v012.md`. Two rounds, 20 cut-outs (`isolation_v023/round1` and `round2`; `map.json`
in each names the case behind every image), ten readers, none of whom saw two drawings of the same thing. The variants
were built as separate bench casts (`TPDB_PAN`, `TPDB_BEG`, `TPDB_HEAD` in `assets/cast/castlib`, read by
`isolation_bench.py` through `BENCH_CAST` and `BENCH_LIB`); the release cast builds with the chosen ones (builder 0.23.0).
The changes that are about where things go (the reading walker's obstacle a full step ahead, a runner and another mover
not heading at each other, ducks off an angler's float) were read in the whole test scenes that followed
(`design_tests_v023.md`).

## The frying pan

In v0.22 a garden probe's pan, held close in front of the flowers with the hand over its short handle, read as "a grey,
round watering can ... no spout or handle". Four drawings held the pan out from the body by the end of its handle, each
read twice over a flower bed.

| Image | Drawing | What the reader said |
|---|---|---|
| round 1 `iso_04`, `iso_11` | B: the v0.19 pan (its face toward the viewer, a grey inside under a black rim) on a long handle (0.25 of the arm's unit) | "reads more like a frying pan, saucepan or large ladle. One reading is 'watering flowers with a watering can'"; "(a) the sprinkler head of a watering can with a very long spout, or (b) a frying pan or ladle tipped to pour" |
| round 1 `iso_05`, `iso_10` | C: as B, tipped forward to pour | "a ladle or a small frying pan ... could also be a watering wand with a rose (shower) head"; "could be a hose watering wand with a shower head. It could also be read as a frying pan, ladle or saucepan" |
| round 2 `iso_04`, `iso_05` | D: the pan seen from above at a slant and deeper, its grey inside an ellipse above the black side, on a thicker handle about as long as the pan is wide | "It looks like a frying pan or saucepan: a round dark pan with a short side handle, with the water pouring over its edge as if from a pot"; "a round gray vessel that looks like a frying pan or shallow saucepan ... reads as a frying pan or saucepan (round, shallow, gray inside, long straight handle), not a watering can" |
| round 2 `iso_03`, `iso_08` | E: the v0.19 face-on pan on D's handle, held out | "It could be read as the sprinkler head (rose) of a watering can ... a hose spray nozzle ... or even as a frying pan or magnifying glass"; "could be a watering can seen from the front ... also reads as a saucepan, frying pan or large ladle" |

A pan seen face-on on a long handle reads as a watering can's rose on its spout, or a wand; seen at a slant with its
depth showing, as a pan. D led both its readings as a frying pan or saucepan, the watering can only a second reading in
one. D is the v0.23 pan (builder 0.23.0).

## The begging dog

The v0.9 beg (sitting, the body sloping down to the tail laid out on the ground, the front paws down) read in v0.22 as
"perhaps hoping for some ... or just walking by", and "sitting up begging with a paw raised, but its back legs and tail
stretch out as if it were half-lying".

| Image | Drawing | What the reader said |
|---|---|---|
| round 1 `iso_01`, `iso_06` | A: sitting up on the haunches, both front paws lifted and folded at the chest, the head tipped up to the food | "sits up on its back legs with its front paws raised. It is looking up at the man, as if it is begging for the ice cream", though "its back leg sticks out flat in front of it"; "as if watching or begging for the ice cream ... a dog sitting up on its haunches to beg, with its front paws raised" |
| round 2 `iso_06`, `iso_07` | A2: as A, the hind legs folded under the haunches | "sits up on its hind legs with one white front paw raised toward him, looking up at the ice cream as if begging"; "apparently begging for the ice cream", but "its lower body stretches long and flat ... like a kangaroo ... or a dog half-lying" |

All four read begging, against one hedged reading of the v0.9 pose in the v0.22 screen. What still looked stretched out
was the tail laid along the ground behind the haunch; the v0.23 beg (A3) keeps A2 and curls the tail tight round the
near haunch. That last change was read in the whole test scenes, not on the bench.

## The older man in profile

His grey ring of hair, seen in profile behind the ear, read in v0.22 as "a beard" or "a face mask", so that he seemed to
face the other way (in the tier-4 park, toward a sleeping cat on the path behind him).

| Image | Drawing | What the reader said (the way he was walking) |
|---|---|---|
| round 1 `iso_02`, `iso_08` | A: the grey kept to a narrower crescent at the back of the head | Walking left: "It is unclear which way he faces ... Either he wears the cap backwards and faces right, or the cap and face point in opposite directions" (the grey patch "could be glasses or goggles, or a face mask"); "walks to the left ... he has grey hair at the back of his head" |
| round 1 `iso_09`, `iso_12` | B: as A, with a fuller nose standing out from the face | Walking right: "walks to the right ... with gray hair showing under a blue-gray flat cap"; "My best reading is a profile facing right: nose at right, ear in the middle and gray hair at the back" |

B read the right way both times, A once. B is the v0.23 older man (builder 0.23.0).

## The barrow's leg

The garden's wheelbarrow stood on a thick dark leg with a foot running forward from its bottom, which two v0.22 readers
saw as "a small dark boot".

| Image | Drawing | What the reader said |
|---|---|---|
| round 1 `iso_03`, `iso_07` | A thin slate strut with a small flat foot centred under it | "one dark grey support leg with a small foot ... looks a bit like a boot or a person's lower leg. It reads mostly as a wheelbarrow stand"; "a dark metal frame and support leg" |
| round 2 `iso_01`, `iso_02` | The strut alone, no foot | "a short gray support leg under the tray ... It reads clearly as a wheelbarrow"; "a dark gray leg/stand near the back of the tray" |

The strut with no foot is the v0.23 leg (`draw.LEG23 = "strut"`).
