# Reproducing the computational supplement

The article and the software have different roles. The article proves the comparison principles and reductions. The programs check the resulting finite inequalities. Lean checks the auxiliary statements listed in [SCOPE.md](SCOPE.md). None of these roles should be inferred from an exit code alone.

## Inputs and dependencies

The pinned Python dependencies are in `requirements.txt`. Lean and mathlib are fixed by `lean-toolchain`, `lakefile.toml`, and `lake-manifest.json`. Install them as described in the README. `SHA256SUMS` records the released files; verify it with `sha256sum -c SHA256SUMS` before replay.

The numerical certificate arrays are the same arrays as in v0.1.0. The T verifier's root enclosure is corrected; see [ERRATA.md](ERRATA.md). Inputs are read with NumPy as numeric arrays. They are not executable serialized objects.

## Numerical verification

```bash
python scripts/check_constants.py
python scripts/check_data.py
python scripts/check_k3.py
```

The constant check uses exact rational alternating-series bounds for π and the first Bessel zero, then Arb interval comparisons. It separately checks the wider root bracket actually used by T. The data check verifies grid endpoints and ordering, array dimensions, index ranges, finite entries, and the complete parameter interval cover.

The k=3 replay copies its inputs to a fresh directory `build/replay-<timestamp>/`, records their hashes, and runs:

| Test | Required result |
|---|---|
| B | All 8,664 tetrahedra pass exact rational checks at excess 0.0872 |
| B control | The requested 0.09 bound is rejected |
| S | All eight mass intervals pass at energy 37.7 |
| S control | The deliberately stronger 37.975 test is rejected |
| Neck | 45.8318 passes on 100,000 cells |
| Neck control | 45.84 is rejected |
| T | All nine parameter boxes, 192,000 triangles each, pass the Arb checker |
| T control | A prescribed corrupted node is rejected |

Every run ends by verifying that the source inputs are unchanged. The receipt and individual logs remain in its build directory. A failed stronger check is a negative control, not a counterexample to that stronger inequality.

## Lean verification

```bash
lake build
python scripts/check_lean.py
```

The second command recompiles every source with warnings treated as errors and kernel type checking enabled. It checks that every theorem has an axiom report and that all dependencies lie in the stated standard set. An independent false lower bound must fail. The complete Lean source shipped here comprises the auxiliary development, conditional interfaces, and earlier torus algebra; it is not a complete formalization of the PDE theorem.

## Evidence and interpretation

`verification/v0.2.0/` contains the replay receipts, source hashes and relevant logs for this release. They are retained to make the reported checks inspectable; running the commands above supplies fresh evidence. Continuous-analysis arguments and the interpretation of certificate conditions still require mathematical review. This preprint has not been externally peer reviewed.

The old torus checks remain in `scripts/verify.sh` and in continuous integration. They are retained for the earlier public result and are not dependencies of the third-eigenvalue argument.
