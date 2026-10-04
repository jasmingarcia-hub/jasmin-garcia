# Economic Research Specification

## Research Question

How is dentist workforce density associated with access to oral health care across countries with different income levels?

## Data Sources

WHO Dentists (per 10,000 population) — country-level dentist workforce density. Coverage is broad, but observation years vary across countries and some values are missing.

World Bank GDP per capita and/or World Bank income classification — for country income comparison.

WHO Global Oral Health Action Plan Core Indicator 4.1 / GHO indicator `ORALHEALTH_SERVICESPHCFACILITIES` — country-level 2023 classification of whether oral-health care services are generally available in primary health care facilities. WHO classifies countries as Fully achieved, Partially achieved, Not achieved, or No information based on three services: oral-health screening, urgent oral care/pain relief, and basic restorative dental care.

The three underlying 2021 NCD Country Capacity Survey indicators (`ORALHEALTH_AVAILABILITY_SCREENING`, `ORALHEALTH_AVAILABILITY_URGENTCARE`, and `ORALHEALTH_AVAILABILITY_RESTORATIVE`) will be retained as supporting variables rather than used to construct the primary outcome ourselves.

Secondary/robustness measure: WHO coverage of the largest government health financing scheme (% of population), interpreted together with whether routine/preventive and essential curative oral-health services are included in that scheme. This will not be used alone as the primary access measure because financing-scheme coverage does not necessarily mean oral-health services are included or actually available.

## Variables

Dentist workforce density = dentists per 10,000 population

Country income level = World Bank income classification, with GDP per capita available for sensitivity analysis

Primary oral-health access measure = WHO 2023 `ORALHEALTH_SERVICESPHCFACILITIES` classification:
- Not achieved = none of the three services generally available
- Partially achieved = one or two services generally available
- Fully achieved = all three services generally available
- No information = country did not report usable data

Supporting access variables = the three 2021 WHO NCD CCS component indicators for screening, urgent care, and restorative care.

## Planned Analysis

- Compare dentist workforce density across World Bank income groups
- Examine whether countries with greater dentist workforce density tend to have greater primary-care oral-health service availability
- Compare dentist density across WHO's 2023 not achieved / partially achieved / fully achieved access categories
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
