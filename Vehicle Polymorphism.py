class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "Diesel"

    def max_speed(self):
        return "300 km/h"

# Polymorphism in action
def car_details(car):
    print(f"Fuel Type: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()}")

# Create objects
bmw_car = BMW()
ferrari_car = Ferrari()

# Use the same function for both
car_details(bmw_car)
print("---")
car_details(ferrari_car)
