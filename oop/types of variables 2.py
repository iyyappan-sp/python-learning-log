# Static Variables

class Employee:
    
    age = 23    #Static Variable

    def display(self):
        print(Employee.age)

e = Employee()
e.display()
