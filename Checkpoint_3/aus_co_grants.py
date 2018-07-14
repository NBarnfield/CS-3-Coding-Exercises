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


def sort_values(dictionary):
    t = list()
    for key, value in dictionary.items():
        t.append((value, key))
    t.sort(reverse=True)
    for value, key in t:
        print(key, value)


# Open and read file
file = open_file()
reader = csv.reader(file)

# Create a dictionary to store results
grantState = dict()

# Loop through each line and calculate if the grant was given in Australia.
for line in reader:
    # List comprehension is awesome!
    line = [x.lower().rstrip() for x in line if line[8]]
    if line[8] == 'australia':
        state_of_grant = line[7]
        grantState[state_of_grant] = grantState.get(state_of_grant, 0) + 1

# Construct a list to sort the grants
sort_values(grantState)
