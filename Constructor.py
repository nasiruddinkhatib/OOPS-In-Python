#1]******Constructor Code********
class Person:
    def __init__(self, name, position):  # Constructor with correct spelling (__init__)
        self.name = name  # Initialize name attribute
        self.position = position  # Initialize position attribute

    def info(self):  # Method to display information of parent class
        print(f"My name is {self.name} and my position is {self.position}")  # Access attributes using self

# Create an object of the Person class
a = Person("Nasir", "Developer")
b = Person("Adil","Tester")
# Call the info method
a.info()
b.info()


# 2]*****Constructor Code by taking 4 arguments*************************

# class Employee:
#     def __init__(self, name, age, salary, gender):
#         self.name = name      # Initialize the employee's name
#         self.age = age        # Initialize the employee's age
#         self.salary = salary  # Initialize the employee's salary
#         self.gender = gender  # Initialize the employee's gender
#
#     def show_employee_details(self):  # Properly indented method
#         print("Name of the employee:", self.name)
#         print("Age of the employee:", self.age)
#         print("Salary of the employee:", self.salary)
#         print("Gender of the employee:", self.gender)
#
#
#
# # Create an object of the Employee class
# e1 = Employee("Nasir", 22, 50000, "Male")
# e2 = Employee("khatib",21,70000,"Male")
#
# # Call the method to display employee details
# e1.show_employee_details()
# e2.show_employee_details()



