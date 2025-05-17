"""
Task:
Create a solution that accepts five integer inputs.
 Output the sum of the five inputs three times, converting the inputs to the
 requested data type prior to finding the sum.

First output: sum of five inputs maintained as integer values
Second output: sum of five inputs converted to float values
Third output: sum of five inputs converted to string values (concatenate)
The solution output should be in the format

Integer: integer_sum_value
Float: float_sum_value
String: string_sum_value
Sample Input/Output:
If the input is:
1
3
6
2
7
then the expected output is:

Integer: 19
Float: 19.0
String: 13627
"""

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())


sum1 = (num1 + num2 + num3 + num4 + num5)
sum2 = (float(num1) + float(num2) + float(num3) + float(num4) + float(num5))
sum3 = (str(num1) + str(num2) + str(num3) + str(num4) + str(num5))


print(f"Integer: {sum1}")
print(f"Float: {sum2}")
print(f"String: {sum3}")

