"""`
# Brute Force Equation Solver
This program solves a system of two linear equations using brute force method:
- First equation: ax + by = c
- Second equation: dx + ey = f
The program tries all possible integer values for x and y in range [-10, 10]
"""

a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

solution_found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if ((a * x) + (b * y) == c and (d * x) + (e * y)) == f:
            print(f"x = {x}, y = {y}")
            solution_found = True
            break
    if solution_found:
        break
if not solution_found:
    print("There is no solution.")

    """
    ALT SOLUTION:
    """


a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

solution_found = False
for x in range(-10, 11):
    for y in range(-10, 11):
        if ((a * x) + (b * y) == c) and ((d * x) + (e * y)) == f:
            print(f"x = {x}, y = {y}")
            solution_found = True
            x_solution = x
            y_solution = y
if solution_found:
    print(f"x = {x_solution}, y = {y_solution}")
else:
    print("There is no solution..")