# Parent - Child
# Super - Sub
# Base - Derived

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Student Name: ",self.name)
        print("Student Age: ",self.age)

class Student (Person):

    def __init__(self,name,age,rollno,mark):
        super(). __init__(name,age)
        self.rollno = rollno
        self.mark = mark

    def display(self):
        super().display()
        print("Student Roll Number:",self.rollno)
        print("Student Mark:",self.mark)

s = Student("Iyyappan",28,101,75)
s.display()
