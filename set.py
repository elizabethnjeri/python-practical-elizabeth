# set.py
# Demonstrates creating a set, adding/removing elements, and automatic
# removal of duplicate values

# Creating a set
colors = {"red", "green", "blue"}
print("Original set:", colors)

# Adding an element to the set
colors.add("yellow")
print("\nAfter adding 'yellow':", colors)

# Removing an element from the set
colors.remove("green")
print("After removing 'green':", colors)

# Demonstrating that duplicates are automatically removed
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers_with_duplicates)

print("\n--- Duplicate Removal ---")
print("Original list (with duplicates):", numbers_with_duplicates)
print("Converted to set (duplicates removed):", unique_numbers)

# Trying to add a value that already exists has no effect
colors.add("red")  # "red" is already in the set
print("\nAfter trying to add 'red' again (already exists):", colors)
