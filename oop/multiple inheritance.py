#Multiple Inheritance

class Parent1:

    def m1(self):
        print("Parent1 Instance Method")

class Parent2:

    def m2(self):
        print("Parent2 Instanse Method")

class Child (Parent1, Parent2):

    def m3(self):
        print("Child Instace Method")

c = Child()
c.m1()
c.m2()
c.m3()
