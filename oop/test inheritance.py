


class Parent:
    x = 10

    def m1(self):
        print("Parent Instance Method")

class Child (Parent):
    x = 999
    
    def m2(self):
        print(super().x)
        print("Child Instance Method")

c = Child()
print(c.x)#999
print(Parent.x)#10
c.m2()
