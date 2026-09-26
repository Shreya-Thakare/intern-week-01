"""Day 2 - Functions, Lambda & List Comprehensions"""

# Regular function
def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting message."""
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# *args and **kwargs
def summary(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

summary(1, 2, 3, name="Alice", age=21)

# Lambda
square = lambda x: x ** 2
print("Square of 5:", square(5))

# List comprehensions
nums = list(range(1, 11))
evens = [n for n in nums if n % 2 == 0]
squares = [n ** 2 for n in nums]
print("Evens:", evens)
print("Squares:", squares)

# Dict comprehension
square_dict = {n: n ** 2 for n in range(1, 6)}
print("Square dict:", square_dict)

# map + lambda
doubled = list(map(lambda x: x * 2, nums))
print("Doubled:", doubled)
