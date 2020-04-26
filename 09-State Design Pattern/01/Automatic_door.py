from abc import ABC, abstractmethod

# State
class State(ABC):

    @abstractmethod
    def action(self):
        pass 


# Concrete States: 1:Open_State, 2:Close_State
class Open_State(State):

    def action(self):
        print("The door closed.")


class Close_State(State):

    def action(self):
        print("The door opened.")


# Context
class Door_Context(State):

    def __init__(self):
        self.state = None
    
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def action(self):
        self.state.action()

# Client => Use
context = Door_Context()
open_state = Open_State()
close_state = Close_State()
context.set_state(open_state)
context.action()
