# AI Prompt Log

This file documents my use of AI tools for coursework and portfolio development.

## Stage 0 — Portfolio Setup

### August 21, 2026

**Tool:** ChatGPT

**Purpose:** GitHub portfolio setup and learning how to use GitHub.

**Prompts / Tasks:**
- Asked ChatGPT to explain the Stage 0 GitHub assignment in plain language.
- Asked for step-by-step assistance creating the required repository structure using the GitHub web interface.
- Used ChatGPT to help draft AGENTS.md based on my background, learning preferences, and academic integrity requirements.
- Used ChatGPT to help create CLAUDE.md and connect it to AGENTS.md.

**How I Used the Output:**
I reviewed the suggested content before adding it to my repository. I used the guidance to learn how to create files, make commits, and organize my GitHub portfolio.

**Reflection:**
I am new to GitHub, so AI helped me understand the purpose of the repository and complete the technical setup without confusing the setup process with the substantive economics work I will complete myself.

## Stage 1 - Engagement Brief

### August 27, 2026

**Tool:** Claude

**Purpose:** Working through the "Perfect Competition" case (market-garden crop-mix problem) — understanding price-taking, marginal analysis, and building a falsifiable prediction before running the actual model.

**Prompts / Tasks:**
- Asked Claude to explain case slides in plain language (price-taking, P=MC, the "predict" framing).
- Asked Claude to help identify what's fixed, chosen, and constrained in the scenario once the full numeric table (crops, prices, labor, diminishing returns) was available.
- Asked Claude to help reason through a rough hand-calculation predicting an optimal bed mix (14 tomatoes / 20 carrots / 30 mesclun) before building the real model.
- Asked Claude what "falsifiable" means, then had it critique my own written engagement brief: named implicit assumptions, unsupported claims, likely client questions, and assessed whether my stated hypothesis is falsifiable.

**How I Used the Output:**
I used Claude's explanations to build my own understanding of price-taking and marginal analysis, and used its hand-calculation as a sanity check against my own reasoning — not as a substitute for building/running the actual spreadsheet/optimizer model, which I have not yet done. I used its critique of my engagement brief to identify assumptions and gaps in my own written reasoning before finalizing it.

**Reflection:**
The predicted 14/20/30 mix is my working hypothesis, not a verified answer — it depends on assumptions (e.g., how the diminishing-returns rate compounds, how to treat my own labor hours) that I need to state explicitly and confirm against the actual model output. The falsifiability check helped me see that my hypothesis is testable in principle, but the test itself isn't fully pinned down until those assumptions are made explicit.


## Stage 1.1 — Revision (Falsifiability + Economic Mechanism)

### September 7, 2026

**Tool:** Claude

**Purpose:** Revising the Stage 1.1 engagement brief in response to instructor feedback (87/100) — replacing an unfalsifiable falsification statement with separable, testable conditions, and checking the arithmetic behind my tomato-bed hypothesis.

**Prompts / Tasks:**

- Asked Claude to explain why my original falsifiability sentence was scored 10/20 and why it was considered tautological.
- Asked Claude to help draft three separable falsification conditions, one per implicit claim in my hypothesis (carrot/mesclun caps, tomato bed count, full 64-bed usage).
- Asked Claude to compute the marginal labor hours and cost for the 14th tomato bed, using the labor formula stated in the case materials, to check whether $8,800 covers that bed's cost as my brief claimed.
- Asked Claude to identify whether the case slide deck I'd been given contained the instructor's own worked answer for this scenario, since I was about to set a falsification band and wanted to avoid using outside information to reverse-engineer it.
- Asked Claude to confirm exactly where in my committed brief (on GitHub) each revision belonged.

**How I Used the Output:** I decided the width of my falsification band (9–18 tomato beds) myself, based on my own confidence in the mechanism, rather than accepting a number Claude suggested. When Claude flagged that a provided course slide deck contained the instructor's own solved answer for this case, I set my band using only my original pre-existing reasoning rather than incorporating that number, so the test would remain a genuine prior rather than a reverse-engineered one. I used Claude's labor-hour arithmetic as a check on my hypothesis, but did not change my committed 14/20/30 mix — I added the arithmetic as an acknowledged tension in my Hypothesis section instead, since I am not permitted to revise the hypothesis itself before the model runs.

**Reflection:** My original falsifiability sentence didn't hold up once you saw it named as tautological because I learned that tautological basically means, "true no matter what." Essentially any guess that is not the actual profit-maximizing combination, will by definition, get beaten by something. So, I had not made a real prediction, just a statement that's automatically true. I decided on 9–18 as my band width, which is considered a wide band. What this means is that I know that there is a real chance that I am off, so I gave myself room to still be right even if my exact number is wrong. I chose this wide band because I knew that the diminishing-returns penalty grows exponentially rather than steadily and I had already flagged that I did not know exactly how many labor hours would be used (farmer's hours versus temp workers), which means that the real answer could be shifted without having done anything incorrectly in my reasoning. I was quite unsure about whether tomatoes should be higher or lower than 14. Looking back now, I feel like the 9-18 was chosen to avoid being wrong. Before seeing the arithmetic, selecting 14 tomato beds was more of an educated guess. After doing the arithmetic, I did not have a change in my falsification band since my selection does fall inside a range that I had anticipated. I agree with the labor-hour arithmetic showing bed 14 may already be unprofitable because it cost $24,998 (720 hrs x $34.72) for the farmer's 720 hours and $451.36 (26 hrs x $17.36) for the temp worker's remaining 26 hours if the farmer solely worked on the tomato beds alone. Thus, the total labor cost would be $24,998 + $451.36 which is equal to $25,449. This estimate assumes the farmer's hours went entirely to tomatoes, which isn't realistic once carrots and mesclun are also competing for that labor — so the true marginal cost of bed 14 is probably different, but I don't yet know in which direction.


## Stage 1.2 — Workbook Build, Solver Debugging, and Audit

### September 11, 2026

**Tool:** Claude and ChatGPT

**Purpose:** Generating the model.xlsx workbook from my committed spec.md,
running the required Solver checks (two starting points), and auditing the
result against the published check figures.

**Prompts / Tasks:**

- Asked Claude to build the workbook exactly as specified in spec.md — every
  input a named range, every calculated cell a formula, validation rules
  computed in the workbook, check figures as acceptance criteria.
- Asked Claude to clarify two ambiguities it found in my spec before
  building: (1) whether "marginal cost" should be computed at my actual
  decision-mix bed counts or standalone with the other two crops at zero,
  and (2) whether the three marginal-cost formulas should be one combined
  output or three separate named outputs.
- Worked through several rounds of Solver setup errors with Claude's help:
  an objective-cell reference pointing at a label instead of a value, an
  "error value in objective or constraint cell" caused by feeding Solver
  boolean TRUE/FALSE check cells directly as constraints, and constraint
  right-hand-side references silently snapping to the wrong cell when set
  via cross-sheet clicking.
- Ran Solver from 0/0/0 and from 20/0/0, per the audit requirement, and
  asked Claude to help interpret the results — including trying Automatic
  Scaling and central-difference derivatives when the second run failed to
  converge.
- Asked Claude to draft the audit findings section for spec.md based on the
  actual Solver output.

**How I Used the Output:** I answered both spec ambiguities myself (marginal
cost at my actual decision mix; three separate named outputs) before Claude
rebuilt the workbook — those were my calls, not Claude's. I ran every
Solver attempt myself in Excel and reported back exactly what happened at
each step; Claude did not run Solver for me. I decided to record Run 2's
non-convergence as a genuine audit finding rather than treating it as a bug
to hide — the case materials specifically warn that GRG Nonlinear can get
stuck depending on its starting point, and my two runs disagreeing is
direct evidence of that risk in this model, not a mistake in my build.

**Reflection:** One of the most useful things I learned from this exercise was that a Solver run that does not produce the expected result is not necessarily a failure of the model. I also mistakenly thought ever time the Solver was run and it gave a pop-up window that it automatically meant that there was an error. In Run 2, the starting point resulted in a REQ_WORKER value of 8, which exceeded the model's maximum of 4 temporary workers. This meant that the starting solution itself was infeasible under the constraints of the case. Initially, I might have interpreted the failed run as evidence that something was wrong with the workbook or Solver setup. Instead, it helped me understand the importance of distinguishing between a model that is incorrect and a starting point that violates the model's constraints.

This actually increased my confidence in the model rather than reducing it. The workbook correctly identified that the proposed starting point required more labor than the farm could obtain under the stated worker cap. In that sense, the constraint was doing exactly what it was supposed to do. I was surprised that a "wrong" Solver run could provide useful information rather than simply represent an error that needed to be fixed. It showed me that failed or infeasible solutions can be diagnostic: they can reveal which constraints are binding and help explain why certain production combinations are not realistic.

I also learned that an AI-generated audit summary should not substitute for verifying the workbook itself. Rather than simply accepting Claude's statement that the model was correctly constructed, I checked the workbook directly. I used Excel's Name Manager to confirm that the required named ranges actually existed and pointed to the appropriate input cells. I also selected calculated cells and reviewed the formula bar to confirm that they contained formulas referencing the model inputs rather than hard-coded answers. Finally, I checked key calculations against the specification and its acceptance figures. This gave me greater confidence that the workbook was not merely producing plausible-looking outputs, but was actually implementing the economic model as specified.

Overall, the exercise changed how I think about model reliability. Reliability does not mean that every attempted solution must succeed. A reliable model should also reject infeasible solutions for the right reasons, make those reasons understandable, and allow its underlying assumptions and calculations to be independently verified.
