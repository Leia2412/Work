        *
        **
        ***
        ****
        *****
        ******
# Ask user for number of rows
rows = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, rows + 1):
    # Print spaces first
    print("  " * (rows - i), end="")
    # Then print stars
    print("* " * i)
M