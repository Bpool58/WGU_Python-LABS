"""
Data Type Conversion Exercise

This program:
1. Takes 5 integer inputs
2. Calculates sums in three different ways:
   - As integers
   - As floats
   - As concatenated strings
   
Example input: 1, 3, 6, 2, 7
Expected output:
Integer: 19
Float: 19.0
String: 13627
"""

# Get five integer inputs from user
# Store each input in a separate variable for clarity
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

# 1. Calculate sum as integers
# Since inputs are already integers, just add them
integer_sum = num1 + num2 + num3 + num4 + num5

# 2. Calculate sum as floats
# Convert each number to float before adding
float_sum = float(num1) + float(num2) + float(num3) + float(num4) + float(num5)

# 3. Create string by concatenation
# Convert each number to string and join them together
# Note: No plus signs needed between numbers for this part
string_sum = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)

# Print results in required format
print(f"Integer: {integer_sum}")
print(f"Float: {float_sum}")
print(f"String: {string_sum}")