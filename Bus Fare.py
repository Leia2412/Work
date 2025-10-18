# Base class representing a generic vehicle
class Vehicle:
    def __init__(self, size):
        """
        Initialize the vehicle with its seating capacity.
        :param size: Number of seats in the vehicle
        """
        self.size = size

    def fare(self):
        """
        Calculate the base fare for the vehicle.
        :return: Base fare as size * 100
        """
        return self.size * 100

    def vehicle_info(self):
        """
        Display basic information about the vehicle.
        """
        print(f"Vehicle Type: {self.__class__.__name__}")
        print(f"Seating Capacity: {self.size}")
        print(f"Base Fare: {self.fare()}")

# Child class representing a bus, inheriting from Vehicle
class Bus(Vehicle):
    def __init__(self, size, route_name)
        """
        Initialize the bus with seating capacity and route name.
        :param size: Number of seats in the bus
        :param route_name: Name of the bus route
        """
        super().__init__(size)
        self.route_name = route_name

    def fare(self):
        """
        Calculate the total fare including maintenance charge.
        Maintenance charge