# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating
# if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should
# ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we
# are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
# Make sure all test cases below will pass.
# Define function - alarm_clock(day, vacation)

def alarm_clock(day, vacation):
    """Set the alarm for tomorrow based on what day it will be and whether or not you are on vacation."""
    try:
    # Weekdays
        if day in range(1, 6):
            if vacation is True:
                print("You can get up tomorrow at 10:00")
            else:
                print("You can get up at 7:00 tomorrow")

    # Weekends
        if day == 0 or day == 6:
            if vacation is True:
                print("You don't need an alarm! Sleep in as long as you'd like.")
            else:
                print("You are not on vacation but it is a weekend - your alarm is set for 7:00")

    except ValueError:
        print("Invalid arguments given...don't go to sleep - that way you don't need an alarm!")


def true_false(question):
    while True:
        try:
            answer = input(question)
            answer = answer.lower()
            if answer == 'true':
                return True
            elif answer == 'false':
                return False
            else:
                print("{} is an invalid response. Please enter True or False".format(answer))
        except ValueError:
            print("That is not a valid argument. Please enter the string True or False.")


def what_day(day_question):
    while True:
        try:
            day = int(input(day_question))
            if day in range(0, 7):
                return day
            else:
                print("That is not a valid answer. Please enter an integer between 0-6")

        except ValueError:
            print("That is not a valid argument. Please enter an integer between 0-6.")


# Run the code
week = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
holiday = true_false("Are you on holiday? (True/False)")
tomorrow = what_day("What day is it tomorrow 0-6 where {} ? ".format(week))

# Pass in day and vacation in as arguments to see what time the user should get up tomorrow.
alarm_clock(tomorrow, holiday)
