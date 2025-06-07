# Function to count the total number of characters in a string
def get_num_of_characters(input_str):
    # Initialize a counter variable to keep track of characters
    count = 0
    
    # Iterate through each character in the input string
    for char in input_str:
        # Increment counter for each character
        count += 1
    
    # Return the total count of characters
    return count

# Function to output the string without any whitespace characters
def output_without_whitespace(input_str):
    # Initialize an empty string to store characters without whitespace
    no_whitespace = ''
    
    # Iterate through each character in the input string
    for char in input_str:
        # Check if the character is not a space or tab
        if char != ' ' and char != '\t':
            # If not whitespace, add the character to our result string
            no_whitespace += char
    
    # Print the final string without whitespace
    print(f'String with no whitespace: {no_whitespace}')

# Main program entry point
if __name__ == '__main__':
    # Prompt the user to enter a sentence or phrase
    print('Enter a sentence or phrase: ')
    # Get the user's input and store it in user_input
    user_input = input()
    
    # Display the original input back to the user
    print(f'You entered: {user_input}')
    
    # Call get_num_of_characters() to count the characters
    # and store the result in num_chars
    num_chars = get_num_of_characters(user_input)
    # Display the total number of characters
    print(f'\nNumber of characters: {num_chars}')
    
    # Call output_without_whitespace() to display the string
    # with all spaces and tabs removed.
    output_without_whitespace(user_input)