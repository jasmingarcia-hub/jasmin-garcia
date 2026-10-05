#!/usr/bin/env python3
"""Build the country-level dataset for the economic-research paper.

Sources:
- WHO GHO OData API
- World Bank API

Primary outcome:
- Direct ORALHEALTH_SERVICESPHCFACILITIES if available; otherwise a category
  derived from three WHO service components. Saved baseline uses 2021 components.

Dentist density:
- HWF_0010, latest observation on or before 2023

Income:
- Current World Bank country-API income group (not a historical classification)
- 2023 GDP per capita (NY.GDP.PCAP.CD)

Outputs:
- data/research_dataset.csv
- data/research_dataset_summary.md
"""

from __future__ import annotations

import csv
import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

WHO_BASE = "https://ghoapi.azureedge.net/api"
WB_BASE = "https://api.worldbank.org/v2"
TARGET_YEAR = 2023

WHO_INDICATORS = {
    "dentist_density": "HWF_0010",
    "access_category": "ORALHEALTH_SERVICESPHCFACILITIES",
    "screening_2021": "ORALHEALTH_AVAILABILITY_SCREENING",
    "urgent_care_2021": "ORALHEALTH_AVAILABILITY_URGENTCARE",
    "restorative_2021": "ORALHEALTH_AVAILABILITY_RESTORATIVE",
}


def get_json(url: str):
    req = Request(url, headers={"User-Agent": "economic-research-coursework/1.0"})
    with urlopen(req, timeout=60) as response:
        return json.load(response)


def who_records(code: str) -> list[dict]:
    data = get_json(f"{WHO_BASE}/{code}?$format=json")
    return data.get("value", [])


def row_year(row: dict) -> int | None:
    value = row.get("TimeDim")
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def numeric_value(row: dict) -> float | None:
    for key in ("NumericValue", "Value"):
        value = row.get(key)
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            match = re.search(r"-?\d+(?:\.\d+)?", value.replace(",", ""))
            if match:
                return float(match.group())
    return None


def text_value(row: dict) -> str | None:
    for key in ("Value", "Dim1", "Dim2", "Comments"):
        value = row.get(key)
        if value not in (None, ""):
            return str(value).strip()
    return None


def latest_by_country(records: list[dict], max_year: int | None = None) -> dict[str, dict]:
    chosen: dict[str, dict] = {}
    for row in records:
        iso3 = row.get("SpatialDim")
        year = row_year(row)
        if not iso3 or year is None:
            continue
        if max_year is not None and year > max_year:
            continue
        prior = chosen.get(iso3)
        if prior is None or year > row_year(prior):
            chosen[iso3] = row
    return chosen


def exact_year_by_country(records: list[dict], year: int) -> dict[str, dict]:
    exact = {r.get("SpatialDim"): r for r in records if r.get("SpatialDim") and row_year(r) == year}
    if exact:
        return exact
    # If the GHO series labels the newest survey differently, use latest <= target
    return latest_by_country(records, max_year=year)


def world_bank_countries() -> dict[str, dict]:
    data = get_json(f"{WB_BASE}/country?format=json&per_page=400")
    rows = data[1]
    countries = {}
    for row in rows:
        iso3 = row.get("id")
        region = (row.get("region") or {}).get("value")
        if not iso3 or not region or region == "Aggregates":
            continue
        countries[iso3] = {
            "country": row.get("name"),
            "income_group": (row.get("incomeLevel") or {}).get("value"),
            "region": region,
        }
    return countries


def world_bank_gdp(year: int) -> dict[str, float | None]:
    params = urlencode({"format": "json", "per_page": 400, "date": year})
    data = get_json(f"{WB_BASE}/country/all/indicator/NY.GDP.PCAP.CD?{params}")
    rows = data[1] if len(data) > 1 and data[1] else []
    return {
        row["countryiso3code"]: row.get("value")
        for row in rows
        if row.get("countryiso3code")
    }


def normalize_access(value: str | None) -> str | None:
    if not value:
        return None
    low = value.lower()
    if "fully" in low:
        return "Fully achieved"
    if "partial" in low:
        return "Partially achieved"
    if "not achieved" in low or low.strip() in {"no", "none"}:
        return "Not achieved"
    if "no information" in low or "no data" in low:
        return None
    return None


def availability_binary(value: str | None) -> int | None:
    """Map a reported WHO component response to 1/0 without treating missing as no."""
    if not value:
        return None
    low = value.strip().lower()
    if "unavailable" in low or low in {"no", "not available"}:
        return 0
    if "available" in low or low in {"yes"}:
        return 1
    return None


def derive_access_category(*values: str | None) -> str | None:
    """Apply WHO Core Indicator 4.1 rules when all three components are reported."""
    binary = [availability_binary(v) for v in values]
    if any(v is None for v in binary):
        return None
    score = sum(binary)
    if score == 3:
        return "Fully achieved"
    if score in (1, 2):
        return "Partially achieved"
    return "Not achieved"


def main() -> None:
    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)

    wb = world_bank_countries()
    gdp = world_bank_gdp(TARGET_YEAR)
    gdp_2021 = world_bank_gdp(2021)

    dentist_records = who_records(WHO_INDICATORS["dentist_density"])
    dentist = latest_by_country(
        dentist_records,
        max_year=TARGET_YEAR,
    )
    dentist_2021 = latest_by_country(
        [r for r in dentist_records if r.get("SpatialDimType") == "COUNTRY"], 2021
    )
    access = exact_year_by_country(
        who_records(WHO_INDICATORS["access_category"]),
        TARGET_YEAR,
    )
    screening = latest_by_country(
        who_records(WHO_INDICATORS["screening_2021"]),
        max_year=TARGET_YEAR,
    )
    urgent = latest_by_country(
        who_records(WHO_INDICATORS["urgent_care_2021"]),
        max_year=TARGET_YEAR,
    )
    restorative = latest_by_country(
        who_records(WHO_INDICATORS["restorative_2021"]),
        max_year=TARGET_YEAR,
    )

    rows = []
    for iso3, meta in sorted(wb.items(), key=lambda item: item[1]["country"] or item[0]):
        d = dentist.get(iso3)
        d21 = dentist_2021.get(iso3)
        a = access.get(iso3)
        s = screening.get(iso3)
        u = urgent.get(iso3)
        r = restorative.get(iso3)

        screening_value = text_value(s) if s else None
        urgent_value = text_value(u) if u else None
        restorative_value = text_value(r) if r else None
        direct_access = normalize_access(text_value(a)) if a else None
        derived_access = derive_access_category(
            screening_value, urgent_value, restorative_value
        )
        access_category = direct_access or derived_access
        component_years = [
            y for y in (row_year(s) if s else None, row_year(u) if u else None, row_year(r) if r else None)
            if y is not None
        ]

        rows.append({
            "iso3": iso3,
            "country": meta["country"],
            "world_bank_region": meta["region"],
            "income_group": meta["income_group"],
            "gdp_per_capita_2023_usd": gdp.get(iso3),
            "dentists_per_10000": numeric_value(d) if d else None,
            "dentist_data_year": row_year(d) if d else None,
            "dentists_per_10000_on_or_before_2021": numeric_value(d21) if d21 else None,
            "dentist_data_year_on_or_before_2021": row_year(d21) if d21 else None,
            "gdp_per_capita_2021_usd": gdp_2021.get(iso3),
            "oral_health_access_category": access_category,
            "access_source": "WHO direct 2023 indicator" if direct_access else (
                "Derived from WHO component indicators" if derived_access else None
            ),
            "access_data_year": row_year(a) if direct_access and a else (
                max(component_years) if derived_access and component_years else None
            ),
            "screening_available": screening_value,
            "urgent_care_available": urgent_value,
            "restorative_care_available": restorative_value,
        })

    fields = list(rows[0].keys())
    csv_path = output_dir / "research_dataset.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    matched = [
        row for row in rows
        if row["dentists_per_10000"] is not None
        and row["oral_health_access_category"] in {
            "Fully achieved", "Partially achieved", "Not achieved"
        }
        and row["income_group"]
    ]
    access_counts = Counter(row["oral_health_access_category"] for row in matched)
    income_counts = Counter(row["income_group"] for row in matched)
    dentist_years = [row["dentist_data_year"] for row in matched if row["dentist_data_year"]]

    summary = [
        "# Research Dataset Summary",
        "",
        f"- Workforce/GDP target year: {TARGET_YEAR}; access timing is recorded separately in access_data_year",
        f"- World Bank countries/territories retained: {len(rows)}",
        f"- Countries with complete primary analysis fields: {len(matched)}",
        f"- Countries missing at least one primary field: {len(rows) - len(matched)}",
        "",
        "## Matched sample by oral-health access category",
        "",
    ]
    for category in ("Not achieved", "Partially achieved", "Fully achieved"):
        summary.append(f"- {category}: {access_counts.get(category, 0)}")

    summary.extend(["", "## Matched sample by World Bank income group", ""])
    for group, count in sorted(income_counts.items()):
        summary.append(f"- {group}: {count}")

    if dentist_years:
        recent_5yr = sum(y >= 2018 for y in dentist_years)
        recent_10yr = sum(y >= 2013 for y in dentist_years)
        pre_2013 = sum(y < 2013 for y in dentist_years)
        summary.extend([
            "",
            "## Dentist-density observation years in matched sample",
            "",
            f"- Earliest: {min(dentist_years)}",
            f"- Latest: {max(dentist_years)}",
            f"- 2018–2023 (within 5 years of target year): {recent_5yr}",
            f"- 2013–2023 (within 10 years of target year): {recent_10yr}",
            f"- Before 2013: {pre_2013}",
            "",
            "A sensitivity analysis should repeat the main comparison using only countries with dentist-density observations from 2018–2023.",
        ])

    summary.extend([
        "",
        "## Matching rule",
        "",
        "Primary analysis requires a WHO oral-health access category, a WHO dentist-density observation (latest available on or before 2023), and a World Bank income group. The script first uses the direct WHO 2023 category if exposed through the API; otherwise it applies WHO Core Indicator 4.1 classification rules to the three reported component services. A category is derived only when all three component responses are present. Missing responses are never coded as unavailable. GDP per capita is retained as a continuous supporting variable but is not required for inclusion in the primary categorical analysis.",
        "",
        "## Timing and provenance audit",
        "",
        f"- Matched access sources: {dict(Counter(row['access_source'] for row in matched))}",
        f"- Matched access observation years: {dict(Counter(row['access_data_year'] for row in matched))}",
        "- Income groups are current classifications returned by the World Bank country API during extraction, not historical 2023 classifications. GDP is for 2023.",
        "- Workforce may postdate the component outcome. The 2018–2023 subset tests workforce recency, not alignment with a 2021 outcome. See data/research_analysis_summary.md for the latest-on/before-2021 sensitivity check.",
        "- Do not equate a derived 2021 sample with WHO's direct 2023 aggregate benchmark.",
        "",
        "## Important interpretation note",
        "",
        "The WHO access category measures reported availability of oral-health services in primary health care facilities. It does not directly measure utilization, affordability, quality, or within-country geographic access.",
    ])

    (output_dir / "research_dataset_summary.md").write_text(
        "\n".join(summary) + "\n", encoding="utf-8"
    )

    print(f"Wrote {csv_path}")
    print("Wrote data/research_dataset_summary.md")
    print(f"Complete primary-analysis countries: {len(matched)}")


def align_existing(dentist_json: str | None = None, gdp_json: str | None = None) -> None:
    """Append timing-check fields without changing the saved baseline values."""
    path = Path("data/research_dataset.csv")
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames)
        rows = list(reader)
    records = json.loads(Path(dentist_json).read_text())["value"] if dentist_json else who_records("HWF_0010")
    records = [r for r in records if r.get("SpatialDimType") == "COUNTRY"]
    aligned = latest_by_country(records, 2021)
    if gdp_json:
        response = json.loads(Path(gdp_json).read_text())
        if response[0]["pages"] != 1:
            raise ValueError("GDP response is incomplete")
        gdp = {r["countryiso3code"]: r["value"] for r in response[1] if r.get("countryiso3code")}
    else:
        gdp = world_bank_gdp(2021)
    new_fields = ["dentists_per_10000_on_or_before_2021", "dentist_data_year_on_or_before_2021", "gdp_per_capita_2021_usd"]
    fields.extend(n for n in new_fields if n not in fields)
    for row in rows:
        record = aligned.get(row["iso3"])
        row[new_fields[0]] = numeric_value(record) if record else None
        row[new_fields[1]] = row_year(record) if record else None
        row[new_fields[2]] = gdp.get(row["iso3"])
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print("Appended 2021 timing fields; original baseline fields preserved.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--align-existing", action="store_true")
    parser.add_argument("--dentist-json")
    parser.add_argument("--gdp-json")
    args = parser.parse_args()
    if args.align_existing:
        align_existing(args.dentist_json, args.gdp_json)
    else:
        main()
