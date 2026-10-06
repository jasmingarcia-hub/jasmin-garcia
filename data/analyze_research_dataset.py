#!/usr/bin/env python3
"""Analyze the matched oral-health research dataset and regenerate figures."""

from __future__ import annotations

import csv
import math
from collections import Counter
from pathlib import Path
from statistics import mean, median, NormalDist

DATA = Path("data/research_dataset.csv")
OUT = Path("data/research_analysis_summary.md")
FIG_DIR = Path("figures")

ACCESS_ORDER = {"Not achieved": 0, "Partially achieved": 1, "Fully achieved": 2}
INCOME_ORDER = {
    "Low income": 0,
    "Lower middle income": 1,
    "Upper middle income": 2,
    "High income": 3,
}
ACCESS_CATS = list(ACCESS_ORDER)
INCOME_CATS = list(INCOME_ORDER)


def percentile(values: list[float], q: float) -> float:
    vals = sorted(values)
    pos = (len(vals) - 1) * q
    lo, hi = math.floor(pos), math.ceil(pos)
    if lo == hi:
        return vals[lo]
    return vals[lo] + (vals[hi] - vals[lo]) * (pos - lo)


def summarize(values: list[float]) -> dict:
    return {
        "n": len(values),
        "mean": mean(values),
        "median": median(values),
        "q1": percentile(values, 0.25),
        "q3": percentile(values, 0.75),
    }


def average_ranks(values: list[float]) -> list[float]:
    pairs = sorted(enumerate(values), key=lambda x: x[1])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(pairs):
        j = i
        while j + 1 < len(pairs) and pairs[j + 1][1] == pairs[i][1]:
            j += 1
        avg_rank = (i + j + 2) / 2
        for k in range(i, j + 1):
            ranks[pairs[k][0]] = avg_rank
        i = j + 1
    return ranks


def pearson(x: list[float], y: list[float]) -> float:
    mx, my = mean(x), mean(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    denx = sum((a - mx) ** 2 for a in x)
    deny = sum((b - my) ** 2 for b in y)
    return num / math.sqrt(denx * deny)


def spearman(x: list[float], y: list[float]) -> float:
    if len(x) < 2 or len(set(x)) < 2 or len(set(y)) < 2:
        return float("nan")
    return pearson(average_ranks(x), average_ranks(y))


def timing_checks(rows: list[dict]) -> list[str]:
    key = "dentists_per_10000_on_or_before_2021"
    year_key = "dentist_data_year_on_or_before_2021"
    aligned = [r for r in rows if r.get(key) not in (None, "")]
    recent = [r for r in aligned if 2018 <= int(r[year_key]) <= 2021]
    lines = ["", "## Exploratory year-alignment checks — October 5, 2026", "",
             "Baseline values are retained. Additional workforce fields use the latest country observation on/before 2021. Outcomes remain the saved 2021 component categories. Income groups remain current classifications.", "",
             "| Sample | n | Workforce–availability Spearman rho | None: median | Partial: median | Full: median |",
             "|---|---:|---:|---:|---:|---:|"]
    for label, sample, field in [("Original workforce through 2023", rows, "dentists_per_10000"),
                                  ("Workforce on/before 2021", aligned, key),
                                  ("Workforce 2018–2021", recent, key)]:
        rho = spearman([float(r[field]) for r in sample], [ACCESS_ORDER[r["oral_health_access_category"]] for r in sample])
        medians = [median([float(r[field]) for r in sample if r["oral_health_access_category"] == c]) if any(r["oral_health_access_category"] == c for r in sample) else float("nan") for c in ACCESS_CATS]
        lines.append(f"| {label} | {len(sample)} | {rho:.3f} | " + " | ".join(f"{v:.2f}" for v in medians) + " |")
    # Same-country baseline separates sample exclusion from observation replacement.
    if recent:
        baseline_same = spearman([float(r["dentists_per_10000"]) for r in recent], [ACCESS_ORDER[r["oral_health_access_category"]] for r in recent])
        lines.extend(["", f"- Original workforce values on the same {len(recent)} countries as the recent aligned subset: rho = {baseline_same:.3f}."])
    lines.extend(["", "### Within-income comparisons using aligned workforce", "",
                  "| Current income group | n | Workforce–availability Spearman rho |", "|---|---:|---:|"])
    for group in INCOME_CATS:
        sample = [r for r in aligned if r["income_group"] == group]
        rho = spearman([float(r[key]) for r in sample], [ACCESS_ORDER[r["oral_health_access_category"]] for r in sample])
        lines.append(f"| {group} | {len(sample)} | {rho:.3f} |")
    gdp = [r for r in aligned if r.get("gdp_per_capita_2021_usd") not in (None, "") and float(r["gdp_per_capita_2021_usd"]) > 0]
    lines.extend(["", "### Continuous 2021 GDP check", ""])
    for label, left, right in [
        ("2021 GDP per capita vs aligned dentist density", "gdp_per_capita_2021_usd", key),
        ("2021 GDP per capita vs service availability", "gdp_per_capita_2021_usd", None)]:
        rho = spearman([float(r[left]) for r in gdp], [float(r[right]) if right else ACCESS_ORDER[r["oral_health_access_category"]] for r in gdp])
        lines.append(f"- {label}: n = {len(gdp)}, rho = {rho:.3f}.")
    lines.extend(["", "GDP is a continuous supporting measure, not a historical income classification or a causal adjustment. Historical income-group checks, reporting-definition checks, and policy-effect evidence remain pending. Financing comparisons are reported below.", "",
                  "Sources retrieved October 5, 2026: https://ghoapi.azureedge.net/api/HWF_0010?$format=json and https://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.CD?format=json&per_page=400&date=2021 . Workforce observations may still be older than 2021; all checks are exploratory."])
    return lines


def read_rows() -> list[dict]:
    with DATA.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return [
        r for r in rows
        if r["dentists_per_10000"]
        and r["oral_health_access_category"] in ACCESS_ORDER
        and r["income_group"] in INCOME_ORDER
    ]


def financing_checks(rows: list[dict]) -> list[str]:
    benefit = "essential_curative_in_public_scheme_2021"
    coverage = "government_scheme_coverage_pct_2021"
    density = "dentists_per_10000_on_or_before_2021"
    available = [r for r in rows if r.get(benefit) in ("Yes", "No")]
    complete = [r for r in available if r.get(coverage) not in (None, "") and r.get("preventive_in_public_scheme_2021") in ("Yes", "No")]
    lines = ["", "## Exploratory public-benefit-package checks — October 5, 2026", "",
             f"- Primary sample: {len(rows)} countries; essential-curative inclusion reported for {len(available)}; all three financing fields reported for {len(complete)}.",
             "- All added financing observations are from 2021. Missing responses remain missing, never No or zero.",
             "- Scheme population coverage is not dental coverage. Benefit inclusion is an entitlement measure, not proof of use, affordability, or service delivery.", "",
             "| Essential-curative dental care in largest public scheme | n | Full service availability: n | Full availability: % | Median aligned dentist density |",
             "|---|---:|---:|---:|---:|"]
    for flag in ("No", "Yes"):
        sample = [r for r in available if r[benefit] == flag]
        full = sum(r["oral_health_access_category"] == "Fully achieved" for r in sample)
        vals = [float(r[density]) for r in sample if r.get(density) not in (None, "")]
        if sample:
            lines.append(f"| {flag} | {len(sample)} | {full} | {100*full/len(sample):.1f}% | {median(vals):.2f} |")
    lines.extend(["", "### Descriptive stratification by dentist supply", "",
                  "Broad density bands are exploratory, not matched countries or causal controls. Density uses the latest observation on/before 2021. Small subgroup counts must be considered.", "",
                  "| Dentists per 10,000 | Benefit included | n | Full availability: n | Full availability: % |", "|---|---|---:|---:|---:|"])
    for label, lower, upper in [("Below 1", 0, 1), ("1 to below 5", 1, 5), ("5 or more", 5, float("inf"))]:
        for flag in ("No", "Yes"):
            sample = [r for r in available if r.get(density) not in (None, "") and lower <= float(r[density]) < upper and r[benefit] == flag]
            full = sum(r["oral_health_access_category"] == "Fully achieved" for r in sample)
            if sample:
                lines.append(f"| {label} | {flag} | {len(sample)} | {full} | {100*full/len(sample):.1f}% |")
    lines.extend(["", "### Descriptive stratification by current income group", "",
                  "| Current income group | Benefit included | n | Full availability: n | Full availability: % |", "|---|---|---:|---:|---:|"])
    for group in INCOME_CATS:
        for flag in ("No", "Yes"):
            sample = [r for r in available if r["income_group"] == group and r[benefit] == flag]
            full = sum(r["oral_health_access_category"] == "Fully achieved" for r in sample)
            if sample:
                lines.append(f"| {group} | {flag} | {len(sample)} | {full} | {100*full/len(sample):.1f}% |")
    lines.extend(["", "### Selected country audit rows", "",
                  "| Country | Aligned dentist density | Service category | Scheme coverage % | Preventive benefit | Essential-curative benefit |", "|---|---:|---|---:|---|---|"])
    for iso in ("CAF", "ROU"):
        r = next((r for r in rows if r["iso3"] == iso), None)
        if r:
            lines.append(f"| {r['country']} | {r.get(density) or 'Missing'} | {r['oral_health_access_category']} | {r.get(coverage) or 'Missing'} | {r.get('preventive_in_public_scheme_2021') or 'Missing'} | {r.get(benefit) or 'Missing'} |")
    lines.extend(["", "These are descriptive cross-sectional comparisons with incomplete reporting, current income groups, and possible confounding. Do not interpret them as effects of expanding financing or as an explanation for particular countries. Country-profile and policy-effect evidence remain to be checked.", "",
                  "Sources: WHO 2021 Health Technology Assessment and Health Benefit Package Survey, indicators ORALHEALTH_UHC_GOVSCHEME, ORALHEALTH_UHC_PREVENTIVE, ORALHEALTH_UHC_ESSENTIAL_CURATIVE. API records retrieved October 5, 2026; metadata: https://www.who.int/data/gho/data/indicators/indicator-details/GHO/essential-curative-oral-health-care ."])
    return lines


def wilson_interval(successes: int, total: int, confidence: float = 0.95) -> tuple[float, float]:
    """Two-sided Wilson score interval without continuity correction."""
    if not 0 <= successes <= total or total <= 0 or not 0 < confidence < 1:
        raise ValueError("Invalid binomial counts or confidence level")
    z = NormalDist().inv_cdf((1 + confidence) / 2)
    p = successes / total
    denominator = 1 + z * z / total
    center = (p + z * z / (2 * total)) / denominator
    half = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / denominator
    return max(0.0, center - half), min(1.0, center + half)


def financing_test_pvalues(table: list[list[int]]) -> tuple[float, float]:
    """Two-sided Fisher exact and uncorrected Pearson chi-square (df=1)."""
    if len(table) != 2 or any(len(row) != 2 for row in table):
        raise ValueError("Expected a 2x2 table")
    a, b = table[0]
    c, d = table[1]
    if any(not isinstance(x, int) or x < 0 for x in (a, b, c, d)):
        raise ValueError("Expected nonnegative integer counts")
    total = a + b + c + d
    first_row, second_row = a + b, c + d
    first_col, second_col = a + c, b + d
    if not all((first_row, second_row, first_col, second_col)):
        return float("nan"), float("nan")
    denominator = math.comb(total, first_row)
    def probability(x: int) -> float:
        return math.comb(first_col, x) * math.comb(second_col, first_row - x) / denominator
    observed = probability(a)
    lower, upper = max(0, first_row - second_col), min(first_row, first_col)
    fisher = min(1.0, sum(probability(x) for x in range(lower, upper + 1) if probability(x) <= observed * (1 + 1e-12)))
    chi_square = total * (a * d - b * c) ** 2 / (first_row * second_row * first_col * second_col)
    chi_p = math.erfc(math.sqrt(chi_square / 2))
    return fisher, chi_p


def financing_uncertainty(rows: list[dict]) -> list[str]:
    field = "essential_curative_in_public_scheme_2021"
    groups = {flag: [r for r in rows if r.get(field) == flag] for flag in ("Yes", "No")}
    table = [[sum(r["oral_health_access_category"] == "Fully achieved" for r in groups[flag]),
              sum(r["oral_health_access_category"] != "Fully achieved" for r in groups[flag])] for flag in ("Yes", "No")]
    fisher, chi_p = financing_test_pvalues(table)
    lines = ["", "## Exploratory financing uncertainty checks — October 5, 2026", "",
             "The 2x2 table contrasts full availability with partial/no availability among countries reporting essential-curative benefit inclusion. Rows: Yes, No. Columns: full, partial/no. These are unadjusted exploratory comparisons, not policy-effect estimates.", "",
             f"- Observed table: {table}.",
             f"- Fisher exact test, two-sided: p = {fisher:.6f}.",
             f"- Pearson chi-square test, df = 1, without continuity correction: p = {chi_p:.6f}.", "",
             "| Benefit included | Full availability | Proportion | 95% Wilson score interval |", "|---|---:|---:|---:|"]
    for flag in ("Yes", "No"):
        n = len(groups[flag])
        k = sum(r["oral_health_access_category"] == "Fully achieved" for r in groups[flag])
        if n:
            low, high = wilson_interval(k, n)
            lines.append(f"| {flag} | {k}/{n} | {100*k/n:.1f}% | {100*low:.1f}–{100*high:.1f}% |")
    if all(groups.values()):
        difference = 100 * (table[0][0] / len(groups['Yes']) - table[1][0] / len(groups['No']))
        lines.extend(["", f"Observed difference: {difference:.1f} percentage points. The intervals above are for individual proportions, not the difference."])
    lines.extend(["", "### Current-income subgroup intervals", "",
                  "| Current income group | Benefit included | Full availability | Proportion | 95% Wilson score interval |", "|---|---|---:|---:|---:|"])
    for income in INCOME_CATS:
        for flag in ("Yes", "No"):
            sample = [r for r in groups[flag] if r["income_group"] == income]
            n = len(sample)
            k = sum(r["oral_health_access_category"] == "Fully achieved" for r in sample)
            if n:
                low, high = wilson_interval(k, n)
                lines.append(f"| {income} | {flag} | {k}/{n} | {100*k/n:.1f}% | {100*low:.1f}–{100*high:.1f}% |")
    lines.extend(["", "Intervals use a binomial working model and Wilson score method with 95% nominal coverage, no continuity correction. Neither intervals nor p-values account for nonrandom country reporting, measurement error, shared regional influences, income/workforce confounding, or current-versus-2021 income classifications. Subgroup comparisons are exploratory; no multiple-testing correction or causal adjustment is applied. An interval near 0% or 100% does not make a small subgroup reliable.", "",
                  "Calculation code uses Python's standard library; the current 2x2 results were independently checked against scipy.stats.fisher_exact and scipy.stats.chi2_contingency(correction=False)."])
    return lines


def svg_bar(title: str, subtitle: str, labels: list[str], values: list[float], path: Path) -> None:
    width, height = 800, 500
    left, right, top, bottom = 95, 40, 95, 80
    chart_w, chart_h = width - left - right, height - top - bottom
    ymax = max(values) * 1.12 if max(values) else 1
    step = chart_w / len(values)
    bar_w = step * 0.58

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="38" text-anchor="middle" font-family="Arial" font-size="23" font-weight="bold">{title}</text>',
        f'<text x="{width/2}" y="64" text-anchor="middle" font-family="Arial" font-size="14">{subtitle}</text>',
        f'<line x1="{left}" y1="{top+chart_h}" x2="{left+chart_w}" y2="{top+chart_h}" stroke="#333"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+chart_h}" stroke="#333"/>',
        f'<text x="25" y="{top+chart_h/2}" transform="rotate(-90 25 {top+chart_h/2})" text-anchor="middle" font-family="Arial" font-size="15">Dentists per 10,000 population (median)</text>',
    ]
    for i, (label, value) in enumerate(zip(labels, values)):
        x = left + step * i + (step - bar_w) / 2
        h = chart_h * value / ymax
        y = top + chart_h - h
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" fill="#777"/>')
        parts.append(f'<text x="{x+bar_w/2:.1f}" y="{max(85,y-8):.1f}" text-anchor="middle" font-family="Arial" font-size="14" font-weight="bold">{value:.2f}</text>')
        parts.append(f'<text x="{x+bar_w/2:.1f}" y="{top+chart_h+28}" text-anchor="middle" font-family="Arial" font-size="13">{label}</text>')
    parts.append(f'<text x="{width/2}" y="{height-15}" text-anchor="middle" font-family="Arial" font-size="11">Source: WHO GHO/NCD CCS; World Bank. Author\'s calculations.</text>')
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    rows = read_rows()
    fresh = [r for r in rows if int(r["dentist_data_year"]) >= 2018]

    access_stats = {}
    fresh_access_stats = {}
    for cat in ACCESS_CATS:
        vals = [float(r["dentists_per_10000"]) for r in rows if r["oral_health_access_category"] == cat]
        fresh_vals = [float(r["dentists_per_10000"]) for r in fresh if r["oral_health_access_category"] == cat]
        access_stats[cat] = summarize(vals)
        fresh_access_stats[cat] = summarize(fresh_vals)

    income_stats = {}
    for group in INCOME_CATS:
        vals = [float(r["dentists_per_10000"]) for r in rows if r["income_group"] == group]
        income_stats[group] = summarize(vals)

    density = [float(r["dentists_per_10000"]) for r in rows]
    access_ord = [ACCESS_ORDER[r["oral_health_access_category"]] for r in rows]
    income_ord = [INCOME_ORDER[r["income_group"]] for r in rows]

    rho_density_access = spearman(density, access_ord)
    rho_density_income = spearman(density, income_ord)
    rho_income_access = spearman(income_ord, access_ord)
    rho_fresh = spearman(
        [float(r["dentists_per_10000"]) for r in fresh],
        [ACCESS_ORDER[r["oral_health_access_category"]] for r in fresh],
    )

    lines = [
        "# Reproducible Research Analysis Summary",
        "",
        f"- Primary matched sample: {len(rows)} countries",
        f"- 2018–2023 dentist-data sensitivity sample: {len(fresh)} countries",
        f"- Spearman ρ, dentist density vs access: {rho_density_access:.3f}",
        f"- Spearman ρ, dentist density vs access (fresh sample): {rho_fresh:.3f}",
        f"- Spearman ρ, dentist density vs income group: {rho_density_income:.3f}",
        f"- Spearman ρ, income group vs access: {rho_income_access:.3f}",
        "",
        "## Dentist density by access category",
        "",
        "| Access category | n | Mean | Median | Q1 | Q3 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for cat in ACCESS_CATS:
        s = access_stats[cat]
        lines.append(f"| {cat} | {s['n']} | {s['mean']:.2f} | {s['median']:.2f} | {s['q1']:.2f} | {s['q3']:.2f} |")

    lines.extend([
        "",
        "## Dentist density by income group",
        "",
        "| Income group | n | Mean | Median | Q1 | Q3 |",
        "|---|---:|---:|---:|---:|---:|",
    ])
    for group in INCOME_CATS:
        s = income_stats[group]
        lines.append(f"| {group} | {s['n']} | {s['mean']:.2f} | {s['median']:.2f} | {s['q1']:.2f} | {s['q3']:.2f} |")

    lines.extend([
        "",
        "## Access composition by income group",
        "",
        "| Income group | Not achieved | Partially achieved | Fully achieved |",
        "|---|---:|---:|---:|",
    ])
    for group in INCOME_CATS:
        rr = [r for r in rows if r["income_group"] == group]
        counts = Counter(r["oral_health_access_category"] for r in rr)
        n = len(rr)
        lines.append(
            f"| {group} | {100*counts['Not achieved']/n:.1f}% | "
            f"{100*counts['Partially achieved']/n:.1f}% | {100*counts['Fully achieved']/n:.1f}% |"
        )

    lines.extend(timing_checks(rows))
    lines.extend(financing_checks(rows))
    lines.extend(financing_uncertainty(rows))
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    FIG_DIR.mkdir(exist_ok=True)

    svg_bar(
        "Median Dentist Density by Basic Service Availability",
        f"{len(rows)}-country matched sample",
        ["Not achieved", "Partially achieved", "Fully achieved"],
        [access_stats[c]["median"] for c in ACCESS_CATS],
        FIG_DIR / "dentist-density-by-access.svg",
    )
    svg_bar(
        "Median Dentist Density by World Bank Income Group",
        f"{len(rows)}-country matched sample",
        ["Low", "Lower middle", "Upper middle", "High"],
        [income_stats[c]["median"] for c in INCOME_CATS],
        FIG_DIR / "dentist-density-by-income.svg",
    )

    print(f"Wrote {OUT}")
    print("Regenerated figures/dentist-density-by-access.svg")
    print("Regenerated figures/dentist-density-by-income.svg")


if __name__ == "__main__":
    main()
