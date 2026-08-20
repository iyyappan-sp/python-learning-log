

class Parent():
    a = 123
    def m1(self):
        print("Hello from parent instance method")
    @classmethod
    def m2(cls):
        print("Hello from parent class method")
    @staticmethod
    def m3():
        print("Hello from parent class method")

class Child(Parent):
    b=456
    def m11(self):
        print("Hello from child instance method")

c = Child()
c.m1()
c.m2()
c.m3()
c.m11()
print(c.a)
print(c.b)
