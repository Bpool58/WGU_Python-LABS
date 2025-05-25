# Get number of stocks to purchase
num_stocks = int(input())

# Dictionary of available stocks and their prices
stocks = {'TSLA': 912.86 , 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 
         'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

# Initialize total cost
total_cost = 0

# Get stock selections and calculate total cost
for _ in range(num_stocks):
    stock = input()
    total_cost += stocks[stock]

# Output formatted total
print(f"Total price: ${total_cost:.2f}")