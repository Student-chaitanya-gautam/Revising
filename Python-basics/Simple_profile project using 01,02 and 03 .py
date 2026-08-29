# Personal Profile Generator
# Revision Project: Variables + Input/Output + Operators


# Getting user information

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_cm = float(input("Enter your height in cm: "))
programming_language = input("Enter your favorite programming language: ")
study_hours = float(input("How many hours do you study per day? "))


# Calculations

age_after_5_years = age + 5
weekly_study_hours = study_hours * 7
height_meters = height_cm / 100


# Comparison

study_target_reached = study_hours >= 3


# Profile Card

print("\n" + "=" * 35)
#we use \n to add a new line before the profile card.
#and we use "=" * 35 to create a line of 35 equal signs for formatting.
print("       PERSONAL PROFILE")
print("=" * 35)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Age after 5 years: {age_after_5_years}")
print(f"Height: {height_meters:.2f} m")
#we use :.2f to format the height to 2 decimal places.
print(f"favorite language: {programming_language}")

print(f"\nDaily study: {study_hours} hours")
print(f"Weekly study: {weekly_study_hours} hours")

print(f"Study target (3+ hours/day): {study_target_reached}")

print("=" * 35)

