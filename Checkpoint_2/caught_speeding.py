def today_birthday(question):
    while True:
        try:
            user_birthday = input(question)
            if user_birthday in ("true", "True"):
                print("Congratulations! Maybe I didn't see you go so quickly there...")
                return True

            elif user_birthday in ("false", "False"):
                print("Well, just another day for you then is it...no special treatment then.")
                return False

            else:
                print("That is not a valid response. Please enter True or False.")

        except ValueError:
            pass


def what_speed(speed_question):
    while True:
        try:
            speed_confession = float(input(speed_question))
            if speed_confession > 0:
                print("So you were going {}km an hour...".format(speed_confession))
                return speed_confession

            else:
                print("That isn't what I saw. Please repeat how fast you were going as an integer or float, buddy.")

        except ValueError:
            print("That is not a valid answer. Please enter an integer or float.")


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
    print("That is not a valid response. Please enter True or False.")


def fine(ticket_value):
    if ticket_value == 0:
        print("No fine for you today, Sir. Have a 'fine' day.")

    elif ticket_value == 1:
        print("You deserve a small ticket for your crimes to public safety.")

    else:
        print("I don't know if I should be perturbed or inspired. Here's a massive fine for being a maniac.")


birthday = today_birthday("Is it your birthday today (True/False)? ")
current_speed = what_speed("What speed do you think you were doing there? ")
ticket = caught_speeding(current_speed, birthday)
fine(ticket)
