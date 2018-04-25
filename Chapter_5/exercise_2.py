# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out
# both the maximum and minimum of the numbers instead of the average.

min_number = None
max_number = None
all_numbers = []

while True:

    try:
        user_input = input("\nPlease enter a numeric value, or enter Done to exit: ")

        if user_input == 'Done':
            break

        else:

            number = float(user_input)
            all_numbers.append(number)

            if min_number is None:
                min_number = number

            if max_number is None:
                max_number = number

            if min_number > number:
                min_number = number

            if max_number < number:
                max_number = number

            print("The current list of numbers is {}".format(all_numbers))
            print("The current smallest number is {}, and the current largest is {}".format(min_number, max_number))

    except ValueError:
        print("Invalid input. Please enter a numeric value, or the string 'Done' to compute results.")


print("The final list of numbers is {}".format(all_numbers))
print("The final smallest number is {}, and the final biggest number is {}.".format(min_number, max_number))
