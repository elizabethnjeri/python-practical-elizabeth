# list.py
# Demonstrates creating, modifying, and looping through a list

# Creating a list of fruits
fruits = ["apple", "banana", "mango", "orange"]
print("Original list:", fruits)

# Adding an item to the end of the list
fruits.append("pineapple")
print("\nAfter adding 'pineapple':", fruits)

# Inserting an item at a specific position
fruits.insert(1, "grape")
print("After inserting 'grape' at index 1:", fruits)

# Removing an item from the list
fruits.remove("banana")
print("\nAfter removing 'banana':", fruits)

# Updating (changing) an item in the list
fruits[0] = "watermelon"
print("After updating index 0 to 'watermelon':", fruits)

# Looping through the list and printing each item
print("\n--- Looping through the list ---")
for fruit in fruits:
    print(fruit)

# Extra: printing with index using enumerate
print("\n--- Looping with index ---")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
