# Day 3 — Data Analysis & Python for AI/ML

## Project Overview
This project analyzes a synthetic **facility hygiene inspection dataset** (1,000 records
covering public washrooms across 10 locations in Nagpur) using NumPy and Pandas, and
visualizes the findings with Matplotlib. It covers the full Day 3 objective: inspect,
clean, analyze, and visualize real-world (here, synthetic) tabular data, and produce
insights that feed directly into the Day 4 machine learning task.

## Problem Statement
Facility managers need to know **which facilities and locations are at risk of poor
hygiene** so cleaning resources can be prioritized. The raw dataset has quality issues
typical of real-world data collection — missing values, duplicate inspection records —
that must be identified and resolved before any analysis or modeling can be trusted.

## Features
- Automated missing-value, duplicate, invalid-range and outlier detection
- A reproducible cleaning pipeline (median/mode imputation, duplicate removal)
- Descriptive statistics (mean, median, std, min, max) for every numeric field
- Group-wise aggregations: by location, facility type, hygiene risk, water availability
- A feature correlation matrix
- Five charts: 2 bar charts, 1 histogram, 1 scatter plot, 1 correlation heatmap
- Written insights derived directly from the computed statistics

## Technology Stack
- **Python 3**
- **Pandas** — loading, cleaning, grouping, aggregation
- **NumPy** — statistical calculations
- **Matplotlib** — visualization
- **openpyxl** (via pandas) — reading/writing `.xlsx`

## Architecture
```
Raw Excel dataset
      │
      ▼
data-cleaning/clean_data.py   → inspects & reports issues, cleans, writes cleaned CSV/XLSX
      │
      ▼
analysis/analysis.py          → computes statistics & insights (JSON + Markdown)
      │
      ▼
visualizations/make_visuals.py → generates 5 PNG charts from the cleaned data
```
Each script is independent and re-runnable; the cleaned dataset in `dataset/` is the
single shared artifact that the analysis and visualization scripts both read from.

## Dataset Fields
`facility_id`, `location`, `facility_type`, `cleanliness_score` (0–10),
`odor_score` (0–10), `waste_level` (0–100 %), `water_availability` (Yes/No),
`footfall`, `complaints`, `inspection_date`, `hours_since_cleaning`,
`hygiene_risk` (Low / Medium / High).

## Data Quality Findings (Raw Data)
| Check | Result |
|---|---|
| Missing `cleanliness_score` | 5 rows |
| Missing `waste_level` | 3 rows |
| Missing `water_availability` | 2 rows |
| Fully duplicated inspection rows | 5 rows (same `facility_id`, re-appended at the end of the file) |
| Values outside valid range (scores 0–10, waste 0–100, no negatives) | 0 — no invalid values found |
| Outliers (IQR method) | `hours_since_cleaning`: 63 · `complaints`: 13 · `footfall`: 3 · `cleanliness_score`: 2 · `odor_score` / `waste_level`: 0 |

**Cleaning actions taken:** duplicate rows dropped (kept first occurrence) →
`cleanliness_score` and `waste_level` missing values filled with the column **median**
→ `water_availability` missing values filled with the column **mode** ("Yes"). Outliers
were **kept** (not removed) since values like 30+ hours since cleaning or 10+ complaints
are plausible real-world extremes and are informative for Day 4's risk prediction model,
rather than data errors.

Result: **995 clean records**, 0 missing values, 0 duplicates.

## Key Statistics (Cleaned Data)
| Metric | Mean | Median | Std Dev | Min | Max |
|---|---|---|---|---|---|
| Cleanliness Score (0–10) | 6.42 | 6.40 | 1.73 | 1.1 | 10.0 |
| Odor Score (0–10) | 4.63 | 4.60 | 2.04 | 1.0 | 10.0 |
| Waste Level (%) | 43.99 | 44.0 | 20.56 | 0.0 | 100.0 |
| Footfall | 441.8 | 435 | 205.3 | 20 | 1148 |
| Complaints | 4.49 | 4.0 | 2.46 | 0 | 12 |
| Hours Since Cleaning | 7.61 | 5.3 | 7.27 | 0.5 | 36.0 |

**Hygiene risk distribution:** Medium 41.2% (410) · Low 31.5% (313) · High 27.3% (272)

## Insights
1. **Time since last cleaning tracks closely with hygiene risk.** High-risk facilities
   averaged 10.06 hours since their last cleaning vs. 5.81 hours for low-risk facilities
   — nearly double the gap — even though it's only weakly linearly correlated with the
   raw cleanliness score, so it behaves more like a risk-tier signal than a straight-line
   predictor.
2. **Water availability is the strongest categorical split in the data.** Facilities
   without water access were rated High risk 63.6% of the time, versus 22.5% for
   facilities with water available.
3. **Hygiene quality varies by location.** Manish Nagar has the highest average
   cleanliness score (6.62); Sitabuldi has the lowest (6.09) and also receives the most
   complaints per facility on average (5.0) — a strong candidate for prioritized cleaning.
4. **Odor and complaints move together** (correlation 0.59), making odor score a useful
   early-warning feature.
5. Full correlation matrix and all group-wise tables are in
   `analysis/summary_statistics.json`.

## Visualizations
All charts are in `visualizations/`:
| File | Type | Shows |
|---|---|---|
| `bar_avg_cleanliness_by_location.png` | Bar chart | Average cleanliness score per location |
| `bar_hygiene_risk_distribution.png` | Bar chart | Count of facilities per hygiene risk class |
| `hist_cleanliness_score.png` | Histogram | Distribution of cleanliness scores across all facilities |
| `scatter_odor_vs_complaints.png` | Scatter plot | Odor score vs. complaints, colored by hygiene risk |
| `heatmap_feature_correlation.png` | Additional (heatmap) | Correlation between all numeric features |

## Installation
```bash
pip install pandas numpy matplotlib openpyxl
```

## How to Run
```bash
cd data-cleaning && python3 clean_data.py      # produces dataset/facility_hygiene_cleaned.csv
cd ../analysis && python3 analysis.py          # produces summary_statistics.json, insights.md
cd ../visualizations && python3 make_visuals.py # produces 5 PNG charts
```

## Challenges Faced
- The dataset's only 5 duplicate rows and 10 total missing values were appended at the
  very end of the file rather than scattered, so a naive `df.duplicated()` check on the
  full row initially looked "too clean" — cross-checking against `facility_id` duplicates
  confirmed the same 5 records.
- Deciding whether to drop or keep outliers: since `hours_since_cleaning` and
  `complaints` had many IQR outliers but no invalid (out-of-range) values, they were
  judged to be genuine extreme cases rather than data errors, and were kept.

## Solutions
- Cross-validated duplicate detection using both the full-row check and the
  `facility_id` subset check to be certain no duplicates were missed.
- Used the IQR method purely for *reporting* outliers, and used documented valid ranges
  (0–10 for scores, 0–100% for waste level, non-negative counts) as the actual filter
  for what counts as an *invalid* value worth correcting.

## Future Improvements
- Engineer a `facility_age` or `days_since_last_inspection` feature from
  `inspection_date` for Day 4 modeling.
- Add a per-location, per-month trend chart once more inspection cycles are available.
- Build an interactive dashboard (Day 6/7) on top of `summary_statistics.json`.
