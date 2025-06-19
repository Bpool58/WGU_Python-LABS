"""
Program: Number Set Difference Calculator
Purpose: Remove numbers from the first set that appear in the second set

Problem-Solving Steps:
1. Data Structure Planning:
   - Need two lists to store two sets of numbers
   - First list will be modified, second list used for comparison

2. Input Requirements:
   - Get two sets of numbers from user
   - Numbers should be space-separated
   - Convert string inputs to integers

3. Processing Logic:
   - Compare each number in first set with second set
   - Remove numbers from first set that appear in second set
   - Keep track of which numbers are being removed

4. Output Requirements:
   - Show position and value while inputting numbers
   - Display which numbers are being deleted
   - Print remaining numbers in first set

5. Visual Formatting:
   - Use blank lines between sections for readability
   - Format final output with proper spacing

"""

nums1 = []
nums2 = []

user_input = input('Enter first set of numbers: ')
tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
print()
for pos, val in enumerate(tokens):
    nums1.append(int(val))

    print(f'{pos}: {val}')

user_input = input('Enter second set of numbers:')
tokens = user_input.split()

# Convert strings to integers
print()
for pos, val in enumerate(tokens):
    nums2.append(int(val))

    print(f'{pos}: {val}')

# Remove elements from nums1 if also in nums2
print()
for val in nums1:
    if val in nums2:
        print(f'Deleting {val}')
        nums1.remove(val)

# Print new numbers
print('\nNumbers only in first set:', end=' ')
for num in nums1:
    print(num, end=' ')