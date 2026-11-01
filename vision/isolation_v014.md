# The v0.14 isolation bench: each weak visual refined on its own

The v0.13 screen left three templates under the gate (`cat_stalks_bird`, `seesaw_heavy`, `wave`), each after one
picture, and nine unintended oddities (`flaws_v013.md`). As in v0.12 and v0.13, each weak visual was first built on
its own, refined, and read blind on its own before it went back into the library and the scenes. The bench
(`isolation_bench.py`, run from the package root) forces one template alone into a picture (no other events) and
crops around that template's own drawing; for the wind it keeps the whole picture, since the question there is
what else in the picture shows the gust. Fresh readers who never saw the code or the intent described each image
with the isolation prompt (the one given in `isolation_v012.md`), two unrelated images each. The images and
descriptions are in `isolation_v014/round1` onward; `map.json` in each round names the bench case behind each image.

## Round 1: the first v0.14 drawings (22 images)

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_01`, `iso_09`, `iso_17` (stalking cat, street, park, playground) | A new stalking crouch: the rump down level with the shoulders, the hind legs folded under it, the tail low | "As if it is running, sneaking or about to pounce ... or it could just be running across the floor"; "running at it or about to pounce ... not clear it is chasing the bird rather than just running past"; "running or chasing ... or slowly stalking" | Read side by side with the v0.13 crouch in round 2 |
| `iso_02`, `iso_10`, `iso_18` (heavy man on the seesaw) | The girl's legs hanging straight down, her face turned to us, one hand on the handle, the other arm reaching out to the man | "One arm stretched up and out ... as if pointing or waving"; "lifts her other arm high ... waving or pointing"; and "the heavier man is on the low end and the light girl is on the high end, which fits a balanced seesaw" | Both hands back on the handle, the legs still hanging, swing arcs by the feet |
| `iso_03`, `iso_11`, `iso_19` (a child waving) | The arm up and out on a wider slant, the hand at the top of the head and clear of it | "Curved motion lines next to her hand suggest she is waving" (all three first), but the arcs "also look like sound-wave symbols", "snapping her fingers or calling out" | One arc on each side of the hand |
| `iso_04`, `iso_12` (square-wheeled bicycle) | Parked at a rack hoop behind it | The wheels "square wheel-holder frames that belong to the rack, with the bike's real wheels missing"; "the wheels sitting inside square boxes"; the hoop's legs "seem to disappear into ... the square wheels" | A narrow hoop between the wheels, its legs clear of them |
| `iso_05`, `iso_13` (ball in a tree) | The ball resting on a branch behind it, leaf clusters over two slivers of its rim (a twig drawn across its lower half first made it a blue cap with a brim, seen before any reader) | "A blue ball ... sits on a branch inside the leafy canopy ... seems to be stuck there"; "stuck up in the tree, resting on a brown branch among the leaf clumps" | None needed |
| `iso_06`, `iso_14` (a kite flying) | The tail streaming downwind in a wave, the string tied at the spars' crossing and drawn over the kite | "The kite string attaches at the kite's bottom point, the same place the tail starts"; "the string and the bow tail both come off the kite's bottom point" | The kite leaned the other way, into the wind, so its lower point and tail are away from the flyer and the string |
| `iso_07`, `iso_15` (dropped ice cream) | A smaller scoop in the same puddle | "A scoop of strawberry ice cream with sprinkles that has fallen and splattered"; "a dropped scoop of pink ice cream"; no remark on its size | None needed |
| `iso_08`, `iso_16`, `iso_22` (walking a dog) | The lead sagging only as far as it can without crossing the dog's back | "The leash runs to the blue collar"; "runs taut to a white dog ... and a blue collar"; "the leash runs to a white dog with brown spots and a blue collar" | None needed |
| `iso_20`, `iso_21` (the wind, whole pictures) | The washing swung out with the gust, wind lines across the open sky | "White wind lines and small leaves blow across the yard, and leaves also blow off the tree ... a towel and a pair of blue jeans, both swinging sideways in the wind"; in the street "white wind lines" in the sky and past the hat | None needed |

## Round 2: the two stalking crouches side by side, and the follow-ups (16 images)

The stalking cat was read side by side: the v0.13 crouch (`stalk_paw`: rump high, a front paw lifted, the hind legs
reaching back) and the round 1 crouch, in the same three scenes, each scene read by a different reader.

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_01`, `iso_05`, `iso_09` (stalking cat, the v0.13 crouch) | Street, garden, park | "Crouched low ... in what looks like a stalking or creeping pose"; "crouched low ... It looks like the cat is stalking the bird"; "crouches low ... seems to be stalking or creeping toward it" (once "or a running or pouncing stride" as a second reading) | The v0.13 crouch stays |
| `iso_03`, `iso_07`, `iso_11` (stalking cat, the round 1 crouch) | The same three scenes | "Either stalking ... or running or leaping at the bird"; "It looks like it is running or creeping toward the bird"; "stalking or creeping toward the bird" | Dropped |
| `iso_02`, `iso_10`, `iso_13` (heavy man on the seesaw) | Both hands on the handle, the legs hanging straight down, the face turned to us, swing arcs by the feet | "Holding a handle. Small motion lines under her feet suggest she is kicking ... impatiently or playfully because she is stuck in the air"; twice "kicking or swinging her legs" with no word of being stuck | Read side by side with the v0.13 pose in round 3 |
| `iso_04`, `iso_12`, `iso_15` (a child waving) | One arc on each side of the hand | "Waving" first in all three; but turned three-quarters the hand still sat by the head and its bun of hair: "holding something like a phone to her ear", "touching or scratching the back of her head" | A waving child faces us |
| `iso_06`, `iso_14` (square-wheeled bicycle) | A narrow hoop between the wheels | "Two square crates or frames standing next to the bike"; the rack "partly looks as if [it] passes through the bicycle" | No rack: the stand drawn in front, light grey against the dark wheel |
| `iso_08`, `iso_16` (a kite flying) | The kite leaned into the wind, its tail and lower point away from the string | No remark on the string and the tail; "the kite tail ends in a thin line past the second bow, which looks a little unfinished" | The bows moved down the tail |

## Round 3: the two seesaw poses side by side, the child facing us, the stand in front (12 images)

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_01`, `iso_05`, `iso_09` (seesaw, the v0.13 pose with the swing arcs) | Bent over the handle, knees bent, the face toward the man | Once "the man's weight is holding his end down, so she is stuck up in the air"; twice not: "the tilt (adult down, child up) matches their weights, so nothing looks physically wrong" | Dropped |
| `iso_03`, `iso_07`, `iso_11` (seesaw, the round 2 pose) | The same three scenes | "The man's end is on the ground and the girl is held up high while he reads" (her look "surprise or worry about being stuck up high"); "his weight holds her end up in the air"; "the man is heavier and focused on his book, so the girl is stuck at the top" | This pose goes into the library (`seesaw_stuck_call`) |
| `iso_02`, `iso_06`, `iso_10` (a child waving, facing us) | The arm up and out to the side, the hand clear of the head, an arc each side | "Curved motion lines around her hand show she is waving"; "waving at someone out of the frame"; "as if waving" (a second reading twice: "raising a hand to get attention or ask a question") | None needed |
| `iso_04`, `iso_12` (square-wheeled bicycle) | The stand in front, light grey | "A gray kickstand angled down to the ground"; "could be a pedal crank arm ... or a kickstand" | The stand starts on the chain stay well behind the crank |
| `iso_08` (a kite flying) | The bows further down the tail | "The kite string runs straight from the centre of the kite to the child's hand"; no remark on the tail | None needed |

## Round 4: the stand behind the crank (2 images)

| Image | What was being tested | What the reader said |
|---|---|---|
| `iso_01`, `iso_02` (square-wheeled bicycle) | The stand from the chain stay, light grey, a broad foot | "A gray bar ... that ends in a flat foot, which looks like a kickstand holding the bike up" (both; "or a crank arm with a pedal" as a second reading) |

## What went back into the library

| Visual | v0.13 | v0.14 |
|---|---|---|
| `seesaw_heavy` | The girl bent over the handle, knees bent, her face (seen at 90 degrees) mostly hair | Legs hanging straight down, toes down, both hands on the handle, her face turned to us (`seesaw_stuck_call`), short swing arcs by her feet |
| `wave` (children) | Turned three-quarters, the hand by the head, two arcs on its outer side | Facing us, the arm up and out on a wider slant, the hand clear of the head, an arc on each side of it (adults keep their three-quarter wave, with the arcs on both sides) |
| `cat_stalks_bird` | The `stalk_paw` crouch | The same crouch (the lower one read as running more often), with the ground round the cat and its bird kept clear of everyone (see `design_tests_v014.md`) |
| `square_wheel` (bicycle) | A dark stand behind the wheel | A light grey stand in front of it, from the chain stay to a broad foot |
| `ball_in_tree` | The ball drawn whole on the crown | Resting on a branch behind it, leaf clusters over slivers of its rim, clusters spread over the crown |
| `fly_kite` | The kite leaning toward the flyer, its tail hanging straight down beside the string | Leaning into the wind, the tail streaming away downwind with the bows along it, the string tied at the spars' crossing and drawn over the kite |
| `ice_cream_drop` | A scoop "about as big as the dog's head" | A smaller scoop in the same puddle |
| `walk_dog` | The lead sagging over the dog's back | The lead sags only as far as it can without crossing the dog's body |
| `windy_hat` | Leaves blown off the tree | The washing on the line swung out downwind and wind lines across the open sky as well |
