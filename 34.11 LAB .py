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
# No discount for fewer than 10 items (no else needed as price stays the same)

# Print the result in required format: "item_purchased $total_purchase_cost"
# The :.2f ensures the price is formatted to exactly 2 decimal places
print(f"{store_item} ${total_price:.2f}")