# Define a function that will take 2 parameters - weekday and vacation.
# This will take a true or false response from the user and then compute if they can sleep in or not.


def sleep_in(weekday, vacation):
    if weekday == 'True':
        if vacation == 'True':
            print("YAY you can sleep in!")
        else:
            print("What a shame, you have to go to work...No sleep in for you.")
    else:
        if vacation == 'True':
            print("YAY you're on holiday - you can sleep in!")
        else:
            print("YAY it's the weekend - you can sleep in!")


# Set a while loop that will continue to ask the user for input until it is valid.
def what_day():
    while True:
        day = input("Is it a weekday today (True/False)? ")
        if day not in ("True", "False"):
            print("That is not a valid response. Please enter True or False.")
        else:
            break

# Set a second while loop to check for our second criteria.
while True:
    holiday = input("Are you on vacation (True/False)? ")
    if holiday not in ("True", "False"):
        print("That is not a valid response. Please enter True or False.")
    else:
        break

# Place the two variables into the sleep_in function to determine if you can sleep in or not.
sleep_in(day, holiday)
