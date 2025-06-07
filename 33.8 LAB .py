"""
Write a program with total change amount as an integer input,
and output the change using the fewest coins,one coin type per line.
The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies.
Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:

0
(or less than 0), the output is:

No change
Ex: If the input is:

45
the output is:

1 Quarter
2 Dimes
"""

# Initialize variables to store the count of each coin type.
# We start with 0 for each type as we haven't calculated anything yet
dollars = 0    # Will store number of dollar coins (100 cents each)
quarters = 0   # Will store number of quarters (25 cents each)
dimes = 0      # Will store number of dimes (10 cents each)
nickels = 0    # Will store number of nickels (5 cents each)
cents = 0      # Will store the input and remaining cents after each calculation

# Get user input for total amount of change needed
# input() gets a string from user, int() converts it to an integer
cents = int(input())

# First check if the input is valid (greater than 0)
# If 0 or negative, we print "No change" and end the program
if cents <= 0:
    print("No change")
else:
    # Calculate dollars (100 cents each)
    # Integer division (//) gives us whole number of dollars
    dollars = cents // 100
    # Modulo (%) gives us remaining cents after taking out dollars
    cents = cents % 100

    # Calculate quarters (25 cents each)
    # Integer division by 25 gives us number of quarters
    quarters = cents // 25
    # Get remaining cents after quarters
    cents = cents % 25

    # Calculate dimes (10 cents each)
    # Integer division by 10 gives us number of dimes
    dimes = cents // 10
    # Get remaining cents after dimes
    cents = cents % 10

    # Calculate nickels (5 cents each)
    # Integer division by 5 gives us number of nickels
    nickels = cents // 5
    # Get remaining cents (these will be pennies)
    cents = cents % 5

    # Print results for each coin type, but only if we have any of that type
    # For each coin, we need to handle singular (1) vs plural (2 or more) cases

    # Print dollars if we have any
    if dollars > 0:
        if dollars == 1:
            print(f'{dollars} Dollar')    # Singular: 1 Dollar
        else:
            print(f'{dollars} Dollars')   # Plural: 2 Dollars, 3 Dollars, etc.

    # Print quarters if we have any
    if quarters > 0:
        if quarters == 1:
            print(f'{quarters} Quarter')  # Singular: 1 Quarter
        else:
            print(f'{quarters} Quarters') # Plural: 2 Quarters, etc.

    # Print dimes if we have any
    if dimes > 0:                        # Changed from != 0 for consistency
        if dimes == 1:
            print(f'{dimes} Dime')       # Singular: 1 Dime
        else:
            print(f'{dimes} Dimes')      # Plural: 2 Dimes, etc.

    # Print nickels if we have any
    if nickels > 0:
        if nickels == 1:
            print(f'{nickels} Nickel')   # Singular: 1 Nickel
        else:
            print(f'{nickels} Nickels')  # Plural: 2 Nickels, etc.

    # Print pennies (remaining cents) if we have any
    if cents > 0:
        if cents == 1:
            print(f'{cents} Penny')      # Special singular: Penny
        else:
            print(f'{cents} Pennies')    # Special plural: Pennies (not Pennys)