
class Book:

    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages+other.pages

b1 = Book(200)
b2 = Book(300)
b3 = Book(50)
print("Total Number of pages:",b1+b3)
