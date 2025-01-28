class Phone:
    def set_color(self, color):
        self.color = color  # Sets the phone's color

    def set_cost(self, cost):
        self.cost = cost  # Sets the phone's cost

    def show_color(self):
        return self.color  # Returns the phone's color

    def show_cost(self):
        return self.cost  # Returns the phone's cost


# Create an object of the Phone class
p2 = Phone()

# Set the color and cost of the phone
p2.set_color("Red")
p2.set_cost(45000)

# Access and print the color and cost of the phone
print("Phone Color:", p2.show_color())  # Output: Phone Color: Red
print("Phone Cost:", p2.show_cost())    # Output: Phone Cost: 45000
