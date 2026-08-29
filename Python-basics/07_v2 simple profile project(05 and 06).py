# Personal Profile Generator - Version 2
# Revision Project:
# Variables + Input/Output + Type Conversion + Operators
# Conditions + Loops


# =========================
# Getting User Information
# =========================

name = input("Enter your name: ")

# Keep asking until a valid age is entered
while True:
    age = int(input("Enter your age: "))

    if age > 0:
        break

    print("Invalid age. Please enter a positive number.")


height_cm = float(input("Enter your height in cm: "))

programming_language = input(~
    "Enter your favorite programming language: "
)

# Keep asking until a valid study time is entered
while True:
    study_hours = float(input("How many hours do you study per day? "))

    if study_hours >= 0:
        break

    print("Study hours cannot be negative. Please try again.")


# =========================
# Calculations
# =========================

age_after_5_years = age + 5
weekly_study_hours = study_hours * 7
height_meters = height_cm / 100


# =========================
# Study Performance
# =========================

if study_hours >= 5:
    study_status = "Excellent study routine"
elif study_hours >= 3:
    study_status = "Good study routine"
elif study_hours >= 1:
    study_status = "You can improve your study routine"
else:
    study_status = "You should start studying regularly"


# =========================
# Profile Card
# =========================

print("\n" + "=" * 40)
print("          PERSONAL PROFILE")
print("=" * 40)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Age after 5 years: {age_after_5_years}")
print(f"Height: {height_meters:.2f} m")
print(f"Favorite language: {programming_language}")

print("\nStudy Information")
print("-" * 40)

print(f"Daily study: {study_hours} hours")
print(f"Weekly study: {weekly_study_hours} hours")
print(f"Study status: {study_status}")

print("=" * 40)


# =========================
# Study Hours Summary
# =========================

print("\nStudy Hours for Each Day:")

for day in range(1, 8):
    print(f"Day {day}: {study_hours} hours")
print(f"\nTotal study hours in a week: {weekly_study_hours} hours")


print("\nProfile generated successfully!")