# Pólya's inequality for the third planar Dirichlet eigenvalue

**Liang Song**

[Read the paper](paper/third-eigenvalue/paper.pdf) · [LaTeX source](paper/third-eigenvalue/main.tex) · [Verification guide](VERIFICATION.md) · [Chinese introduction](README.zh.md)

This repository accompanies a preprint on the inequality

$$ |\Omega|\lambda_3(\Omega)>12\pi $$

for every planar open set of finite positive area. Eigenvalues are Dirichlet eigenvalues, counted with multiplicity. The domain may have holes, may be disconnected, and need not be bounded.

The proof chooses an area-bisecting line and reflects the two halves. Two estimates for cross-sectional profiles show that either this cut, or a perpendicular bisector, has the required spectral bound. Rearrangement and one-dimensional comparison reduce these estimates to finite rational and interval inequalities.

The paper gives the mathematical argument and verification criteria. The computational supplement supplies the certificate arrays, executable checks, and Lean source. This is a research preprint, not a claim of journal acceptance.

## Current revision

The revised manuscript expands the analytic bridges and corrects the true π/2 integration endpoint in S. See [revision notes](REVISION.md), the [supplement map](SUPPLEMENT-MAP.md), and the fresh records in `verification/revision-2026-10-22/`. The previous release remains available as a historical version. Lean development is kept on a separate branch and has not completed the main theorem.

## Verification

| Material | What it establishes |
|---|---|
| [Paper](paper/third-eigenvalue/paper.pdf) | The analytic argument, including the geometric reduction and comparison principles |
| [Certificate data](certificates) and [replay](scripts/check_k3.py) | Exact rational verification of the pair-profile bound; Arb interval verification of the small-window, large-window and neck bounds |
| [K3Algebra.lean](K3Algebra.lean) | Nine universal auxiliary theorems: threshold and π bounds, parameter identities, cubic allocation, cap minimization, Robin elimination, Picone algebra and affine comparison |
| [K3Interfaces.lean](K3Interfaces.lean) | Parameter arithmetic and conditional assembly, with analytic assumptions explicit |
| [Recorded checks](verification/v0.2.0) | Source hashes, fresh compiler output, certificate results and negative controls |

**The complete spectral/PDE theorem is not yet formalized in Lean.** The Lean files do not define the Dirichlet spectrum of an arbitrary open set or prove the rearrangement, coarea and Sturm steps. Those arguments are in the paper. See [SCOPE.md](SCOPE.md) for the exact boundary. The general Pólya conjecture, for every index, is not claimed here.

## Reproduce the checks

Use Python 3.12 or later and [Lean's official installation](https://lean-lang.org/install/). Lean is fixed at 4.34.0 and mathlib at commit `5ed2965256430c3649e86755f9576b54eca72435`.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
lake update
lake exe cache get
lake build
bash scripts/verify.sh
```

The numerical checks take several minutes. Each k=3 replay creates a new directory under `build/`; it does not modify the shipped certificate arrays. Positive checks and deliberately false or corrupted controls are both required. A successful run means that the listed checks passed; it is not a replacement for reviewing the analytic argument.

To rebuild the paper with Tectonic:

```bash
python scripts/build_paper.py
```

The resulting `paper/third-eigenvalue/paper.pdf` is the document linked above. The article can also be compiled with a standard LaTeX installation from its source directory.

## Changes from the first release

Version 0.2.0 adds the English manuscript under Liang Song's name and nine Lean auxiliary theorems. It corrects the Bessel-zero enclosure in the small-window verifier and reruns all nine parameter boxes. It also rounds the paper's displayed mass lower bounds down. The numerical conclusions survive these corrections. Details are in [ERRATA.md](ERRATA.md).

The [earlier torus result](paper/torus.md), its [Lean source](FullTorus.lean), and the v0.1.0 release remain available. They are separate from the third-eigenvalue argument.

## Citation and license

Citation metadata is in [CITATION.cff](CITATION.cff). The manuscript and code are released under the [MIT license](LICENSE); external dependencies retain their own licenses, listed in [THIRD_PARTY.md](THIRD_PARTY.md).
