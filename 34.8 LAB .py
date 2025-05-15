"""
Task:
Create a solution that accepts one integer input representing the index value
 for any of the string elements in the following list:

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]
Output the string element of the index value entered.
The solution should be placed in a try block and implement an exception of "Error"
if an incompatible integer input is provided.

The solution output should be in the format :
frameworks_element
Sample Input/Output:
If the integer input is

2
then the expected output is

CherryPy
Alternatively, if the integer input is

7
then the expected output is

Error
"""
# Define the list of web frameworks
frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

# Try block to handle potential errors
try:
    # Get input from user and convert it to integer
    index = int(input())
    
    # Try to get the framework name at the specified index
    framework_name = frameworks[index]
    
    # Print the framework name if found
    print(framework_name)

# If any error occurs (like index out of range or invalid input), 
# the except block will run
except:
    # Print "Error" for any error cases
    print("Error")