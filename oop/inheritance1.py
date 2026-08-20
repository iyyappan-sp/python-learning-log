

class Parent():
    def m1(self):
        print("Hello from parent method")

class Child(Parent):
    def m2(self):
        print("Hello from child method")

#c = Child()
#c.m1()
#c.m2()


p = Parent()
p.m1()
p.m2()
