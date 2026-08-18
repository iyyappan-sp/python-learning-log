

from functools import reduce

prices = [250,900,1200,400,1800]
expensive = list(filter(lambda x : x > 1000, prices))

total = reduce (lambda a,b : a+b, expensive)
print(total)
