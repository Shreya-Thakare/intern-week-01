"""Day 2 - Conditions & Loops"""

# if-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"
print(f"Score {score} → Grade {grade}")

# for loop
print("\nFor loop over list:")
for fruit in ["apple", "banana", "cherry"]:
    print(f"  - {fruit}")

# range
print("\nRange 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# while loop
print("\nWhile loop (countdown):")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")

# break & continue
print("\nBreak/Continue demo:")
for i in range(1, 10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i, end=" ")
print()

# Nested loop (simple pattern)
print("\nPattern:")
for i in range(1, 5):
    print("*" * i)
