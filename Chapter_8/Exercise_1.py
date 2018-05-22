# Exercise 1:
# Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.


def chop(everything):
    """Remove the first and last elements - return None"""
    everything.pop()
    del everything[0]
    return None


def middle(full_list):
    """create a new list and return only the middle values"""
    new_list = full_list
    new_list.pop()
    del new_list[0]
    return new_list

# Create a list
num_list = list()
counter = 0

# Create a while loop to accept floats and integers and store them in a list. If invalid data is entered use except.
while True:
    try:
        if len(num_list) < 5:
            print("Current numbers in list: {}".format(num_list))
            inp = input("You have entered a total of {} values. Please enter {} more integers or float values: ".format(counter, (5 - counter)))
            value = float(inp)
            num_list.append(value)
            counter = counter + 1

        else:
            break

    except ValueError:
        print("That is not a valid entry - please enter an integer or float.")

print("The final list of values is {}".format(num_list))

# Demonstrate the return values of the functions.
print(chop(num_list))
middle_list = middle(num_list)
print(middle_list)