"""
Task:
Create a solution that accepts three integer inputs
 representing the number of times an employee travels to a job site.
 Output the total distance traveled to two decimal places given
  the following miles per employee commute to the job site.
  Output the total distance traveled to two decimal places given the
  following miles per employee commute to the job site:

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



Employee_A_miles = 15.62
Employee_B_miles = 41.85
Employee_C_miles = 32.67


Trips_A = int(input())
Trips_B = int(input())
Trips_C = int(input())

total_miles = (Trips_A * Employee_A_miles) + (Trips_B * Employee_B_miles) + (Trips_C * Employee_C_miles)




print(f"Distance: {total_miles:.2f} miles ")