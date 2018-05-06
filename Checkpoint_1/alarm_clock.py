# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating
# if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should
# ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we
# are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
# Make sure all test cases below will pass.
# alarm_clock(day, vacation)


def alarm_clock(tomorrow, on_vacation):
    """Set the alarm for tomorrow based on what day it will be and whether or not you are on vacation."""
    # Weekdays
    if tomorrow in range(1, 6) and on_vacation is True:
        print("You can get up tomorrow at 10:00")
    elif tomorrow in range(1, 6) and on_vacation is False:
        print("You can get up at 7:00 tomorrow")
    # Weekends
    elif tomorrow == 0 and on_vacation is True or tomorrow == 6 and on_vacation is True:
        print("You don't need an alarm! Sleep in as long as you'd like.")
    elif tomorrow == 0 and on_vacation is False or tomorrow == 6 and on_vacation is False:
        print("You are not on vacation but it is a weekend - your alarm is set for 7:00")
    else:
        print("Invalid arguments given...don't go to sleep - that way you don't need an alarm!")


# Collect user input as to what day it will be tomorrow.
while True:
    try:
        week = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
        day = int(input("What day is it tomorrow 0-6 where {} ? ".format(week)))

        if day in range(0, 7):
            break
        else:
            print("That is not a valid answer. Please enter an integer between 0-6")

    except ValueError:
        print("That is not a valid argument. Please enter an integer between 0-6.")


# Collect user input as to whether they are on vacation or not.
while True:
    try:
        vacation = input("Are you on vacation (Yes or No)? ")
        if vacation == 'Yes':
            vacation = True
            break

        elif vacation == "No":
            vacation = False
            break

        else:
            print("That is not a valid answer. Please enter Yes or No.")

    except ValueError:
        print("That is not a valid argument. Please enter the string Yes or No.")

# Pass in day and vacation in as arguments to see what time the user should get up tomorrow.
alarm_clock(day, vacation)
