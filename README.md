# PLP-PYTHON-DISCOUNT-CALCULATION-FUNCTION
This Python script defines and uses a function to calculate the final price of an item after applying a discount of 20% or more, otherwise returning the original price.

# PLP Python Discount Calculation Function

This is a basic Python program that calculates the final price of an item after applying a discount. The discount is only applied if it is **20% or more**; otherwise, the original price is returned.

## Features

* Defines a reusable function to calculate discounted prices.
* Applies discount only if it is **20% or higher**.
* Demonstrates usage with both fixed and user-provided input values.

## How It Works

1. The program starts by printing a header.
2. It defines a function:
   `calculate_discount(price, discount_percent)`

   * If `discount_percent` is 20 or higher, it calculates the discounted price.
   * Otherwise, it returns the original price.
3. It shows:

   * A hardcoded example (`$200` price with `80%` discount).
   * A user input example, where the user enters a price and a discount percentage.

## Example Output

```
PLP PYTHON DISCOUNT CALCULATION FUNCTION

_____Price requiring no user inputs_____

The price of the item is: USD 160.0

_____Price requiring user inputs_____
Enter the price: 100
Enter the discount_percentage: 10

The price of the item is: USD 100.0
```

## Requirements

* Python 3.x

## How to Run

Save the code in a `.py` file (e.g., `discount_calculator.py`) and run it using:

```bash
python discount_calculator.py
```

---

Let me know if you want to include screenshots or a flowchart for visual learners.
