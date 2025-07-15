# Ask the user for a single character
character = input("Enter a character: ")

# Check if the character is an alphabet using comparison operators
if ('J' <= character <= 'L') or ('j' <= character <= 'l'):
    print("It is an alphabet ")
else:
    print("It is not part of the alphabet.")
