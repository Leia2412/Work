import calendar

for month_num in range(1, 13):
    print(calendar.month_name[month_num])
import calendar
import time  # Optional: for adding delays

# Welcome message
print("Welcome to the Python Month Viewer")
print("This program uses Python's built-in calendar module to display all 12 months of the year.\n")

# Decorative header
print("=" * 40)
print(" List of Months in a Year")
print("=" * 40)

# Loop through and print each month
for month_num in range(1, 13):
    month_name = calendar.month_name[month_num]
    print(f"{month_num:>2}. {month_name}")
    time.sleep(0.3) 

# Summary message
print("\n All months have been displayed successfully!")
print("Thanks for using the Month Viewer.")

# Optional: Ask user to press Enter to exit
input