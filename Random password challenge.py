import random
import string

def generate_password(length):
    if length < 6:
        return "Password too short. Choose at least 6 characters."
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 12 and score == 4:
        return "Perfect"
    elif length >= 8 and score >= 3:
        return "Strong"
    else:
        return "Moderate"

# Main program
try:
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    print("\nGenerated password:", password)
    print("Password strength:", check_strength(password))
except ValueError:
    print("Please enter a valid number.")
