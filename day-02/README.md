# Day 2 — Python Development

## Objective
Learn Python well enough to write maintainable programs and process data.

## Topics Covered
- Syntax, Variables & Data Types
- Lists, Tuples, Sets, Dictionaries
- Conditions & Loops
- Functions, Lambda & List Comprehensions
- Modules, Packages & Exception Handling
- File Handling (CSV/JSON)
- Classes, Objects, Inheritance & Encapsulation
- Virtual Environments & pip

## Structure
```
day-02/
├── python-exercises/     # Topic-wise practice scripts
├── management-system/    # Full CRUD + Stats system (JSON)
├── csv-analysis/         # CSV reader with statistics
└── README.md
```

## How to Run
```bash
# Optional: create virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# No external packages required (pure standard library)

# Run exercises
python python-exercises/01_syntax_variables.py
python python-exercises/02_data_structures.py
python python-exercises/03_conditions_loops.py
python python-exercises/04_functions_lambda.py
python python-exercises/05_modules_exceptions.py
python python-exercises/06_file_handling.py
python python-exercises/07_oop_classes.py

# Management System
python management-system/student_management.py

# CSV Analysis
python csv-analysis/data_analyzer.py
```

## Deliverables Completed
- [x] All core Python concepts demonstrated
- [x] Student/Employee Management System (Add, Update, Delete, Search, Filter, Sort, Statistics)
- [x] CSV/JSON analysis with record count, missing values, duplicates, avg/min/max, category-wise stats
- [x] Exception handling throughout
