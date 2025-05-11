print("Enter a 9-digit student ID number (e.g., 154175430):")


number = int(input())

first_part = number // 1000000

second_part = (number // 10000) % 100

third_part = number %10000

print(f"{first_part}-{second_part}-{third_part}")




"""
Student ID Formatter
Converts a 9-digit number into format: XXX-XX-XXXX
Example: 154175430 → 154-17-5430

Using division and modulo to break down the number:
- First 3 digits: number // 1000000     (154)
- Middle 2 digits: (number // 10000) % 100   (17)
- Last 4 digits: number % 10000     (5430)
"""


#ALTERNATIVE SOLUTION: USING STRING SLICING
number = input() #Get input as a string. DO NOT CONVERT TO INTEGER

first_part = number[0:3]
second_part = number[3:5]
third_part = number[5:]

formatted_number = (f"{first_part}-{second_part}-{third_part}")

print(formatted_number)