# looping.py
# Demonstrates for loops and while loops

# --- 1. For loop: print numbers from 1 to 20 ---
print("--- Numbers from 1 to 20 ---")
for i in range(1, 21):
    print(i, end=" ")
print()  # Move to a new line after the loop

# --- 2. For loop: multiplication table of a user-entered number ---
print("\n--- Multiplication Table ---")
number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# --- 3. While loop: sum of numbers from 1 to 100 ---
print("\n--- Sum of numbers from 1 to 100 ---")
total = 0
count = 1
while count <= 100:
    total += count  # Add current count to the running total
    count += 1      # Move to the next number
print("Sum of numbers from 1 to 100 is:", total)

# --- 4. Print only the even numbers between 1 and 50 ---
print("\n--- Even numbers between 1 and 50 ---")
for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=" ")
print()
