"""Day 2 - Syntax, Variables & Data Types"""

# Variables (dynamic typing)
name = "Alice"
age = 21
height = 5.6
is_student = True
complex_num = 3 + 4j

print(f"Name: {name} (type: {type(name)})")
print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} (type: {type(height)})")
print(f"Is Student: {is_student} (type: {type(is_student)})")
print(f"Complex: {complex_num} (type: {type(complex_num)})")

# Multiple assignment
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# Type conversion
num_str = "100"
num_int = int(num_str)
print(f"Converted: {num_int + 50}")

# Constants (convention)
PI = 3.14159
print(f"PI ≈ {PI}")
