<!-- PR TARGET: https://github.com/jasmingarcia-hub/jasmin-garcia | Stage 1.2 (8 pts) -->
# Stage 1.2 review — spec, build, audit

**Spec-side 34 out of 62.5 — held, not entered. The stage is not due until 6 September and this is a first draft, which is the right thing to have right now.**

**Spec:** [`capabilities/marginal-analysis/spec.md`](https://github.com/jasmingarcia-hub/jasmin-garcia/blob/main/capabilities/marginal-analysis/spec.md)

> Graded 2026-08-31, first pass. There is a real specification started here with the right bones in it. You also flagged one thing as unresolved rather than guessing at it, which was the correct call — the answer is in the second section below.

| Criterion | Earned | Notes |
|---|---|---|
| Spec completeness — inputs, structure, calculation flow | 22 / 37.5 | The input contract is nearly complete — 24 named inputs with values, units, and sources, which is more than most first drafts carry — and the structure table names each region and what it is for. The labor function is written in named-range notation with the exponent on q, correctly, and the conventions section states the three rules that matter: 64 beds is a maximum rather than a requirement, bed counts are non-negative whole numbers, and the farmer's 720 field hours are used before temporary-worker hours. The deductions are for what is still template text and three errors — details below. |
| Spec validation rules | 12 / 25 | The q = 1 tomato anchor is there and correct at 99 hours, and you require every calculated cell to contain a formula, no error cells, and compliance with all capacity limits. What is missing is the acceptance criteria as testable rows: the published check figures are referred to rather than written down, none of them carries a tolerance, there is no second labor anchor, and the two Solver starting points are not specified. A validation rule a builder cannot mechanically check is a hope. |
| Workbook satisfies the contract | 0 / 25 | No workbook yet, and none was due at this point in the stage. |
| Audit note | 0 / 12.5 | Correctly marked "Pending — workbook has not been built or audited." That is the right state and the right way to say so. |
| **Spec-side subtotal** | **34 / 62.5** | the part that can be earned before a workbook exists |

### The answer to what you flagged

You wrote: "The exact labor-cost calculation is still unresolved. I need the course's detailed costing instructions before deciding how salaries, unused worker hours, and the blended rate enter total cost."

That is the right thing to have written and you are the only person who wrote it. The same ambiguity is in your Stage 1.1 brief, where you assumed the farm pays the full $25,000 per temporary worker regardless of hours. Here is the convention:

- Compute total labor hours across all three crops first. The farmer's 720 field hours are consumed before any temporary hours, regardless of which crop those hours belong to.

- Charge the farmer's field hours at her implied rate, derived as $50,000 over her 1,440 paid season hours — $34.7222 per hour, so her 720 field hours cost exactly $25,000, half her salary. The other half buys non-field time and does not vary with beds. It is not added to the $20,000 fixed costs.

- Charge temporary hours at $25,000 over 1,440 = $17.3611 per hour, for the hours actually used — not as a lump sum per worker hired. The per-worker figures exist to derive the rate and to size the four-worker cap, not to be charged directly.

- Then blend: total labor dollars divided by total labor hours gives one farm-wide rate, and every crop's labor cost is its own hours at that blended rate. The permanent-versus-temporary split is a farm-level fact and never gets pushed down into an individual crop.

Derive both rates rather than typing $34.72 and $17.36. Typing the rounded figures shifts season profit by about $13, which is small enough to look like a modeling subtlety and large enough to fail a tolerance — a workbook in this cohort has exactly that problem right now and it took a while to find. For the same reason, store carrot labor as 2.50 / 3 rather than 0.833.

### Three errors to fix

- TEMP_WORK CAP is listed as 1,400 hours per worker. It is 1,440. That is the denominator of the temporary wage rate, so the error propagates into every labor dollar in the model.

- CAR_MAX_BEDS and MES_MAX_BEDS both carry the unit "tomato beds", and CAR_DIM_RET and MES_DIM_RET are both described as a rate "per additional tomato bed". Copy-paste from the tomato rows. Harmless to a reader who knows the case; not harmless to a builder reading the spec as its own source of truth, which is the whole premise of writing one.

- The name TEMP_WORK CAP contains a space, which cannot be an Excel defined name.

### What is still template text

Several sections still hold their instruction text alongside your writing: "Every input gets a name, a value, a unit, and a source. You choose the names." under Inputs; "Define these:" and "Specify the revenue, labor, fertilizer, total-cost, and profit calculations without cell addresses" under Calculation logic; "Explain rounding and how zero production is handled" under Conventions; "Leave Audit findings empty until you actually build" under Outputs.

Those are instructions to you, and they read as unfinished work when a reviewer opens the file. Delete them as you fill each section in.

### One thing about the purpose section

It currently opens "A farmer decided to plant 14 beds of tomatoes, 20 beds of carrots and 30 beds of mesclun for the season." That is your Stage 1.1 hypothesis, and it belongs in the brief rather than here.

The distinction matters more than it sounds. The brief is where you commit to what you think the answer is; the spec is where you define a model that will find the answer on its own. A spec whose purpose statement contains the prediction is a spec that can be built to confirm it — and Stage 3 compares the two, which only means something if they were arrived at independently.

Rewrite it as the question: determine the profit-maximizing number of beds of each crop, subject to the bed caps, the 64-bed total, the labor constraint, and compounding labor requirements.

### A note on the point value, new as of today

This stage is now worth **15 points** rather than the 8 in the stage brief, and **Stage 1.3** — the analysis, the memo, and the prompt log — is now worth **15** as well. Cases 2 and 3 have been dropped for this cohort, so Case 1 *is* the case.

In practice: this stage and the next one are together worth **30 of the 35 points** on the case. Stage 0 and Stage 1.1 are 2.5 each. The weight has moved onto the build and the analysis, which is where the work actually is.

Nothing about the grading changes — the score is still out of 100 and converted at the end. The stage brief and the case page still show the old numbers; they have not been updated yet.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your spec into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then correct the spec, not the workbook.** This is the rule that makes the stage work: when a check fails, you fix the specification and regenerate, so the document keeps describing what was actually built.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*Nothing here is final. Stage 1.2 is not due until 6 September, and the stage is re-graded from scratch at the deadline.*

— Adam
