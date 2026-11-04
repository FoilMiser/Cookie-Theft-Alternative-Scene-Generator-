# v0.27 isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (the method of `isolation_v023.md`). Round 1 was twelve readers and 34 cut-outs, up to three to a reader, no reader seeing two versions of one thing (`isolation_v027/round1`); round 2 was eight readers and 17 cut-outs (`isolation_v027/round2`). Each `map.json` says which cut-out is which case. The variants are behind `TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ` and `TPDB_BEARD` in the cast; `vision/isolation_bench.py` has the cases.

Looking closely at what the v0.26 readers remarked on, before drawing anything, changed the list. The walkers' feet do point the right way, as the flat shoes only look alike. The hose reaches the fist but vanishes behind the forearm first. And in full profile the eye sits on the head's outline, whichever face it is, which is what the newspaper dog's turned head had shown in v0.26.

## The head in full profile (`TPDB_PROFILE`)

"Face hidden", "hard to read", and in v0.26 seven pictures of it. The bench gives every person in full profile a twin of each pose with the head turned 35 degrees toward the viewer, baked as its own action (a pose set at render time is overwritten when the renderer re-evaluates the action). Poses with a hand-held thing at the face keep their profile, as it would be left behind.

| Case | Drawing | What the readers said |
|---|---|---|
| `proO_1` to `_4`, `trpO_1`, `trpO_2` | Full profile | "The dark mark at her eye could be glasses, sunglasses or just a heavy eye"; "facing away from the viewer or to the left"; "the face is mostly turned away and hidden"; "a dark mark on it could be an eye, glasses, a beard or a mouth" |
| `proB_1` to `_4`, `trpB_1`, `trpB_2` | Turned 35 degrees | "Round glasses"; "looking up"; "his eyes are turned down toward the book" |

**Chosen: turned.** Gaze still reads: readers said where each was looking without a hedge. It showed a new thing, the beard, on `person.dev`: "a dark face covering or mask", and in round 2 "a chin strap, helmet strap or face mask". His beard now stops short of the ear, so hair and beard do not join (`TPDB_BEARD`); that change was not read on the bench and goes to the design tests.

## The stride (`TPDB_FOOT`)

"His head and arms face left", while "his legs and feet look like they stride towards the right" (v0.26, and half marks on the trip in two pictures). The bench lifts the back heel, on its toe.

| Case | Drawing | What the readers said |
|---|---|---|
| `trpO_1`, `trpO_2` | Both feet flat | "Stands or walks"; "standing or walking"; "the box has no visible connection to the person" |
| `trpB_1`, `trpB_2` | The back heel lifted, with the head turned | "Walking across a paved plaza while reading"; "he is about to trip over the box because he is looking at his book"; "something he is about to walk into or trip over" |

**Chosen: the lifted heel.** With both changes together, the trip was offered unprompted in both cut-outs and in neither of the old. The two are not separated here.

## The broom (`TPDB_BROOM`)

The v0.26 fan of bristles: "a long yellow-headed rake", that screen's one misread. Read beside `rake`, as the last release's lesson asks.

| Case | Drawing | What the readers said |
|---|---|---|
| `brmA_1`, `brmA_2` | **A**: the v0.26 fan | "A long-handled broom", "looks small and fan-shaped"; "a long wooden-handled broom" |
| `brmB_1`, `brmB_2`, `brmR_1` | **B**: dense, overlapping bristles, flared | "A long-handled broom or rake with a yellow fanned head", "a broom or a fan rake"; "a long wooden broom"; beside a raker, "a yellow-bristled broom" |
| `brmC_1`, `brmC_2` | **C**: a yard broom, a block across the pole | "Could be a broom or a rake-like tool; the bristles make me read it as a broom"; "it could read as her standing on the broom" |
| `brmD_1`, `brmD_2`, `brmD_3`, `brmR_2` (round 2) | **B2**: dense and nearly parallel, two bindings at the neck | "A long-handled yellow broom"; "a long-handled straw broom"; "a long-handled broom"; beside "a long-handled rake", "a yellow-bristled broom" |

**Chosen: B2.** Four of four said broom, none rake. The flare was what said rake.

## The ice cream (`TPDB_ICE`)

Two half marks in v0.26 on one bearded man, "looking at or eating it".

| Case | Drawing | What the readers said |
|---|---|---|
| `icrO_1`, `icrO_2` | Held up before the face | "Licking or about to bite"; "apparently eating an ice cream". Both stand at 45 degrees, where the old pose was already fine |
| `icrB_1`, `icrB_2` | The scoop at the mouth | "Apparently eating or licking it", but "smelling it like a flower" as it "sits right at his nose and mouth" |
| `icwD_1`, `icwD_2` (round 2) | The scoop lower, at the lips, on the walker the screen half read | "Appears to be about to lick or eat it"; "as if about to lick or eat it" |

**Chosen: at the lips.**

## The hand on the book (`TPDB_BOOK`)

Not on the list. All four first-round cut-outs of the reading walker said the same thing: "the forearm passes straight across the front of the book and the hand sticks out past its right edge as a small rounded lump". Round 2's near hand holds the book's outer corner from under it: "only one hand is clearly visible under the book", and no reader had it past the edge.

## The mouth (`TPDB_MOUTH`)

Also not on the list. "A dark mark around the mouth could be a mouth or a small beard or moustache", "facial hair on someone in a dress": a black line near the edge of the face, in five cut-outs of round 1. Now thinner and in a lip colour. No reader of round 2 took a mouth for a beard, on a small sample.

## Shorter legs (`TPDB_BODY`)

v0.26 tried a fuller body, and the readers' words did not move. This time the legs are an eighth shorter, with the rest of the figure lowered with them, and the limbs 14% thicker.

| Cases | Drawing | What the readers said about the body |
|---|---|---|
| `bodD_1` to `_4` | As they are | "Very tall and thin, with long legs"; "narrow and long-legged"; "his lower legs hang very long and thin", "his torso looks small and narrow compared with his long legs"; "the head looks large for the thin body" |
| `bodE_1` to `_4` | Shorter and thicker | "The legs look long and slightly tube-like"; "his legs are long and thin"; "his torso looks oddly narrow and flat" |

**Chosen: shorter.** Counted by hand, eight remarks on the figure's proportions in the four old cut-outs against three in the four new, though two of those three still call the legs long, and four cut-outs a side is a small sample. Taken because every person was being rendered again for the head anyway, so it costs nothing it would not have cost, and no pose broke. Reaching misses fell (`dig_lift`).

## The smaller things

| Case | Drawing | What the readers said |
|---|---|---|
| `pckO_1` | The pecking bird as it was | "I could not make out a clear eye or beak", "a bird toppling forward", its tail "a party hat or a funnel" |
| `pckB_1`, `pckB_2` | The body less tipped, the head in front of it, an eye on its side | "A yellow beak"; "appear to be pecking at them". One now "looking toward the cat", as the head is less low |
| `drsO_1` | The dress as it was | "A visible break at the waist, with the top and skirt looking like two separate yellow shapes" |
| `drsB_1`, `icrB_2` | A belt at the join | "A yellow dress"; "a thin brown belt". Nothing about the waist |
| `digB_1`, `digB_2` | A lumpy heap with clods | "A mound of brown dirt with a few small clods around it"; "a larger mound of brown soil" (v0.26: "a neat flat-bottomed dome") |
| `pkgB_1`, `pkgB_2` | Two short drips from the lid | "A closed cardboard box with brown flaps and a pale tape strip"; once "box or crate" |
| `hosB_1`, `hosB_2`, `hosD_1` | The hose hanging from the fist, in a slack hook | "The dark teal hose runs along the grass from his hand back to a round hose reel"; "a thick dark teal garden hose runs from the nozzle down past his body". The join still draws a remark: "a short thin stub joined to the thicker hose", then, with the stub thicker, "not quite connected" |

**All chosen.** The spoked bicycle wheels and the duck's shorter wake were not on the bench and go to the design tests.

## Looked at and left

The seesaw's plank "through" its sitter: looked at closely, the near leg does lie over the plank, as it would on a rider astride one. A rider cut in two would be a larger job, and the plank is left. The leaf clumps over a caught kite are already spread over the crown; left.
