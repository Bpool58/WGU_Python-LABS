"""
Create a Python solution to the following task.
Ensure that the solution produces output in exactly the same format shown in the sample(s) below,
including capitalization and whitespace.

Task:
Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit.
Output a description of the water state based on the following scale:

If the temperature is below 33° F, the water is “Frozen”.
If the water is between 33° F and 80° F (including 33), the water is “Cold”.
If the water is between 80° F and 115° F (including 80), the water is "Warm".
If the water is between 115° F and 211° (including 115) F, the water is “Hot".
If the water is greater than or equal to 212° F, the water is “Boiling”.
Additionally, output a safety comment only during the following circumstances:

If the water is exactly 212° F, the safety comment is "Caution: Hot!"
If the water temperature is less than 33° F, the safety comment is "Watch out for ice!"
The solution output should be in the format:

water_state
optional_safety_comment
"""

# Accept the water temperature as input from user
# Convert string input to integer using int()
temperature = int(input())

# Start checking temperature ranges from highest to lowest
# Using if-elif-else structure for mutually exclusive conditions
if temperature >= 212:
    # For temperatures at or above 212°F
    print("Boiling")
    
    # Special case: exactly 212°F needs safety warning.
    if temperature == 212:
        print("Caution: Hot!")

# For temperatures between 115°F and 211°F (including 115)
elif temperature >= 115:
    print("Hot")

# For temperatures between 80°F and 114°F (including 80)
elif temperature >= 80:
    print("Warm")

# For temperatures between 33°F and 79°F (including 33)
elif temperature >= 33:
    print("Cold")

# For any temperature below 33°F
else:
    print("Frozen")
    # Temperatures below 33°F always get ice warning
    print("Watch out for ice!")