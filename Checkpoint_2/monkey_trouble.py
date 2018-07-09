# Program name: monkey_trouble.py
# We have two monkeys, a and b. Accept the input telling if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
# Make sure all test cases below will pass.
# monkey_trouble(monkey a is smiling, monkey b is smiling)


def monkey_smiling():
    """Ask the user whether the monkey is smiling or not"""
    while True:
        try:
            smiling = input("Is the monkey smiling (True/False)? ")
            if smiling == "True":
                return True
            elif smiling == "False":
                return False
            else:
                print("That is not a valid response. Please enter True or False.")
        except ValueError:
            print("That is not a valid response. Please enter True or False.")


def monkey_trouble(monkey_one, monkey_two):
    """Return a True or False to determine if you need to run or hide."""
    if monkey_one == monkey_two:
        print("We are in for some big trouble...brace yourself!!!!")
    else:
        print("We are safe! Let's continue on our journey!!")


# Prompt the user to provide details
print("There are two monkeys standing in front of you...Monkey A and Monkey B...")
print("You look towards Monkey A...")
monkey_a = monkey_smiling()
print("You now turn to Monkey_B...")
monkey_b = monkey_smiling()
print("Let's see...Monkey A - {}, and Monkey B - {}...".format(monkey_a, monkey_b))

# Calculate the appropriate course of action.
monkey_trouble(monkey_a, monkey_b)

