# Marginal Analysis

**Capability:** Constrained profit optimization using marginal-cost reasoning
(P = MC) under price-taking conditions.

**Exercised in:** Perfect Competition case, Stage 2 — determining the
profit-maximizing crop mix (tomatoes, carrots, mesclun) for a market-garden
farm subject to bed caps, a total-acreage limit, and a compounding
labor-hour constraint.

**Contents of this folder:**
- `spec.md` — the model specification, written before the workbook existed,
  including validation rules and audit findings recorded after the build.
- `model.xlsx` — the workbook generated from the spec, with the optimal
  crop mix found via Excel Solver (GRG Nonlinear).

**Result:** 10 tomato beds, 20 carrot beds, 30 mesclun beds; season profit
$42,761.67, matching the case's published check figures ($42,762) within
rounding.
