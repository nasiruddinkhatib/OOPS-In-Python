#****----**********---****Class in python/OOP******----------*********-**--*-*
# To make Class we use keyword Class try to keep name of class in CamelCase so easily we'll know that it is a class 
# we call class using objectand also  we can create many object to call Class and
# by making class we call Functions/methods and Variable 
class Phone:  # Class Definition
    def make_call(self):  # Method to make a call
        print("Making a call")  # Prints a message indicating a call is being made

    def play_game(self):  # Method to play a game
        print("Playing Game")  # Prints a message indicating a game is being played

p1 = Phone()  # Object instantiation of the Phone class
p1.make_call()  # Calls the make_call method on the Phone object
p1.play_game()  # Calls the play_game method on the Phone object

