# Decimal to Binary Conversion using while loop

# Step 1: Get user input
decimal = int(input("Enter a decimal number: "))

# Step 2: Initialize variables
binary = ""
num = decimal

# Step 3: Use while loop to convert
while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

# Step 4: Display result
print(f"Binary of {decimal} is {binary}")
