<!-- PR TARGET: https://github.com/jasmingarcia-hub/jasmin-garcia | Stage 1.1 -->
# Stage 1.1 review — engagement brief

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/jasmingarcia-hub/jasmin-garcia/blob/main/docs/briefs/perfect-competition-brief.md)

> Graded 2026-08-31, first pass on this brief. Your problem statement is the most complete in the cohort. One section is holding the score down and it is the same section that holds most of this cohort down.

| Criterion | Where it stands |
|---|---|
| Problem restated in your own voice | The best-structured problem statement anyone submitted for this stage. You separate what is fixed, what is chosen, and what limits the choice into three explicit lists, which is exactly the frame the stage asks for and which four people out of twenty-five actually built. Everything in the lists is correct — the caps, the prices, the labor hours, the diminishing-returns rates, the farmer's 720 field hours ahead of temporary labor, and the integer, non-negative bed counts. One item deserves separate credit: "Farmer pays the full $25,000 for temporary work labor regardless of number of hours (up to 1,440)." That is not in the case as a stated rule. It is a modeling decision, it materially changes the answer, and you surfaced it as a decision rather than absorbing it silently. That is what a good specification writer does, and you did it in the brief. |
| Hypothesis names a specific mix | 14 tomato, 20 carrot, 30 mesclun, in the frontmatter and again in the body. Specific, committed, and inside every constraint you listed. |
| Economic mechanism | Correct and clearly reasoned. The core claim is right and well put: "a crop that initially appears to be the most profitable per bed may not remain the most profitable choice as additional beds are planted." You then say why — different diminishing-returns rates, so the ranking is not fixed — and you name what you would test with more time, which is the sensitivity of the answer to prices, labor costs, and the rates themselves. What is still open: the same reason as most of this cohort: the argument is comparative where the case hands you quantities. You say tomatoes' higher revenue "will outweigh their higher labor requirements and faster diminishing returns up to that point," and the point you name is bed 14. The case lets you check that. One tomato bed takes 2.5 x 36 = 90 labor hours; the fourteenth takes 1.1 to the fourteenth power more per bed. Whether $8,800 still covers that is one line of arithmetic, and it is the line that would turn this from a good prediction into a defended one. |
| Falsifiability and process | This is the whole gap. "My hypothesis would be falsified if the analysis shows that a different combination of tomato, carrot, and mesclun beds produces a higher profit than my predicted mix." That is true of every hypothesis ever written about this case, including a correct one — the model's job is to find the profit-maximizing mix, so by construction any mix that is not the optimum will be beaten. The sentence cannot fail to be satisfied, so it tests nothing. It is also the single most common failure in this stage: nine of the eighteen graded briefs have a version of it. |

### What a falsification condition has to do, and how to write yours

The test is not "could this turn out to be false." It is "does this name a specific observation that would tell me which part of my reasoning was wrong." Your brief contains three distinct claims, and each one has an observation attached to it that you have not written down.

- You claim carrots and mesclun both run to their caps because their labor penalties are small. If the model returns fewer than 20 carrot beds or fewer than 30 mesclun, that claim is dead — something stopped them before the cap and it was not the cap.

- You claim tomatoes stop at 14 because that is where the revenue advantage runs out. If the model returns 18 tomato beds you underestimated how long the advantage lasts; if it returns 8 you badly overestimated it. Pick the band now: is 12 close enough? Is 10?

- You claim all 64 beds get used. If beds come back empty, then leaving a bed unplanted beats planting it, which is a different and more interesting result than any mix.

Each of those is a sentence. Together they are ten minutes of work and eight or nine points, and they have to be written before you build, because a condition written after you have seen the answer is not a prediction.

### One thing worth saying

The $25,000-regardless-of-hours question you raised is a real fork, and it is worth knowing that you found it before I answered it — you have also flagged the same thing in your Stage 1.2 specification, where you wrote that the labor-cost calculation is unresolved and you need the costing convention before deciding. That is the correct way to be stuck: you identified the ambiguity, wrote down that it is unresolved, and did not guess.

The answer is in your Stage 1.2 comment, because that is where it changes the arithmetic. What it does not change is this brief, which is graded on the reasoning you committed to before you knew.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error.*

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
