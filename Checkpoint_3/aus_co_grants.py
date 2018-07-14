import csv


def open_file():
    """Open file"""
    user_file = input("Enter file: ")
    try:
        fhand = open(user_file, 'r')
        return fhand
    except IOError:
        print("{} is not a valid file.".format(file))
        quit()


def sort_values(dictionary):
    t = list()
    new_t = list()
    for key, value in dictionary.items():
        t.append((value, key))
    t.sort(reverse=True)
    for value, key in t:
        new_t.append((key, value))
        return new_t


def largest_in_dict(dictionary, key):
    most_common_value = None
    most_common_key = None
    for value in dictionary:
        if most_common_value is None or dictionary[key] > most_common_value:
            most_common_value = dictionary[key]
            most_common_key = value
    return most_common_value, most_common_key


# Open and read file
file = open_file()
reader = csv.reader(file)

# Create a dictionary to store results
grantState = dict()
grantMoney = dict()

# Loop through each line and calculate if the grant was given in Australia.
for line in reader:
    # List comprehension is awesome!
    line = [x.lower().rstrip() for x in line]
    if line[8] == 'australia':
        state_of_grant = line[7]
        grantState[state_of_grant] = grantState.get(state_of_grant, 0) + 1
        sum_of_grant = line[4]
        grantMoney[sum_of_grant] = grantMoney.get(sum_of_grant, 0) + 1


# Construct a list to sort the grants
print("The number of grants given to each state over the last 10 years is:\n")
print(sort_values(grantState))
print("\nThe most common value grant distributed was {}".format(largest_in_dict(grantMoney, sum_of_grant)))
