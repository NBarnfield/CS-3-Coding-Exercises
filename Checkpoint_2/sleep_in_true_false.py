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


def what_day():
    while True:
        current_day = input("Is it a weekday today (True/False)? ")
        if current_day in ("True", "False"):
            return current_day
        else:
            print("That is not a valid response. Please enter True or False.")


def is_holiday():
    while True:
        on_holiday = input("Are you on vacation (True/False)? ")
        if on_holiday in ("True", "False"):
            return on_holiday
        else:
            print("That is not a valid response. Please enter True or False.")


day = what_day()
holiday = is_holiday()
sleep_in(day, holiday)
