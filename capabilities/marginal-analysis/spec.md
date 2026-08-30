---
type: spec
capability: marginal-analysis
engagement: perfect-competition
date: 2026-08-29
status: draft            # draft | built | audited
built_with: "not built yet"
---

# <Capability> — model specification

## Purpose
Farmer decided to plant 20 beds of tomatoes, 30 beds of carrots and 20 beds of mesclun for the season. We are trying to determine if this is the best or optimal number of beds of each produce given a number of constraints. These constraints include diminishing-returns % compounds and how many hours are worked by temporary workers.

## Inputs — the named contract
| Name | Value | Unit | Source |
|---|---|---|---|
| `TOM_MAX_BEDS`   | 20  | tomato beds  | Case scenario, crop table |
| `TOM_PRICE` | 8800 | USD per bed | Case scenario, crop table |
| `TOM_HRS_PER_BED`   | 2.5  | hours per week per bed | Case scenario, crop table |
| `TOM_FERT`   | 880  | USD per bed  | Case scenario, crop table |
| `TOM_DIM_RET`   | 10  | Labor-increase rate per additional tomato bed  | Case scenario, crop table |
| `WEEKS`   | 36  | weeks per season | Case scenario, crop table |
| `CAR_MAX_BEDS`   | 20  | tomato beds  | Case scenario, crop table |
| `CAR_PRICE` | 2094 | USD per bed | Case scenario, crop table |
| `CAR_HRS_PER_BED`   | 0.833  | hours per week per bed | Case scenario, crop table |
| `CAR_FERT`   | 440  | USD per bed  | Case scenario, crop table |
| `CAR_DIM_RET`   | 2.5  | Labor-increase rate per additional tomato bed  | Case scenario, crop table |
| `WEEKS`   | 36  | weeks per season | Case scenario, crop table |
| `MES_MAX_BEDS`   | 30  | tomato beds  | Case scenario, crop table |
| `MES_PRICE` | 2700 | USD per bed | Case scenario, crop table |
| `MES_HRS_PER_BED`   | 1.25  | hours per week per bed | Case scenario, crop table |
| `MES_FERT`   | 880  | USD per bed  | Case scenario, crop table |
| `MES_DIM_RET`   | 1.25  | Labor-increase rate per additional tomato bed  | Case scenario, crop table |
| `WEEKS`   | 36  | weeks per season | Case scenario, crop table |

Every input gets a name, a value, a unit, and a source. You choose the names.
The requirement is that they exist and are used consistently below.

## Structure
Each region
Inputs, Cost Structure
Marginal-Cost Schedules
Optimization 
Checks

## Calculation logic
In named-range notation, never cell addresses:

  LABOR_HRS(q) = q x HRS_PER_BED x WEEKS x (1 + DIM_PCT)^q

"Column D times column E" is not a specification — it describes a spreadsheet
that does not exist yet.

The supplied labor formula means that the diminishing-return multiplier applies to all beds of that crop at quantity q. Marginal cost means the change in total cost when production increases from q − 1 to q. Specify the revenue, labor, fertilizer, total-cost, and profit calculations without cell addresses.

## Conventions
The rules that are not visible in the formulas: costing order, allocation basis,
rounding, what happens at the boundaries. State all of them. A convention you
leave out is a convention the builder invents.

64 beds is a maximum, not a requirement to plant all 64.
Bed counts must be nonnegative whole numbers.
The farmer’s 720 field hours are used before temporary-worker hours.
The case requires labor allocation at a blended rate.
Explain rounding and how zero production is handled.

Your brief also assumes whole temporary-worker salaries are paid. Make sure that treatment matches the detailed Stage 2 instructions; it affects profit materially.

## Validation rules
The conditions the finished artifact must satisfy — check figures as acceptance
criteria, hand calculations, and structural rules ("every calculated cell
contains a formula", "no error cells").

TOM_LABOR_HRS(1) = 1 × 2.5 × 36 × 1.10 = 99 hours

Also require every calculated cell to contain a formula, no spreadsheet error cells, and compliance with all capacity limits. Add the instructor’s complete Stage 2 check figures—the section referenced as “below” was missing from your paste.

## Outputs
Each result the model reports, by name.

Identify the results needed: crop quantities, workers required, labor usage, revenue, costs, profit, marginal costs, and unused capacity. Leave Audit findings empty until you actually build and check the workbook.

## Audit findings
Added AFTER the build. For each check: what you checked, what you found, what
you did about it.
