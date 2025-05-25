"""
5.14 LAB: Interstate highway numbers
Primary U.S. interstate highways are numbered 1-99.
 Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west.
 Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits.
 Thus, I-405 services I-5, and I-290 services I-90. Note: 200 is not a valid auxiliary highway because
 00 is not a valid primary highway number.

Given a highway number, indicate whether it is a primary or auxiliary highway.
 If auxiliary, indicate what primary highway it serves. Also indicate if the (primary)
  highway runs north/south or east/west.

Ex: If the input is:

90
the output is:

I-90 is primary, going east/west.
Ex: If the input is:

290
the output is:

I-290 is auxiliary, serving I-90, going east/west.
Ex: If the input is:

0
the output is:

0 is not a valid interstate highway number.
Ex: If the input is:

200
the output is:

200 is not a valid interstate highway number.
"""

# Get the highway number from user input and convert it to integer
highway_number = int(input())

# Check if the highway number is invalid (less than or equal to 0, or greater than 999)
if highway_number <= 0 or highway_number > 999:
    print(f"{highway_number} is not a valid interstate highway number.")
elif 1 <= highway_number <= 99:
    # Handle primary highways (numbered 1-99)
    if highway_number % 2 == 0:
        # Even numbered highways run east/west
        direction = "east/west"
    else:
        # Odd numbered highways run north/south
        direction = "north/south"
    print(f"I-{highway_number} is primary, going {direction}.")
elif 100 <= highway_number <= 999:
    # Handle auxiliary highways (numbered 100-999)
    # Get the primary highway number by taking last two digits
    primary_served = highway_number % 100

    # Check if the primary highway number is 00 (invalid)
    if primary_served == 0:
        print(f"{highway_number} is not a valid interstate highway number.")
    else:
        # Determine direction based on the primary highway it serves
        if primary_served % 2 == 0:
            # If primary highway is even, direction is east/west
            direction = "east/west"
        else:
            # If primary highway is odd, direction is north/south
            direction = "north/south"
        print(f"I-{highway_number} is auxiliary, serving I-{primary_served}, going {direction}.")
