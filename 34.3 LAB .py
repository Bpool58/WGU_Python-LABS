"""
Task: Data Type Identifier

Description:
    This program identifies the data type of elements in a predefined list.
    The user provides an index number, and the program returns the data type
    of the element at that index.

List Contents:
    - Index 0: 516 (integer)
    - Index 1: 112.49 (float)
    - Index 2: True (boolean)
    - Index 3: "meow" (string)
    - Index 4: ("Western", "Governors", "University") (tuple)
    - Index 5: {"apple": 1, "pear": 5} (dictionary)

Input:
    - An integer between 0 and 5 representing the index position

Output Format:
    Element <index>: <data_type>

Example:
    Input: 4
    Output: Element 4: tuple
"""

# Create a list containing different data types
various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

# Get input from user and convert it from string to integer
# This number will be used as the index to access list elements
index = int(input())

# Use the index to get the specific element from the list
# For example: if index is 4, element will be ("Western", "Governors", "University")
element = various_data_types[index]

# Get the type of the element using type() function
# __name__ attribute returns the name of the type as a string
# For example: if element is a tuple, type_of_element will be "tuple"
type_of_element = type(element).__name__

# Print the result using f-string formatting.
# Format: "Element index: type"
# For example: "Element 4: tuple"
print(f"Element {index}: {type_of_element}")