# The v0.20 changes, read blind in whole test scenes

After the isolation bench (`isolation_v020.md`) the refined visuals and the new placement rules went back into whole
scenes, with the other events around them, and were read blind there before the set was regenerated, as in v0.8 to
v0.19. Each reader was a fresh model that saw only its one picture, with the screen's reader prompt
(`screen_prompts.md`). The pictures and descriptions are in `design_tests_v020/`; `map.txt` names the scene behind each
picture. The four templates the v0.19 gate failed were put in them: the bucket hat in three (once at the back of the
park), a drink on a park bench, the dropped ice cream in three with no ice-cream eater beside it, and a jumper in three
with a bird nearby.

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (garden, tier 4) | The bucket hat; the frying pan with no watering can in the picture; a jumper with a bird perched on the fence; a dug hole off the path | "A woman ... stands with her hands on her hips and a white bucket upside-down on her head like a hat"; "He is pouring the water from a grey frying pan, not a watering can"; "a child ... is jumping in the air with both arms raised, looking happy", the bird simply "on top of the fence"; "digging a hole with a shovel, with a mound of dirt piled next to it" |
| `test_2.png` (park) | The ladder clear of the pond; the dropped ice cream with no eater beside it | "A wooden ladder ... stands upright behind the bench, beside the path ... resting against nothing"; but "its feet are just behind the bench backrest, so it could also be read as propped on or just behind the bench". The girl "holds an empty ice-cream cone ... Her pink scoop ... has fallen and splattered on the grass at her feet", the dog "about to lick or eat it" |
| `test_3.png` (park) | A drink on a bench; a runner | The man "sits on a wooden park bench and drinks from a red cup with a straw"; a woman "running fast along the path ... speed lines behind her", but "heading in the general direction of the bench and the man's outstretched feet, so she might come close to him or run past right in front of him" |
| `test_4.png` (garden, windy) | The blown swing inside its frame; the standing wheelbarrow; the hose's jet ending in the bed | Hat, leaves and washing blowing; "an empty swing set with one red seat ... slightly tilted, which might hint that the wind is moving it"; "an empty wheelbarrow"; "watering a colourful flower bed with a green garden hose". No overlap remarked. The water "falls straight onto the flowers and is not blown sideways" (O6) |
| `test_5.png` (street, tier 4) | The bucket hat; the dropped ice cream; sitting on nothing; the reading walker | "An upside-down bucket on her head like a hat"; the child "holds an empty ice-cream cone and covers their face as if crying, because a pink scoop ... has fallen"; "sitting on thin air"; "walking ... while reading an open book. A red ball lies on the ground just in front of him" |
| `test_6.png` (playground, tier 4) | A jumper with a bird on the railing; animals by the sandpit; the dropped ice cream | "Both arms up in the air and is off the ground above his own shadow, as if jumping for joy", the bird far off on the fence; the dog by the ice cream and the dog reading clear of the sandpit, no remark on the frame |
| `test_7.png` (park, tier 4) | The bucket hat at the back of the park; an ice-cream eater with no dropped ice cream; a runner; a jumper | "Wearing what looks like a metal bucket upside down on his head"; "a child ... licking or holding up a pink ice-cream cone"; the runner "with one arm reaching forward ... running toward the jumping girl / the child with ice cream", unclear why |

The bucket hat read as a bucket worn as a hat in all three scenes, once "white", at the back of the park "a metal bucket"
(one reader thought him "rather large for his distance": the pail adds a head's height). The drink on the bench read as
"a red cup with a straw". No jumper was read as reaching for a bird, and no ice-cream eater shared a picture with a
dropped ice cream. The pan read as a frying pan, the wheelbarrow and the hose drew no remark, and the swing seat read as
moved by the wind or "just how it was drawn", inside its frame.

Two remarks led to changes before the set was built (placement revision 18):

- A runner's lane, the ground ahead that nothing of another event may enter now or later, is longer and deeper for a
  runner: 300 instead of 230 px ahead (at full scale), and from 150 px behind the runner's line to 50 px in front of it,
  instead of 26 and 16, for people, animals and things; standing structures, and now the flower bed and rocks, only on the
  runner's own line. Both runners above ran at someone off their line, which the old lane missed: the bench sitter's feet
  115 px behind it, the jumping girl in the air above it.
- The ladder kept 40 px clear of a bench at the sides and 80 px behind it.
