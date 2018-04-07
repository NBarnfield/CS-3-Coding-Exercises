try:
    hours = float(input("How many hours did you work? "))
except:
    print("Error: That is not a numeric value.")
    exit()

try:
    rate = float(input("What is your hourly rate? "))
except:
    print("Error: That is not a numeric value.")
    exit()

if hours > 40:
    pay = 40 * rate
    overtime = (hours - 40) * (rate * 1.5)
    print(("Your wage will be {}.".format(pay + overtime)))
    print(("This is inclusive of ${} of regular salary, and ${} of overtime.".format(pay, overtime)))

else :
    pay = hours * rate
    print("Your wage will be {}.".format(pay))
    print("You did not qualify for any overtime this week.")