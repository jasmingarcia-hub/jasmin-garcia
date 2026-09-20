# Perfect Competition — Analysis

## Model Result

The model recommends planting:

- 10 tomato beds
- 20 carrot beds
- 30 mesclun beds

This uses 60 of the 64 available beds and leaves four beds unplanted. The resulting seasonal profit is approximately **$42,761.66**.

The result matched the published check figure of approximately **$42,762**, which gave me more confidence that the model was working as intended.

## Comparison With My Original Hypothesis

My original hypothesis was 14 tomato beds, 20 carrot beds, and 30 mesclun beds.

I was correct in predicting that carrots and mesclun would reach their maximum allowable number of beds. Both crops have lower diminishing-return penalties than tomatoes, so their labor requirements increase more slowly as production expands.

I was wrong about the number of tomato beds. I predicted 14, but the model recommends only 10. I had correctly anticipated that tomatoes would eventually become too expensive to continue producing because their labor requirements increase much faster, but I underestimated how quickly that would happen.

I was also wrong about all 64 beds being used. The model leaves four beds empty. This was one of the most useful findings for me because it showed that using every available bed is not necessarily the most profitable decision.

If planting another bed costs more than the revenue it generates, leaving that bed unused can actually produce a better outcome.

## Marginal Analysis

The tomato marginal-cost schedule helped me understand the result more clearly.

At 10 tomato beds, the marginal cost is approximately **$8,248.59**, which is still below the tomato market price of **$8,800**.

At 11 tomato beds, the marginal cost increases to approximately **$9,390.72**, which is now above the market price.

This helped me see the **P = MC** rule more clearly. The farmer should keep adding tomato beds while the additional revenue from another bed is greater than the additional cost of producing it. Once the next bed costs more than it brings in, production should stop.

The standalone schedules also show approximate price and marginal-cost crossing points at around 10 carrot beds and six mesclun beds. However, the full optimization model ultimately places carrots and mesclun at their maximum allowable quantities.

This showed me that looking at each crop by itself is not enough. The crops are competing for the same farm labor resources, so the final decision depends on the overall crop mix rather than only on the marginal cost of each crop in isolation.

## An Unexpected Marginal-Cost Pattern

One thing I did not initially expect was that the marginal-cost schedules do not always increase smoothly.

For example, tomato marginal cost rises through the fifth bed but then falls at the sixth bed. Similar decreases occur later in the carrot and mesclun schedules.

The reason is related to how labor is valued in the model. The farmer's field labor has an implied rate of approximately **$34.72 per hour**, while temporary labor has an implied rate of approximately **$17.36 per hour**.

Once the farmer's 720 available field hours are used, additional labor is valued at the lower temporary-labor rate.

This means that marginal cost can temporarily fall even though the actual number of labor hours required is still increasing.

This helped me understand that a marginal-cost curve is influenced not only by the physical production process, but also by the way resources are priced and allocated in the model.

## Modeling Convention and Limitation

The model follows the labor-costing convention used in the specification and published check figures by converting temporary-worker compensation to an hourly rate of approximately **$17.36**.

This differs from my initial Stage 1 interpretation that each temporary worker would generate the full **$25,000** cost once hired.

Because the optimization results match the published check figures, I retained the hourly-rate convention in the final model.

This distinction is important because changing the treatment of temporary labor could change the marginal costs and potentially the optimal crop mix.

## Constraints and Capacity

The optimal mix uses 60 of the 64 available beds, so the overall 64-bed limit is not binding.

The carrot and mesclun limits are binding because both crops reach their individual maximums of 20 and 30 beds.

The model requires four temporary workers. Total labor demand is approximately **5,277 hours**, of which 720 hours are provided by the farmer and approximately 4,557 hours are provided by temporary labor.

The Solver run that started at 20 tomato beds was also helpful in understanding the constraints.

At that starting point, the model required eight temporary workers, which was above the maximum of four. This meant that the starting solution itself was not feasible.

At first, I thought a Solver run that failed to produce a solution meant that something was wrong with the workbook. Instead, this helped me understand that an unsuccessful Solver run can still provide useful information. In this case, it showed that the starting combination violated one of the model's limits.

## What I Learned

My biggest takeaway is that maximizing profit is not the same as maximizing production or using every available resource.

Initially, it seemed intuitive that if a bed was available, it should be planted with something. The model showed why that reasoning can be wrong.

Once the marginal cost of additional production becomes greater than the additional revenue, producing more actually reduces profit.

The exercise also helped me understand why marginal analysis is more useful than simply comparing average revenue or cost per crop.

Tomatoes generate much more revenue per bed than carrots or mesclun, but their labor requirements increase much faster. Eventually, that extra labor cost outweighs the revenue advantage.

The final recommendation therefore depends not just on which crop brings in the most revenue, but on what happens to the cost of producing the next unit.

## AI Use Disclosure

I used ChatGPT and Claude to help me understand some of the economic concepts, work through problems with the Excel model, organize my thoughts, and improve the clarity of my writing. I reviewed the model myself, checked the calculations in Excel, and made the final decisions about the analysis and conclusions.

More detail about how I used AI is included in `prompt-log.md`.
