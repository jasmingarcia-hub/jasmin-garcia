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
Determine the profit-maximizing number of beds of tomatoes, carrots, and mesclun for the season, subject to the per-crop bed caps, the 64-bed total, the labor-hour constraint, and each crop's compounding labor requirement as beds increase. Diminishing returns affect labor requirements and the capacity limits are the constraints.

## Inputs — the named contract
| Name | Value | Unit | Source |
|---|---|---|---|
| `TOM_MAX_BEDS`   | 20  | tomato beds  | Case scenario, crop table |
| `TOM_PRICE` | $8800 | USD per bed | Case scenario, crop table |
| `TOM_HRS_PER_BED`   | 2.5  | hours per week per bed | Case scenario, crop table |
| `TOM_FERT`   | 880  | USD per bed  | Case scenario, crop table |
| `TOM_DIM_RET`   | 10%  | Labor-increase rate per additional tomato bed  | Case scenario, crop table |
| `CAR_MAX_BEDS`   | 20  | carrot beds  | Case scenario, crop table |
| `CAR_PRICE` | $2094 | USD per bed | Case scenario, crop table |
| `CAR_HRS_PER_BED`   | 2.5/3  | hours per week per bed | Case scenario, crop table |
| `CAR_FERT`   | 440  | USD per bed  | Case scenario, crop table |
| `CAR_DIM_RET`   | 2.5%  | Labor-increase rate per additional carrot bed  | Case scenario, crop table |
| `MES_MAX_BEDS`   | 30  | mesclun beds  | Case scenario, crop table |
| `MES_PRICE` | $2700 | USD per bed | Case scenario, crop table |
| `MES_HRS_PER_BED`   | 1.25  | hours per week per bed | Case scenario, crop table |
| `MES_FERT`   | $880  | USD per bed  | Case scenario, crop table |
| `MES_DIM_RET`   | 1.25%  | Labor-increase rate per additional mesclun bed  | Case scenario, crop table |
| `WEEKS`   | 36  | weeks per season | Case scenario, slide 4 |
| `TOT_BED_CAP`   | 64  | beds | Case scenario, slide 4 |
| `FIX_SEAS_COST`   | $20,000  | US dollars | Case scenario, slide 4 |
| `FARM_SEAS_SAL`   | $50,000  | US dollars | Case scenario, slide 4 |
| `FARM_AVAIL_HRS`   | 720  | hours | Case scenario, slide 4 |
| `FARM_SHARE_FIELD_TIME`   | 50%  | share of time in the field | Case scenario, slide 4 |
| `TEMP_WORK_SEAS_SAL`   | $25,000  | US dollars per worker | Case scenario, slide 4 |
| `TEMP_WORK_CAP`   | 1,440  | hours per worker | Case scenario, slide 4 |
| `MAX_TEMP_WORK`   | 4  | persons | Case scenario, slide 4 |


## Structure
| Region | What it is for|
|---|---|
| Inputs | Store the named case assumptions: prices, costs, hours, percentages, and limits |
|Cost Structure|Calculates revenue and breaks down fertilizer, labor and other costs|
|Marginal-Cost Schedules|Shows how cost changes as beds of each crop are added|
|Optimization|Finds the most profitable crop mix that satisfies the limits| 
|Checks|Tests whether formulas, results, and constraints are correct|

## Calculation logic
TOM_LABOR_HRS(q) = q × TOM_HRS_PER_BED × WEEKS × (1 + TOM_DIM_RET)^q
q is the number of tomato beds

TOM_REVENUE(q) = q × TOM_PRICE
TOM_FERT_COST(q) = q × TOM_FERT

CAR_LABOR_HRS(q) = q × CAR_HRS_PER_BED × WEEKS × (1 + CAR_DIM_RET)^q
q is the number of carrot beds

CAR_REVENUE(q) = q × CAR_PRICE
CAR_FERT_COST(q) = q × CAR_FERT

MES_LABOR_HRS(q) = q × MES_HRS_PER_BED × WEEKS × (1 + MES_DIM_RET)^q
q is the number of mesclun beds

MES_REVENUE(q) = q × MES_PRICE
MES_FERT_COST(q) = q × MES_FERT

FARM_RATE = FARM_SEAS_SAL × FARM_SHARE_FIELD_TIME / FARM_AVAIL_HRS
  (derived, not typed — equals $50,000 × 50% / 720 = $34.7222/hr)

TEMP_RATE = TEMP_WORK_SEAS_SAL / TEMP_WORK_CAP
  (derived, not typed — equals $25,000 / 1,440 = $17.3611/hr)

TOTAL_LABOR_HRS = TOM_LABOR_HRS(q_tom) + CAR_LABOR_HRS(q_car) + MES_LABOR_HRS(q_mes)

FARM_HRS_USED = MIN(TOTAL_LABOR_HRS, FARM_AVAIL_HRS)
TEMP_HRS_USED = MAX(TOTAL_LABOR_HRS − FARM_AVAIL_HRS, 0)

REQ_WORKER = ROUNDUP(TEMP_HRS_USED / TEMP_WORK_CAP, 0)
  (number of temporary workers needed to cover TEMP_HRS_USED;
   must not exceed MAX_TEMP_WORK)

TOTAL_LABOR_DOLLARS = (FARM_HRS_USED × FARM_RATE) + (TEMP_HRS_USED × TEMP_RATE)

BLENDED_RATE = TOTAL_LABOR_DOLLARS / TOTAL_LABOR_HRS

Each crop's labor cost = that crop's own labor hours × BLENDED_RATE.
The farmer's hours are consumed against total farm-wide labor demand first,
regardless of which crop generated them — the permanent/temporary split is a
farm-level fact, never allocated per crop.

TOTAL_REVENUE = TOM_REVENUE(q_tom) + CAR_REVENUE(q_car) + MES_REVENUE(q_mes)

TOTAL_FERT_COST = TOM_FERT_COST(q_tom) + CAR_FERT_COST(q_car) + MES_FERT_COST(q_mes)

TOTAL_COST = TOTAL_FERT_COST + TOTAL_LABOR_DOLLARS + FIX_SEAS_COST

PROFIT = TOTAL_REVENUE − TOTAL_COST

UNUSED_BEDS = TOT_BED_CAP − (q_tom + q_car + q_mes)

MARGINAL_COST_TOM(q) = [TOTAL_COST at q_tom = q] − [TOTAL_COST at q_tom = q − 1],
  holding q_car and q_mes fixed
(same definition applies for MARGINAL_COST_CAR(q) and MARGINAL_COST_MES(q),
 each holding the other two crops' bed counts fixed)

The supplied labor formula means that the diminishing-return multiplier applies to all beds of that crop at quantity q. Marginal cost means the change in total cost when production increases from q − 1 to q. 

## Conventions
The rules that are not visible in the formulas: costing order, allocation basis,
rounding, what happens at the boundaries.

64 beds is a maximum, not a requirement to plant all 64.
Bed counts must be nonnegative whole numbers.
The farmer’s 720 field hours are used before temporary-worker hours.
The case requires labor allocation at a blended rate.

| Decision | Example of an explicit rule|
|---|---|
| Rounding | Keep full precision in calculations; display dollars and labor hours to two decimal places|
| Whole beds | Restrict planting quantities to nonnegative whole numbers|
| Zero Production | At zero beds of a crop, its revenue, fertilizer cost, and required field hours are zero; fixed seasonal costs still apply|

## Validation rules

The conditions the finished artifact must satisfy — check figures as acceptance
criteria, hand calculations, and structural rules.

**Structural rules:**
- Every calculated cell contains a formula (no pasted values).
- No spreadsheet error cells.
- All bed counts are nonnegative whole numbers.
- All three bed caps (TOM_MAX_BEDS, CAR_MAX_BEDS, MES_MAX_BEDS) are respected.
- Total beds planted ≤ TOT_BED_CAP (64).
- REQ_WORKER ≤ MAX_TEMP_WORK (4). If a candidate bed mix produces
  REQ_WORKER > 4, that mix is infeasible and must be excluded from the
  optimization, regardless of its profit.

**Labor-hour anchors (hand-calculated, independent of the workbook):**

| Check | Formula | Expected value | Tolerance |
|---|---|---|---|
| Tomato, q=1 | 1 × 2.5 × 36 × 1.10^1 | 99.00 hours | exact |
| Tomato, q=10 | 10 × 2.5 × 36 × 1.10^10 | 2,334.37 hours | ± 0.5 hours |

**Marginal-cost check figures (published in case materials):**

| Check | Expected value | Tolerance |
|---|---|---|
| Tomato marginal cost at bed 10 | $8,249 | ± $5 |
| Tomato marginal cost at bed 11 | $9,391 | ± $5 |
| Marginal carrot bed value (at cap) | ≈ $352 | ± $5 |
| Marginal mesclun bed value (at cap) | ≈ $246 | ± $5 |

**Solver runs (required, both):**
- Run 1: start from 0 tomato / 0 carrot / 0 mesclun beds.
- Run 2: start from 20 tomato / 0 carrot / 0 mesclun beds.
- Both runs must converge to the same optimal bed counts; note any
  path-dependence if they do not.

**Acceptance criteria (published check figures):**

| Check | Value | Tolerance |
|---|---|---|
| Optimal mix | 10 tomato / 20 carrot / 30 mesclun beds (60 total) | exact |
| Season profit | $42,762 | ± $5 |
| Standalone P ≈ MC crossing — tomatoes | ≈ 10 beds | ± 1 bed |
| Standalone P ≈ MC crossing — carrots | ≈ 10 beds | ± 1 bed |
| Standalone P ≈ MC crossing — mesclun | ≈ 6 beds | ± 1 bed |

## Outputs
Each result the model reports, by name.

Identify the results needed: crop quantities, workers required, labor usage, revenue, costs, profit, marginal costs, and unused capacity. 

| Result | Possible name |
|---|---|
| Recommended tomato beds | OPT_TOM_BEDS |
| Recommended carrot beds | OPT_CAR_BEDS |
| Recommended mesclun beds | OPT_MES_BEDS |
| Total seasonal profit | PROFIT |
| Labor hours required | TOTAL_LABOR_HRS |
| Unplanted beds | UNUSED_BEDS |
| Required worker | REQ_WORKER |
| Revenue | TOTAL_REVENUE |
| Cost | TOTAL_COST |
| Marginal-cost results | MARGINAL_COST_TOM, MARGINAL_COST_CAR, MARGINAL_COST_MES |

## Audit findings
Pending — workbook has not been built or audited.

Added AFTER the build. For each check: what you checked, what you found, what
you did about it.
