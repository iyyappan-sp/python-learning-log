


with open("input_file.csv", "r") as file:
    lines = file.readline()
    for line in lines[1:]:   #skip header
        columns = line.strip().split(",")   #columns[0],columns[1],...
        print(columns[2])   #colimn of age
