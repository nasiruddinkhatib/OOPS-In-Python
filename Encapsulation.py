#Encapsulation is one of the four main pillars of Object-Oriented Programming (OOP)
# (along  with Abstraction, Inheritance, and Polymorphism).
# Encapsulation in Python : Restricting direct access to attributes & methods
#Encapsulation restricts access to certain attributes or methods to protect the data and enforce controlled access.
# It refers to the bundling of data (variables) and methods (functions)
# into a single unit (class) and restricting direct access to some of the object's details.
# 📌 Key Features of Encapsulation:
# ✔ Restricts direct access to variables.
# ✔ Prevents accidental modification of important data.
# ✔ Provides controlled access via getter and setter methods.
#Examples code:
#**************----------****************-----------***********------------*****************---------**********
#Example:Using Getter and Setters method
class Student:  # Defining the Student class
    def __init__(self):  # Constructor method
        self.__name = ""  # Private attribute (indicated by double underscore)

    # Getter method to retrieve the value of __name
    def getname(self):
        return self.__name

    # Setter method to update the value of __name
    def setname(self, Work):
        self.__name = Work  # Assigns the new value to __name
# Creating an instance of the Student class
obj = Student()
obj.setname("It is a encapsulation using Getter and Setter to access private variable ") #Setting the name attribute using the setter method
name = obj.getname()  # Retrieving the name attribute using the getter method
print(name)
# Output:It is a encapsulation using Getter and Setter to access private variable

#***********************-------------------********************-----------------**********---****---***--
##Example 1
# class Person:
#     # Constructor to initialize private attributes
#     def __init__(self, name, age):
#         self.__name = name  # Private attribute (cannot be accessed directly outside the class)
#         self.__age = age    # Private attribute

#     # Public method to access private attributes
#     def display_info(self):
#         print(f"The person's name is {self.__name} and age is {self.__age}")

# # Creating an object (instance) of the Person class
# p1 = Person("Nasir", 24)

# Accessing private attributes via a public method
# p1.display_info()  # Output: The person's name is Nasir and age is 24

# Trying to access private attributes directly will result in an AttributeError
# print(p1.__name)  # Uncommenting this will cause an error
# print(p1.__age)   # Uncommenting this will cause an error

#****-***---**--**--**--**--**Another Method to access to Private method is by making class *-*-*-*-*-*-**-*-*-*
## Example 2
# class Person:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     def __display_info(self):   #Private method (cannot be accessed directly outside the class)
#         print(f"the person name is {self.__name} and age is {self.__age}")
#
#     def display_private_data(self):  #Public method to access private data With the help of this function we had access our Private data
#         self.__display_info()
#
# p1=Person("nasir",24)
# #p1.display_private_data() # Allowed (indirect access to private method)

#****----*******---------**********----------*********-------*******----------********---------*******----***--***
##Example 3
# class Student:
#     def __init__(self, name, grade, percentage):
#         self.name = name
#         self.grade = grade
#         self.__percentage = percentage  # Private attribute (hidden)
#
#     def get_percentage(self):  # Public method to access the private attribute
#         return self.__percentage
#
# # Creating a student object
# student1 = Student("Madhav", 10, 98)
#
# # Accessing the private attribute using the public method
# print(f"{student1.name}'s percentage is {student1.get_percentage()}%.")
# # print(student1.__percentage)  # This will raise an AttributeError



#*****--------**********---------************----------**********----------*********---------*********----------******---********
#Example 4
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number  # Public attribute
#         self.__balance = balance  # Private attribute (Encapsulation)

#     def deposit(self, amount):
#         """Public method to add money"""
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         """Public method to withdraw money"""
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.__balance}")
#         else:
#             print("Invalid withdrawal amount.")

#     def get_balance(self):
#         """Public method to check balance"""
#         return self.__balance  # Encapsulated access to private variable

# # Creating an object of BankAccount
# acc1 = BankAccount("1234567890", 5000)

# acc1.deposit(1000)  # ✅ Deposited 1000. New balance: 6000
# acc1.withdraw(2000)  # ✅ Withdrew 2000. New balance: 4000

# print(acc1.get_balance())  # ✅ Output: 4000
# #print(acc1.__balance)  # ❌ ERROR! Cannot access private variable directly
