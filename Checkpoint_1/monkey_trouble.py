# Problem 4 - PFE Checkpoint 1

# Define a function to ask the user if a monkey is smiling, and loop through until a valid answer is given.
def monkey_smiling():
    "This function prompts the user to answer if the monkey is smiling or not and returns a True/False response"
    monkey_counter = 0
    while monkey_counter == 0:
        monkey = input("Is the monkey smiling (y/n)? ")
        if monkey == 'y':
            print("The monkey appears to be in a good mood...")
            return True
        elif monkey == 'n':
            print("The monkey is not smiling...this could be bad.")
            return False
        else:
            print("That is not a valid option, please try again.")


# Take two variables and then test them to see what the outcome of the event will be.
print("There are two monkeys standing in front of you - Monkey A and Monkey B.")
print("If even one of them shows any sign of unhappiness this mightn't be good.")
print("You look at Monkey A....")
monkey_a = monkey_smiling()
print("You look to Monkey B now...")
monkey_b = monkey_smiling()


# Now that the variables have had True/False returned we can guage what is going to happen.
if monkey_a == True and monkey_b == True:
    print("Everything is going to be great!!")
elif monkey_a == True and monkey_b == False:
    print("Watch out, you might be in for a fight!")
elif monkey_a == False and monkey_b == True:
    print("Watch out, it's about to get rough around here!")
else:
    print("It's going to be a rough day...")