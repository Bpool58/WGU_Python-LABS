"""
Create a solution that accepts an integer input.
 Import the built-in module math and use its factorial() method
 to calculate the factorial of the integer input. Output the value of the factorial,
  as well as a Boolean value identifying whether the factorial output is greater than 100.

The solution output should be in the format

factorial_value
Boolean_value
Sample Input/Output:
If the input is

10
then the expected output is

3628800
True
Alternatively, if the input is

3
then the expected output is

6
False

"""

# Import the math module to use its factorial() function
import math

# Get integer input from user and convert string to int
number = int(input())

# Calculate factorial of the input number using math.factorial()
factorial_result = math.factorial(number)

# Print the factorial result.
print(factorial_result)

# Check if factorial is greater than 100 and print the boolean result
print(factorial_result > 100)