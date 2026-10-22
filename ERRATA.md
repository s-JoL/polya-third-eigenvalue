# Corrections to v0.1.0

## Bessel-zero enclosure in the small-window verifier

The original T verifier parsed a long decimal approximation to the first positive zero of J₀ at 100-bit precision, discarded the conversion radius with `mid()`, and attached a radius of `1e-45`. The midpoint rounding error was larger than that radius. Both endpoints of the resulting narrow interval had negative J₀, so the interval did not enclose the zero. A successful run of that version alone is insufficient certification of T.

The corrected verifier uses

```
2.40482555769577276 < j_{0,1} < 2.40482555769577277
```

and checks the opposite signs of J₀ with Arb before taking the union of the endpoint intervals. The conversion radii are retained. The constant checker independently verifies the endpoint signs with exact rational bounds for the Bessel series. The estimate J₁(x) ≥ x(1 − x²/8)/2 > 0 identifies the first zero in this range.

All nine small-window parameter boxes pass with the corrected enclosure. Each box contains 192,000 triangles. Corrupting the designated barrier node is still rejected. The underlying certificate arrays have not changed.

The old release and its receipts remain historical records; the T entries in those receipts are superseded by v0.2.0 verification.

## Displayed mass lower bounds

Some old logs rounded a lower bound to the nearest seven-place decimal. For example, 0.2100008616… was displayed as 0.2100009. That display is an approximation, not a valid lower bound. The current paper truncates these bounds downward to six decimal places. The internal interval tests did not use the rounded display and are unaffected.

## The small-window barrier

The piecewise affine function is Θ; the actual comparison function is ρ = 20 cot Θ and is piecewise smooth. The paper states the conditions for Θ and derives the corresponding conditions for ρ. Earlier descriptions that called ρ piecewise affine should be read with this correction.

## True initial angle in the large-window verifier (post-v0.2.0)

The angular grid contains the exact binary64 value `math.pi / 2`, which lies just below the mathematical initial angle. The previous accumulation of A and B included the short interval between these two points. Checking the sine extremum on that cell did not correct its integration length.

The verifier now clips the first integration cell to the Arb enclosure of the true pi/2, in both the A and B bounds. All slope feasibility checks still cover the full original cell. The dip bound starts at the prescribed floor and requires no such correction. Replay records store the initial-angle convention and the enclosed grid-origin offset. Historical S receipts remain available but do not certify the corrected implementation.

Fresh replay of the corrected source passed all eight S intervals, all nine T boxes, B and the neck calculation, together with their stronger-bound and corrupted-node controls. The smallest S mass margin exceeds 0.00114; all downward-rounded bounds displayed in the article remain valid. Records are in `verification/revision-2026-10-22/certificates/`.
