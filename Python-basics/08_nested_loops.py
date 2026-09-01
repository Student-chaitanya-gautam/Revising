# Nested Loops in Python
"""
Nested loops are loops inside another loop.

The outer loop usually controls the rows,
while the inner loop performs repeated work
for each row.
"""


# =========================
# Example 1: Basic Nested Loop
# =========================

print("Basic Nested Loop:")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
    print()


# =========================
# Example 2: Rectangle Pattern
# =========================

print("Rectangle Pattern:")

for i in range(1, 4):
    for j in range(1, 5):
        print("*", end=" ")
    print()


# =========================
# Example 3: Increasing Star Pattern
# =========================

print("\nIncreasing Star Pattern:")

for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end="")
    print()


# =========================
# Example 4: Decreasing Star Pattern
# =========================

print("\nDecreasing Star Pattern:")

for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()


# =========================
# Example 5: Number Triangle
# =========================

print("\nNumber Triangle:")

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# =========================
# Example 6: Multiplication Pattern
# =========================

print("\nMultiplication Pattern:")

for i in range(1, 5):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()


# =========================
# Example 7: Multiplication Table
# =========================

print("\nMultiplication Tables:")

for i in range(2, 5):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()


# =========================
# Example 8: Nested Loop + Condition
# Print Even Numbers
# =========================

print("\nEven Numbers in Each Row:")

for i in range(1, 4):
    for j in range(1, 5):
        if j % 2 == 0:
            print(j, end=" ")
    print()


# =========================
# Example 9: Main Diagonal
# =========================

print("\nMain Diagonal:")

for i in range(1, 5):
    for j in range(1, 5):
        if i == j:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()


# =========================
# Example 10: Opposite Diagonal
# =========================

print("\nOpposite Diagonal:")

for i in range(1, 5):
    for j in range(1, 5):
        if i + j == 5:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()


# =========================
# Example 11: Checkerboard Pattern
# =========================

print("\nCheckerboard Pattern:")

for i in range(1, 6):
    for j in range(1, 6):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()


# =========================
# Example 12: Centered Pyramid
# =========================

print("\nCentered Pyramid:")

for i in range(1, 5):

    # Print spaces
    for j in range(4 - i):
        print(" ", end="")

    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()


# =========================
# Example 13: Full Increasing
# and Decreasing Pattern
# =========================

print("\nIncreasing and Decreasing Pattern:")

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()

for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()


print("\nNested loop practice completed!")