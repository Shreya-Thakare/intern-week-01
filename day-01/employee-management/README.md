# Employee Management CLI

## Project Overview
A command-line application for managing employee records: add, update,
delete, search, list, and analyze salary/department data. Built as the
Day 1 practical assignment of the 10-Day Intern Technical Training program.

## Problem Statement
Small teams need a lightweight way to track employee records (name,
department, salary, email) without setting up a database or web server.
This CLI provides that functionality with persistent local storage.

## Features
- **Add** a new employee (auto-incrementing ID)
- **Update** an existing employee's name, department, salary, or email
- **Delete** an employee by ID
- **Search** employees by name, department, or ID
- **List** all employees, sorted by ID
- **Highest Salary** — show the top-paid employee
- **Average Salary** — compute the average salary across all employees
- **Department Filter** — list employees in a given department
- Input validation (non-empty name, non-negative salary)
- Data persists between runs in a local JSON file

## Technology Stack
- Python 3.10+ (standard library only — `dataclasses`, `json`, `os`)
- No external dependencies

## Architecture
```
employee-management/
├── employee.py     # Employee dataclass (model)
├── storage.py       # JSON read/write (persistence layer)
├── manager.py        # EmployeeManager: business logic / operations
├── main.py            # CLI: menu, input handling, orchestration
└── data/
    └── employees.json  # Persisted employee records
```
The layers are deliberately separated:
- `main.py` only handles user interaction (I/O).
- `manager.py` only handles business rules (validation, search, stats).
- `storage.py` only handles reading/writing the JSON file.

This means the storage format or the UI (e.g. swapping the CLI for a
web API) could be changed independently without touching the other
layers.

## Installation
```bash
# No installation needed — just Python 3.10+
git clone <repo-url>
cd employee-management
```

## Environment Variables
None required. The data file path is resolved automatically relative
to the project folder (`data/employees.json`).

## How to Run
```bash
python main.py
```
Then follow the on-screen menu (options 1–9).

## Screenshots
Not applicable (console application).

## Challenges Faced
- Deciding where to draw the line between the CLI layer and the
  business-logic layer so each could be tested independently.
- Handling partial updates (leaving a field blank to keep its current
  value) without introducing ambiguous "empty string vs. no change"
  behavior for numeric fields like salary.

## Solutions
- Used a manager class (`EmployeeManager`) with keyword-argument
  updates, where `None` explicitly means "no change" for salary,
  while empty strings are treated as "no change" for text fields.
- Wrote a non-interactive test script (calling `EmployeeManager`
  directly) to verify business logic separately from the CLI's
  input-handling, plus a piped-input run of `main.py` to confirm the
  full interactive flow.

## Future Improvements
- Add unit tests (e.g. with `pytest`) instead of ad-hoc scripts.
- Support CSV export/import.
- Add sorting options in the CLI (currently `list_employees` sorts by
  ID only).
- Add pagination for large employee lists.
