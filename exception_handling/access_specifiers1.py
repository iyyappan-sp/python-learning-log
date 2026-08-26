



# Acces Specifiers

#1. Public
#2. Protected
#3. Private


# Scenario's
#1. Same Class (Public, Protected, Private)
#2. Child Class (Public, Protected, Private)
#3. Other Class (Public, Protected, Private)



"""
# Access From Same Class

class Parent:
    def __init__(self):

        self.public_var = "I am Public Variable"
        self._protected_var = "I am Protected Variable"
        self.__private_var = "I am Private Variable"


    def access_from_same_class(self):

        print("Inside Parent Class")
        print("Public :",self.public_var)
        print("Protected :",self._protected_var)
        print("Private :",self.__private_var)

p = Parent()
print("\n -> Access from Same Class :")
p.access_from_same_class()

"""



""""
# Access From Child/Sub Class
class Parent:
    def __init__(self):

        self.public_var = "I am Public Variable"
        self._protected_var = "I am Protected Variable"
        self.__private_var = "I am Private Variable"


    def access_from_same_class(self):

        print("Inside Parent Class")
        print("Public :",self.public_var)
        print("Protected :",self._protected_var)
        print("Private :",self.__private_var)

class Child(Parent):
    
    def access_from_subclass(self):
        print("Inside Child/Sub Class")
        print("Public :",self.public_var)
        print("Protected :",self._protected_var)
        try:
            print("Private :",self.__private_var)
        except AttributeError as msg:
            print("Private: X Cannot acces ",msg)

p = Parent()
print("\n -> Access from Same Class :")
p.access_from_same_class()

c = Child()
print("\n -> Access from Child/Sub Class :")
c.access_from_subclass()

"""



# Access From Other Class
class Parent:
    def __init__(self):

        self.public_var = "I am Public Variable"
        self._protected_var = "I am Protected Variable"
        self.__private_var = "I am Private Variable"


    def access_from_same_class(self):

        print("Inside Parent Class")
        print("Public :",self.public_var)
        print("Protected :",self._protected_var)
        print("Private :",self.__private_var)

class Child(Parent):
    
    def access_from_subclass(self):
        print("Inside Child/Sub Class")
        print("Public :",self.public_var)
        print("Protected :",self._protected_var)
        try:
            print("Private :",self.__private_var)
        except AttributeError as msg:
            print("Private: X Cannot acces ",msg)

class Stranger:
    
    def access_from_other_class(self, obj):
        print("Inside Stranger Class")
        print("Public :",obj.public_var)
        print("Protected :",obj._protected_var)
        try:
            print("Private :",obj._Parent__private_var)
        except AttributeError:
            print("Private: X Cannot acces AttributeError")


p = Parent()
print("\n -> Access from Same Class :")
p.access_from_same_class()

c = Child()
print("\n -> Access from Child/Sub Class :")
c.access_from_subclass()

s = Stranger()
print("\n -> Access from Other Class :")
s.access_from_other_class(p)
