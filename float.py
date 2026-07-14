# float.py
# Demonstrates the float data type and calculations with decimal numbers

# Creating float variables
price = 12.5
quantity = 3.25

print("price =", price)
print("quantity =", quantity)
print("Type of price:", type(price))

# Calculations involving decimal numbers
total_cost = price * quantity
print("Total cost (price * quantity):", total_cost)

average = (price + quantity) / 2
print("Average of price and quantity:", average)

difference = price - quantity
print("Difference (price - quantity):", difference)

# Rounding a float to 2 decimal places
rounded_total = round(total_cost, 2)
print("Rounded total cost:", rounded_total)

# Converting an integer to a float
whole_number = 7
converted_float = float(whole_number)
print("Integer 7 converted to float:", converted_float)
