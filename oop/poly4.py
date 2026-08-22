


class Test:
    def __init__(self):
        print("No Argument Constructor")
    def __init__(self,a):
        print("One Argument Constructor")
    def __init__(self,a,b):
        print("Two Argument Constructor")

#t = Test() Error
#t = Test(10) Error
t = Test(10,20)
