# user_defined_functions.py
# Demonstrates writing and using user-defined functions


# 1. Function to add two numbers
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


# 2. Function to find the area of a rectangle
def rectangle_area(length, width):
    """Returns the area of a rectangle given its length and width."""
    return length * width


# 3. Function to determine whether a number is prime
def is_prime(n):
    """Returns True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


# 4. Function to find the factorial of a number
def factorial(n):
    """Returns the factorial of a non-negative integer n (n!)."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 5. Function to display a student's details
def display_student(name, admission_number, course):
    """Prints a student's details in a readable format."""
    print(f"Name: {name}")
    print(f"Admission Number: {admission_number}")
    print(f"Course: {course}")


# --- Testing the functions ---
print("--- Add Numbers ---")
print("5 + 8 =", add_numbers(5, 8))

print("\n--- Rectangle Area ---")
print("Area of a 6 x 4 rectangle:", rectangle_area(6, 4))

print("\n--- Prime Check ---")
for number in [2, 4, 7, 15, 17]:
    print(f"Is {number} prime? {is_prime(number)}")

print("\n--- Factorial ---")
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))

print("\n--- Student Details ---")
display_student("Mark Otieno", "CS/1234/2023", "Computer Science")
