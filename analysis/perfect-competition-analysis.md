# Perfect Competition — Analysis

## What the Model Found

According to the model, the profit-maximizing crop mix is **10 tomato beds, 20 carrot beds, and 30 mesclun beds**, producing an estimated seasonal profit of **$42,761.66**. The result matches the published check figure of approximately $42,762. (Optimization!B4:B6; Optimization!B33)

This was my own optimizer’s output, which I compared to the assignment’s published check figure.

## Why Tomato Production Stops at 10 Beds

At 10 tomato beds, marginal cost is approximately **$8,248.59**, which is still below the market price of **$8,800 per bed**. Once we advance to 11 beds, marginal cost rises to approximately **$9,390.72**, which is above the market price. (Marginal-Cost Schedules!H16:H17; Marginal-Cost Schedules!B27)

Beyond 10 beds, the next tomato bed would no longer be profitable to the farmer.

Figure 1 shows where the marginal-cost curve crosses the market-price line. The farmer benefits from producing the 10th tomato bed because the additional revenue is greater than the additional cost. The 11th bed would cost more than it brings in at the market price of $8,800, so tomato production should stop at 10 beds.

The tomato marginal-cost schedule gives the clearest example of the **P ≈ MC** decision rule for this model.

![Figure 1. Tomato marginal cost versus market price.](figures/tomato-mc-vs-price.png)

*Figure 1. Tomato marginal cost versus the $8,800 market price. Source: Marginal-Cost Schedules!A6:H27.*

An interesting finding was that the tomato marginal-cost curve does not rise smoothly. Marginal cost falls between some bed quantities, particularly between beds 5 and 6, even though the physical labor requirement continues to increase.

The reason for this is that the farmer's field labor is valued at **$34.72 per hour**, while temporary labor is valued at **$17.36 per hour**. Once the farmer's 720 available field hours are exhausted, additional labor is valued at the lower temporary-worker rate. (Optimization!B18:B19)

Total labor demand at the recommended mix is approximately **5,277.22 hours**, and the model requires the maximum of **four temporary workers**. (Optimization!B14; Optimization!B17) This was different from what I originally predicted.

This helped me understand that marginal cost is influenced not only by the physical labor needed to produce another bed, but also by how that labor is valued in the model. The broader lesson is that marginal cost reflects input prices as well as physical production requirements.

The farm also uses only 60 of its 64 available beds, leaving **four beds unused**. This was important because it showed that maximizing profit does not necessarily mean using all available capacity. If another bed costs more to produce than the revenue it brings in, leaving it empty can be the better decision. (Optimization!B34)

## Why the Carrot and Mesclun Caps Matter

In the model, carrots reach their maximum of **20 beds**. At bed 20, standalone carrot marginal cost is approximately **$1,688.95**, while the market price is **$2,094**. (Inputs!B9; Optimization!B5; Marginal-Cost Schedules!H51; Marginal-Cost Schedules!B52)

Figure 2 shows that carrots are still economically attractive when the 20-bed cap is reached. The marginal cost of the 20th bed remains below the market price, which suggests that the farmer would want to plant more carrots if the crop-specific limit were relaxed.

![Figure 2. Carrot marginal cost versus market price.](figures/carrot-mc-vs-price.png)

*Figure 2. Carrot marginal cost versus the $2,094 market price. Source: Marginal-Cost Schedules!A31:H52.*

Mesclun shows the same general pattern as carrots. The model reaches the maximum of **30 mesclun beds**. At bed 30, standalone marginal cost is **$2,420.10**, which remains below the **$2,700 market price**. (Inputs!B14; Optimization!B6; Marginal-Cost Schedules!H86; Marginal-Cost Schedules!B87)

Figure 3 shows that mesclun is still economically attractive at the 30-bed cap. Because the marginal cost of the 30th mesclun bed remains below the market price, the model suggests that the farmer would still have an incentive to plant more mesclun if the crop-specific limit were relaxed.

![Figure 3. Mesclun marginal cost versus market price.](figures/mesclun-mc-vs-price.png)

*Figure 3. Mesclun marginal cost versus the $2,700 market price. Source: Marginal-Cost Schedules!A56:H87.*

This means the carrot and mesclun crop limits are binding, while the overall 64-bed limit is not. The farm already has four unused beds, so simply adding more general acreage would not improve the result. The more useful change would be relaxing one of the crop-specific limits.

## Carrot vs. Mesclun Shadow-Price Comparison

I tested this by relaxing each cap by one bed and comparing the change in profit.

Increasing the carrot cap from 20 to 21 raises profit from **$42,761.66 to approximately $43,114.16**, which is an increase of about **$352.49**.

Increasing the mesclun cap from 30 to 31 raises profit to approximately **$43,008.14**, which is an increase of about **$246.47**.

If only one crop-specific limit could be relaxed, I would prioritize **carrot capacity first** because the increase in profit is greater than it is for mesclun. One additional carrot bed is worth about $352 in seasonal profit compared with about $246 for one additional mesclun bed.

The model helped me see that the better question is not simply whether capacity, meaning the number of beds, is available. The more important question is whether producing the next unit adds more revenue than cost.

## Why Carrots and Mesclun Are Worth Planting Despite Their Apparent Losses

At first glance, carrots and mesclun might appear unprofitable when the farm's entire $20,000 fixed cost is allocated to each crop individually. However, the short-run shutdown rule explains why both crops should remain in the production plan. As long as the market price covers average variable cost (AVC), producing the crop contributes toward fixed costs that the farmer must pay regardless of whether the crop is planted.

At the recommended quantity of **20 carrot beds**, average variable cost is **$1,918.45 per bed**, which is below the market price of **$2,094**. Similarly, at **30 mesclun beds**, average variable cost is **$2,430.74 per bed**, compared with a market price of **$2,700**. Both crops therefore generate revenue beyond their variable production costs and make a contribution toward the farm's fixed expenses.

It is important to distinguish average variable cost from average total cost. A crop can appear unprofitable after being assigned the farm's entire fixed cost while still making a positive contribution to the farm's overall profit. Eliminating that crop would not eliminate the existing fixed costs, but it would eliminate the revenue available to help pay them.

This conclusion applies at the quantities in the recommended plan, not necessarily at every production level. For example, mesclun's average variable cost exceeds its market price at beds 13 and 14. At the recommended 30 beds, however, price exceeds AVC. This supports keeping both carrots and mesclun in the final crop mix.

## Modeling Convention and Limitation

The model follows the labor-costing convention used in the specification and published check figures by converting temporary-worker compensation to an hourly rate of approximately **$17.36**.

This differs from my original Stage 1 interpretation that hiring a temporary worker would create the full **$25,000** cost once that worker was needed. I retained the hourly-rate convention because it is the convention used in the final specification and produces results that match the published check figures.

This assumption matters because changing the way temporary labor is charged could change the marginal costs and potentially change the recommended crop mix.

## Comparison With My Stage 1 Hypothesis

My Stage 1 hypothesis was **14 tomato beds, 20 carrot beds, and 30 mesclun beds**, using all 64 available beds. The model found **10 tomato beds, 20 carrot beds, and 30 mesclun beds**, leaving four beds unused.

I was correct that carrots and mesclun would reach their caps, but I overestimated how long the higher revenue from tomatoes would outweigh their rapidly increasing labor cost. I was also wrong in assuming that all available beds should be planted.

The model showed me that having unused capacity does not mean the farm should automatically produce more. The better decision depends on whether the next unit adds more revenue than cost.

## AI Use Disclosure

I used ChatGPT and Claude to help me understand some of the economic concepts, work through problems with the Excel model, organize and draft parts of my analysis, and improve the clarity of my writing. I reviewed the model myself, checked the calculations in Excel, and made the final decisions about the analysis and conclusions.

More detail about how I used AI is included in `prompt-log.md`.
