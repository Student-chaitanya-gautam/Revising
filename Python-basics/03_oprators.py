# Operators in Python
# Arithmetic, Comparison, and Logical Operators


# =========================
# Arithmetic Operators
# =========================

first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))

print("Arithmetic Operators")

print(f"Addition: {first_number + second_number}")
print(f"Subtraction: {first_number - second_number}")
print(f"Multiplication: {first_number * second_number}")
print(f"Division: {first_number / second_number}")
print(f"Modulus (Remainder): {first_number % second_number}")
print(f"Exponentiation: {first_number ** second_number}")
print(f"Floor Division: {first_number // second_number}")


# =========================
# Comparison Operators
# =========================

print("\nComparison Operators")

x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))

print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} >= {y}: {x >= y}")
print(f"{x} <= {y}: {x <= y}")


# =========================
# Logical Operators
# =========================

print("\nLogical Operators")

age = int(input("Enter your age: "))
study_hours = int(input("Enter your daily study hours: "))

print(f"Age >= 18 and Study hours >= 3: {age >= 18 and study_hours >= 3}")
print(f"Age >= 18 or Study hours >= 6: {age >= 18 or study_hours >= 6}")
print(f"Not (Age < 18): {not (age < 18)}")

