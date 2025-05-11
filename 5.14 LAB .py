highway_number = int(input())
if (highway_number < 1) or (highway_number > 999) or (highway_number == 0):
    print("invalid")
else:
    if highway_number > 99:
        primary_number = highway_number % 100



