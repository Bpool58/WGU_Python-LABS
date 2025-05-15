# Define dictionary of stocks with their prices
# Key: Stock symbol (string)
# Value: Stock price (float)
stocks = {
    'TSLA': 912.86,  # Tesla stock
    'BBBY': 24.84,   # Bed Bath & Beyond stock
    'AAPL': 174.26,  # Apple stock
    'SOFI': 6.92,    # SoFi Technologies stock
    'KIRK': 8.72,    # Kirkland's stock
    'AURA': 22.12,   # Aura Biosciences stock
    'AMZN': 141.28,  # Amazon stock
    'EMBK': 12.29,   # Embark Technology stock
    'LVLU': 2.33     # Lulus Fashion stock
}

# Get the number of stock selections from user
# Convert input string to integer using int()
num_shares = int(input())

# Initialize variable to keep track of total cost
# Start with 0 since we haven't added any stocks yet
total_cost = 0

# Loop through to get each stock selection
# Range creates sequence from 0 to num_shares-1
# We use _ since we don't need the loop counter variable
for _ in range(num_shares):
    # Get stock symbol input from user
    stock_symbol = input()
    
    # Look up price in stocks dictionary using stock_symbol as key
    # Add the price to our running total
    # stocks[stock_symbol] gives us the price for that stock
    total_cost += stocks[stock_symbol]

# Print the final total cost
# f-string allows us to embed the total_cost variable
# :.2f formats the number to exactly 2 decimal places
# $ is included in the string as required by output format
print(f"Total price: ${total_cost:.2f}")