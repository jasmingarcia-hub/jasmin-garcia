# Perfect Competition — Analysis

## What the Model Found

According to the model, the profit-maximizing crop mix is **10 tomato beds, 20 carrot beds, and 30 mesclun beds**, producing an estimated seasonal profit of **$42,761.66**. The result matches the published check figure of approximately $42,762. (Optimization!B4:B6; Optimization!B33) This was my own optimizer’s output which was being compared to the assignment’s published check figure that was given to us. 

## Why Tomato Production Stops at 10 Beds

At 10 tomato beds, marginal cost is approximately **$8,248.59**, which is still below the market price of **$8,800 per bed**. One we advance to 11 beds, marginal cost rises to approximately **$9,390.72**, which is above the market price. (Marginal-Cost Schedules!H16:H17; Marginal-Cost Schedules!B27) Beyond 10 beds the yield would no longer be profitable to the farmer.

Figure 1 shows where the intersection is regarding when the number of beds is no longer profitable. The farmer benefits from producing the 10th tomato bed because the additional revenue is greater than the additional cost. The 11th bed would cost more than it brings in (Marcet price of $8,800), so tomato production should stop at 10 beds.
The tomato marginal-cost schedule gives the clearest example of the **P ≈ MC** decision rule for this model.

![Figure 1. Tomato marginal cost versus market price.](figures/tomato-mc-vs-price.png)

*Figure 1. Tomato marginal cost versus the $8,800 market price. Source: Marginal-Cost Schedules!A6:H27.*

An interesting find was that the tomato marginal-cost curve does not rise smoothly. Marginal cost falls between some bed quantities, particularly bed 5 and bed 6, even though the physical labor requirement continues to increase. 

The reason for this discrepancy is because the farmer's field labor is valued at **$34.72 per hour**, while temporary labor is valued at **$17.36 per hour**. Once the farmer's 720 available field hours are exhausted, additional labor is valued at the lower temporary-worker rate. (Optimization!B18:B19)

Total labor demand at the recommended mix is approximately **5,277.22 hours**, and the model requires the maximum of only **four temporary workers**. (Optimization!B14; Optimization!B17), which was different from my prediction.

This helped me understand that marginal cost is influenced not only by the physical labor needed to produce another bed, but also by how that labor is valued in the model. So, the general lesson or principle is that the marginal cost reflects the input prices as much as physical returns.

Also, the farm uses only 60 of its 64 available beds, leaving **four beds unused**. This was important because it showed that maximizing profit does not necessarily mean using all available capacity. If another bed costs more to produce than the revenue it brings in, leaving it empty can be the better decision. (Optimization!B34)

## Why the Carrot and Mesclun Caps Matter

In the model, carrots reach their maximum of **20 beds**. At bed 20, standalone carrot marginal cost is approximately **$1,688.95**, while the market price is **$2,094**. (Inputs!B9; Optimization!B5; Marginal-Cost Schedules!H51; Marginal-Cost Schedules!B52)

Figure 2 shows that carrots are still economically attractive when the 20-bed cap is reached. The marginal cost of the 20th bed remains below the market price, which suggests that the farmer would want to plant more carrots if the crop-specific limit were relaxed.


![Figure 2. Carrot marginal cost versus market price.](figures/carrot-mc-vs-price.png)

*Figure 2. Carrot marginal cost versus the $2,094 market price. Source: Marginal-Cost Schedules!A31:H52.*

Mesclun shows the same general pattern as the carrots. The model reaches the maximum of **30 mesclun beds**. At bed 30, standalone marginal cost is **$2,420.10**, which remains below the **$2,700 market price**. (Inputs!B14; Optimization!B6; Marginal-Cost Schedules!H86; Marginal-Cost Schedules!B87)

This means the carrot and mesclun crop limits are binding, while the overall 64-bed limit is not. The farm already has four unused beds, so simply adding more general acreage would not improve the result. The more useful change would be relaxing one of the crop-specific limits.


##Carrot vs. mesclun shadow-price comparison
The above was tested by relaxing each cap by one bed and comparing the profit gain. Increasing the carrot cap from 20 to 21 raises profit from **$42,761.66 to approximately $43,114.16**, which is an increase of about **$352.49**. Increasing the mesclun cap from 30 to 31 raises profit to approximately **$43,008.14**, an increase of about **$246.47**.

This means that if we had to choose one crop-specific limit could be relaxed, we should prioritize **carrot capacity first** since the increase is greater than mesclun. One additional carrot bed is worth about $352 in profit compared with about $246 for an additional mesclun bed.
I was correct that carrots and mesclun would reach their caps, but I overestimated how long the higher revenue from tomatoes would outweigh their rapidly increasing labor cost. I was also wrong in assuming that all available beds should be planted.

The model helped me see that the better question is not whether capacity (number of beds) is available, but whether producing the next unit adds more revenue than cost.


## Modeling Convention and Limitation

The model follows the labor-costing convention used in the specification and published check figures by converting temporary-worker compensation to an hourly rate of approximately **$17.36**.

This differs from my original Stage 1 interpretation that hiring a temporary worker would create the full **$25,000** cost once that worker was needed. I retained the hourly-rate convention because it is the convention used in the final specification and produces results that match the published check figures.

This assumption matters because changing the way temporary labor is charged could change the marginal costs and potentially change the recommended crop mix.

## Comparison With My Stage 1 Hypothesis

My Stage 1 hypothesis was **14 tomato beds, 20 carrot beds, and 30 mesclun beds**, using all 64 available beds. The model found **10 tomato, 20 carrot, and 30 mesclun beds**, leaving four beds unused.


## AI Use Disclosure

I used ChatGPT and Claude to help me understand some of the economic concepts, work through problems with the Excel model, organize and draft parts of my analysis, and improve the clarity of my writing. I reviewed the model myself, checked the calculations in Excel, and made the final decisions about the analysis and conclusions.

More detail about how I used AI is included in `prompt-log.md`.
