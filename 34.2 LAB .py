"""
Instructions:
Create a Python solution to the following task.
Ensure that the solution produces output in exactly the same format shown in the sample(s) below,
 including capitalization and whitespace.

Task:
Create a solution that accepts an integer input representing any number of ounces.
 Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value.
 There are 16 ounces in a pound and 2,000 pounds in a ton.

The solution output should be in the format

Tons: value_1
Pounds: value_2
Ounces: value_3
Sample Input/Output:
If the input is

32035
then the expected output is

Tons: 1
Pounds: 2
Ounces: 3

"""
# Get input from user and convert to integer
ounces = int(input())

# Step 1: Convert ounces to pounds first (16 ounces = 1 pound)
total_pounds = ounces // 16    # Use integer division to get whole pounds

# Step 2: Convert pounds to tons (2000 pounds = 1 ton)
tons = total_pounds // 2000    # Get whole tons

# Step 3: Calculate remaining pounds after tons are taken out
pounds = total_pounds % 2000   # Use modulo to get remainder pounds

# Step 4: Calculate remaining ounces
ounces = ounces % 16          # Use modulo to get remainder ounces

# Print results in required format
print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {ounces}")