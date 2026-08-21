


class Test:
    def m1(self):
        print("No Arguments Method")
    def m1(self,a,b,c):
        print("Three Arguments Method")
    def m1(self,a,b):
        print("Two Arguments Method")
    
t = Test()
t.m1(10,2)
