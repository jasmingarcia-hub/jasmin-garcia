# Reproducible Research Analysis Summary

- Primary matched sample: 171 countries
- 2018–2023 dentist-data sensitivity sample: 159 countries
- Spearman ρ, dentist density vs access: 0.306
- Spearman ρ, dentist density vs access (fresh sample): 0.327
- Spearman ρ, dentist density vs income group: 0.739
- Spearman ρ, income group vs access: 0.322

## Dentist density by access category

| Access category | n | Mean | Median | Q1 | Q3 |
|---|---:|---:|---:|---:|---:|
| Not achieved | 23 | 2.41 | 0.76 | 0.12 | 4.10 |
| Partially achieved | 37 | 2.27 | 0.72 | 0.11 | 2.80 |
| Fully achieved | 111 | 4.42 | 2.97 | 0.96 | 7.70 |

## Dentist density by income group

| Income group | n | Mean | Median | Q1 | Q3 |
|---|---:|---:|---:|---:|---:|
| Low income | 21 | 0.81 | 0.06 | 0.02 | 0.11 |
| Lower middle income | 42 | 1.10 | 0.31 | 0.15 | 1.22 |
| Upper middle income | 53 | 3.59 | 2.33 | 1.13 | 5.24 |
| High income | 55 | 6.85 | 7.39 | 3.77 | 8.91 |

## Access composition by income group

| Income group | Not achieved | Partially achieved | Fully achieved |
|---|---:|---:|---:|
| Low income | 28.6% | 33.3% | 38.1% |
| Lower middle income | 16.7% | 40.5% | 42.9% |
| Upper middle income | 5.7% | 17.0% | 77.4% |
| High income | 12.7% | 7.3% | 80.0% |

## Exploratory year-alignment checks — October 5, 2026

Baseline values are retained. Additional workforce fields use the latest country observation on/before 2021. Outcomes remain the saved 2021 component categories. Income groups remain current classifications.

| Sample | n | Workforce–availability Spearman rho | None: median | Partial: median | Full: median |
|---|---:|---:|---:|---:|---:|
| Original workforce through 2023 | 171 | 0.306 | 0.76 | 0.72 | 2.97 |
| Workforce on/before 2021 | 171 | 0.305 | 0.76 | 0.57 | 2.93 |
| Workforce 2018–2021 | 157 | 0.325 | 0.76 | 0.57 | 3.57 |

- Original workforce values on the same 157 countries as the recent aligned subset: rho = 0.340.

### Within-income comparisons using aligned workforce

| Current income group | n | Workforce–availability Spearman rho |
|---|---:|---:|
| Low income | 21 | 0.374 |
| Lower middle income | 42 | 0.098 |
| Upper middle income | 53 | -0.170 |
| High income | 55 | 0.179 |

### Continuous 2021 GDP check

- 2021 GDP per capita vs aligned dentist density: n = 167, rho = 0.764.
- 2021 GDP per capita vs service availability: n = 167, rho = 0.330.

GDP is a continuous supporting measure, not a historical income classification or a causal adjustment. Historical income-group checks, reporting-definition checks, and financing analysis remain pending.

Sources retrieved October 5, 2026: https://ghoapi.azureedge.net/api/HWF_0010?$format=json and https://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.CD?format=json&per_page=400&date=2021 . Workforce observations may still be older than 2021; all checks are exploratory.
