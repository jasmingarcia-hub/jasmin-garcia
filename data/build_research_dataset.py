#!/usr/bin/env python3
"""Build the country-level dataset for the economic-research paper.

Sources:
- WHO GHO OData API
- World Bank API

Primary outcome:
- ORALHEALTH_SERVICESPHCFACILITIES (WHO 2023 oral-health service availability)

Dentist density:
- HWF_0010, latest observation on or before 2023

Income:
- World Bank income group and 2023 GDP per capita (NY.GDP.PCAP.CD)

Outputs:
- data/research_dataset.csv
- data/research_dataset_summary.md
"""

from __future__ import annotations

import csv
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
    return value


def main() -> None:
    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)

    wb = world_bank_countries()
    gdp = world_bank_gdp(TARGET_YEAR)

    dentist = latest_by_country(
        who_records(WHO_INDICATORS["dentist_density"]),
        max_year=TARGET_YEAR,
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
        a = access.get(iso3)
        s = screening.get(iso3)
        u = urgent.get(iso3)
        r = restorative.get(iso3)

        rows.append({
            "iso3": iso3,
            "country": meta["country"],
            "world_bank_region": meta["region"],
            "income_group": meta["income_group"],
            "gdp_per_capita_2023_usd": gdp.get(iso3),
            "dentists_per_10000": numeric_value(d) if d else None,
            "dentist_data_year": row_year(d) if d else None,
            "oral_health_access_2023": normalize_access(text_value(a)) if a else None,
            "access_data_year": row_year(a) if a else None,
            "screening_available_2021": text_value(s) if s else None,
            "urgent_care_available_2021": text_value(u) if u else None,
            "restorative_care_available_2021": text_value(r) if r else None,
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
        and row["oral_health_access_2023"] in {
            "Fully achieved", "Partially achieved", "Not achieved"
        }
        and row["income_group"]
    ]
    access_counts = Counter(row["oral_health_access_2023"] for row in matched)
    income_counts = Counter(row["income_group"] for row in matched)
    dentist_years = [row["dentist_data_year"] for row in matched if row["dentist_data_year"]]

    summary = [
        "# Research Dataset Summary",
        "",
        f"- Target oral-health access year: {TARGET_YEAR}",
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
        summary.extend([
            "",
            "## Dentist-density observation years in matched sample",
            "",
            f"- Earliest: {min(dentist_years)}",
            f"- Latest: {max(dentist_years)}",
        ])

    summary.extend([
        "",
        "## Matching rule",
        "",
        "Primary analysis requires a WHO 2023 access category, a WHO dentist-density observation (latest available on or before 2023), and a World Bank income group. GDP per capita is retained as a continuous supporting variable but is not required for inclusion in the primary categorical analysis.",
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


if __name__ == "__main__":
    main()
