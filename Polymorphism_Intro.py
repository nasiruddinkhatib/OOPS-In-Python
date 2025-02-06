#Polymorphism means "many forms" and allows objects of different classes to be treated as objects of a common base class.
# It enables a single interface (method or operator) to work with different types of data or classes.
# 📌 Types of Polymorphism in Python:
# 1✔ Method Overriding (Runtime Polymorphism) – Child class redefines a method from the parent class.
# 2✔ Method Overloading (Compile-time Polymorphism - Not Natively Supported) – Multiple methods with
# the same name but different parameters (handled using default arguments).
# 3✔ Operator Overloading – Defining custom behavior for operators like +, -, etc.
#Code:
#1 Method Overriding
# class Animal:
#     def sound(self):
#         print("Animals make different sounds.")
#
# class Dog(Animal):  # Inheriting from Animal
#     def sound(self):  # Overriding method
#         print("Dog barks.")
#
# class Cat(Animal):  # Inheriting from Animal
#     def sound(self):  # Overriding method
#         print("Cat meows.")
#
# # Creating objects
# a = Animal()
# d = Dog()
# c = Cat()
#
# a.sound()  # ✅ Output: Animals make different sounds.
# d.sound()  # ✅ Output: Dog barks.
# c.sound()  # ✅ Output: Cat meows.
# So Here Method sound() is overridden in Dog and Cat, providing different implementations
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*********--*---************------***************----**********----*********---***

#2 Method Overloading  Python does not support true method overloading, but we can achieve it using default arguments or *args.
class Calculator:
    def add(self,*args):  # Default argument used to handle different cases
        total=0
        for i in args:
            total=total+i
        return total

# Creating an object
c1= Calculator()
print(c1.add(2, 3))      # ✅ Output: 5 (Uses 2 parameters)
print(c1.add(2, 3, 4))   # ✅ Output: 9 (Uses 3 parameters)
print(c1.add(1,2,3,4,5,6)) # By *args we (Uses multiple parameters)
#  Here, *args allows the method to accept either 2 or 3 arguments.

#**--*---**--**--**--**--**--**--**--**--**--**-*-*-*-*-*-***--**--***-**-***-**-***-**-***-**-***--***---***
#3 Operator Overloading
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __gt__(self, other):  # This __gt__it is possible to operator overloading
#         return self.age > other.age  # Returns True if self is older
#
# # Creating objects
# p1 = Person("Nasir", 22)
# p2 = Person("Aman", 20)
#
# # Comparing objects using `>`
# if p1 > p2:  # ✅ Calls __gt__()
#     print(f"{p1.name} will pay the bill.")
# else:
#     print(f"{p2.name} will pay the bill.")

