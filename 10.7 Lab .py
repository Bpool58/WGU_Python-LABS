# This program counts how many times a specific character appears in a phrase
# Input format example: "n Monday" (character followed by space, then phrase)

# Step 1: Get input from user
# The input will be a character, followed by a space, then a phrase
user_input = input()

# Step 2: Extract the search character (first position of input)
# user_input[0] takes the very first character from the input
# Example: if input is "n Monday", search_char will be "n"
search_char = user_input[0]

# Step 3: Extract the phrase (everything after the space)
# user_input[2:] takes everything from the third position to the end
# We use [2:] because:
#   - Position 0 is the search character
#   - Position 1 is the space
#   - Position 2 is where the phrase begins
# Example: if input is "n Monday", phrase will be "Monday"
phrase = user_input[2:]

# Step 4: Count how many times the search character appears in the phrase
# The count() method counts occurrences of a character in a string
# Example: if search_char is "n" and phrase is "sunny", count will be 1
count = phrase.count(search_char)

# Step 5: Print the result with proper formatting
# We need different formats based on the count:
#   - If count is 1: print "1 character"
#   - If count is 0 or more than 1: print "count character's"
if count == 1:
    print(f"1 {search_char}")
else:
    print(f"{count} {search_char}'s")

user_input = input()
searched_char = user_input[0]
phrase = user_input[2:]
count = phrase.count(searched_char)
if count ==1:
    print(f"1 {searched_char}")
else:
    print(f"{count} {searched_char}'s")