from singleton_logger import SingletonObject

obj1 = SingletonObject()
obj1.file_name = "log1.txt"
obj1.critical("in payame critical hast")
print("print obj1: ", obj1)

obj2 = SingletonObject()
obj2.file_name = "log2.txt"
obj2.warning("in payame warning hast")
print("print obj1:", obj1)
print("print obj2:", obj2)