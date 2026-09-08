---
type: brief
engagement: perfect-competition
capability: marginal-analysis
date: 2026-08-27
status: committed          # committed | superseded
hypothesis: "14 tomato beds, 20 carrot beds, and 30 mesclun beds"
---

# Perfect Competition — Engagement Brief

## The problem
In the case scenario we are given, we are discussing a tiny seller or farmer, in a huge market. What the farmer needs to determine is the specific amount of three different crops that should be planted that will maximize the farmer’s profit given fixed constraints and what can be chosen. A poor crop-mix decision could reduce the farmer's potential profit for a season that cannot be undone once planting occurs.

The market is the one that sets the price and the only decision the farmer gets to make is how much to produce and how many workers to hire.

What is fixed:
- Season: 36 weeks
- Fixed costs: $20,000 for the season
- Number of plots: 64 beds (4 plots each with 16 available beds)
- Max number of crop beds: Tomatoes 20, Carrots 20, Mesclun 30
- Price per bed for each crop ($8800, $2094, $2700)
- Labor hours per bed per week for each crop (2.5, 0.833, 1.25)
- Fertilizer cost per bed for each crop ($880, $440, $880)
- Diminishing returns rate per crop (10%, 2.5%, 1.25%)
- Farmer's labor: 720 field hours, part of her fixed $50,000 salary
- Temporary worker labor: $25,000 per worker for less than or equal to 1,440 hours, up to 4 workers, after using the farmer's 720 field hours

What is chosen:
- How many beds of tomatoes to plant
- How many beds of carrots to plant
- How many beds of mesclun to plant
- How many temporary workers to hire (0-4)

What limits the choice:
- Bed totals: 64 or fewer
- Maximum crop beds: Tomatoes 20, Carrots 20, Mesclun 30
- Labor: total hours required must be less than or equal to available hours
- Cannot plant a negative number of beds and must be whole numbers
- Farmer pays the full $25,000 for temporary work labor regardless of number of hours (up to 1,440), the number of workers is related to the bed-mix choice

## What I am assuming

I am assuming the information given such as prices, costs, labor requirements, crop limits, and other details that were provided in the case are accurate and will remain constant for the season.

I am also assuming that we cannot determine the best crop mix solely by comparing the initial per-bed cost or revenue of each crop. The diminishing returns are different for each crop, which means that the labor required for additional beds increases as more beds of that crop are planted. Therefore, a crop that initially appears to be the most profitable per bed may not remain the most profitable choice as additional beds are planted. Carrots and mesclun require less labor compared to tomatoes and have lower diminishing-return penalties, so they should do well.

Tomatoes earn much more revenue per bed, so I expect the farm to use a substantial number of tomato beds even though their labor requirements and diminishing returns rise faster. 

If I had more time and information, I would want to evaluate how the optimal crop mix would be affected by changes in market prices, labor costs, and the diminishing-returns rates.

## Hypothesis

I expect the optimal crop mix to be 14 tomato beds, 20 carrot beds, and 30 mesclun beds. I expect carrots and mesclun to reach their maximum number of beds because they have lower labor requirements and lower diminishing-returns rates than tomatoes. I expect tomatoes to make up the remaining 14 beds because their much higher revenue per bed will outweigh their higher labor requirements and faster diminishing returns up to that point.

## How I would know I was wrong

My hypothesis rests on three separable claims, each with its own falsification condition:

Claim 1 — carrots and mesclun run to their caps. If the model returns fewer than 20 carrot beds or fewer than 30 mesclun beds, this is falsified: something other than the stated cap is binding, and my labor-penalty reasoning for these two crops is wrong.

Claim 2 — tomatoes settle at roughly 14 beds because that is where the revenue advantage stops outweighing the compounding labor penalty. If the model returns tomato beds outside the range 9–18, this is falsified. Below 9, I badly overestimated how long tomatoes' revenue advantage holds against their diminishing returns; above 18, I badly underestimated it. I've set this band wider than a point estimate because the diminishing-returns term compounds exponentially, and the labor-costing convention (farmer's hours vs. temp-worker hours) — which I flagged as unresolved in my Stage 1.2 spec — could shift the true crossover meaningfully in either direction.

Claim 3 — all 64 beds get planted. If any bed is left empty in the optimal solution, this is falsified: it means leaving that bed idle beats planting anything in it, a qualitatively different result than a mix among the three crops.
