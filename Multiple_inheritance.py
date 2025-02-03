# What is Multiple Inheritance?
# Multiple inheritance is a feature in Python where a class can
# inherit attributes and methods from more than one parent class.
# This allows a child class to combine and extend the functionality of multiple parent classes.

# 1] ************Code of multiple inheritance**********************
# class Parent1:
#     def assign_string_one(self, str1):
#         self.str1 = str1  # Assign string to an instance variable
#
#     def show_string_one(self):  # Define this method at the correct level
#         return self.str1
#
# class Parent2:
#     def assign_string_two(self, str2):
#         self.str2 = str2  # Assign string to an instance variable
#
#     def show_string_two(self):  # Define this method at the correct level
#         return self.str2
#
#
# class Child(Parent1, Parent2):  # Child inherits from Parent1 and Parent2
#     def assign_string_three(self, str3):
#         self.str3 = str3  # Assign string to an instance variable
#
#     def show_string_three(self):  # Define this method at the correct level
#         return self.str3
#
#
# # Create an object of the Child class
# my_child = Child()
#
# # Assign strings using methods from parent and child classes
# my_child.assign_string_one("I am string of Parent 1.")
# my_child.assign_string_two("I am string of Parent 2.")
# my_child.assign_string_three("I am string of Child.")
#
# # Access and print the strings using their respective methods
# print(my_child.show_string_one())  # From Parent1
# print(my_child.show_string_two())  # From Parent2
# print(my_child.show_string_three())  # From Child



#2]***********-Same Program Using class name Person-*************
#Parent class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_details(self):
        print(f"Name is : {self.name} And Age:{self.age}")


# Parent class 2
class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

    def display_employee_details(self):
        print(f"Employee ID is : {self.id}, Salary: {self.salary}")


# Child class inheriting from both Class parent1(Person) and Parent2(Employee)
class Manager(Person, Employee):
    def __init__(self, name, age, id, salary, department):
        super().__init__(name, age)  # Calls Person's constructor
        Employee.__init__(self, id, salary)  # Calls Employee's constructor
        self.department = department


    def display_manager_details(self):
        # self.display_person_details()  # Reuse method from Person
        # self.display_employee_details()  # Reuse method from Employee
        print(f"Department is :{self.department}")  # Display department


# Creating an object of the Manager class
m1 = Manager("Nasiruddin", 30, "M123", 85000, "IT")

# Displaying details
m1.display_person_details()  #By Manage Object we Call Parent1 and parent2 methods this is call multiple inheritance
m1.display_employee_details()
m1.display_manager_details()

#Output: