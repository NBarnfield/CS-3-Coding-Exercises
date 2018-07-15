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
    for k, v in dictionary.items():
        t.append((v, k))
    t.sort(reverse=True)
    for v, k in t:
        new_t.append((k, v))
    return new_t


# Open and read file
file = open_file()
reader = csv.reader(file)
next(reader)

# Create a dictionary to store results
grantState = dict()
grantMoney = dict()
grantYear = dict()

# Loop through each line and calculate if the grant was given in Australia.
for line in reader:
    if line[8] == 'AUSTRALIA':
        state_of_grant = line[7]
        grantState[state_of_grant] = grantState.get(state_of_grant, 0) + 1
        sum_of_grant = line[4]
        grantMoney[sum_of_grant] = grantMoney.get(sum_of_grant, 0) + 1

        # Split the dates and take the year
        year_of_grant = line[6]
        year_of_grant = year_of_grant.split('-')
        year_of_grant = year_of_grant[2]
        grantYear[year_of_grant] = grantYear.get(year_of_grant, 0) + 1


print("The number of grants given to each state over the last 10 years is:")
sorted_grant_state = sort_values(grantState)
for key, value in sorted_grant_state:
    print(key, value)

print("\nThe top 10 most common value grants distributed were:")
sorted_grant_money = sort_values(grantMoney)
for key, value in sorted_grant_money[:10]:
    print(key, value)

print("\nThe year in which the most grants were given was:")
sorted_year_of_grant = sort_values(grantYear)
for key, value in sorted_year_of_grant:
    print(key, value)
