# selection.py
# Demonstrates if, if...else, and if...elif...else selection structures

# --- Example 1: Simple if statement ---
print("--- Simple if statement ---")
temperature = 30
if temperature > 25:
    print("It is a hot day.")

# --- Example 2: if...else statement ---
print("\n--- if...else statement ---")
number = 7
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

# --- Example 3: if...elif...else statement - Pass/Fail based on score ---
print("\n--- Pass/Fail based on score ---")
score = 65

if score >= 50:
    print(f"Score: {score} -> Result: PASS")
else:
    print(f"Score: {score} -> Result: FAIL")

# --- Example 4: Check whether a user-entered number is even or odd ---
print("\n--- Even or Odd Checker ---")
user_number = int(input("Enter a number to check if it is even or odd: "))
if user_number % 2 == 0:
    print(user_number, "is an EVEN number.")
else:
    print(user_number, "is an ODD number.")

# --- Example 5: Find the largest of three numbers using if...elif...else ---
print("\n--- Largest of Three Numbers ---")
num1 = 15
num2 = 42
num3 = 28

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"Among {num1}, {num2}, and {num3}, the largest number is: {largest}")
