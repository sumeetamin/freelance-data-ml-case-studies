# Catalog Data Pipeline (Synthetic Example)

## Problem

Large entertainment catalogs need consistent identifiers and duplicate handling across sources. The freelance work included assembling structured movie and series records and associating source metadata. This portfolio example uses synthetic rows only and contains no client catalog, image, or source data.

## Method

The companion script normalizes titles and years, creates a stable matching key, merges duplicate records, and retains the source URL values as provenance. It is a small local-file example rather than a live scraper; it avoids contacting third-party websites or republishing copyrighted media.

## Reproduce

Run `python normalize_catalog.py sample.csv normalized.json` from this folder.

## Production considerations

A production collector should use source-specific permission and rate limits, retries, schema validation, explicit provenance, quality checks, and a review process for ambiguous matches. Image rights and quality require separate verification.
