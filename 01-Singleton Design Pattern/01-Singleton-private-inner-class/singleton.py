# Method 1 : Using private inner class 
class SingletonObject(object):
    class __SingletonObject(): # private inner class
        def __init__(self):
            self.val = None

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)

    instance = None

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()

        return SingletonObject.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

# use singleton class
obj1 = SingletonObject()
obj1.val = "Obj value 1"
print(obj1)

obj2 = SingletonObject()
obj2.val = "Obj value 2"
print(obj2)