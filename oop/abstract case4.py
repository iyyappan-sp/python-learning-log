


from abc import *

class Vehicle(ABC):

    @abstractmethod
    def noofwheels(self):
        pass

class Bus (Vehicle):
    def noofwheels(self):
        return 6
class Car (Vehicle):
    def noofwheels(self):
        return 4
    
b = Bus()
print(b.noofwheels())

c = Car()
print(c.noofwheels())
