"""
CSV / JSON Data Analyzer
Reports: record count, missing values, duplicates,
averages, min/max, category-wise statistics
"""

import csv
from pathlib import Path
from collections import defaultdict
from statistics import mean, median
from typing import List, Dict, Any


def load_csv(filepath: Path) -> List[Dict[str, Any]]:
    records = []
    try:
        with open(filepath, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numeric fields safely
                for key in ("id", "age"):
                    if row.get(key):
                        try:
                            row[key] = int(row[key])
                        except ValueError:
                            row[key] = None
                if row.get("marks"):
                    try:
                        row["marks"] = float(row["marks"])
                    except ValueError:
                        row["marks"] = None
                else:
                    row["marks"] = None
                records.append(row)
    except FileNotFoundError:
        print(f"[Error] File not found: {filepath}")
    except Exception as e:
        print(f"[Error] Failed to read CSV: {e}")
    return records


def analyze(records: List[Dict[str, Any]]) -> None:
    if not records:
        print("No records to analyze.")
        return

    total = len(records)
    print("\n" + "=" * 50)
    print("DATA ANALYSIS REPORT")
    print("=" * 50)
    print(f"Total records          : {total}")

    # Missing values
    missing = defaultdict(int)
    for r in records:
        for k, v in r.items():
            if v is None or (isinstance(v, str) and v.strip() == ""):
                missing[k] += 1
    print("\nMissing values:")
    if missing:
        for col, cnt in missing.items():
            print(f"  {col:15} : {cnt}")
    else:
        print("  None")

    # Duplicates (by name + department + marks for demo)
    seen = set()
    duplicates = 0
    for r in records:
        key = (r.get("name"), r.get("department"), r.get("marks"))
        if key in seen:
            duplicates += 1
        else:
            seen.add(key)
    print(f"\nPotential duplicate rows : {duplicates}")

    # Numeric stats on marks
    marks = [r["marks"] for r in records if r.get("marks") is not None]
    if marks:
        print(f"\nMarks Statistics (n={len(marks)}):")
        print(f"  Average  : {mean(marks):.2f}")
        print(f"  Median   : {median(marks):.2f}")
        print(f"  Minimum  : {min(marks):.2f}")
        print(f"  Maximum  : {max(marks):.2f}")
    else:
        print("\nNo valid marks data.")

    # Category-wise (department)
    print("\nCategory-wise Statistics (by Department):")
    dept_groups = defaultdict(list)
    for r in records:
        dept = r.get("department") or "Unknown"
        if r.get("marks") is not None:
            dept_groups[dept].append(r["marks"])

    print(f"{'Department':<20} {'Count':>6} {'Avg':>8} {'Min':>8} {'Max':>8}")
    print("-" * 55)
    for dept, mlist in sorted(dept_groups.items()):
        print(f"{dept:<20} {len(mlist):>6} {mean(mlist):>8.2f} {min(mlist):>8.2f} {max(mlist):>8.2f}")

    # Age stats
    ages = [r["age"] for r in records if r.get("age") is not None]
    if ages:
        print(f"\nAge Statistics:")
        print(f"  Average  : {mean(ages):.1f}")
        print(f"  Min/Max  : {min(ages)} / {max(ages)}")

    print("=" * 50 + "\n")


def main():
    csv_file = Path(__file__).parent / "sample_students.csv"
    print(f"Analyzing: {csv_file}")
    records = load_csv(csv_file)
    analyze(records)


if __name__ == "__main__":
    main()
