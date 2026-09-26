"""
EmployeeManager: holds the in-memory list of employees and implements
all the required operations (Add, Update, Delete, Search, List,
Highest Salary, Average Salary, Department Filter). It persists to
disk via storage.py after every change.
"""

from employee import Employee
from storage import load_employees, save_employees


class EmployeeManager:
    def __init__(self):
        self.employees: list[Employee] = load_employees()

    # -- internal helpers -------------------------------------------------

    def _next_id(self) -> int:
        if not self.employees:
            return 1
        return max(e.id for e in self.employees) + 1

    def _find_by_id(self, emp_id: int) -> Employee | None:
        for e in self.employees:
            if e.id == emp_id:
                return e
        return None

    def _persist(self) -> None:
        save_employees(self.employees)

    # -- required operations ----------------------------------------------

    def add_employee(self, name: str, department: str, salary: float, email: str = "") -> Employee:
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if salary < 0:
            raise ValueError("Salary cannot be negative")

        employee = Employee(
            id=self._next_id(),
            name=name.strip(),
            department=department.strip(),
            salary=salary,
            email=email.strip(),
        )
        self.employees.append(employee)
        self._persist()
        return employee

    def update_employee(self, emp_id: int, **fields) -> Employee:
        employee = self._find_by_id(emp_id)
        if employee is None:
            raise ValueError(f"No employee found with id {emp_id}")

        if "name" in fields and fields["name"]:
            employee.name = fields["name"].strip()
        if "department" in fields and fields["department"]:
            employee.department = fields["department"].strip()
        if "salary" in fields and fields["salary"] is not None:
            if fields["salary"] < 0:
                raise ValueError("Salary cannot be negative")
            employee.salary = fields["salary"]
        if "email" in fields and fields["email"] is not None:
            employee.email = fields["email"].strip()

        self._persist()
        return employee

    def delete_employee(self, emp_id: int) -> bool:
        employee = self._find_by_id(emp_id)
        if employee is None:
            return False
        self.employees.remove(employee)
        self._persist()
        return True

    def search_employees(self, keyword: str) -> list[Employee]:
        keyword = keyword.strip().lower()
        return [
            e for e in self.employees
            if keyword in e.name.lower()
            or keyword in e.department.lower()
            or keyword == str(e.id)
        ]

    def list_employees(self) -> list[Employee]:
        return sorted(self.employees, key=lambda e: e.id)

    def highest_salary(self) -> Employee | None:
        if not self.employees:
            return None
        return max(self.employees, key=lambda e: e.salary)

    def average_salary(self) -> float:
        if not self.employees:
            return 0.0
        return sum(e.salary for e in self.employees) / len(self.employees)

    def filter_by_department(self, department: str) -> list[Employee]:
        department = department.strip().lower()
        return [e for e in self.employees if e.department.lower() == department]
