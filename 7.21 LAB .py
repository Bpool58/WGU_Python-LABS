# Define a function called `int_to_reverse_binary` which takes an integer as input
def int_to_reverse_binary(integer_value):
    """
    This function converts a given positive integer into its binary representation 
    in reverse order.

    Parameters:
    integer_value (int): The positive integer to be converted to binary
    
    Returns:
    str: A string representing the binary digits in reverse order
    """

    # Initialize an empty string to store the binary digits
    binary_str = ''

    # A while loop that continues as long as integer_value is greater than 0
    while integer_value > 0:
        # Get the remainder of integer_value divided by 2 (this will be 0 or 1)
        # This represents the least significant bit of the binary representation
        remainder = integer_value % 2

        # Convert the remainder (0 or 1) to a string and append it to binary_str
        # Appending the digits gives a reversed binary order
        binary_str += str(remainder)
        
        # Perform integer division by 2 (this reduces the number by removing the least significant bit)
        # The quotient will become the new integer_value for the next iteration
        integer_value = integer_value // 2

    # When the loop ends, we have a reversed binary string in binary_str
    return binary_str  # Return the reversed binary string to the caller


# Define a function called `string_reverse` to reverse a given string
def string_reverse(input_string):
    """
    This function takes a string as input and returns the reversed version of that string.

    Parameters:
    input_string (str): The input string to be reversed
    
    Returns:
    str: The reversed string
    """

    # Use Python's slicing feature to reverse the string
    # The slicing syntax [::-1] works as follows:
    #  - The first colon (:) specifies starting from the whole string (default start).
    #  - The second colon (:) specifies no stopping point (default stop).
    #  - The `-1` means move backward (step size is negative one).
    return input_string[::-1]  # The result is returned to the caller.


# The entry point of the program
# The `if __name__ == '__main__':` construct ensures this part runs only if the file
# is executed directly, not when it is imported as a module in another Python script.
if __name__ == '__main__':
    """
    The main function of the program. It:
    1. Accepts a positive integer input from the user.
    2. Converts it to its binary representation in reverse order using the function `int_to_reverse_binary`.
    3. Reverses the reversed binary string into the correct binary order using the function `string_reverse`.
    4. Prints the correct binary representation.
    """
    
    # Step 1: Get the input from the user as a string and convert it to an integer.
    #   - Python's `input()` function reads input as a string (e.g., "6").
    #   - `int()` converts it into an integer (e.g., "6" → 6).
    #   - This conversion is necessary because we perform mathematical operations
    #     on the input later (division and modulus).
    # Example: If the user inputs "12", this will store the integer 12 in `number`.
    number = int(input("Enter a positive integer: "))

    # Step 2: Call the `int_to_reverse_binary` function to convert the input number
    #         to its binary representation in reverse order.
    #   - Pass the integer `number` to the function.
    #   - The function will return a string that contains the binary digits in reverse.
    # Example: If number = 12, this will return the string "0011".
    reversed_binary = int_to_reverse_binary(number)

    # Step 3: Call the `string_reverse` function to reverse the reversed binary string
    #         and get the correct binary representation.
    #   - Pass the `reversed_binary` string to the function.
    #   - The function will return a string that contains the proper binary digits.
    # Example: If reversed_binary = "0011", this will return the string "1100".
    binary = string_reverse(reversed_binary)

    # Step 4: Print the final binary string (which represents the correct binary
    #         representation of the original input number).
    # Example: If number = 12, this will print "1100".
    print(binary)