"""
Employee model.

A plain data class representing one employee record, plus conversion
helpers to/from the dict shape we store in JSON.
"""

from dataclasses import dataclass, asdict


@dataclass
class Employee:
    id: int
    name: str
    department: str
    salary: float
    email: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Employee":
        return Employee(
            id=data["id"],
            name=data["name"],
            department=data["department"],
            salary=data["salary"],
            email=data.get("email", ""),
        )

    def __str__(self) -> str:
        return (
            f"[{self.id}] {self.name:<20} "
            f"Dept: {self.department:<15} "
            f"Salary: {self.salary:>10,.2f} "
            f"Email: {self.email}"
        )
