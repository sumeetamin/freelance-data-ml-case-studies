"""Normalize and deduplicate a synthetic catalog CSV using only the standard library."""
import csv
import json
import re
import sys
from pathlib import Path


def clean(value):
    return re.sub(r"\s+", " ", (value or "").strip())


def key(row):
    title = clean(row.get("title", "")).casefold()
    year = clean(row.get("year", ""))
    kind = clean(row.get("kind", "")).casefold()
    return title, year, kind


def normalize(input_path, output_path):
    records = {}
    with Path(input_path).open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            title, year, kind = key(row)
            if not title:
                continue
            item = records.setdefault((title, year, kind), {
                "title": clean(row.get("title", "")),
                "year": year,
                "kind": kind,
                "source_urls": [],
            })
            source_url = clean(row.get("source_url", ""))
            if source_url and source_url not in item["source_urls"]:
                item["source_urls"].append(source_url)
    Path(output_path).write_text(
        json.dumps(list(records.values()), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python normalize_catalog.py input.csv output.json")
    normalize(sys.argv[1], sys.argv[2])
