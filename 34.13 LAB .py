import csv                   # Step 1: Import the csv module to handle CSV files

filename = input()          # Step 2: Get filename from user input (e.g., "input1.csv")

with open(filename) as file: # Step 3: Open the file (the 'with' ensures file is properly closed)
    csv_reader = csv.reader(file)  # Step 4: Create a CSV reader object
    
    # ----- HANDLING FIRST ROW -----
    row = next(csv_reader)  # Step 5: Get first row as a list
                           # If row is "a,100,b,200,c,300"
                           # row becomes ['a', '100', 'b', '200', 'c', '300']
    
    # Create dictionary for first row
    print({row[i]: row[i+1] for i in range(0, len(row), 2)})
    # Let's break this line down:
    #   range(0, len(row), 2) - creates sequence: 0, 2, 4
    #   For each i in that sequence:
    #     row[i]   becomes the key
    #     row[i+1] becomes the value
    #
    # Detailed steps for first row:
    # i = 0:
    #   key   = row[0] = 'a'
    #   value = row[1] = '100'
    #   Adds 'a': '100' to dictionary
    #
    # i = 2:
    #   key   = row[2] = 'b'
    #   value = row[3] = '200'
    #   Adds 'b': '200' to dictionary
    #
    # i = 4:
    #   key   = row[4] = 'c'
    #   value = row[5] = '300'
    #   Adds 'c': '300' to dictionary
    #
    # Final result printed: {'a': '100', 'b': '200', 'c': '300'}

    # ----- HANDLING SECOND ROW -----
    row = next(csv_reader)  # Step 6: Get second row as a list
                           # If row is "bananas,1.85,steak,19.99,cookies,4.52"
                           # row becomes ['bananas', '1.85', 'steak', '19.99', 'cookies', '4.52']
    
    # Create dictionary for second row
    print({row[i]: row[i+1] for i in range(0, len(row), 2)})
    # Same process as above:
    # i = 0:
    #   key   = row[0] = 'bananas'
    #   value = row[1] = '1.85'
    #   Adds 'bananas': '1.85' to dictionary
    #
    # i = 2:
    #   key   = row[2] = 'steak'
    #   value = row[3] = '19.99'
    #   Adds 'steak': '19.99' to dictionary
    #
    # i = 4:
    #   key   = row[4] = 'cookies'
    #   value = row[5] = '4.52'
    #   Adds 'cookies': '4.52' to dictionary
    #
    # Final result printed: {'bananas': '1.85', 'steak': '19.99', 'cookies': '4.52'}