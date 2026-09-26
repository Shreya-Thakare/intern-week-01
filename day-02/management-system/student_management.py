"""
Student Management System
Features: Add, Update, Delete, Search, Filter, Sort, Statistics
Storage: JSON  |  Exception Handling included
"""

import json
from pathlib import Path
from typing import List, Dict, Optional
from statistics import mean, median
from collections import Counter

DATA_FILE = Path(__file__).parent / "students.json"


class StudentManager:
    def __init__(self, filepath: Path = DATA_FILE):
        self.filepath = filepath
        self.students: List[Dict] = []
        self.load()

    def load(self):
        try:
            if self.filepath.exists():
                with open(self.filepath, "r", encoding="utf-8") as f:
                    self.students = json.load(f)
            else:
                self.students = []
                self.save()
        except (json.JSONDecodeError, OSError) as e:
            print(f"[Error] Could not load data: {e}")
            self.students = []

    def save(self):
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.students, f, indent=2)
        except OSError as e:
            print(f"[Error] Could not save data: {e}")

    def _next_id(self) -> int:
        if not self.students:
            return 1
        return max(s["id"] for s in self.students) + 1

    def add(self, name: str, age: int, department: str, marks: float) -> bool:
        try:
            if not name.strip():
                raise ValueError("Name cannot be empty")
            if age < 15 or age > 100:
                raise ValueError("Age must be between 15 and 100")
            if marks < 0 or marks > 100:
                raise ValueError("Marks must be between 0 and 100")

            student = {
                "id": self._next_id(),
                "name": name.strip().title(),
                "age": age,
                "department": department.strip().title(),
                "marks": float(marks)
            }
            self.students.append(student)
            self.save()
            print(f"[Success] Added student ID {student['id']}")
            return True
        except ValueError as e:
            print(f"[Validation Error] {e}")
            return False

    def update(self, student_id: int, **kwargs) -> bool:
        for s in self.students:
            if s["id"] == student_id:
                try:
                    if "name" in kwargs and kwargs["name"]:
                        s["name"] = kwargs["name"].strip().title()
                    if "age" in kwargs:
                        age = int(kwargs["age"])
                        if not (15 <= age <= 100):
                            raise ValueError("Invalid age")
                        s["age"] = age
                    if "department" in kwargs and kwargs["department"]:
                        s["department"] = kwargs["department"].strip().title()
                    if "marks" in kwargs:
                        marks = float(kwargs["marks"])
                        if not (0 <= marks <= 100):
                            raise ValueError("Invalid marks")
                        s["marks"] = marks
                    self.save()
                    print(f"[Success] Updated student ID {student_id}")
                    return True
                except (ValueError, TypeError) as e:
                    print(f"[Error] {e}")
                    return False
        print(f"[Error] Student ID {student_id} not found")
        return False

    def delete(self, student_id: int) -> bool:
        for i, s in enumerate(self.students):
            if s["id"] == student_id:
                removed = self.students.pop(i)
                self.save()
                print(f"[Success] Deleted {removed['name']} (ID {student_id})")
                return True
        print(f"[Error] Student ID {student_id} not found")
        return False

    def search(self, keyword: str) -> List[Dict]:
        keyword = keyword.lower()
        results = [
            s for s in self.students
            if keyword in s["name"].lower()
            or keyword in s["department"].lower()
            or keyword == str(s["id"])
        ]
        return results

    def filter_by(self, department: Optional[str] = None,
                  min_marks: Optional[float] = None,
                  max_marks: Optional[float] = None) -> List[Dict]:
        result = self.students[:]
        if department:
            result = [s for s in result if s["department"].lower() == department.lower()]
        if min_marks is not None:
            result = [s for s in result if s["marks"] >= min_marks]
        if max_marks is not None:
            result = [s for s in result if s["marks"] <= max_marks]
        return result

    def sort_by(self, key: str = "name", reverse: bool = False) -> List[Dict]:
        valid_keys = {"id", "name", "age", "department", "marks"}
        if key not in valid_keys:
            print(f"[Error] Invalid sort key. Use one of {valid_keys}")
            return self.students[:]
        return sorted(self.students, key=lambda s: s[key], reverse=reverse)

    def statistics(self) -> None:
        if not self.students:
            print("No data available for statistics.")
            return

        marks = [s["marks"] for s in self.students]
        ages = [s["age"] for s in self.students]
        depts = [s["department"] for s in self.students]

        print("\n========== STATISTICS ==========")
        print(f"Total Students     : {len(self.students)}")
        print(f"Average Marks      : {mean(marks):.2f}")
        print(f"Median Marks       : {median(marks):.2f}")
        print(f"Highest Marks      : {max(marks):.2f}")
        print(f"Lowest Marks       : {min(marks):.2f}")
        print(f"Average Age        : {mean(ages):.1f}")
        print("\nDepartment-wise count:")
        for dept, count in Counter(depts).most_common():
            dept_marks = [s["marks"] for s in self.students if s["department"] == dept]
            print(f"  {dept:15} : {count:3} students | Avg marks: {mean(dept_marks):.2f}")
        print("================================\n")

    def display(self, students: Optional[List[Dict]] = None) -> None:
        data = students if students is not None else self.students
        if not data:
            print("No records found.")
            return
        print(f"\n{'ID':<5} {'Name':<20} {'Age':<5} {'Department':<15} {'Marks':<6}")
        print("-" * 55)
        for s in data:
            print(f"{s['id']:<5} {s['name']:<20} {s['age']:<5} {s['department']:<15} {s['marks']:<6.1f}")
        print()


def menu():
    manager = StudentManager()

    while True:
        print("""
========= Student Management System =========
1. Add Student
2. Update Student
3. Delete Student
4. Search
5. Filter
6. Sort & Display
7. Statistics
8. Display All
0. Exit
=============================================
""")
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                name = input("Name: ")
                age = int(input("Age: "))
                dept = input("Department: ")
                marks = float(input("Marks: "))
                manager.add(name, age, dept, marks)

            elif choice == "2":
                sid = int(input("Student ID to update: "))
                print("Leave blank to keep current value")
                name = input("New Name: ").strip() or None
                age = input("New Age: ").strip() or None
                dept = input("New Department: ").strip() or None
                marks = input("New Marks: ").strip() or None
                kwargs = {}
                if name: kwargs["name"] = name
                if age: kwargs["age"] = age
                if dept: kwargs["department"] = dept
                if marks: kwargs["marks"] = marks
                manager.update(sid, **kwargs)

            elif choice == "3":
                sid = int(input("Student ID to delete: "))
                manager.delete(sid)

            elif choice == "4":
                kw = input("Search keyword (name/dept/id): ")
                results = manager.search(kw)
                manager.display(results)

            elif choice == "5":
                dept = input("Department (blank=any): ").strip() or None
                min_m = input("Min marks (blank=any): ").strip()
                max_m = input("Max marks (blank=any): ").strip()
                min_marks = float(min_m) if min_m else None
                max_marks = float(max_m) if max_m else None
                results = manager.filter_by(dept, min_marks, max_marks)
                manager.display(results)

            elif choice == "6":
                key = input("Sort by (id/name/age/department/marks): ").strip() or "name"
                order = input("Descending? (y/n): ").strip().lower() == "y"
                sorted_list = manager.sort_by(key, reverse=order)
                manager.display(sorted_list)

            elif choice == "7":
                manager.statistics()

            elif choice == "8":
                manager.display()

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("[Error] Please enter valid numeric values where required.")
        except Exception as e:
            print(f"[Unexpected Error] {e}")


if __name__ == "__main__":
    menu()
