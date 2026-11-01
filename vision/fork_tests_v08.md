# The giant fork, tested on its own before going back into the set (v0.8)

Three screens in a row failed the giant fork: v0.5 and v0.6 readers saw a garden fork someone leaned on
or dug with; v0.7 readers saw "a long fan rake" or "a litter picker" (`fork_v07_for_comparison.png`:
two v0.7 scene crops and the v0.7 gallery render). v0.8 redrew it and read it blind on its own, then in
four test scenes, before it went back into the generated set. The pictures are in `fork_tests_v08/`.

## The redraw

- **Outline.** A dinner fork's proportions scaled to a person's height (1.30 u, about the height of a
  grown-up's chest): four tines 0.30 u long and 0.032 u wide with 0.028 u gaps, a head no wider than the
  tines, rounded shoulders down to a 0.046 u neck, and a flat handle that widens to a rounded end
  0.135 u across. It is one flat plate cut to that outline (`flat_prism` in `castlib/core.py`,
  `giant_fork_outline` in `castlib/actions.py`), so the silhouette is exact at any size.
- **Pose.** Held like a broom (`sweep_giant_fork`): the tine tips on the ground ahead and to one side,
  the flat face turned to the viewer, both hands on the handle, leaning into the stroke.
- **Context.** Swept on a path or pavement only, with a heap of grey dust and grit (two paper scraps)
  pushed ahead of the tines, a cloud of dust over it and sweep marks behind; the heap is reserved when
  the sweeper is placed, so it is never left out.

## The reads

Each reader was a fresh model that saw only its one picture, with the screen's reader prompt.

| Picture | What the reader said about the fork | Called it wrong or odd | Action |
|---|---|---|---|
| `figure.png` (one figure, white page) | "It is a giant metal table fork, the dinner fork you eat with." Alternatives in order: a garden or digging fork, a pitchfork (less likely: "no wooden handle and the prongs are short, flat and close together"), a carving fork | "An ordinary dinner fork is drawn at a huge size and held like a tool" | Holding it, prongs at the ground ("digging … or leaning on it"): no context to sweep |
| `scene_1.png` (street, grandmother) | "a giant silver dinner fork as tall as she is, held like a broom with the tines on the ground" | "The odd thing is what she sweeps with" | Sweeping a small pile of dirt and litter |
| `scene_2.png` (park, on the path) | "a normal dinner fork blown up to tool size", "shaped exactly like a dinner fork with four prongs" | "The odd or impossible thing is the fork" | "raking or sweeping the rubbish" |
| `scene_3.png` (garden, stone path) | "a giant silver dinner fork instead of a rake"; "it is clearly shaped like a dinner fork, not a garden fork or rake" | "the obviously impossible thing in the picture" | Sweeping a pile of rubbish |
| `scene_4.png` (street, busy) | "a huge silver fork, using it like a broom" | "This is the obviously wrong or impossible part of the picture" | Sweeping a small pile of dirt and litter |

All four scene readers named a giant fork (three of them a dinner fork, the fourth "a huge silver fork") and
called it the impossible thing; three of four called the action sweeping. Two found the dust heap "small and hard to make out"; it is the heap the set
uses (already 1.7 times the first try).
