# State
class MobileState:

    # class variables : for example : mobile.__class__.__name__
    name = 'state'
    allowed = []

    def switch(self, state): # state is a class : On, Off, Restart, Airplane
        if state.name in self.allowed:
            print("Current State:", self, "Change to => ", state.name)
            self.__class__ = state # class change to state 
        else:
            print("Current State:", self, "Change to => ", state.name, "it is not possible")
    
    def __str__(self):
        return self.name


# Concrete States => 1:Off, 2:On, 3:Restart, 4:Airplane
class Off(MobileState):
    name = "Off"
    allowed = ['On']

class On(MobileState):
    name = "On"
    allowed = ['Off', 'Restart', 'Airplane']

class Restart(MobileState):
    name = "Restart"
    allowed = ['On']

class Airplane(MobileState):
    name = "Airplane"
    allowed = ['On', 'Off', 'Restart']

# Context
class MobileContext():

    def __init__(self, model='SAMSUNG'):
        self.model = model
        self.state = Off() # first state

    def change(self, state):
        self.state.switch(state)


# Client:
if __name__ == "__main__":
    mobile = MobileContext()
    mobile.change(On)
    mobile.change(Off)
    mobile.change(On)
    mobile.change(Restart)
    mobile.change(On)
    mobile.change(Airplane)
