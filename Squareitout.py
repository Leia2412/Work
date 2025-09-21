def square_and_filter(start, end):
    squares = [i**2 for i in range(start, end+1)]
    even_squares = [num for num in squares if num % 2 == 0]
    odd_squares = [num for num in squares if num % 2 != 0]
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)

# Example usage
square_and_filter(1, 10)
def square_and_filter(start, end):
    # Create a list of numbers in the given range
    numbers = list(range(start, end + 1))
    print(f"Original numbers from {start} to {end}: {numbers}")

    # Calculate squares of each number
    squares = [i ** 2 for i in numbers]
    print(f"Squares of the numbers: {squares}")

    # Separate even and odd squares
    even_squares = [num for num in squares if num % 2 == 0]
    odd_squares = [num for num in squares if num % 2 != 0]

    # Display results
    print("\n--- Results ---")
    print(f"Even squares ({len(even_squares)} values): {even_squares}")
    print(f"Odd squares ({len(odd_squares)} values): {odd_squares}")

    # Optional: Return the lists if needed for further use
    return even_squares, odd_squares

# Interactive part
try:
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))

    if start_range > end_range:
        print("Start of range must be less than or equal to end of range.")
    else:
        square_and_filter(start_range, end_range)

except ValueError:
    print("Please enter valid integers for the range.")
