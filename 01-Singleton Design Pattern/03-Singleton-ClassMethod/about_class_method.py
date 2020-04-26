class Square:
    area = 50

    @classmethod
    def printarea(cls):
        print("Square Area : ", cls.area * cls.area)
        
Square.printarea()        
