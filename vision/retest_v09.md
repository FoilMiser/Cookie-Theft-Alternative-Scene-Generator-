# Test-retest: the v0.9 pictures read again by fresh readers

The v0.9 gate fell from 60 to 54, and eight of its ten failures were within one half point of passing.
To measure how much of that movement comes from the readers rather than the pictures, the same 41
pictures (the 21 of the v0.9 set and its 20 probes, unchanged, in the same order) were screened a second
time, with the same prompts (`screen_prompts.md`): six new readers who had never seen the key described
them (`v09_retest/desc_pic_NN.md`), and two new scorers scored pictures 1 to 20 and 21 to 41 against the
same key (`v09_retest/scores_a.json`, `scores_b.json`, merged in `scores.json`). The gate is in
`v09_retest/gate.json`.

## Item by item

Of the 505 scored items, 489 (96.8%) got the same score both times. Of the 16 that differed, 13 were
scored higher the second time, and 13 of the 16 were a move between half and full credit: a reader who
offered two readings, or left the meaning implied, against one who stated it. Only three moved further:
a misread to full credit (the small sleeping cat), a misread to half credit (the floating box by the
house) and a half credit to a misread (the empty cone, "held to her mouth").

| | v0.9 screen | Retest |
|---|---|---|
| Things | 0.99 | 0.99 |
| Actions | 0.95 | 0.96 |
| Inferences | 0.91 | 0.94 |
| Contradictions | 0.95 | 1.00 |
| All items | 0.96 | 0.97 |
| Misread items | 1 of 284 | 1 of 284 |
| Unintended oddities per picture | 2.3 | 1.5 |

(The 21 set pictures, as in the release headline.)

## The gate

| | v0.9 screen | Retest |
|---|---|---|
| Pass | 54 | 59 |
| Fail | 10 | 5 |

The two screens agree on 59 of 64 templates. The five that failed both times are the five with a cause
visible in the picture: the dropped ice cream (0.78 and 0.80: the empty cone read as held to the mouth
again, once as "being eaten"), the fork on the stepping stones (read as digging again), the fence cat over
the clothesline (read as walking the line again), the bird across a roofline (read as perched again) and
the person about to trip between the clothesline posts (the book read as laundry again). The other five
v0.9 failures passed on the retest: the sleeping cat, the duck coming for the bread, the floating box, the
child at the foot of the slide and the upward stream. No template went the other way.

So about half of the v0.9 drop (five of the six templates lost) came from which readers saw the pictures,
and half from real faults that any reader finds. A template that fails the gate by one half point on two
pictures is as likely to be a hedge as a fault; one that fails with the same reading twice is a fault.

## What this changes

- The v0.10 fixes cover all ten v0.9 failures, but the five that failed twice come first (`flaws_v09.md`).
- Gate outcomes between releases move by about five templates on reader variance alone, so a change
  of a few templates is not evidence of a better or worse release. The headline means moved by at most
  0.05 per item type.
- Unintended oddities vary the most between screens (2.3 against 1.5 per picture for the same
  pictures), since readers differ in how much they list.
