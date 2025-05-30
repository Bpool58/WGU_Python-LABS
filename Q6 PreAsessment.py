"""
Create a solution that accepts an integer input representing a 9-digit unformatted student identification number.
 Output the identification number as a string with no spaces.

The solution output should be in the format

111-22-3333
Sample Input/Output:
If the input is

154175430
then the expected output is

154-17-5430
Input to program
"""

number = int(input())

first_part = number // 1000000

second_part = (number // 10000) % 100

third_part = number // 1000000

print(f"{first_part}-{second_part}-{third_part}")

