# The v0.20 isolation bench: the v0.19 failures and oddities, each refined on its own

v0.20 takes the failures and oddities of the v0.19 screen that are about how things look (`flaws_v019.md`) to the bench
first, as in v0.12 to v0.19: the template forced alone into a picture (or with the one event it needs), cut out with
little else around it, and read blind by fresh readers with the isolation prompt given in `isolation_v012.md`, two
cut-outs each. Two rounds, 14 cut-outs (`isolation_v020/round1`, `round2`; `map.json` in each names the case behind every
image). The changes that are about where things go (no bird above or beside a jumper's raised hands, no ice-cream eater
in a picture with the dropped ice cream, the runner kept away from it, no watering can on the lawn beside the pan, the
water's end inside the flower bed, a dug hole clear of the path, a ladder clear of the pond, animals' feet clear of the
sandpit frame) were read in the whole test scenes that followed (`design_tests_v020.md`).

## Round 1 (10 cut-outs)

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_02`, `iso_06`, `iso_09` (the bucket hat: the park's back row, the street, the park) | A silver pail, tapered, with ridges and small side lugs, in place of the blue bucket that read as "a tall blue hat ... or fez" at the back of the garden in v0.19 | "An upside-down silver metal bucket (or pot) with horizontal ribs, worn like a hat"; "like a bucket or pot ... several stacked rims could also read as a stack of metal bowls or pans"; "a silver metal cooking pot or bucket ... ridged bands and small side handles". In the park the pail "sits high on top of the hair" | The cap the hat sat on hidden, so the pail comes down over the head; more taper, one ridge in place of three, no lugs, a dark wire handle behind (builder 0.20.0) |
| `iso_05`, `iso_10`, `iso_08` (a drink: on a park bench at the back, on a garden bench, sitting on air) | A red cup with a white lid and a yellow straw at the mouth, in place of the white cup that read as "something white ... as if drinking or eating" | In the garden, "drinking through a yellow straw from a red cup with a white lid"; on air, the same, and "she is sitting on nothing ... as if her seat is missing" (the contradiction, read as meant); but small at the back of the park, "white with a red top or rim ... I can't tell what she is drinking, or whether she is drinking or just holding it" | The cup a quarter bigger and the straw thicker |
| `iso_01` (the frying pan, with the stream kept inside the bed) | No watering can near the pan, and the water's end inside the flower bed (in two probes it landed "at the front edge of the bed / on the grass") | "Gripping a dark handle attached to a round gray object ... it reads at least as easily as a frying pan or saucepan"; the stream "seems to end in the middle of the bed" | None needed |
| `iso_03` (water from a hose) | The jet ending inside the bed, at whichever of five lengths fits | "Watering a raised oval bed ... curving from the nozzle down into the flowers. It reads as a water stream", the unsure section adding "it could also be read as a second, light-blue hose", "a few separate droplets ... help it read as water" | None needed |
| `iso_04` (the windy garden's empty swing) | The blown seat swung out less, so it stays clear of the frame (swung out 16 degrees it "overlaps (or passes through)" the frame's leg) | "The right end of the seat overlaps the front leg of the right-hand A-frame ... so the seat looks as if it passes through the frame leg" | The ropes no longer swung about the bar: the seat pushed 6 pixels downwind and tilted 10 degrees, each rope to its end of the seat |
| `iso_07` (the garden's wheelbarrow) | Redrawn standing on its wheel and a leg, the tub raised, the handles sloping up (in three v0.19 probes it lay "very flat on the grass with no visible legs, looks tipped or squashed") | "A gray metal wheelbarrow seen from the side ... one dark wheel at the front ... a single dark leg/stand under the back of the tray ... standing empty and at rest. Nothing looks like it is floating" | None needed |

## Round 2 (4 cut-outs)

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_03`, `iso_02` (the bucket hat: the park's back row, the garden) | The pail down over the head, one ridge, no lugs | "A large silver-grey metal bucket (pail) upside down on their head like a hat"; "an upside-down silver metal bucket on her head, worn like a hat ... the small dark dot near the rim looks like where a handle attaches". No reader said pot, bowls or fez | None needed |
| `iso_01` (a drink on a park bench at the back) | The bigger cup and thicker straw | "Holding a red-and-white cup up to her mouth, drinking from it through a straw", the unsure section adding "it could also be an ice-cream cup ... It is too small to tell for sure" | None needed |
| `iso_04` (the windy garden's empty swing) | The seat pushed and tilted inside the frame | No overlap: "the swing frame legs ... appear to be in front of [the fence], which looks fine". "The swing seat is tilted ... and the two ropes are not parallel. This could read as the swing being in motion/twisted, or as a drawing error" | None on the bench; read in the windy test scene, beside the blown washing and wind lines |

## What went into the library and the generator

| Visual | v0.19 | v0.20 |
|---|---|---|
| The bucket hat | A blue bucket with a rim, on top of the cap | A tapered silver pail down over the head (the cap hidden), one ridge, a grey rim, a dark wire handle behind (builder 0.20.0) |
| A drink | A white cup | A red cup with a tan sleeve, a white lid and a yellow straw at the mouth, a quarter bigger than the first try (builder 0.20.0) |
| The garden's wheelbarrow | Flat on the grass | Standing on its wheel and a leg, the tub raised, the handles sloping up, a shadow under it |
| The windy garden's swing | The seat and ropes swung 16 degrees about the bar | The seat pushed 6 pixels downwind and tilted 10 degrees, inside the frame |
| Watering | A watering can could lie on the lawn beside the pan; the water could end at the bed's front edge | No watering can in a picture with the pan; the can's or pan's stream, and a hose's jet, end inside the bed (a jet tries five lengths; if none ends in the bed the waterer is placed elsewhere) |
