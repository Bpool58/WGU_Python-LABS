"""
Mad Libs are activities that have a person provide various words,
 which are then used to complete a short story in unexpected (and hopefully funny) ways.
- Write a program that takes a string and an integer as input, and outputs a sentence using
the input values as shown in the example below. The program repeats until the input string is
quit and disregards the integer input that follows.

Ex: if the input is:
apples 5
shoes 2
quit 0

the output should be:
Eating 5 apples a day keeps the doctor away.
Eating 2 shoes a day keeps the doctor away.
"""

# This program creates Mad Lib sentences using user input until 'quit' is entered
# Each sentence follows the pattern: "Eating {number} {word} a day keeps the doctor away."

# Each sentence follows the pattern: "Eating {number} {word} a day keeps the doctor away."

while True:  # Start an infinite loop - will keep running until explicitly broken
    # Get a line of input from the user
    # Each input line should contain a word followed by a number (e.g., "apples 5")
    user_input = input()

    # Split the input string into two parts at the space character
    # Example: "apples 5" becomes ["apples", "5"]
    # The split() method returns a list of strings
    word, number = user_input.split()

    # Check if the user wants to quit
    # If the first word is 'quit', exit the loop
    # The number following 'quit' is ignored as per requirements
    if word == 'quit':
        break  # Exit the while loop

    # Create and print the Mad Lib sentence:
    # - Using f-string for string formatting
    # - {number} inserts the number from input
    # - {word} inserts the word from input
    # Example: if word="apples" and number="5",
    # output will be: "Eating 5 apples a day keeps the doctor away."
    print(f"Eating {number} {word} a day keeps the doctor away.")
