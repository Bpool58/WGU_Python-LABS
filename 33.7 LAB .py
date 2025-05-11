# Solution 1: Finding smallest number using comparison method
# -------------------------------------------------------

# Get three integers as input from the user
# input() reads a string, int() converts it to an integer
num1 = int(input())  # First number
num2 = int(input())  # Second number
num3 = int(input())  # Third number

# Initialize the smallest variable with the first number
# We'll compare other numbers against this
smallest = num1

# Compare second number with current smallest
# If num2 is smaller, update our smallest value
if num2 < smallest:
    smallest = num2

# Compare third number with current smallest
# If num3 is smaller, update our smallest value
if num3 < smallest:
    smallest = num3

# Print the smallest number found
print(smallest)


# Solution 2: Finding smallest number using min() function
# ----------------------------------------------------

# Get three integers as input from the user
num1 = int(input())  # First number
num2 = int(input())  # Second number
num3 = int(input())  # Third number

# Use Python's built-in min() function to find the smallest value
# min() compares all arguments and returns the smallest one
smallest = min(num1, num2, num3)

# Print the smallest number found
print(smallest)