from abc import ABCMeta, abstractmethod

class Book(metaclass = ABCMeta):

    @abstractmethod
    def num_of_pages(self):
        pass

class Head_First_Python(Book):

    def num_of_pages(self):
        print("500")

class Python_CookBook(Book):

    def num_of_pages(self):
        print("300")

#Publication Factory
class PublicationFactory():

    def Book_publicator(self, object_type):
        return eval(object_type)().num_of_pages()

#Client code
if __name__ == '__main__':
    pf = PublicationFactory()
    book = input("che ketabi ro chap konam, Head_First_Python ya Python_CookBook?\n")
    pf.Book_publicator(book)                
