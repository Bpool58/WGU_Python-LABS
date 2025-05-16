# Import the csv module - this is a built-in Python module that helps work with CSV (Comma Separated Values) files
# CSV files are text files where data is separated by commas
import csv

# Get the filename from user using input()
# input() reads a line of text from the user and returns it as a string
# The program will wait here until the user enters something and presses Enter
filename = input()

# Create an empty list that will store our dictionaries
# We need this because we'll create one dictionary for each row in the CSV file
# Using [] creates an empty list
rows_as_dicts = []

# Open the CSV file for reading
# 'with' statement is used to properly handle opening and closing the file
# 'r' means we're opening the file in read mode
# 'file' is the variable that will hold our opened file object
with open(filename, 'r') as file:
    # Create a CSV reader object using csv.reader()
    # This object knows how to read and parse CSV formatted data
    # It will automatically handle the commas and line breaks in the CSV file
    csv_reader = csv.reader(file)
    
    # Loop through each row in the CSV file
    # csv_reader will give us one row at a time
    # Each row is a list of strings
    for row in csv_reader:
        # Create an empty dictionary for the current row
        # This dictionary will store the key-value pairs from this row
        # Using {} creates an empty dictionary
        row_dict = {}
        
        # Loop through the items in the current row
        # range(0, len(row), 2) creates a sequence of numbers:
        # - starts at 0
        # - goes up to len(row) (the length of the row)
        # - steps by 2 (so we get 0, 2, 4, ...)
        # This lets us get both the key and its corresponding value
        for i in range(0, len(row), 2):
            # Get the key from the current position (i)
            # strip() removes any extra spaces from the beginning and end
            key = row[i].strip()
            
            # Get the value from the next position (i+1)
            # strip() removes any extra spaces from the beginning and end
            value = row[i+1].strip()
            
            # Add the key-value pair to our dictionary
            # This creates or updates the key in the dictionary with its value
            row_dict[key] = value
            
        # After the inner loop finishes, we have processed all key-value pairs in this row
        # Add the completed dictionary to our list
        rows_as_dicts.append(row_dict)

# After the outer loop finishes, we have processed all rows
# Now we print each dictionary

# Print the first dictionary (index 0)
# This corresponds to the first row of the CSV file
print(rows_as_dicts[0])

# Print the second dictionary (index 1)
# This corresponds to the second row of the CSV file
print(rows_as_dicts[1])