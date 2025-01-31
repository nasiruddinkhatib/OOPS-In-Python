#   *************Inheritance************
# Inheritance in Python is an Object-Oriented Programming
# (OOP) concept where a child class (derived class) inherits the attributes and methods
# of a parent class (base class). This allows code reuse and better organization.
class Employee:  # Parent class
    def __init__(self, name, id):  # Constructor to initialize name and id
        self.name = name  # Store name
        self.id = id      # Store id

    def show_details(self):  # Method to display employee details
        print(f"The name is {self.name}, and the ID is {self.id}")

class Programmer(Employee):  # Child class inheriting from Employee
    def __init__(self, name, id, language):  # Constructor with an additional 'language' attribute
        super().__init__(name, id)  # Call parent class constructor to initialize name and id
        self.language = language    # Store the programming language

    def show_language(self):  # Method specific to Programmer class
        print(f"The default language is {self.language}")

# Create an object of the Employee class
e1 = Employee("Nasiruddin", 22)  # Initialize an employee
e1.show_details()  # Call method to display employee details

# Create an object of the Programmer class
e2 = Programmer("Musa", 20, "Python")  # Initialize a programmer
e2.show_details()  # Call inherited method to display details
e2.show_language()  # Call method specific to Programmer class

