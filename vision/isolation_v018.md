# The v0.18 isolation bench: the v0.17 failure and oddities, each refined on its own

v0.18 takes the oddities of the v0.17 screen that are about how things look (`flaws_v017.md`) to the bench first, as in
v0.12 to v0.17: the template forced alone into a picture (or with the one event it needs), cut out with little else
around it, and read blind by fresh readers with the isolation prompt given in `isolation_v012.md`, two cut-outs each.
Two rounds, 14 cut-outs (`isolation_v018/round1`, `round2`; `map.json` in each names the case behind every image). The
failure itself (the waver, whose raised hand met the hedge line behind it) and the other changes that are about where
things go (a body gap between figures of different events, the ground behind a catcher, fillers well inside the frame,
a duck's wake kept off figures) were read in the whole test scenes that followed (`design_tests_v018.md`).

## Round 1 (8 cut-outs)

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_07`, `iso_02` (the dark-haired woman catching, in profile) | Her bob's side hair stopping short of the cheek (in profile it had covered the face: "no visible face; head is a round dark shape") | "A tall woman ... both arms stretched forward with her hands open, ready to catch"; "looking up at the ball as if getting ready to catch it". No reader said her face was missing | None needed |
| `iso_05`, `iso_04` (the same woman reading as she walks) | The same hair, her head bent over the book | "Her eyes are on the book, not on the ground"; but in the other, "Her head is mostly dark hair with only a small part of her face visible on the right, so it could be read either as her looking down at the book or as her head turned partly away from the viewer" | The hairline raised and the side hair cut back behind the ear |
| `iso_03`, `iso_08` (a sleeping cat in a whole picture, someone nearby) | The cats drawn 1.2 times larger (in v0.17 a sleeping cat in front was "very small compared with the people") | "A small orange cat curled up asleep on the grass" (both); but "very small ... it could also be read as a fox or a small orange toy", "small for how close it sits to the viewer ... slightly undersized" | The cats larger again, 1.4 times their v0.17 size |
| `iso_06`, `iso_01` (a cat stalking a bird, on the grass and on the fence) | The larger cat beside the bird (in v0.17 the bird was "fairly large compared with the cat") | "Crouched low on green grass in a stalking or about-to-pounce pose"; "creeping toward the left ... It looks like it is stalking"; but "the bird is large compared with the cat, close to half the cat's body length" | The cats larger again (as above) |

## Round 2 (6 cut-outs)

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_01`, `iso_05` (the woman reading as she walks) | The raised hairline, the side hair behind the ear | "She reads an open book ... and she is looking down at it, not where she is going"; in the other, smaller and further back, "No facial features are visible, only a skin-coloured profile edge under dark hair" | Every reading walker's head bent 20 degrees instead of 30, so more of the face shows (read in the test scenes) |
| `iso_06` (the woman catching) | The same hair | "A tall woman in a yellow dress with dark hair and red shoes ... with both arms raised toward the ball, ready to catch it"; "her head is tilted up and back toward the ball" | None needed |
| `iso_04`, `iso_03` (a sleeping cat) | The cats 1.4 times their v0.17 size | "A small orange cat lies curled up asleep on the grass" (both), still "very small" in both | None (below) |
| `iso_02` (a cat stalking a bird) | The same | "Crouched low facing the bird ... It looks like it is stalking the bird or about to pounce"; the bird "fairly large next to the cat (roughly a third of the cat's body length)", where it had been half | None needed |

The sleeping cat read as a sleeping cat in all four cut-outs, but small in all four, at 1.2 and at 1.4 times its v0.17
size. A curled cat 70 px across in front of the picture is about the size of a real one beside people drawn at that
depth; drawn larger still, the standing and stalking cats would come out as big as the small white dog. It stays at 1.4
times, and its size is a note for the pilot (`flaws_v018.md` will say if the screen still reports it).

## What went into the library and the generator

| Visual | v0.17 | v0.18 |
|---|---|---|
| The dark-haired woman's bob | Side hair down over the cheeks to the jaw; hairline at the brow | Side hair only behind the ear, hairline raised, so a profile shows the face (builder 0.18.0) |
| Reading as you walk | Head bent 30 degrees | Head bent 20 degrees (every person) |
| Cats | The black cat at 0.62 of the cat model's size, the orange one at 0.60 | 0.86 and 0.84 (1.4 times) |
