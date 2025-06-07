"""
Write a program whose input is two integers.
Output the first integer and subsequent increments of 5
as long as the value is less than or equal to the second integer. End with a newline.

Ex: If the input is:

-15
10
the output is:

-15 -10 -5 0 5 10
Ex: If the second integer is less than the first as in:

20
5
the output is:

Second integer can't be less than the first..
"""


first = int(input())
second = int(input())

if first > second:
    print("Second integer can't be less than the first.")

else:
    for i in range(first, second + 1, 5):
        print(i, end=" ")
    print()
