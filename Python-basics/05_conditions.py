# Conditions in Python
'''if, elif, and else statements are used to control the flow of
a program based on certain conditions.'''


# =========================
# Example 1: Voting Eligibility
# =========================

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# =========================
# Example 2: Positive, Negative, or Zero
# =========================

number = float(input("\nEnter a number: "))
#I am using \n to add a new line before the input prompt for better readability
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# =========================
# Example 3: Simple Grade Checker
# =========================

marks = float(input("\nEnter your marks: "))

if marks > 100 or marks < 0:
    print("Invalid marks. Please enter a value between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Fail")