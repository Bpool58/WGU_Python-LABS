# Get temperature input
temp = int(input())

# Check temperature ranges and print appropriate state
if temp < 33:
    print("Frozen")
    print("Watch out for ice!")
elif temp >= 33 and temp < 80:
    print("Cold")
elif temp >= 80 and temp < 115:
    print("Warm")
elif temp >= 115 and temp < 212:
    print("Hot")
else:  # temp >= 212
    print("Boiling")
    if temp == 212:
        print("Caution: Hot!")