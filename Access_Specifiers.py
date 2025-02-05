#*-*-*-*-*-*-*-*-*-*-Access Specifiers/Access Modifiers*-*-*-*-*-*-*-*-*-*-*-*-*
# In Object-Oriented Programming (OOP), Access Specifiers (also known as Access Modifiers)
# define the visibility of attributes and methods within a class.
# 📌 Types of Access Specifiers in Python:
#
# Access Specifier ||	Symbol	 ||      Description
# Public	      self.variable	       Accessible anywhere inside or outside the class.
# Protected	     _self.variable	       Can be accessed within the class and its child classes (by convention, not enforced).
# Private	     __self.variable	   Accessible only within the class (Name Mangling applies).

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-*Public Access Specifier*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
class Student:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print(f"Hi Myself {self.name} from Mumbai")
s1 = Student("nasir")
print(s1.name)
s1.display_name()

#*-*-*-*-*-*-*-*Protected Access Specifier*-*-*-*-*-*-*-*
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self._rollno=rollno     # protected
    def display_name(self):
        print(f"Hi Myself {self.name} from Mumbai  and roll is {self._rollno}")
s1 = Student("nasir",2)
s1.display_name()

#*-*-*-*-**-*-**Private Access Specifiers*-*-*-*-*-**-*-*-*-*-*-*-*-*-**-*-*-*-*
class Person:
    def __init__(self,name,age):
        self.__name=name  # Private
        self.__age=age    # private
    def display_info(self):
        print(f"the person name is {self.__name} and age is{self.__age} ")

person=Person("Nasiruddin",22)
#print(person.__name) # it will throw an error because you are calling it outside the class and private method doesn't allow this
#print(dir(person))  # Output Will come but only it show variable names
person.display_info()  # the person name is Nasiruddin and age is22
