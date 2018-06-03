file_name = input("Enter file name: ")

try:
    fhand = open(file_name, "r")
except:
    print("File name {} was invalid.".format(file_name))
    quit()

for line in fhand:
    line = line.upper()
    print(line)
