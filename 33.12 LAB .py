"""
Complete the calc_average() function that has an integer list parameter
 and returns the average value of the elements in the list as a float.

Ex: If the input list is:

1 2 3 4 5
then the returned average will be:

3.0

"""

def calc_average(nums):
    # First, check if the list is empty
    # 'not nums' evaluates to True if nums is empty
    # This prevents division by zero errors
    if not nums:
        return 0.0    # Return 0.0 for empty lists
    
    # Calculate the sum of all numbers in the list
    # sum() is a built-in function that adds all elements in an iterable
    total = sum(nums)
    
    # Get the total count of numbers in the list
    # len() returns the length (number of elements) of the list
    count = len(nums)
    
    # Calculate the average:
    # 1. Convert total to float to ensure floating-point division
    # 2. Divide by count to get average
    # Example: if total = 15 and count = 5
    # then average = 15.0 / 5 = 3.0
    average = float(total) / count
    
    # Return the calculated average
    return average

# This is the main program entry point
# This code only runs if this file is run directly
# (not when imported as a module)
if __name__ == '__main__':
    # Create a test list with numbers 1 through 5
    nums = [1, 2, 3, 4, 5]
    
    # Call calc_average() with our test list and print the result
    # For nums = [1, 2, 3, 4, 5]:
    # total = 1 + 2 + 3 + 4 + 5 = 15
    # count = 5
    # average = 15.0 / 5 = 3.0
    print(calc_average(nums))   # Will print: 3.0