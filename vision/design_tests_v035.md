# v0.35 design tests

The bench's choice and revision 33 were read blind in whole test scenes among other events: ten pictures, ten fresh readers, one picture each (`design_tests_v035/test_N.png`, `desc_test_N.md`; the prompts are `tpdb_work/dtp35p/test_N.txt`, the reader template cut to one picture). `tools/cycle/design_tests.py` has the jobs. Tests 1 to 6 were drawn with the frame widened on both sides, as on the bench; the first one's reader found its leg on the path, so the frame was widened on the side away from the path only, the seat swung that way, and the four swing pictures were drawn again and read by four more readers (tests 7 to 10, the same seeds).

| Test | Picture | What it tests | What the reader said |
|---|---|---|---|
| 1 | Tier-3 garden | The child on the swing, swung out, and a man raking | "She sits on a red swing seat that is pushed out towards the right, with motion lines on her left. She seems to be swinging". And: "The left front leg of the swing set seems to stand on or right at the edge of the paved path instead of on the grass" |
| 2 | Tier-3 garden | The same, by a kite stuck in a tree and a man carrying a box | "sitting on a red swing seat; swinging (motion lines behind the seat), smiling" |
| 3 | Tier-3 garden | The same, with a woman sitting on nothing | "Sitting on the red swing seat and swinging (there are motion lines to the left of the swing)" |
| 4 | Tier-3 garden | The swing in the wind | "swinging (motion lines on the left of the swing)". Of the wind: "The tree, bushes, flowers, the man's clothes and the child's hair don't move at all" |
| 5 | Tier-3 garden | The wind with no pile swept or raked (revision 33), someone digging and a cat on the fence | "This is a sunny but windy back garden"; nothing said to lie still in the wind |
| 6 | Tier-3 park | Sweeping and raking with no wind, as before | Both read: "both are clearing up fallen leaves". And, as since v0.11: "the trees are fully green while both people are clearing piles of fallen leaves" |
| 7 | Test 1 again, the frame widened away from the path | | "She sits on a red swing seat holding the ropes, swinging (motion lines trail to her left)" |
| 8 | Test 2 again | | "Small point: the swing seat tilts noticeably while the child's legs hang down. This fits a swing in motion and doesn't look wrong." |
| 9 | Test 3 again | | "Sitting on the swing seat, smiling with eyes closed, swinging (motion lines to the right of the seat)" |
| 10 | Test 4 again | | "He is swinging, and the seat is pushed out to the left with motion lines behind it on the right" |

In all eight swing pictures the child is swinging, and no reader says the swing hangs still. The frame is widened by the swing itself, when it swings a child, so a garden with an empty swing keeps v0.34's frame: drawn wider for every swing set, the tier-4 garden's empty seat hung off the middle of its beam. Tests 7 to 10 come out identical to the pixel under that code. The leg on the path is gone with the one-sided frame, and no reader of the four pictures drawn again mentions the path or the frame. The windy garden draws no remark of a pile lying still, and sweeping and raking still place where there is no wind. The hair and clothes that the wind does not move are a limit of the cast, as noted since v0.19. No reading called for a new rule.
