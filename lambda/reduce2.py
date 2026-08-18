



from functools import reduce

nums = [10,20,7,5,38]
maxi = reduce (lambda a,b : a if a > b else b,nums)
print(maxi)
