# >> Implementation of UML diagram
from abc import ABC, abstractmethod
# ---------------------------------
# Abstract class
class Abstract_Class(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    @abstractmethod
    def operation3(self):
        pass
    
    # Template Method => Defines algorithm with calling operation methods
    def templateMethod(self):
        print("[Order of operations]\n step1=>operation3()\n step2=>operation1()\n step3=>operation2()\n")
        self.operation3()
        self.operation1()
        self.operation2()

# ---------------------------------
# Concrete Classe
class Concrete_Class(Abstract_Class):

    def operation1(self):
        print("operation1 anjam shud")
    
    def operation2(self):
        print("operation2 anjam shud")

    def operation3(self):
        print("operation3 anjam shud")

# ---------------------------------
# Client
class Client:

    def action(self):
        self.concrete_class = Concrete_Class()
        self.concrete_class.templateMethod()

# Use
client = Client()
client.action()