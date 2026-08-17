



def get_numbers(n):
    for i in range(n):
        yield i

for num in get_numbers(5):
    print(num)
