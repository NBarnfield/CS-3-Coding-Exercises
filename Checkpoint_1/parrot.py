# Program name: parrot_trouble.py
# We have a loud talking parrot. The "hour" input is the current hour time
# in the range 0..23. We are in trouble if the parrot is talking
#(input True if talking and False if not) and the hour is before 7 or after 20.
#Return True if we are in trouble.
# Make sure all test cases below will pass.
# parrot_trouble(talking, hour)

def parrot_trouble(talking, hour):
    #TODO: nested if statements for the hours? Seperate if statements?
    if talking == True and hour < 7 or hour > 20:
        print("We could be in for some drama!")
    #elif talking == False and hour < 7 or hour > 20:
    #    print("Quiet....perfect.")
    else:
        print("Quiet...perfect.")

def current_hour():
    "Set loop to request user input for the current hour. If the response is not within the 24 hour range then loop."
    hour_counter = 0
    while hour_counter == 0:
        hour = float(input("What is the hour in 24 hour time (0-23)? "))
        if 0 < hour > 23:
            return hour
        else:
            print("That is not a valid response. Please enter an integer between 0 - 23.")

def parrot_talking(talking):
    "Request user input to determine if the parrot is speaking or not. Return a True or False response."
    talking_counter = 0
    while talking_counter == 0:
        is_talking = input("Is the parrot talking (y/n)? ")
        if is_talking == 'y':
            talking = True
            return talking
        elif is_talking == 'n':
            talking = False
            return talking
        else:
            print("That is not a valid response, please enter y or n.")

# Set variables
hour = 0
talking = 0

# Ask user for the current hour
try:
    hour =
    current_hour(hour)
except:
    print("There appears to be an error with the current_hour function.")
    exit()

# Ask user if the parrot is talking
try:
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