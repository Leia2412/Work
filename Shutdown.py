def shutdown(user_input):
    if user_input == "Yes":
        print("Shutting down")
    elif user_input == "No":
        print("Abort shutdown")
    else:
        print("Sorry")
shutdown("Yes")  # Output: Shutting down
shutdown("No")   # Output: Abort shutdown
shutdown("Maybe")  # Output: Sorry
user_input = input("Do you want to shut down the system? (Yes/No): ")
shutdown(user_input)
def shutdown(user_input):
    user_input = user_input.lower()
    if user_input == "yes":
        print("Shutting down")
    elif user_input == "no":
        print("Abort shutdown")
    else:
        print("Sorry")
