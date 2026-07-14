# dictionary.py
# Demonstrates creating a dictionary and accessing/updating its values

# Creating a dictionary representing a student
student = {
    "name": "Mark Otieno",
    "age": 22,
    "course": "Computer Science",
    "grade": "A"
}

print("Student dictionary:", student)

# Accessing values using keys
print("\n--- Accessing values ---")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student.get("course"))

# Updating existing values
student["age"] = 23
student["grade"] = "A+"
print("\n--- After updating age and grade ---")
print(student)

# Adding a new key-value pair
student["year_of_study"] = 3
print("\n--- After adding 'year_of_study' ---")
print(student)

# Looping through keys and values
print("\n--- Looping through the dictionary ---")
for key, value in student.items():
    print(f"{key}: {value}")
