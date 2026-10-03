# Economic Research Specification

## Research Question

How is dentist workforce density associated with access to oral health care across countries with different income levels?

## Data Sources

WHO Dentists (per 10,000 population) — country-level dentist workforce density. Coverage is broad, but observation years vary across countries and some values are missing.

World Bank GDP per capita and/or World Bank income classification — for country income comparison.

WHO NCD Country Capacity Survey oral-health indicators — country-level availability of three oral-health services in primary care:
- oral health screening for early detection of oral diseases
- urgent treatment for emergency oral care and pain relief
- basic restorative dental procedures to treat existing dental decay

WHO defines a service as "generally available" when it reaches 50% or more of patients in need. These same three components are used in WHO Global Oral Health Action Plan Core Indicator 4.1 for availability of oral-health services in primary health care.

Secondary/robustness measure: WHO coverage of the largest government health financing scheme (% of population), interpreted together with whether routine/preventive and essential curative oral-health services are included in that scheme. This will not be used alone as the primary access measure because financing-scheme coverage does not necessarily mean oral-health services are included or actually available.

## Variables

Dentist workforce density = dentists per 10,000 population

Country income level = World Bank income classification, with GDP per capita available for sensitivity analysis

Primary oral-health access measure = service-availability score based on the three WHO NCD CCS indicators:
- 0 = none of the three services generally available
- 1 = one service generally available
- 2 = two services generally available
- 3 = all three services generally available

For interpretation, WHO's newer monitoring framework groups these as:
- Not achieved = 0 services
- Partially achieved = 1–2 services
- Fully achieved = all 3 services

## Planned Analysis

- Compare dentist workforce density across World Bank income groups
- Examine whether countries with greater dentist workforce density tend to have greater primary-care oral-health service availability
- Compare dentist density across the 0–3 access score and WHO-style not achieved / partially achieved / fully achieved categories
- Identify countries that perform better or worse on access than their dentist density and income level might suggest
- Discuss whether those exceptions may relate to financing, workforce policy, geographic distribution, task sharing, or training capacity
- Use the government-financing-scheme indicators as a secondary check where country overlap is sufficient

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

The primary access measure is based on country-reported service availability and uses a threshold definition (generally available = reaching at least 50% of patients in need). It therefore measures health-system service availability rather than actual utilization, quality, affordability, or individual patient access.

The 0–3 access score is an ordered summary created from the three WHO component indicators. It should be interpreted as an ordinal measure rather than a precise continuous quantity.

Cross-country associations will not establish causation. Differences in financing, geography, health-system structure, workforce mix, reporting quality, and observation years may affect the results.
