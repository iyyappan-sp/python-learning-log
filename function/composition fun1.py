

def add(x):
    return x + 2

def multi(x):
    return x * 2

def composed(x):
    return add(multi(x))

print(composed(2))
