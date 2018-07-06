# When squirrels get together for a party, they like to have cigars.
# A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
# Unless it is the weekend, in which case there is no upper bound on the number of cigars.
# Return True if the party with the given values is successful, or False otherwise.
# Make sure all test cases below will pass.
# cigar_party(cigars, is_weekend)


def cigar_party(cigars, is_weekend):
    """Calculate if you can hold a party based on the number of cigars you have and whether it is a weekend."""
    if is_weekend is True:
        if cigars >= 40:
            print("What a great time you'll have! Party on!")
        else:
            print("Its the weekend! Shame you don't have enough cigars for a party...")
    elif is_weekend is False:
        if 40 >= cigars <= 60:
            print("Yay! We can have a respectable work-night party!!")
        else:
            print("So it's not the weekend, and you don't have the right number of cigars for a gathering...")
            print("What a bummer!")


print("You are a squirrel. You want to have a party, but do you have the right number of cigars, and is it a weekend?")

# Ask user for input to determine the number of cigars they have.
cigar_counter = 0
while cigar_counter == 0:
    try:
        number_of_cigars = int(input("\nHow many cigars do you have? "))
        cigar_counter = 1
    except ValueError:
        print("That's not an integer! No counting half cigars! Try again!")

# Ask user for input to determine whether it is a weekend or not.
weekend_counter = 0
while weekend_counter == 0:
    try:
        weekend = input("Is it the weekend (y/n)? ")
        if weekend == 'y':
            weekend = True
            weekend_counter = 1

        elif weekend == 'n':
            weekend = False
            weekend_counter = 1

        else:
            print("That is not a valid response. Please enter y or n.")

    except ValueError:
        print("Please enter a character.")

# Compute whether you can have a party or not.
cigar_party(number_of_cigars, weekend)





