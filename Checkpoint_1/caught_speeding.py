# Program name: caught_speeding.py
# You are driving a little too fast, and a police officer stops you.
# Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1.
# If speed is 81 or more, the result is 2.
# Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
# Make sure all test cases below will pass.
# caught_speeding(speed, is_birthday):


def caught_speeding(speed, is_birthday):

    # If it is your birthday then reduce the speed by 5.
    if is_birthday is True:
        speed = speed - 5
        print("Considering it is your birthday, let's say you were doing {}.".format(speed))
    else:
        pass

    # Calculating the speed, return what ticket the user is liable for.
    if speed <= 60:
        print("Hmmm that's a respectable pace.")
        print("You don't receive a ticket")
        return 0

    elif 61 <= speed <= 80:
        print("You were going a little quick there, Stan.")
        return 1

    elif speed >= 81:
        print("That's too fast!! You could have hurt someone! ")
        return 2

    else:
        print("Valid input was not passed in as arguments. Go to jail, do not pass go and collect $200.")


# Initialise variables
ticket = None
birthday = None
current_speed = None


# Ask the user if it is their birthday.
while True:
    try:
        birthday = input("Is it your birthday today (True/False)? ")
        if birthday == "True":
            birthday = True
            print("Congratulations! Maybe I didn't see you go so quickly there...")
            break

        elif birthday == "False":
            birthday = False
            print("Well, just another day for you then is it...no special treatment then.")
            break

        else:
            print("That is not a valid response. Please enter True or False.")

    except ValueError:
        print("That is not a valid response. Please enter True or False.")


# Ask user for input to tell us what speed they were doing.
while True:
    try:
        current_speed = float(input("What speed do you think you were doing there? "))
        if current_speed > 0:
            print("So you were going {}km an hour...".format(current_speed))
            break

        else:
            print("That isn't what I saw. Please repeat how fast you were going as an integer or float, buddy.")

    except ValueError:
        print("That is not a valid answer. Please enter an integer or float.")


# Given this information, calculate whether to give them a fine or not.
ticket = caught_speeding(current_speed, birthday)

if ticket == 0:
    print("No fine for you today, Sir. Have a 'fine' day.")

elif ticket == 1:
    print("You deserve a small ticket for your crimes to public safety.")

else:
    print("I don't know if I should be perturbed or inspired. Here's a massive fine for being a maniac.")
