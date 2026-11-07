# v0.40 isolation bench

Each visual was forced into a picture with little else and cut out, then read blind by fresh readers (the method of `isolation_v023.md`), two cut-outs to a reader and never two takes of one thing. There were two rounds:
- round 1: twenty-one readers of 41 cut-outs (`isolation_v040/round1`);
- round 2: four readers of 7 cut-outs (`isolation_v040/round2`).

`map.json` in each says which cut-out is which case.

What was drawn is `flaws_v039.md`'s list. Four changes are in the cast, behind switches read when it is built:
- `TPDB_REACH40`: the reach for a blown hat with one hand, the other by the chest (B) or at the side (C), where both arms went up before;
- `TPDB_HOSE40`: the hose held at the nozzle and, with the other hand, lower down;
- `TPDB_GRAZE40`: the goat's graze, its back level on straight legs with the mouth at the grass (B), or its chest a little higher and its head further ahead (C);
- `TPDB_WALK40`: the walking front foot left flat.

Three changes are in placement revision 38:
- `draw.HEAP40`: the broom's heap and the raked pile of dry leaves and twigs (D) or of cut grass (G);
- `templates.TUFT40`: the goat's tuft ahead of its muzzle and behind its head;
- `templates.ICE40`: an ice-cream eater at least 170 px tall. This is a placement rule only, so it was not benched.

Each thing was read in v0.39's cast and scene, **O** (`BENCH_CAST=assets/cast/out039`, its library copied), against the new drawings: **N** with every cast switch at B, **C** with the reach and the graze at C, and the heaps at D and G. The first three letters of a case name the thing.

Before the readers, the bench's own look caught two things:
- **The first reach crossed the face.** It used the near arm, which at 45 crossed in front of the face like a hand shading the eyes. It now uses the far arm.
- **Ana's reach was out of date.** Built before that change, it still crossed her face, because only three people had been rebuilt. The N cast was built again whole and every N case was run again.

The goat's graze was looked at in three rounds of four settings first (`tpdb_work/bench40/look_G1` to `G12`). Lowering the hips and chest together made it crouch on bent knees.

## Round 1

| Case | Drawn | What the readers said |
|---|---|---|
| `wh0O_1` to `_3` | the blown hat, v0.39: both arms up | The second reading in all three: "she is reaching for the cap, or she is simply startled with her hands up" (`_1`); "a surprised or cheering "hands up" gesture" (`_2`); "a cheering or throwing gesture" (`_3`) |
| `wh0N_1` to `_3` | one hand up, the other by the chest (B) | Reaching in all three, but the hand by the chest drew remarks: "Her other hand holds a thin white object upright against her chest" (`_1`); "The hand on her stomach is small and blobby ... it also looks a little stuck on" (`_2`); and once "She could be grabbing after it or just throwing up her hand in surprise" (`_2`) |
| `wh0C_1` to `_3` | one hand up, the other at the side (C) | Reaching in all three: "Her right arm is raised up and to the left toward a blue baseball cap tumbling through the air above her" (`_1`); "The most likely reading is that the wind has blown her cap off and she is reaching after it" (`_2`); "She has one arm stretched up toward an orange baseball cap" (`_3`). Once "or waving" (`_1`), once "tossed the cap" (`_2`) |
| `hi0O_1`, `_2` | the hose inspected, v0.39 | "The man's arms are drawn as one white block reaching forward" (`_1`); "His arms are held out stiffly and level at chest height" (`_2`) |
| `hi0N_1`, `_2` | the hose in two hands | Both: "One raised hand holds the nozzle up near his face, and the other hand holds the hose lower down" (`_1`); nothing said of the arms but that |
| `gt0O_1` to `_3` | the goat grazing, v0.39, at 90, 45, 135 | Hunched in all three: "the pose reads as hunched or contorted rather than a natural grazing stance" (`_1`); "The head looks squashed into the front of the body" (`_2`); "The goat looks folded or curled up rather than standing level" (`_3`); the tuft over the muzzle twice ("it could also look as if the grass is passing", `_1`) |
| `gt0N_1` to `_3` | B, the tuft ahead of the muzzle | Grazing in all three; at 90 the head "slightly pasted onto the body" (`_1`); at 45 and 135 still "a strong hump over the back" (`_2`), "hunched with a high, lumpy back" (`_3`), the legs "tangled" (`_2`) or "cramped" (`_3`) |
| `gt0C_1` to `_3` | C, the tuft ahead of the muzzle | Grazing in all three; at 90 no remark on the body; at 45 and 135 "the back is hunched and lumpy" (`_2`), "a tall, humped body" (`_3`); the bite apart from the tuft: "The green blade in the mouth sits to the right of the grass tuft and is not attached to it" (`_1`), "as if hanging or floating near the mouth" (`_3`) |
| `wk0O_1`, `_2`; `wd0O_1`, `_2` | walkers, v0.39 (the boy with an ice cream, the grandfather and his dog) | The shoes: "flat white ovals with little shoe shape" (`wk0O_1`), "look slightly pasted on" (`wk0O_2`) |
| `wk0N_1`, `_2`; `wd0N_1`, `_2` | the walking front foot flat | No gain: "reads more like a crouching step or lunge" (`wk0N_1`); "His back foot (left side) seems to point backward or down-left, not forward ... as if that foot is twisted" (`wd0N_2`) |
| `hp0O_1`, `_2`; `rk0O_1` | the heaps, v0.39's summer heap | "a small pile of fallen leaves (green, olive and brown)" (`hp0O_1`), "green, olive, brown and tan leaves" (`hp0O_2`), "could also be grass clip[pings]" (`hp0O_2`) |
| `hp0D_1`, `_2`; `rk0D_1`, `_2` | dry leaves as ovals | Leaves, but each with another reading: "They read as dry fallen leaves, but could also be read as seeds, nuts, beans" (`hp0D_1`); "wood chips, bark or small sticks" (`hp0D_2`); "peanuts, seeds, or crisps" (`rk0D_1`); "nuts, seeds, pebbles or wood chips" (`rk0D_2`) |
| `hp0G_1`, `_2`; `rk0G_1`, `_2` | cut grass | The broom's as a dome: "a green dustpan/scoop" (`hp0G_1`), "a solid green dome or upturned bowl" (`hp0G_2`); the raked pile "green leaves or clippings" (`rk0G_1`), "dark, spiky material ... twigs, dried grass clippings, pulled weeds" (`rk0G_2`) |

**Round 1.**
- **The reach: C.** It took away the hands-up reading that all three O readers offered, and its far arm at the side drew nothing; B's hand by the chest drew two remarks.
- **The hose: B.** The two hands were read apart in both.
- **The goat: C, by a little.** Its 90 was the cleanest, and both new grazes lost the "contorted" and "folded" of v0.39's. "Hunched" stays at 45 and 135 in both, which is the redrawn goat's body there, not the graze, and goes on the list.
- **The walking front foot: O.** Flat, it gained nothing, and the remark that remains is about the back foot, on its toe, which goes on the list.
- **The heaps went to round 2.** Dry leaves read as leaves every time, but ovals as nuts; cut grass as a dome.

## Round 2

The winners' cast (`BENCH_CAST=tpdb_work/bench40/out_C`), two drawings changed, on round 1's seeds:
- the dry heap's pieces drawn as leaves, pointed at both ends with a midrib and a stalk (`draw.leaf`, about twice as long as wide);
- the goat's bite running from its mouth to the tuft's top.

| Case | Drawn | What the readers said |
|---|---|---|
| `hp0D_3`, `_4`; `rk0D_3`, `_4` | the dry heap, leaf-shaped | Dry leaves in all four, and no seeds or nuts: "sweeping a small pile of brown, dry leaves next to her feet" (`hp0D_3`); "a small pile of dark brown dried leaves" (`hp0D_4`); "raking a small scatter of brown dry leaves near his feet" (`rk0D_3`); "a small pile of brown, dry-looking leaves ... some of the bits could also be read as twigs or debris" (`rk0D_4`) |
| `gt0C_4` to `_6` | C, the bite joined to the tuft, at 90, 45, 135 | "a thin green stem runs from its mouth down into the tuft, as if it is pulling up or chewing a blade" (`_6`); grazing or "sniffing or eating the flower" (`_4`). The body as before: "The head is a large round white blob that sits straight on the shoulder with almost no neck" (`_4`); "It reads as hunched rather than a normal grazing pose" (`_5`) |

**Chosen.**

| Switch | Setting |
|---|---|
| `TPDB_REACH40` | **C** |
| `TPDB_HOSE40` | **B** |
| `TPDB_GRAZE40` | **C** |
| `TPDB_WALK40` | **O** |
| `draw.HEAP40` | **D**, the leaves leaf-shaped |
| `templates.TUFT40` | **B**, the bite joined |
| `templates.ICE40` | 170 |

The goat's hunch at 45 and 135 and its short neck, and the walking back foot on its toe, go on the list (`flaws_v040.md`).
