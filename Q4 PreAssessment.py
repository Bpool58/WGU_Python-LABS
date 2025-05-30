"""
Task:
Create a solution that accepts any three integer inputs representing
 the base (b1, b2) and height (h) measurements of a trapezoid in meters.
 Output the exact area of the trapezoid in square meters as a float value.
  The exact area of a trapezoid can be calculated by finding the average
  of the two base measurements, then multiplying by the height measurement.

Trapezoid Area Formula:
A = [(b1 + b2) / 2] * h

The solution output should be in the format

Trapezoid area: area_value square meters
"""

b1 = int(input())
b2 = int(input())
h = int(input())


area = .5 * (b1 + b2) * h

print(f"Trapezoid area = {area} square meters")

#hints
#solution accepts three integer values representing base and height measurements of a trapezoid
#first and second integers represent base 1 and base 2; third integer represents height
#solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h