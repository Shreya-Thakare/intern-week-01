"""Day 2 - Classes, Objects, Inheritance & Encapsulation"""

class Person:
    """Base class with encapsulation."""
    def __init__(self, name: str, age: int):
        self._name = name          # protected
        self.__age = age           # private

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        if 0 <= age <= 150:
            self.__age = age
        else:
            raise ValueError("Invalid age")

    def introduce(self) -> str:
        return f"I am {self._name}, {self.__age} years old."


class Student(Person):
    """Inheritance example."""
    def __init__(self, name: str, age: int, student_id: int, marks: list):
        super().__init__(name, age)
        self.student_id = student_id
        self.marks = marks

    def average(self) -> float:
        return sum(self.marks) / len(self.marks) if self.marks else 0.0

    def introduce(self) -> str:  # method overriding
        base = super().introduce()
        return f"{base} My ID is {self.student_id} and avg is {self.average():.1f}."


# Demo
s1 = Student("Alice", 20, 101, [85, 90, 78])
print(s1.introduce())
print("Age (via getter):", s1.get_age())
s1.set_age(21)
print("Updated:", s1.introduce())
