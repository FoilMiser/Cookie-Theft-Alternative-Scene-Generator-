# The v0.22 changes, read blind in whole test scenes

After the isolation bench (`isolation_v022.md`) the new square wheel and the placement rules of revision 20 went into whole
scenes, with the other events around them, and were read blind there before the set was regenerated, as in v0.8 to
v0.21. Each reader was a fresh model that saw only its one picture, with the screen's reader prompt (`screen_prompts.md`).
The pictures and descriptions are in `design_tests_v022/`; `map.txt` names the scene behind each picture. Two rounds,
eight pictures.

## Round 1 (six pictures)

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (street, tier 4) | A jumper clear of the stall and the benches behind; the square-wheeled bicycle; the dropped ice cream | The bicycle's "wheels are drawn as squares instead of circles, which is impossible"; but the jumper, a girl at the back right by the shop fronts, "seems to be jumping or dancing for joy" and then "either jumping in the air or just standing with her arms raised (cheering, stretching or dancing). Her shadow being a bit off from her feet could also just be a drawing quirk" |
| `test_2.png` (park, tier 4) | The reading walker with her bucket, a sleeping cat placed later, the barrow's new square wheel, a runner | "A blue bucket sits on the grass right in her path, so she looks about to trip over it or kick it"; the cat "curled up asleep on the grass", not linked to her; the wheelbarrow's "wheel is drawn as a square, which would be impossible to roll ... It could also be read as a square box or crate"; the runner "running quickly to the left", nothing on his line |
| `test_3.png` (garden) | The sprinkler's hose off the side, not the bottom; a kick clear of people further back | "A garden hose runs along the grass to a sprinkler, which sprays arcs of water straight onto a cardboard box"; the hose "comes in from off the left edge ... runs past the bench legs at ground level"; the ball "flying toward a paved path that leads to a closed wooden gate" |
| `test_4.png` (garden) | The frying pan over a flower bed on the ground; a jumper in front | "Pouring water from a grey can/pan onto a round bed ... The main oddity is the grey watering vessel, which looks more like a frying pan or saucepan than a watering can"; "a small girl in a pink dress is jumping in the air with both arms raised, looking excited" |
| `test_5.png` (park) | The ladder's top up against the hedge, clear of the lamp post | "The wooden ladder ... stands upright in the open grass and leans slightly with nothing to lean against, which could not really happen" |
| `test_6.png` (playground, tier 4) | The reading walker and her box, the square-wheeled bicycle, a sleeping dog; a jumper | "A cardboard box sits right in front of her leading foot, so she looks about to trip over it"; the bicycle's "wheels are drawn as squares"; the puppy "curled up ... asleep"; but the jumper, a boy at the back by the fence behind the bicycle, "seems to be jumping or cheering ... it could also just be a loosely placed shadow on the ground" |

Every rule read as meant except the jumper's. Clear of the stall, at the back of the street and of the playground, the
jumper was still hedged between jumping and standing with arms raised, as in the v0.21 tier-4 street; at the front of
the garden she was "jumping in the air with both arms raised". A jumper's lift is drawn to scale, so at the back the gap
under the feet is small. Revision 20 therefore also keeps a jumper in the front half of the ground (at least 200 px below
the horizon), and test_1 and test_6 were rebuilt.

## Round 2 (the two rebuilt scenes)

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_7.png` (street, tier 4) | test_1's scene, the jumper in the front half | "Both arms raised, mouth open and smiling, feet off the ground with her shadow beneath her; she is jumping for joy or cheering"; "the girl in pink is clearly jumping, with her shadow on the ground below her" |
| `test_8.png` (playground, tier 4) | test_6's scene, the jumper in the front half | "Jumping with both arms raised overhead ... his shadow is a separate oval on the grass beneath him, so he is in mid-air"; "clearly jumping" |

Both jumpers read as jumping, with no other reading offered.
