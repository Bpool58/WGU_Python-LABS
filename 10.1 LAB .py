#%% md
# # String Slicing Tutorial
# This notebook demonstrates how to slice strings in Python using a simple function that prints the first X characters of a string.
#%%
def printFirst(mystring, x):
    print(mystring[0:x])

print("Test Case 1: printFirst('WGU College of IT', 3)")
printFirst('WGU College of IT', 3)
print("\nTest Case 2: printFirst('WGU College of IT', 11)")
printFirst('WGU College of IT', 11)
#%% md
# ## Understanding String Indices
# Let's see how Python indexes string characters:
#%%"""


# - Index starts at 0
# - Spaces count as characters
# - Slicing gets characters from start index up to (but not including) end index
#%%
print("Example 1: First 2 characters of 'Python'")
print("Expected: 'Py'")
printFirst("Python", 2)

print("\nExample 2: First 4 characters of 'Hello'")
print("Expected: 'Hell'")
printFirst("Hello", 4)

print("\nExample 3: All characters of 'Test'")
print("Expected: 'Test'")
printFirst("Test", 4)

print("\nExample 4: Zero characters (empty result)")
print("Expected: ''")
printFirst("Something", 0)
#%% md
# ## Practice Exercises
# Try predicting what these will print before running them:
# 1. `printFirst("Programming", 3)`
# 2. `printFirst("JavaScript", 4)`
# 3. `printFirst("Python is fun!", 6)`
#%%
print("Exercise 1:")
printFirst("Programming", 3)

print("\nExercise 2:")
printFirst("JavaScript", 4)

print("\nExercise 3:")
printFirst("Python is fun!", 6)
#%% md
# ## Key Points to Remember:
# 1. String indices start at 0
# 2. Slicing `[0:x]` includes the character at position 0 but stops before position x
# 3. Spaces and punctuation marks count as characters
# 4. If x is larger than the string length, it will print the entire string
# 5. If x is 0, it will print an empty line