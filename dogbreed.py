class Dog:
    """
    A class to represent a dog with breed and color traits.
    Includes methods to display information, bark, update color,
    and compare with another different dog.
    """

    # Class variable
    animal = "Dog"

    def __init__(self, breed, color):
        # Instance variables
        self.breed = breed
        self.color = color

    def display_info(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")

    def bark(self):
        print(f"{self.breed} says: Woof! Woof!")

    def update_color(self, new_color):
        print(f"Updating {self.breed}'s color from {self.color} to {new_color}")
        self.color = new_color

    def compare_dogs(self, other_dog):
        if self.breed == other_dog.breed:
            print(f"Both dogs are of the same breed: {self.breed}")
        else:
            print(f"{self.breed} and {other_dog.breed} are different breeds.")

# Creating two dog objects
dog1 = Dog("Corgi", "Black, Gold and White")
dog2 = Dog("Schnauzer", "Black")

# Displaying their details
dog1.display_info()
dog1.bark()
print()

dog2.display_info()
dog2.bark()
print()

# Comparing the two dogs
dog1.compare_dogs(dog2)

# Updating color of dog2
dog2.update_color("Salt and Pepper")
dog2.display_info()
