# ASCII Value Checker 
character = input("Enter a character: ")
ascii_value = ord(character)
print("The ASCII value of", character, "is", ascii_value)
characters = input("Enter characters: ")
for char in characters:
    print(f"The ASCII value of '{char}' is {ord(char)}")
import string

if character in string.ascii_letters:
    category = "Letter"
elif character in string.digits:
    category = "Digit"
elif character in string.punctuation:
    category = "Symbol"
else:
    category = "Other"

print(f"The ASCII value of '{character}' is {ascii_value}. It is a {category}.")
