"""
Employee Management CLI
--------------------------
Entry point for the console application. Presents a menu, reads user
input, and delegates all real work to EmployeeManager.

Run with:  python main.py
"""

from manager import EmployeeManager

MENU = """
==================== Employee Management ====================
1. Add employee
2. Update employee
3. Delete employee
4. Search employee
5. List all employees
6. Show highest paid employee
7. Show average salary
8. Filter by department
9. Exit
================================================================
"""


def prompt_float(label: str) -> float:
    while True:
        raw = input(label).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def prompt_int(label: str) -> int:
    while True:
        raw = input(label).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid whole number.")


def add_employee(manager: EmployeeManager) -> None:
    name = input("Name: ")
    department = input("Department: ")
    salary = prompt_float("Salary: ")
    email = input("Email (optional): ")
    try:
        employee = manager.add_employee(name, department, salary, email)
        print(f"Added: {employee}")
    except ValueError as e:
        print(f"Error: {e}")


def update_employee(manager: EmployeeManager) -> None:
    emp_id = prompt_int("Employee ID to update: ")
    print("Leave a field blank to keep its current value.")
    name = input("New name: ")
    department = input("New department: ")
    salary_raw = input("New salary: ").strip()
    email = input("New email: ")

    try:
        salary = float(salary_raw) if salary_raw else None
        employee = manager.update_employee(
            emp_id, name=name, department=department, salary=salary, email=email
        )
        print(f"Updated: {employee}")
    except ValueError as e:
        print(f"Error: {e}")


def delete_employee(manager: EmployeeManager) -> None:
    emp_id = prompt_int("Employee ID to delete: ")
    if manager.delete_employee(emp_id):
        print(f"Employee {emp_id} deleted.")
    else:
        print(f"No employee found with id {emp_id}.")


def search_employee(manager: EmployeeManager) -> None:
    keyword = input("Search by name, department, or ID: ")
    results = manager.search_employees(keyword)
    if not results:
        print("No matching employees found.")
        return
    for e in results:
        print(e)


def list_employees(manager: EmployeeManager) -> None:
    employees = manager.list_employees()
    if not employees:
        print("No employees on record.")
        return
    for e in employees:
        print(e)


def show_highest_salary(manager: EmployeeManager) -> None:
    employee = manager.highest_salary()
    if employee is None:
        print("No employees on record.")
        return
    print(f"Highest paid employee: {employee}")


def show_average_salary(manager: EmployeeManager) -> None:
    avg = manager.average_salary()
    print(f"Average salary: {avg:,.2f}")


def filter_by_department(manager: EmployeeManager) -> None:
    department = input("Department to filter by: ")
    results = manager.filter_by_department(department)
    if not results:
        print(f"No employees found in department '{department}'.")
        return
    for e in results:
        print(e)


ACTIONS = {
    "1": add_employee,
    "2": update_employee,
    "3": delete_employee,
    "4": search_employee,
    "5": list_employees,
    "6": show_highest_salary,
    "7": show_average_salary,
    "8": filter_by_department,
}


def main() -> None:
    manager = EmployeeManager()

    while True:
        print(MENU)
        choice = input("Choose an option (1-9): ").strip()

        if choice == "9":
            print("Goodbye!")
            break

        action = ACTIONS.get(choice)
        if action is None:
            print("Invalid option, please try again.")
            continue

        action(manager)


if __name__ == "__main__":
    main()
