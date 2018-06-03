# Program name: monkey_trouble.py
# We have two monkeys, a and b. Accept the input telling if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
# Make sure all test cases below will pass.
# monkey_trouble(monkey a is smiling, monkey b is smiling)


def monkey_smiling(monkey):
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


def monkey_trouble(monkey_a, monkey_b):
    """Return a True or False to determine if you need to run or hide."""
    try:
        if monkey_a == monkey_b:
            return True
        else:
            return False

    except ValueError:
        print("I don't know what to make of the situation...better back away slowly...")


def in_trouble(outcome):
    """Based on the results of monkey_trouble() determine the best course of action."""
    try:
        if outcome is True:
            print("We are safe! Let's continue on our journey!!")
        else:
            print("We are in for some big trouble...brace yourself!!!!")

    except ValueError:
        print("I don't know what to make of the situation...better back away slowly...")


# Set Variables
Monkey_A = None
Monkey_B = None
run_or_hide = None

# Prompt the user to provide details
print("There are two monkeys standing in front of you...Monkey A and Monkey B...")
print("You look towards Monkey A...")
Monkey_A = monkey_smiling(Monkey_A)
print("You now turn to Monkey_B...")
Monkey_B = monkey_smiling(Monkey_B)
print("Let's see...Monkey A - {}, and Monkey B - {}...".format(Monkey_A, Monkey_B))

# Calculate the appropriate course of action.
run_or_hide = monkey_trouble(Monkey_A, Monkey_B)
in_trouble(run_or_hide)
