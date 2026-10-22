# Scope of the Lean development

The complete PDE theorem in the paper is **not** formalized in Lean. A compiled auxiliary theorem does not imply that the analytic objects satisfy its hypotheses.

## Third eigenvalue: unconditional auxiliary theorems

`K3Algebra.lean` contains nine declarations.

| Declaration | Statement checked by Lean | Analytic work outside this declaration |
|---|---|---|
| `target_below_certificate` | 12π < 377/10 | A spectral estimate for an actual domain |
| `checker_pi_bounds` | Exact rational lower and upper bounds for π | Correctness of the full finite checker |
| `parameter_identities` | Threshold arithmetic and overlap of window ranges | Geometric selection of a cutting line |
| `angle_budget` | 3x ≤ 2m + x³/m² for m > 0, x ≥ 0 | Prüfer transformation and integration |
| `cubic_allocation` | Weighted cubic allocation inequality | The full Hamiltonian and all certificate cells |
| `cap_minimization` | The scalar minimization after Hölder | Hölder, slicing and trace admissibility |
| `robin_elimination` | Elimination of cap mass from explicit energy assumptions | The PDE estimates providing those assumptions |
| `picone_identity` | The pointwise algebraic identity | BV/Stieltjes integration and endpoint terms |
| `affine_rectangle` | Four corner inequalities imply an affine inequality throughout a rectangle | Decoding the data and complete subdivision coverage |

All nine are universal statements. They are not numerical samples of their variables.

## Conditional assembly

`K3Interfaces.lean`, retained from v0.1.0, contains threshold arithmetic, selection logic and a scalar square identity. Its four-gate theorem takes the analytic conclusions as explicit hypotheses. It does not prove those hypotheses. In particular, its convenient abstract gate formulation must not be mistaken for a stronger spectral conclusion than the paper proves.

## Earlier torus material

`FullTorus.lean` proves polynomial identities and positive Bernstein expansions on an entire cosine square, hence all real phases for those scalar expressions. It does not prove the raw finite-element assembly, complex matrix identification, Fourier decomposition or full inertia return. This separate result is not used in the third-eigenvalue paper.

## What a complete formalization still requires

The missing development includes the Sobolev form domain and Dirichlet spectrum for finite-area open sets, min–max bracketing, sign-part admissibility, Faber–Krahn and rearrangement in the needed form, trace-support and coarea/Stieltjes arguments, Sturm/Prüfer comparison, approximation of measurable profiles, and certified interpretation of the finite data. These have not been replaced by custom axioms or opaque theorem declarations.

Every shipped theorem has an axiom report. The accepted standard dependencies are `propext`, `Classical.choice`, and `Quot.sound`. The replay rejects `sorry`, `admit`, new `axiom`/`opaque` declarations and native unchecked decisions, and enables kernel type checking. A false lower bound must fail independently.
