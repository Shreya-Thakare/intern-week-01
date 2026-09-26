"""
Storage layer: handles reading and writing employee records to a JSON
file on disk. Keeping this separate from the business logic (manager.py)
means the storage format could be swapped later (e.g. to CSV or a real
database) without touching the rest of the application.
"""

import json
import os
from employee import Employee

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "employees.json")


def load_employees() -> list[Employee]:
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: could not read data file ({e}). Starting with an empty list.")
        return []

    return [Employee.from_dict(item) for item in raw]


def save_employees(employees: list[Employee]) -> None:
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([e.to_dict() for e in employees], f, indent=2)
