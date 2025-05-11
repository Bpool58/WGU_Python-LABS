"""
Write a program that removes all non-alphabetic characters from input.
ex: if the input is:
-Hello world$!
the output should be:
Helloworld
"""


# This program removes all non-alphabetic characters from input
# Non-alphabetic characters include: numbers, spaces, punctuation marks, etc.

# Step 1: Get the input string from user
user_input = input()

# Step 2: Create an empty string to store our result
result = ""

# Step 3: Loop through each character in the input
# Only keep characters that are alphabetic (letters a-z or A-Z)
for character in user_input:
    # isalpha() checks if a character is alphabetic
    if character.isalpha():
        result += character

# Step 4: Print the final result
print(result)