age = float(input("You have just had a birthday and would like to get your licence. How old are you? "))

if age > 16:

    practice_hours = float(input("How many practice hours have you done? "))

    if practice_hours > 200:

        print("Congratulations you qualify for your licence!")

    else:

        print("You havent done enough practice yet unfortunately - Keep at it!")

else:

    print("You don't qualify for a licence yet. Try again when you're 16!")
