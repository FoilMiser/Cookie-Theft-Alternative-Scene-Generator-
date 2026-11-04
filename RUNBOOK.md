# TPDB release runbook

How each release from v0.12 to v0.27 was made, written so that a fresh session can make the next one (v0.28) from this
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
  Patch the published page (https://claude.ai/artifact/6affEGUfuZyCQNoguG5dnL) with the files that
  `python tools/cycle/site_patch.py site<PREV> site<TAG>` lists, after reading its current version.
- Spec doc ("TPDB Difficulty Model Spec", https://claude.ai/artifact/3fdacwmfKaN4YRePWLrddF): add a section after the
  previous release's "Legibility gate outcome" paragraph, in the same shape as the earlier ones.
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
- A pose set at render time is overwritten when the renderer re-evaluates the action. To change a pose for one view, bake a twin action (`__p`, `Poser.build`), and let `render_assets.py` choose it.
- Parallel runs may render into one library. `Library.ensure` now renders aside into `.render_<pid>` and moves the files in with the manifest last; before that, two runs left "image file is truncated".
- Look closely at crops before drawing anything: the walkers' feet did point the right way, the hose did reach the fist, and what was wrong (the eye on the head's outline) was on nobody's list.
- A bench win can fail to show in whole pictures. Shorter legs took the bench from eight remarks to three, on four cut-outs a side, and did not move the screen. `python vision/remark_topics.py vision/v<PREV> vision/v<TAG>` compares what two screens remark on, roughly; read the hits.
- `package_release.py` keeps a zip that is already there, so delete `tpdb_v<this release>.zip` to rebuild it, after looking at it, and never with a pattern. Earlier zips stay.
