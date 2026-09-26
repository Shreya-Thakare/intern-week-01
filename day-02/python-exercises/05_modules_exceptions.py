"""Day 2 - Modules, Packages & Exception Handling"""

import math
import datetime
from collections import Counter

print("Pi:", math.pi)
print("Today:", datetime.date.today())

# Exception handling
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid types for division!")
        return None
    else:
        print("Division successful")
        return result
    finally:
        print("Cleanup done")

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "2"))

# Custom exception
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(f"Age {age} is invalid")
    return age

try:
    set_age(-5)
except InvalidAgeError as e:
    print("Caught:", e)

# Counter example
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print("Word counts:", Counter(words))
