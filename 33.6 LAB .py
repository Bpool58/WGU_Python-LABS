"""
Given an integer representing a 10-digit phone number, output the area code,
prefix, and line number using the format (800) 555-1212.
Ex: If the input is:
8005551212
the output is: (800) 555-1212
Hint: Use % to get the desired rightmost digits.
 Ex: The rightmost 2 digits of 572 is gotten by 572 % 100, which is 72.
Hint: Use // to shift right by the desired amount.
 Ex: Shifting 572 right by 2 digits is done by 572 // 100, which yields 5. (Recall integer division discards the fraction).
For simplicity, assume any part starts with a non-zero digit. So 0119998888 is not allowed.
"""

# Get the input phone number
phone_number = int(input())

line_number = phone_number % 10000

# Get the last 4 digits (line number) using modulo
line_number = phone_number % 10000      # For 8005551212, this gives us 1212

prefix = (phone_number // 10000) % 1000

# Get the middle 3 digits (prefix)
# First remove last 4 digits (// 10000) then get last 3 digits (% 1000)
prefix = (phone_number // 10000) % 1000  # For 8005551212: 800555 % 1000 = 555

# Get the first 3 digits (area code)
# Remove last 7 digits
area_code = phone_number // 10000000    # For 8005551212: gives us 800

# Print in required format using f-string
print(f"({area_code}) {prefix}-{line_number}")

"""
Here is a second solution that will work for the question
"""

# Convert the integer phone_number to a string
# Example: if phone_number = 8005551212, phone_str becomes "8005551212"
phone_str = str(phone_number)

# Using f-string (formatted string) to construct the output
# f'...' allows us to embed expressions inside {} brackets
print(f'({phone_str[0:3]}) {phone_str[3:6]}-{phone_str[6:]}')
    # phone_str[0:3]   -> Takes characters from index 0,1,2 (first 3 digits)
    #                     Example: "800"
    # phone_str[3:6]   -> Takes characters from index 3,4,5 (middle 3 digits)
    #                     Example: "555"
    # phone_str[6:]    -> Takes all characters from index 6 to the end (last 4 digits)
    #                     Example: "1212"
    # The rest of characters ( , ), - and spaces are string literals that appear as-is
    
    # So.. if phone_str is "8005551212", this constructs:
    # (800) 555-1212