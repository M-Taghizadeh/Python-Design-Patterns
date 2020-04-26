class Book:

    _shared_state = {"subject":"programming"} 

    def __init__(self):
        self.pages = 150
        self.__dict__ = self._shared_state # __dict__: private dict include states about objects of this class
        pass

book1 = Book()
book2 = Book()
book1.pages = 250 # shared with all objects

print("book obj 'book1': ", book1)
print("book obj 'book2': ", book2)
print("obj state 'book1': ", book1.__dict__)
print("obj state 'book2': ", book2.__dict__)
