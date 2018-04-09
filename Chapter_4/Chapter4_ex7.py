# We are going to ask the user for input of a score between 0-1.0 and then give them their grade based on that input.
def computegrade(score):
    if score >= 1.0:
        return ("That is impossible, but good on you for having immense self belief!")
    elif score >= 0.9:
        return ("You received an A grade!")
    elif score >= 0.8:
        return ("You received a B grade!")
    elif score >= 0.7:
        return ("You received a C grade!")
    elif score >= 0.6:
        return ("You received a D grade!")
    else:
        return ("You received an F grade!")


# Setting a variable of 0 for our score we can establish a while loop to accept a correct answer
score = 0

# Until an appropriate float or integer has been given the loop will continue to prompt the user for acceptable input.
while score == 0:
    try:
        score = float(
            input("You have just received your test back that was given a mark between 0 - 1.0, what was your score? "))
    except:
        print("That is not a valid float or integer.")

# This will then take the string that was returned and stored in the grade variable and print the corresponding statement.
print(computegrade(score))
