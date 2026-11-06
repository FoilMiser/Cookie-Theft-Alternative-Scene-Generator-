# v0.34 design tests

The bench's choice and revision 32 were read blind in whole test scenes among other events: six pictures, six fresh readers, one picture each (`design_tests_v034/test_N.png`, `desc_test_N.md`; the prompts are `tpdb_work/dtp34/test_N.txt`, the reader template cut to one picture). `tools/cycle/design_tests.py` has the jobs; the three of the woman in yellow seated reading needed up to 80 seeds each, as the bench's reader is drawn from the whole cast.

| Test | Picture | What it tests | What the reader said |
|---|---|---|---|
| 1 | Tier-3 garden | The woman in yellow, long-haired, reading on the bench, and a man raking | "a woman or teenage girl in a yellow dress and red shoes sits on a wooden bench reading a red book"; "Dark hair tied back, yellow short-sleeved dress". "The person on the bench could be read as an adult woman or as a teenage girl." |
| 2 | Tier-3 park | The same, by the pond, with a man fishing | "a girl or young woman with dark hair in a ponytail, a yellow dress and red shoes sits on a wooden park bench reading a red book"; "the reader on the bench could be a girl or a young woman" |
| 3 | Tier-3 street | The same, with a walker | "a girl or young woman with dark tied-back hair, a yellow dress and red shoes sits on a wooden bench, reading a red book" |
| 4 | Tier-3 garden | The storm pointer, with washing on the line | "points up towards the sky and the dark clouds with her mouth open, as if calling out or warning someone". Weighed: "most likely the dark clouds (warning that rain is coming), but she could also be read as pointing at the washing on the line, which is up and to her left as well." The washing is about 40 degrees off her arm's line, outside the cone of 36 that revision 32 now checks it against |
| 5 | Tier-3 garden | A hose beside a floating box, which revision 31 refused | "waters a flower bed with a garden hose"; "The odd thing is a cardboard box hanging in the sky above the fence" |
| 6 | Tier-3 garden | The wind, nobody watering | "It is a sunny, windy day in a back garden"; the cap "has just blown off his head"; the hose "lying on the grass" |

No reading called for a new rule. In all three pictures the woman in yellow is a woman or a girl in a yellow dress, where on the bench with the bob she had been "a child", "a boy" or "a person", and the readers who call her "the woman" outnumber those who settle on a girl. The hose and the floating box read side by side, and the windy garden draws nothing on water. The storm pointer by the washing reads first at the clouds, and the washing, wider of her arm than the cone, still came up as a second reading: a wider cone for the washing is on the list for v0.35.
