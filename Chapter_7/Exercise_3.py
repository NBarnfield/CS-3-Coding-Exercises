file_name = input("Enter file name: ")

easter_egg = "na na boo boo"

if file_name == easter_egg:
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
else:
    pass

try:
    fhand = open(file_name, "r")

except:
    print("File name {} was invalid.".format(file_name))
    quit()

counter = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith("Subject:"):
        continue
    counter = counter + 1

print("The total number of subject lines in {} was {}.".format(file_name, counter))
