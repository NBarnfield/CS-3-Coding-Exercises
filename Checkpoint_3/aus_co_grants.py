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


# Open and read file
ifile = open_file()
reader = csv.reader(ifile)

# Create a dictionary to store results
grant_state_dict = dict()

# Loop through each line and calculate if the grant was given in Australia.
for line in reader:
    # List comprehension is awesome!
    line = [x.lower().rstrip() for x in line]
    if line[9] == 'australia':
        print(line)
    # state_of_grant = line[8]

#     grant_state_dict[state_of_grant] = grant_state_dict.get(state_of_grant, 0) + 1
#
#
# for key in grant_state_dict:
#     print(key, grant_state_dict[key])
