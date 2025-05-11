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