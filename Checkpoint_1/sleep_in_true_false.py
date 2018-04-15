# Define a function that will take 2 parameters - weekday and vacation.
# This will take a true or false response from the user and then compute if they can sleep in or not.
def sleep_in(weekday, vacation):

    if weekday == 'True' and vacation == 'False':
        print("What a shame, you have to go to work...No sleep in for you.")

    elif weekday == 'True' and vacation == 'True':
        print("YAY you can sleep in!")

    elif weekday == 'False' and vacation == 'True':
        print("YAY you're on holiday - you can sleep in!")

    elif weekday == 'False' and vacation == 'False':
        print("YAY it's the weekend - you can sleep in!")

    else:
        print("Those aren't correct values! Please try again")

# Setting a condition for a while loop that will continue to ask the user for input until it is valid.
weekday_valid = True
while weekday_valid == True:
    weekday = input("Is it a weekday today (True/False)? ")
    if weekday not in ("True", "False"):
        print("That is not a valid response. Please enter True or False.")
        weekday_valid = True
    else:
        weekday_valid = False

# Setting a second condition and while loop to check our second criteria.
vacation_valid = True
while vacation_valid == True:
    vacation = input("Are you on vacation (True/False)? ")
    if vacation not in ("True", "False"):
        print("That is not a valid response. Please enter True or False.")
        vacation_valid = True
    else:
        vacation_valid = False

# Place the two variables into the sleep_in function to determine if you can sleep in or not.
sleep_in(weekday, vacation)
