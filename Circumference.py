def calculate_circumference(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference

# Example usage
r = float(input("Enter the radius of the circle: "))
result = calculate_circumference(r)
print(f"The circumference of the circle is: {result}")
def get_valid_radius():
    while True:
        try:
            radius = float(input("Enter a positive radius: "))
            if radius > 0:
                return radius
            else:
                print("Radius must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")
