


from abc import *

class Printer(ABC):     # Interface

    @abstractmethod
    def printit(self,text):
        pass

    def disconnect(self):
        pass

class EPSON (Printer):      #Concrete class / Normal class

    def printit(self,text):
        print("Printing from EPSON Printer...")
        print(text)

    def disconnect(self):
        print("Printing Completed on EPSON Printer...")

class HP (Printer):      #Concrete class / Normal class

    def printit(self,text):
        print("Printing from HP Printer...")
        print(text)

    def disconnect(self):
        print("Printing Completed on HP Printer...")

with open('config.txt','r') as f:
    pname=f.readline()
classname=globals()[pname]
x=classname()
x.printit("This data has to print...")
x.disconnect()
