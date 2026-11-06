# v0.36 isolation bench

Each visual was forced into a picture with little else and cut out, then read blind by fresh readers (the method of `isolation_v023.md`). Two rounds, every cut-out to its own reader: round 1, twelve readers and 12 cut-outs, the grandfather under the bucket drawn four ways (`isolation_v036/round1`); round 2, nine readers and 9 cut-outs, the moustache chosen in round 1 against a flatter one, under the bucket and kneeling in profile (`isolation_v036/round2`). `map.json` in each says which cut-out is which case. The drawings are switches in the cast, `TPDB_MOUSTACHE36`, `TPDB_MOUSTACHE36_FLAT` and `TPDB_BUCKET36` in `assets/cast/castlib/people.py` and `actions.py`, each bench cast built with its own (`tpdb_work/bench36a.sh`).

## The grandfather under the bucket (`TPDB_MOUSTACHE36`, `TPDB_BUCKET36`)

`bucket_hat`, v0.35's one failure: the grandfather with a bucket on his head, hands on hips, was "a boy in a white shirt, brown waistcoat and dark trousers" (v0.35, picture 74), and in v0.34 the same picture's reader wrote "I can't see the bucket-wearing man's hair, so I can't tell his age". The bucket covers his white hair and his cap, and his face shows nothing of his age. His spec gives him a moustache, but it has never been drawn: every expression hides each face part it does not name, and it named the moustache nowhere. Each case's three cut-outs are a garden, a park and a street, with him forced as the wearer.

| Case | Drawn | What the readers said |
|---|---|---|
| `bktO_1` to `_3` | **O**: v0.35 | His age not read: "A man stands on green grass" (`_1`); "A man with brown skin" (`_2`); "A cartoon man with brown skin and short dark hair" (`_3`) |
| `bktM_1` to `_3` | **M**: a bold white moustache, drawn where expressions show it | All three older: "An older man with a grey moustache and grey hair at the side of his head" (`_1`); "An older man with a grey moustache" (`_2`); "An older man with a tan complexion and a gray moustache" (`_3`). Two asked what it was: "It could just be part of the moustache, or it could be a pipe, cigar or whistle" (`_2`); "could also be read as something held in his mouth, like a pipe or whistle" (`_3`) |
| `bktR_1` to `_3` | **R**: the bucket sat higher, the white hair at the temples below its rim | Two older: "An older man with grey hair" (`_1`, `_2`). The third: "A cartoon person with brown skin and dark hair" (`_3`) |
| `bktB_1` to `_3` | **B**: M and R | All three older, nothing taken for a pipe: "An older man with brown skin, a grey moustache and grey hair at the sides" (`_1`); "An older man with grey hair and a grey moustache" (`_2`, and alike in `_3`) |

**Chosen in round 1: B.** The moustache said his age in all six readings that had it, where none of the three without it did, and the raised bucket alone said it in two of three. With both, no reader asked about a pipe. But the bold moustache stood off the face, and drawn in his other poses it stood out from his profile like something in his mouth, so it went to a second round, against one lying flatter on the skin.

## Round 2: the moustache in profile (`TPDB_MOUSTACHE36_FLAT`)

| Case | Drawn | What the readers said |
|---|---|---|
| `bktF_1` to `_3` | **F** under the raised bucket: the moustache slimmer and lying on the skin, a little higher | All three: "An older man with grey hair and a grey moustache" (`_1`, `_2`, `_3`); one reader took the grey at his mouth for a moustache "It could also be a smudge or an open mouth" (`_1`) |
| `prfM_1` to `_3` | Round 1's bold moustache, kneeling to plant, in profile | All three older men with a grey moustache. One: "The grey shape under his nose reads as a mustache, but it is small and blocky and could be mistaken for something held in his mouth" (`_3`) |
| `prfF_1` to `_3` | **F**, the same | All three: "An elderly man with grey hair and a grey moustache" (`_1`); "An older man with grey hair and a grey moustache" (`_2`, `_3`), and nothing said of his mouth |

**Chosen: F with the raised bucket.** The flatter moustache said his age in all six of its readings, and nobody took it for something in his mouth; the bold one, in profile, was taken for that once in three, as it had been twice under the bucket. The moustache is his in every pose, so all his variants re-render: the library's on demand, the gallery's eight at once, with the one bucket pose of the gallery.

## No drawing

**The storm pointer and the washing.** "The pointing woman could be pointing at the dark clouds (rain coming) or at the laundry on the line" (v0.35, picture 63), the same seed as v0.34's "to bring it in", with the washing kept out of her cone since revision 32. Revision 34 takes the washing off the line in a storm pointer's picture; the empty line stays, and a picture where someone hangs the washing up has no storm pointer.

**The gate's knob.** "It could be a hair bun, or it could be the gate's knob showing behind his head" (v0.35, picture 73, and in v0.34). Revision 34 keeps the box round every face 16 px clear of the garden gate's knob. The box is drawn round the eyes and mouth, and that picture's sweeper stands in profile, his face turned from the gate: the picture came back identical, and the screen read the knob as a bun a third time (`flaws_v036.md`).
