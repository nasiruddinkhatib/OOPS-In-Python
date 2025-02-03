#*-*-*-*-*-**************-Inheritance in Python-***********-*-*-*-*-*-*-*-*-**-**-*-*-*-*-*-*-*-
# Inheritance in Python is an Object-Oriented Programming
# (OOP) concept where a child class (derived class) inherits the attributes and methods
# of a parent class (base class). This allows code reuse and better organization.

#*-*-*-*-*-*-*-*-*Simple Example 1 Of Inheritance*-*-*-*-*-*-*-*
# Parent class
class Car:
    def show_work(self):  # Method in the parent class
        print("Cars are used for driving.")

# Child class inheriting from Car
class Toyota(Car):  # Toyota is a child class of Car
    def show_color(self):  # Method specific to Toyota
        print("Toyota cars are mostly red.")

# Creating an object of the child class Toyota
t1 = Toyota()
t1.show_work()  # ✅ Inherited method from Car class (Parent)
t1.show_color()  # ✅ Method defined in Toyota class (Child)

#*-*-*-*-*-*-*--*-*-*Example 2 of inheritance-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Parent class: Car
# class Car:
#     def __init__(self, work):  # Constructor to initialize 'work'
#         self.work = work  # Assign value to instance variable 'work'
#         # print("I love Driving")  # (Commented out, but could be used to display a message)
#
#     def show_work(self):  # Method to display the work of a car
#         print(f"The work of car is {self.work}")
#
# # Child class: Toyota (Inheriting from Car)
# class Toyota(Car):  # Toyota inherits from Car
#     def __init__(self, work, color):  # Constructor with additional 'color' attribute
#         super().__init__(work)  # Call the parent class constructor to initialize 'work'
#         self.color = color  # Assign value to instance variable 'color'
#
#     def show_color(self):  # Method specific to Toyota
#         print(f"My color is {self.color}")
#
# # Create an object of Toyota class
# t2 = Toyota("Driving", "Red")  # Toyota car with 'Driving' work and 'Red' color
# t2.show_work()   # ✅ Inherited method from Car class (Displays the work of the car)
# t2.show_color()  # ✅ Method from Toyota class (Displays the color of the Toyota car)



#*-*-*-*-*-*-*-*-*-*-*-*-*-Example:3-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# class Employee:  # Parent class
#     def __init__(self, name, id):  # Constructor to initialize name and id
#         self.name = name  # Store name
#         self.id = id      # Store id
#
#     def show_details(self):  # Method to display employee details
#         print(f"The name is {self.name}, and the ID is {self.id}")
#
# class Programmer(Employee):  # Child class inheriting from Employee
#     def __init__(self, name, id, language):  # Constructor with an additional 'language' attribute
#         super().__init__(name, id)  # Call parent class constructor to initialize name and id
#         self.language = language    # Store the programming language
#
#     def show_language(self):  # Method specific to Programmer class
#         print(f"The default language is {self.language}")
#
# e1 = Employee("Nasiruddin", 22)  ## Create an object of the Employee class Initialize an employee
# e1.show_details()  # Call method to display employee details
#
# # Create an object of the Programmer class
# e2 = Programmer("Musa", 20, "Python")  # Initialize a programmer
# e2.show_details()  # Call inherited method to display details
# e2.show_language()  # Call method specific to Programmer class
