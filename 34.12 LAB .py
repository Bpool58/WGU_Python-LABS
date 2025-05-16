# Get the filename from user input
filename = input()

# Open the file in read mode ('r') and store the file object in 'file' variable
file = open(filename, 'r')

# Read first line from file, remove extra spaces/newlines with strip(), store in word1
word1 = file.readline().strip()
# Read second line, strip it, store in word2
word2 = file.readline().strip()
# Read third line, strip it, store in word3
word3 = file.readline().strip()

# Close the file since we're done reading
file.close()

# Combine the three words with spaces between them to make a sentence
sentence = word1 + " " + word2 + " " + word3

# Open the same file again, but in append mode ('a') to add content
file = open(filename, 'a')
# Write the sentence to the file with a newline character (\n) before it
file.write("\n" + sentence)
# Close the file after writing
file.close()

# Open the file one more time in read mode
file = open(filename, 'r')
# Read all contents of the file into 'content' variable
content = file.read()
# Print everything that was in the file
print(content)