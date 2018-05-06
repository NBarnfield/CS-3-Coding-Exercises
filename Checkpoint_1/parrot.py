# We have a loud talking parrot.
# The "hour" input is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking(input True if talking and False if not) and the hour is before 7 or after 20.
# Return True if we are in trouble.
# parrot_trouble(talking, hour)


def parrot_talking(talking, hour):
    if talking is True and hour not in range(7, 20):
        return True
    else:
        return False


# Get user input on what the hour is in 24 hour time.
while True:
    try:
        current_time = int(input("What is the current hour (0 - 23)? "))
        if current_time in range(0, 23):
            break
        else:
            print("That is not a valid answer, please enter an integer or float between 0 - 23.")

    except ValueError:
        print("That is not a valid answer, please enter an integer or float between 0 - 23.")


# Get user input on whether or not the parrot is talking
while True:
    try:
        current_talking = input("Is the parrot talking (Y/N)? ")
        if current_talking == "Y":
            current_talking = True
            break

        elif current_talking == "N":
            current_talking = False
            break
        else:
            print("That is not a valid answer, please enter the character Y or N.")

    except ValueError:
        print("That is not a valid answer, please enter the character Y or N.")


# Confirm the values that were returned as a result of the user's input
print("So the time is {}, and the parrot is talking {}...".format(current_time, current_talking))

# Pass those values in as arguments to our user defined function
trouble = parrot_talking(current_talking, current_time)

# Based on the results of our function determine if we are in trouble!
if trouble is True:
    print("You better get out of there, it's going to get messy real soon!!")
else:
    print("Awesome, you can cruise on by!")
