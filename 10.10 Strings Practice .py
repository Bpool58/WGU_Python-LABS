#TODO TASK 1 Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
    # Use string slicing to get characters from start (0) up to position x
    # mystring[0:x] means: start at position 0, get characters up to (but not including) position x
    print(mystring[0:x])

# Test cases
# expected output: WGU
printFirst('WGU College of IT', 3)    
 
# expected output: WGU College
printFirst('WGU College of IT', 11)



#TODO Task 2
# Complete the function to return the last X number of characters
# in the given string
def getLast(mystring, x):
    # Get the length of the string
    length = len(mystring)
    # Return characters from (length - x) to the end
    return mystring[length - x:]

# Test cases
# expected output: IT
print(getLast('WGU College of IT', 2))
 
# expected output: College of IT
print(getLast('WGU College of IT', 13))

#TODO Task 3
# Complete the function to return True if the word WGU exists in the given string
# otherwise return False
def containsWGU(mystring):
    # Use the 'in' operator to check if 'WGU' exists in mystring
    return "WGU" in mystring
    
# Test cases
# expected output: True
print(containsWGU('WGU College of IT'))
    
# expected output: False
print(containsWGU('Night Owls Rock'))

#TODO Task 4  Complete the function to print all of the words in the given string
def printWords(mystring):
    # Use split() method to separate string into words
    # By default, split() uses whitespace as the delimiter
    words = mystring.split()
    print(words)
    
# Test cases
# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')    
    
# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')


#TODO Task 5  Complete the function to combine the words into a sentence and return a string
def combineWords(words):
    # Use join() method with a space as separator to combine the words
    return ' '.join(words)
    
# Test cases
# expected output: WGU College of IT
print(combineWords(['WGU', 'College', 'of', 'IT']))
    
# expected output: Night Owls Rock
print(combineWords(['Night', 'Owls', 'Rock']))

# TODO Task 6 Complete the function to replace the word WGU with Western Governors University
#  and print the new string
def replaceWGU(mystring):
    # Use replace() method to substitute 'WGU' with 'Western Governors University'
    new_string = mystring.replace('WGU', 'Western Governors University')
    print(new_string)
    
# Test cases
# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')
    
# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')

# TODO Task 7 Complete the function to remove the word WGU from the given string
# ONLY if it's not the first word and return the new string
def removeWGU(mystring):
    # Check if the string starts with 'WGU'
    # startswith() is a string method that returns True if the string begins with the specified value
    if mystring.startswith('WGU'):
        # If the string starts with 'WGU', return the original string unchanged
        # This handles cases like 'WGU Rocks' where we want to keep WGU
        return mystring
    
    # If the string doesn't start with 'WGU', remove all instances of 'WGU'
    # replace() is a string method that replaces all occurrences of a substring
    # Here we replace 'WGU' with an empty string '', effectively removing it
    return mystring.replace('WGU', '')
    
# Test case 1: string starts with WGU - should return unchanged
# Output: WGU Rocks
print(removeWGU('WGU Rocks'))
    
# Test case 2: string has WGU in the middle - should remove WGU
# Output: Hello, John
print(removeWGU('Hello, WGUJohn'))


# TODO Task 8 Complete the function to remove trailing spaces from the first string
# and leading spaces from the second string and return the combined strings
def removeSpaces(string1, string2):
    # Step 1: Clean the first string
    # rstrip() removes any spaces at the end (right side) of the string
    # Example 1: "WGU Rocks    " -> "WGU Rocks"
    # Example 2: "Welcome WGU " -> "Welcome WGU"
    clean_first = string1.rstrip()

    # Step 2: Clean the second string
    # lstrip() removes any spaces at the beginning (left side) of the string
    # Example 1: "  -You know it!" -> "-You know it!"
    # Example 2: " -IT Students" -> "-IT Students"
    clean_second = string2.lstrip()

    # Step 3: Combine the cleaned strings
    # Use + to join the strings with no space between them
    # The spaces have already been removed where needed
    result = clean_first + clean_second

    # Step 4: Return the final combined string
    return result


# Test case 1
# Input 1: "WGU Rocks    " (has 4 spaces at the end)
# Input 2: "  -You know it!" (has 2 spaces at the start)
# Expected output: "WGU Rocks-You know it!"
print(removeSpaces('WGU Rocks    ', '  -You know it!'))

# Test case 2
# Input 1: "Welcome WGU " (has 1 space at the end)
# Input 2: " -IT Students" (has 1 space at the start)
# Expected output: "Welcome WGU-IT Students"
print(removeSpaces('Welcome WGU ', ' -IT Students'))





#TODO Task 9
# Complete the function to print the specified hourly rate with two decimals
def displayHourlyRate(rate):
    # round() function is used to round the rate to 2 decimal places
    # Example: 34.789123 becomes 34.79
    rounded_rate = round(rate, 2)
    
    # Format the output with a dollar sign
    # We use an f-string to combine the $ symbol with the rounded rate
    # The :.2f ensures exactly 2 decimal places are shown
    # Example: 34.79 becomes "$34.79"
    print(f"${rounded_rate:.2f}")
    
# Test case 1: rounds 34.789123 to 34.79
# expected output: $34.79
displayHourlyRate(34.789123)    
 
# Test case 2: rounds 24.123456 to 24.12
# expected output: $24.12
displayHourlyRate(24.123456)

#TODO Task 10 Complete the Function to return the number of uppercase letters in the given string
def countUpper(mystring):
    # Create a variable to keep track of uppercase letters
    # Start it at 0 since we haven't counted any letters yet
    count = 0
    
    # Look at each letter one at a time in the string
    # For example, in "Hello" we look at 'H', then 'e', then 'l', etc.
    for letter in mystring:
        
        # Use isupper() to check if the letter is uppercase
        # isupper() gives us True if it's uppercase, False if it isn't
        if letter.isupper():
            # If we found an uppercase letter, add 1 to our count
            count = count + 1
    
    # After checking all letters, return the final count
    return count

# Test 1: Count uppercase letters in 'Welcome to WGU'
# W, W, G, U are uppercase, so we expect 4
print(countUpper('Welcome to WGU'))

# Test 2: Count uppercase letters in 'Hello, Mary'''
# H, M are uppercase, so we expect 2
print(countUpper('Hello, Mary'))

#Edit