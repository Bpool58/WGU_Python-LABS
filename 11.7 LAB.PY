
"""
11.17 LAB: Filter and sort a list
Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

Ex: If the input is:

10 -7 4 39 -6 12 2
the output is:

2 4 10 12 39
"""



# input() gets the line: "10 -7 4 39 -6 12 2"
# split() breaks it at spaces into: ['10', '-7', '4', '39', '-6', '12', '2']
# these are still strings at this point!

# Step 2: Make an empty list to store our positive numbers
positive_numbers = []
# positive_numbers is now just: []

# Step 3: Go through each number and keep only the positive ones
for num in numbers:
    # First loop: num is '10'
    # Second loop: num is '-7'
    # And so on...

    num = int(num)  # Convert string to integer
    # First loop: '10' becomes 10
    # Second loop: '-7' becomes -7

    if num >= 0:  # Is the number positive or zero?
        positive_numbers.append(num)  # If yes, add it to our list
    # After all loops, positive_numbers has: [10, 4, 39, 12, 2]

# Step 4: Sort the numbers from lowest to highest
positive_numbers.sort()
# positive_numbers is now: [2, 4, 10, 12, 39]

# Step 5: Print each number with a space after it
for i in range(len(positive_numbers)):
    # i will be 0, then 1, then 2, then 3, then 4
    print(positive_numbers[i], end=' ')
    # First loop: prints "2 "
    # Second loop: prints "4 "
    # Third loop: prints "10 "
    # Fourth loop: prints "12 "
    # Fifth loop: prints "39 "
