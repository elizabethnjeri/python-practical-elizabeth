# string.py
# Demonstrates string creation, concatenation, indexing, slicing, and methods

# Creating strings
first_name = "liz"
last_name = "njeri"

# Concatenation - joining strings together
full_name = first_name + " " + last_name
print("Full name (concatenation):", full_name)

# String indexing - accessing individual characters (index starts at 0)
message = "Python Programming"
print("\n--- Indexing ---")
print("First character:", message[0])
print("Last character:", message[-1])
print("Character at index 7:", message[7])

# String slicing - extracting a portion of a string [start:end]
print("\n--- Slicing ---")
print("First 6 characters:", message[0:6])
print("Characters from index 7 to end:", message[7:])
print("Last 11 characters:", message[-11:])

# String methods
print("\n--- String Methods ---")
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Replace 'Python' with 'Java':", message.replace("Python", "Java"))
print("Split into words:", message.split())
