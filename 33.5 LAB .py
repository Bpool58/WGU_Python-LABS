"""
Given four values representing counts of quarters, dimes,
 nickels and pennies, output the total amount as dollars and cents.

Output each floating-point value with two digits after the decimal point,
which can be achieved as follows:
print(f'Amount: ${dollars:.2f}')

Ex: If the input is:
4
3
2
1
where 4 is the number of quarters, 3 is the number of dimes, 2 is the number of nickels,
and 1 is the number of pennies, the output is:

Amount: $1.41
"""

base_char = input()
head_char = input()

row1 = '      ' + head_char
row2 = (base_char * 6) + (head_char * 2)
row3 = (base_char * 6) + (head_char * 3)

print(row1)
print(row2)
print(row3)
print(row2)
print(row1)

