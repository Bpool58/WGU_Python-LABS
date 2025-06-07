"""
Task:
Create a solution that accepts a string input representing a grocery store item
 and an integer input identifying the number of items purchased on a recent visit.
  The following dictionary purchase lists available items as the key with the cost per item as the value.

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

Additionally, If fewer than ten items are purchased, the price is the full cost per item.
If between ten and twenty items (inclusive) are purchased, the purchase gets a 5% discount.
If twenty-one or more items are purchased, the purchase gets a 10% discount.
Output the chosen item and total cost of the purchase to two decimal places..

The solution output should be in the format
"""

# Get the item name from user input
store_item = input()
# Get the quantity and convert it to integer
Num_of_items = int(input())

# Dictionary of items with their prices
purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

# Calculate initial total price (price per item * quantity)
total_price = purchase[store_item] * Num_of_items

# Apply discounts based on quantity purchased:
# 10% discount for 21 or more items
if Num_of_items >= 21:
    total_price = total_price * 0.90
# 5% discount for 10-20 items (inclusive)
elif Num_of_items >= 10:
    total_price = total_price * 0.95
f
# No discount for fewer than 10 items (no else needed as price stays the same)

# Print the result in required format: "item_purchased $total_purchase_cost"
# The :.2f ensures the price is formatted to exactly 2 decimal places
print(f"{store_item} ${total_price:.2f}")