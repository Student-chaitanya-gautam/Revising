# Loops in Python

"""
Loops are used to execute a block of code repeatedly
as long as a certain condition is met.

Python provides two main types of loops:
1. while loop
2. for loop
"""


# =========================
# Example 1: While Loop
# Print numbers from 1 to 10
# =========================

print("Numbers 1 to 10 using while loop:")

number = 1

while number <= 10:
    print(number)
    number = number + 1


# =========================
# Example 2: For Loop
# Print numbers from 1 to 10
# =========================

print("\nNumbers 1 to 10 using for loop:")

for number in range(1, 11):
    print(number)


# =========================
# Example 3: Even Numbers
# Print even numbers from 2 to 20
# =========================

print("\nEven numbers from 2 to 20 using for loop:")

for number in range(2, 21, 2):
    print(number)


print("\nEven numbers from 2 to 20 using while loop:")

number = 2

while number <= 20:
    print(number)
    number += 2


# =========================
# Example 4: Sum of 1 to 100
# =========================

print("\nSum of numbers from 1 to 100 using for loop:")

total = 0

for number in range(1, 101):
    total = total + number

print(f"Sum using for loop: {total}")


print("\nSum of numbers from 1 to 100 using while loop:")

total = 0
number = 1

while number <= 100:
    total = total + number
    number += 1

print(f"Sum using while loop: {total}")


# =========================
# Example 5: Break
# Stop the loop when number reaches 5
# =========================

print("\nBreak example:")

for number in range(1, 11):

    if number == 5:
        break

    print(number)


# =========================
# Example 6: Continue
# Skip the number 5
# =========================

print("\nContinue example:")

for number in range(1, 11):

    if number == 5:
        continue

    print(number)


# ==================================================
#                   PRACTICE
# ==================================================


# =========================
# Challenge 1
# Print numbers from 1 to 10
# =========================

print("\n" + "=" * 40)
print("          Challenge 1")
print("=" * 40)

print("\nUsing for loop:")

for i in range(1, 11):
    print(i)


print("\nUsing while loop:")

number = 1

while number <= 10:
    print(number)
    number += 1


# =========================
# Challenge 2
# Print odd numbers from 1 to 30
# =========================

print("\n" + "=" * 40)
print("          Challenge 2")
print("=" * 40)

print("\nUsing for loop:")

for i in range(1, 31):

    if i % 2 != 0:
        print(i)


print("\nUsing while loop:")

i = 1

while i <= 30:
    print(i)
    i += 2


# =========================
# Challenge 3
# Multiplication Table
# =========================

print("\n" + "=" * 40)
print("          Challenge 3")
print("=" * 40)

print("\nUsing for loop:")

number = int(input("Choose a table: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


print("\nUsing while loop:")

number = int(input("Choose a table: "))

i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1


# =========================
# Challenge 4
# Sum of numbers from 1 to 100
# =========================

print("\n" + "=" * 40)
print("          Challenge 4")
print("=" * 40)

total = 0

for number in range(1, 101):
    total += number

print(f"Sum from 1 to 100: {total}")


# =========================
# Challenge 5
# Count Digits
# =========================

print("\n" + "=" * 40)
print("          Challenge 5")
print("=" * 40)

number = int(input("\nEnter a number: "))

count = 0
temp = abs(number)

if temp == 0:
    count = 1
else:

    while temp > 0:
        temp = temp // 10
        count += 1

print(f"Number of digits: {count}")


# =========================
# Challenge 6
# Sum of Digits
# =========================

print("\n" + "=" * 40)
print("          Challenge 6")
print("=" * 40)

number = int(input("\nEnter a number: "))

total = 0
temp = abs(number)

while temp > 0:
    digit = temp % 10
    total += digit
    temp = temp // 10
    print(f"Sum of digits: {total}")


# =========================
# Challenge 7
# Reverse a Number
# =========================

print("\n" + "=" * 40)
print("          Challenge 7")
print("=" * 40)

number = int(input("\nEnter a number: "))

reverse = 0
temp = abs(number)

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if number < 0:
    reverse = -reverse

print(f"Reversed number: {reverse}")


# =========================
# Challenge 8
# Factorial
# =========================

print("\n" + "=" * 40)
print("          Challenge 8")
print("=" * 40)

number = int(input("\nEnter a non-negative number: "))

if number < 0:

    print("Factorial is not defined for negative numbers.")

else:

    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print(f"Factorial of {number}: {factorial}")


# =========================
# Challenge 9
# Skip Multiples of 3
# =========================

print("\n" + "=" * 40)
print("          Challenge 9")
print("=" * 40)

print("Numbers from 1 to 20 except multiples of 3:")

for number in range(1, 21):

    if number % 3 == 0:
        continue

    print(number, end=" ")

print()


# =========================
# Challenge 10
# Stop at 7
# =========================

print("\n" + "=" * 40)
print("          Challenge 10")
print("=" * 40)

print("Numbers before 7:")

for number in range(1, 11):

    if number == 7:
        break

    print(number, end=" ")

print()


# =========================
# Challenge 11
# Multiplication Tables
# =========================

print("\n" + "=" * 40)
print("          Challenge 11")
print("=" * 40)

for number in range(2, 6):

    print(f"\nTable of {number}:")

    for multiplier in range(1, 11):
        print(
            f"{number} x {multiplier} = "
            f"{number * multiplier}"
        )


# =========================
# Challenge 12
# Nested Loop Practice
# Print a 5 x 5 square
# =========================

print("\n" + "=" * 40)
print("          Challenge 12")
print("=" * 40)

for row in range(5):

    for column in range(5):
        print("*", end=" ")

    print()


# =========================
# Practice Completed
# =========================

print("\n" + "=" * 40)
print("       Loop Practice Completed")
print("=" * 40)