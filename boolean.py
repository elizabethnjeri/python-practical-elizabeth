# boolean.py
# Demonstrates the Boolean data type and comparison operators

# Creating boolean variables
is_student = True
is_working = False

print("is_student =", is_student)
print("is_working =", is_working)
print("Type of is_student:", type(is_student))

# Comparison operators return boolean values
x = 10
y = 20

print("\n--- Comparison Operators ---")
print("x == y:", x == y)   # Equal to
print("x != y:", x != y)   # Not equal to
print("x > y:", x > y)     # Greater than
print("x < y:", x < y)     # Less than
print("x >= y:", x >= y)   # Greater than or equal to
print("x <= y:", x <= y)   # Less than or equal to

# Boolean values resulting from a real comparison
age = 18
can_vote = age >= 18
print("\nCan vote (age >= 18)?", can_vote)
