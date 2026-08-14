def add(*n):
    total = 0
    for i in n:
        total = total+i
    print("The Sum is",total)

add()
add(1,2)
add(10,20)
add(10,20,30,40,50)
