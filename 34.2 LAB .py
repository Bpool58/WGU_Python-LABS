# Get input from user and convert to integer
ounces = int(input())

# Step 1: Convert ounces to pounds first (16 ounces = 1 pound)
total_pounds = ounces // 16    # Use integer division to get whole pounds

# Step 2: Convert pounds to tons (2000 pounds = 1 ton)
tons = total_pounds // 2000    # Get whole tons

# Step 3: Calculate remaining pounds after tons are taken out
pounds = total_pounds % 2000   # Use modulo to get remainder pounds

# Step 4: Calculate remaining ounces
ounces = ounces % 16          # Use modulo to get remainder ounces

# Print results in required format
print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {ounces}")