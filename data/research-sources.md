## Source 1 (Draft in progress)

Title:
Author:
Date:
Source:

Key finding:

How I may use it:


## Sources retrieved October 5, 2026 — research support

These are source records and AI research notes for student verification, not the student's submitted interpretation.

| Source | Role | What it supports | Limit |
|---|---|---|---|
| WHO, [Dentists per 10,000 metadata](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/dentists-(per-10-000-population)) | Workforce definitions | Source-dependent active versus registered counts; variability in sector coverage, timing, and completeness. | Standard definitions do not guarantee comparable national implementation. |
| WHO, [HWF_0010 API](https://ghoapi.azureedge.net/api/HWF_0010?$format=json) | Workforce timing check | Latest country-level observation on/before 2021. | May be older than 2021; historical records may be retrospectively revised. |
| World Bank, [2021 GDP per capita API](https://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.CD?format=json&per_page=400&date=2021) | Continuous income comparison | GDP per capita in current US dollars for 2021; 167 matched usable observations. | Not GNI-based historical income classification, purchasing-power adjustment, or causal control. |
| WHO, [Health financing](https://www.who.int/health-topics/health-financing/) | Policy mechanism | Funding, pooling, purchasing, provider incentives, and alignment with workforce capacity. | Guidance; does not show that financing caused the current dataset's availability categories. |
| European Observatory, [Oral health care in Europe: Financing, access and provision](https://eurohealthobservatory.who.int/publications/i/oral-health-care-in-europe-financing-access-and-provision), June 9, 2022 | Financing evidence to read next | Review of 31 European countries, public benefit gaps, private spending, and financially driven unmet dental need. | Regional descriptive review; not a global policy-effect estimate. The overview was checked; full country sections remain to be reviewed. |

### Next evidence questions for the financing preference

- Do countries with comparable workforce levels differ in benefit-package inclusion and reported availability?
- Does coverage include essential dental treatment, not merely enrollment in a health scheme?
- What evidence concerns treatment received or financially driven unmet need rather than our public-primary-care availability outcome?
- What workforce or provider-payment barriers limit the benefits of expanding coverage?

Historical income classifications source to inspect: [World Bank income and region classifications](https://datatopics.worldbank.org/world-development-indicators/the-world-by-income-and-region.html). Fiscal-year classifications require an explicit alignment convention before use.


## WHO financing indicators — October 5, 2026 retrieval

| Indicator | Observation year | Use | Limitation |
|---|---:|---|---|
| [ORALHEALTH_UHC_GOVSCHEME](https://ghoapi.azureedge.net/api/ORALHEALTH_UHC_GOVSCHEME?$format=json) | 2021 | Population eligible under largest public scheme, percentage | Enrollment/eligibility alone does not measure dental coverage or access. |
| [ORALHEALTH_UHC_PREVENTIVE](https://ghoapi.azureedge.net/api/ORALHEALTH_UHC_PREVENTIVE?$format=json) | 2021 | Routine/preventive care in benefit package, Yes/No | Inclusion does not establish delivery or affordability. |
| [ORALHEALTH_UHC_ESSENTIAL_CURATIVE](https://ghoapi.azureedge.net/api/ORALHEALTH_UHC_ESSENTIAL_CURATIVE?$format=json) | 2021 | Essential-curative care in benefit package, Yes/No | Covers essential treatment such as nonsurgical extraction and abscess drainage; do not equate it with all restorative/advanced care. |

[WHO indicator metadata](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/essential-curative-oral-health-care) describes the 2021 Health Technology Assessment and Health Benefit Package Survey. The largest scheme is the government scheme with the greatest eligible population. These are country-reported entitlements, not a policy evaluation.

Country-level overlap: 99 of the 171-country sample report essential-curative inclusion, and 92 report all three fields. Missingness and small subgroups limit interpretation. Romania has benefit inclusion but no reported primary-care service availability; Central African Republic lacks financing responses, preventing a two-country financing test.
