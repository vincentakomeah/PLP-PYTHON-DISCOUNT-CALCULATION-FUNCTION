print("PLP PYTHON DISCOUNT CALCULATION FUNCTION\n")
# Discount calculation function.
def calculate_discount(price, discount_percent):
    # If discount_percent >= 20, the calculation below is performed.
    # Else the price is maintained as it is.
    if discount_percent >= 20:
        final_price = discount_percent / 100 * price
    else:
        final_price = price
    return final_price

print("_____Price requiring no user inputs_____")
# the_price1 variable holds the function and it's arguments and prints the results.
the_price1 = calculate_discount(200, 80)
print(f"\nThe price of the item is: USD {the_price1}")

print("\n_____Price requiring user inputs_____")
# User enters the price.
original_price = float(input("Enter the price: "))

# User enters the discount_percent.
original_discount_percentage = float(input("Enter the discount_percentage: "))

# the_price2 variable holds the function and it's arguments and prints the results.
the_price2 = calculate_discount(original_price, original_discount_percentage)
print(f"\nThe price of the item is: USD {the_price2}")