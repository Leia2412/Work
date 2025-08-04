# Ask the user to enter a number
num = int(input("Enter a number: "))

# Initialize digit counter
count = 0

# Use a while loop to count digits
while num != 0:
    num = num // 10
    count += 1

# Print the result
print("Total number of digits:", count)
