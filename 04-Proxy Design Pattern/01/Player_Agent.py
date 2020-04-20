class Player:

    def __init__(self):
        self.hascontract = False # by default player hase not contract
    
    def occupied(self):
        self.hascontract = True
        print(type(self).__name__, "dar hale hazer ba yek team gharardad darad")
    
    def available(self):
        self.hascontract = False
        print(type(self).__name__, "baraye in transfer azad ast")

    def get_status(self):
        return self.hascontract

# Proxey
class Agent:

    def work(self):
        self.player = Player()
        if self.player.get_status():
            self.player.occupied()
        else: 
            self.player.available()


if(__name__) == "__main__":
    a = Agent()
    a.work()

