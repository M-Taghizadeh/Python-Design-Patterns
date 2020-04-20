from abc import ABC, abstractmethod

# Subject Abs
class Pardakhtan(ABC):

    @abstractmethod
    def do_pay(self):
        pass 

# ---------------------------------------
# Real Subject:
class Bank(Pardakhtan):
    
    def __init__(self):
        self.card = None
        self.account = None
    
    # Private method
    def __getAcount(self):
        self.account = self.card
        return self.account

    # Private method
    def __mojoodiDashtan(self):
        print("Bank : Checking that account of [", self.__getAcount(), "] have enough money or not..")
        return False

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__mojoodiDashtan():
            print("Bank : Successfully paid.")
            return True
        else:
            print("Bank : Your money is not enough.")
            return False

# ---------------------------------------
# Proxy
class Card(Pardakhtan):

    def __init__(self):
        self.bank = Bank() # Initialize Real subject

    def do_pay(self):
        card = input("Enter your card number : ")
        self.bank.setCard(card)
        return self.bank.do_pay()

# ---------------------------------------
# Client:
class You:

    def __init__(self):
        print("You : I want to buy a product.")
        self.card = Card() # client request to proxy
        self.isPurchased = None

    def pardakht(self):
        self.isPurchased = self.card.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You : I bought the product.")
        else: 
            print("You : My money is not enough to buy.")

# Use 
you = You()
you.pardakht()
