def drivers_licence(age):
    if age > 16:
        practice_hours = float(input("How many practice hours have you done? "))
        if practice_hours > 200:
            print("Congratulations you qualify for your licence!")
        else:
            print("You haven't done enough practice yet unfortunately - Keep at it!")
    else:
        print("You don't qualify for a licence yet. Try again when you're 16!")


# Ask user for the their age
while True:
    try:
        how_old = float(input("You have just had a birthday and would like to get your licence. How old are you? "))
        break
    except ValueError:
        print("That's not an integer or float! Try again!")

# Pass it in as an argument to the drivers_licence function
drivers_licence(how_old)