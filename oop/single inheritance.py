# Single Inheritance

class Parent:
    def m1(self):
        print("parent instance method")

class Child (Parent):
    def m2(self):
        print("child instance method")

c = Child()
c.m1()
c.m2()
