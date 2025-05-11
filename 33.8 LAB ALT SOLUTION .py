# Get the total change amount in cents from user
# We use int() because input() returns a string
change = int(input())

# # First handle the special case - zero or negative input
# This is called "edge case" handling
if change <= 0:
    print("No change")
else:
    # Dictionary stores coin types and their values
    # Using dictionary because:
    #   - Keeps coin name and value paired together
    #   - Maintains order (Python 3.7+)
    #   - Easy to modify if coin values change
    coins = {
        "Dollar": 100,  # 100 cents
        "Quarter": 25,  # 25 cents
        "Dime": 10,  # 10 cents
        "Nickel": 5,  # 5 cents
        "Penny": 1  # 1 cent
    }

    # Process each coin type from largest to smallest
    # coins.items() returns pairs of (name, value)
    for coin_name, coin_value in coins.items():
        # Integer division (//) gives us how many coins we need
        # Example: 45 // 25 = 1 (one quarter from 45 cents)
        num_coins = change // coin_value

        # Only print if we need this coin type
        if num_coins > 0:
            # Modulo (%) gives us the remaining change
            # Example: 45 % 25 = 20 (20 cents left after using quarter)
            change = change % coin_value

            # Handle singular vs plural forms
            if num_coins == 1:
                # Singular form: "1 Dollar", "1 Quarter", etc.
                print(f"1 {coin_name}")
            else:
                # Plural form needs special handling for "Penny"
                if coin_name == "Penny":
                    # Special case: "Pennies" instead of "Pennys"
                    print(f"{num_coins} Pennies")
                else:
                    # Regular plural: just add 's'
                    # Example: "Dollars", "Quarters", etc.
                    print(f"{num_coins} {coin_name}s")
