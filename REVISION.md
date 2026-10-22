# Revision following the review of v0.2.0

The reviewed base is `8e1e2d5281b3e020c2823f0ef2c0a180a6907c91`. This revision keeps the title and Liang Song's authorship. It changes the exposition and corrects one integration endpoint in the numerical supplement; it does not change the theorem or the certificate arrays.

## Mathematical changes

1. The narrow-neck argument now starts with the explicit assumption `m′ ≤ 0.03`.
2. The perimeter function is defined separately at zero window: `P(0,s) = sqrt(4πs)`. The positive-window circular-arc estimate is not used there.
3. Three named lemmas now state and prove the strip rearrangement with its trace inequality, the window perimeter/coarea reduction with plateau and Stieltjes conventions, and the comparison for monotone BV paths. The last proof treats the absolutely continuous, singular continuous and atomic parts separately and explains both endpoints.
4. A finite-area spectral lemma explains coercivity, compact embedding on unbounded sets, multiplicities and min–max.
5. The introduction distinguishes the third-index result from an optimal shape bound and from recent all-index results. The geometric choice between perpendicular cuts is the central contribution. The cited Speciel and Tang–Wang preprint abstracts were checked on 22 October 2026; their full arguments were not newly reviewed in this revision.
6. The paper includes a proof dependency table and a B/T/S/N certificate table. Computational data remain ordinary supplementary material; the paper does not use source-code filenames in place of mathematical arguments.

## Numerical correction

The S checker now integrates from the Arb enclosure of the true initial angle π/2. Both A and B bounds clip their first integration cell; full-cell slope verification is unchanged. See ERRATA.md and the fresh replay records under `verification/revision-2026-10-22/`.

The old v0.2.0 records are retained as historical evidence. They should not be read as checks of the revised source. The displayed downward-rounded S bounds are retained only after comparison with the new replay.

## Formalization and submission

The article and numerical supplement are published together. The ongoing Lean development is maintained separately and has a locally checked bounded-domain spectral/min–max bridge, but the complete main theorem is not yet kernel-checked. No complete-formalization claim has been added to the article. The paper's mathematical proofs remain subject to expert review.

This is a revision of the public preprint and its supplement, not a journal submission. A submission should pair this PDF with the exact supplementary files named in its hash manifest. Journal choice and any required declarations should be settled against the actual submission requirements.
