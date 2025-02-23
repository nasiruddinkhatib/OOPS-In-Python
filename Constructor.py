##**************************************What Is Constructor******************************************
#A constructor in Python is a special method used to initialize objects when they are created from a class. 
#In Python, the constructor method is named __init__(). It’s automatically called when a new instance of a class
#is created.

#Key points about constructors:
# The constructor sets up the initial state of the object by assigning values to its properties.
# It takes self as the first parameter, which refers to the instance being created.
# It can take additional parameters to initialize the object’s attributes.

##1] ************************Constructor Example Program*******************************
class Person:
    def __init__(self, name, position):  # Constructor with correct spelling (__init__)
        self.name = name  # Initialize name attribute
        self.position = position  # Initialize position attribute

    def info(self):  # Method to display information of parent class
        print(f"My name is {self.name} and my position is {self.position}")  # Access attributes using self

# Create an object of the Person class
a = Person("Armaan", "Developer")
b = Person("Nasir","Tester")
# Call the info method 
a.info()
b.info()
##Output : 
# My name is Armaan and my position is Developer  
# My name is Nasir and my position is Tester  

##2] ***********************Constructor Program by taking 4 arguments********************************
# class Employee:       
#     def __init__(self, name, age, salary, gender):
#         self.name = name      # Initialize the employee's name
#         self.age = age        # Initialize the employee's age
#         self.salary = salary  # Initialize the employee's salary
#         self.gender = gender  # Initialize the employee's gender

#     def show_employee_details(self):    # Properly indented method
#         print("Name of the employee:", self.name)
#         print("Age of the employee:", self.age)
#         print("Salary of the employee:", self.salary)
#         print("Gender of the employee:", self.gender)
#         print("-" * 30)          # Added a separator for readability for clearer output between employees.

# e1 = Employee("Nasir", 22, 50000, "Male") # Create an object of the Employee class
# e2 = Employee("khatib",21, 70000, "Male")

# e1.show_employee_details()            # Call the method to display employee details
# e2.show_employee_details()

## Output:
# Name of the employee: Nasir
# Age of the employee: 22
# Salary of the employee: 50000
# Gender of the employee: Male
# ------------------------------
# Name of the employee: Khatib
# Age of the employee: 21
# Salary of the employee: 70000
# Gender of the employee: Male
