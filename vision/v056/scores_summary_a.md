# Scores summary, set A (v0.56, 25 pictures)

Coverage check: all 278 items in keys_a.json across all 25 pictures have exactly one score each in scores_a.json. None is missing, none is invented, and the picture and item ids match the key exactly (checked by script).

## Mean score by item type

| Type | Items | Total | Mean |
|---|---|---|---|
| entity | 169 | 168 | 0.994 |
| action | 68 | 68 | 1.000 |
| inference | 15 | 14.5 | 0.967 |
| contradiction_notice | 13 | 13 | 1.000 |
| contradiction_explain | 13 | 12.5 | 0.962 |
| **All** | **278** | **276** | **0.993** |

No item was scored "misread".

## Items scored 0, 0.5 or misread

| Pic | Id | Score | Target | What the describer said |
|---|---|---|---|---|
| pic_10 | i03 | 0.5 | The man is much heavier, so the girl is stuck up in the air | The man "does not seem to be paying attention to the girl" and she is calling out "maybe because she is stuck up in the air". The unsure section gives a second reading ("just sitting there reading while she plays"). The man's weight is never mentioned. |
| pic_16 | i11 | 0.5 | The person is sitting on nothing: there is no chair or bench under them | This appears only in the unsure section: "I can't see a chair, stool or bench under him; he appears to be sitting on nothing (could be a missing seat, or something hidden I can't make out)". The free description just says he "sits drinking". |
| pic_16 | i20 | 0 | There are a few white clouds | Not mentioned. Only the sun is named. |

## Judgement calls scored 1

- pic_02 i04 (walking a dog): the describer said she is walking the dog on a lead, but the unsure section adds that the dog might be pulling her.
- pic_12 i02 (walking a dog): the describer said she is walking the dog, but the unsure section says she and the dog face opposite ways, so she may be "pulled the other way".
- pic_04 i04 (dog blocking the water): stated in the free description, but the unsure section adds that the dog "could also simply be standing there by chance".
- pic_09 i03 (box floating): the box is described as "hanging in mid-air". The unsure section also gives "thrown over the fence" as a reading beside floating.
- pic_10 i02 (girl calling out): her open mouth is read "as if calling out", but the unsure section says she could also be complaining or just talking.
- pic_13 i05 (woman reaching for the hat): the unsure section says her gesture "could also be read as waving".
- pic_01 i03, pic_13 i04, pic_17 i07 (fish in the tree): each is called impossible. The unsure sections also offer a fish-shaped toy or ornament (pic_01), "a bird drawn as a fish" (pic_13), or a toy or kite shaped like a fish (pic_17).
- pic_16 i10 (notice: how the person is sitting): the oddity is noticed only in the unsure section, with a hedge.
- pic_17 i03 (bird stealing the sandwich): "about to steal" is stated, but the unsure section adds that the bird "could be ... just standing next to it".
- pic_18 i04 and i05 (kite stuck in the tree): "his kite is caught", but the unsure section adds it "could be ... flying low in front of it".
- pic_22 i03 (frying pan): the describer said frying pan is the most likely reading, but also offered "a dark ladle/scoop".
- pic_24 i02 and i03 (dog begging): the unsure section says the pose "could also read as just sitting tall".
- Age labels (near words) on action items, where the action itself was right:
  - "boy" for teenager: pic_04 i14, pic_06 i02, pic_10 i04, pic_16 i17, pic_17 i01, pic_22 i04.
  - "older/elderly woman" for grandmother: pic_04 i01, pic_08 i02, pic_14 i02, pic_16 i01, pic_24 i04, pic_25 i01.
  - "elderly man" for grandfather: pic_16 i09.

## Unintended oddities, grouped by kind

**Drawing clarity (an element is hard to read)**
- pic_01: the sprinkler's water arcs are separate thin lines, so it is unclear where the spray starts.
- pic_03: the soil on the spade looks like a separate brown object (a bag or rock) resting on the blade.
- pic_07: the garden hose is very short, only a short loop from the reel to the nozzle.

**Pose and direction**
- pic_10: the man sits awkwardly on the very end of the seesaw with his legs over the plank.
- pic_16: the man in green holds the fork tucked under his arm with his hand at his chest, an awkward pose.
- pic_12: the woman faces and steps right while the dog walks left on a taut lead [dog, profile].

**Scale**
- pic_06: the red bird looks fairly large next to the woman's feet [bird, profile].

**Physical effects**
- pic_13: the wind streaks are on the far side of the blowing cap, so the wind direction is unclear.
- pic_04: water drips and a small puddle forms at the hose reel.

**Unusual but plausible content**
- pic_04: the fence being painted pink looks unusual.
- pic_12: a wine-like green bottle is in the basket of a child picnicking alone.
- pic_19: a goat in a town park is a little out of place [goat, three-quarter front].

**Oddities about animals, counted by angle**
- profile: 2 (pic_06 bird, pic_12 dog)
- three-quarter front: 1 (pic_19 goat)
