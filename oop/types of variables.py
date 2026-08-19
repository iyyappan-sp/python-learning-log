
# Inside Python Class 3 types of variables are allowed.

# 1. Instance Variables (Object Level Variables)
# 2. Static Variables (Class Level Variables)
# 3. Local Variables (Method Level Variables)


class Student:
    def __init__(self): # Constructor
        self.name = "Iyyappan"  #Instance Variable
        self.age = 28
        #print("Constructor Executed...")

    def display(self):  # Instance Method
        print("Name :",self.name)
        print("Age :",self.age)
        print("Instance Method Executed...")

s = Student()
s.display()
