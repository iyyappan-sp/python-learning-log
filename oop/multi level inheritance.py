#Multi Level Inheritance

class GrandParent:

    def m1(self):
        print("Grandparent Instance Method")

class Parent (GrandParent):

    def m2(self):
        print("Parent Instance Method")

class Child(Parent):

    def m3(self):
        print("Child Instance Method")

c = Child()
c.m1()
c.m2()
c.m3()

p = Parent()
p.m1()
p.m2()

g = GrandParent()
g.m1()
