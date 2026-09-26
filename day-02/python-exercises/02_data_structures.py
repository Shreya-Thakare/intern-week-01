"""Day 2 - Lists, Tuples, Sets, Dictionaries"""

# List (mutable, ordered)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits[1] = "blueberry"
print("List:", fruits)
print("Sliced:", fruits[1:3])

# Tuple (immutable, ordered)
coordinates = (10.5, 20.3)
print("Tuple:", coordinates)
# coordinates[0] = 1  # would raise TypeError

# Set (unordered, unique)
numbers = {1, 2, 2, 3, 4, 4}
numbers.add(5)
print("Set:", numbers)
print("Union:", numbers | {4, 5, 6})

# Dictionary (key-value)
student = {
    "id": 101,
    "name": "Bob",
    "marks": [85, 90, 78]
}
student["grade"] = "A"
print("Dict:", student)
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

# Nested
classroom = {
    "A": [{"name": "Alice", "score": 92}, {"name": "Bob", "score": 85}],
    "B": [{"name": "Charlie", "score": 78}]
}
print("Nested access:", classroom["A"][0]["name"])
