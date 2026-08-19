# Setter and Getter Methods

class Product:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
p = Product()
p.setName("Iphone 15")
print("Product Name is: ",p.getName())
