



class Test:
    def Sum(self, a = None, b = None, c = None):
        if a!=None and b!=None and c!=None:
            print("The Sum of Three no's:",a+b+c)
        elif a!=None and b!=None:
            print("The Sum of Two no's:",a+b)
        else:
            print("Please Provide 2 or 3 Values")

t = Test()
t.Sum(10,20,30)
t.Sum(20,30)
t.Sum(40)
