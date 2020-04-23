from abc import ABC, abstractmethod
# --------------------------------------------
# Command Interface
class Order(ABC):

    @abstractmethod
    def execute(self):
        pass

# --------------------------------------------
# Concrete Commands => 1:BuyHouse, 2:SellHouse
class BuyHouse(Order):
    
    def __init__(self, house):
        self.house = house # house => Reciever

    # imp abs method 
    def execute(self):
        self.house.buy() # execute reciever => call action() in reciever


class SellHouse(Order):

    def __init__(self, house):
        self.house = house
    
    # imp abs method 
    def execute(self):
        self.house.sell()

# --------------------------------------------
# Reciever
class HouseTrade:

    def buy(self):
        print("You are buying this house.")
    
    def sell(self):
        print("You are selling this house")

# --------------------------------------------
# Invoker
class Agent:

    def __init__(self):
        self.__orderQueue = []
    
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute() # each order implemente execute() In its own way

# --------------------------------------------
# Client
if __name__ == "__main__":
    house1 = HouseTrade()
    house2 = HouseTrade()
    buyHouse = BuyHouse(house1)
    sellHouse = SellHouse(house2)

    # invoker
    agent = Agent()
    agent.placeOrder(buyHouse)
    agent.placeOrder(sellHouse)