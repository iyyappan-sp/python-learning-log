journy = {
    "custID":"RD123",
    "custName":"SIR",
    "pickup":"kodampaakkam",
    "drop":"vadapalani"
    }
print(journy)

journy.update({"Date":"07/02/2026"})

print(journy)


for k,v in journy.items():
    print(k,"---->",v)

journy.pop("Date")

print(journy)
