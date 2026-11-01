# The v0.17 isolation bench: the v0.16 failure and oddities, each refined on its own

v0.17 takes the one template the v0.16 screen failed (`photo`) and the oddities its readers reported (`flaws_v016.md`)
to the bench first, as in v0.12 to v0.16: the template forced alone into a picture (or with the one event it needs),
cut out with little else around it, and read blind by fresh readers with the isolation prompt given in
`isolation_v012.md`, two cut-outs each. Two rounds, 19 cut-outs (`isolation_v017/round1`, `round2`; `map.json` in each
names the case behind every image). Changes that are about where things go rather than how they look (a photographer
only with someone to photograph, birds on the playground railing kept from the slide, a pram's wider lane, feet kept off
benches, fillers inside the frame) were read in the whole test scenes that followed (`design_tests_v017.md`).

## Round 1 (13 cut-outs)

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_04`, `iso_07` (a photographer with someone in front of the lens) | A two-tone camera, a silver top over a black body, one big lens ringed in silver, a flash on top (a small dark box with a grey lens had read as "binoculars or a camera") | "Holding a white-and-dark camera up to his eye ... It reads as a photo camera ... Binoculars are less likely because I see only one lens"; "holding a camera up to her eye, aiming it to the right" | None needed |
| `iso_02`, `iso_11` (the sprinkler and the box it soaks) | The longest arc coming down on the box's lid; no drops above the lid; drips down the box's front, water running off its lid, a puddle at its foot, darker wet patches | "The longest arc reaches a box ... blue streaks running down its front, which look like water dripping off it"; "the box is getting soaked while the flowers are not". No reader saw water coming out of the box. But the two shorter arcs "end in mid-air short of the ground", and the box was "a wooden crate ... a hay/straw bale" | The shorter arcs come down on the grass, a few drops where they land |
| `iso_08`, `iso_09` (a goat grazing) | Larger, darker horns; a pointed beard on the chin | "A white goat ... one dark, curved horn"; but the beard, at its mouth as it grazed, was "a small pale, cone-shaped object ... it looks a bit like an ice cream cone" | The beard back to the small cream one of v0.16; the horns stay |
| `iso_06`, `iso_10` (the white dog reading), `iso_13` (the white dog on a lead) | Floppy brown ears instead of pointed ones (the reading animal "could be a goat (brown pointed shape reads as ear or horn)") | "A white cartoon dog with a brown ear ... holding up a large open folded sheet ... like a person reading a newspaper"; "a white dog with brown spots and a brown ear, which walks ahead of him". No reader saw a goat or a horn | None needed |
| `iso_01`, `iso_12` (a wheelbarrow, and the square-wheeled one) | The handles running back from under the tub, rising gently to the grips (from the tub's rim they stood up "as if tipped") | "A long brown wooden handle runs from the wheel up to the right past the tub"; the square wheel "looks unintentional/odd". No reader saw it tipped; one: the handle "looks laid on top of the tub rather than running underneath it" | The near handle drawn behind the tub |
| `iso_03`, `iso_05` (a bird on the playground railing) | The bird kept clear of the slide, the swing frame, the seesaw and the tree | "A small blue bird with an orange beak and legs sits on the top rail of the fence"; "a red bird is perched on the top rail of the fence near the middle" | None needed |

## Round 2 (6 cut-outs)

| Image | What was being tested | What the reader said |
|---|---|---|
| `iso_03`, `iso_04` (the soaked box) | The shorter arcs landing on the grass | "Two of the arcs fall short and drip onto the grass, one lands on the crate"; "two arcs land in the grass with small droplets. The largest arc reaches a box ... the block looks drenched (puddle, drips down the sides)". The box was still "a hay or straw bale" to one reader, and in the test scenes "a wooden crate, a cardboard box or a picnic basket": the darker wet patches were taken for a texture, so they were dropped, leaving the drips, the run-off and the puddle |
| `iso_05`, `iso_06` (the goat) | The small cream beard back | "A white goat ... with one dark curved horn ... grazing"; no remark on the mouth |
| `iso_01`, `iso_02` (the wheelbarrows) | The near handle behind the tub | "Two brown wooden handles reaching out to the left ... Nobody is using it; it is just sitting there"; the square one "looks strange ... a square wheel" |

## What went into the library and the generator

| Visual | v0.16 | v0.17 |
|---|---|---|
| Camera | A small dark box with a grey lens | Silver top over a black body, one big lens ringed in silver with a dark glass and a glint, a flash on top (builder 0.17.0) |
| Goat | Small light horns | Horns 1.45 times as long, slate grey |
| White dog | Pointed brown ears | Floppy brown ears |
| The soaked box | Drops drawn above the lid | The longest arc landing on the lid, drips down the front, water running off the lid, a puddle; the shorter arcs landing on the grass |
| Wheelbarrow | Handles from the tub's rim | Handles from under the tub, rising gently to the grips |
| Bird on the playground railing | Anywhere along it | Clear of the slide, the swing frame, the seesaw and the tree |
