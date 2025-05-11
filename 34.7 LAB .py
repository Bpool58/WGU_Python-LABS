# Define the predetermined list of numbers
predef_list = [4, -27, 15, 33, -10]

# Get integer input from user
user_input = int(input())

# Find the maximum value in predef_list using max() function
# max() returns the highest value in the list
# In this case, 33 is the maximum value in predef_list
max_value = max(predef_list)

# Compare user_input with max_value using > operator
# This will return True if user_input is greater than max_value
# False otherwise
# Example: if user enters 20, comparison will be (20 > 33), which is False
is_greater = user_input > max_value

# Print the result using f-string
# Format: "Greater Than Max? {Boolean_result}"
print(f"Greater Than Max? {is_greater}")