# The function computepay has two parameters that need to be passed in - hours and rates.
# As there is no return value given this is considered a void function.

def computepay(hours, rate):

    if hours > 40:
        pay = 40 * rate
        overtime = (hours - 40) * (rate * 1.5)
        print(("Your wage will be {}.".format(pay + overtime)))
        print(("This is inclusive of ${} of regular salary, and ${} of overtime.".format(pay, overtime)))

    else:
        pay = hours * rate
        print("Your wage will be {}.".format(pay))
        print("You did not qualify for any overtime this week.")


# Setting hours and rate to 0 we can prompt the user with a while loop until acceptable input is given.
hours = 0
rate = 0

while hours == 0:
    try:
        hours = float(input("How many hours did you work? "))
    except:
        print("Error: That is not a numeric value.")

while rate == 0:
    try:
        rate = float(input("What is your hourly rate? "))
    except:
        print("Error: That is not a numeric value.")

# This will then take the arguments passed in and use them to compute the appropriate salary and overtime due.
# The execution of this will print the results to the screen as per the print() statements defined in the function.
computepay(hours, rate)