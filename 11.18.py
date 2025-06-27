"""

Write a program that first gets a list of integers from input.
 That list is followed by two more integers representing lower
  and upper bounds of a range. Your program should output all
integers from the list that are within that range (inclusive of the bounds).

Ex: If the input is:
25 51 0 200 33
0 50
the output is:
25 0 33
"""

line1 = input().split()
nums = []
for item in line1:
    nums.append(int(item))


line2 = input().split()
upper = int(line2[1])
lower = int(line2[0])

in_range = []

for num in nums:
    if num >= lower and num <= upper:
        in_range.append(num)

for num in in_range:
    print(num, end = ' ')
