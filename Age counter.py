try:
    age = int(input("Enter your age: "))
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
except ValueError:
    print("Invalid input! Please enter a whole number.")
from colorama import Fore, Style, init
init(autoreset=True)

while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print(Fore.RED + "Age can't be negative. Try again.")
            continue

        if age % 2 == 0:
            print(Fore.GREEN + f"Your age ({age}) is even.")
        else:
            print(Fore.BLUE + f"Your age ({age}) is odd.")

        # Fun age messages
        if age < 5:
            print("You're just a baby.")
        elif age < 13:
            print("Enjoy your childhood!")
        elif age < 20:
            print("Teenage years free! ")
        elif age < 60:
            print("Adulting in progress...")
        else:
            print("Golden years ")

        break  # Exit loop after valid input

    except ValueError:
        print(Fore.YELLOW + "Oops! Please enter a whole number.")
