# The v0.15 changes, read blind in whole test scenes

After the isolation bench (`isolation_v015.md`) the refined visuals went back into whole scenes, with the other events
around them, and were read blind there before the set was regenerated, as in v0.8 to v0.14. Each reader was a fresh model
that saw only its one picture, with the screen's reader prompt (`screen_prompts.md`). The pictures and descriptions are in
`design_tests_v015/`; `map.txt` names the scene behind each picture.

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (garden) | A wave among a kite flyer, a sweeper and a reader walking toward a ball; the washing in the kite's breeze | The child "has one arm raised, as if waving" ("or holding or throwing something small"); the reader "looks about to trip over it"; no remark on the washing |
| `test_2.png` (park) | The sprinkler's hose clear of the path; a bird on a branch; raking with the open-eyed face | The hose runs "from the left edge to the sprinkler"; the bird "perched on a short branch inside the tree's leaves" ("the branch looks a bit stuck on"); the raker's face "points right" |
| `test_3.png` (street) | A wave beside a lost balloon; the lost balloon's colour beside a girl's yellow balloon | The man "raises one hand high in a wave; little motion marks around the hand show it is moving"; the red balloon "has just slipped away and is floating off" |
| `test_4.png` (playground) | A wave beside the stuck girl on the seesaw and a kicker; the girl in a dress on the seesaw | "A tall bearded man ... waves with one hand high in the air"; the girl "is stuck up on the high end ... the old man is so absorbed in his book that he seems unaware he is keeping her up in the air" |
| `test_5.png` (garden) | A wave beside the blocked hose; the swing; the bird table on the lawn | "He has one hand raised and is waving ... mouth open as if he is calling hello"; the child on the swing "smiling ... swinging"; "a birdhouse with a red roof on a tall pole"; the blocked hose read in full ("when the dog steps off, water may suddenly gush out") |
| `test_6.png` (park, tier 4) | A wave beside a picnic and a reader walking toward a bucket; a bird on the lamp | "A woman in a yellow dress ... stands with one arm raised high, waving"; the bucket "directly in her path, so she looks about to walk into it or trip over it" |

The wave read as a wave in all five scenes, aimed each time at someone simply going about their day, and no waver was
read as reacting to a mishap. No reader saw a leg apart from a body, closed eyes on a chore, a hose across a path, a
bush or a bird table behind the fence, or washing hanging still beside a kite. The remarks left were small and
mostly older: fallen leaves under green trees (raking, as since v0.11), a man waving at the back who looks a little large
for his distance, the broom handle running along the gate's diagonal brace, and the swing's ropes hanging straight while
its motion lines show it moving. No change followed.
