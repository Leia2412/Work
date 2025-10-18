import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

    def display_details(self):
        """Print the radius, area, and perimeter of the circle."""
        print(f"\nCircle Details:")
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area():.2f}")
        print(f"Perimeter: {self.perimeter():.2f}")

def get_radius_input():
    """Prompt the user for a valid radius and return it."""
    while True:
        try:
            radius_input = float(input)