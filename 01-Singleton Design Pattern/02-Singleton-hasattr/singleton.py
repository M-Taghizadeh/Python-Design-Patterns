class Singleton():
    def __new__(cls): # class method that return a instance object
        if not hasattr(cls, 'instance'): # is a special python method
            cls.instance = super().__new__(cls)
        return cls.instance
s1 = Singleton()
print("obj created ", s1)
s2 = Singleton()
print("obj created ", s2)


# kind of methods in classes: 
# 1:class method : get class and return a instance for that class
    # hasattr(cls)
    # __new__(cls)
    # __cal__(cls)

# 2:object method : get object and not return any things just for define or initialization of variabls and attrs 
    # __init__(self)