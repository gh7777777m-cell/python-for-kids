# Lesson 09: Lists in Python
# Author: Marjan Gholizadeh

# Example 1: Create a list
fruits = ["apple", "banana", "orange"]

print(fruits)


# Example 2: Access list items
print(fruits[0])
print(fruits[1])


# Example 3: Add an item
fruits.append("mango")

print(fruits)


# Example 4: Remove an item
fruits.remove("banana")

print(fruits)


# Example 5: Change an item
fruits[0] = "watermelon"

print(fruits)


# Example 6: Find the length of a list
print("Number of fruits:", len(fruits))


# Example 7: Loop through a list
for fruit in fruits:
    print(fruit)


# Example 8: Numbers in a list
numbers = [10, 20, 30, 40, 50]

print("First number:", numbers[0])
print("Last number:", numbers[-1])

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
