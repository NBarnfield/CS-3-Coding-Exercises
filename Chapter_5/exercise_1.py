# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except and
# print an error message and skip to the next number.


total = 0
count = 0

while True:

    try:
        number_to_sum = input("Please enter a numeric value, or the Done to exit: ")

        if number_to_sum == 'Done':
            break

        else:

            number = float(number_to_sum)
            count = count + 1
            total = total + number
            print("The current count is {}, and the current total is {}".format(count, total))

    except ValueError:
        print("Invalid input. Please enter a numeric value, or the string 'Done' to sum values.")


print("The final count is {}, and the total of those number is {}.".format(count, total))
print("The average of those numbers is {}".format(total / count))
