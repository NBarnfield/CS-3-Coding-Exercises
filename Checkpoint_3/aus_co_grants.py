import csv


def open_file():
    """Open file"""
    file = input("Enter file: ")
    try:
        fhand = open(file, 'r')
        return fhand
    except IOError:
        print("{} is not a valid file.".format(file))
        quit()


ifile = open_file()
reader = csv.reader(ifile)


for line in reader:
    if line[9] == 'AUSTRALIA' : continue
    grant_state_dict = dict()
    for state in line:
        grant_state_dict[State] = grant_state_dict.get(state, 0) + 1

print(grant_state_dict)