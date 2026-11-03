# v0.24 blind screen: what it found (the work list for v0.25)

The v0.24 screen used the same prompts as the twenty before it (`screen_prompts.md`). Nine readers who never saw the key described 72 pictures (`v024/desc_pic_NN.md`): the 21 pictures of the set (16 showcase pictures and 5 isomorphs) and 51 probe pictures. Three scorers with the same prompt scored pictures 1 to 24, 25 to 48 and 49 to 72 against `keys.json` (`scores_a.json` to `scores_c.json`, merged in `scores.json`). Per-template means are in `screen_summary.json` (`by_template`; probes count there, not in the headline figures). The gate is in `v024/gate.json`. It is the first screen run on Windows, by readers and scorers on Claude Opus 5.5; earlier screens' models were not recorded.

## Headline (the 21 pictures of the set)

| | v0.21 (21) | v0.22 (21) | v0.23 (21) | v0.24 (21) |
|---|---|---|---|---|
| Things | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions | 0.996 | 1.00 | 1.00 | 0.988 |
| Inferences | 1.00 | 0.971 | 1.00 | 0.986 |
| Contradictions | 0.84 | 1.00 | 1.00 | 1.00 |
| All items | 0.989 | 0.997 | 1.00 | 0.993 |
| Misread items | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 |
| Oddities per picture, as logged by the scorers | 1.1 | 1.2 | 1.0 | 5.2 (see below) |
| Remarks in the readers' "unsure" sections per picture (all screened pictures) | 4.35 | 4.49 | 4.32 | 5.67 |

Across all 72 pictures 799 of 805 scored items had full marks, six had half marks, and none was misread or missed.

## The oddity row does not compare across this release

Logged oddities rose from 21 to 110 in the set and from 42 to 227 in the probes. This is mostly a change in the instruments, measured two ways:

- **The scorers.** v0.23's scorers logged 22% of what the readers wrote in their "unsure" sections (0.97 per picture of 4.32); v0.24's logged 83% (4.68 of 5.67). The prompt is the same; it does not say how much to log. This is the larger part of the rise, by far.
- **The readers.** A control (`v024/control/`): one current reader described eight unchanged v0.23 pictures of the set, blind. On those same eight pictures it wrote 6.88 remarks per picture, where the v0.23 readers had written 6.0: 15% more.

Remarks per picture rose 31% between the screens (4.32 to 5.67), of which the control accounts for 15%. The rest could be the pictures, the mix of pictures (51 probes, was 44) or one reader's sample of eight; the control cannot separate these. So no claim is made either way about whether v0.24's pictures are odder or cleaner overall. The specific oddities below can be compared, because they are named.

## The v0.23 list

| v0.23 reading | v0.24 result |
|---|---|
| The teenager called "a woman with a brown ponytail" (13 items, credited) | Named a boy in **all 25** pictures he is in, a woman in none; five inventories said unprompted "red cap worn backwards". No reader volunteered "teenager". In the control, the current reader called the old drawing "woman in blue hoodie ... brown ponytail" in all four of the eight pictures it is in, so this is the drawing and not the reader. His direction held: the one remark is "brim pointing right, backwards relative to his running direction", which reads the cap correctly |
| A sleeping cat on the path behind a walking man's back foot: "he could trip over it or step on it" | No reader put a sleeping animal at anyone's feet in the 72 pictures. In the control, the current reader saw the old picture as v0.23's readers did: "it could trip up the walkers" |
| A figure at the back "drawn as large as foreground people" (four pictures) | No such remark in the park or on the playground, or in the street |
| Arms raised across the face on the slide: "holding her head or hair" | No such remark in the three slide pictures: "arms raised up in front". Two remarks remain, "rather small for the slide" and "nearly upright, small and stiff" |
| Riders "slightly in front of" the plank or the chute | The bench left the seesaw alone; "seesaw riders not clearly on the plank" still comes up in two probes (61, 68), and "no shadow under the raised seesaw girl" in others. Note for the pilot, as since v0.21 |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 |
|---|---|---|---|---|---|
| Pass | 64 | 61 | 63 | 64 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 0 | 3 | 1 | 0 | 1 |

Every template was screened in at least three pictures (49 in three, 6 in four, 7 in five, 2 in six). The v0.9 retest put the gate's reader variance at about five templates between screens.

## What reads poorly (the v0.25 list)

| # | Template | v0.24 | What the readers saw | Fix for v0.25 |
|---|---|---|---|---|
| R1 | `carry_bag` | 0.75 (4 items, 4 pictures): **gate fail** | The older man's long, narrow yellow bag: "carrying something yellow", "looks like a bag", or "a folded newspaper or tag" (pictures 2 and 4, one reader, half marks). In pictures 21 and 45 it scored in full, though "too long for a shopping bag". The design tests also read it as "a long narrow bag, a folded newspaper or a plank or ruler". The drawing did not change in v0.24 and read in full in v0.23, so this may be variance, but the remarks are consistent | Redraw on the bench: wider and shorter, with two visible handles, seen flat on rather than edge-on |

The other half marks, each in one picture: a grandmother who "might walk into" a bucket but might "just miss it" (`about_to_trip`, picture 4); a teenager with the giant fork "as if using it as a shovel or broom" (`sweep_fork`, picture 10); a girl pointing "at the bird or at the man" rather than the sky (`rain_coming`, picture 27); a square wheel also offered as "a wheel seen oddly or a separate crate" (`square_wheel`, picture 50).

## Unintended oddities

Named kinds, from the scorers' lists (`scores_summary_a.md` to `_c.md`). Counts are of reports and are not comparable with earlier screens' (above).

| # | Sev | Oddity | Where | Fix for v0.25 |
|---|---|---|---|---|
| O1 | C | Figures "stiff, narrow, tall", tube-like sleeves, small hands, faces hard to read in profile (the largest group, about a third of all reports) | Throughout | The cast is a stand-in; note for final art |
| O2 | B | A large oval shadow under the wheelbarrow, "a large green oval" | Probes 62, 65, 67, 72 | Shrink it to the barrow's footprint: cheap and specific |
| O3 | C | A paint roller or brush "barely touching" the fence; a spade over the foot | Probes 58, 63, 70; 56, 72 | Look at both on the bench |
| O4 | C | The blue bird at the sandwich oversized or overhanging the lap, "a blue kettle or jug"; the sandwich read as on the lap | Set pictures 2, 7, 16, 55 | Note for the pilot; bench if it recurs |
| O5 | C | Feet straddling the edge of a path or pond | Pictures 2, 7, 11 | Note for the pilot |
| O6 | C | Older ones: goats hard to read or unexpected in a garden; wind with nothing else blowing; balloon strings ending in mid-air; a hose reel read as a fan or speaker; a slide's chute hovering above the grass; a kick caught before or after the ball leaves | Throughout | Note for the pilot, as since v0.11 |
| O7 | C | The curled-up sleeping cat "a tangle" or "hurt", while still read as asleep (design tests and the control) | Several | Note for the pilot |
| O8 | C | A figure against the shop fronts "looks large compared with the door" (design tests only; none in the screen) | Street | Revision 22 leaves the street alone; note for the pilot |

## For the next screen

Tell the scorers how much to log, or count the readers' remarks directly, so the oddity row means the same thing again. The remark count above can be taken from any screen's `desc_pic_NN.md`.
