


f = open("abcd.txt","w")
f.write("Welcome\n")
f.write("To Python\n")
f.write("rogramming")
print("File Update Done")
f.close()



f = open("abcd.txt","w")
l = ["Raman\n","Tom\n","Sam\n","Jerry"]
f.writelines(l)
print("File Update Success")
f.close()
