# Function to calculate the change to be returned
def calculate_change(bill_amount, paid_amount):
    """
    This function takes the bill amount and the amount paid by the customer,
    then calculates and returns the change to be given back.
    """
    return paid_amount - bill_amount

# Welcome message
print("Welcome to the Change Calculator!")

# Asking the user for input
try:
    bill_amount = float(input("Enter the total bill amount: $"))
    paid_amount = float(input("Enter the amount paid by the customer: $"))

    # Check if paid amount is sufficient
    if paid_amount < bill_amount:
        print("Error: Paid amount is less than the bill amount. Please check the values.")
    else:
        # Calculate the change
        change = calculate_change(bill_amount, paid_amount)

        # Display the result
        print(f"\nBill Amount: ${bill_amount:.2f}")
        print(f"Paid Amount: ${paid_amount:.2f}")
        print(f"Change to return: ${change:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for the bill and paid amount.")
