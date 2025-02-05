from Abstraction import Vehicle
class Bike(Vehicle):
    def __init__(self, n, color):
        super().__init__(n) # n is calling from vehicle class its is means tyres
        self.color = color  # Bike-specific attribute

    def start(self):
        print("Start with Kick")  # Implementing abstract method

    def display(self):
        print(f"{self.color} is the color of the bike.")

# Concrete class 2
class Scooty(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def start(self):
        print("Start with Self")  # Implementing abstract method

# Concrete class 3
class Car(Vehicle):
    def __init__(self, name, no_of_gears):
        super().__init__(name)
        self.no_of_gears = no_of_gears  # Initialize with given value

    def start(self):
        print("Start with Key")  # Implementing abstract method