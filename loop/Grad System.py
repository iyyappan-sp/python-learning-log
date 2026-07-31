mark = int(input("Enter Your Mark"))
if mark >= 80 and mark <=100:
    print("Excellent")
elif mark >= 60 and mark <80:
    print("Good")
elif mark >=40 and mark <60:
    print("Fair")
elif mark >=0 and mark <40:
    print("Poor")
else:
    print("Invalid Value")
