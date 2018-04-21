# Program name: parrot_trouble.py
# We have a loud talking parrot. The "hour" input is the current hour time
# in the range 0..23. We are in trouble if the parrot is talking
#(input True if talking and False if not) and the hour is before 7 or after 20.
#Return True if we are in trouble.
# Make sure all test cases below will pass.
# parrot_trouble(talking, hour)


def current_hour(time):
    """"Return a True/False computation of hour."""
    if 7 > time < 20:
        return True
    elif 7 < time > 20:
        return False
    else:
        print("That is not a valid answer.")
        exit()


def parrot_talking(noise):
    """Request user input to determine if the parrot is speaking or not. Return a True or False response."""
    if noise == 'y':
        return True
    elif noise == 'n':
        return False
    else:
        print("That is not a valid answer.")
        exit()


def parrot_trouble(noise, time):
    """Take two variables and determine if we are in trouble or not!"""
    if noise is True and time is True:
        print("We could be in for some drama!")
    elif noise is True and time is False:
        print("Who knew that this would happen...")
    elif noise is False and time is False:
        print("We're all clear!!")
    else:
        print("Quiet...perfect.")


# Ask user for the current hour
try:
    hour = float(input("What is the hour in 24 hour time (0-23)? "))
    current_hour(hour)
except:
    print("There appears to be an error with the current_hour function.")
    exit()

# Ask user if the parrot is talking
try:
    talking = input("Is the parrot talking (y/n)? ")
    parrot_talking(talking)
except:
    print("There appears to be an error with the parrot_talking function.")
    exit()

# Compute the result of our scenario
try:
    parrot_trouble(talking, hour)
except:
    print("There appears to be an error with the parrot_trouble function.")
    exit()

