# The v0.16 isolation bench: the v0.15 failures and oddities, each refined on its own

v0.16 takes the three templates the v0.15 screen failed (`cat_stalks_bird`, `seesaw_heavy`, `bird_perched`) and the
oddities its readers reported (`flaws_v015.md`) to the bench first, as in v0.12 to v0.15: the template forced alone into a
picture, cut out with nothing else around it, and read blind by fresh readers with the isolation prompt given in
`isolation_v012.md`, two cut-outs each. Two rounds, 26 cut-outs (`isolation_v016/round1`, `round2`; `map.json` in each
names the case behind every image). Changes that are about where things go rather than how they look (a second cat on
the stalking cat's fence, a pointing hand beside it, walkers heading into other events) were read in the whole test
scenes that followed (`design_tests_v016.md`).

## Round 1 (21 cut-outs)

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_11`, `iso_19`, `iso_14` (the girl stuck on the seesaw) | Without the motion lines at her feet (in a busy picture her "legs dangling with motion lines" had read as ordinary play) | "The tilt makes sense: the heavier adult's end is down and the child's end is up"; "she seems to be smiling"; "her expression is small and neutral ... happy, bored, or waiting". None of the three saw her stuck | The lines put back. A version with her head turned along the plank to look down at the man was rendered and dropped: turned that way her face was hidden, the back of her head toward us. She now always calls out, the mouth open toward us |
| `iso_08`, `iso_20` (a bird on the garden fence beside the washing line) | Kept off the stretch of fence behind the clothesline | "A red bird perches on top of the fence"; "a blue bird perched on the fence" | None needed |
| `iso_06` (someone at the back of the playground) | The railing drawn 0.85 m tall at its depth (0.4 m before) | No remark on anyone's size: "the woman's smaller size fits her being farther back" | None needed |
| `iso_07` (the dog by the door) | Its head clear of the door knob | "Sits upright in front of the door, holding a red leash in its mouth"; the knob named on the door, not on the dog | None needed |
| `iso_17`, `iso_18` (playing catch) | A lower arc, the ball past its top and coming down to the catcher | "A woman ... with both arms raised forward and hands together, apparently getting ready to catch the ball"; "the child seems to have just thrown it to the woman" | None needed |
| `iso_09`, `iso_10` (the square-wheeled bicycle) | A two-legged centre stand under the crank | "Two pedal arms hanging down ... read as a small stand or kickstand rather than pedals"; "both point downward and outward in an upside-down V ... read either as pedals or as a pair of legs" | Dropped: the bicycle keeps the v0.14 stand. Four stands have now been tried |
| `iso_02`, `iso_04` (a pram) | A sleeping face on the baby | "A baby with closed eyes, apparently asleep" (both) | None needed (the blanket can look "like a flat disc or lid") |
| `iso_12`, `iso_01` (watering from a can, from a pan) | One unbroken stream instead of dashes | The can's water "looks more like a solid bent tube, hose or rod than flowing water"; from the pan it "comes straight out of the side of its rim" | From the can, a shower of drops from the rose; from the pan, a pour from the lip, wide there and thinning as it falls almost straight down |
| `iso_16`, `iso_21` (a star jump) | The whole body lifted, the legs straight and spread (with the hips at standing height the lifted feet had bent the knees into a squat in mid-air) | "Jumping in the air with both arms raised ... an oval grey shadow ... well below her feet, which shows that she is off the ground"; "most likely shows a jump, but it could also look like the person is floating" | None needed |
| `iso_03`, `iso_13` (a low kick) | The head bowed further over the ball | The boy, his face under his curls: "which way the child faces is unclear"; the teenager: "head tilted down toward the ball" | The kick goes to the teenager first |
| `iso_05`, `iso_15` (readers) | The plain, open-eyed face for reading | "Reading a red book that she holds up in front of her chest with her head bent toward it"; no reader saw closed eyes | None needed |

## Round 2 (5 cut-outs)

| Image | What was being tested | What the reader said |
|---|---|---|
| `iso_02` (watering can) | The shower of drops | "Tips it so water pours from the long spout onto a round bed"; "drawn as strings of small light-blue dots ... could also look like a beaded chain" (the drops were then drawn as short streaks, read in the test scenes) |
| `iso_03` (frying pan) | The pour from the lip | "A stream of water pours from it in an arc onto a round bed ... He seems to be watering the flowers"; "the water comes out of the lower edge of the bowl" |
| `iso_04` (the teenager kicking) | The kick with the head bowed | "Her body and face point to the right, but the leg swings out behind her to the left ... a backward kick": the bowed head did not settle the direction either, so the kick keeps its v0.15 pose, which the v0.15 screen read in full in all three of its pictures |
| `iso_01`, `iso_05` (readers) | The open-eyed face | Both read as reading; no closed eyes |

## What went into the library and the generator

| Visual | v0.15 | v0.16 |
|---|---|---|
| Star jump | Feet lifted 0.26 m, knees bent out | The whole body lifted 0.18 m, legs straight and spread |
| Playground railing | 0.4 m tall at its depth | 0.85 m, three rails |
| Watering | Dashed streams | A shower of streaks from a can's rose; a thinning pour from a pan's lip |
| Baby in the pram | A plain round head | A sleeping face and a curl of hair |
| Readers | The "focused" or "content" face, half-lidded | The plain face, eyes open |
| The stuck girl | Calling or scared | Always calling, the motion lines at her feet kept |
| The low kick | Any child or teenager | The teenager first |
| Bird on the garden fence | Anywhere along it | Not on the stretch behind the clothesline, the bird table or the swing |
| Dog by the door | Its head could cover the knob | Its head clear of the knob |
| Playing catch | A high arc, the ball at its top | A lower arc, the ball coming down to the hands |
