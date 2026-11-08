# TPDB release runbook

How each release from v0.12 to v0.41 was made, written so that a fresh session can make the next one (v0.42) from this
repository (https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator-; clone it to start). The README describes the package; this file describes the work. The scripts named here are in
`tools/cycle/`, and the work list for the next release is the newest `vision/flaws_v0XX.md`.

## Standing rules (from Sam)

- Colour first; the grayscale PNG is derived.
- Generic settings: no text, logos or brands anywhere in a picture.
- No cartoon emote symbols (no hearts, sweat drops, question marks over heads). Poses carry the meaning, not faces.
- Contradictions are physical, biological or functional (a square wheel, a fish in a tree, watering with a frying pan).
- Exact rebuilds within a release: every record rebuilds pixel for pixel with that release's package.
- Keep finding the weakest visuals and refining them one at a time, each read blind on its own before it goes into scenes.
- A release is one zip (`python3 package_release.py 0.XX --single`), sent to Sam, and pushed to GitHub when done.

## Setup

```bash
python -m venv .venv
source tools/env.sh                  # activates .venv, sets TPDB_VER and TPDB_WORK (repo/tpdb_work, ignored by git), UTF-8 text
pip install -r requirements.txt      # Linux without an installed Blender: also pip install bpy==5.2.3 (Python 3.13)
```

`source tools/env.sh` comes first in every new shell. It works from Git Bash on Windows too, where `python build_cast.py`
and `render_set.py` re-run themselves inside the installed Blender (`assets/blender_run.py`; set `TPDB_BLENDER` if it is
not under Program Files) and cairosvg draws through the cairo in the pycairo wheel (`scenegen/cairo_compat.py`).

`tools/cycle/cfg.py` reads `TPDB_VER`, from which the scripts derive TAG=024 and PREV=023, and `TPDB_WORK`. More CPU cores
help most with the tier-4 seed searches and the Blender renders; two cores were enough but slow (a tier-4 street search
can take hours).

## The cycle

Each step names its script. Keep the previous release's folders (`scenes`, `probes`, `site`) untouched until the swap in
step 7, and build the new release beside them in `scenes<TAG>`, `probes<TAG>`, `site<TAG>`,
`assets/cast/{out,lib,gallery}<TAG>`.

### 1. Read the work list

`vision/flaws_v0<PREV>.md` lists what the last screen's readers misread or half-read (R rows) and the oddities they
reported (O rows), each with a proposed fix. Sort them into drawing changes (go to the bench, step 2) and placement
changes (a new placement revision, step 3).

### 2. Drawing changes: the isolation bench

- Cast drawings live in `assets/cast/castlib/` (Blender, `bpy`): `actions.py` (poses and props), `animals.py`, `people.py`
  (bodies, hair, faces). Scene drawings (settings, props drawn in SVG) live in `scenegen/draw.py` and `scenegen/settings.py`.
- Put each candidate drawing behind a switch so the release cast is unchanged until a winner is chosen. v0.23 used
  environment variables (`TPDB_PAN`, `TPDB_BEG`, `TPDB_HEAD` in castlib) and module flags (`draw.SQUARE_STYLE20`,
  `draw.LEG23`); keep the old drawings reachable, and record in a comment which bench chose which variant.
- Build a bench cast per variant set: `cd assets/cast && TPDB_PAN=D python build_cast.py <WORK>/bench/out_b1`; seed a bench
  library from the current one minus the changed families' files; then add bench cases to `vision/isolation_bench.py`
  (`BENCH` dict: setting, seed, forced templates, what to crop) and run
  `BENCH_CAST=<out> BENCH_LIB=<lib> python vision/isolation_bench.py <WORK>/bench/r1 case1 case2 ...`.
- `tools/cycle/iso_round.py <bench_dir> vision/isolation_v<TAG>/round1 <WORK>/isop <tag> case1 case2 ...` shuffles the
  crops into `iso_NN.png`, writes `map.json`, and writes one reader prompt per two crops (never two takes of the same
  thing for one reader). Give each prompt to a fresh reader (a subagent) that sees only its images.
- Write `vision/isolation_v<TAG>.md`: each case, what was tested, what the readers said (quotes), which variant wins.
  Make the winners the defaults, bump `BUILDER_VERSION` in `assets/cast/build_cast.py` if the cast changed, then
  `python build_cast.py out<TAG>`; copy `lib<PREV>` to `lib<TAG>` minus the changed families' files (they re-render on
  demand); copy `gallery<PREV>` to `gallery<TAG>`, delete the changed variants and re-render them with
  `render_set.py out<TAG> gallery<TAG> <list.json> 16`; validate with `cd assets && python validate_assets.py cast/gallery<TAG>`
  and move the `validation_report.json` it writes out of the folder.

### 3. Placement changes: a new placement revision

- `scenegen/scene.py`: bump `PLACEMENT_REV`, add a header comment for the new revision (what the readers saw, what the
  rule does), and gate every new rule on `PLACEMENT_REV >= N` so older records still rebuild. Per-template rules live in
  `scenegen/templates.py`, planner rules in `scenegen/planner.py`.
- Point `scenegen/library.py` (`CAST_DIR`, `LIB_DIR`) at `out<TAG>`/`lib<TAG>` and bump `GENERATOR_VERSION` in
  `scenegen/planner.py`.

### 4. Design tests (whole scenes)

`tools/cycle/design_tests.py <WORK>/t<TAG> [park23405,...]` builds the test scenes listed in its `jobs` (edit them:
each forces the changed templates among others). Copy the pictures to `vision/design_tests_v<TAG>/test_N.png`, give each
to a fresh reader with `tools/cycle/prompts/reader_template.txt` (one picture), and write
`vision/design_tests_v<TAG>.md`. When a reading shows a new problem, add a rule, rebuild that scene and read it again
(round 2).

### 5. Calibrate, then build the set

```bash
python tools/cycle/calib_wrap.py      # -> <WORK>/calibration<TAG>.json
python tools/cycle/set_prior.py       # rewrites the PRIOR block in scenegen/planner.py
cp $TPDB_WORK/calibration$TAG.json calibration.json
bash tools/cycle/build_set.sh         # showcase pass into scenes<TAG>, then searches for missing tier 1-3 cells
bash tools/cycle/t4_search.sh street <previous street base seed> 400000   # one per tier-4 cell still missing
python tools/cycle/isos.py 0,1,2,3 isomorph_summary_a.json   # tier 2-3 isomorphs; ISO_X=1 or ISO_Y=1 try more seeds (edit GROUPS_X/Y)
python tools/cycle/iso_t4.py 6111,7111,8111,9111,10111      # the tier-4 isomorph
```

- The previous release's base seeds are in its `scenes/showcase_summary.json` (`base_seed`). Try those first for tier 4.
- Exactly one picture per (setting, tier) and five isomorphs. If two searches both add a cell, move the extra out.
- Merge the isomorph summaries into `scenes<TAG>/isomorph_summary.json`, then edit `OPEN` and `NOTES` in
  `tools/cycle/fix_summary.py` and run it.
- Look at every picture. Anything wrong: a new rule (record it in the revision's header comment and the README), then
  rebuild what it touches and check the other pictures still rebuild identically.

### 6. Probes, verification, library

```bash
python tools/cycle/probes.py 3          # probes<TAG>: every template in at least three screened pictures; must end "SHORT {}"
python tools/cycle/probes_fix.py NAME [seed]   # rebuild one probe with the same templates (SETTING=park to move it)
python tools/cycle/verify_all.py scenes<TAG>   # every record rebuilt and compared; writes <WORK>/variants_used.json
python tools/cycle/verify_probes.py probes<TAG>
python tools/cycle/prune_lib.py               # lib<TAG> keeps only the variants the set and probes use
cd assets && python validate_assets.py cast/lib<TAG>   # then move validation_report.json out of the library
python -m scenegen.combos --out combos.json
```

Look at every probe too. Then swap: `scenes -> scenes_v<PREV>`, `probes -> probes_v<PREV>`, `scenes<TAG> -> scenes`,
`probes<TAG> -> probes`.

### 7. The blind screen and the gate

```bash
python vision/prepare_screen.py scenes,probes vision/v<TAG>   # blind/pic_NN.png, keys.json, key_map.json
python tools/cycle/make_readers.py 9     # <WORK>/v<TAG>prompts/reader_1..9.txt (7-8 pictures each)
python tools/cycle/make_scorers.py       # scorer_a/b/c.txt and keys_a/b/c.json (three equal parts of the pictures)
```

- Give each reader prompt, verbatim, to a fresh reader (a subagent with no other context); it writes
  `vision/v<TAG>/desc_pic_NN.md`. When a scorer's pictures are all described, give it its scorer prompt; it writes
  `scores_<a|b|c>.json` and `scores_summary_<a|b|c>.md`. Readers and scorers must never see the code, the keys (readers)
  or the pictures (scorers).
- Merge `scores_a/b/c.json` into `vision/v<TAG>/scores.json`, then `bash tools/cycle/summarize.sh` and
  `python vision/gate.py vision/v<TAG> scenes,probes`.
- Write `vision/flaws_v<TAG>.md` (headline table, what the earlier list became, the gate table, the R rows and O rows for
  the next release), update `vision/limits.txt` (it fills the README's Known limits) and add the release's line to
  `vision/screen_prompts.md`.

### 8. Publish

- README: rewrite the fixed text of `tools/cycle/README.template.md`; copy
  `vision/readme_v0<PREV>_text.json` to `readme_v<TAG>_text.json` and rewrite its keys (intro, design, screen, redrawn,
  gate, inspection, calib, zip_mb); update the version strings in `vision/fill_readme.py`; run it.
- Showcase page: update `scenegen/site.py` (`PREV, CUR`, `REDRAWN_NOTES`, `WEAK_NOTES`, `SCREEN_NOTE`, `FIXES`) and
  `scenegen/site_template.html` (version strings, the screens list `VS`, the intro paragraph), then
  `python -m scenegen.site --scenes scenes --gallery assets/cast/gallery<TAG> --old-gallery assets/cast/gallery<PREV> --combos combos.json --screen vision/screen_summary.json --out site<TAG>`.
  `site<TAG>/index.html` is a whole document with a doctype, which the publishing route requires (since v0.31; before that the old route put the skeleton round it).
  Publish to the page (https://claude.ai/artifact/6affEGUfuZyCQNoguG5dnL, slug `2d310fee-c012-4eea-b09a-cd0405c4c225`) through the `claude-artifacts` tools: read `guide` topic `pages` first, take
  `base_version` from `get_artifact`, then `publish_files` with `files` as `{as, path}` and `remove` for what is gone, for the files that `python tools/cycle/site_patch.py site<PREV> site<TAG>` lists. A publish changes only the files it names.
  To compare with what is live, use `list_files`. The live page from v0.30 and before differs from `git archive`'s `index.html` by that skeleton.
- Spec doc ("TPDB Difficulty Model Spec", https://claude.ai/artifact/3fdacwmfKaN4YRePWLrddF): add a section after the
  previous release's "Legibility gate outcome" paragraph, in the same shape as the earlier ones, through the docs connector (`update` on the doc's node, engine `prose`, an `insert` after the last block). Its screen table carries every version's column, so copy the last one and add a column.
- `python tools/cycle/lf.py`, then `python3 package_release.py 0.XX --single` (it checks the zip file by file); set `zip_mb` in the text JSON to the size,
  refill the README and package again. Send the zip to Sam.
- GitHub (https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator-): the working folder is the clone. Work on a
  `v0.XX` branch; when the release is packaged, remove what the zip leaves out (`git rm` the previous `lib`, `out` and
  `gallery` folders; their files stay in history), squash onto `main` as one commit "TPDB v0.XX: scene generator, cast, set,
  probes, blind screens" with a short body, and push.

## Lessons

- Kill background jobs by PID (`ps | grep | awk | xargs kill`); `pkill -f <pattern>` can match and kill your own shell.
- Variant ids contain dots: strip the known suffix (`.mask.png`, `.json`, `.png`), never split on `.` (an early prune
  moved the whole library).
- Seed searches for one cell must stop when the cell exists (`search_open.py` does); otherwise two searches add two.
- Long jobs: run them in the background with a long timeout and check their logs; a tier-4 street search can need dozens
  of seeds of up to 40 casts each.
- A rule that changes where events go changes what the planner picks for every seed, so pictures from the last release
  rarely come back; the tier-4 cells sometimes do, on their old seed.
- Readers report oddities freely; a fix for one picture's reading must be read again in a whole scene before the set is
  built, and the scores are at the ceiling, so the screen is a filter for illegible drawing, not a measure of difficulty.
- Parallel bench runs need an output folder each: `isolation_bench.py` writes `<OUT>/_scenes/<name>.png`, the same seed gives
  the same name, and two runs into one folder crop each other's pictures. Look at every crop before giving it to a reader.
- Exact rebuilds depend on Pillow (`requirements.txt` pins it): Pillow 13 resamples RGBA differently from 12, and every
  embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical.
- Look at a new drawing yourself before spending readers on it; two of the first v0.24 candidates did not survive that. But trust the
  reading over the eye: the seesaw riders that looked best on the v0.24 bench read worst.
- Run two things in one message only if the second does not depend on the first: a broken `set_prior.py` and the set build went out
  together, and the build ran on stale priors. Stopping a background job can leave its children running on Windows, and a job that can't
  be stopped can be waited out: then delete what it wrote.
- `wave` needs someone to wave at, so it cannot be probed alone; force it with other events.
- `package_release.py` says nothing and keeps the old zip if one exists: delete it first, and check for "VERIFY OK". RUNBOOK.md ships in
  the zip, so edit it before the last packaging. Then extract the zip to a clean folder and rebuild a few records from there.
- The tier-4 searches take far less than hours on 12 threads: run one per cell side by side, then several per cell for the slow ones.
- Compare the oddity row with care: scorers differ in how much they log (`vision/flaws_v024.md`). The readers' remarks can be counted
  directly from `desc_pic_NN.md`, and a control reader on the previous release's pictures tells readers from pictures.
- From v0.25 the scorer prompt caps "unintended" at three per picture, so the logged row no longer compares across that line, and
  `summarize_screen.py` records the remarks row for every screen. Use `--add` (`summarize.sh` does), which keeps the earlier screens.
- When an object reads as something thin or small, look first at which way it faces: the bag and the roller both showed their narrow edge
  to a figure in profile, and turning them did what no amount of redrawing had.
- A template this release did not touch can still fall under the gate. Read what the readers wrote, and weigh it against the retest's
  five templates of variance, before calling it a regression or noise.
- Before packaging, run `python tools/cycle/check_quotes.py`: it looks for every quotation in the new prose in what the readers and
  scorers wrote. Then check each count against its file too, without `head` or a remembered number: v0.25's first draft said "5 in six"
  for three in six and two in seven, and took a count from the v0.24 screen as its own.
- Write Python patches with the Write tool, not a heredoc, which turned `\n` into real newlines. Keep a release's patches in `tpdb_work/`.
- A count of what readers wrote needs its negatives taken out. The remarks counter took "Nothing is floating ..." bullets for remarks, and a published
  11% rise was 5%. When a counter is fixed, recount every screen, say what the published figures were, and recheck anything derived from them (the v0.24 control went from 15% to 18%).
- A bench that reads one thing alone does not read it against its neighbours in the library. The fan of bristles was chosen with one reader's "broom or rake" on the
  table, and the heap of leaves gave it `rake`'s other cue: the screen's one misread. When a redraw adds a cue, read it beside the template that already has that cue.
- Writes to the exFAT drive fail now and then with `OSError 22`, and the file is intact: `tpdb_work/psub.py` retries.
- The tier-4 isomorph can take hundreds of tries (676 in v0.26): run several seed lists side by side from the start. `iso_t4.py` stops each as soon as one exists.
  Two lists can finish together: keep the one in `isomorph_summary.json` and move the other out.
- When a tier-4 cell has not come after a dozen seeds, force a template set that placed in an earlier release before running more (`forced` in `build_one`; the record keeps it, so it rebuilds exactly).
  Forced, the v0.24, v0.25 and v0.26 playground sets each placed within seconds where 219 free seeds had placed nothing: the difficulty is in the sets the planner draws, not the room. Say so in `fix_summary.py`.
  v0.32's street went the same way: 39 free seeds failed under revision 30, and v0.31's set, forced on v0.31's seed, placed in 12 s. Run two or three forced lists beside the free
  search (`tpdb_work/t4_forced32.py`); they can finish together, so move the extras out and keep the one whose picture reads best.
- A pose set at render time is overwritten when the renderer re-evaluates the action. To change a pose for one view, bake a twin action (`__p`, `Poser.build`), and let `render_assets.py` choose it.
- Parallel runs may render into one library. `Library.ensure` now renders aside into `.render_<pid>` and moves the files in with the manifest last; before that, two runs left "image file is truncated".
- Look closely at crops before drawing anything: the walkers' feet did point the right way, the hose did reach the fist, and what was wrong (the eye on the head's outline) was on nobody's list.
- When a release's helper scripts are made from the last release's by substitution, replace the bare version too (`0.32` as well as `v0.32` and `032`):
  v0.32's packaging script first called `package_release.py 0.31`, and only the packager's refusal to overwrite `tpdb_v0.31.zip` caught it. Grep the new scripts for the old number.
- Read the validator's last line every release. v0.31's library passed 338 of 350, the 12 split riders failing on their names alone, and no one wrote it down; v0.32 found it,
  widened the schema to the `~` suffix, and then found six pieces failing the ground rule that a far leg alone cannot meet. Either is a check that has stopped checking.
- When the gate's one failure is on a picture that came back identical, read the retest before redrawing. Two releases running (`jump` in v0.31, `blocked_hose` in v0.32) the
  failure was the retest's moves downward, on a picture whose items had full marks the time before. Bench it if the readers' words point at the drawing; otherwise watch.
- A bench win can fail to show in whole pictures. Shorter legs took the bench from eight remarks to three, on four cut-outs a side, and did not move the screen. `python vision/remark_topics.py vision/v<PREV> vision/v<TAG>` compares what two screens remark on, roughly; read the hits.
- `package_release.py` keeps a zip that is already there, so delete `tpdb_v<this release>.zip` to rebuild it, after looking at it, and never with a pattern. Earlier zips stay.
- Other apps can hold most of the memory (15 GB here): eight side-by-side runs ran Blender and cairo out of memory ("render failed", `MemoryError`). Keep it to about five, and fewer while a library is still filling. When a run dies of it, look at what else stopped, and rerun.
- To find out why something will not place, take the search's own filters off. Twelve rounds of testing one change at a time on the tier-4 playground told nothing, because each failure named whichever template came last. What told it was to try 226 random sets with `require_band=False`, keep the records of the five that placed, and read what they had in common, including their features and their content counts (`tools/cycle/try_sets.py`). Then the cause was a loop: short of the tier's things, plans went back for the fixtures that took the ground.
- Three rules that each do nothing can do it together. Test them singly and together, on the same seeds, and say which you did: `TIER4_MUST`, `TIER4_NO_SCENERY` and the railing's limit placed 0, 0 and 0 of 12, and 2 of 12 together. Say too when a picture's seed came from such a test.
- A fix can move a reading it was not aimed at. Shadows from the footprint took the remarks away, and the sleeping dog, not otherwise changed, fell under the gate, perhaps because a wide oval had been saying "lying down". When a template you did not draw falls, look at what you drew round it, then at whether the readers' words differ at all: on `ducks_bread` they did not, and the scorers did.
- A shadow drawn at the ground point can vanish under a body that reaches below it. Look at a whole sheet of poses, not one, before spending readers. The same look stopped a ball with two bands that looked like a target.
- `probes.py` tries templates in crowded groups, the garden first, and gives up after three failures. When it ends SHORT, force the short ones in small groups in a setting that suits them, with `build_one(..., forced=..., require_band=False)`, and mark each record `"probe": true`.
- After the set is built, any later change to shared drawing means rebuilding every record, not only new ones: `tools/cycle/rebuild_set.py` does it in place, the pictures before the isomorphs that read them. Refresh `isomorph_summary.json` from the records afterwards, and run `fix_summary.py` before the folder swap, as it reads `scenes<TAG>`.
- A rule can have a cliff. The ladder's margin from a lamp at 240 or 200 units placed none of 8 seeds, in every combination tried, and at 160 it placed 7 or 8. Try a new rule on a few seeds at several values before the set, not after a search has failed.
- Count what a drawing costs in placement as well as what it buys in reading. The trip's long box took its meaning item from 0.75 to 1.00, and the tier-4 cells from 80 failed seeds to 166, the trip being what those failures name most. And look at where the pictures that passed came from: its five were all street pictures.
- A full gate is not the end of the reading. v0.20 and v0.23 also read 64 of 64, and the next screens read 61 and 63. Read what full marks rest on: the unsure sections, and any rule a scorer writes down (v0.29's scorer c listed 18 hedged credits). Compare it with how the last screen's scorers marked the same kind of sentence before saying the drawing did it or the scorers did.
- A hit in `remark_topics.py` is not yet a remark on the topic: v0.29's "hose's bulge" held a skirt that bulges, and "feet overlapping" a bird on a lamp. Read the hits before writing a row, and check a superlative against every earlier `gate.json` before writing it.
- A figure's prop and a drawn line need a joint, and a joint is a drawing like any other. The hose in the fist belongs to the figure and the hose on the ground to the scene. A butt-capped piece over the join hid the gap and read as a sleeve, in one picture of three. It went from the bench to the set unread on its own, and that is why the screen found it. Give the last change a bench round too.
- A bench can test a thing and find nothing. The lifted heel, read two ways, had nothing to choose between them, and keeping it saved re-rendering every walker. Write that down as a result.
- Do not chain `;` after a command that can fail with `OSError 22` on this drive: `tpdb_work/psub.py` for patches, which retries and is safe to re-run, and `cd ... || exit 1` in scripts. One patch stopped midway and the commands after it ran from the wrong folder.
- Count again before writing "all" or "two of four". Three counts in this release's bench and design notes were wrong on first writing, and one reached a status message: the trip is in three of six design tests, not four. Recount from the files, by script where you can.
- A release that changes little leaves most of the set identical to the pixel, and then the screen is a retest as well. Compare with `git`-free hashes (`tpdb_work/retest30.py` did it): v0.30's 19 identical pictures gave 223 of 230 items the same, and showed a half mark and a keyword row to be noise. Do this whenever pictures come back, and do not read a move on such a picture as anything but the readers.
- A test with `require_band=False` does not test the search. Forced that way, every width of the box placed 40 of 40 and 24 of 24, and that says nothing about what fails with the band on. It told me that only after the run.
- Look at a release's scripts before running them, above all one that deletes. A `sed` from `t028` to `t029` turned `out028` into `out029`, and `finish_tree` would have removed this release's cast. The script now checks the folders it keeps. Likewise a patch that matches a line by a substring can land on a longer line with more indent: anchor it on the newline.
- A side test running beside a build shares its library. A variant rendered on demand by two runs at once kept one run's image and the other's manifest, and validation caught `sha256 mismatch` on one goat. The picture was right and only the hash stale. Validate after pruning, as the runbook says, and read a failure there before going on.
- A bench's switches need setting for the new names as well as the new drawings: the flags in `isolation_bench.py` go by name prefix, and new cases took the old obstacle and the old duck. A mirrored figure swaps its hands' anchors, so choose a fist by what it is near. Look at every crop before spending readers: that caught all three.
- "A larger job" is a claim, so price it. A rider cut in two was left in v0.27 for being one, and stayed on the list for four releases. It took a mask by bone weights at render time, a pose name with `~near` or `~far` and no change to the cast. Frame the camera before cutting, so that the pieces register.
- A fix can have two halves, and either alone reads as nothing. Drawing the far leg behind the plank read no better, and raising the riders read worse in v0.24. Together the children sit on the plank. And look at what an old decision rested on: v0.24's rested on one cut-out each.
- What a figure draws that is not an object goes in with role `background`. As `setting`, the far leg entered the object count and the final checks, every layout failed, and a bench's forty-seed loop ran for eleven minutes saying nothing. When a bench case runs long, dump the stack (`tpdb_work/dbg31.py`, `faulthandler`) and do not wait.
- Moving a thing off one neighbour can land it on another. The reel, 24 units off the flower bed, "overlaps the step slightly". Read the second neighbour too.
- Look at a file's keys before merging it. `isomorph_summary.json` is keyed `A` and `B`, and a merge by `name` kept the first file and dropped the tier-4 entry, without a word. Print what came out, and count it.
- Stop when a remark has outlived every drawing. "Stiff" has been said of every hose held at the waist since v0.25 and costs no marks, and a seventh curve would not end it. Say so, and take it off the list.
  The seesaw man went the same way in v0.32: turned away, or both legs behind the plank, and every reader of each still doubted his seat (legs out was set aside on looking).
- A remark can be about the thing next to it. "Hovering slightly" was said of the girl raised onto the plank, and lowering her found nothing on the bench; what
  the readers said instead, 7 times in 15, was that her fists sat above the handle, which the raise had left where it was. Raising the handle with her ended it. Read
  every line a cut-out draws, not only the ones about the case.
- A bench's switches are module values, and one process runs many cases. `isolation_bench.py` set each by name prefix with a default for names that matched none,
  and many defaults were older drawings, so new cases would have drawn v0.30's seesaw. It now restores the release's value of every switch before each case.
  When adding a switch, check what a case that does not name it gets. And never cut the old cases to make room: the v0.32 patch first dropped every case since v0.23.
- A bench case's name must be new. v0.32 named three cases `ridO_1` to `_3`, as v0.31 had, and when v0.31's cases were put back further down the dict, the
  later entries won without a word: the file as committed ran v0.31's cases under v0.32's names. v0.33 renamed v0.31's (`ridO31_1` to `_3`), and the bench
  now refuses a name used twice. Look at a round's cut-outs before trusting its write-up: v0.32's round 1 had run before the cases were put back, and its
  pictures were v0.32's own.
- A template's exclusive tags are claims, not features. Revision 31 asked whether the wind was drawn by asking whether any template claimed `wind`,
  and the kite, a thing stuck in a tree, the storm pointer and the floating box claim it only to keep away from the wind template; so it also kept a hose
  out of pictures with no wind. To ask what is drawn, ask for the template that draws it (`templates._windy`, revision 32), and keep the old test for the
  old revision so its records rebuild.
- When readers take a figure for someone else, try the head before the clothes. The woman in yellow, seated, was "a child" and "a boy"; a dress drawn
  across her lap changed none of it, and long hair changed every reading.
- A second reading can be a reason, not an aim. The storm pointer's washing was kept out of her cone in v0.34, and a reader still offered it, "to bring it in":
  what the rain will soak, not what the arm points at. Before widening a rule, read why the reader gave the other thing.
- One reader can empty a row. v0.34's ninth reader named nothing in the sky, and seven of the screen's eleven items under full marks are its clouds.
  Look at who wrote a run of misses before taking it for the pictures.
- A change can undo an old fix next to it. v0.35 widened the swing frame on both sides for the swung seat, and the first design test found its leg on
  the path, which v0.15 had moved it off. Before widening or moving a setting element, read the comments on it and on what stands beside it.
- Change a shared setting element from the template that needs it. Drawn wider for every swing set, the frame left an empty seat off the middle of its
  beam and moved the tier-4 garden round it; redrawn by the swing template when it swings a child (`settings.swing_frame`), the set came back identical.
- A figure turned in the picture must be turned in every check too: its box, its anchors and its mask (`library.Placed.rot`; `compose.asset_mask`
  draws a turned figure through its SVG). Keep the unturned path byte for byte, so older records rebuild.
- A spec is not a drawing. The grandfather's spec has given him a moustache since the cast's first build, and no render ever showed it: every expression
  hides each face part it does not name (`face.py`), and none named it. Before reasoning from what a character is meant to wear, look at a render of it.
- A cue that reads in one pose can misread in another. The bold moustache said the grandfather's age under the bucket, at three-quarters, and in profile
  stood out from his face like "something held in his mouth"; read a cast change in every view the character is drawn in, the profiles above all.
- A rule about a drawn thing must measure the drawing. Revision 34 kept the gate's knob 16 px off a box drawn round the face's eyes and mouth; the sweeper it
  was written for stands in profile, his face turned from the gate, and the back of his hair still covered the knob, 8 px past the box. His picture came back
  identical and read as a bun a third time. Rebuild the picture that asked for a rule, and look at it, before the design tests.
- Taking a thing out of a picture moves what is left. With the washing off the line, the storm pointer placed beside the fork sweeper and stood on his
  dustpan, which no rule keeps feet off. Look at every picture a rule changed, not only at the thing the rule is about.
- A cue added for one reading can outlive its need. The stuck rider's kick arcs went in at v0.16, when readers of her without them saw nothing wrong; by
  v0.32 she called out and held a raised handle, the arcs drew "hovering slightly above the plank", and without them every bench reader had her stuck.
  Bench the cue's absence as a case of its own.
- A gate written in a class body (`sky = "clear" if PLACEMENT_REV >= 30 else None`) is read when the module is imported, not when a record is rebuilt, so it changes
  what an older revision's records rebuild into: two of three v0.31 records did not rebuild under v0.32's code, a hose under storm clouds and a street with a
  watering can under a clear sky (its planner samples sets under both skies); with the watering templates' sky put back, the street rebuilt identical to the pixel. Records rebuild
  exactly with their own release's package, which is what the standing rule promises. A rule that must leave old records alone goes in `place()` or `feasible()`.
- Rebuilding the picture a rule is for shows what the rule moves as well as whether it works. v0.37 rebuilt v0.36's picture 63 with the knob and dustpan rules
  alone, and the storm pointer, off the dustpan, now pointed up through the left post of the empty line, which no reader had yet been shown. The line came out
  of her garden before any reader saw the picture (`tpdb_work/rb37_73.py` rebuilds a probe from its record's own `regen`).
- Read the comment on a thing before leaving it half drawn. Revision 34 left the washing line empty under a storm pointer, and the planner, where it hangs washing
  on every line it draws, says why: "an empty line reads as a bare wire". The reader of her picture offered the empty line as what she pointed
  at. Revision 19 also shows the way out: it drops the line, posts and all, in the planner (revision 35 does the same for the storm pointer).
- A filler slot at the picture's edge is moved in by revision 15 until it shows whole, so where it is drawn is not where the slot says. The street's spare crate,
  set at x 1560, was drawn 30 px further in, its lid at the foot of the fruit stall's leg. Look at where a filler is drawn (its element's `bbox` in the record) before moving it.
- Before drawing a new thing, look for one already drawn. The garden has had a laundry basket since v0.4, a filler no v0.37 picture drew, and older readers had
  named it at once; v0.38's fix for the washing was that basket set at the hanger's feet. `grep` the readers' descriptions for the thing a reading lacks, too:
  "there is no laundry basket to show which" had been written in three screens.
- A second cue can tell a story of its own. The drops said the shirt was wet, and so being hung out; under it, the basket's clothes with no drop on them read dry,
  and a design test read "the dry laundry may be about to get wet". The fix was to make the story whole (everything on the line and in the basket wet), not to
  move the basket: kept from under the shirt, it had room only where the planter kneels, and the washing and a planter placed 3 of 12 where they had placed 12.
  Price a move in placement before taking it (`tpdb_work/bcost38.py` runs a forced set on twelve seeds with a switch either way).
- Trace a placement over all its tries. `build_one` tries several seeds, and the first can fail on its cast before reaching the rule (the first trace of the basket
  saw a woman too short to reach the line and nothing else); `max_tries=1` traced the wrong thing.
- A planner rule changes more than the pictures it is about. A plan re-picked in one try moves the rest of that seed's plans, and a plan changed in one try
  changes the template usage the next try plans with: keeping a perched bird from a storm pointer, re-picked, cost two set cells that show neither, and
  dropped from the plan in every setting it still cost one. Write the rule where it must fire (the garden, for the fence), and rebuild every record of the set
  before building on it (`verify_all.py` on a copy of the folder).
- A clean screen can rest on its scorers. v0.38's two scorers listed 23 full marks given to readings the reader hedged; halved, 58 of 64 templates passed, not
  64. Count them (`tpdb_work/strict38.py`) and check them against the last screen's scorers on the identical pictures before calling a template fixed.
- A clamp on a baked mesh acts on the rest pose, not the picture. The hoodie's hem was flattened below the waist, and at rest an adult's wrists hang at 0.785,
  under the hem: every long sleeve was cut off at the hem's height, and the kicker's hands floated. The people sheet had it too, unseen. Before clamping, list
  what lies past the clamp at rest (`flatten_below(..., spare=...)` keeps the vertices weighted to the named bones), and look at each bench crop at full size.
- Bench a whole cast round as two: v0.38's cast against every switch on, two cut-outs to a reader, then the losers taken back and read once more on the same
  seeds. A switch can lose for its neighbour: the belt band read as "a hoop or rubber ring" because the tucked tee above it was narrower than the waistband,
  and with the tee untucked v0.38's belt drew nothing. Twenty-two readers read round 1 in about a minute each, side by side.
- A colour edge on an animal is a line readers cut along. White legs under a brown goat read as "a sack or saddle blanket draped over a white animal"; brown
  legs moved the edge to the neck, and the white head became "a separate white ball or egg with horns", the name going from goat to "goat, antelope or deer".
  Put a coat's edge where the animal's own parts would carry it (a face blaze on a head of the body's colour, socks below the knee), and read it at 45 and 135,
  where the neck hides.
- An angle in a table is not an angle drawn: count what places. Revision 37 drew the dog walked on a lead at 45 half the time, and at 45 the lead from the
  walker's hand crossed the dog's back at every spot (1893 lead curves in 12 probes, none clear), so every such try failed and the planner moved on, and the
  set and probes held the walk only at 90. The probes stratified by angle (`tpdb_work/probe_angle39.py`) found it. Before the screen, count each
  (template, angle) in the records; one that never places is dropped by drawing it at another angle with the draw kept (`templates.UNPLACED`), so the records
  that drew the other angles rebuild as they were.
- A bench cast rebuilt in part is two casts. v0.40's first N cast was built, then the reach was redrawn and three people rebuilt, and the bench's
  windy-hat cut-outs of Ana still had the first reach, across her face. After any pose change, build the bench cast whole again, and run every case
  of it again into a fresh library.
- `render_set.py` skips a variant whose files exist. A library or gallery carried from the last release keeps its old renders of a redrawn pose
  unless those files are deleted first (v0.40's goat graze came through unchanged, by an anchored pattern that matched nothing). After rendering,
  compare a file of each redrawn variant against the last release's.
- A reader can describe the wrong picture. v0.40's reader 7 wrote picture 56's park under picture 55's name, and the scorer found it: eleven items of 15 at
  0, and the next description saying the two "look identical". Check the blind files are distinct (they were), set the wrong description aside, and read the
  picture again with a fresh reader and score it with a fresh scorer, each with the screen's own prompt cut to the one picture; drop any oddity the mix-up
  left on its neighbour.
- A pose's head aims a check. v0.41's leaning begging dog, its head tipped up 18 or 20 degrees, placed on none of 40 street seeds at 45, where v0.40's placed on the
  first: its gaze ray (`library.looks_at`) passed under the eater's food. Run every new pose's cases at every angle its template draws before the readers, and when
  one fails every seed, count which check says no (wrap `Scene.gaze_ok` and `Scene.fits` and count their answers) instead of reading the failure's last line.
- Read what every variant on the bench shares, the old one too. Round 1 of v0.41 read two new begs beside v0.40's, and the remark on all of them was the forelegs
  held out level, "like stiff rods", which neither new drawing touched. Round 2 folded the forelegs on v0.40's body and won; a choice among the round-1 variants
  would have taken a lean that bought nothing.
- A remark can go as it came. The heaps' brown leaves under green trees drew remarks in five v0.40 pictures and in none of v0.41's 93, with the heap unchanged, and
  the bench's v0.40 cases drew none either; the bench's turning trees drew fruit. Before redrawing for a remark, count it on the pictures that came back unchanged,
  and bench the old drawing beside the new.
