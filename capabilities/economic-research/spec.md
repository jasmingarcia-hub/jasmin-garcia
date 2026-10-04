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
