# __init__() and __call__() 
class A:
    
    def __init__(self):
        print ("init")

    def __call__(self):
        print("call")

a = A()
a()        

# __new__()
class B:

    def __new__(cls):
        return 20

b = B()
print(type(b))

print(b)        

     
