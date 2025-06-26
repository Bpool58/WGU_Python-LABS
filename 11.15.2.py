# Define a nested dictionary structure for storing student grades
# The outer dictionary uses student names as keys
# The inner dictionary contains different assessment types and scores
grades = {
    'John Ponting': {                    # First student's data
        'Homeworks': [79, 80, 74],       # List of homework scores
        'Midterm': 85,                   # Single midterm score
        'Final': 92                      # Single final exam score
    },
    'Jacques Kallis': {                  # Second student's data
        'Homeworks': [90, 92, 65],
        'Midterm': 87,
        'Final': 75
    },
    'Ricky Bobby': {                     # Third student's data
        'Homeworks': [50, 52, 78],
        'Midterm': 40,
        'Final': 65
    },
}

# Get initial input from user
# This will be used to look up student records
user_input = input('Enter student name: ')

# Continue loop until user types 'exit'
while user_input != 'exit':
    # Check if the entered name exists in our grades dictionary
    if user_input in grades:
        # Extract values from the nested dictionary structure
        # Using dictionary key access to get specific values
        homeworks = grades[user_input]['Homeworks']    # Get list of homework scores
        midterm = grades[user_input]['Midterm']        # Get midterm score
        final = grades[user_input]['Final']            # Get final exam score

        # Print homework scores using enumerate
        # enumerate provides both index (hw) and value (score) in each iteration
        # hw will start from 0, representing homework number
        for hw, score in enumerate(homeworks):
            print(f'Homework {hw}: {score}')

        # Print midterm score
        print(f'Midterm: {midterm}')

        # Print final exam score
        print(f'Final: {final}')

        # Calculate total points using list comprehension and sum
        # [i for i in homeworks] creates a list of all homework scores
        # sum() adds up all values in the list
        # Adding midterm and final scores to get total points
        total_points = sum([i for i in homeworks]) + midterm + final

        # Calculate and print final percentage
        # 500.0 represents maximum possible points
        # Multiply by 100 to get percentage
        # :.1f formats to 1 decimal place
        print(f'Final percentage: {100 * (total_points / 500.0):.1f}%')

    # Get next student name or 'exit' to end program
    user_input = input('Enter student name: ')

# Example of program flow:
# 1. Enter "John Ponting"
# 2. Program displays:
#    Homework 0: 79
#    Homework 1: 80
#    Homework 2: 74
#    Midterm: 85
#    Final: 92
#    Final percentage: 82.0%
# 3. Program asks for another name or 'exit' to quit