# The v0.10 changes, read blind in test scenes before going into the set

The v0.9 screen and its retest (`retest_v09.md`) left ten templates under the gate, five of them failing
both times for a cause visible in the picture (`flaws_v09.md`). v0.10 redesigned the dropped ice cream
and changed the placements behind the other failures, then read the changes blind in test scenes before
regenerating the set, as v0.8 and v0.9 did. Each reader was a fresh model that saw only its one picture,
with the screen's reader prompt (`screen_prompts.md`). The pictures and descriptions are in
`design_tests_v010/`.

## The reads

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (park) | Dropped ice cream; curled sleeping cat; crumbs floating ahead of the duck; smaller flying bird; photographer in three-quarter view | "Holding an empty ice-cream cone in one hand and has the other hand up at their face, looking upset or crying; the pink scoop with sprinkles has fallen onto the ground ... A brown dog ... has its head down in the dropped ice cream and is eating it." The cat "lies stretched out asleep". The duck swims "toward the man and the crumbs", more crumbs "floating on the water near the duck" (coming for them, not said to be going to eat them). The dog's head "pressed right onto the pink scoop", hard to tell "where the dog's head ends and the ice cream begins" |
| `test_2.png` (street) | Dropped ice cream; upward stream below the awnings | The girl "holds an empty ice-cream cone and has a hand to her face as if she is crying ... a brown dog ... apparently eating the ice cream she dropped". The water "arcs up and over the flowers ... rather than simply pouring down", read two ways: "a spray arcing up and falling onto the flowers", or "water flowing upward, which is odd". The dog's head again "merge[s] a little" with the scoop |
| `test_3.png` (playground) | Child half way down the slide; teenager and child on the seesaw; smaller sandwich | The girl "is halfway down a yellow slide ... her arm raised as if she is enjoying the ride". The seesaw riders: one "up in the air", one "down at the low end with their feet on the ground", but the plank "seems to pass behind or across their legs" and the high child's feet "rest on the plank". The bird "about to steal or peck at her food while she is too busy reading to notice" |
| `test_4.png` (garden) | Giant fork on the paved path; floating box clear of the house; curled cat | The fork "pushing down ... where the prongs hit the path there is a small grey pile of rubble or dirt and a puff of dust, as if he has just struck or scraped something": used "like a garden fork", digging. The box "in mid-air ... falling, flying or thrown". The cat "apparently asleep" |

Four changes followed:

- **The fork's heap.** The white chips that made the heap look like broken paving are gone, the heap
  stays on the paving (in `test_4` it lay on the grass beside the path), and a red dustpan waits beyond
  it.
- **The upward stream.** It now leaves the spout already rising, like a pour turned upside down (starting
  down toward the flowers and curving up, it read as a spray arcing over them).
- **The dog at the ice cream.** Its nose meets the far side of the scoop instead of its head lying over
  the top.
- **The ordinary seesaw.** Two children of a size wherever two are free; with a teenager and a child,
  the child up high holds on with the legs hanging, as the stranded child does.

Two pictures were then read again, one reader each:

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_5.png` (garden) | The fork's heap on the paving, with a dustpan | "Using a giant silver dinner fork, as big as a rake, to sweep or rake a small grey pile of dirt or gravel on the path ... A red dustpan ... presumably for collecting the swept dirt." The fork "looks deliberately absurd" |
| `test_6.png` (street) | The rising stream; the dog's nose at the scoop | "The water does not fall onto the flowers. It arcs upward and backward from the spout, ending in drops in the air ... as if the water is flowing up ... The strangest thing in the picture is the water rising out of the watering can instead of pouring down." The girl "holds an empty ice-cream cone and rubs her eye as if she is crying. Her pink scoop of ice cream has fallen"; the dog "with its nose right at the dropped ice cream" |

The empty cone, read in none of the v0.9 pictures, was read in all three test reads (the park picture,
and the street picture before and after the stream change), each time with the child upset and the scoop
dropped.
