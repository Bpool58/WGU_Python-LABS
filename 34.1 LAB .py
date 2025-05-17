"""
Task:
Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site.
Output the total distance traveled to two decimal places given the following miles per employee commute to the job site.
Output the total distance traveled to two decimal places given the following miles per employee commute to the job site:

Employee A: 15.62 miles
Employee B: 41.85 miles
Employee C: 32.67 miles
The solution output should be in the format

Distance: total_miles_traveled miles
Sample Input/Output:
If the input is

1
2
3
then the expected output is

Distance: 197.33 miles
"""
# Constants for miles per trip
EMPLOYEE_A_MILES = 15.62
EMPLOYEE_B_MILES = 41.85
EMPLOYEE_C_MILES = 32.67

# Get input for number of trips for each employee
trips_a = int(input())
trips_b = int(input())
trips_c = int(input())

# Calculate total distance
total_miles = (EMPLOYEE_A_MILES * trips_a + 
               EMPLOYEE_B_MILES * trips_b + 
               EMPLOYEE_C_MILES * trips_c)

# Format and print the output
print(f"Distance: {total_miles:.2f} miles")