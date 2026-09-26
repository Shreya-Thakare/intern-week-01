"""
Day 3 - Data Cleaning Script
Facility Hygiene Dataset

Steps performed:
1. Load the raw dataset
2. Inspect and report missing values
3. Inspect and report duplicate records
4. Inspect and report invalid / out-of-range values
5. Detect outliers using the IQR method
6. Clean the dataset (impute / drop as appropriate)
7. Save the cleaned dataset to dataset/facility_hygiene_cleaned.csv
"""

import pandas as pd
import numpy as np
import json
import os

RAW_PATH = os.path.join(os.path.dirname(__file__), "..", "dataset", "facility_hygiene_raw.xlsx")
CLEAN_CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "dataset", "facility_hygiene_cleaned.csv")
REPORT_PATH = os.path.join(os.path.dirname(__file__), "cleaning_report.json")

NUMERIC_COLS = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "footfall",
    "complaints",
    "hours_since_cleaning",
]


def load_raw():
    return pd.read_excel(RAW_PATH, sheet_name="Facility Hygiene Dataset")


def report_missing(df):
    missing = df.isna().sum()
    return {col: int(count) for col, count in missing.items() if count > 0}


def report_duplicates(df):
    # Duplicate facility_id is the clearest signal of a duplicated inspection record
    dup_mask = df.duplicated(subset=["facility_id"], keep="first")
    return {
        "duplicate_rows_full": int(df.duplicated().sum()),
        "duplicate_facility_ids": int(dup_mask.sum()),
        "duplicate_facility_id_list": df.loc[dup_mask, "facility_id"].tolist(),
    }


def report_invalid(df):
    invalid = {}
    # Scores are documented on a 0-10 scale
    for col in ["cleanliness_score", "odor_score"]:
        bad = df[(df[col] < 0) | (df[col] > 10)]
        invalid[col + "_out_of_0_10_range"] = int(len(bad))
    # waste_level is a 0-100 percentage
    bad_waste = df[(df["waste_level"] < 0) | (df["waste_level"] > 100)]
    invalid["waste_level_out_of_0_100_range"] = int(len(bad_waste))
    # footfall / complaints cannot be negative
    invalid["negative_footfall"] = int((df["footfall"] < 0).sum())
    invalid["negative_complaints"] = int((df["complaints"] < 0).sum())
    invalid["negative_hours_since_cleaning"] = int((df["hours_since_cleaning"] < 0).sum())
    return invalid


def detect_outliers_iqr(df, col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    return {
        "q1": round(float(q1), 2),
        "q3": round(float(q3), 2),
        "iqr": round(float(iqr), 2),
        "lower_bound": round(float(lower), 2),
        "upper_bound": round(float(upper), 2),
        "outlier_count": int(len(outliers)),
    }


def clean(df):
    df = df.copy()

    # 1. Drop exact duplicate inspection records (same facility_id + same values),
    #    keeping the first occurrence.
    before = len(df)
    df = df.drop_duplicates(subset=["facility_id"], keep="first").reset_index(drop=True)
    dropped_duplicates = before - len(df)

    # 2. Impute missing numeric values with the column median (robust to outliers).
    imputed = {}
    for col in ["cleanliness_score", "waste_level"]:
        n_missing = int(df[col].isna().sum())
        if n_missing:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            imputed[col] = {"count": n_missing, "filled_with_median": round(float(median_val), 2)}

    # 3. Impute missing categorical values with the mode.
    if df["water_availability"].isna().sum():
        n_missing = int(df["water_availability"].isna().sum())
        mode_val = df["water_availability"].mode().iloc[0]
        df["water_availability"] = df["water_availability"].fillna(mode_val)
        imputed["water_availability"] = {"count": n_missing, "filled_with_mode": mode_val}

    # 4. Derive a helper column used later in analysis / modeling.
    df["inspection_date"] = pd.to_datetime(df["inspection_date"])
    df["inspection_month"] = df["inspection_date"].dt.to_period("M").astype(str)

    return df, {"dropped_duplicate_rows": dropped_duplicates, "imputed": imputed}


def main():
    df_raw = load_raw()

    report = {
        "raw_shape": list(df_raw.shape),
        "missing_values": report_missing(df_raw),
        "duplicates": report_duplicates(df_raw),
        "invalid_values": report_invalid(df_raw),
        "outliers_iqr": {col: detect_outliers_iqr(df_raw, col) for col in NUMERIC_COLS},
    }

    df_clean, clean_actions = clean(df_raw)
    report["cleaning_actions"] = clean_actions
    report["clean_shape"] = list(df_clean.shape)

    df_clean.to_csv(CLEAN_CSV_PATH, index=False)

    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=2, default=str)

    print(json.dumps(report, indent=2, default=str))
    print(f"\nCleaned dataset written to: {CLEAN_CSV_PATH}")


if __name__ == "__main__":
    main()
