# Import the csv module which provides functionality to read/write CSV files
import csv

# Get the filename from user input (e.g., "input1.csv")
filename = input()

# Open the CSV file in read mode ('r')
# 'with' statement ensures the file is properly closed after we're done
with open(filename, 'r') as file:
    # Create a CSV reader object
    # This object will help us read the CSV file line by line
    reader = csv.reader(file)
    
    # Loop through each row in the CSV file
    # In this case, we expect only two rows
    for row in reader:
        # Initialize an empty dictionary for current row
        row_dict = {}
        
        # Process each row in pairs (key, value)
        # range(start=0, stop=len(row), step=2) means:
        # - start at index 0
        # - go up to length of row
        # - increment by 2 each time (to handle pairs)
        for i in range(0, len(row), 2):
            # row[i] is the key (at even index)
            # row[i + 1] is the value (at odd index)
            row_dict[row[i]] = row[i + 1]
            
        # Print the dictionary for current row.
        print(row_dict)