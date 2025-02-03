#**-**-**-**-**-**-Multilevel Inheritance-**-**-**-**-**-**
#Multilevel Inheritance in Python
# Multilevel Inheritance is a type of inheritance
# where a class inherits from another child class, forming a chain of inheritance.
# The child class (Level 1) inherits from the parent class (Level 0).
# Then, a sub-child class (Level 2) inherits from the child class, creating a hierarchy.
#*-*-*-*-*-*******-Code For Multilevel Inheritance-*-**-*-*-*-*-*-*-*********
class Person:                  # Parent class: Person
    def __init__(self, name):  # Constructor to initialize name
        self.name = name
        print("This is name from Person class")

    def show_name(self):  # Method to display name
        print(f"Name: {self.name}")

class Employee(Person):            # Child class: Employee (Inheriting from Person)
    def __init__(self, name, id):  # Constructor to initialize name and id
        super().__init__(name)  # Call parent class constructor
        self.id = id

    def show_employee(self):  # Method to display employee ID
        print(f"Employee ID: {self.id}")

# Grandchild class: Manager (Inheriting from Employee)
class Manager(Employee):
    def __init__(self, name, id, department):  # Constructor to initialize name, id, and department
        super().__init__(name, id)  # Call Employee class constructor
        self.department = department

    def show_manager(self):  # Method to display department
        print(f"Department is {self.department}")

# Creating an object of the Manager class
m1 = Manager("Nasiruddin", "ID11", "Management")

m1.show_name()        # ✅ Calls method from Person class
m1.show_employee()    # ✅ Calls method from Employee class
m1.show_manager()     # ✅ Calls method from Manager class
