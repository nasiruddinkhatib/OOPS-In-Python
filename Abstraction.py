#Abstraction
from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres = n
    @abstractmethod
    def start(self):    # there should be one method of pass to achieve abstraction start method will be common in all the child class
        pass
    def display(self):         # concrete method
        print("I am calling a Vehicle class ")

