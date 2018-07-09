# We have a loud talking parrot.
# The "hour" input is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking(input True if talking and False if not) and the hour is before 7 or after 20.
# Return True if we are in trouble.
# parrot_trouble(talking, hour)


def twenty_four_hour_time():
    while True:
        try:
            time_now = int(input("What is the current hour (0 - 23)? "))
            if time_now in range(0, 24):
                return time_now
            else:
                print("That is not a valid input, please enter an integer between 0 - 23.")

        except ValueError:
            print("That is not a valid answer, please enter an integer between 0 -23.")


def is_talking():
    while True:
        try:
            talking_now = input("Is the parrot talking (y/n)? ")
            talking_now = talking_now.lower()
            if talking_now == "y":
                return True
            elif talking_now == "n":
                return False
            else:
                print("That is not a valid answer, please enter the character y or n.")
        except ValueError:
            print("That is not a valid answer, please enter the character y or n.")


def parrot_talking(talking, hour):
    if talking is True and hour not in range(7, 21):
        print("You better get out of there, it's going to get messy real soon!!")
    else:
        print("Awesome, you can cruise on by!")


# Take user input
current_time = twenty_four_hour_time()
current_talking = is_talking()

# Confirm the values that were returned as a result of the user's input
print("So the time is {}, and the parrot is talking {}...".format(current_time, current_talking))

# Pass those values in as arguments to our user defined function
parrot_talking(current_talking, current_time)
