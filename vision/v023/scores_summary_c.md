# Scores summary, set c (v023, pic_44 to pic_65)

Sources: the 22 `desc_pic_*.md` files scored against `keys_c.json`. The per-item scores and evidence are in `scores_c.json`.

**Completeness check:** keys_c.json has 22 pictures and 220 items. scores_c.json has the same 22 pictures and 220 items. Every key item has exactly one score. No item is missing, and no item or picture was added that is not in the key. Every score is one of 0, 0.5, 1 or "misread". This was checked with a script that compares the two files.

## Mean score by item type

| Item type | n | Mean |
|---|---|---|
| entity | 122 | 1.00 |
| action | 64 | 1.00 |
| inference | 16 | 1.00 |
| contradiction_notice | 9 | 1.00 |
| contradiction_explain | 9 | 1.00 |
| **all items** | **220** | **1.00** |

## Items scored 0, 0.5 or misread

None. No item was scored 0, 0.5 or misread.

### Credited 1, with caveats worth knowing
These items still got full credit under the rules, but the description differed from the key in some detail.

- **The person doing the action is described differently from the key.** The action itself is right.
  - pic_48 i01, teenager drinking on the bench: called "a woman".
  - pic_56 i02, teenager feeding the birds: called "a woman in a blue hoodie".
  - pic_57 i04, teenager reading while walking: called "a woman in a blue hoodie".
  - pic_52 i02, woman sweeping: called "a girl (or slim young woman)".
  - pic_54 i01, woman sitting and reading: called "a girl (child or slim young woman)".
  - The "teenager in a blue hoodie" figure is read as a woman 3 times, as a boy twice (pic_47, pic_49) and as a young man once (pic_55).
- **A detail of an object differs.** pic_44 i05: the key's "wooden box" is described as a "brown cardboard box with tape stripe".
- **Part of the target is not mentioned.**
  - pic_60 i02 and pic_63 i02: the girl is described as "stuck up in the air", but "calling out" is not mentioned and her face is read as neutral.
  - pic_61 i12: the girl reaching for her balloon is not described as upset.
- **The describer committed to a reading but added a hedge in the "unsure" section.**
  - pic_44 i04 and pic_61 i11: the cat is stalking the bird, or maybe just walking.
  - pic_55 i03: she will trip over the box, or maybe walk past it.
  - pic_46 i01: she is hanging up the laundry, or maybe taking it down.
  - pic_61 i14: the balloon escaped, or maybe it was never hers.
  - pic_54 i03: she is sitting with no chair, or maybe squatting (the describer rejects squatting).
  - The rule gives 0.5 only when the target meaning is *only* offered as one of two readings. Here the free description states the target meaning outright, so these got 1.

## Unintended oddities (reported by the describer, not scored items), grouped by kind

There are 22 in total across 15 pictures. Seven pictures report none: 47, 49, 50, 52, 53, 54, 55, 65.

**Overlap, occlusion or unclear contact (7)**
- pic_45: the slide ladder leans on the outside of the frame, and its join to the platform is vague.
- pic_46: the woman's head overlaps the striped towel, so she seems to stand among the laundry.
- pic_51: the girl's legs are hidden behind the sandcastle, with one shoe showing below it (judged normal).
- pic_60: the seesaw plank passes behind the man's body, so it is "a little unclear" whether he is sitting on it or floating.
- pic_63: the same plank-behind-the-body overlap (the same scene template as pic_60).
- pic_62: the woman's legs stretch off the picnic blanket, "slightly offset".
- pic_64: the woman's body overlaps the pond because of perspective (read as standing in front of it).

**Out-of-place or unexplained elements (5)**
- pic_44: a hose reel stands on the open lawn (judged "not really odd").
- pic_57: a hole is being dug in the middle of the lawn rather than in a flower bed.
- pic_59: a brown dog is loose, with no owner or leash in sight.
- pic_59: some crumbs sit at the pond's edge, so it is unclear whether they are on the water or the grass.
- pic_61: the freshly painted blue section of the fence could be read as a blue gate.

**Pose or figure rendering (4)**
- pic_45: the girl's raised arms could mean cheering or holding her head.
- pic_56: the goat is in a bent, hunched, contorted pose and could be taken for a sheep or a dog.
- pic_57: the begging dog is drawn very upright and stiff.
- pic_58: the older man's eyes look closed, and a grey patch could be hair or glasses.

**Something the describer took to be a deliberate "wrong thing" that the key does not list (2)**
- pic_48: the sprinkler is read as mis-aimed and named "the 'wrong' thing in the scene". This is an inference scene (the package getting soaked) treated as a contradiction.
- pic_56: a goat loose in a public park is flagged as possibly "the odd thing in the picture".

**Ambiguous motion lines (2)**
- pic_60 and pic_63: the lines under the girl's feet could mean she is kicking impatiently or bouncing.

**Scale or perspective (1)**
- pic_48: the man carrying the box is too large for his distance, so he could look like he is walking on top of the hedge.

**Support or floating (1)**
- pic_59: the ball in the tree seems to rest on a branch rather than being caught in it, "slightly floaty-looking".
