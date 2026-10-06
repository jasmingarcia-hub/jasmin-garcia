---
type: spec
capability: economic-research
engagement: global-dental-workforce
date: 2026-10-03
status: built
built_with: "ChatGPT, Python, WHO GHO and World Bank APIs, GitHub Actions"
---

> Metadata and build audit added October 3, 2026. Status remains built: student verification and the remaining timing checks are pending. The earlier pre-build plan remains in Git history.

# Economic Research Specification

## Research Question

How is dentist workforce density associated with access to oral health care across countries with different income levels?

## Data Sources

WHO Dentists (per 10,000 population) — country-level dentist workforce density. Coverage is broad, but observation years vary across countries and some values are missing.

World Bank GDP per capita and/or World Bank income classification — for country income comparison.

WHO Global Oral Health Action Plan Core Indicator 4.1 / GHO indicator `ORALHEALTH_SERVICESPHCFACILITIES` — country-level 2023 classification of whether oral-health care services are generally available in primary health care facilities. WHO classifies countries as Fully achieved, Partially achieved, Not achieved, or No information based on three services: oral-health screening, urgent oral care/pain relief, and basic restorative dental care.

Actual extraction: the direct aggregate series did not return usable country categories. All 171 matched countries instead use a category derived from the three 2021 NCD Country Capacity Survey indicators (`ORALHEALTH_AVAILABILITY_SCREENING`, `ORALHEALTH_AVAILABILITY_URGENTCARE`, and `ORALHEALTH_AVAILABILITY_RESTORATIVE`). WHO's published none / one-or-two / all-three rule is applied only when all three responses are reported. This derived 2021 outcome is the primary measure in the saved dataset; it is not a direct observation from WHO's 2023 aggregate series.

Secondary/robustness measure: WHO coverage of the largest government health financing scheme (% of population), interpreted together with whether routine/preventive and essential curative oral-health services are included in that scheme. This will not be used alone as the primary access measure because financing-scheme coverage does not necessarily mean oral-health services are included or actually available.

## Additional Data sources - working draft

| # | Variable / role | Source and exact title | Publisher | Year(s) of data | Countries (n) | Access date | URL | Known limitations | Cited in paper? |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Dentist density (dentists per 10,000 people): explanatory variable | [exact indicator title] | WHO | Observations range [2018-2023]; latest per country | [n] | [date] | [URL] | Observation years differ across countries; some post-date the 2021 outcome; definitions of "dentist" may vary | |
| 2 | Service availability: outcome (proxy for access) | [exact indicator title] | WHO | 2021 | [n] | [date] | [URL] | Availability is not access; check whether the indicator is partly driven by having dentists at all; self-reported | |
| 3 | Income level: control / grouping variable | [World Bank classification or GDP per capita title] | World Bank | [current vs. 2021] | [n] | [date] | [URL] | Current classifications mismatch the 2021 outcome; some countries changed groups | |
| 4 | Background: disease burden and policy context | Global oral health status report: Towards universal health coverage for oral health by 2030 | WHO | 2022 | 194 | [date] | https://www.who.int/publications/i/item/9789240061484 | Motivates the problem; measures burden, not access or workforce supply | Yes |

## Variables

Dentist workforce density = dentists per 10,000 population

Country income level = World Bank current income classification returned by the country API during extraction (not a historical 2023 classification), with 2023 GDP per capita available as a supporting variable

Primary oral-health service-availability measure = derived category from three WHO 2021 component responses, using WHO's Core Indicator 4.1 classification rule:
- Not achieved = none of the three services generally available
- Partially achieved = one or two services generally available
- Fully achieved = all three services generally available
- No information = country did not report usable data

Underlying access variables = the three 2021 WHO NCD CCS component indicators for screening, urgent care, and restorative care. Retain the component responses and `access_source` / `access_data_year` fields for audit.

## Planned Analysis

- Compare dentist workforce density across World Bank income groups
- Examine whether countries with greater dentist workforce density tend to have greater primary-care oral-health service availability
- Compare dentist density across derived 2021 not achieved / partially achieved / fully achieved service-availability categories
- Identify countries that perform better or worse on access than their dentist density and income level might suggest
- Discuss whether those exceptions may relate to financing, workforce policy, geographic distribution, task sharing, or training capacity
- Use the government-financing-scheme indicators as a secondary check where country overlap is sufficient
- Repeat the primary comparison as a sensitivity analysis using only countries with dentist-density observations from 2018–2023

## Planned Figures

Primary figure:
- grouped dot/strip plot or box plot
- y-axis: dentists per 10,000 population
- x-axis: oral-health service availability category (not achieved / partially achieved / fully achieved)
- country income group distinguished by symbol, facet, or separate summary

Supporting figure:
- dentist density by World Bank income group

Optional robustness figure:
- financing-scheme population coverage versus dentist density, restricted to countries where essential oral-health services are included in the scheme

## Success Criteria

Project succeeds if it can:

- use comparable international data from credible sources
- assess whether a measurable relationship exists between workforce density, country income, and oral-health access
- test whether dentist density is associated with access rather than assuming causation
- identify at least one meaningful exception or counterexample
- develop a policy recommendation that is supported by the findings
- include at least one figure that materially supports the argument
- have sufficient overlapping country-level data across the workforce, access, and income variables to support a meaningful comparison

## Limitations

WHO dentist-density observations are not all from the same year, and some countries have missing values.

The primary access measure is WHO's country-reported service-availability classification. It measures health-system service availability rather than actual utilization, quality, affordability, or individual patient access.

The access outcome is ordinal (not achieved / partially achieved / fully achieved), not a precise continuous quantity.

Cross-country associations will not establish causation. Differences in financing, geography, health-system structure, workforce mix, reporting quality, and observation years may affect the results.


## Structure and outputs

- `data/build_research_dataset.py`: retrieve and match WHO/World Bank records by ISO3.
- `data/research_dataset.csv`: source fields and country-level matched observations, including incomplete rows.
- `data/research_dataset_summary.md`: matching and timing audit.
- `data/analyze_research_dataset.py`: descriptive calculations, rank correlations, and workforce-year sensitivity subset.
- `data/research_analysis_summary.md`: generated calculations.
- `figures/dentist-density-by-access.svg` and `figures/dentist-density-by-income.svg`: current median bar charts. The proposed distribution plot is a future improvement, not an implemented output.
- `drafts/YYYY-MM-DD-draft.md`: dated working snapshots, with student writing distinguished from inherited AI notes.
- `analysis/research-paper.pdf`: future student-authored finished paper; not yet produced.

## Audit findings

| Check | Finding | Correction / remaining action |
|---|---|---|
| Direct versus derived WHO outcome | All 171 matched rows say "Derived from WHO component indicators"; all have access year 2021. | Corrected this spec's description. Do not label the sample as direct 2023 availability data or equate it with WHO's 2023 aggregate benchmark. |
| Classification and missing responses | Category derivation requires three recognizable component responses; missing is not coded unavailable. | Preserve the rule and source fields; student should verify selected cases against original sources. |
| Sample overlap | 171 complete primary-analysis rows; 23 none, 37 partial, 111 full. | Counts checked against the saved CSV. GDP is not required for this categorical sample. |
| Timing | Workforce uses latest observation on/before 2023; outcome uses 2021. 159 workforce records fall in 2018–2023. | This is a workforce-recency check, not contemporaneous alignment with the 2021 outcome. A latest-on/before-2021 sensitivity check remains pending. |
| Income vintage | Country API returns current income classifications, separately from 2023 GDP. | Disclose the distinction. Historical income classifications or a consistent-year GDP sensitivity check remain pending. |
| Causal interpretation | Within-income descriptive comparisons and outliers do not identify effects of financing, deployment, or task sharing. | Treat these mechanisms as hypotheses for further investigation, not demonstrated explanations or a completed policy recommendation. |
| Drafts and authorship | AI prose was added to an October 2 file during October 3 work. | Preserve it with provenance labels; create an October 3 snapshot. Student writes the first substantive analysis/recommendation/reflection. |
| Current visuals | Existing SVGs show group medians, not box/strip plots. | Describe implemented figures accurately; distribution figures may be considered later. |


## October 5, 2026 — timing-check build audit

- Added `dentists_per_10000_on_or_before_2021`, `dentist_data_year_on_or_before_2021`, and `gdp_per_capita_2021_usd` to the existing dataset. Original baseline fields were retained unchanged.
- `python data/build_research_dataset.py --align-existing` appends these fields without rebuilding baseline values. Optional `--dentist-json` and `--gdp-json` accept cached official API responses. A full build also generates the timing fields.
- Analyst calculations use the latest valid country workforce observation on/before 2021; a second subset requires 2018–2021. Zero density is valid; missing density is excluded.
- All 171 original matched countries retain usable aligned workforce records. Rho is 0.305 versus baseline 0.306; the 157-country recent aligned subset gives 0.325. The baseline values on those same 157 countries give 0.340, separating observation replacement from exclusions.
- 167 aligned countries have positive 2021 GDP per capita. Continuous GDP rank comparisons are supporting checks, not substitutes for historical income classifications or estimates of a workforce effect adjusted for income.
- Correlations were independently verified with SciPy, including tied ranks. Baseline-field preservation and cutoff/subset counts were checked.
- WHO workforce metadata states source-dependent inclusion of active versus registered dentists and variability in sector coverage, timing, and completeness. Year restriction does not fix reporting comparability.
- Source retrieval date: October 5, 2026. WHO records can be retrospectively revised. This is an exploratory check on the retrieved data.
- Prior timing audit entries above describe the October 3 state. The on/before-2021 calculation is now complete. Historical income-group checks, financing analysis, and original-source review of outliers remain pending.


## October 5, 2026 — exploratory financing comparison

- Added three WHO 2021 Health Technology Assessment and Health Benefit Package Survey fields to the saved dataset: `government_scheme_coverage_pct_2021`, `preventive_in_public_scheme_2021`, `essential_curative_in_public_scheme_2021`.
- Indicator codes: `ORALHEALTH_UHC_GOVSCHEME`, `ORALHEALTH_UHC_PREVENTIVE`, and `ORALHEALTH_UHC_ESSENTIAL_CURATIVE`. Only country records with observation year 2021 are used; duplicate country records and unexpected response values fail validation.
- Reproduce enrichment with `python data/build_research_dataset.py --add-financing`. Optional `--financing-cache-dir` reads saved API JSON files. Existing baseline and year-alignment fields are preserved. Full builds also add financing fields.
- 99 of 171 primary-analysis countries report essential-curative inclusion: 78 Yes, 21 No. All three financing fields are available for 92 countries. The primary sample remains 171; missing financing responses are not recoded No or zero.
- Full primary-care service availability: 49/78 (62.8%) when essential-curative care is included; 9/21 (42.9%) when it is not.
- Descriptive workforce stratification uses exploratory bands below 1, 1–below 5, and 5+ dentists per 10,000, using aligned observations. These are broad bands, not matched comparisons or simultaneous income-and-workforce controls. Counts and proportions are reported in the generated summary.
- Current-income subgroup comparisons vary in direction and have small No groups. Missing reports, confounding, and reporting differences prevent a causal interpretation.
- Scheme coverage describes eligible population in the largest government scheme, not the proportion with effective dental coverage. Essential-curative inclusion concerns benefit entitlement, not observed affordability, use, or delivery.
- Romania reports 90% scheme coverage and inclusion of preventive and essential-curative dental care, despite no reported primary-care availability in the outcome. The Central African Republic has no usable financing fields in these three series, so it cannot provide a financing comparison here.
- API responses retrieved October 5, 2026. Counts, original-field preservation, source years, and missing responses verified independently.
- Source metadata: https://www.who.int/data/gho/data/indicators/indicator-details/GHO/essential-curative-oral-health-care .
- Financing comparisons are now implemented. Country policy-effect evidence, historical income classifications, and the student's policy interpretation remain pending. Earlier audit entries retain the earlier session state.


## October 5, 2026 — financing uncertainty methods

- The exploratory 2x2 table is [[49, 29], [9, 12]]: rows indicate essential-curative benefit inclusion (Yes, No); columns indicate full availability versus partial/no availability. Only the 99 countries reporting inclusion are used.
- Two-sided Fisher exact p = 0.134634; uncorrected Pearson chi-square (1 degree of freedom) p = 0.099240. These are different named tests; do not report an unspecified p-value of approximately 0.10.
- Individual proportions: 49/78 = 62.8%, with 95% Wilson interval 51.7–72.7%; 9/21 = 42.9%, with interval 24.5–63.5%. The observed difference is 20.0 percentage points; the reported intervals concern each proportion, not the difference.
- Wilson score intervals without continuity correction are also calculated for each current-income subgroup, with counts visible. Zero or all-success subgroups still have uncertainty.
- Binomial/independence assumptions are working statistical models for exploratory description. Nonrandom reporting, country measurement differences, regional dependence, workforce/income confounding, and income-vintage issues are not addressed by these intervals or tests.
- These checks do not identify causal effects, rank policies, establish a dentist-density threshold, or estimate supply elasticity. Subgroup intervals are descriptive with no multiple-comparison adjustment.
- Implemented in the existing analysis script using Python standard-library combinatorics, normal quantiles, and the df=1 chi-square survival formula. GitHub Actions requires no additional dependency.
- Validation: Fisher and chi-square implementations checked against SciPy on the observed table and three additional tables; Wilson headline intervals and zero/all-success boundaries checked; invalid denominators rejected.
- No new student policy interpretation was drafted. The student may revise the dated draft after reviewing these calculations.

## October 5, 2026 — country-case and outcome-definition clarification

- Original-source check: WHO's Romania profile, p. 2, defines general availability as reaching at least 50% of patients in need in public-sector primary-care facilities. Below that threshold is not general availability. Thus “Not achieved” means none of the three services meets the general-availability criterion; it does not mean a country has no dental care.
- This clarifies interpretation without changing saved component responses, categories, correlations, or medians. Paper/table labels should retain “generally available” and the public-primary-care scope.
- Romania's 2021 dental expenditure was only 5% publicly financed (OECD / European Observatory 2023 profile, p. 15). This helps distinguish recorded benefit inclusion from financial protection; it does not measure provider ownership or an intervention effect.
- Eurostat's 2024 unmet-need figures are later case context, with a denominator of people aged 16+ needing dental care and combined cost/wait/distance reasons. They were not merged into the 2021 global analysis.
- Source links, page locations, evidence boundaries, and the unverified provider-contract hypothesis are recorded in [research sources](../../data/research-sources.md#romania-case-check--october-5-2026).
- Country evidence now supports discussion of entitlement versus access. Historical income classification, provider-delivery details, policy-effect evidence, student source verification, and student recommendation remain pending.

## October 5, 2026 — pre-PDF completion audit

- The student has supplied the mixed-financing interpretation and recommendation/objection/response. These are now consolidated in the October 5 draft with editing assistance; earlier “student recommendation pending” notes describe prior session states.
- WHO dataset/metadata and World Bank classification references have been added to the paper candidate. Figure/table source captions avoid repository links. Bibliography year suffixes are consistent.
- Main text, including financing Table 1 and new citations, still fits four pages in the Times Roman layout test. Exact Times New Roman formatting and full-PDF anonymity remain to be checked.
- Student review of additional sources and a student-written closing reflection in root `prompt-log.md` remain outstanding. The reflection should explain AI's help, an oversimplification/invention, and an error personally caught and verified.
- The final PDF at `analysis/research-paper.pdf` has not yet been produced or submitted. The dated draft includes a completion checklist separating paper content from working notes. Historical income alignment and policy-effect gaps remain disclosed limitations.

## October 5, 2026 — student closing reflection supplied

The student supplied a three-part closing reflection, now saved with editing assistance at the end of root `prompt-log.md`. The edited text accurately distinguishes AI-assisted calculations and early prose from the student's later interpretation, and internal figure anchors from repository URLs. Earlier pending-reflection notes describe the previous session state. Student review of the edits and added sources, final required-font PDF formatting, and submission remain pending.
