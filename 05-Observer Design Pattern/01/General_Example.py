# Subject => Object
class Subject:

    def __init__(self):
        self.__observers = [] # private observers list

    def register(self, observers):
        self.__observers.append(observers)

    def notifyEveryOne(self, *args): # args and kwarg for all things
        for observer in self.__observers:
            observer.notify(self, *args) # observer set notify 

# ----------------------------------------------
# Observers

class Observer1():

    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, args, "it has arrived from", type(subject).__name__)


class Observer2():

    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, args, "it has arrived from", type(subject).__name__)

# ----------------------------------------------
# Use 
subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)

# Event Services:
subject.notifyEveryOne("Warning", "Your registeration was successfuly.", "access token : 2385439857435")
