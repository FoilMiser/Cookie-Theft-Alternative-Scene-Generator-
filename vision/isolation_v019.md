# The v0.19 isolation bench: the v0.18 failures and oddities, each refined on its own

v0.19 takes the failures and oddities of the v0.18 screen that are about how things look (`flaws_v018.md`) to the bench
first, as in v0.12 to v0.18: the template forced alone into a picture (or with the one event it needs), cut out with
little else around it, and read blind by fresh readers with the isolation prompt given in `isolation_v012.md`, two
cut-outs each. Two rounds, 15 cut-outs (`isolation_v019/round1`, `round2`; `map.json` in each names the case behind every
image). The changes that are about where things go (no reading walker under a gust of wind or at the far back, a gap
between people and the thin parts of standing structures and the stall's legs, the begging dog clear of the eater's
legs) were read in the whole test scenes that followed (`design_tests_v019.md`).

## Round 1 (10 cut-outs)

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_07`, `iso_02` (the frying pan, no hose reel in the picture) | The pan watering the flowers with no hose or reel near it (in v0.18, beside a reel, it read as "a dark grey hose nozzle or watering wand") | "A dark gray, round, bowl-like object on a long straight handle ... (a) a frying pan or saucepan (or a big ladle) ... or (b) only the long spout and round sprinkler head ('rose') of a watering can"; "a rounded dark grey dish on a long straight handle with no visible spout ... (a) a frying pan, saucepan or ladle ... or (b) a watering can or watering wand"; "the handle is very long and thin for its round head" | The pan turned further toward the viewer, a grey inside under a black rim, on a shorter, stouter handle (builder 0.19.0) |
| `iso_01`, `iso_04` (a runner, in the park and in the street) | Three motion lines trailing from the runner's back (in v0.18 a runner read as "striding or jogging") | "Running to the right ... three horizontal speed lines behind her ... show she is moving"; "moving quickly ... Horizontal speed lines behind him show fast motion", though "the upright posture ... could also read as fast walking or hurrying" | None needed |
| `iso_08`, `iso_03` (the stalking cat on the fence) | The cat close to a bird perched on the fence (in v0.18, well over a cat's length from a pecking bird, it read as walking along the fence) | "The cat seems to be stalking or sneaking up on the bird"; "in a low, stretched-out stalking or creeping posture ... A small red bird ... sits on the same fence top a short distance ahead of the cat" | None needed |
| `iso_05` (water from a hose) | The jet drawn as one unbroken ribbon (dashed, it was "a dotted line") and the hose brought up to the hand from in front of the waterer (behind, it ran "very tightly behind/around the old man's legs") | "A curved stream of water sprays down toward an oval bed of brown soil"; but "the hose looks disconnected ... ends in an open, rounded end in the grass, without reaching her hand" | The hose's path fixed to reach the hand (its last point had been dropped) |
| `iso_10` (a sprinkler soaking a box) | The sprinkler's arcs drawn unbroken, outlined, with drops breaking off them (dashed, "a dotted trajectory rather than water") | "The sprinkler throws three arcs of water to the left. The highest arc lands on a small wooden box or crate ... with drops flying off" | None needed |
| `iso_06` (the curly-haired boy in profile) | Curls cut back from the front of his head (in v0.18 his head looked "almost seen from behind while the body is side-on") | "The head is drawn mostly as hair, with only a thin brown strip of face on the left edge, so the child could be looking away from the viewer ... or be seen from behind at an angle" | Below the temples his hair kept behind the ear, as the dark-haired woman's since v0.18 |
| `iso_09` (a kick) | The ball against the toe of the kicking foot (a little ahead of it on the ground, the foot seemed "stretched past/over the ball ... a swing-and-miss") | "She stands on her bent right leg and swings her left leg out to the left so her toe meets the ball" | None needed |

## Round 2 (5 cut-outs)

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_02`, `iso_04` (the frying pan) | The pan turned toward the viewer, grey inside a black rim, on a shorter handle | "It could be read as a frying pan, a saucepan or a pot lid"; "looks more like a frying pan or saucepan (a flat grey disc with a darker rim and a straight side handle) than a watering can". No reader said a spout, a rose or a wand | None needed |
| `iso_03`, `iso_01` (the curly-haired boy) | His hair kept behind the ear below the temples | In profile, "walking to the right ... holds the string of a yellow balloon", with no remark about his face; from the front, he "points straight up ... frowning, worried or annoyed expression, as if his ball got stuck in the tree" | None needed |
| `iso_05` (water from a hose) | The hose's path fixed | "The dark teal hose runs from her hands down in front of her, then along the grass around the front of the flower bed"; but the jet "is a solid, even line, so it could be read as a thin second tube or wire rather than a water stream. The droplets around its end suggest water" | The jet widening as it goes, with drops spraying off both sides of its second half (read in the test scenes) |

## What went into the library and the generator

| Visual | v0.18 | v0.19 |
|---|---|---|
| The frying pan | Seen at a slant, a slate inside, a long thin handle | Turned toward the viewer, a grey inside under a black rim, a shorter, stouter handle (builder 0.19.0) |
| The curly-haired boy | Curls and the hair shell over the side of the head down to the jaw | No curls over the front half below the hairline, and below the temples the hair only behind the ear |
| Reading as you walk | Head bent 20 degrees (every person) | 20 degrees for the dark-haired woman, whose face it shows; 30 again for everyone else, as in v0.17, when every reading walker read in full in six pictures |
| A runner | No marks | Three motion lines trailing from the back at shoulder, waist and hip height |
| Water from a hose | A dashed stream | An unbroken ribbon widening as it goes, a white glint, drops spraying off both sides |
| A sprinkler | Three dashed arcs | Three unbroken, outlined arcs with drops breaking off them |
| A kick | The ball on the ground a little ahead of the toe | The ball against the toe of the kicking foot |
