# Loops in Python
'''Loops are used to execute a block of code repeatedly as 
long as a certain condition is met. Python provides two main types
of loops: while loops and for loops.'''


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
# range(start, stop, step), the step is 2 to get even numbers.
    print(number)

print("\nEven numbers from 2 to 20 using while loop:")

number = 2
while number <= 20:
    print(number)
    number += 2  # Increment by 2 to get even numbers


# =========================
# Example 4: Sum of 1 to 100
# =========================

print("\nSum of numbers from 1 to 100 using for loop:")

total = 0

for number in range(1, 101):
    total = total + number

print(f"\nSum of numbers from 1 to 100 using for loop: {total}")

print("\nSum of numbers from 1 to 100 using while loop:")

total = 0
number = 1

while number <= 100:
    total = total + number
    number += 1
    
print(f"Sum of numbers from 1 to 100 using while loop: {total}")

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





# =========================
#    practicing loops
# =========================


# =========================
#     Challenge 1
# =========================
print("\n" + "=" * 40)
print("          Challenge 1")
print("=" * 40)
#print (1 to 10 numbers)

print("\nUsing For loop: ")#solving using for loop

for i in range (1 , 11):
    print(i)

print("\nUsing While loop: ")#solving using while loop

number = 1
while number <= 10:
    print(number)
    number += 1

# =========================
#     Challenge 2
# =========================
print("\n" + "=" * 40)
print("          Challenge 2")
print("=" * 40)
# print only the odd numbers from 1 to 30:

print("\nUsing For loop: ")#solving using for loop

for i in range(1 , 31):
    if i % 2 != 0:
        print(i)

print("\nUsing While loop: ")#solving using while loop

i = 1
while i <= 30:
    
    print(i)
    i+=2

# =========================
#     Challenge 3
# =========================
print("\n" + "=" * 40)
print("          Challenge 3")
print("=" * 40)
#Ask the user foe a number and print its multiplications table

print("\nUsing For loop: ")#solving using for loop

number = int(input("\nChoice any table: "))

for i in range ( 1 , 11 ):
    print(f"{number} x {i} = {number*i}")

print("\nUsing While loop: ")#solving using while loop

number = int(input("\nChoice any table: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number*i}")
    i+=1
