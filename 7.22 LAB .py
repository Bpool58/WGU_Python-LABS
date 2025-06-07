"""
LAB: Swapping variables

Write a program that:
1. Defines a function called swap_values that:
   - Takes four integers as parameters
   - Swaps first value with second value
   - Swaps third value with fourth value
   - Returns the swapped values

2. Main program should:
   - Read four integers from input (one per line)
   - Call swap_values() function with these integers
   - Print the swapped values on a single line separated by spaces

Required function:
def swap_values(user_val1, user_val2, user_val3, user_val4)

Example:
Input:
3
8
2
4

Output:
8 3 4 2

Notes:
- Each input number will be on a separate line
- Output numbers should be on a single line with spaces between them
- No space should appear after the last number.
"""


def swap_values(user_val1, user_val2, user_val3, user_val4):
    return user_val2, user_val1, user_val4, user_val3

if __name__ == "__main__":

    user_input1 = int(input())
    user_input2 = int(input())
    user_input3 = int(input())
    user_input4 = int(input())


    out1, out2, out3, out4 = swap_values(user_input1, user_input2, user_input3, user_input4)

    print(f"{out1}, {out2}, {out3}, {out4}")