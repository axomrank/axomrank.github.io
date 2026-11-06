# Mathematics visuals: the idea behind each scene

Decide what a concept *is* before drawing it. A scene must make the idea visible,
and the learner's action must be the mathematical act itself. A picture beside the
idea, or a formula with decoration, does not count. Scenes live in `app/mathstage.js`.

| Concept | What it really is | Scene | The act |
|---|---|---|---|
| Number, sign | A position; −3 is 3 reflected in 0 | `line` with `mirror` | Drag the pin; its reflection follows |
| Order | Further left is smaller | `line` | Compare positions, not digit size |
| Decimals | Each digit is one ×10 zoom | `line` | Zoom; the ladder shows where you came from |
| Fractions | The same points, named by cutting | `line`, `fracbar` | Fractions appear below the line, decimals above |
| Recurring decimals | A zoom that never lands | `line` with `pin` | Dive towards $\frac{1}{3}$; each level misses |
| Factor, prime | A rectangle the dots can make | `array` | Reflow the rows; primes never fit |
| HCF | The largest square that tiles a rectangle (Euclid) | `tiles` | Cut the biggest square until nothing is left |
| LCM | When two rhythms return together | `gears`, `hops` | Turn; the two marks touch at the meeting |
| Unit digits | Arithmetic on a ten-point clock | `dial` | Step powers until the path closes |
| Adding fractions | Pieces need common cuts | `cuts` | Change the cuts until every mark lands on one |
| Percent | Two scales on one length | `dual`, `grid100` | Slide one cursor across both rulers |
| Successive percent | Area: $\frac{ab}{100}$ is a real corner | `area` | Stretch both sides; watch the corner |
| Ratio | Counting equal blocks | `blocks` | Find what one block is worth |
| Proportion | Equal ratios share one line through 0 | `ray` | Multiplying stays on the line; adding leaves it |
| Linked ratios | B must be one size in both | `chain` | Stretch both rows until the B's align (LCM again) |
| Average | The level where surplus equals gap | `level` | Drag a line until above = gap |
| Consecutive numbers | Symmetry about the middle | `level` | Each value above cancels one below |
| Group average | A balance point, nearer the bigger group | `seesaw` | Slide the pivot until the beam is level |
| Order of operations | Multiplying makes groups, so groups resolve first | `order` | Tap the step that goes next; the line collapses |
| Square root | The side of a square with that area | `square` | Slide until the area fits |
| Perfect square | Every prime has a partner | `pairs` | Pair primes; what is left is the multiplier |
| $a^2 - b^2$ | A real rearrangement into a rectangle | `diffsq` | Slide the strip round to the side |
| Profit, discount | Two bases: cost, then marked price | `dual`, `ladder` | Mark up, discount, watch where selling lands |
| Same price, ±a% | The loss item cost more | `twosale` | Slide a; the pair always loses |
| Simple, compound interest | One repeated slice against interest on interest | `growth`, `area` | Slide the years; gold appears from year 2 |
| Time and work | A job of LCM units; rates add | `tank` | Run the days until it is full |
| Pipes | Work with a negative rate | `tank` | Add a draining tap; only the net rate matters |
| People and days | A fixed area, so one rises as the other falls | `mandays` | Reshape the rectangle |
| Trains | The tail must clear; only closing speed matters | `track` | Run time forward until the tail leaves |
| Average speed | Time-weighted: width is time, height is speed | `journey` | Level the line, as in Average |
| Ages | Both move together, so the gap is fixed | `ages` | Slide the years; the red gap never changes |
| AP | Counting steps: the first term has none | `stairs` | Slide the terms; gold shows n − 1 |
| Sum of an AP | Two copies make a rectangle | `stairs` | Add a flipped copy |
| GP | Repeated multiplying runs away | `stairs` in `gp` mode | Slide the terms |
| Trig ratios | Same shape, same ratio | `triangle` | Resize; sine does not move |
| Value table | A point on a radius of 1 | `quarter` | Rotate; sin is height, cos is width |
| Height and distance | One right triangle | `tower` | Raise it to the sight line |
| Scale | k times the side is k² the area, k³ the volume | `scaleup` | Count the copies inside |
| Triangle area | Half its box, wherever the top sits | `shear` | Slide the apex; the area stays |
| Triangle rule | Two sides must reach past the third | `sticks` | Slide until they close or fail |
| Rhombus | Half the box around its diagonals | `kite` | Fold the corners in |
| Circumference | One roll of the wheel | `roll` | Roll it; the ground shows the length |
| Circle area | Slices rearrange into πr × r | `sectors` | Cut finer until it is a rectangle |
| Perfect cube | Every prime in groups of three | `pairs` with `group: 3` | Group primes; what is short is the multiplier |
| Outer angle | The two far angles added | `exterior` | Move two angles; the outer one and the triangle's names follow |
| Tangent | A right angle with the radius | `tangent` | Slide Q; Pythagoras gives the distance |
| Fixed perimeter | One fence, many rectangles | `fence` | Change the length; the square holds the most |
| Volume | Layers of base area | `stack` | Build it up |
| Surface | What you can unfold | `net` | Unfold six squares |
| Cone | A third of its cylinder | `pour` | Three cones fill it |

Colour has one meaning everywhere: blue positive, red negative, gold zero, green fractions.

## Rules for new scenes

- **No answer before action.** A question's scene must not show its answer. The first LCM
  grid coloured the answer in advance, and the first equal-fractions task passed with
  nothing changed. Neither one measured anything.
- **Do, then discover.** A story card with `tasks` gives an instruction and a goal. The
  insight appears only when the goal is met. "Show me" is always available, so a card can
  never trap a learner, and Continue stays off until the tasks are done.
- **Honest units.** One tooth is one count, even though a 4-tooth gear looks plain.
- A scene exposes `state()` for goals and `demo(goal)` for "Show me". `scripts/check_math.py`
  rejects a goal the scene cannot report.

## Design direction

A maths exercise book, set only by `html.maths` in `app/math.css`: squared paper, red
margin, ballpoint ink. It re-points the app's colour tokens, so other courses are
unchanged. The number line is the one bold element and runs edge to edge.
