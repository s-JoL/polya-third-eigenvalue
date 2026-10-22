import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

noncomputable section
namespace K3Paper

/-- The target lies strictly below the certificate energy. -/
theorem target_below_certificate : 12 * Real.pi < (377 / 10 : ℝ) := by
  have h := Real.pi_lt_d6
  linarith

/-- Rational pi bounds used by the exact B checker. -/
theorem checker_pi_bounds :
    (314159265358979 / 10^14 : ℝ) < Real.pi ∧
    Real.pi < (314159265358980 / 10^14 : ℝ) := by
  constructor
  · have h := Real.pi_gt_d20; linarith
  · have h := Real.pi_lt_d20; linarith

/-- The geometric thresholds and the overlap of the two window tests. -/
theorem parameter_identities :
    2*(9/20:ℝ)=9/10 ∧
    1-4*(1141/5000:ℝ)=109/1250 ∧
    (109/1250:ℝ)<879293/10000000 ∧
    (6/25:ℝ)<241/1000 ∧
    (6/25:ℝ)*(9/20)=27/250 := by norm_num

/-- Exact scalar inequality behind the monotonicity of the B slack variable. -/
theorem angle_budget (m x : ℝ) (hm : 0 < m) (hx : 0 ≤ x) :
    3*x ≤ 2*m + x^3/m^2 := by
  have hp : 0 ≤ (m-x)^2*(2*m+x) :=
    mul_nonneg (sq_nonneg _) (by linarith)
  have hid : 2*m+x^3/m^2-3*x = (m-x)^2*(2*m+x)/m^2 := by
    field_simp
    ring
  have hn := div_nonneg hp (sq_nonneg m)
  rw [← hid] at hn
  linarith

/-- Weighted cubic allocation: the minimization used in the B Hamiltonian. -/
theorem cubic_allocation (a b u v : ℝ)
    (ha : 0 < a) (hb : 0 < b) (hu : 0 ≤ u) (hv : 0 ≤ v) :
    (u+v)^3/(a+b)^2 ≤ u^3/a^2 + v^3/b^2 := by
  have hab : a+b ≠ 0 := ne_of_gt (by linarith)
  have hid : u^3/a^2 + v^3/b^2 - (u+v)^3/(a+b)^2 =
      (b*u-a*v)^2 * (b*(b+2*a)*u+a*(a+2*b)*v) /
        (a^2*b^2*(a+b)^2) := by
    field_simp
    ring
  have hn : 0 ≤ (b*u-a*v)^2 * (b*(b+2*a)*u+a*(a+2*b)*v) /
        (a^2*b^2*(a+b)^2) := by positivity
  rw [← hid] at hn
  linarith

/-- The exact one-variable minimization after the cap Holder estimate. -/
theorem cap_minimization (x c : ℝ) (hx : 0 < x) (hc : 0 < c) :
    4*c^3 ≤ x^3 + 3*c^4/x := by
  have hid : x^3 + 3*c^4/x - 4*c^3 =
      (x-c)^2*(x^2+2*c*x+3*c^2)/x := by field_simp; ring
  have hn : 0 ≤ (x-c)^2*(x^2+2*c*x+3*c^2)/x := by positivity
  rw [← hid] at hn
  linarith

/-- Eliminate cap mass, keeping the spectral threshold in the hypothesis. -/
theorem robin_elimination (lam upper nu mass capMass inside energy trace alpha : ℝ)
    (hnu : 0 < nu) (hu : 0 ≤ upper) (hupper : lam ≤ upper) (hbelow : upper ≤ nu)
    (hcap : 0 ≤ capMass)
    (hmass : nu*capMass ≤ energy) (htrace : alpha*trace ≤ energy)
    (hbalance : lam*(mass+capMass)=inside+energy) :
    inside+(1-upper/nu)*(alpha*trace) ≤ lam*mass := by
  have hweight : 0 ≤ 1-upper/nu := by
    apply sub_nonneg.mpr
    exact (div_le_one hnu).mpr hbelow
  have htr := mul_le_mul_of_nonneg_left htrace hweight
  have hcm : lam*capMass ≤ upper/nu*energy := by
    have h1 : lam*capMass ≤ upper*capMass := mul_le_mul_of_nonneg_right hupper hcap
    have h2 : upper*capMass ≤ upper/nu*energy := by
      have hh := mul_le_mul_of_nonneg_left hmass hu
      have ht : upper*capMass*nu ≤ upper*energy := by nlinarith [hh]
      calc
        upper*capMass ≤ upper*energy/nu := (le_div_iff₀ hnu).mpr ht
        _ = upper/nu*energy := by ring
    exact le_trans h1 h2
  nlinarith

/-- Pointwise Picone identity. Integration and endpoint traces are separate obligations. -/
theorem picone_identity (p q dq z dz lam : ℝ) (hp : p ≠ 0) :
    p*dq^2-lam*q^2 =
      p*(dq+z*q/p)^2 + (dz-z^2/p-lam)*q^2 - (dz*q^2+2*z*q*dq) := by
  field_simp
  ring

/-- A linear function on a rectangle is nonnegative if all four corners are. -/
theorem affine_rectangle (a b c xl xu yl yu x y : ℝ)
    (hx : xl ≤ x ∧ x ≤ xu) (hy : yl ≤ y ∧ y ≤ yu)
    (hll : 0 ≤ a*xl+b*yl+c) (hlu : 0 ≤ a*xl+b*yu+c)
    (hul : 0 ≤ a*xu+b*yl+c) (huu : 0 ≤ a*xu+b*yu+c) :
    0 ≤ a*x+b*y+c := by
  by_cases ha : 0 ≤ a <;> by_cases hb : 0 ≤ b
  · nlinarith [mul_nonneg ha (sub_nonneg.mpr hx.1), mul_nonneg hb (sub_nonneg.mpr hy.1)]
  · nlinarith [mul_nonneg ha (sub_nonneg.mpr hx.1), mul_nonneg_of_nonpos_of_nonpos (le_of_not_ge hb) (sub_nonpos.mpr hy.2)]
  · nlinarith [mul_nonneg_of_nonpos_of_nonpos (le_of_not_ge ha) (sub_nonpos.mpr hx.2), mul_nonneg hb (sub_nonneg.mpr hy.1)]
  · nlinarith [mul_nonneg_of_nonpos_of_nonpos (le_of_not_ge ha) (sub_nonpos.mpr hx.2), mul_nonneg_of_nonpos_of_nonpos (le_of_not_ge hb) (sub_nonpos.mpr hy.2)]

#print axioms target_below_certificate
#print axioms checker_pi_bounds
#print axioms parameter_identities
#print axioms angle_budget
#print axioms cubic_allocation
#print axioms cap_minimization
#print axioms robin_elimination
#print axioms picone_identity
#print axioms affine_rectangle
end K3Paper