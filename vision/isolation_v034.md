# v0.34 isolation bench

Each visual was forced into a picture with little else and cut out, then read blind by fresh readers (the method of `isolation_v023.md`). One round: twelve readers and 12 cut-outs, one to a reader, as all twelve are the one thing drawn four ways (`isolation_v034/round1`; `map.json` says which cut-out is which case). The drawings are switches in the cast, `TPDB_SEAT34` and `TPDB_HAIR34` in `assets/cast/castlib/people.py` and `assets/cast/build_cast.py`, each bench cast built with its own (`tpdb_work/bench34a.sh`).

## The woman in yellow, seated reading (`TPDB_SEAT34`, `TPDB_HAIR34`)

`read_bench`, v0.33's one failure: the woman in the yellow dress, seated with a book, was "a child with short dark hair, in a yellow top, yellow shorts and red shoes" (v0.33, picture 39). Seated, her dress is drawn as two lobes, one round each thigh, and the bell between them hangs from the hips; with the thighs forward, the two lobes and the gap between them look like shorts. Her hair is a bob. Each case's three cut-outs are a garden, a park and a street, with her forced as the reader.

| Case | Drawn | What the readers said |
|---|---|---|
| `seaO_1` to `_3` | **O**: v0.33 | "A child or young person with short dark hair" (`_1`); "A boy with short dark hair, wearing a yellow short-sleeved top, yellow shorts and red shoes" (`_2`); "A person with short dark hair" (`_3`) |
| `seaP_1` to `_3` | **P**: one flat ellipsoid over both thighs, the dress across the lap to the knees, seated only | No better: "A person with short dark hair" (`_1`); "They wear a yellow short-sleeved top, yellow shorts and red shoes ... the short hair suggests a boy" (`_2`); "The large head and simple outfit suggest a boy or child" (`_3`) |
| `seaH_1` to `_3` | **H**: long hair, tied back | All three a woman or a girl: "A girl with dark hair tied back in a ponytail, wearing a yellow short-sleeved dress" (`_1`); "A girl or young woman with dark hair tied back in a ponytail" (`_2`); "A woman with black hair tied back ... She wears a short-sleeved yellow dress with a belt" (`_3`) |
| `seaB_1` to `_3` | **B**: H and P | As H: "A girl or young woman with dark hair in a ponytail ... She wears a short-sleeved yellow dress with a belt" (`_1`); "A girl or young woman" (`_2`); "A girl or woman with dark hair tied back" (`_3`) |

**Chosen: H.** The hair, not the dress, was what the readers went by: with long hair all six readings of H and B were a girl or a woman, where the bob had her "a child", "a boy" or "a person", and the dress across the lap changed nothing ("yellow shorts" twice). P adds an object to every seated dress-wearer and buys nothing, so it stays a switch, off. Her long hair is drawn in every pose, so all her variants re-render: the library's on demand, the gallery's 25 at once.

The first P was rungs from one thigh to the other, overlapping; looked at before any reader saw it, they drew seams, a stack of yellow rolls on her knees, and one flat ellipsoid took their place.

## No drawing

**The wind, asked for exactly.** Revision 31 kept a hose from spraying in the wind by asking whether any other template in the picture claimed the `wind` tag. The wind template claims it, and so do the kite, a thing stuck in a tree's canopy, the storm pointer and the floating box, which claim it only to keep away from the wind: so revision 31 also kept the hose out of pictures with no wind drawn. Revision 32 asks for the wind template itself (`templates.WIND32`, `_windy`), and keeps a can, a pan and a sprinkler out of the wind as well ("Despite the strong wind, the water from the pan falls fairly straight", v0.33, picture 18). Revision 31's test is kept as it was, so v0.33's records rebuild: six of them, the windy garden, the pan in the wind and both storm pointers by the washing among them, rebuilt identical under v0.34's code.

**The storm pointer and the washing.** "She could be pointing at the storm clouds, or at the washing on the line (or both); her finger points up and to the right, roughly between the two" (v0.33, picture 36, and once more in 60). The washing on the line is part of the setting, not a scored thing, so revision 6's check of the line to the clouds passed it. Revision 32 checks it as it checks a scored thing.

**The roller.** The painted patch is "very neat and rectangular, with sharp edges, even though the painter's roller is only at its top-left corner" (v0.33, picture 71). The painting pose holds the roller overhead, so its place on the patch is the pose's; left as a note.
