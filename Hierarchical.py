#***-***-***-***-***-Hierarchical Inheritance-***-***-***-***
#One 1 Parent Class Multiple Child Class and its inherits from parent class
#Hierarchical Inheritance is a type of inheritance where multiple child classes inherit from the same parent class.
# 📌 Key Characteristics:
# One parent class is shared by multiple child classes.
# Each child class can have its own unique methods and attributes.
# This promotes code reusability by
# allowing all child classes to share common attributes and methods from the parent class.

# Parent class
class Employee:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Employee Name: {self.name}")

# Child class 1
class Manager(Employee):  # Inherits from Employee
    def show_role(self):
        print(f"{self.name} is a Manager.")

# Child class 2
class Developer(Employee):  # Inherits from Employee
    def show_role(self):
        print(f"{self.name} is a Developer.")

m1 = Manager("Nasiruddin")    # Creating objects
d1 = Developer("Amit")

# Calling methods
m1.show_name()   # ✅ Inherited from Employee
m1.show_role()   # ✅ Specific to Manager

d1.show_name()   # ✅ Inherited from Employee
d1.show_role()   # ✅ Specific to Developer
