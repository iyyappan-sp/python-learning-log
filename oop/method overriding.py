


class Parent:
    def property(self):
        print("Land + House + Car + Jewels")

    def source(self):
        print("Parent Source Salary")

class Child (Parent):
    def source(self):
        super().source()
        print("Child Source Online Trading")

c = Child()
c.property()
c.source()
