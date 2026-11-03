# v0.24 design tests

The new drawings and the rules of revision 22 were read blind in whole test scenes among other events: six pictures, three fresh readers, two pictures each in different settings (`design_tests_v024/test_N.png`, `desc_test_N.md`; `map.json` names the records). `tools/cycle/design_tests.py` lists what each forces. No new rule came out of them, so there was no second round.

| Test | Picture | What it tests | What the reader said |
|---|---|---|---|
| 1 | Tier-4 park | Older man walking with a bag, a sleeping cat, the reading walker; nobody in the strip before the horizon | The cat lies clear of everyone, with no word of tripping; the older man at the back drew no remark on his size. The cat "could be curled up asleep or lying upside down on its back" |
| 2 | Tier-3 playground | Teenager kicking, riders on the seesaw | "Boy ... Red cap worn backwards ... kicking a ball to the right"; "I read the cap as being on backwards. It could be misread as him facing left". No remark on how the riders sit |
| 3 | Tier-3 park | Teenager with an ice cream, a sleeping dog among a walker and a runner | "The boy's cap could be on backwards or sideways"; nothing about the dog and anyone's feet |
| 4 | Tier-4 street | Teenager as photographer, a flying cap on someone else, a bucket for a hat | "They could be a boy or an adult, as they are about as tall as the older man"; the flying cap goes with the bareheaded woman. "The woman in yellow stands right against the shop front and looks large compared with the door" |
| 5 | Tier-3 garden | Teenager catching, a sleeping cat on the path behind a walker and her dog | "Boy", "getting ready to catch". The dog "faces away from it and is walking the other way". The cat "could be read as an orange heap ... or hurt" |
| 6 | Tier-2 playground | The other child on the slide, a sleeping dog, a pram | "Sitting and sliding to the right, with both arms stretched up and forward"; "enjoying the ride with her arms up, or reaching"; "on or just above the chute ... very slightly hovering" |

## What this says

- **The teenager.** Named a boy in three pictures and "a boy or an adult" in the fourth; no reader called him a woman, where in v0.23 the pattern held in all four of one scorer's pictures. No reader volunteered "teenager". The key's accepted answers include "boy", and the v0.24 screen scores it across many more pictures. The cap worn backwards was read as such each time it was mentioned, and one reader noted it could mislead about which way he faces.
- **Sleepers.** No reader put a sleeping animal at anyone's feet. In test 5 the walker's dog was noticed near the cat and judged to be walking away from it.
- **The back strip.** No remark on size in the park or on the playground. The one remark is in the street (test 4), which revision 22 leaves alone: its back row stands at the shop fronts, and the tier-4 street is already the hardest cell to place. Kept as a note for the pilot.
- **The slide's arms.** Read as raised, with the face in view. No reader said she was holding her head or covering her face. Her contact with the chute is still read loosely ("very slightly hovering"), as since v0.21.
- **The curled-up cat.** Two readers offered "hurt" or a heap as a second reading of `sleep_tuck`, and both still read it as asleep. Not on the v0.23 list; left for the screen to count.
