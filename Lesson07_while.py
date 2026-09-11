# Lesson 07: While Loop in Python
# Author: Marjan Gholizadeh

# Example 1: Counting from 1 to 5
number = 1

while number <= 5:
    print(number)
    number += 1


# Example 2: Counting backwards
number = 5

while number >= 1:
    print(number)
    number -= 1


# Example 3: Even numbers from 1 to 10
number = 2

while number <= 10:
    print(number)
    number += 2


# Example 4: Sum of numbers from 1 to 10
number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print("Sum:", total)


# Example 5: Multiplication table
number = 1

while number <= 10:
    print(5, "x", number, "=", 5 * number)
    number += 1
