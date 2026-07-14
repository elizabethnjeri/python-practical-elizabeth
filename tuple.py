# tuple.py
# Demonstrates creating a tuple, accessing elements, and tuple immutability

# Creating a tuple of coordinates
coordinates = (10, 20, 30)
print("Tuple:", coordinates)

# Accessing elements by index
print("\n--- Accessing elements ---")
print("First element:", coordinates[0])
print("Second element:", coordinates[1])
print("Last element:", coordinates[-1])

# Demonstrating that tuples cannot be modified
# Uncommenting the line below will raise a TypeError because tuples are immutable:
# coordinates[0] = 100
# TypeError: 'tuple' object does not support item assignment

print("\n--- Immutability ---")
try:
    coordinates[0] = 100
except TypeError as error:
    print("Error occurred:", error)
    print("Explanation: Tuples are immutable, meaning once created, their")
    print("elements cannot be changed, added, or removed. This is different")
    print("from lists, which are mutable and can be modified freely.")
