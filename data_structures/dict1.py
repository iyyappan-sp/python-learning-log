d = {101:'Arun', 102:'Bala', 103:'Deva', 104:'Tom', 105:'Ram'}

print(d)

# insertion order is preserved

d.update({106:'SIR'})

print(d)


print(d[103])

for k,v in d.items():
    print(k,"--->",v)


d.pop(104)

print(d)
