# Research Dataset Summary

- Workforce/GDP target year: 2023; access timing is recorded separately in access_data_year
- World Bank countries/territories retained: 217
- Countries with complete primary analysis fields: 171
- Countries missing at least one primary field: 46

## Matched sample by oral-health access category

- Not achieved: 23
- Partially achieved: 37
- Fully achieved: 111

## Matched sample by World Bank income group

- High income: 55
- Low income: 21
- Lower middle income: 42
- Upper middle income: 53

## Dentist-density observation years in matched sample

- Earliest: 2004
- Latest: 2023
- 2018–2023 (within 5 years of target year): 159
- 2013–2023 (within 10 years of target year): 169
- Before 2013: 2

A sensitivity analysis should repeat the main comparison using only countries with dentist-density observations from 2018–2023.

## Matching rule

Primary analysis requires a WHO oral-health access category, a WHO dentist-density observation (latest available on or before 2023), and a World Bank income group. The script first uses the direct WHO 2023 category if exposed through the API; otherwise it applies WHO Core Indicator 4.1 classification rules to the three reported component services. A category is derived only when all three component responses are present. Missing responses are never coded as unavailable. GDP per capita is retained as a continuous supporting variable but is not required for inclusion in the primary categorical analysis.

## Timing and provenance audit

- Matched access sources: {'Derived from WHO component indicators': 171}
- Matched access observation years: {2021: 171}
- Income groups are current classifications returned by the World Bank country API during extraction, not historical 2023 classifications. GDP is for 2023.
- Workforce may postdate the component outcome. The 2018–2023 subset tests workforce recency, not alignment with a 2021 outcome. A latest-on/before-2021 sensitivity check remains pending.
- Do not equate a derived 2021 sample with WHO's direct 2023 aggregate benchmark.

## Important interpretation note

The WHO access category measures reported availability of oral-health services in primary health care facilities. It does not directly measure utilization, affordability, quality, or within-country geographic access.
