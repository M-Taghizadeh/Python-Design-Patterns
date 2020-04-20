from abc import ABC, abstractmethod

# -----------------------------------------------------------
# Abstract Factory => Interface
class CoffeFactory(ABC):
    
    @abstractmethod
    def create_CoffeWithoutMilk(self):
        pass
    
    @abstractmethod
    def create_CoffeWithMilk(self):
        pass

# -----------------------------------------------------------
# Concrete Factory 1:
class Italian_CoffeFactory(CoffeFactory):

    def create_CoffeWithoutMilk(self):
        return ItalianEspresso() # Our method work such as a creator object ==> return a class object

    def create_CoffeWithMilk(self):
        return ItalianCappucino() # Our method work such as a creator object ==> return a class object

# Concrete Factory 2:
class French_CoffeFactory(CoffeFactory):

    def create_CoffeWithoutMilk(self):
        return FrenchEspresso() # Our method work such as a creator object ==> return a class object

    def create_CoffeWithMilk(self):
        return FrenchCappucino() # Our method work such as a creator object ==> return a class object

# -----------------------------------------------------------
# Abstract Product 1:
class CoffeWithoutMilk(ABC):

    @abstractmethod
    def prepare(self, CoffeWithoutMilk):
        pass

# Abstract Product 2:
class CoffeWithMilk(ABC):

    @abstractmethod
    def serve(self, CoffeWithoutMilk):
        pass

# -----------------------------------------------------------
# Concrete Product 1:
class ItalianEspresso(CoffeWithoutMilk):
    
    def prepare(self):
        print("Prepare ", type(self).__name__)

# Concrete Product 2:
class ItalianCappucino(CoffeWithMilk):
    
    def serve(self, CoffeWithoutMilk):
        print(type(self).__name__, "is served with sheep's milk on ", type(CoffeWithoutMilk).__name__)

# Another Concrete Product 1:
class FrenchEspresso(CoffeWithoutMilk):
    
    def prepare(self):
        print("Prepare", type(self).__name__)

# Another Concrete Product 2:
class FrenchCappucino(CoffeWithMilk):
    
    def serve(self, CoffeWithoutMilk):
        print(type(self).__name__, "is served with cow's milk on ", type(CoffeWithoutMilk).__name__)

# -----------------------------------------------------------
# CLient => Using Factory :
class CoffeStore:

    def __init__(self):
        pass

    def makeCoffe(self):
        for factory in [Italian_CoffeFactory(), French_CoffeFactory()]:
            self.factory = factory 
            self.CoffeWithoutMilk = self.factory.create_CoffeWithoutMilk()
            self.CoffeWitMilk = self.factory.create_CoffeWithMilk()
            self.CoffeWithoutMilk.prepare()
            self.CoffeWitMilk.serve(self.CoffeWithoutMilk)

Coffe = CoffeStore()
Coffe.makeCoffe()