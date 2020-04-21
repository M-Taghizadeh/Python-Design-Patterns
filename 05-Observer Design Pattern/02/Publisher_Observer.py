# Publisher and notification of newly published

# ----------------------------------------------
# Subject => as a interface
class Publisher:

    def __init__(self):
        self.__subscribers = [] # observers list => private
        self.__latestBooks = None

    def register(self, subscribers):
        self.__subscribers.append(subscribers)
    
    def un_register(self):
        return self.__subscribers.pop()

    def get_subscribers(self):
        return [type(s).__name__ for s in self.__subscribers]

    def add_book(self, books):
        self.__latestBooks = books

    def get_books(self):
        return "newly published", self.__latestBooks

    def notify_all_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

# ----------------------------------------------
# Observer => abs class with abs method => update() : notify method
from abc import ABC, abstractmethod

class Subscriber(ABC):

    @abstractmethod
    def update(self):
        pass

# ----------------------------------------------
# Concrete Observers => 1:SMS, 2:Email, ...

class SMS_Suscriber(Subscriber):

    def __init__(self, publisher):
        self.publisher = publisher 
        self.publisher.register(self) # Register itself

    def update(self):
        print(type(self).__name__, self.publisher.get_books())


class Email_Suscriber(Subscriber):

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self) # Register itself

    def update(self):
        print(type(self).__name__, self.publisher.get_books())


class AnyOther_Subscriber(Subscriber):

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self) # Register itself

    def update(self):
        print(type(self).__name__, self.publisher.get_books())

# ----------------------------------------------
# Client
if __name__ == "__main__":
    # 1-Create subject
    publisher = Publisher()

    # 2-Register all observers
    for Subscribers in [SMS_Suscriber, Email_Suscriber, AnyOther_Subscriber]:
        Subscribers(publisher)
    
    # 2-Register one observer (sms observers)
    # smsSub = SMS_Suscriber(publisher) 

    # 3-The event happened => one event or one update
    publisher.add_book("Advance Python") 

    # 4-Notify this event with update()
    publisher.notify_all_subscribers()
    
    # Use other methods (not very important)
    print("Subscribers : ", publisher.get_subscribers()) # get observers
    print("Unregistered : ", type(publisher.un_register()).__name__)
    print("Subscribers : ", publisher.get_subscribers()) # get observers

