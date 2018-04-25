# Program name: caught_speeding.py
# You are driving a little too fast, and a police officer stops you.
# Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1.
# If speed is 81 or more, the result is 2.
# Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
# Make sure all test cases below will pass.
# caught_speeding(speed, is_birthday):


def caught_speeding(speed, is_birthday):
    ticket = 0
    if speed <= 60 and is_birthday = True:


        if current_speed <= 60:
            print("Hmmm that's a respectable pace.")
            print("You don't receive a ticket")
            ticket = 0

        elif 61 <= current_speed >= 80:
            print("You were going a little quick there, Stan.")
            speed_counter = 1

        elif current_speed >= 81:
            print("That's too fast!! You could have hurt someone! ")
            speed_counter = 1

        else:
            print("That is not a valid answer. Please enter an integer.")

    elif determination == 1:
        print("You receive a small ticket")
    elif determination == 2:
        print("You receive a big ticket")
    else:
        pass


# Ask the user if it is their birthday.
birthday_counter = 0
while birthday_counter == 0:
    birthday = input("Is it your birthday today (True/False)? ")
    try:
        if birthday is True:
            print("Congratulations! Maybe I didn't see you go so quickly there...")
            birthday_counter = 1

        elif birthday is False:
            print("Well, just another day for you then is it...no special treatment then.")
            birthday_counter = 1

        else:
            print("That is not a valid response. Please enter y or n.")

    except ValueError:
        print("That is not a valid response. Please enter y or n.")


# Ask user for input to tell us what speed they were doing.
speed_counter = 0
while speed_counter == 0:
        try:
            current_speed = int(input("What speed do you think you were doing there? "))

            if birthday is True:
                new_speed = current_speed - 5
                speed_counter = 1
            else:
                new_speed = current_speed
                speed_counter = 1

        except ValueError:
            print("That is not a valid answer. Please enter an integer.")

# Given this information, calculate whether to give them a fine or not.
# caught_speeding(new_speed, birthday)
