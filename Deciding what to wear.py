# Ask the user for the current temperature
temperature = int(input("Enter the current temperature in Celsius:56.7 "))

# Decide what Rohan should wear based on the temperature
if temperature >= 30:
    print("It's hot! Rohan should wear a light t-shirt and shorts.")
elif temperature >= 20:
    print("It's warm! Rohan can wear a t-shirt and jorts.")
elif temperature >= 10:
    print("It's cool. Rohan should wear a sweater .")
else:
    print("It's cold! Rohan needs a jacket a beanie and pullover.")



