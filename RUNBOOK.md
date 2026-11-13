# TPDB release runbook

How each release from v0.12 to v0.53 was made, written so that a fresh session can make the next one (v0.54) from this
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
- When the brief is about how a figure looks (v0.48 the faces, v0.49 the head), judge the drawing before any event: trials of one family built
  alone and rendered at 800 px per metre (`TPDB_PPM`), sheets of heads with a row at scene size under them, and blind reviewers who compare two
  drawings at a time, each pairing in both orders. A sheet of more than two rows is ranked by a row's place (Lessons, v0.49).
  `python tools/cycle/fig_pairs.py ROUND A_DIR B_DIR A_NAME B_NAME [SETS.json]` makes the sheets of such a bench from two folders of renders (v0.52's own, with its
  six sets of four views and its prompt written in: edit them): each set twice, one drawing above and then the other, the map outside the folder; and
  `fig_pairs_tally.py ROUND` counts the choices by set and order. A set whose choice follows the row in every round is a toss-up (Lessons, v0.52).
- After any change to the body's hull, build with `TPDB_HULLCHECK=1` and compare each family's vertex count with the last build's; then look at every
  figure standing at four angles. The hull can break at the shoulders for one figure of ten (Lessons, v0.52).
- A cast that changes every figure is read in whole scenes as well: `tools/cycle/who_build.py ARM pic,pic` builds the last screen's pictures again from their own
  records with a trial cast (v0.52's own, its arms and paths written in), and `age_scenes.py prepare` and `tally` deal and count them.
- A drawing of the scene and a trial cast can share one bench in whole scenes (v0.53): `tools/cycle/bench_build.py ARM pic,pic` builds the last screen's pictures
  again with a scene switch made to act at the records' own revision (`templates.WHEEL53_REV`) or with a trial cast; `bench_prepare.py` deals both questions to one set
  of readers, a reader's two pictures of the scene's thing both of one arm; `bench_tally.py` counts who a figure is called and where a thing is named. Count the last
  screen by reader before building a bench for a naming fault, and look at a trial figure large first (Lessons, v0.53).
- `python tools/cycle/crops.py OUT.png [SCALE] NAME:substr[:pad] ...` cuts named elements out of built pictures onto one sheet (`CROP_DIRS` for other folders):
  the flagged pictures of the last screen at full size, before anything is drawn.
- The age bench, whenever heads, proportions or marks of age change, reads whole scenes (v0.50). Build each trial cast into its own folder
  (`TPDB_AGE50=M python build_cast.py <WORK>/age/out_M`), give each a library that starts as a copy of the last one minus the changed
  families, and build the picked pictures of the last screen again from their own records with it (`G.regenerate(lib, record, out)`:
  the same seed and the same forced set). Then `python tools/cycle/age_scenes.py prepare vision/isolation_v<TAG>/who <WORK>/maps/who_map.json
  <picks.json> O=scenes,probes M=<folder> ...` deals the pictures to readers, eight each, two of every cast and no picture
  twice, with the screen's own reader prompt, and `age_scenes.py tally <out> <map>` counts by `who_cmp.py`'s rule how each grown figure
  was called. The first arm is the last release's own pictures: it must show the fault the screen showed, or the bench measures nothing.
  The cut-out bench of v0.48 and v0.49 (`age_bench.py`, `age_tally.py`: strips of four small figures) sits at its ceiling and is kept
  only for what a reader names on a face.
- When the screen's fault is a reading of who does what to whom, bench it in the pictures that failed (v0.51, the game of catch). `tools/cycle/ws_build.py ARM pic,pic`
  builds the last screen's pictures again from their own records with a trial cast and, for one arm, a scene switch made to act at the record's own revision
  (`templates.CATCH51_REV`); `ws_prepare.py` deals the arms to readers with the screen's own prompt, the map kept outside the folder; `ws_tally.py catch` prints by arm
  every sentence on the event. The three are v0.51's own, with its picks, arms and paths written in: edit them. Give a reader one picture of a pair of people, or count
  by reader as well as by arm: a reader who has two pictures of the same people carries the reading from one to the other (Lessons, v0.51).
- `python tools/cycle/qcheck.py <doc.md> [folders]` looks up every quotation of a document in the readers' own files while it is being written.
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
python tools/cycle/calib_cmp.py $TPDB_WORK/calibration$PREV.json $TPDB_WORK/calibration$TAG.json   # what moved by 0.002 or more, the README's count
python tools/cycle/set_prior.py       # rewrites the PRIOR block in scenegen/planner.py
cp $TPDB_WORK/calibration$TAG.json calibration.json
bash tools/cycle/build_set.sh         # showcase pass into scenes<TAG>, then searches for missing tier 1-3 cells
bash tools/cycle/t4_search.sh street <previous street base seed> 400000   # one per tier-4 cell still missing
python tools/cycle/yield_set.py 6 playground 6043 3 '<forced set as JSON>'   # does a forced set place and land in the band? (seconds)
python tools/cycle/forced_cell.py street 4 v047street 430752,447752        # a cell from a forced set, when the free search has failed
python tools/cycle/isos.py 0,1,2,3 isomorph_summary_a.json   # tier 2-3 isomorphs; ISO_X=1 or ISO_Y=1 try more seeds (edit GROUPS_X/Y)
python tools/cycle/iso_t4.py 6111,7111,8111,9111,10111      # the tier-4 isomorph
python tools/cycle/iso_t4_wide.py 164111,38111,94111,...    # when that finds none: only the pairs that can build (edit `pairs`), last release's seed first
python tools/cycle/merge_iso.py                             # the part summaries into scenes<TAG>/isomorph_summary.json, each entry checked
TPDB_EDGE49=O python tools/cycle/iso_one.py T4_park_s728923 street 164111 $TPDB_WORK/iso_o   # one isomorph call with a switch off: is a new rule what stops a search?
```

- The previous release's base seeds are in its `scenes/showcase_summary.json` (`base_seed`). Try those first for tier 4.
- Exactly one picture per (setting, tier) and five isomorphs. If two searches both add a cell, move the extra out.
- Merge the isomorph summaries into `scenes<TAG>/isomorph_summary.json`, then edit `OPEN`, `FORCED` and `NOTES` in
  `tools/cycle/fix_summary.py` and run it. `FORCED` is the cells built from a forced set; each needs its reason in `NOTES`
  and its set, with the history, in `forced_cell.py`'s `SETS`.
- Look at every picture. Anything wrong: a new rule (record it in the revision's header comment and the README), then
  rebuild what it touches and check the other pictures still rebuild identically.

### 6. Probes, verification, library

```bash
python tools/cycle/probes.py 3          # probes<TAG>: every template in at least three screened pictures; must end "SHORT {}"
python tools/cycle/probes_fix.py NAME [seed]   # rebuild one probe with the same templates (SETTING=park to move it)
python tools/cycle/probe_angle.py 2     # every angle an animal template is drawn at in at least two screened pictures; must end "SHORT {}"
python tools/cycle/more_probes.py       # the templates probes.py gave up, forced in small groups (edit GROUPS and NEED_T); must end "SHORT {}"
python tools/cycle/extra_probes.py 51700 garden:square_wheel,sprinkler_package,rake park:square_wheel,fly_kite   # probes forced whatever the counts say: a carrier
                                        # the passes cannot count (the wheelbarrow, where three square wheels of four were bicycles)
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
python tools/cycle/make_readers.py 11    # <WORK>/v<TAG>prompts/reader_1..11.txt (7-8 pictures each: pictures / 8, rounded up)
python tools/cycle/make_scorers.py 1-22,23-44,45-66,67-87   # scorer_a..d.txt and keys_a..d.json (four near-equal parts; no ranges gives three)
```

- Give each reader prompt, verbatim, to a fresh reader (a subagent with no other context); it writes
  `vision/v<TAG>/desc_pic_NN.md`. When a scorer's pictures are all described, give it its scorer prompt; it writes
  `scores_<a|b|c>.json` and `scores_summary_<a|b|c>.md`. Readers and scorers must never see the code, the keys (readers)
  or the pictures (scorers).
- Merge `scores_a/b/c.json` into `vision/v<TAG>/scores.json`, then `bash tools/cycle/summarize.sh` and
  `python vision/gate.py vision/v<TAG> scenes,probes`.
- Then the three counts beside the gate: `python tools/cycle/gate_yaw.py vision/v<TAG> scenes,probes` (the gate per template and angle, and the
  animal oddities by angle); `python tools/cycle/strict_count.py` (fill its two lists from the scorers' judgement calls first); and
  `python tools/cycle/who_called.py person.ana purple` for each grown figure (what the readers called it: a woman or a girl, a man or a boy), and
  `python tools/cycle/who_cmp.py` for the count of the four grown figures called young first, this screen beside the last by one rule.
- Write `vision/flaws_v<TAG>.md` (headline table, what the earlier list became, the gate table, the R rows and O rows for
  the next release), update `vision/limits.txt` (it fills the README's Known limits) and add the release's line to
  `vision/screen_prompts.md`.

### 8. Publish

- README: rewrite the fixed text of `tools/cycle/README.template.md`; copy
  `vision/readme_v0<PREV>_text.json` to `readme_v<TAG>_text.json` and rewrite its keys (intro, design, screen, redrawn,
  gate, inspection, calib, zip_mb); update the version strings in `vision/fill_readme.py`; run it.
- Showcase page: update `scenegen/site.py` (`PREV, CUR`, `REDRAWN_NOTES`, `WEAK_NOTES`, `SCREEN_NOTE`, `FIXES`; the next list is every
  template under 0.9 and, from v0.47, every one that fails the gate) and
  `scenegen/site_template.html` (version strings, the screens list `VS`, the intro paragraph), then
  `python -m scenegen.site --scenes scenes --gallery assets/cast/gallery<TAG> --old-gallery assets/cast/gallery<PREV> --combos combos.json --screen vision/screen_summary.json --out site<TAG>`.
  `site<TAG>/index.html` is a whole document with a doctype, which the publishing route requires (since v0.31; before that the old route put the skeleton round it).
  Publish to the page (https://claude.ai/artifact/6affEGUfuZyCQNoguG5dnL, slug `2d310fee-c012-4eea-b09a-cd0405c4c225`) through the `claude-artifacts` tools: read `guide` topic `pages` first, take
  `base_version` from `get_artifact`, then `publish_files` with `files` as `{as, path}` and `remove` for what is gone, for the files that `python tools/cycle/site_patch.py site<PREV> site<TAG>` lists. A publish changes only the files it names.
  To compare with what is live, use `list_files`. The live page from v0.30 and before differs from `git archive`'s `index.html` by that skeleton.
- Spec doc ("TPDB Difficulty Model Spec", https://claude.ai/artifact/3fdacwmfKaN4YRePWLrddF): two tabs since v0.48. The first,
  "Spec and current release", holds the spec, a paragraph that points to the second tab, the sections of the releases from v0.48 on,
  then "Open decisions" and "References". The second, "Release history, v0.5 to v0.47", holds the older sections and is close to the
  service's limit of 20,000 blocks a tab, so nothing is added to it. Add the new release's section to the first tab, after the last
  paragraph of the previous release's section and in the same shape, through the docs connector (`update` on that tab's body node,
  engine `prose`, an `insert` after that block). Its screen table has the last five screens only; the columns from v0.4 are in the
  table of the v0.47 section, in the history tab. The tools do not move blocks between tabs: a tab's content is sent inline, and
  `export` gives a tab back as markdown to check it against.
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
  search (`tools/cycle/forced_cell.py`, from v0.47; v0.32's was a scratch file); they can finish together, so move the extras out and keep the one whose picture reads best.
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
- `isolation_bench.py` runs every case when it is given none. v0.42's first bench script picked its cases with `re.findall` on a pattern with groups, which returns
  tuples; the picker failed, the lists came back empty, and four runs set off through every case since v0.23 before they were stopped. A script that starts the
  bench now refuses an empty list (`tpdb_work/bench42_run.sh`).
- Read what a count counts before acting on it. `probes.py` ended `SHORT {'windy_hat': 1}`, the number of pictures it had, and it was read as one short: one probe
  was added where two were needed, and the screen started with `windy_hat` in two pictures.
- A rule made after the screen moves more than its target. Keeping the square wheel off the stall changed one isomorph, and with it went the fourth picture of
  `about_to_trip`, which then fell under the gate, and the third of `balloon` and `wave`. After such a rule, rebuild, count every template's pictures again, and
  replace what the change took before reading the changed picture again.
- Run the validator on a bench winner's renders before choosing it. The begging dog's rump, lower than v0.41's, failed the ground check after the bench, and the pose
  went into the set 4 cm higher than the readers had read it.
- A bench crop must show the thing at a size a reader can judge. Round 1 cut the dogs at 45 out with their whole template, the hose and the man, and nothing was said
  of their chests or legs either way; round 2 cut out the dog alone (`crop` on its element). And a redraw can trade one remark for another: the reading dog's
  shorter trunk took the "person" away and left its paper "standing upright on its own", the paws reaching less of it. When a pose changes, look at what it holds.
- A bench win can lose in whole pictures, and the cut-out is why. The reading dog lying over a paper on the ground read as reading in three of three cut-outs and in
  both design tests, and in the screen, small among other events, as a dog "lying on an open newspaper", pawing at it or tearing it, in all five pictures, with the
  screen's one misread. Read a pose that changes what a thing is doing in whole pictures before choosing it, at the size the set draws it, and a thing laid flat under
  an animal as something it may lie on.
- A head's pitch on a tipped trunk is not the angle it shows. On the begging dog's upright trunk, head pitches of 38, 22 and 12 drew nearly the same nose; only 0
  lowered it. And the lowered head placed on none of 12 seeds at 45, the gaze check counting 2772 refusals and no pass in four: at three-quarters it faced the
  viewer. Look at the renders of every value before tuning, and price the pose at every angle its template draws (`tpdb_work/place43.py` counts each check's answers).
- A rule priced in two settings can still fail in a third, or seem to. The stalking cat in profile with a gap before its bird placed 12 of 12 in the garden and the
  park, and the tier-3 playground then failed 13 base seeds, most failures naming the cat; priced in the playground's own sets, the rule changed nothing, and two
  fresh seed lists placed the cell at once. Price a rule in every setting its template draws, and read a failure log's last template as a symptom.
- A stopped job can leave a render folder in the release library. The calibration stopped by PID left `.render_6572` in `lib043`, and `prune_lib.py` reported it
  as `UNKNOWN`. Read the prune's report, look inside such a folder, and delete it before the library is validated and packaged.
- `psub.sub` cannot delete: it skips a pair whose replacement is already in the file, and a deletion's replacement is always inside the text it replaces. Delete
  with a plain replace, or keep a word of context that changes.
- A rule written for one clash can make another. The props' colour rule (`TPDB_PROP44`) turned a pink scoop cream wherever pink was near a garment's hue: pale on pale
  skin, the man in red's cone tip read as "a moustache or a chocolate smear" in two design tests, and the girl in pink's ice cream as "something small and white" in
  the screen. Check a recoloured prop against the skin and the face it sits by, and read it where the rule fires, not only where it fixes.
- A post-screen fix is a guess until it is read. The scoop put back to pink, the three pictures rebuilt and read again did no better (two half marks and a misread,
  where the first read gave three half marks): the cone was too small, not the wrong colour. Before fixing after a screen, ask what else the misreads share (here one
  child, one pose, at one size), and when the re-read comes back, report it as it is.
- Measure what a pose leaves room for before writing the scene's part of it. The reading dog's paws raised to chest height stood 126 render px above the ground (0.472
  scene px a render px at sz 1), room for a paper 0.73 times v0.42's, so the paper placed on no seed; at eye level the tan dog's left room for 1.1, the white dog's for
  0.83. Read the anchors of the render (`paw_FL`, `paw_FR`) against the ground point first. And fold every fit check into the size loop: the tilt, checked after the
  loop had chosen a size, refused every spot.
- A switch the bench sets at run time is invisible to anything read at import. A template's `exclusive` is a class attribute the planner reads, and an exclusive that
  depends on a switch must be computed when the planner asks (`templates._Ex44`, a descriptor), or the bench plans with the release's value.
- `G.regenerate` writes a probe's record without its `probe` flag, which `probes.py` adds; `summarize_screen.py` then counts the probe as a set picture (24 pictures, 317
  items, where the set is 21 and 286). After regenerating a probe, put `"probe": true` back, in its place and in the generator's format (`indent=1`, no final newline),
  and verify. And `isos.py`'s alternative lists (`ISO_X`, `ISO_Y`) are one group each, which stops at its first success: to search one source alone, call
  `build_isomorph` for it (`tpdb_work/iso44b.py`).
- Readers say what they see, and seldom what is missing. v0.45's list came half from `flaws_v044.md` and half from four reviewers who were shown v0.44's pictures and
  cut-outs and asked what was wrong with the drawing, each with a share of its own (`tpdb_work/review45/`). They named what the readers had not: a duck standing on the
  water, a picnic with no food, a hose inspector looking away from the viewer (a sign error in v0.44's pose), a box the fence's colour. Take what two or more name.
- An oddity two readers name unprompted is a work item, not a watch item. v0.44's readers twice called the reading dog's paper "floating"; it "looked fine" to the builder
  in four pictures and was left on the watch list, and in v0.45 one reader's paper "up in the air" was a misread and failed the gate at the first count.
- A scored thing drawn behind a figure may lose at most 20% of its area. The fix drew the paper under the dog's paws: at 20 and 10 px the paws hid 25% and the garden
  isomorph could not be built; at 12 and 6 they hide 17 to 18%. A record's box, occlusion and salience come from the rendering, so before calling a change "drawing only",
  run `finalize`'s checks on every picture it touches and calibrate the one template with the switch off and on (`calibrate.py --only`); if the numbers are the shipped
  ones, the calibration and the priors stand.
- Regenerate over the files after a post-screen fix (`G.regenerate`), a form A before its isomorph, then verify all records.
- A re-read rolls every item of its picture again. Of the 66 items in three pictures that the fix did not touch, 64 scored the same and two went down: picture 42's
  thief bird, full marks at the first read and two half marks at the second on nearly the same words, which took its profile row under 0.9. The second scores stand;
  report both counts, and keep the first descriptions and scores (`vision/v045/first/`).
- A prior moved after the set is built can cost cells. A late rule (`WOOD45`, the lost balloon's string above the garden fence) moved one prior by 0.02, which shifts
  `choose`'s weights: the tier-3 garden's base seed gave other templates and the tier-4 playground's seed failed, with the next 14. Settle every rule that moves a scored
  thing before the calibration the set is built from, and run `verify_all.py` straight after any `set_prior.py`.
- Test a furniture rule in every setting that has such furniture. The lost balloon's string was kept off the playground's railing after a design test (`RAIL45`), and
  lay on the garden's wooden fence in two set pictures until `WOOD45`; `settings.py` already carried the lesson for the older placement (`balloon_max_y`).
- Check the casting pools (`scenegen/combos.py`, `POOLS`) before forcing a rule on a combination: design test 4 asked for a child's ice cream beside a lost balloon and
  a slide, and the cast has two children.
- No outlines on fine shapes. The bird table's tuft drawn as thin outlined blades was a ring of black spikes; filled blades without outlines on a low mound read as
  "a tuft of grass".
- `scenes/` and `probes/` hold list-shaped JSON beside the records (the summaries): a script that globs `*.json` skips what is not a dict. A score can be the string
  `"misread"`. And `probes.py`'s `SHORT` is a count of pictures per template: 0 means the template has none at all.
- A soft warning that jumps is a finding. v0.46's first validator run passed every record, and 374 of the library's 386 carried the palette warning where
  v0.45's had 83 of 382. The colour off the palette was the line's own: Line Art's strokes were lit by the lamp and had come out at (28, 28, 34) for the
  palette's (38, 38, 46) in every release since Line Art came in, and a thin line hid it. Before calling a warning noise, measure which colour it is about.
- When a heavier line closes over a small feature, give the feature a thin edge of its own; do not take its edge away. v0.46's inner line closed over the
  line mouth ("a dark smudge"). The mouth with no edge, thickened to be seen, was the one shape in a figure with no dark edge, and a reviewer read it as
  "a cut or blood". The coloured line at v0.45's width riding on a wider dark line of its own, both kept out of Line Art, ended that reading.
- A crop that cuts a thing off what it is tied to changes what it is. Both reviewers of the woman walking the dog read the lead, which the figure's crop
  cut off from the dog, as "a thin red stick (a cane)". Cut a figure with everything it holds or is tied to, to the far end.
- When reviewers disagree about a length, take it from the model. Of one neck in one pose, one wrote "too long and too thin" and another "a little too
  thick and slightly long"; the model's own numbers said the neck that shows had gone from 8.2 cm to 3.9 cm. Report both, and do not redraw for a
  remark that the old drawing and the new one both get.
- A round folder holds only what a reviewer may see. From v0.46's round 4 the map of which picture is which lies outside the folder until the reviews
  are in (`FIG_MAP`), the prompt says not to list the folder, and the draw of "a" and "b" is balanced (`FIG_BALANCE`): round 3's coin had put v0.45's
  drawing first in eight pairs of twelve.
- `render_set.py` skips a record that is there. After part of a cast is built again, move those families' records aside by exact names before
  rendering (`tpdb_work/v046/aside_people.py`), in the library, the gallery and the bench's library alike, or the folder is two casts. Blender also
  leaves a `.blend1` beside a cast file it saves over: look for them and remove them by name before packaging.
- Study one figure before changing a cast. v0.47 drew `person.mei` at eight yaws and in a dozen poses, gave the sheets to three fresh reviewers, then
  the whole cast and the animals to four more, and listed a point only when two or more of them named it. Each fix went behind a switch of its own
  (`TPDB_<NAME>47`, whose "O" is the release before's drawing), so that the old drawing and the new could go to a reviewer as a pair.
- Measure a posed surface before redrawing it (`tpdb_work/v047/dbg_pose.py` slices one). The belly was a dent: as a leaf node inside its parent's radius it
  gave the hull only a flat end, and the shirt's front lay 3 cm inside its back. The seated skirt reached forward to 0.176 where the knee was at 0.28, so
  a reviewer saw "knees pasted on top of the skirt". Neither showed in the code; both showed in a slice.
- A shell over a body (a vest, a cardigan, a coat's markings) rides on its host's finished surface (`core.shell_over`, `TPDB_SHELL47`). Bent by weights of
  its own it is another surface wherever a joint bends far, and the top came through the cardigan at the elbows. Bind it lying on the surface and move
  it out afterwards (bound a centimetre off, vertices at the trunk's side took the inside of the arm as their nearest face); bind to a hidden
  triangulated copy smoothed to the shell's own level; and keep the rim smaller than the clearance, or Line Art draws the inner edge dashed.
- A thing that is part of a figure's own drawing is measured as a part of its host. The reading dog's newspaper is an object of the pose
  (`PROP_sit_read_*`, in `rig.pose_props`); in a scene it is an element with `part_of` and `mask_svg` that draws nothing, and `compose.measure` takes its
  mask inside the host's. A new manifest field needs its line in `assets/asset_manifest.schema.json` before the validator runs.
- A new pose changes what an old placement rule draws. After a pose a template uses is redrawn, measure that template's yield again in every setting
  before anything else (`tools/cycle/yield_set.py` with a set of one template and `BAND=0`: nothing is saved, so it answers in seconds).
- A rule that draws a distance and then tests a gap sits at the edge of failing. Draw the tested quantity itself.
- Nothing upright of the setting between a hunter and its prey (`POST47`), and nothing upright behind or ahead of a walker headed for an obstacle
  (`TRIP47`): a lamp post between the cat and its bird, and a tree just past the walker's book, were each read as part of the event.
- A rule measured on its template alone can still take the template out of a crowded set. `TRIP47` placed 24 of 24 alone in each setting, and the tier-4
  street's forced set then failed on 31 bases of eight sets each, every set on the walker. Measure the earlier releases' forced sets under a new rule
  (`yield_set.py ... BAND=0`) before the set is built, and swap the template out of the set if the rule is worth more than the cell.
- When a tier 1 to 3 cell has failed a dozen bases, force a set as for tier 4 (`tools/cycle/forced_cell.py`). A forced set must also land in its tier's
  band, by its count of content items and its inference estimate: v0.47's first set for the tier-3 playground placed and never landed on six bases.
  Measure candidates with `tools/cycle/yield_set.py` (build_one's own loop, band and all) and build the one that placed. A set's templates must be
  feasible in the setting, must not want the same animal, and can hold at most two child templates (the cast has two children).
- A bench case that cannot build stalls every case after it. Check that a bench tag is new before using it, and put a case that may not place last.
- A family whose builder changed is rendered whole, every pose and yaw; a library with some poses from the old builder is two casts (`render_set.py`
  skips what is there, above).
- A long patch script, or one whose text holds apostrophes, goes in a file (`tpdb_work/v0XX/patch_*.py`, with `assert s.count(old) == 1` before each
  replacement); a bash heredoc breaks on the apostrophes. A file a script has changed is read again before it is edited by hand.
- Poses, from v0.47's blind rounds (`vision/isolation_v047.md`):
  - a stride on a thing reads as walking over it: the dog on the hose stands, one forepaw a step out and planted, and is drawn side on only;
  - tip a standing body about its hips, which stay at their standing height; tipped about its feet the hips drop and the legs splay or sink into the belly;
  - a pose tipped far over carries its eye to the outline of the head: past 48 degrees below level the pecking bird's eye was on the edge again;
  - a sitting animal needs a hind foot showing ahead of the rump, or its hindquarters are a blob;
  - four legs read as four only when each paw has its own place on the ground, and legs set that far apart read as a stride as well;
  - taking a pet's collar off takes away what made it a dog: upright, thin and with no collar, the reading dog was a weasel, an otter or a meerkat to
    three readers of three. Fit a band to the body's measured section; a ring on the neck bone showed as a flap behind the neck;
  - a heap with coloured bits at both ends reads as an animal; a long low swelling on the ground reads as a puddle and a short round one as a connector;
  - a drawing that reads better can still lose its pair as a drawing (the pecking bird lost three pairs of four to v0.46's level bird, and was read as
    pecking in every cut-out). Say which was taken and why, and put what was lost on the watch list.
- A shadow taken from a figure's filled columns moves under a wide thing the figure holds (`SHADOW47`).
- When a template "could not place", ask seed by seed and not layout by layout, and look at what the plan cast. v0.47's tier-4 isomorphs failed for
  three seed lists on `ice_cream_drop`; counted by seed (`tpdb_work/v047/dbg_ice.py`), every plan with the younger child failed every spot on one test
  and every plan with the older child placed. The older child passed that test by a tenth of a pixel: a test passed that narrowly is a rule at the
  edge of failing, and it had drawn the event with one child of two since v0.28 with no one seeing it (`CONE47`).
- Check the isomorph classes of the tier-4 cells before the set is settled (`batch.iso_key`). A template alone in its class maps only to itself:
  `ice_cream_drop` (no garden), `paint_tracks` and `blocked_hose` (garden only), `bird_steals`, `dog_reading`. A form that holds `paint_tracks` or
  `blocked_hose` has no isomorph anywhere, and one that holds `ice_cream_drop` has none in the garden; v0.47's four tier-4 cells left six pairs of
  twelve. A cell with none of those five keeps every pair open.
- When the tier-4 isomorph still will not build, count what stops it before touching a rule: replay `build_isomorph` without saving and tally every
  try and layout by the mapping it drew (v0.47's `tpdb_work/v047/dbg_iso4.py`). With the rules final, v0.47's stop was crowding (the dropped ice
  cream's group is placed late and needs a clear band), no one test. Crowding is a matter of seeds: search only the pairs that can build, the roomier
  target first, on four seed lists side by side, each stopping when any of them has saved a record (`tpdb_work/iso47t4.py`, a copy of
  `tools/cycle/iso_t4.py` with those three changes). After 48 calls on eight seeds had found none, it found one on its 63rd call, in five minutes.
  Settle the isomorphs before the probes are built: the probes count the templates the set already shows.
- A rule found after the set is built: calibrate its template alone with the switch off and on (`calibrate.py --only`). Off must give the shipped
  numbers. If on moves a prior only in a decimal the planner's band does not feel, leave the priors and say so; then run `verify_all.py` on the
  set, since a record rebuilds through its failed tries and a rule that lets an earlier try succeed changes the record. Rebuild what changed with
  the final rules, look at it again, and give a drawing no picture has held a blind reading of its own before it goes into the set.
- Readers and reviewers: tell them to write with the Write tool and not to list the folder; remove an old reading before a new reader writes to the
  same path; keep a first reading and its picture under a `_first` name when a test picture is rebuilt; give a digest agent the right key.
- Quotes: a quote in a doc or a code comment is checked against the description file it came from, since a flaws file's own quote may be shortened; a
  quote stays on one line of the doc, so that a checker can find it.
- A mend is benched for the reading it is meant to change. `about_to_trip` failed v0.46's gate on a walker read as going the other way; v0.47 drew
  the walk again for that, one bench reader of three still wrote "it is not obvious which foot is in front", and the walk went on to the screen as
  it was. It failed the same way there, on the smallest walker of five (0.41 of full size, the others 0.46 to 0.51). A doubt the bench names about
  the very thing a mend is for is not left to the screen: bench the figure alone at the smallest size a scene draws it, with the one question the
  mend is for (which way is he walking), and v0.46's drawing beside it.
- A change to how every side view is drawn needs a reading of its own. v0.47 turned the side view's head 48 degrees toward the viewer for 35 and drew
  the walk and the run again, and five readers of the screen, one picture each, wrote of which way a figure faces. The two changes went in together
  and the cause was not tested: put one such change in at a time, or bench each alone.
- What is added to a prompt when it is sent is part of the prompt. v0.47's scorers were asked, in the message that sent `scorer_<x>.txt` and not in the
  template, to read only the named files, to write with the Write tool and to list every judgement call they scored 1. They listed 71 where v0.46's,
  unasked, had listed 11, so the strict count of v0.47 compares with no earlier one. Put an addition into `tools/cycle/prompts/` before the screen,
  record it word for word in `vision/screen_prompts.md`, and keep it in the next screen if its count is to be compared.
- The screen's reader prompt must say how to write a file. v0.47's did not, as v0.39's does not: two readers tried the shell first, the write failed,
  and they listed the screen's folder to find out why, which the prompt forbids. Add "write each description with the Write tool" to
  `tools/cycle/prompts/reader_template.txt` before v0.48's screen, and say in `screen_prompts.md` that it was added.
- A list defined by a threshold misses what sits on it. `about_to_trip` had a mean of exactly 0.90 and failed the gate on its misread; the page's
  next list was "under 0.9" and would have been empty. It now takes the gate's failures too (`scenegen/site.py`).
- Describe an old drawing from a picture of it, not from memory of what the new one replaced. Three files of the release called v0.46's pecking bird "upright" where
  a reviewer had it "nearly level with only the head dipped"; the slip was found only when the page's pairs were laid out on a sheet. Lay the page's
  pairs out and look at them before their notes are written.
- Say what was looked at, and no more. The notes of v0.47 record a look at every probe on sheets of four and none at the set's pictures one by one,
  so the README says the first only.
- A study of the drawing itself is done large and fast. v0.48 built one family alone with one change (`python build_cast.py <dir> person.mei`, about
  5 s), rendered a row of heads at twice the release's size (`TPDB_PPM=800`) with a row at scene size under it, and looked at the sheet before the
  next change (`tpdb_work/v048/tryh.sh`). Look at the first sheet before writing the list: v0.47's head was wider than tall, which no reader's
  quote had said in those words.
- Give the whole head one map. v0.48's egg head is a function of the ball's point (`core.head_pt`), and the hair, the hats, the ears and every
  feature of the face are placed through it, so a change of the head's shape moves all of them together. Before it, each part had its own radii.
- A pair bench can go backward, and that is what it is for. Bench 2 gave v0.47 six pairs of sixteen where bench 1 had given it three, because a
  change made for one reading (a side view's head turned to 15 degrees, which the direction bench preferred at scene size) was a worse drawing at
  a reviewer's size: the front view's face on a head in profile left "the single eye sits on the very front edge of the face outline, partly cut off". A reading measured at scene
  size and a drawing judged at figure size are two tests, and a change must pass both. Run the pair bench again after every round of mends.
- When every answer is right, ask how sure the reader was. All 48 answers of the direction bench had the way the figure goes; "sure" was 4, 6 and
  11 of 16 for the three drawings, and that is what chose between them.
- Drawing a thing more correctly is not drawing it more readably. The walk drawn as the true instant of a step, the leading foot lifted, read as
  standing to five readers of six; the long stride with both feet down is what says walking, and two short motion lines say which way.
- A change to how every figure is drawn can go to a worker with a brief, but the bench stays here. The animals were redrawn by a delegated worker
  from a written brief; its own report said the work was done, and the pair bench then gave v0.47 three pairs of twenty, all one dog's legs. The
  reviewers' own words went back to the worker, and the second bench took fourteen of fifteen. Bench a hand-back as if it were your own trial.
- Look at the isomorphs and the probes as closely as at the sixteen cells. The one flaw found on the look at v0.48's set was in an isomorph: a
  begging dog's head on the hose reel's drum. A redrawn figure has a new height, and a fixture that an old figure cleared may now sit behind a
  head. The rule that came of it (`REEL48`) was checked by rebuilding every other record to the pixel.
- When a cell's templates are last release's, try last release's seeds first, for the isomorph too: v0.48's tier-4 isomorph built on v0.47's
  seed, 164111, on the third call of the wide search, after 65 calls of the plain one had found none.
- Check who is who in `castlib/specs.py` before a document names a character. A first draft of v0.48's design-test record had the bearded man
  in green as the study's second figure; the study's second figure is the man in the red shirt.
- A patch whose text holds an apostrophe goes into a file written with the Write tool and is then run; a shell heredoc ends at the apostrophe.
- A finer drawing can drop a cue that only worked because it was coarse. v0.47's moustache was named by the screen's readers in ten of its wearer's
  fifteen pictures; a reviewer of enlarged figures called it "very large and curled, sitting over an open red mouth; slightly comic", the study drew
  it short and thin, and v0.48's readers named it in none of seventeen, nor the beard in any of twenty-four. The design tests had shown it first
  (three readers of the older man, no moustache named) and it went to the screen as it stood. What a mend takes off a face is read at a picture's
  size before the screen: one question, what is on this person's face, on the smallest figure a scene draws.
- Ask who a figure is, not only what it does. Four grown figures were called a girl or a boy in 11 of their 81 screened pictures, for 6 of 80; the
  scorers credit the action, so no score shows it. `tools/cycle/who_called.py` counts it from the inventory lines; run it on the design tests'
  descriptions too, and put an age question on the bench when a release changes heads or proportions.
- A template nobody touched can fail on one unsaid thought. `rain_coming` has one inference a picture and three pictures; one reader named the storm
  clouds and the pointing child and did not go on to the rain, and 0.889 fails. Give five pictures (`NEED_T` in `probes.py`) to every template whose
  verdict rests on one inference a picture, and treat an inference that only the sky carries as drawn too quietly.
- The helper scripts a release needs belong in `tools/cycle/`, not in `tpdb_work/`, which git ignores. Until v0.47 the angle pass, the forced probes,
  the wide isomorph search, the merge, the per-angle gate and the strict count were copied from one release's scratch folder to the next; v0.48
  moved them (`probe_angle.py`, `more_probes.py`, `iso_t4_wide.py`, `merge_iso.py`, `gate_yaw.py`, `strict_count.py`, `who_called.py`).
- A sheet of several rows is ranked by a row's place as much as by its drawing. v0.49's first head bench gave four reviewers the same nine
  heads drawn five ways, the rows shuffled for each: all four put the top row last and the second row fourth, whatever was in them, and
  three different shapes were somebody's first. Compare two drawings at a time, larger, each pairing in both orders, and count the
  choices (`vision/isolation_v049.md`, benches 1 and 2). A reviewer can describe its two rows the wrong way round and still choose:
  count that choice and quote only words that fit the picture.
- When the brief is about taste, send Sam the candidates before the cast is built. v0.49 sent one sheet (`vision/isolation_v049/head_candidates.png`:
  the old head and four shapes, heads large and whole figures small) with the one the release would go ahead with named on it, and went ahead.
- A line where two parts join has to come from Line Art's intersections, not from an outline that happens to cross. The chin's line across the
  neck came out as stubs or dashes while the neck was a piece of the skin's one mesh, which draws no intersections (v0.39): the head's
  underside is buried in the neck there, and Line Art shows or hides whole segments of it. The neck as a part of its own, with its
  intersections kept, drew the line whole in every view. To find which part draws a stray line, open the family's `.blend`, set
  `bpy.data.objects[<name>].lineart.usage = "EXCLUDE"` on one suspect, save a copy and render it; a dash under a collar was the rim of the
  neck's rounded foot.
- Bench a new gesture against the old one on the same seeds before it replaces it. A hand held out, palm up, for the first drop of rain
  looked right on my own sheet and read worse than the pointer it was to replace: at a picture's size an open hand held level is a
  finger pointed at whatever stands in front of it.
- A pass is not a mend. `rain_coming` failed v0.48's gate in three pictures and passes v0.49's in five with the drawing unchanged. Say which it
  is wherever the result is reported, and do not take a template off the list for a pass its drawing did not earn.
- v0.49 wrote here that what makes a small figure read as grown is a mark of age and not the head, and not to spend a release on
  proportions. The first half held and the second was wrong. That bench (`age_bench.py`: figures cut out on strips) gave the same answer
  for four casts, one figure of fourteen called young or none, because it was at its ceiling: nobody calls a figure alone on a strip a
  child. In whole scenes (`age_scenes.py`, v0.50) the marks of age alone took 13 young names of 45 to 3, a head at 0.86 of its size alone
  took them to 5, and both to 1; the screen then counted 3 of 79 for 20 of 89. A lesson drawn from a bench is as good as the bench.
- Price a rule that takes ground away on the crowded cells before the set is built, with the rule on and off. Revision 46's edge rule was
  written three times. For every figure at 14 px it did nothing to a single event's yield and all but stopped tier 4: the tier-4 garden
  failed on 56 seeds, the tier-3 playground went to a forced set, and no tier-4 isomorph came in 235 calls. For animals at 14 px the set
  came back and the tier-4 isomorph still would not build in 126 calls. At 8 px it built on last release's seed, third call. A scene switch
  is read from the environment when `scenegen.scene` is imported, so a comparison is two runs: `TPDB_EDGE49=O python tools/cycle/yield_set.py ...`
  beside the plain one.
- When a search that took three calls in the last release has taken two hundred, stop and look for the rule. One call with each new
  switch off (`tools/cycle/iso_one.py`: last release's isomorph on its own seed, into a scratch folder) answered in half a minute what the
  wider and wider searches had not. Then look at the boxes: the cat and the bird that the 14 px margin refused stood 8 and 10 px above the foot.
- When a rule changes after the set is built, `verify_all.py` under the new value says what to build again. `TPDB_EDGE49_PX=8` over the 106
  records built at 14 px found 104 identical and 2 different; those two were built again and the rest stand. Without that count the choice
  is a third whole build or a rule nobody tested on the release's own pictures. The calibration was left as measured, and the README says so.
- Measure a forced set before a design test spends 80 seeds on it (`yield_set.py N SETTING SEED 3 '<set>' BAND=0`, seconds once the
  variants are rendered). v0.49 lost two design-test builds to sets that cannot be cast or placed: a swing forced in the playground
  (it is the garden's event) and the washing beside the watered flowers.
- The washing can only be hung by the three tallest grown figures: the hanger's feet must stand within 30 px of the posts' depth, and
  the others' hands do not reach the line from there. `probes.py` gives the template up when its three groups cast a shorter one;
  `more_probes.py` with small groups on more seeds fills it. In v0.49's last build `probes.py` left nine templates short, each on a partner
  (the storm beside a watering template, a second dog, the playground's events with each other), and small groups filled all nine.
- A rerun of `probe_angle.py` starts again at its first seed and overwrites a probe of the same name: v0.49's replaced an angle probe of the
  dropped ice cream with one of the playing dog. Both passes still ended `SHORT {}`, but count the probes and rerun `probes.py 3` and
  `probe_angle.py 2` for their last line after any rerun.
- The setting's items are most of what a screen leaves under full marks, and they are a reader's habit: 41 of v0.49's 42, from seven readers,
  two of whom left the clouds out of all eight of their pictures, and the set's mean fell from 0.993 to 0.967 on them alone. Read a set's
  headline with the things apart from the rest, and say in the README which moved.
- State the rule with a count, so the next release can make the same one. v0.48's "51 of the calibration's 252 numbers moved" could not be
  made again from the two files (45 by a threshold of 0.002, 66 with none). v0.49's is: of n, b0_mean, b0_sd, s_mean, d_mean, r and a over
  the 36 items, those that moved by 0.002 or more (24).
- `make_readers.py` deals the pictures in the order their names sort as text, so with more than 99 pictures the second reader has pictures 9,
  10 and 100 to 105. It harms nothing; say it in `screen_prompts.md`.
- Begin every shell command at the repository's root (`cd /e/Cognitive_Test_Scene_Creator && ...`). A `cd` into a subfolder in one call is
  still in force in the next, and twice in v0.49 a command ran in the wrong folder for it.
- A write on this exFAT drive can fail once with `OSError: [Errno 22] Invalid argument` and work on the next try. Check the file's size
  and tail before going on; a patch script that asserts what it replaces can simply be run again.
- A bench at its ceiling measures nothing, and a choice made on it is no choice. v0.49's age bench read figures cut out on strips and found
  every cast grown; v0.41's and v0.43's benches of the same fault had chosen on cut-outs too. The fault lives in whole scenes, so bench it
  there: `tools/cycle/age_scenes.py` takes pictures of the last screen that hold the figures, builds each again with every candidate cast
  from its own record, gives each reader two pictures of every cast and no picture twice, and counts with the screen's own counter. v0.50's
  found the fault where the screen had it (13 of 45 appearances called young, for the screen's 16 of 45 on the same pictures) and what
  cured it (1 of 45).
- Before trusting a new bench, see that it shows the fault with the old drawing. That is what the O cast was for.
- Two changes that each may help are benched as a square: neither, each, both. Marks of age alone took 13 to 3 and smaller heads alone
  to 5; both to 1. Without the two middle casts the release could not have said that either would have done most of it.
- A trial cast's library starts as a copy of the last library's variants of the families the trial does not change; the rest render on
  demand. All 96 rebuilt pictures came back with the same templates and the same poses for the same people.
- A constant that seats a figure stops seating it when the figure is drawn again. The seesaw's riders had sat on the plank at a rise of 14
  units in v0.31; after two redrawings of the bodies their hips lay 4 to 10 units above it, and the remark was carried five times as a
  drawing problem. Measure the drawing where the rule acts (`templates._under50` reads the sprite's own underside at its seat anchor),
  and when a remark is carried, measure before designing a fix.
- A fix can hide the thing the fault was showing. Seated on the plank, the riders covered the handle's post, and all three readers wrote
  that they had no handles. Read a round for what is new as well as for what it was aimed at, and give the mend its own round.
- When a remark comes back from every position, it is not about the position. The slider was read in front of the chute, behind its near
  wall, sunk in it and on top of it, and sat "slightly above" the chute in two or three cut-outs of three each time. Stop, say so, and put
  the other kind of change (the chute's drawing, the pose) on the list.
- A cue that is misnamed can still carry the reading. The hose's swelling is a connector to every bench reader and is also what tells two
  of three that the water stops at the paw; without it one of three got there. Bench a cue's absence before taking it away for its name.
- A rule that came from the builder's own look is a guess until a reader has had it. `WOOD45` lifted the lost balloon's string up to 200
  units from the hand in the garden, from my look at two pictures; all six of v0.49's pictures of the template were garden ones, and a
  reader took the balloon for perhaps someone else's. When a template's pictures all come from one setting, look for a rule that only
  that setting has.
- Look at the picture at full size before taking the list's own fix. The tear on the catcher's cheek was the white of a wide eye at the
  edge of a face in profile, and the roller held oddly high was a roller on a pole drawn in the colour of the fence behind it.
- A template that was looked at and left can fail the next gate. `play_catch` had 1.00 by v0.49's gate and 0.812 on its strict count, on
  one reader's doubt about who threw; v0.50 left it, and in two pictures of five the catcher was then read as the thrower, or as either: 0.80. The strict count
  (`strict_count.py`) is the list of passes that are one doubt from a failure: bench the lowest of them, or say that the release chose not to.
- A template can fail on a neighbour nobody benched. `square_wheel` failed on its one wheelbarrow, with the sprinkler's hose on the ground
  behind the square wheel: a square with a hose through it is a hose reel. Three of its four pictures were bicycles in v0.49 too. When
  a template has two carriers, see that the probes hold both more than once, and look at what lies behind a contradiction's object.
- A bench run with the default library renders what it lacks into that library. Before the release's own library existed, round 1 rendered
  one variant into the last release's `lib049`, which is tracked. Give every bench a scratch library (`BENCH_LIB`), and look at
  `git status` after a bench.
- A failed write can leave a patch unapplied and the next command running. `python patch.py && [ ... ] && cp ...; ls ... && run` went on
  after the patch's `OSError 22`: the bench was asked for case names that did not exist, built nothing and said nothing. Chain with `&&`
  to the end, and check a log's size.
- A patch that replaces everything between two marks replaces what you did not read between them. v0.50's site patch cut from the
  screens' pair to the first function and took the page's skeleton (`PAGE_OPEN`) with the notes; the build said so. Keep a copy of the
  file, cut from the first thing replaced to the end of the last, and diff the result against the copy before running it.
- A set can change though no rule about it did. With a new cast and its prior, 5 of 16 cells came back with v0.49's templates (v0.49: 13
  of 16 with v0.48's); the tier-4 garden failed on v0.49's base and placed on v0.48's. Try the bases of the last two releases.
- The site's before-and-after pairs can come from the bench: a round's cut-outs of the old and the new drawing are on the same seed
  (`crop:` keys in `scenegen/site.py`, the round's map says which is which). The notes in `site.py` keep clear of apostrophes,
  which `check_quotes.py` pairs as quotation marks on a line.
- A cut-out bench can sit at its ceiling for an event as it did for an age. v0.50's game of catch was read the wrong way round in two
  whole pictures of five, and on the bench all three readers of the same drawing, cut out, read it right. When the screen's fault is a
  reading of who does what to whom, bench it where it failed: build the failing pictures again from their own records
  (`tools/cycle/ws_build.py`: `G.regenerate` with the trial cast, and the switch made to act at the record's own revision,
  `templates.CATCH51_REV`), one arm as screened, and give each arm several fresh readers with the screen's prompt.
- A reader who has two pictures of the same people carries the reading of one to the other. Each reader of v0.51's catch bench had one
  picture 79 and one picture 90, the same girl and the same woman, from two arms. The four readers whose arms were the old ball twice read
  none of eight right; the eight who had one picture with the early ball read it right seven times, and their other picture, an old ball,
  seven times too. Counted by arm that made the old ball 3 and 4 of 8 where, alone, it was 0 of 8. Give a reader one picture of a pair,
  or count by reader as well as by arm, and say which arms shared readers.
- A trail does not say which end it began at; what it is next to does. A ball at the far end of a dashed arc, by the catcher's hands,
  was hers to throw, and the same dashed line with the ball a third of the way from the thrower's hand was read right by seven of eight.
  Three solid lines behind the ball, as behind a runner, were read no better than the dashes and drew more doubt on cut-outs.
- A pose can be right for the bench and not move the reading. The catcher's two open hands ended the clasped hands that six cut-outs of
  six had remarked, and in whole scenes changed nothing of who threw. Take such a change for what it does, and say that.
- Before redrawing a mark for a reading, count the reading by pose. The man in the red shirt was a boy in two v0.50 pictures and the list
  asked for a wider moustache; on sixteen pictures a side the wider one changed nothing (a boy in two of sixteen each, the moustache named in
  nine for seven), and three of the four boys were one pose, the sweeper bent over his broom. `tools/cycle/ws_tally.py moustache` prints
  the line each count rests on.
- A second look at a first drawing is cheap when it is only a pose. The catcher was drawn three times in an afternoon (one family alone
  builds in five seconds, `tpdb_work/v051/try.sh`), and the second, which looked right on my sheet, was "waving or fending the ball off" to
  all three readers: an open palm shown flat to a side view is a wave. Read a new gesture before building a bench cast round it.
- When a thing is misread beside a neighbour, order the placing before writing a check in every neighbour. The barrow needed to keep off four
  templates' hoses; placed after them all (`planner.realize`'s rank), one check in the barrow's own template did it, from the boxes the
  hoses had already left (`sc.keepout`, the hose elements' boxes). Price it with the crowded sets as well as alone.
- `yield_set.py` now takes `BENCH_CAST` and `BENCH_LIB`, as the bench does: before the release has a library of its own, a rule is priced
  on a scratch copy of the last library and nothing is rendered into a tracked folder.
- Renders are not the same to the byte from one run to the next: an unchanged pose rendered from the new cast differed from the last
  library's file in one pixel by one level. A library carried from the last release (minus what was redrawn) is what keeps a release's
  unchanged figures identical; compare redrawn variants by their pixels and not by a hash.
- A quote in a code comment is counted as well as checked. "in six cut-outs of six" and "two of three wrote" were each one reader's words
  put in several mouths in a first draft of v0.51's comments; the count goes outside the quotation marks, and each quoted phrase is
  looked up in the file it came from.
- A template's pictures are counted two ways, and they differ. The records' template lists gave the fence painter five pictures; the gate counts the
  pictures that hold one of its items, and the painter of `paint_tracks` is its item too: nine. Take a count from `gate.json` when the sentence
  is about what was scored, and say which count it is.
- An entry of `vision/limits.txt` can run over two lines. v0.50's patch put three new entries after the first line of the rider's and parted
  it from its second; v0.51 found the stray line and put it back. Insert after the last line of an entry (the next line that starts with `- `),
  and read the entries round an insertion in the built README.
- A screen with pictures that came back identical is a retest as well, and it is cheap to count: six of v0.51's 102 pictures were v0.50's to
  the pixel, and 70 of their 71 items had the same score from other readers and scorers. Say it beside the gate; it is what a single half mark
  is measured against.
- A full gate after two failures is the gate as the scorers applied it. v0.51's 64 of 64 has 44 full marks beside another reading and eight
  templates that would fall with them halved, one of them (`bird_steals`) not drawn since v0.47. Write the next list from the strict count
  when the gate gives none, and say of each pass whether its drawing earned it.
- When the brief is about how a part of every figure is drawn (v0.52: the upper arms, the shoulders and the sleeves), start with sheets of the last
  release's own cast, large: every person standing at five angles, and two of them in every pose that moves the part (`tpdb_work/v052/rs.sh`
  renders a list from a cast at 800 px per metre; `upper.py` cuts the upper half of each figure). The list of faults comes from those sheets.
  v0.51's readers had written nothing of a sleeve in 102 pictures, and neither did v0.52's: a reader of a whole picture does not name it.
- A fault of line can be a part that draws no line. The bare arm is `Skin`, which draws no line where it passes into another part (v0.39), so a
  sleeve that ended in the hull's rounded end had no hem at all. Before redrawing an edge, ask which object draws it and with which Line Art usage.
- An opening is a lid. A hull's branch is cut at a plane across the limb, its end faces come off, and those faces, set a few millimetres inside,
  are a part of their own that draws the line where the limb comes through (`core.open_branch`, as `open_end` for a hem). Make the lid a
  little smaller than the opening, or its edge lies on the sleeve's own wall and Line Art draws dashes of it; and begin the limb well up inside
  the sleeve, or its rounded end sits at the lid and the line is dashes again.
- The Skin hull is fragile where four branches meet (the neck, the chest and two shoulders). A shoulder's radius scaled to a slimmer arm, or its
  place moved a centimetre, left one figure of ten with a plate of cloth through the chest, and only that figure. Build with `TPDB_HULLCHECK=1`,
  which prints each hull's vertex count, compare the counts with the last build's, and look at every figure standing at four angles after any
  change to a node of the trunk. The count is a hint: three figures have counts of their own and are sound.
- Give a garment the width of its wearer where it lies on the wearer, and its own width where it hangs. A tee's sleeve as wide as a man's on
  every arm stood off a woman's and a child's arms "like wings"; a long sleeve as wide as a slim arm was "a stick". The tee's sleeve follows the
  arm's own thickness (`LA`), the long sleeve the garment's (`LB`).
- A bench of pairs has a place effect, and both orders are what cancels it. Row b was chosen by 8 reviewers of 12, 8 of 12 and 5 of 6. Where
  a drawing wins in both orders the effect does not matter. Where the choice follows the row, in every round, the two drawings are a toss-up,
  and that is the result: say it, and do not count such a set for either. Two reviewers of one set gave the same reason for opposite rows.
- Stop refining when a round's remarks come back from the other drawing too. "A long thin tube" was said of the new sleeve on a raised arm in
  round 3 by the reviewer who had the old drawing below, and the reviewer who had it above preferred the new one for the same arm.
- Send the sheet to Sam when the choice is made, with the choice named, and go on (`vision/isolation_v052/arms_v051_v052.png`).
- A release that changes only the cast, and by a few pixels of outline, can bring the whole set back: all sixteen cells, the five isomorphs
  and the 81 probes placed on v0.51's seeds with v0.51's templates and people, by v0.51's own commands in v0.51's order. Run the last release's
  commands first, compare records by template, cast and place (`python tools/cycle/same_set.py scenes scenes_v051`), and say in the README that the
  screen is then a second reading of the last set.
- A second reading shows what one reader is worth. With the same pictures, keys and picture numbers, 1,054 of 1,114 items had v0.51's score;
  fifty of the sixty others were the clouds or a tree; and of the ten that were not, three were all of v0.51's non-setting items under full
  marks, now at full marks with nothing drawn, and seven were new misses. Compare item by item whenever the keys are the same.
- "Nothing to draw" was wrong. v0.51's list said it of the square wheel because every reader had seen it, three of eight only among the unsure
  things. In v0.52 those three pictures cost the template the gate: two readers did not name the wheel at all. A thing that a third of its
  readers name only in passing goes to a bench in whole pictures, where not noticing can happen; a cut-out is always noticed.
- When a bench in whole scenes is run for one question, read it for the cast's other questions too. The eighteen pictures built for the sweeper
  were also the test that new sleeves do not change how old a figure looks (4, 3 and 1 of 35), and the design test of the cast in whole scenes.
  And see what the first arm shows before reading the others: the sweeper was grown in 9 of 10 as screened, so the bench could not have shown
  an upright sweeper to be better. Two arms that share files for most pictures also measure the readers: the same two pictures made the woman
  in purple a girl in one arm and a woman in the other.
- A helper script made to try one family at a time pays for itself in an hour: `tpdb_work/v052/try.sh TAG LIST.json` builds the named families
  with the environment's switches, renders a list and makes a sheet. `TPDB_SLEEVE52_P`, a JSON dict of the drawing's numbers, let a trial change
  a width or a length without a patch.
- `tools/env.sh` and `tools/cycle/cfg.py` carry the release's number: set both at the start (`age_scenes.py` took v0.50's key map until they
  were). `cd` to the repository's root at the start of every command; a `cd` inside a command chain moved the working folder three times.
- Read a list's proposal against the code's comments before drawing it. Three of v0.52's proposals had been the drawing before: the floating box lower
  with its shadow (revisions 10 and 11 took it up from there, and say why), a level box (benched in v0.41), a piece of bread in the thief bird's beak (the
  drawing until v0.47's bench took the bite). `grep` the template for the thing the list asks for; a comment that quotes a reader is a bench already run.
- Measure a remark before designing for it. The heavy seesaw's man "in front of the plank" sits within 1.6 units of where the children's measure
  (`_under50`) would put him; the remark is of his legs, one each side of the plank, as v0.32 found. And look at where the code puts a figure before
  moving it: the grown duck feeders stand at the pond's front because the ends' spots fail on the cattails' zone, which keeps a reed from behind a head.
- Before building a bench for what readers call a figure, count the screen by reader (the readers' prompt files say who had which picture). v0.52's four
  girls were three readers' of thirteen, and the nine others never wrote it. A bench of nine fresh readers then had none of the three kinds among them: she was
  a woman in 18 readings of 18 as screened, and the bench could choose nothing. A fault that is some readers' habit needs more readers than the screen had
  to show itself, or it is left as a note for the scoring.
- A bench whose first arm does not show the fault is still a result, and the first arm is what says so. Report all arms, say that nothing was chosen,
  and keep the drawings behind their switch.
- Look at a trial figure large before spending readers on it, and look for what it becomes from the front: hair drawn back into a bun made a woman a boy
  with short hair, and a skirt to the knee made her younger. Three of six trials were set aside on one sheet each (`build_cast.py <dir> person.ana`, a minute).
- One bench can ask two questions of one set of readers when the pictures do not overlap (`tools/cycle/bench_build.py`, `bench_prepare.py`,
  `bench_tally.py`). Where a reader has two pictures of the thing in question, give both of one arm, so that what the reader carries from the first to the
  second stays inside the arm, and count by reader as well as by reading: the old wheel was named late by two readers of four, in both their pictures each.
- A fault that is a thing not noticed shows on a bench as a thing named late. No bench reader missed the old wheel altogether, as two of the screen's had;
  half of them came to it only in the unsure section. Count where in a description a thing is named, not only whether.
- A larger drawing is noticed more and read more ways. The larger wheel was in every description, and two readers of five then offered a crate or a grate
  for it, which nobody had said of the smaller one on the same bench. Take the change for what it was for, and put the new reading on the list.
- When a gap between two events does not end a reading, stop tuning the gap. The jumper 150 units behind the catcher was still jumping for the ball to two
  readers of two; the two templates now share an exclusive tag (`templates._Ex53`, a descriptor read when the planner asks, so that older records keep
  their plans). A rule of that kind draws nothing, so it has no test of its own: say so.
- A cell whose templates a new rule forbids will not come back, and the free search for another can be long. Measure the earlier releases' sets for that
  cell with `yield_set.py` first, each from the seed it was built on with the band on: of four garden sets one placed, in seconds, and was forced
  (`forced_cell.py`, its `SETS` and the reason). A forced copy of a free cell's own set does not reproduce the free plan, so pricing a rule that way on
  the cell's own seed shows nothing: all four arms failed alike.
- A release that changes no figure keeps the cast: copy `out`, `lib` and `gallery` to the new tag so that the tools' paths hold, leave `BUILDER_VERSION`,
  and say in the README that the cast is the last release's. Cells that hold none of the changed templates then come back to the pixel (19 of 21), and
  their items are a retest. The probes do not come back: the probe pass composes its groups from what the set shows, and two changed cells changed
  73 of 78. Compare by pixels (`tools/cycle/retest.py`), not by names: 63 names were in both releases and 24 pictures were the same.
- The retest keeps saying one thing: v0.52's three non-setting items under full marks in pictures that came back unchanged were all in full in v0.53,
  with nothing drawn. A template that passes on such a picture has not been mended; say "a pass its drawing did not earn" where the result is reported.
- A scorer can list what is not a call. One listed seven items for a grandparent called an older man or an older woman, which are the key's accepted
  names. Check a listed near word against the key's accepted phrasings before counting it, and say what was left out and why.
- `grep -c "^PROBE"` on a log counts a line that starts `PROBES_EXIT` too. Count with the name after it (`^PROBE \S`), and check a sum of passes against
  the folder: 61, 2, 12 and 3 are 78, and the first draft had 62 and 11.
- A patch that replaces several things in one file should write only at its end. v0.53's patch of the limits stopped on a wrong anchor at its eleventh
  step and had changed nothing, so it could be mended and run again.
