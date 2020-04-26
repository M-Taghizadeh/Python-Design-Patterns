from abc import ABC, abstractmethod

class State(ABC):
    
    @abstractmethod
    def handling(self):
        pass


class Concrete_State1(State):

    def handling(self):
        print("Concrete_State1")


class Concrete_State2(State):

    def handling(self):
        print("Concrete_State2")


class Context(State):

    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state 

    def handling(self):
        self.state.handling()

# Client
# Use
context = Context()
state1 = Concrete_State1()
state2 = Concrete_State2()
context.set_state(state1)
context.handling()
context.set_state(state2)
context.handling()