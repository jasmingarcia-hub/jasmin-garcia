# Research Sources

## Current register status — October 8, 2026

The unused source-note template has been removed. The completed [data source register](../capabilities/economic-research/spec.md#data-source-register--finalized-october-8-2026) records sources used in the final paper, indicator codes, observation years, sample counts, documented check dates, and limitations. Unknown access dates are explicitly labeled; no personal source review is inferred from AI-assisted checks. The dated notes below preserve the research history.

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

## Romania case check — October 5, 2026

AI research support for student verification; these notes are not student-written policy conclusions. Sources were checked separately from the global dataset.

| Source and location | Observation year | Verified evidence | Interpretation limit |
|---|---:|---|---|
| WHO, [Romania oral health country profile](https://cdn.who.int/media/docs/default-source/country-profiles/oral-health/oral-health-rou-2022-country-profile.pdf), pp. 1–2 (2022) | 2021 | Preventive and essential-curative benefits included; largest scheme covers 90%; all three public-primary-care services marked unavailable. The definition uses a 50%-of-patients-in-need threshold. | Below threshold does not mean no care anywhere. Scheme eligibility does not measure effective dental coverage. The profile's workforce entry is from 2017, unlike the aligned API record. |
| OECD / European Observatory, [Romania: Country Health Profile 2023](https://eurohealthobservatory.who.int/docs/librariesprovider3/country-health-profiles/chp2023pdf/chp-romania.pdf?download=true&sfvrsn=773136b7_5), p. 15, Figure 15 | 2021 | Public funds financed 5% of dental expenditure in Romania, versus 34% across the EU; the text identifies a heavier cost burden on lower-income people. | Spending share is neither population coverage nor treatment received. Private financing does not establish private provider ownership or an exact out-of-pocket share. |
| WHO Europe, [Romania financial-protection release](https://www.who.int/europe/news/item/29-08-2022-out-of-pocket-payments-for-health-care-in-romania-undermine-progress-towards-universal-health-coverage), August 29, 2022 | Report discusses 2010–2015 trends and later policy context | WHO identifies dental budget constraints and recommends strengthening dental coverage and purchasing for poorer households. | This is country-specific descriptive evidence and policy guidance, not an estimated reform effect. |
| Eurostat, [6% experience unmet dental care needs in the EU](https://ec.europa.eu/eurostat/en/web/products-eurostat-news/w/ddn-20250829-2), August 29, 2025; dataset `hlth_silc_09b` | 2024 | Romania: 16.2% unmet dental need; 43.5% among people at risk of poverty versus 12.6% among others. Denominator: people aged 16+ who needed dental care. | Self-reported cost, waiting-list, or distance barriers combined; not a cost-only measure. Later contextual evidence, not a 2021 outcome or global-sample variable. |

### Evidence boundaries and remaining checks

- These sources make Romania a useful case for distinguishing benefit entitlement from financial protection. They do not explain causally its WHO service classification or establish which policy would work best.
- The hypothesis that privately owned dentists contracted by insurance account for the public-facility result remains unverified. The full WHO financial-protection PDF could not be retrieved (access denied); no contract terms, payment caps, or provider-ownership claims were taken from search snippets.
- Central African Republic still lacks financing responses in the matched fields. This check does not supply those missing observations or resolve its service/workforce contrast.
- Keep the 2024 unmet-need evidence separate from the 2021 cross-country analysis. Do not infer a time trend by comparing percentages with different denominators.
- Student task: decide whether this case changes the financing preference, what delivery condition the recommendation requires, and which causal claim remains unsupported.

## Romania spending-share citation and payer check — October 5, 2026

- Bibliography citation: OECD/European Observatory on Health Systems and Policies. (2023). *Romania: Country Health Profile 2023.* OECD Publishing. https://doi.org/10.1787/f478769b-en .
- Verified against p. 15, Figure 15 and accompanying text: 5% publicly funded dental spending, observation year 2021; cited underlying dataset is OECD Health Statistics 2023. This is spending, not patient coverage.
- The remaining approximately 95% is privately financed in the report's framing. The report does not give the dental-specific split between household out-of-pocket payments, voluntary insurance, and other sources. Do not label all 95% out-of-pocket.
- A later [European Observatory Romania financing chapter](https://eurohealthobservatory.who.int/monitors/health-systems-monitor/countries-hspm/hspm/romania-2026/financing/sources-of-revenue-and-financial-flows), section 3.2, describes household payments as important for dental services, but its 96.6% figure concerns private spending on **all health care in 2022**, not dental spending in 2021. It cannot supply the missing dental payer split.
- Provider reimbursement and participation are discussed in the student revision as economic reasoning and policy-design considerations, not a demonstrated Romanian mechanism or universally necessary condition.

## Pre-PDF citation audit — October 5, 2026

- Added bibliography entries for WHO's Global Health Observatory dataset, dentist metadata, essential-curative metadata, and World Bank country/lending groups. Official pages checked; dynamic sources have an October 5 retrieval date.
- WHO benefit metadata confirms a 2021 survey and defines essential-curative treatment separately from advanced/restorative treatment. Do not treat benefit inclusion as the same variable as the three basic-service components.
- WHO dentist metadata confirms active-versus-registered and source-completeness differences. World Bank classifications use GNI-based categories; current API groups are not historical 2021 groups.
- APA same-year suffixes now follow title order in the current paper candidate: 2022a global report, 2022b Romania oral-health profile, 2022c WHO news release. Citations and entries were changed together; historical draft snapshots were preserved.
- Student source review remains pending for added bibliography items. The separate bibliography still needs final ordering and page formatting when the PDF is prepared.


## Final-review disclosure correction — October 10, 2026

The student confirmed personally checking all added bibliography sources in this session. Earlier pending-personal-review notes describe their dated historical status. The final disclosure no longer says that source verification and methodological checks are pending. Numerical and methodological checks are documented in the specification and analysis summary; measurement comparability, historical income alignment, and lack of causal policy evidence remain limitations. No new source, statistic, or policy finding is added.
