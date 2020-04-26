class Book():

    _shared_state = {}

    # We can pass any number of arguments
    def __new__(cls, *args, **kwargs): 
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

book1 = Book()
book2 = Book()
book3 = Book()
book1.pages = "200"
book1.color = "rangi"
book2.pages = "300"
book3.chapter = "20"


print("book obj 'book1': ", book1)
print("book obj 'book2': ", book2)
print("book obj 'book3': ", book3)
print("obj state 'book1': ", book1.__dict__)
print("obj state 'book2': ", book2.__dict__)
print("obj state 'book3': ", book3.__dict__)
