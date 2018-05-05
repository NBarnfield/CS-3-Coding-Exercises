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
    """Determine if you need to run or hide."""
    try:
        if monkey_a is True and monkey_b is False:
            print("We are safe! Let's continue on our journey!!")
        elif monkey_a is False and monkey_b is True:
            print("Phew! No trouble here, let's continue!")
        else:
            print("We are in for some big trouble...brace yourself!!!!")

    except ValueError:
        print("I don't know what to make of the situation...better back away slowly...")


# Set variables
Monkey_A = None
Monkey_B = None

# Prompt user for details
print("There are two monkeys standing in front of you...Monkey A and Monkey B...")
print("You look towards Monkey A...")
Monkey_A = monkey_smiling(Monkey_A)
print("You now turn to Monkey_B...")
Monkey_B = monkey_smiling(Monkey_B)

# Confirm that you received a True/False response from the monkey_smiling() function.
print("Let's see...Monkey A - {}, and Monkey B - {}...".format(Monkey_A, Monkey_B))

# Calculate the best course of action.
monkey_trouble(Monkey_A, Monkey_B)
