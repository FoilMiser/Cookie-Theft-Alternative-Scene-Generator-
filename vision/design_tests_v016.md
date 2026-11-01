# The v0.16 changes, read blind in whole test scenes

After the isolation bench (`isolation_v016.md`) the refined visuals and the new placement rules went back into whole
scenes, with the other events around them, and were read blind there before the set was regenerated, as in v0.8 to
v0.15. Each reader was a fresh model that saw only its one picture, with the screen's reader prompt
(`screen_prompts.md`). The pictures and descriptions are in `design_tests_v016/`; `map.txt` names the scene behind each
picture. The three templates that failed the v0.15 gate were each put back among the kind of neighbours that had pulled
their reading away: the stalking cat beside a teenager pointing at a ball in a tree (no second cat may now share its
fence), the stuck girl on the seesaw in two busy playgrounds, and a bird perched on a garden fence with a clothesline.

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (garden, tier 4) | The stalking cat with no other cat on its fence and the ball in the tree near it; a bird on the fence away from the clothesline | "A black-and-white cat creeps along toward a blue bird perched further left, so the cat looks like it is stalking the bird and might pounce"; "a red bird sits on the fence further right", in front of the tree, not "on the line"; the girl below the tree "reaching or asking for the ball" |
| `test_2.png` (playground) | The stuck girl calling, the motion lines at her feet kept, beside a kick, a carried box and a wave | "Because his end stays down, she seems to be stuck up in the air"; the lines "could mean impatient kicking"; the teenager "has just kicked an orange ball" |
| `test_3.png` (park) | The lower catch arc; a walker's lane clear of other events; the dog on its lead facing the way they walk | The ball "arcing over the path toward a woman ... reaching out with both hands together to catch it"; the reader "about to walk into it or trip over it"; the dog "walking to the right ahead of the bearded man" |
| `test_4.png` (playground, tier 4) | The stuck girl beside a dropped ice cream, a pram, a photographer and a carried box; the baby's sleeping face | The man "doesn't seem to notice that the girl is stuck up in the air"; "a sleeping baby"; but the cream oval on the pram "looks like a flat disc or lid sitting on top ... a blanket, a tray or a cake" |
| `test_5.png` (street) | The square-wheeled bicycle with the rack bicycle gone; a pram; a wave aimed at a passer-by | The square wheels "could never roll"; the baby "with eyes closed, apparently asleep"; the waver "facing left toward the woman with the pram". The bicycle still "balances upright by itself" |
| `test_6.png` (garden) | The dog clear of the door knob; the shower from a watering can; the star jump | The dog "sits in front of the door holding its own red leash in its mouth, as if asking to be taken for a walk"; "water drops coming from the spout" ("the aim looks a little low"); the jumper's "feet are clearly above the shadow", but the child jumped under the washing line: "perhaps to grab the clothes" |

All three of the v0.15 failures read in full: the cat as stalking, with no second cat to share the fence and no hand
pointing beside it; the girl on the seesaw as stuck, in both playgrounds; and the bird on the fence as perched on the
fence. The sleeping baby, the shower of water, the lower catch, the dog clear of the knob and the lead dog's direction
read as intended. No reader saw a walker heading for another event's objects, anyone too big for the playground's
railing, or closed eyes on a reader.

Two remarks led to changes before the set was built, both read in the screen that followed: the pram's flat cream
oval of a blanket ("a flat disc or lid", as on the bench) became a pink quilt over the baby, rising over its body and
hanging down the pram's side in soft folds with a stitched hem; and a jumper is never placed under the washing line or
just in front of it. The square-wheeled bicycle standing on its own stays a known limit, after four stands were tried.
