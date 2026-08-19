
class Animal:
     legs = 4

     @classmethod
     def display(cls,name):
         print("{} has {} legs".format(name,cls.legs))

Animal.display("Cow")
Animal.display("Dog")
Animal.display("Goat")
