# Program to read and display available food items from a file

# Get the filename from user input
# input() waits for user to type something and press Enter
filename = input()

# Create empty lists to store each piece of information
# These lists will hold data in parallel (index 0 in each list belongs to the same food item)
categories = []    # Will store food categories (e.g., "Sandwiches", "Salads")
names = []         # Will store food names (e.g., "Ham sandwich")
descriptions = []  # Will store food descriptions
availability = []  # Will store availability status ("Available" or "Not available")

# try-except block to handle potential errors when working with files
try:
    # Open the file for reading ('r' means read mode)
    # 'with' statement automatically closes the file when we're done
    # 'file' is a variable that represents our opened file
    with open(filename, 'r') as file:
        
        # Read the file line by line
        # Each iteration of this loop processes one line from the file
        for line in file:
            # Remove extra spaces/newlines from start and end of line
            # Split the line into parts wherever there's a tab character (\t)
            # This creates a list of strings, stored in 'parts'
            parts = line.strip().split('\t')
            
            # Check if we got exactly 4 parts (category, name, description, availability)
            if len(parts) == 4:
                # Assign each part to a variable
                # This unpacks the list 'parts' into individual variables
                category, name, description, avail = parts
                
                # Add each piece of data to its corresponding list
                # append() adds an item to the end of a list
                categories.append(category)
                names.append(name)
                descriptions.append(description)
                availability.append(avail)

    # After file is read, loop through all food items
    # range(len(names)) creates a sequence of numbers from 0 to the length of our lists
    for i in range(len(names)):
        # Check if this food item is available
        if availability[i] == "Available":
            # If available, print the food item in the required format
            # f-string allows us to embed variables inside string using {}
            print(f"{names[i]} ({categories[i]}) -- {descriptions[i]}")

# If the file isn't found, this code will run
except FileNotFoundError:
    print(f"Error: Could not open {filename}")