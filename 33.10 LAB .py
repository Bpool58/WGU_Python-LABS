"""
Write a program that takes in a line of text as input,
and outputs that line of text in reverse. The program repeats,
 ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:

Hello there
Hey
done
then the output is:

ereht olleH
yeH
"""


# Start an infinite loop that will keep running until explicitly broken
while True:
    # Get a line of text input from the user and store it in variable 'text'
    text = input()
    
    # Check if the user wants to quit
    # This line checks if text matches any of these three values: 'Done', 'done', or 'd'
    if text in ['Done', 'done', 'd']:
        # If user entered any quit command, exit the loop
        break
    
    # If we get here, user didn't enter a quit command, so we reverse their text
    # text[::-1] breaks down as follows:
    # - text[start:end:step]
    # - Empty start means begin from start of string
    # - Empty end means go to end of string
    # - -1 step means move backwards through string
    print(text[::-1])