

class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def display(self):
        print("Hi : ",self.name)
        print("Your Mark is : ",self.mark)
    def grade(self):
        if self.mark >= 70:
            print("Excellent")
        elif self.mark >= 50 and self.mark < 70:
            print("Good")
        elif self.mark > 35 and self.mark < 50:
            print("Fair")
        else:
            print("Poor")
n = int(input("Enter the Number of Students: "))
for i in range(n):
    name = input("Enter Student Name: ")
    mark = int(input("Enter Student Mark: "))
    s = Student(name,mark)
    s.display()
    s.grade()
    print()
