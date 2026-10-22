# Computational supplement map

The article labels its finite calculations B, T, S and N. Its mathematical criteria are stated in the article; this table locates their implementations.

| Test | Files | Mathematical use | Acceptance |
|---|---|---|---|
| B | `certificates/B/certE_exact.py`, `wE3_W090_32_snap.npz` | Piecewise affine comparison for a pair of profiles | 8664 tetrahedra; every final rational rectangle check; excess > 0.0872 |
| T | `certificates/T/ctangle.py`, `ctcert.py`, `barriers/*.npz` | Two derivative inequalities for the small-window angular barrier | Nine mass boxes, 192000 triangles each, no failing triangle |
| S | `certificates/S/cert_slices2.py`, `cert_slice.py`, `cert_common.py` | Potential inequalities covering all large-window trajectories | Eight intervals; each required mass lower bound exceeds its upper mass endpoint; true π/2 origin |
| N | `certificates/S/cert_riccati.py` and common constants | Narrow-neck Riccati comparison | No pole, 100000 cells, lower bound 45.8318 |

Run `python scripts/check_k3.py` with the dependencies in `requirements.txt`. It creates an immutable-input replay directory in `build/`, tests all four groups, and requires the deliberately stronger or corrupted controls to fail. No optimization is rerun. See `verification/revision-2026-10-22/` for this revision's records and `SHA256SUMS` for the shipped bytes.

Lean is a separate companion project. Its current checked statements do not replace any of these analytic or interval-arithmetic obligations and do not constitute a complete formalization of the paper.
