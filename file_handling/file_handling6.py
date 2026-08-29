
with open("input_file.csv","r") as infile, open("output_file.csv","w") as outfile:
    for line in infile:
        print(line.strip())
        outfile.write(line)
