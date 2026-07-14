# builtin_functions.py
# Demonstrates the use of at least 10 Python built-in functions

numbers = [12, 4, 56, 23, 8, 45]
text = "Cooperative University"

# 1. len() - returns the number of items in an object
print("len(numbers):", len(numbers))

# 2. max() - returns the largest item
print("max(numbers):", max(numbers))

# 3. min() - returns the smallest item
print("min(numbers):", min(numbers))

# 4. sum() - adds up all items in an iterable
print("sum(numbers):", sum(numbers))

# 5. type() - returns the data type of an object
print("type(numbers):", type(numbers))

# 6. sorted() - returns a new sorted list from the items in an iterable
print("sorted(numbers):", sorted(numbers))
print("sorted(numbers, reverse=True):", sorted(numbers, reverse=True))

# 7. abs() - returns the absolute (positive) value of a number
print("abs(-15):", abs(-15))

# 8. round() - rounds a number to a given number of decimal places
print("round(3.14159, 2):", round(3.14159, 2))

# 9. input() - reads text input from the user (returns a string)
user_name = input("Enter your name: ")
print("You entered:", user_name)

# 10. print() - displays output to the console (used throughout this file)
print("This line was displayed using print().")

# Bonus built-in functions
# 11. str() - converts a value to a string
print("str(100):", str(100), type(str(100)))

# 12. int() - converts a value to an integer
print("int('25'):", int("25"))

# 13. list() - converts an iterable (e.g. a string) into a list
print("list(text):", list(text))
