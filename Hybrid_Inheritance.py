#*-*-*-*-*-*-*-*-*-*-*-*-*-*-Hybrid-Inheritance-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# Hybrid Inheritance is a combination of two or more types of inheritance in a single program.
# It can include single, multiple, multilevel, or hierarchical inheritance, depending on the complexity of the class relationships.
# meaning it gets access to all methods from its parent classes.
#📌 Key Characteristics of Hybrid Inheritance:
# ✔ Combines different types of inheritance into one structure.
# ✔ Provides maximum code reusability.
# ✔ Can become complex, so method resolution order (MRO) is important.

# Parent class
class Vehicle:
    def show_vehicle(self):
        print("This is a vehicle.")

# First Child class (inherits from Vehicle)
class Car(Vehicle):
    def show_car(self):
        print("This is a car.")

# Second Child class (inherits from Vehicle)
class Bike(Vehicle):
    def show_bike(self):
        print("This is a bike.")

# Grandchild class (inherits from both Car and Bike - Multiple Inheritance)
class Hybrid(Car, Bike):
    def show_hybrid(self):
        print("This is a hybrid vehicle, which can be both a car and a bike.")

h1 = Hybrid()

h1.show_vehicle()  # ✅ Inherited from Vehicle
h1.show_car()      # ✅ Inherited from Car
h1.show_bike()     # ✅ Inherited from Bike
h1.show_hybrid()   # ✅ Defined in Hybrid

#Output
#This is a vehicle.
# This is a car.
# This is a bike.
# This is a hybrid vehicle, which can be both a car and a bike.
#********---********---*****---*****---*****---*****----*****--**--**--**--**
#Example2
# Base class
class Employee:
    def __init__(self, name):
        self.name = name

    def show_employee(self):
        print(f"Employee Name: {self.name}")

# First Level Child (inherits from Employee)
class Manager(Employee):
    def show_manager(self):
        print(f"{self.name} is a Manager.")

# Another First Level Child (inherits from Employee)
class Developer(Employee):
    def show_developer(self):
        print(f"{self.name} is a Developer.")

# Second Level Child (inherits from both Manager and Developer - Multiple Inheritance)
class TeamLead(Manager, Developer):
    def show_team_lead(self):
        print(f"{self.name} is a Team Lead, managing projects and coding.")


tl = TeamLead("Nasiruddin")

tl.show_employee()   # ✅ Inherited from Employee
tl.show_manager()    # ✅ Inherited from Manager
tl.show_developer()  # ✅ Inherited from Developer
tl.show_team_lead()  # ✅ Defined in TeamLead

# Output:
# Employee Name: Nasiruddin
# Nasiruddin is a Manager.
# Nasiruddin is a Developer.
# Nasiruddin is a Team Lead, managing projects and coding.

