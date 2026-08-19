

class Example:

    x = 10    #Static Variable

    def __init__(self):#Constructor
        self.a = 123
        self.b = 456

    def display(self):#Method
        print(self.a)
        print(self.b)
        print(Example.x)

e = Example()
Example.x = 999
e.display()
e1 = Example()
e1.a = 555
e1.display()
e2 = Example()
e2.display()

