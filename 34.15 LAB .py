# Import the custom pigAge module from the same directory
# This module contains the pigAge_converter() function that converts pig years to human years
from pigAge import pigAge_converter

# Get integer input from user representing the pig's age
# int() converts the string input to an integer number
pig_age = int(input())

# Use the imported pigAge_converter() function to convert pig age to human years
# The function handles the conversion where 1 pig year = 5 human years
human_age = pigAge_converter(pig_age)

# Format and print the output string
# Using f-string to embed the values of pig_age and human_age in the output string
# Output format: "<pig_age> is <human_age> in human years."
print(f"{pig_age} is {human_age} in human years")