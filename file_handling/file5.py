#==========================
#tell()
#==========================

f = open('abcd.txt','r')
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())
f.close()

#==========================
#seek()
#==========================

f = open('abcd.txt','r')
f.seek(12)
print(f.tell())
