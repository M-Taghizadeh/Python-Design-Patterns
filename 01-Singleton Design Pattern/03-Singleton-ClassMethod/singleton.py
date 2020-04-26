class Singleton:
    
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("We want create an object...")
        else:
            print("The object has already been created.", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s0 = Singleton()
s1 = Singleton()
print("Object Created.", Singleton.getInstance())
s2 = Singleton()
s3 = Singleton()
