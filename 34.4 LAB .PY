"""
Trapezoid Area Calculator

This program calculates the area of a trapezoid given:
- Two parallel base lengths (b1 and b2) in meters
- Height (h) in meters

Formula used: A = [(b1 + b2) / 2] * h

Input: Three integers representing:
    - First base (b1)
    - Second base (b2)
    - Height (h)

Output: Area of trapezoid in square meters (as a float)
"""

# Get the first base measurement (b1) from user
# Convert the input string to integer using int()
b1 = int(input())

# Get the second base measurement (b2) from user
b2 = int(input())

# Get the height measurement (h) from user
h = int(input())

# Calculate the area using the trapezoid formula:
# 1. Add the two base measurements (b1 + b2)
# 2. Find their average by dividing by 2
# 3. Multiply by height
area = ((b1 + b2) / 2) * h

# Print the result using f-string formatting
# The format matches exactly: "Trapezoid area: {value} square meters"
print(f"Trapezoid area: {area} square meters")