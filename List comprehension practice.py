# Task 1: Odd Numbers Processing
user_input = int(input("Enter a number: "))

# List of all odd numbers below the input
odd_numbers = [x for x in range(user_input) if x % 2 != 0]
print("Odd numbers:", odd_numbers)

# Squared odd numbers
squared_odds = [x**2 for x in odd_numbers]
print("Squared odd numbers:", squared_odds)

# Filtered odd numbers greater than 10
filtered_odds = [x for x in odd_numbers if x > 10]
print("Odd numbers > 10:", filtered_odds)

# Even numbers for bonus
even_numbers = [x for x in range(user_input) if x % 2 == 0]
print("Even numbers:", even_numbers)

# Merged and sorted list
merged_sorted = sorted(odd_numbers + even_numbers)
print("Merged and sorted list:", merged_sorted)

# Task 2: Fruit List Transformation
fruits = ["apple", "banana", "cherry", "kiwi", "watermelon", "grape"]

# Capitalize each fruit
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:", capitalized_fruits)

# Fruits with more than 5 letters
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print("Fruits with >5 letters:", long_fruits)

# Reverse each fruit name
reversed_fruits = [fruit[::-1] for fruit in fruits]
print("Reversed fruit names:", reversed_fruits)


