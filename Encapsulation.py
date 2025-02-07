class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def display_info(self):
        print(f"the person name is {self.__name} and age is {self.__age}")

    # def display_private_data(self):   # With the help of this function we had access our Private data
    #     self.__display_info()

p1=Person("nasir",24)
#p1.display_private_data()
p1.display_info()


# Another Method to access to Private method is by making class *-*-*-*-*-*-**-*-*-*
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