# Define the predefined list
predef_list = [4, -27, 15, 33, -10]

# Get input from user and convert to integer
user_input = int(input())

# Find maximum value from predef_list
max_value = max(predef_list)

# Compare user input with maximum value
result = user_input > max_value

# Print the result in required format
print(f"Greater Than Max? {result}")