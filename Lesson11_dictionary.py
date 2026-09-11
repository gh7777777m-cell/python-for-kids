# Lesson 11: Dictionary
# Author: Marjan Gholizadeh

# Create a Dictionary
student = {
    "name": "Sara",
    "age": 12,
    "grade": 7
}

print(student)
# Output:
# {'name': 'Sara', 'age': 12, 'grade': 7}


# Access values
print(student["name"])
# Output: Sara

print(student["age"])
# Output: 12

print(student["grade"])
# Output: 7


# Add a new item
student["city"] = "Karaj"

print(student)
# Output:
# {'name': 'Sara', 'age': 12, 'grade': 7, 'city': 'Karaj'}


# Change a value
student["age"] = 13

print(student)
# Output:
# {'name': 'Sara', 'age': 13, 'grade': 7, 'city': 'Karaj'}


# Remove an item
student.pop("city")

print(student)
# Output:
# {'name': 'Sara', 'age': 13, 'grade': 7}


# Loop through Dictionary
for key, value in student.items():
    print(key, ":", value)

# Output:
# name : Sara
# age : 13
# grade : 7
