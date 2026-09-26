# Day 1 — Programming Fundamentals & Problem Solving

## Project Overview
Day 1 of the 10-Day Intern Technical Training & Domain Assessment
Program. Covers programming fundamentals, core data structures &
algorithms, and Git basics, through 15 solved exercises plus a
practical Employee Management CLI application.

## Problem Statement
Build a strong foundation in programming logic, common data
structures (array, stack, queue, hash map), and basic algorithms
(searching, sorting, recursion) — then apply that foundation to a
small but complete CRUD application.

## Features
- 15 standalone exercises, each runnable independently and covering:
  string manipulation, arrays, hash maps, stacks/queues, sorting,
  searching, and recursion.
- A full Employee Management CLI with Add, Update, Delete, Search,
  List, Highest Salary, Average Salary, and Department Filter.

## Technology Stack
- Python 3.10+
- Standard library only (`dataclasses`, `json`, `os`, `collections`)
- Git for version control

## Architecture
```
day-01/
├── exercises/                  # 15 solved DSA/programming problems
│   ├── 01_reverse_string.py
│   ├── 02_palindrome_check.py
│   ├── 03_largest_second_largest.py
│   ├── 04_remove_duplicates.py
│   ├── 05_missing_number.py
│   ├── 06_duplicate_number.py
│   ├── 07_character_frequency.py
│   ├── 08_first_non_repeating_char.py
│   ├── 09_merge_sorted_arrays.py
│   ├── 10_common_elements.py
│   ├── 11_stack_implementation.py
│   ├── 12_queue_implementation.py
│   ├── 13_maximum_subarray_sum.py
│   ├── 14_sorting_without_builtin.py
│   └── 15_searching_and_recursion.py
├── employee-management/         # Practical assignment (own README)
│   ├── employee.py
│   ├── storage.py
│   ├── manager.py
│   ├── main.py
│   └── data/employees.json
└── README.md                    # This file
```

## Database Design
Not applicable — data is stored in a flat JSON file
(`employee-management/data/employees.json`). See the
`employee-management/README.md` for details.

## API Documentation
Not applicable — this is a console application, not a web API.

## Installation
```bash
git clone <repo-url>
cd day-01
```
No third-party packages are required; only Python 3.10+.

## Environment Variables
None required.

## How to Run

**Exercises** — each file can be run individually and prints its own
test output:
```bash
cd exercises
python 01_reverse_string.py
python 02_palindrome_check.py
# ...and so on for each file
```

**Employee Management CLI**:
```bash
cd employee-management
python main.py
```

## Screenshots
Not applicable (console output only).

## Challenges Faced
- Choosing algorithmically clean solutions (e.g. Kadane's algorithm
  for max subarray sum, the Gauss-sum trick for the missing number)
  instead of brute-force approaches, while keeping the code readable
  for a first-week intern audience.
- Structuring the CLI app so business logic could be tested without
  needing to simulate interactive input every time.

## Solutions
- Added inline complexity notes (time/space) in each exercise file to
  document *why* a given approach was chosen.
- Split the CLI into `employee.py` / `storage.py` / `manager.py` /
  `main.py` so the core logic could be exercised directly in a test
  script, and separately verified the full interactive flow using
  piped stdin input.

## Future Improvements
- Add automated unit tests (`pytest`) for both the exercises and the
  CLI application.
- Extend the Employee Management CLI with CSV import/export and
  richer filtering/sorting options.
