# v0.43 isolation bench

Each visual was forced into a picture with little else and cut out, then read blind by fresh readers (the method of `isolation_v023.md`). There were two rounds:
- round 1: sixteen readers of 31 cut-outs, two to a reader (one had one) and never two takes of one thing (`isolation_v043/round1`);
- round 2: six readers of 12 cut-outs, two to a reader (`isolation_v043/round2`).

`map.json` in each says which cut-out is which case.

What was drawn is two lists: `flaws_v042.md`'s and Sam's notes on the figures (`figure-fixes-v042.md`, kept in `tpdb_work/`), which ranked nine things by what they cost a reader. Four changes are in the cast, behind switches read when it is built:
- `TPDB_READ43` (the notes' item 2, R2): the reading dog. Its paper "stands upright on its own" in three v0.42 descriptions. **A** lays the dog down like a sphinx with its head bowed and its forepaws on a paper laid open on the ground (a new pose, `down_read`). **B** keeps it sitting, the head bowed and the forepaws lower, on the top of a paper whose foot rests on the ground. The paper is the scene's (`templates.READ43`).
- `TPDB_ADULT43` (item 3, O1 and O2): the two women. **B** makes the head smaller again and the neck longer, the face narrower and taller with smaller eyes set lower and red lips, and puts the woman in yellow's bob back (v0.41's; the bun read as "a dark ponytail"). **C** adds the clothes: the yellow dress to mid-calf, and the woman in purple's hair tied back.
- `TPDB_GOAT43` (item 4): the goat. **B** grazes with the withers raised, the hips a little lower, the hind feet further back and the front knees a little bent; draws each horn as one smooth tapered curve (five stacked pieces, "springs or screws" in the notes); makes the beard larger and grey; and stands with the neck forward at about 35 degrees.
- `TPDB_DOG43` (items 5 and 6): the dogs. **B** makes the legs a tenth shorter and tapered, thick at the shoulder and narrow at the paw, and draws the hind leg's thigh as part of the body, the leg leaving it above the stifle. It adds a brown patch over the spotted dog's near hip, darkens the far legs a step again, and lowers the begging head, the nose up at about 35 degrees.

Six changes are in placement revision 41:
- `templates.TRIP43` **B** (item 1, R1): the reading dog kept out of a zone round the trip's walker and box, and away from anyone reading as they walk; a placement rule, left to the design tests;
- `templates.READ43`: the paper for `TPDB_READ43`'s A and B;
- `templates.HOSE43` **B** (item 4): a dog on the stopped hose, never a goat (in v0.42's picture 30 a goat stood on the hose in a back garden, untethered, "unusual");
- `templates.CAT43` (item 8): the stalking cat at 90 only (**B**) or at 90 and 135 (**C**), not 45;
- `templates.BEGX43` **B** (item 6): the begging dog's mouth closed, its eyes open;
- `templates.TETHER43` **R**, made after round 1: the goat's rope slack (below).

O is v0.42's cast and scene (`BENCH_CAST=assets/cast/out042`, a copy of its library). Round 1's N is the cast with every switch on (DOG43 B, GOAT43 B, READ43 B, ADULT43 B) and NA the same with READ43 A, each built whole into its own library. The first three letters of a case name the thing.

Not drawn:
- **The camera and the planting** (item 7). Both pass the gate and fall only under the strict count, three items each. They have five probes each this time (`probes.py`).
- **The shoes** (item 9), but for the woman in yellow's, made a darker red after round 1. No v0.42 screen description mentioned a shoe.

Before the readers, the bench's own look caught these:
- **The begging head barely moved.** On the upright trunk the head's frame turns with the chest. Pitches of 38, 22 and 12 drew nearly the same nose, and only 0 lowered it to about 35 degrees (`tpdb_work/bench43/look_e1.png`, `look_e2.png`).
- **The woman in purple's ponytail vanished from the front.** Tied back, she looked short-haired, a man's cut (`look_n1.png`). The ponytail went to C, and B kept her long hair.
- **The stalking cat at 135 was as tangled as at 45.** It was still put to one reader beside v0.42's at 45. A third case, set on the fence, was drawn at 90 there and was not read.
- **The begging dog with its head lowered did not place.** Placement went from the first seed to the 28th in one case, and nowhere in 40 in the other (below).

## Round 1

| Thing | O (v0.42) | New | Taken |
|---|---|---|---|
| The reading dog | Holding the paper, "as if reading", three of three; but "kneeling upright on its hind legs like a person" and "holds the paper with both forelegs like a person" | **A**, lying down: reading in three of three, and no person. Each reader also offered sniffing or pawing ("seems to be reading, or at least looking at or sniffing, the book"). The paper was "an open book" three times, once "unclear whether it lies flat on the grass or stands upright and open toward the viewer". **B**, leaning: "balanced on one corner", "the paper falling or being pushed or knocked over", "unclear whether the newspaper is held in the paws or rests on the floor" | A, and round 2 |
| The women | The woman in yellow "a woman or older girl" and "A woman or girl", two of two hedged; the woman in purple a woman in two of two | **B**: the woman in yellow "a woman" in both, unhedged, and the woman in purple in both. Her red shoes once "flat and splayed, almost flipper-like" | B, the shoes darker |
| The dogs (close cut-outs at 45 and 90) | "The front legs are long, straight posts", "thin and stiff like stilts" | **B**: no post, stilt or stiffness in three. The darker far legs once "like grey stockings or stuck-on parts", and the foreleg's patch once "a bandage or wound on the leg" | B |
| The goat grazing (45, 135, 90) | "a raised bump at the rump"; the rope "like a J-shaped hook or walking-stick handle" | **B**: "the front legs look bunched or folded under the chest", "cramped and somewhat unnatural", "a large, rounded, high-backed mass"; the rope "like a rigid wire or stick". The horns and beard drew nothing either way | The horns, the beard and the standing neck (**C**); the graze as v0.42; the rope to round 2 |
| The stalking cat | At 45, legs "bunched and overlapping under its body" | At 135: "Its front and back legs are jumbled together under the body" | **B**, profile only |

**The begging dog** was held back from the readers. Lowered, the head placed on none of 12 street seeds at 45, at pitches of 0, 12 and 22 (`tpdb_work/begp43.sh`), where v0.42's placed on all 12. Wrapping the checks found the gaze refusing every spot: 2772 refusals in four seeds and no pass. At three-quarters a lower head faces the viewer and not the food, as v0.41's leaning beg had done. At 90 the pitches of 12 and 22 placed on 12 of 12, but they hardly lowered the nose. So the head stays v0.42's. The closed mouth went to round 2 on its own, since the "howling" of v0.42's bench came with the tongue out.

## Round 2

The cast with DOG43 B, GOAT43 C, READ43 A and ADULT43 B (`out_N2`), the begging head v0.42's, against v0.42's.
- **The reading dog** was redrawn with the paper larger and slanted as the ground is, and the head higher off the page. The paper became "an open newspaper lying flat on the grass", three of three. But the raised head looked past it: "looks forward, to the right, rather than down at the paper", "past the paper, not clearly down at it". Readers offered pinning down, fetching, or "pawing at or playing with a paper laid on the floor". The head was set between the two rounds' heads and read in the design tests.
- **The goat's rope (TETHER43 R)** was slack, bowed out from the collar, lying on the grass in a loose S and knotted round the peg's foot. It drew no stiffness. "The rope's end loops around its top", once, with no stake, wire or stick. v0.42's on the same seed: "It does not hang or curve the way a slack tether would". At 45 in the park both casts drew the goat untethered: at the picture's foot every peg fell off the edge (`tpdb_work/tether43dbg.py`). Revision 41 now keeps room in front of the goat for the peg, and fails the spot rather than draw a goat with no rope. The case was rebuilt and read.
- **The begging dog** was redrawn with the new legs and the mouth closed, and placed on the same seeds as v0.42's at 90 and 45. At 45 v0.42's spotted dog was "begging" or "happily stretching or sniffing the air". The new one was "as if begging, possibly for the ice cream". At 90 both read as begging.
- **The woman in yellow with darker shoes** was "a woman" in her three pictures of the round, two hers and one beside the begging dog. No reader mentioned her shoes.

## Taken

- Cast (builder 0.43.0): `TPDB_DOG43` B (the legs; the head v0.42's), `TPDB_GOAT43` C, `TPDB_READ43` A, `TPDB_ADULT43` B.
- Revision 41: `TRIP43` B, `READ43` A, `HOSE43` B, `CAT43` B, `BEGX43` B, `TETHER43` R.
