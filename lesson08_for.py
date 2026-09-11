# Lesson 08: For Loop in Python
# Author: Marjan Gholizadeh

# Example 1: Print numbers from 1 to 5
for number in range(1, 6):
    print(number)


# Example 2: Print even numbers
for number in range(2, 11, 2):
    print(number)


# Example 3: Print odd numbers
for number in range(1, 11, 2):
    print(number)


# Example 4: Calculate the sum of numbers
total = 0

for number in range(1, 11):
    total += number

print("Sum:", total)


# Example 5: Multiplication table
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# Example 6: Loop through a list
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
