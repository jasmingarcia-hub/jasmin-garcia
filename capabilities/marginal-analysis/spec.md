---
type: spec
capability: marginal-analysis
engagement: perfect-competition
date: 2026-08-29
status: draft            # draft | built | audited
built_with: "not built yet"
---

# Marginal Analysis — model specification

## Purpose
A farmer decided to plant 14 beds of tomatoes, 20 beds of carrots and 30 beds of mesclun for the season. The model must determine the most profitable combination of beds of each produce given a number of constraints to include land, crop and labor limits. Diminishing returns affect labor requirements and the capacity limits are the constraints.

## Inputs — the named contract
| Name | Value | Unit | Source |
|---|---|---|---|
| `TOM_MAX_BEDS`   | 20  | tomato beds  | Case scenario, crop table |
| `TOM_PRICE` | $8800 | USD per bed | Case scenario, crop table |
| `TOM_HRS_PER_BED`   | 2.5  | hours per week per bed | Case scenario, crop table |
| `TOM_FERT`   | 880  | USD per bed  | Case scenario, crop table |
| `TOM_DIM_RET`   | 10%  | Labor-increase rate per additional tomato bed  | Case scenario, crop table |
| `CAR_MAX_BEDS`   | 20  | tomato beds  | Case scenario, crop table |
| `CAR_PRICE` | $2094 | USD per bed | Case scenario, crop table |
| `CAR_HRS_PER_BED`   | 0.833  | hours per week per bed | Case scenario, crop table |
| `CAR_FERT`   | 440  | USD per bed  | Case scenario, crop table |
| `CAR_DIM_RET`   | 2.5%  | Labor-increase rate per additional tomato bed  | Case scenario, crop table |
| `MES_MAX_BEDS`   | 30  | tomato beds  | Case scenario, crop table |
| `MES_PRICE` | $2700 | USD per bed | Case scenario, crop table |
| `MES_HRS_PER_BED`   | 1.25  | hours per week per bed | Case scenario, crop table |
| `MES_FERT`   | $880  | USD per bed  | Case scenario, crop table |
| `MES_DIM_RET`   | 1.25%  | Labor-increase rate per additional tomato bed  | Case scenario, crop table |
| `WEEKS`   | 36  | weeks per season | Case scenario, slide 4 |
| `TOT_BED_CAP`   | 64  | beds | Case scenario, slide 4 |
| `FIX_SEAS_COST`   | $20,000  | US dollars | Case scenario, slide 4 |
| `FARM_SEAS_SAL`   | $50, 000  | US dollars | Case scenario, slide 4 |
| `FARM_AVAIL_HRS`   | 720  | hours | Case scenario, slide 4 |
| `FARM_SHARE_FIELD_TIME`   | 50%  | share of time in the field | Case scenario, slide 4 |
| `TEMP_WORK_SEAS_SAL`   | $25,000  | US dollars per worker | Case scenario, slide 4 |
| `TEMP_WORK CAP`   | 1,400  | hours per worker | Case scenario, slide 4 |
| `MAX_TEMP_WORK`   | 4  | persons | Case scenario, slide 4 |

Every input gets a name, a value, a unit, and a source. You choose the names.
The requirement is that they exist and are used consistently below.

## Structure
| Region | What it is for|
|---|---|
| Inputs | Store the named case assumptions: prices, costs, hours, percentages, and limits |
|Cost Structure|Calculates revenue and breaks down fertilizer, labor and other costs|
|Marginal-Cost Schedules|Shows how cost changes as beds of each crop are added|
|Optimization|Finds the most profitable crop mix that satisfies the limits| 
|Checks|Tests whether formulas, results, and constraints are correct|

## Calculation logic
In named-range notation, never cell addresses:

TOM_LABOR_HRS(q) = q × TOM_HRS_PER_BED × WEEKS × (1 + TOM_DIM_RET)^q
q is the number of tomato beds

TOM_REVENUE(q) = q × TOM_PRICE
TOM_FERT_COST(q) = q × TOM_FERT

Define these:
The corresponding carrot and mesclun calculations.
Total revenue as the sum of the three crops’ revenues.
Total cost from the specified cost components.
Profit as total revenue minus total cost.
Marginal cost as the additional cost of increasing a crop from q − 1 to q beds.

The exact labor-cost calculation is still unresolved. I need the course’s detailed costing instructions before deciding how salaries, unused worker hours, and the blended rate enter total cost.

The supplied labor formula means that the diminishing-return multiplier applies to all beds of that crop at quantity q. Marginal cost means the change in total cost when production increases from q − 1 to q. Specify the revenue, labor, fertilizer, total-cost, and profit calculations without cell addresses.

## Conventions
The rules that are not visible in the formulas: costing order, allocation basis,
rounding, what happens at the boundaries.

64 beds is a maximum, not a requirement to plant all 64.
Bed counts must be nonnegative whole numbers.
The farmer’s 720 field hours are used before temporary-worker hours.
The case requires labor allocation at a blended rate.
Explain rounding and how zero production is handled.

| Decision | Example of an explicit rule|
|---|---|
| Rounding | Keep full precision in calculations; display dollars and labor hours to two decimal places|
| Whole beds | Restrict planting quantities to nonnegative whole numbers|
| Zero Production | At zero beds of a crop, its revenue, fertilizer cost, and required field hours are zero; fixed seasonal costs still apply|

## Validation rules
The conditions the finished artifact must satisfy — check figures as acceptance
criteria, hand calculations, and structural rules ("every calculated cell
contains a formula", "no error cells").

TOM_LABOR_HRS(1) = 1 × 2.5 × 36 × 1.10 = 99 hours

Also require every calculated cell to contain a formula, no spreadsheet error cells, compliance with all capacity limits, all planting and labor limits are satisfied, results match the instructor's published check figures. 

## Outputs
Each result the model reports, by name.

Identify the results needed: crop quantities, workers required, labor usage, revenue, costs, profit, marginal costs, and unused capacity. Leave Audit findings empty until you actually build and check the workbook.

| Result | Possible name |
|---|---|
| Recommended tomato beds | OPT_TOM_BEDS |
| Recommended carrot beds | OPT_CAR_BEDS |
| Recommended mesclun beds | OPT_MES_BEDS |
| Total seasonal profit | TOTAL_PROFIT |
| Labor hours required | LABOR_HRS_USED |
| Unplanted beds | UNUSED_BEDS |
| Required worker | REQ_WORKER |
| Revenue | REVENUE |
| Cost | COST |
| Marginal-cost results | MARG_COST RESULTS |


## Audit findings
Pending — workbook has not been built or audited.

Added AFTER the build. For each check: what you checked, what you found, what
you did about it.
