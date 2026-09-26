"""Day 2 - File Handling (text, JSON, CSV)"""

import json
import csv
from pathlib import Path

# Text file
text_path = Path("sample.txt")
with open(text_path, "w", encoding="utf-8") as f:
    f.write("Hello, Python!\nDay 2 File Handling\n")

with open(text_path, "r", encoding="utf-8") as f:
    content = f.read()
print("Text content:\n", content)

# JSON
data = [
    {"id": 1, "name": "Alice", "marks": 92},
    {"id": 2, "name": "Bob", "marks": 85}
]
json_path = Path("students.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open(json_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print("JSON loaded:", loaded)

# CSV
csv_path = Path("students.csv")
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "marks"])
    writer.writeheader()
    writer.writerows(data)

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("CSV rows:")
    for row in reader:
        print(row)

# Cleanup demo files (optional)
# text_path.unlink(missing_ok=True)
# json_path.unlink(missing_ok=True)
# csv_path.unlink(missing_ok=True)
