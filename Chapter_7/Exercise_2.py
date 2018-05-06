file_name = input("Enter file name: ")

try:
    fhand = open(file_name, "r")
except:
    print("File name {} was invalid.".format(file_name))
    quit()


counter = 0
total = 0
average = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    counter = counter + 1
    total = total + float(line[21:])
    print(line)

average = total/counter

print("The total occurrences of X-DSPAM-Confidence: in {} was {}, the total sum was {}, and the average was {}".format(file_name, counter, total, average))

