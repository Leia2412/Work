# Power Calculator using for loop

# Step 1: Get input from the user
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Step 2: Initialize result
result = 1

# Step 3: Use a for loop to calculate power
for _ in range(exponent):
    result *= base

# Step 4: Display the result
print(f"{base} raised to the power of {exponent} is {result}")
