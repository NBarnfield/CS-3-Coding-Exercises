# Exercise 1:
#
# Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
#
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.


def chop(list):
    list.pop()
    list.remove[0]
    return None


def middle(truncated_list):




# Create a list
num_list = list()

# Create a while loop to accept floats and integers and store them in a list. If invalid data is entered use except.
while True:
    try:
        inp = input("Please enter an integer or float: ")
        if inp == 'done': break
        value = float(inp)
        numlist.append(value)

    except ValueError:
        print("That is not a valid entry - please enter an integer or float.")

