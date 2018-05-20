# Create a list
numlist = list()

# Create a while loop to accept floats and integers and store them in a list. If invalid data is entered use except.
while True:
    try:
        inp = input("Please enter an integer or float: ")
        if inp == 'done': break
        value = float(inp)
        numlist.append(value)

    except ValueError:
        print("That is not a valid entry - please enter an integer or float.")

try:
    # Set variables to contain the maximum and minimum numbers in the list.
    max_value = max(numlist)
    min_value = min(numlist)

    # print the full list of numbers and then print the highest and smallest value.
    print("The list of numbers entered was {}.".format(numlist))
    print("The maximum value entered was {}, and the minimum was {}.".format(max_value, min_value))

except:
    # If no value other than done was entered, wish them well and exit!
    print("Thank you. Have a great day!")
    #quit() - obviously uneccesary as at the end of the script, but useful if continuing.
