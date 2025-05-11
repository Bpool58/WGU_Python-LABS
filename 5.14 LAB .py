highway_number = int(input())
if (highway_number < 1) or (highway_number > 999) or (highway_number == 0):
    print("invalid")
else:
    if highway_number > 99:
        primary_number = highway_number % 100



"""
LAB: Interstate Highway Numbers

This program determines if a highway number represents a primary or auxiliary interstate 
and provides information about its direction or service route.

Rules:
1. Primary highways are numbered 1-99
   - Odd numbers run north/south
   - Even numbers run east/west

2. Auxiliary highways are numbered 100-999
   - Service the primary highway indicated by last two digits
   - Example: I-405 services I-5, I-290 services I-90

3. Invalid highway numbers:
   - Numbers less than 1 or greater than 999
   - Auxiliary highways ending in '00' (like 200, 300) are invalid
     because '00' is not a valid primary highway number

Input: 
- Single integer representing highway number

Output formats:
1. For primary highways (1-99):
   "I-{number} is primary, going {north/south or east/west}."

2. For auxiliary highways (100-999):
   "I-{number} is auxiliary, serving I-{primary}, going {north/south or east/west}."

3. For invalid numbers:
   "{number} is not a valid interstate highway number."

Examples:
Input: 90
Output: I-90 is primary, going east/west.

Input: 290
Output: I-290 is auxiliary, serving I-90, going east/west.

Input: 0
Output: 0 is not a valid interstate highway number.

Input: 200
Output: 200 is not a valid interstate highway number.
"""
