# v0.41 design tests

The cast of builder 0.41.0, whose one redrawing is the begging dog's folded forelegs (`vision/isolation_v041.md`), was read blind in whole test scenes among other events: three pictures, three fresh readers, one picture each. Revision 39 draws nothing new. The files are `design_tests_v041/test_N.png` and `desc_test_N.md`; the prompts are `tpdb_work/dtp41p/test_N.txt`, the reader template cut to one picture. The jobs are in `tools/cycle/design_tests.py`, each with the dog at a forced angle.

| Test | Picture | What it tests | What the reader said |
|---|---|---|---|
| 1 | Tier-3 street | The dog begging in profile (90), a sweeper, an ice cream | Begging: "a brown dog with a red collar or bandana sits up on its haunches with its front paws raised, as if begging". But the dog stands nearer the passing girl with an ice cream than the boy on the bench, and it begs "perhaps for the girl's ice cream". The body once: "its hind legs are folded forward under it like a kneeling person". The dog's upturned nose and eye were "a fly or bee buzzing around it", the head as in v0.40 |
| 2 | Tier-3 park | The dog begging at 45, a kicker, a raker | Begging, and nothing more: "a small white dog with brown ears and a blue collar sits up on its hind legs with its front paws raised, begging". The heap's season once more: "the dead leaves seem a little out of place because every tree is fully green" |
| 3 | Tier-3 park | The dog begging in profile (90), a game of catch | Begging: "It looks like it is begging for the ice cream, and the man does not seem to notice". The body: "The dog's pose is very upright and almost human-like", with "a meerkat-like animal" or "a dog jumping up at the man" as other readings. The catch reads in full: "He faces left towards the girl and the ball, with both arms out and hands open, ready to catch" |

**What the tests show.**
- **The fold reads as benched.** The dog is begging in all three pictures, and in none are its forelegs rods or arms.
- **At 90 the body stays upright.** The remark of the v0.40 screen that the bench's lean did not take away, "upright", "kneeling", "human-like", comes back in both pictures at 90 and not at 45. It goes on v0.42's list with the dog's head, read as an insect in one of them.
- **A second ice cream.** In the street the dog was placed nearer a walking eater than the one on the bench. The inference, that the dog wants the food, holds either way, and it is a note.
- **The heap's season** came back in one picture of three, as in v0.40, and the bench took it off the list (`isolation_v041.md`).
