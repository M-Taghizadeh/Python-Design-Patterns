from abc import ABC, abstractmethod

# Command => Abstract class
class Command(ABC):

    def __init__(self, reciever):
        self.reciever = reciever

    @abstractmethod
    def execute(self):
        pass


# Concrete Command
class Concrete_Command(Command):

    def __init__(self, reciever):
        self.reciever = reciever

    def execute(self):
        self.reciever.action() # Aggregation between Concrete_command and Reciever 


# Reciever : do action => action()
class Reciever:
    
    def action(self):
        print("Action")


# Invoker => invoke command => execute()
class Invoker:

    def command(self, com):
        self.com = com

    def execute(self):
        self.com.execute() # Aggregation between Invoker and Concrete_command


# Client
if __name__ == "__main__":
    # step 1 : create a reciever 
    reciever = Reciever()
    # step 2 : create a command
    command = Concrete_Command(reciever)
    # step 3 : invoking a command
    invoker = Invoker()
    invoker.command(command)
    # step 4 : execute a command 
    invoker.execute()