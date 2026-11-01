# The v0.13 isolation bench: each weak visual refined on its own

The v0.12 screen left one template under the gate (`blocked_hose`), three inferences that lost a half point
once each, and ten unintended oddities (`flaws_v012.md`). As in v0.12, each weak visual was first built on
its own, refined, and read blind on its own before it went back into the library and the scenes. The bench
(`isolation_bench.py`, run from the package root) forces one template alone into a picture (no other
events) and crops around that template's own drawing. Fresh readers who never saw the code or the intent
described each crop with the isolation prompt (the one given in `isolation_v012.md`), at most two unrelated
crops each. The crops and descriptions are in `isolation_v013/round1` to `round5`; `map.json` in each round
names the bench case behind each crop.

## Round 1: the first v0.13 drawings (14 crops)

| Crop | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_01`, `iso_03`, `iso_05` (blocked hose, three gardens) | The hose pinched under the animal's back paw: a fat lens-shaped bulge behind the paw, a flat band under it, a thin hose on to the nozzle | The bulge "could be a puddle, a hose connector or bulge, or a second shadow"; "a dark blue lens-shaped blob ... a bulge or kink in the hose, a hose connector, or a small puddle"; once "the dog is standing on the hose and pinching it, so the hose bulges" as the first of two readings. The hose rising to the hands "in a perfectly straight, stiff vertical line, more like a pole" (twice) | The swelling redrawn as part of the hose, growing toward the paw; the hose draped from the hand in a curve |
| `iso_02`, `iso_12` (sleeping cat, street and garden) | Curled up asleep, turned 45 degrees (face-on the curled cat was too small for the size rule) | "Stretched out on its belly with its back legs extended behind it ... could look collapsed, injured or dead"; "collapsed, exhausted or hurt" | A new cat pose (below) |
| `iso_06` (sleeping dog, street) | Curled up asleep, face-on | "Curled up in a compact ball with its head down. Its eyes look closed ... sleeping or resting" | None needed |
| `iso_07`, `iso_09` (stalking cat, park and playground) | A paw lifted mid-step, hind legs bunched | "Crouched low ... It looks like it is stalking or creeping up on the bird"; "as if it is stalking or about to pounce on the bird" | None needed (the pecking bird "could also read as ... tipping", see below) |
| `iso_04`, `iso_11` (kite in a tree, park and garden) | Sprays of small leaves over the kite's corners | "Caught in the canopy, partly covered by dark leafy tufts", but the tufts "look like spiky scribbles or starbursts ... splats or explosions"; "a different, scratchier style ... stuck-on decorations" | Redrawn in rounds 2 to 4 |
| `iso_13` (floating box, garden) | The box high above the fence, no ground shadow | "Flying or falling ... or it could be resting at a tilt on top of the hedge. Its lower edge overlaps the top outline of the bushes" | In the garden the box hangs clear above the row of trees beyond the fence |
| `iso_08` (pram, park) | The shorter handle | Pushing "a baby stroller with both hands on its handle" (no complaint about the handle) | None needed |
| `iso_10` (square-wheeled bicycle, street) | The heavier stand | "Both wheels are square ... clearly strange"; the bar to the ground "could be a kickstand" | None needed |
| `iso_14` (sandbox, playground) | The child kept inside the sand | "Kneeling in a wooden-framed sandbox ... a tan sandcastle" | None needed |

**The sleeping cat.** The cat's trunk is one long bone, so any lying pose seen from the side is long and
flat. The new pose `sleep_tuck` (cats only) shortens and rounds the trunk (the spine bone scaled to 0.55 of
its length and 1.25 of its width; the neck and front legs keep their size), tucks the legs under, bows the
head down onto the front paws and turns it to the viewer, and lays the tail along the side. It was first
drawn at 60 degrees; the asset schema allows only 0, 45, 90, 135 and 180, so it went into the set at 45
(round 5), still above the size rule. Two blind checks of the pose sheet came first: with the
chest raised the cream bib showed above the back like a second ear, and with the head pitched further
down the white muzzle and nose looked like an open eye, so the chest was lowered and the head pitched
less. Wrapping the tail round the front was tried four ways; on so short a body it stayed hidden. The
dogs keep the face-on curl (`sleep_ball`), which read well.

**The pecking bird.** Two readers offered "tipping or falling over" as a second reading of the songbird
pecking beside the stalking cat. Two flatter tilts were tried; both hid the beak under the head, so the
peck was left as it was (no v0.12 reader misread it).

## Round 2: the follow-ups (10 crops)

| Crop | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_02`, `iso_06`, `iso_10` (sleeping cat, street, garden, park) | `sleep_tuck` | "Lies curled ... Its eyes are drawn as closed curved lines, so it seems to be asleep or resting ... Nothing clearly shows distress"; "asleep or resting"; in the park, "sleeping or resting", but "could also be read as ... hurt, unconscious, or dead, because nothing (such as 'Zzz' marks or a curled-up pose) clearly signals sleep" | In the scenes the sleeping cat is the orange one (below) |
| `iso_04`, `iso_09` (floating box, garden) | Clear above the trees beyond the fence | "Hangs in mid-air against a light blue sky"; "hangs in mid-air ... It is also possible that it is simply floating"; no hedge | None needed |
| `iso_01`, `iso_05`, `iso_08` (blocked hose) | The hose swelling toward the paw, draped from the hand | "Reads as the dog pinching the hose and blocking the water" (the goat garden); elsewhere the swelling "widens into a cone shape, like a nozzle ... a connector or a second nozzle"; and the hose draped toward the animal: "the dog stands inside the loop of hose" | The swelling made a long egg ending against the paw; the drape bowed back toward the holder |
| `iso_03`, `iso_07` (kite in a tree) | The kite hung from the side of the crown, its top behind the leaves | "It could be flying just beside or behind the tree, or it could be caught in the tree"; "the kite seems to be farther away than the tree ... You could also read it as the kite caught" | Back inside the crown (round 3) |

## Round 3: the kite in the crown, the egg-shaped swelling (5 crops)

| Crop | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_01`, `iso_04` (kite in a tree) | The kite back in the crown, the clumps over its corners drawn in the crown's own green with an outline only where they cross the kite | "Looks caught in the tree", but the kite "is not a clean diamond. It is a lopsided four-sided shape with a notch"; "a broken spar or a torn sail" | Leaf clusters of a lighter green with a thin darker edge, over the kite's corners and spread over the crown |
| `iso_02`, `iso_03`, `iso_05` (blocked hose) | The egg-shaped swelling, the drape bowed toward the holder | "Peering at the nozzle to see why it isn't spraying ... It might be standing on the hose and blocking the water, which would explain the bulge and the drip"; "a swelling of water backed up behind a blockage (because the dog is standing on the hose and pinching it ...)" first; once "a connector or coupling, a second nozzle" | The swelling's end run in under the paw, so the paw stands on it; a seam where the swelling joined the hose removed |

## Round 4: the leaf clusters, the paw on the swelling (5 crops)

| Crop | What was being tested | What the reader said |
|---|---|---|
| `iso_02`, `iso_03` (kite in a tree) | Leaf clusters over the kite and on the crown | "Clumps of leaves are drawn on top of the kite and its stick pokes into the foliage, which suggests it is caught in the tree"; "most likely stuck in the tree (leaf clumps drawn on top of it, slack string)". No pasted clumps, no scribbles |
| `iso_01`, `iso_04`, `iso_05` (blocked hose) | The paw on the swelling's end | "The swollen section next to the dog together with the single drip reads as the dog standing on the hose and blocking the water, with pressure building up behind it"; "the dog could be standing on the hose, blocking the water so pressure builds up"; "one reading is that the dog is pinching the hose and stopping the water" |

In every hose crop the intended reading now comes first (in round 1 it came first once in three, after a
puddle and a connector); the readers still hedge on whether the paw is on the hose. The kite reads as caught
among the leaves without the pasted look. Two remarks were left: the kite's string meets it near its tail,
so the two lines are hard to tell apart close to the kite, and the hose holder's face is hard to read at
this size.

## Round 5: the sleeping cat at 45 degrees (2 crops)

| Crop | What was being tested | What the reader said |
|---|---|---|
| `iso_01`, `iso_02` (sleeping cat, garden and street) | `sleep_tuck` turned 45 degrees, the angle the asset schema allows | "Its eyes appear closed and its head is tilted down, so it looks like it is sleeping or resting"; "curled up on a beige tiled floor ... it looks like it is sleeping or resting ... closed eyes and a curled pose look most like sleep" |

## What went back into the library

| Visual | v0.12 | v0.13 |
|---|---|---|
| `blocked_hose` | A pinched hose of even thickness, rising straight to the hand | Full and round from the reel, swelling into a long egg that runs in under the back paw, flat under the paw, thin and slack beyond, draped from the hand in a curve |
| `cat_sleeping` | Lying stretched out flat, seen from the side (`sleep_curl`) | Curled up with a short round trunk, head bowed on the paws and turned to the viewer, turned 45 degrees (`sleep_tuck`); the orange cat, whose closed eyes show |
| `dog_sleeping` | Lying stretched out flat (`sleep`) | Curled up in a ball, face-on (`sleep_ball`) |
| `cat_stalks_bird` | Crawling on four stretched legs (`stalk`) | Frozen mid-step, one front paw lifted, hind legs bunched (`stalk_paw`); a bird pecking on the fence top is keyed there |
| `kite_in_tree` | Round clumps outlined all round over the kite's corners | Leaf clusters, a lighter green with a thin darker edge, over the kite's corners and spread over the crown, all clipped to the crown |
| `floating_box` | A shadow on the lawn far below the raised box; in the garden its lower edge on the treetops beyond the fence | No ground shadow once the box hangs high; in the garden clear above the treetops |
