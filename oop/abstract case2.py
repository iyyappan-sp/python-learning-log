



from abc import *

class Test(ABC):
    def m1(self):
        print('Hello')

    @abstractmethod
    def m2(self):
        pass

t = Test()
t.m1
