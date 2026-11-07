# Blind screen prompts

The prompts given to the readers and the scorer in all thirty-five screens (v0.4 to v0.38) and the v0.9 retest, with the
picture count and paths left as placeholders. Each reader is a fresh model instance that sees only its
own blind pictures (`vNN/blind/pic_NN.png`); the scorer sees only the descriptions and `keys.json`.
In v0.6 four readers described 7, 6, 6 and 6 pictures. In v0.7 six readers described 7, 7, 7, 7, 7 and 6
pictures, and the reader prompt gained one sentence (one v0.6 reader had cropped and enlarged its pictures):
"Look at each picture as a whole, the way it opens with the Read tool: do not crop, zoom, enlarge or
otherwise process the images."

In v0.7 and v0.8 the scoring was split between two scorers with the same prompt, each given part of the
pictures and the matching part of the key (`keys_a.json`, `keys_b.json`), writing `scores_a.json` and
`scores_b.json`, which were merged into `scores.json`; each scorer also validated that every key item was
scored exactly once. In v0.8 six readers described 7, 7, 7, 6, 6 and 6 pictures (39 in all), and the
scorers took pictures 1 to 16 (240 items) and 17 to 39 (242 items). The fork tests before the screen
(`fork_tests_v08.md`) used the same reader prompt for one picture each. In v0.9 six readers described
7, 7, 7, 7, 7 and 6 pictures (41 in all), and the scorers took pictures 1 to 20 (256 items) and 21 to
41 (249 items); the design tests before the screen (`design_tests_v09.md`) again used the reader prompt
for one picture each. The v0.9 retest (`v09_retest/`) read the same 41 v0.9 pictures again with six
new readers (7, 7, 7, 7, 7 and 6 pictures, the blind copies in `v09/blind/`) and two new scorers (pictures 1
to 20 and 21 to 41). In v0.10 nine readers described 7, 7, 7, 6, 6, 6, 6, 6 and 6 pictures (57 in all),
and three scorers took pictures 1 to 16 (237 items), 17 to 38 (227) and 39 to 57 (219), writing
`scores_a.json` to `scores_c.json`; the design tests before the screen (`design_tests_v010.md`) used the
reader prompt for one picture each. In v0.11 nine readers described 7, 7, 7, 7, 7, 7, 7, 6 and 6
pictures (61 in all), and three scorers took pictures 1 to 17 (239 items), 18 to 38 (230) and 39 to 61 (236);
the design tests before the screen (`design_tests_v011.md`, three rounds, fourteen pictures) used the reader
prompt for one picture each.
In v0.12 nine readers described 7, 7, 7, 7, 7, 7, 6, 6 and 6 pictures (60 in all), and three scorers took
pictures 1 to 18 (219 items), 19 to 38 (238) and 39 to 60 (237). Before the screen, the isolation bench
(`isolation_v012.md`) had readers describe single cut-outs, one template alone, with its own short prompt
(given there), and the design tests (`design_tests_v012.md`, five rounds, nineteen pictures) used the
reader prompt for one picture each.
In v0.13 nine readers described 7, 7, 7, 7, 7, 7, 7, 6 and 6 pictures (61 in all), and three scorers took
pictures 1 to 19 (248 items), 20 to 39 (231) and 40 to 61 (238), each told to check that every item of
its share was scored. The isolation bench (`isolation_v013.md`, five rounds, 36 cut-outs) used the
isolation prompt given in `isolation_v012.md`, and the design tests (`design_tests_v013.md`, two rounds,
ten pictures) the reader prompt for one picture each.
In v0.14 nine readers described 7, 7, 7, 7, 7, 6, 6, 6 and 6 pictures (59 in all), and three scorers took
pictures 1 to 18 (237 items), 19 to 39 (226) and 40 to 59 (226). One more probe, built after a set picture was
rebuilt so that every template stayed in three screened pictures, was read by a tenth reader and scored by a
fourth scorer with the same prompts (picture 60, 14 items). The isolation bench (`isolation_v014.md`, four
rounds, 52 images, two of them side-by-side readings of competing drawings) used the isolation prompt given in
`isolation_v012.md`, and the design tests (`design_tests_v014.md`, three rounds, eleven pictures) the reader
prompt for one picture each.
In v0.15 nine readers described 7, 7, 7, 7, 7, 7, 7, 7 and 6 pictures (62 in all), and three scorers took
pictures 1 to 20 (250 items), 21 to 40 (243) and 41 to 62 (245), each told to check that every item of its share
was scored and to list the half points as well as the zeros and misreads. The isolation bench (`isolation_v015.md`, two
rounds, 36 images) used the isolation prompt given in `isolation_v012.md`, and the design tests
(`design_tests_v015.md`, one round, six pictures) the reader prompt for one picture each.
In v0.16 nine readers described 8, 7, 7, 7, 7, 7, 7, 7 and 7 pictures (64 in all), and three scorers took pictures
1 to 21 (251 items), 22 to 43 (248) and 44 to 64 (247), with the v0.15 scorer prompt (each told to check that every
item of its share was scored and to list the half points). The isolation bench (`isolation_v016.md`, two rounds,
26 cut-outs) used the isolation prompt given in `isolation_v012.md`, and the design tests (`design_tests_v016.md`,
one round, six pictures) the reader prompt for one picture each.
In v0.17 nine readers described 8, 8, 7, 7, 7, 7, 7, 7 and 7 pictures (65 in all), and three scorers took pictures
1 to 22 (246 items), 23 to 42 (247) and 43 to 65 (255), with the same scorer prompt. The isolation bench
(`isolation_v017.md`, two rounds, 19 cut-outs) used the isolation prompt given in `isolation_v012.md`, and the design
tests (`design_tests_v017.md`, one round, six pictures) the reader prompt for one picture each.
In v0.18 nine readers described 7, 7, 7, 7, 7, 7, 6, 6 and 6 pictures (60 in all), and three scorers took pictures
1 to 18 (239 items), 19 to 39 (245) and 40 to 60 (236), with the same scorer prompt, given the file names of its share
(`keys_a.json` to `keys_c.json`, `scores_a.json` to `scores_c.json`). The isolation bench (`isolation_v018.md`, two
rounds, 14 cut-outs) used the isolation prompt given in `isolation_v012.md`, and the design tests
(`design_tests_v018.md`, one round, six pictures) the reader prompt for one picture each.
In v0.19 nine readers described 8, 8, 7, 7, 7, 7, 7, 7 and 7 pictures (65 in all), and three scorers took pictures
1 to 22 (253 items), 23 to 43 (258) and 44 to 65 (249), with the same scorer prompt, given the file names of its share.
The isolation bench (`isolation_v019.md`, two rounds, 15 cut-outs) used the isolation prompt given in
`isolation_v012.md`, and the design tests (`design_tests_v019.md`, one round, six pictures) the reader prompt for one
picture each.
In v0.20 nine readers described 8, 8, 7, 7, 7, 7, 7, 7 and 7 pictures (65 in all), and three scorers took pictures
1 to 22 (245 items), 23 to 43 (254) and 44 to 65 (247), with the same scorer prompt, given the file names of its share.
The isolation bench (`isolation_v020.md`, two rounds, 14 cut-outs) used the isolation prompt given in
`isolation_v012.md`, and the design tests (`design_tests_v020.md`, one round, seven pictures) the reader prompt for one
picture each.
In v0.21 nine readers described 8, 8, 7, 7, 7, 7, 7, 7 and 7 pictures (65 in all), and three scorers took pictures
1 to 22 (223 items), 23 to 43 (278) and 44 to 65 (243), with the same scorer prompt, given the file names of its share.
v0.21 changed no drawing, so there was no isolation bench; the design tests (`design_tests_v021.md`, one round, seven
pictures) used the reader prompt for one picture each.
In v0.22 nine readers described 8, 8, 7, 7, 7, 7, 7, 7 and 7 pictures (65 in all), and three scorers took pictures
1 to 22 (247 items), 23 to 43 (254) and 44 to 65 (254), with the same scorer prompt, given the file names of its share.
The isolation bench (`isolation_v022.md`, one round, eight cut-outs) used the isolation prompt given in
`isolation_v012.md`, and the design tests (`design_tests_v022.md`, two rounds, eight pictures) the reader prompt for one
picture each.
In v0.25 nine readers described 8, 8, 8, 8, 8, 7, 7, 7 and 7 pictures (68 in all), and three scorers took pictures 1 to 22, 23 to 45 and 46 to 68, on Claude Opus 5.5.
In v0.26 nine readers described 8, 8, 8, 8, 7, 7, 7, 7 and 7 pictures (67 in all), and three scorers took pictures 1 to 22, 23 to 44 and 45 to 67, on Claude Opus 5.5, with the prompts unchanged.
In v0.27 nine readers described 8, 8, 8, 8, 7, 7, 7, 7 and 7 pictures (67 in all), and three scorers took pictures 1 to 22, 23 to 44 and 45 to 67, on Claude Opus 5.5, with the prompts unchanged.
In v0.28 nine readers described 8, 8, 8, 8, 8, 8, 8, 7 and 7 pictures (70 in all), and three scorers took pictures 1 to 23, 24 to 46 and 47 to 70, on Claude Opus 5.5, with the prompts unchanged.
In v0.29 nine readers described 9, 9, 9, 8, 8, 8, 8, 8 and 8 pictures (75 in all), and three scorers took pictures 1 to 25, 26 to 50 and 51 to 75, on Claude Opus 5.5, with the prompts unchanged.
In v0.30 nine readers described 9, 9, 9, 9, 9, 9, 8, 8 and 8 pictures (78 in all), and three scorers took pictures 1 to 26, 27 to 52 and 53 to 78, on Claude Opus 5.5, with the prompts unchanged.
In v0.31 nine readers described 8, 8, 8, 8, 8, 8, 8, 8 and 7 pictures (71 in all), and three scorers took pictures 1 to 23, 24 to 47 and 48 to 71, on Claude Opus 5.5, with the prompts unchanged. Its readers each remarked less than the least of v0.30's (`flaws_v031.md`).
In v0.32 nine readers described 8, 8, 8, 8, 8, 7, 7, 7 and 7 pictures (68 in all), and three scorers took pictures 1 to 22, 23 to 45 and 46 to 68, on Claude Opus 5.5, with the prompts unchanged.
In v0.33 nine readers described 9, 9, 9, 9, 9, 9, 9, 9 and 8 pictures (80 in all), and three scorers took pictures 1 to 26, 27 to 53 and 54 to 80, on Claude Opus 5.5, with the prompts unchanged.
In v0.34 nine readers described 10, 10, 9, 9, 9, 9, 9, 9 and 9 pictures (83 in all), and three scorers took pictures 1 to 27, 28 to 55 and 56 to 83, on Claude Opus 5.5, with the prompts unchanged.
In v0.35 nine readers described 10, 9, 9, 9, 9, 9, 9, 9 and 9 pictures (82 in all), and three scorers took pictures 1 to 27, 28 to 54 and 55 to 82, on Claude Opus 5.5, with the prompts unchanged.
In v0.36 nine readers described 10, 9, 9, 9, 9, 9, 9, 9 and 9 pictures (82 in all), and three scorers took pictures 1 to 27, 28 to 54 and 55 to 82, on Claude Opus 5.5, with the prompts unchanged.
In v0.37 nine readers described 10, 9, 9, 9, 9, 9, 9, 9 and 9 pictures (82 in all), and three scorers took pictures 1 to 27, 28 to 54 and 55 to 82, on Claude Opus 5.5, with the prompts unchanged.
In v0.38 nine readers described 9, 9, 9, 9, 8, 8, 8, 8 and 8 pictures (76 in all), and three scorers took pictures 1 to 25, 26 to 50 and 51 to 76, on Claude Opus 5.5, with the prompts unchanged.
One line was added to the scorer prompt, for the first time since v0.4: "List under "unintended" only what the describer presents as looking wrong, impossible or confusing,
at most three for a picture, the most striking first; leave out hedges about small details." The isolation bench (`isolation_v025.md`, two rounds, 20 cut-outs) used the
isolation prompt, and the design tests (`design_tests_v025.md`, six pictures, two each per reader) the reader prompt.

In v0.24 nine readers described 8 pictures each (72 in all), and three scorers took pictures 1 to 24, 25 to 48 and 49 to 72. The readers and
scorers ran on Claude Opus 5.5. The prompts are unchanged, and they do not say how many oddities to log: this release's scorers logged 83% of
what the readers reported, v0.23's 22% (`flaws_v024.md`). The isolation bench (`isolation_v024.md`, two rounds, 16 cut-outs) used the isolation
prompt, and the design tests (`design_tests_v024.md`, six pictures, two each per reader) the reader prompt. One further reader, the control in
`v024/control/`, described eight unchanged v0.23 pictures with the reader prompt.

In v0.23 nine readers described 8, 8, 7, 7, 7, 7, 7, 7 and 7 pictures (65 in all), and three scorers took pictures
1 to 22 (237 items), 23 to 43 (272) and 44 to 65 (220), with the same scorer prompt, given the file names of its share.
The isolation bench (`isolation_v023.md`, two rounds, 20 cut-outs) used the isolation prompt given in
`isolation_v012.md`, and the design tests (`design_tests_v023.md`, two rounds, eight pictures) the reader prompt for one
picture each.

## Reader

```
You are taking part in a picture-description legibility check. Look at N cartoon pictures and describe them as an attentive test participant would. You must NOT open, list or search any other file or folder (no Glob, Grep, ls, or reading JSON/code) — only the N image files named below, so your descriptions stay blind to the answer key.

Images (open each with the Read tool):
/home/claude/tpdb/vision/vNN/blind/pic_01.png
/home/claude/tpdb/vision/vNN/blind/pic_02.png
/home/claude/tpdb/vision/vNN/blind/pic_03.png
/home/claude/tpdb/vision/vNN/blind/pic_04.png
/home/claude/tpdb/vision/vNN/blind/pic_05.png
/home/claude/tpdb/vision/vNN/blind/pic_06.png
/home/claude/tpdb/vision/vNN/blind/pic_07.png

For each picture, write a file /home/claude/tpdb/vision/vNN/desc_pic_NN.md (NN = the picture number) with these sections:
1. "Free description": 4–10 sentences telling someone who can't see the picture everything that is going on — who is there, what they are doing, anything that seems about to happen, anything that looks wrong, odd or impossible.
2. "Inventory": one line per person or animal: where it is (left/centre/right, front/back), what it looks like (e.g. "boy in yellow shirt"), and what it is doing. Then one line per notable object (kites, balls, boxes, hats in the air, water, etc.) saying what it is and what it seems to be doing or for.
3. "Unsure or ambiguous": anything you could not make out or that could be read two ways (say both readings), and anything that looks unintentionally strange (e.g. things floating, objects passing through people, odd shapes).

Be literal about what you actually see; don't guess what a test designer intended. When done, reply with just the N file paths.
```

## Scorer

```
Score picture descriptions against an answer key, like a clinician scoring a picture-description test.

Inputs (read only these files):
- /home/claude/tpdb/vision/vNN/desc_pic_01.md … desc_pic_MM.md — blind descriptions of M cartoon pictures. Each has a free description, an inventory, and an "unsure or ambiguous" section.
- /home/claude/tpdb/vision/vNN/keys.json — for each picture (pic_01 … pic_MM), the scored items: id, type (entity, action, inference, contradiction), the target text, and accepted phrasings.

For each item decide, using the whole description file (free description + inventory + unsure section):
- 1 = clearly mentioned with the right meaning (any wording that conveys the target; accepted phrasings are examples, not an exhaustive list)
- 0.5 = partly (the right element seen but the action/meaning only half right, or only offered as one of two readings)
- 0 = not mentioned
- "misread" = the element was mentioned but read as something else (record what they said instead)
For inference items, credit 1 only if the describer states the inferred meaning (the cause, prediction or intention), not just the visible elements. For contradiction items, credit 1 only if they say it is wrong/impossible/odd or describe the impossible fact itself.

Write /home/claude/tpdb/vision/vNN/scores.json as:
{"pic_01": {"items": {"i01": {"score": 1, "note": "short evidence or misreading"}, ...},
            "unintended": ["oddities the describer reported that are NOT scored items, e.g. 'bike standing by itself'"]}, ...}
Then write /home/claude/tpdb/vision/vNN/scores_summary.md: a table of mean score by item type, a list of every item scored 0 or misread (pic, id, target text, what the describer said), and a list of all unintended oddities grouped by kind.

Reply with a 10-line summary: mean score by type, and the five most common failure patterns.
```
