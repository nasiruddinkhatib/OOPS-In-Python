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

#****************----------------*********************------------------******************----------*****************
#Simple Example Using Class Method and static method 
class A:
    a = 10  # Class attribute 'a' initialized to 10
    b = 20  # Class attribute 'b' initialized to 20

    def __init__(self, c, d):
        self.c = c  # Instance attribute 'c' initialized with the value passed during object creation
        self.d = d  # Instance attribute 'd' initialized with the value passed during object creation

class B(A):  # Class 'B' inheriting from class 'A'
    a = 100  # Class attribute 'a' in 'B' overrides the 'a' from class 'A'

    @classmethod
    def display(cls):  # Class method 'display' that takes the class itself as the first argument 'cls'
        print(cls.a)  # Accessing the class attribute 'a' of the current class ('B' in this case)

class C(A):  # Class 'C' inheriting from class 'A'
    m = 3000  # Class attribute 'm' initialized to 3000

    @staticmethod
    def msg():  # Static method 'msg' that does not take 'self' or 'cls' as an argument
        print("heirarchical inheritance ")  # Prints a message

print(A.a, A.b)  # Accessing class attributes 'a' and 'b' directly using the class name 'A'
print(B.a, B.b)  # Accessing class attribute 'a' from class 'B' (which overrides 'A.a') and 'b' from class 'A' through inheritance
print(C.a, C.b, C.m)  # Accessing class attributes 'a' and 'b' from class 'A' through inheritance, and 'm' which is a class attribute of 'C'
#Output:
# 10 20
# 100 20
# 10 20 3000
