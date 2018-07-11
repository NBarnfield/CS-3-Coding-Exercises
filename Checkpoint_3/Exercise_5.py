def open_file():
    """Open file"""
    file = input("Enter file: ")
    try:
        fhand = open(file, 'r')
        return fhand
    except IOError:
        print("{} is not a valid file.".format(file))
        quit()


def sum_of_approvals(user_file):
    """Split lines and sum if item 2 == Central"""
    total_c_approvals = 0
    for line in user_file:
        line = line.split('|')
        if line[1] == "Central":
            total_c_approvals += int(line[2])
    return total_c_approvals


# Open the DPE_approvals.txt file, and report the cumulative total of 2016 approvals
approvals = open_file()
central = sum_of_approvals(approvals)
print("The cumulative total of approvals in 2016 for the NSW Central district was {}.".format(central))
