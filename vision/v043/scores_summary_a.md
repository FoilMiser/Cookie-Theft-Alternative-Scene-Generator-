# v0.43 picture descriptions scored against keys_a.json

Sources: desc_pic_01.md to desc_pic_24.md and keys_a.json only. Full scores are in scores_a.json.

## Coverage check

- keys_a.json has 24 pictures and 231 items. scores_a.json has 24 pictures and 231 scored items.
- Every key item has exactly one score. No item is missing and none is invented (checked by script: ids in scores_a.json match the key ids for every picture).
- Every score is 1, 0.5, 0 or "misread". No picture has more than three unintended oddities.

## Mean score by item type

| Item type | Items | Mean | 1 | 0.5 | 0 | misread |
|---|---|---|---|---|---|---|
| entity | 146 | 1.000 | 146 | 0 | 0 | 0 |
| action | 58 | 1.000 | 58 | 0 | 0 | 0 |
| inference | 9 | 1.000 | 9 | 0 | 0 | 0 |
| contradiction_notice | 9 | 0.944 | 8 | 1 | 0 | 0 |
| contradiction_explain | 9 | 0.944 | 8 | 1 | 0 | 0 |
| **all** | **231** | **0.996** | 229 | 2 | 0 | 0 |

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_09 | i09 | contradiction_notice | Something is wrong with the dog | 0.5 | Never calls the dog odd. It only appears in the unsure section, where the dog "could be 'reading' it (comically) or about to chew/tear it". |
| pic_09 | i10 | contradiction_explain | The dog is reading a newspaper, but dogs can't read | 0.5 | Dog reading is one of two readings: "reading it or about to tear it". The dog lying on the paper is described correctly (i08 = 1). |

No item scored 0 or misread.

Scored 1, but worth knowing:
- pic_18 i01: the man with the hose is called "a boy" all the way through. The action is right.
- pic_16 i02: the boy is "holding" the ice-cream cone; the describer never says he is eating it.
- pic_21 i02: the girl reaching for the balloon is described, but not as upset.
- pic_09 i04: the cat is "creeping toward" and "stalking" the bird, but the unsure section adds "or just walking along the fence".
- pic_02 i03, pic_03 i05 and pic_04 i03 are stated in the free description and then hedged in the unsure section, which leans towards the intended reading each time.

## Unintended oddities (8 in 7 pictures)

Grouped by kind:

**Set or prop construction (3)**
- pic_09: the top of the blue-painted fence section is uneven, with pointed pickets on the left and a flat, lower top on the right, unlike the rest of the fence.
- pic_11: the swing frame has only one swing ("a little unusual").
- pic_23: the branch the fish sits on seems to grow from the trunk specially for it.

**Odd placement on the fence (2)**
- pic_04: the cat's feet sit right on the pointed tops of the fence boards [cat, profile].
- pic_14: the boy flies the kite standing right up against the fence.

**Body or prop overlap, attachment unclear (2)**
- pic_12: the old man's shins and feet appear to cross over the seesaw plank ("a slightly awkward overlap").
- pic_21: it is hard to see where the swing ropes attach; the child sits partly in front of them.

**Unintended story cue (1)**
- pic_09: the cat is standing on the freshly painted, possibly still wet, fence section [cat, profile].

The fence is involved in 4 of the 8 oddities (pic_04, pic_09 twice, pic_14).

### Animal oddities by angle

| Angle | Animals in the keys | Oddities | Which |
|---|---|---|---|
| profile | 5 (cat pic_04, cat pic_09, bird pic_09, dog pic_09, cat pic_14) | 2 | cat pic_04 (feet on fence points), cat pic_09 (on wet paint) |
| three-quarter front | 6 (dog pic_07, dog pic_09, duck pic_10, bird pic_13, cat pic_21, duck pic_22) | 0 | none |
| three-quarter back | 1 (dog pic_18) | 0 | none |

Neither animal oddity is about how the animal is drawn (legs, head or body shape). Both are about where the cat stands on the fence.

### Noted but not counted

These were left out because they are hedges about small details, or because the describer said they read fine:
- pic_01 and pic_15: the old man's legs overlap the seesaw plank (pic_01) and the fisherman overlaps the pond edge (pic_15). Both "read as" sitting or standing on the bank.
- pic_02: the woman's glasses "look like they have one dark lens".
- pic_03: it is hard to tell whether the kite string passes in front of or behind the trunk.
- pic_06: the ladder's base overlaps the edge of the path.
- pic_17: a small yellow shape under the girl, probably her shoe, sits at the edge of the plank.
- pic_18: a "wider dark blob" on the hose under the dog, which could be a squashed section or a puddle.
