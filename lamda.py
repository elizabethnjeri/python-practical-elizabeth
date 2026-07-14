# lambda_functions.py
# Demonstrates lambda (anonymous) functions in Python

# 1. Lambda function to add two numbers
add = lambda x, y: x + y
print("Add (3, 4):", add(3, 4))

# 2. Lambda function to multiply two numbers
multiply = lambda x, y: x * y
print("Multiply (3, 4):", multiply(3, 4))

# 3. Using a lambda function to sort a list of tuples by a specific key
students = [("John", 85), ("Alice", 92), ("Peter", 78)]

# Sort by score (the second item in each tuple)
sorted_students = sorted(students, key=lambda student: student[1])
print("\nStudents sorted by score (ascending):")
print(sorted_students)

# Sort by score in descending order
sorted_students_desc = sorted(students, key=lambda student: student[1], reverse=True)
print("Students sorted by score (descending):")
print(sorted_students_desc)

# 4. Using filter() with a lambda function
numbers = [10, 15, 22, 33, 40, 55, 68]

# Filter out only even numbers
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("\nEven numbers from the list:", even_numbers)

# 5. Using map() with a lambda function
# Square every number in the list
squared_numbers = list(map(lambda n: n ** 2, numbers))
print("Squared numbers:", squared_numbers)
