"""Day 8 SQL demo using SQLite (in-memory) — no MySQL install required."""
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.executescript("""
CREATE TABLE departments (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE);
CREATE TABLE employees (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  department_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  salary REAL NOT NULL,
  FOREIGN KEY(department_id) REFERENCES departments(id)
);
CREATE TABLE facilities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  location TEXT NOT NULL,
  cleanliness_score REAL,
  water_availability INTEGER DEFAULT 1
);
CREATE TABLE inspections (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  facility_id INTEGER NOT NULL,
  inspection_date TEXT NOT NULL,
  cleanliness_score REAL,
  odor_score REAL,
  waste_level REAL,
  status TEXT NOT NULL,
  remarks TEXT,
  FOREIGN KEY(facility_id) REFERENCES facilities(id)
);
CREATE TABLE complaints (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  facility_id INTEGER NOT NULL,
  description TEXT NOT NULL,
  status TEXT DEFAULT 'Open',
  FOREIGN KEY(facility_id) REFERENCES facilities(id)
);

INSERT INTO departments(name) VALUES ('Engineering'),('HR'),('Operations');
INSERT INTO employees(department_id,name,email,salary) VALUES
 (1,'Asha Patil','asha@example.com',65000),
 (2,'Ravi Shah','ravi@example.com',48000),
 (1,'Neha Joshi','neha@example.com',58000);
INSERT INTO facilities(name,location,cleanliness_score,water_availability) VALUES
 ('Central Washroom','Nagpur Central',5.5,1),
 ('Cafeteria','Dharampeth',8.2,1),
 ('Library Restroom','Sitabuldi',6.8,0);
INSERT INTO inspections(facility_id,inspection_date,cleanliness_score,odor_score,waste_level,status,remarks) VALUES
 (1,'2026-09-20',5,7,6,'Needs Attention','Cleaning needed'),
 (2,'2026-09-20',8,2,2,'Good','Maintained'),
 (3,'2026-09-21',6,4,5,'Needs Attention','Monitor odor');
INSERT INTO complaints(facility_id,description,status) VALUES
 (1,'Bad odor reported','Open'),
 (1,'Waste bin is full','In Progress'),
 (3,'Water not available','Open');
""")

queries = [
    ("Employees per department",
     "SELECT d.name, e.name, e.salary FROM departments d JOIN employees e ON e.department_id=d.id ORDER BY d.name"),
    ("Average salary", "SELECT AVG(salary) FROM employees"),
    ("Highest paid", "SELECT name, salary FROM employees WHERE salary=(SELECT MAX(salary) FROM employees)"),
    ("Needs attention",
     "SELECT f.name, f.location, i.status FROM facilities f JOIN inspections i ON i.facility_id=f.id WHERE i.status='Needs Attention'"),
    ("Complaint counts",
     "SELECT f.name, COUNT(c.id) FROM facilities f LEFT JOIN complaints c ON c.facility_id=f.id GROUP BY f.id"),
    ("Inspection history",
     "SELECT f.name, i.inspection_date, i.status, i.cleanliness_score FROM facilities f JOIN inspections i ON i.facility_id=f.id ORDER BY f.name"),
]

for title, sql in queries:
    print(f"\n=== {title} ===")
    for row in c.execute(sql):
        print(row)

conn.close()
print("\nDay 8 SQL demo completed (in-memory SQLite).")
