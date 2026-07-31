# Methodology Notes

## Data Extraction (SEC EDGAR)

- Financial metrics were pulled from the SEC EDGAR Company Facts API for Walmart, covering fiscal years 2008–2025.
- Seven metrics were extracted: Revenue, Net Income, Operating Cash Flow, Capital Expenditure, Diluted EPS, Total Assets, Stockholders' Equity.
- SEC XBRL tags fall into two types, which required different handling:
  - **Flow metrics** (Revenue, Net Income) report a `start` and `end` date and were filtered/deduplicated using a duration-based function.
  - **Snapshot metrics** (Assets, Stockholders' Equity) only report an `end` date, so the duration-based logic didn't apply — these were filtered separately.
- Diluted EPS required the unit key `USD/shares` rather than `USD` (the `USD` unit only returned a handful of stray, unusable entries).
- Where a metric was restated across multiple filings for the same period, the earliest-filed value was kept to avoid double-counting.


## Known Data Gaps

- Assets and Stockholders' Equity are missing (NaN) for FY2007, since SEC XBRL filing history only goes back to roughly 2009. The full 2007–2025 range was kept rather than truncating the dataset, and this gap is accepted as a known limitation.

## Validation Against Walmart's Official Annual Report

- The final merged dataset was cross-checked against Walmart's official FY2026 annual report.
- Revenue and Diluted EPS matched exactly.
- Minor discrepancies in Net Income and pre-2014 Revenue were investigated and traced to two known, documented causes rather than pipeline errors:
  - Differences in how noncontrolling interest is treated in reported totals.
  - SEC filing restatements issued after the original period was reported.

## Store Count Discrepancy (Executive Summary vs. Store Analytics)

- The **Executive Summary** dashboard's store count is sourced from a historical store-count-by-fiscal-year table (through FY2025).
- The **Store Analytics** dashboard's store count is sourced from a live/current U.S. store-locator dataset, which reflects stores as of data collection and includes a small number added since FY2025 closed.
- This is why the two dashboards show slightly different totals (4,605 vs. 4,619) — it's a known, intentional difference in what each number represents (a historical snapshot vs. a current count), not a data error.
